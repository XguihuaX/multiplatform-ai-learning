#!/usr/bin/env python3
"""Build source notes and a category index from the reviewed catalog."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / 'sources/catalog.json').read_text())
assert len({x['id'] for x in items}) == len(items), 'duplicate ID'
assert len({x['source_id'] for x in items}) == len(items), 'duplicate source'
lines = ['# 收藏学习索引', '', '阅读日期：2026-11-16。范围为B站学习_llm收藏夹，以及小红书最新收藏至指定截止笔记（含该条）。', '',
         '状态：小红书27条已完成全段ASR检查与关键帧抽样的首轮整理；B站23项共26分P媒体已取得，完整内容学习进行中。每条笔记注明阅读范围。', '',
         '| ID | 标题与笔记 | 分类 | 实际阅读范围 |', '| --- | --- | --- | --- |']
for x in items:
    path = ROOT / x['note_path']
    path.parent.mkdir(parents=True, exist_ok=True)
    refs = '\n'.join('- ' + u for u in x['references']) or '- 暂无已定位的原始项目链接。'
    path.write_text(f"# {x['id']} · {x['title']}\n\n"
        f"- 平台：{x['platform']}\n- 来源：[原始内容]({x['url']})\n- 稳定ID：{x['source_id']}\n"
        f"- 分类：{x['category']}\n- 阅读日期：{x['reviewed_at']}\n- 阅读范围：{x['coverage']}\n"
        f"- 学习状态：{x.get('learning_status', '已完成全段ASR与关键帧的本轮整理' if x.get('audio_notes') else '待补完整音频阅读')}\n"
        f"- 画面覆盖：{'关键帧抽样，未连续逐帧观看' if x.get('visual_observations') else '未完成系统画面阅读'}\n- 实机复现：未进行\n\n"
        f"## 已提取内容\n\n{x['summary']}\n\n## 核查与阅读缺口\n\n{x['verification']}\n\n" +
        (f"## 视频画面观察\n\n{x['visual_observations']}\n\n" if x.get('visual_observations') else '') +
        (f"## 音频内容学习\n\n{x['audio_notes']}\n\n" if x.get('audio_notes') else '') +
        f"## 下一步学习或练习\n\n{x['next_action']}\n\n## 补充来源\n\n{refs}\n", encoding='utf-8')
    lines.append(f"| {x['id']} | [{x['title'].replace('|','／')}](../{x['note_path']}) | {x['category']} | {x['coverage']} |")
lines += ['', '## 分类数量', '']
for key, count in Counter(x['category'] for x in items).items():
    lines.append(f'- {key}：{count}条')
(ROOT / 'sources/README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'Generated {len(items)} notes; platforms: {dict(Counter(x["platform"] for x in items))}')

# Main navigation is organized by knowledge type, with platform retained as metadata.
categories = json.loads((ROOT / 'sources/categories.json').read_text())
nav = ['# 知识分类索引', '', '按学习内容分类；平台仅作为来源字段。每条笔记归入一个主类，跨类联系由专题串联。', '', '| 知识类型 | 条目数 | 内容范围 | 专题总结 |', '| --- | ---: | --- | --- |']
for cat in categories:
    group = [x for x in items if x['category'] == cat['name']]
    nav.append(f"| [{cat['name']}](#{cat['slug']}) | {len(group)} | {cat['description']} | [阅读专题](../topics/{cat['topic']}) |")
for cat in categories:
    nav += ['', f'<a id="{cat["slug"]}"></a>', f'## {cat["name"]}', '', '| 笔记 | 阅读范围 |', '| --- | --- |']
    for x in items:
        if x['category'] == cat['name']:
            nav.append(f"| [{x['title'].replace('|','／')}]({x['note_path'].removeprefix('knowledge/')}) | {x['coverage']} |")
(ROOT / 'knowledge/README.md').write_text('\n'.join(nav)+'\n')
(ROOT / 'sources/README.md').write_text('# 素材登记\n\n日常阅读请从[知识分类索引](../knowledge/README.md)进入。\n\ncatalog.json保存50项素材的稳定ID、原链接、主分类、笔记路径、证据范围及核查记录。平台保留为溯源字段，不再作为笔记目录。\n')
