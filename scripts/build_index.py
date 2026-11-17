#!/usr/bin/env python3
"""Build teaching-first navigation and source appendices; never overwrite lesson inputs."""
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = json.loads((ROOT / 'sources/catalog.json').read_text())
categories = json.loads((ROOT / 'sources/categories.json').read_text())
assert len({x['id'] for x in items}) == len(items), 'duplicate ID'
assert len({x['source_id'] for x in items}) == len(items), 'duplicate source'
assert len({x['note_path'] for x in items}) == len(items), 'duplicate note path'
by_name = {c['name']: c for c in categories}

def relative(target, parent):
    return Path(os.path.relpath(ROOT / target, parent)).as_posix()

for x in items:
    path = ROOT / x['note_path']
    path.parent.mkdir(parents=True, exist_ok=True)
    cat = by_name[x['category']]
    lesson = ROOT / cat['lesson_path']
    assert lesson.is_file(), f'missing lesson: {lesson}'
    if x.get('lesson_body_path'):
        body = (ROOT / x['lesson_body_path']).read_text().rstrip() + '\n\n'
    else:
        body = (f"# {x['id']} · {x['title']}\n\n"
                f"**学习正文：[阅读《{cat['lesson_title']}》]({relative(cat['lesson_path'], path.parent)})**\n\n"
                f"本页保留这条素材的要点和来源；完整概念、案例与练习在上面的主题教程。\n\n"
                f"## 本条素材提供的内容\n\n{x['summary']}\n\n")
    refs = '\n'.join('- ' + u for u in x['references']) or '- 暂无已定位的原始项目链接。'
    appendix = (f"<details>\n<summary>{x['id']} 来源、阅读记录与待补内容</summary>\n\n"
        f"- 原标题：{x['title']}\n- 平台：{x['platform']}\n- 来源：[原始内容]({x['url']})\n"
        f"- 稳定ID：{x['source_id']}\n- 分类：{x['category']}\n- 阅读日期：{x['reviewed_at']}\n"
        f"- 阅读范围：{x['coverage']}\n"
        f"- 素材处理状态：{x.get('learning_status', '已整理现有资料；参见具体阅读范围')}\n"
        f"- 画面覆盖：{'关键帧抽样，未连续逐帧观看' if x.get('visual_observations') else '未完成系统画面阅读'}\n"
        f"- 实机复现：未进行\n\n### 核查记录\n\n{x['verification']}\n\n" +
        (f"### 画面记录\n\n{x['visual_observations']}\n\n" if x.get('visual_observations') else '') +
        (f"### 音频记录\n\n{x['audio_notes']}\n\n" if x.get('audio_notes') else '') +
        f"### 待补工作\n\n{x['next_action']}\n\n### 原始项目与补充来源\n\n{refs}\n\n</details>\n")
    path.write_text(body + appendix, encoding='utf-8')

nav = ['# 从这里开始学习', '',
       '教程按知识类型组织。先读下面的学习正文，再按需展开素材记录；每章包含概念解释、实例和自测答案。', '',
       '**本轮重点详解：低延迟语音、网页设计、Skill与工作流。** 其余章节提供跨素材的基础讲解与设计案例；尚未展开的具体项目操作与B站长课程，不计作已完成教程。', '',
       '| 学习正文 | 读完可以做什么 | 本章深度 |', '| --- | --- | --- |']
for c in categories:
    nav.append(f"| [{c['lesson_title']}](../{c['lesson_path']}) | {c['learning_outcome']} | {c['lesson_depth']} |")
nav += ['', '## 推荐阅读顺序', '',
        '想做新东西：先读语音章节，按固定句子WAV、流式播放、LLM短句队列逐步实现；再读动画章节给角色接嘴型。想搭学习系统：先读工作流，再读Agent与记忆。想做展示页面：直接读网页设计。', '',
        '## 收藏素材与原始出处', '',
        '共50项：B站23项、小红书27项。下列阅读范围是素材处理记录，不等同于对应完整课程已经写成讲义。', '']
for c in categories:
    group = [x for x in items if x['category'] == c['name']]
    nav += [f'<details>\n<summary>{c["name"]} · {len(group)}项素材</summary>', '',
            '| 素材记录 | 实际阅读范围 |', '| --- | --- |']
    for x in group:
        nav.append(f"| [{x['id']} · {x['title'].replace('|','／')}]({x['note_path'].removeprefix('knowledge/')}) | {x['coverage']} |")
    nav += ['', '</details>', '']
(ROOT / 'knowledge/README.md').write_text('\n'.join(nav).rstrip() + '\n')
(ROOT / 'sources/README.md').write_text('# 素材登记\n\n学习请从[教程索引](../knowledge/README.md)进入。\n\n'
    'catalog.json保存50项素材的稳定ID、原链接、主分类、笔记路径和阅读证据。categories.json指定各类的手写教程路径、学习目标与深度。\n\n'
    'lessons目录保存手写正文，生成器只读取它。指定lesson_body_path的素材页会内嵌对应教程，其余素材页链接到教程。媒体、原始长篇转写与签名链接留在本地缓存。\n')
print(f'Generated {len(items)} source pages and {len(categories)} lesson links; platforms: {dict(Counter(x["platform"] for x in items))}')
