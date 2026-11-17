# 从这里开始学习

教程按知识类型组织。先读下面的学习正文，再按需展开素材记录；每章包含概念解释、实例和自测答案。

**本轮重点详解：低延迟语音、网页设计、Skill与工作流。** 其余章节提供跨素材的基础讲解与设计案例；尚未展开的具体项目操作与B站长课程，不计作已完成教程。

| 学习正文 | 读完可以做什么 | 本章深度 |
| --- | --- | --- |
| [把需求变成Skill与工作流](../lessons/workflows.md) | 写出有输入、输出和恢复路径的Skill；设计YonWORK工具接口 | 完整流程示例 |
| [Agent任务续接与长期记忆](../lessons/agents.md) | 区分上下文、任务状态与知识；设计可恢复任务 | 原理与设计案例 |
| [训练方法、Infra与最小实验](../lessons/research-training.md) | 区分微调维度，设计有对照的蒸馏/检索实验 | 概念与实验设计 |
| [网页设计：从需求到可执行设计](../lessons/design.md) | 写设计brief、信息结构、文案、样式和验收条件 | 详细教程与可复制Prompt |
| [低延迟GPT-SoVITS与语音应用](../lessons/speech.md) | 读懂AnifLive优化，接API、PCM、分句队列和打断 | 详细技术教程与开发任务书 |
| [从角色图到会说话的形象](../lessons/animation.md) | 理解制作管线，设计音量嘴型与播放同步 | 管线讲解与算法示例 |
| [把业务经验变成AI流程](../lessons/business.md) | 按明确口径算订单贡献，设计SOP与业务Skill | 完整业务算例 |
| [从收藏找到可复用项目资料](../lessons/resources.md) | 确认项目身份、接口和版本，保留可检索知识 | 方法讲解 |

## 推荐阅读顺序

想做新东西：先读语音章节，按固定句子WAV、流式播放、LLM短句队列逐步实现；再读动画章节给角色接嘴型。想搭学习系统：先读工作流，再读Agent与记忆。想做展示页面：直接读网页设计。

## 收藏素材与原始出处

共50项：B站23项、小红书27项。下列阅读范围是素材处理记录，不等同于对应完整课程已经写成讲义。

<details>
<summary>工具与工作流 · 9项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B01 · DSH吞噬进化！AI工作台搭建焚决！](workflows/B01.md) | 页面简介 |
| [B02 · 一键节省大肥鱼40% token花费的dsh插件！](workflows/B02.md) | 页面简介＋官方README |
| [B08 · 别随便让AI替你选技术栈！](workflows/B08.md) | 页面简介＋完整本地ASR审读 |
| [B13 · Deepseek Harness实时自压缩插件Live-Compact](workflows/B13.md) | 页面详细简介 |
| [B20 · 超便宜快速的DSH一起看插件](workflows/B20.md) | 页面详细简介＋官方README |
| [X14 · 分享几款我们团队在用的AI工具](workflows/X14.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X17 · 释放双手，让AI全权接管电脑](workflows/X17.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X18 · Harness深度解析（上）：从工作几秒到连续数周](workflows/X18.md) | 完整正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X20 · Codex使用必做动作](workflows/X20.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>Agent与记忆 · 5项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B05 · 动态记忆？嵌套学习？我解决了大肥鱼的记忆死亡难题](agents/B05.md) | 页面简介 |
| [B06 · 自主意图？自我意识？让大肥鱼真正的活下去……](agents/B06.md) | 页面简介 |
| [B18 · 一个有“自主意识”的DeepSeek插件：SurfCore](agents/B18.md) | 页面详细简介＋官方README |
| [B22 · 致B站所有AI的第一课：记忆、人格、自进化、多agent协作](agents/B22.md) | 页面详细简介 |
| [X23 · 文科生如何成为Grok负责人？](agents/X23.md) | 正文标签＋平台AI评论片段＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>科研与模型训练 · 8项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [X03 · 谷歌100%全自动科研碾压人类最佳模型!!!](research-training/X03.md) | 正文标签＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X05 · 大模型微调的10种方法](research-training/X05.md) | 正文＋完整可见信息图＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X06 · 面试官：都是7B生成推理链来蒸馏，为啥DeepSeek-R1效果不同？](research-training/X06.md) | 正文＋开场画面＋官方文档补充＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X07 · AI Infra知识体系梳理](research-training/X07.md) | 正文＋开场画面＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X08 · 我用AI几天写完ICML论文·完整步骤](research-training/X08.md) | 完整正文＋本地视频关键帧抽样＋完整英文ASR审读与中文归纳 |
| [X10 · ICML一起写AI顶会论文：大模型记忆](research-training/X10.md) | 完整正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X12 · DeepSeek-R1蒸馏Qwen-7B强在哪？](research-training/X12.md) | 正文标签＋官方文档补充＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X19 · 谷歌全自动科研AI：ScientistTwo](research-training/X19.md) | 正文＋原论文摘要与项目页＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>设计与内容制作 · 5项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B12 · 更强的设计能力！DSH Oil UI插件来了！](design/B12.md) | 页面简介＋官方README |
| [X09 · 10秒出一张4K图：MiniMax H3-Image](design/X09.md) | 正文＋官方README＋本地视频关键帧抽样＋全段ASR审读（X09无可用技术口播） |
| [X22 · 好看哭了的神级网页Skill](design/X22.md) | 正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X26 · PPT-Master：答辩、汇报、演讲](design/X26.md) | 正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X27 · 这个神级Skill，做的网页超好看！](design/X27.md) | 完整正文＋演示画面＋官方README＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>语音合成 · 3项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B07 · 我把GPT-SoVITS的首音延迟做到了74.6ms！AnifLive-TTS](speech/B07.md) | 页面简介＋全段ASR空结果检查＋8帧画面抽样＋官方README/API/性能与Mac安装文档 |
| [B14 · BreezeTTS2：克隆、声音设计、情绪与多角色配音](speech/B14.md) | 页面详细简介＋官方README |
| [B21 · Breeze TTS2 V3整合升级：8G显存与2.3倍速度](speech/B21.md) | 页面简介＋全段本地ASR审读＋8帧画面抽样＋上游README |

</details>

<details>
<summary>3D与动画 · 12项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B03 · Blender卡提希娅3D角色建模教程](animation/B03.md) | 页面元信息 |
| [B04 · 一键制作MMD真的实现了！震惊瘫坐！](animation/B04.md) | 页面简介 |
| [B09 · 开源：全AI模型生成工作流](animation/B09.md) | 页面元信息 |
| [B10 · HairDeck单张生成风格化发片整合包](animation/B10.md) | 页面详细简介与原项目链接 |
| [B11 · 仅需24MB内存！轻量化的ADRY实时AI动画方案](animation/B11.md) | 页面简介 |
| [B15 · DSH直连Blender插件与视觉反馈](animation/B15.md) | 页面详细简介＋官方README |
| [B16 · 如何丝滑地解决AI视频的衔接问题](animation/B16.md) | 页面简介 |
| [B17 · HAST-SEC：0.8B让3D角色听懂中文并实时行动](animation/B17.md) | 页面简介 |
| [B19 · MMD模型物理优化2.0：RGBA与史莱姆物理](animation/B19.md) | 页面简介与插件链接 |
| [B23 · 自然语言驱动的LumenACT表情系统](animation/B23.md) | 页面简介＋一个演示画面 |
| [X02 · 立绘转可动形象，一张插画变直播分身](animation/X02.md) | 正文＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X15 · 又一个参数化工具](animation/X15.md) | 正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>商业与组织 · 7项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [X01 · 一个人在出租屋里是干不成跨境电商的](business/X01.md) | 正文标签＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X04 · 头等舱采访：AI最先淘汰中层？](business/X04.md) | 正文＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X11 · 我家4个工位，3个是AI员工](business/X11.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X13 · Codex接管跨境投放效果怎么样](business/X13.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X21 · 靠AI不上班如何月入2万？](business/X21.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X24 · 清华应届生5千元起步，自研智能体做跨境电商，半年营收700万](business/X24.md) | 正文＋嘉宾评论＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X25 · 一人公司，为啥晒收入？我在国外找到了答案](business/X25.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>资源与检索 · 1项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [X16 · 第30期：让虚拟资料卖家集体失业的网站](resources/X16.md) | 正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>
