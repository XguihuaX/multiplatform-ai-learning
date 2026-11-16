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
         '状态：小红书27条已完成全段ASR检查与关键帧抽样的首轮整理；B站23条仍为正文/文档整理，完整媒体待补。每条笔记注明阅读范围。', '',
         '| ID | 标题与笔记 | 分类 | 实际阅读范围 |', '| --- | --- | --- | --- |']
for x in items:
    path = ROOT / 'sources' / x['platform'] / (x['id'] + '.md')
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
    lines.append(f"| {x['id']} | [{x['title'].replace('|','／')}]({x['platform']}/{x['id']}.md) | {x['category']} | {x['coverage']} |")
lines += ['', '## 分类数量', '']
for key, count in Counter(x['category'] for x in items).items():
    lines.append(f'- {key}：{count}条')
(ROOT / 'sources/README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'Generated {len(items)} notes; platforms: {dict(Counter(x["platform"] for x in items))}')
