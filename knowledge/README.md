# 从这里开始学习

教程按知识类型组织。先读下面的学习正文，再按需展开素材记录；每章包含概念解释、实例和自测答案。

想搭建大肥鱼，可先读 [DSH 教程](../lessons/dsh.md)，再按问题查[插件与角色资料](../topics/dsh.md)。语音、网页设计、Skill 与工作流也有独立的实践章节。

| 学习正文 | 读完可以做什么 | 本章深度 |
| --- | --- | --- |
| [DSH：从工作台到陪伴角色](../lessons/dsh.md) | 搭建鲸鱼娘，区分场景人格与推理前缀，定位视觉和用量问题 | 搭建教程、插件清单与对照练习 |
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

共66项：B站39项、小红书27项。下列阅读范围是素材处理记录，不等同于对应完整课程已经写成讲义。

<details>
<summary>DSH · 20项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B01 · DSH吞噬进化！AI工作台搭建焚决！](dsh/B01.md) | 页面简介 |
| [B02 · 一键节省大肥鱼40% token花费的dsh插件！](dsh/B02.md) | 页面简介＋官方README |
| [B05 · 动态记忆？嵌套学习？我解决了大肥鱼的记忆死亡难题](dsh/B05.md) | 页面简介 |
| [B06 · 自主意图？自我意识？让大肥鱼真正的活下去……](dsh/B06.md) | 页面简介 |
| [B12 · 更强的设计能力！DSH Oil UI插件来了！](dsh/B12.md) | 页面简介＋官方README |
| [B13 · Deepseek Harness实时自压缩插件Live-Compact](dsh/B13.md) | 页面详细简介 |
| [B15 · DSH直连Blender插件与视觉反馈](dsh/B15.md) | 页面详细简介＋官方README |
| [B18 · 一个有“自主意识”的DeepSeek插件：SurfCore](dsh/B18.md) | 页面详细简介＋官方README |
| [B20 · 超便宜快速的DSH一起看插件](dsh/B20.md) | 页面详细简介＋官方README |
| [B24 · 不改提示词也能去人机味？为什么说大肥鱼的尽头是猫娘……](dsh/B24.md) | 页面简介、约00:07至03:06分段抽看画面与内嵌字幕、官方接口文档 |
| [B25 · 给她一双眼睛，让她看清世界！【B站AI创造公开赛】](dsh/B25.md) | 视频画面、内嵌文字、系列目录与配套资料列表 |
| [B26 · DeepSeek Harness 大肥鱼终极教程：新手进阶/插件生态/界面美化/手机端互通/全能鲸鱼娘【附完整文档】](dsh/B26.md) | 全片章节、跨全时长预览帧与内嵌字幕抽样、作者置顶更正、SurfCore 文档 |
| [B27 · 【小众好用】有哪些DeepSeek好用的必装插件？如何榨干 DeepSeek Harness所有性能？DSH插件安装指南！](dsh/B27.md) | 全片章节、跨全时长预览帧与内嵌字幕抽样、片尾九项清单 |
| [B29 · 大肥鱼看视频不用逐帧硬啃了！DeepSeekHarness看片Skill配置教程](dsh/B29.md) | 简介＋全段本地ASR审读＋全时长分布抽帧与关键帧原尺寸核对＋官方Skill文档 |
| [B30 · 🐳鲸鲸震撼，大肥鱼边逛街边给你发自拍？！🐳一条视频教会你 DSH插件分享](dsh/B30.md) | 收藏列表及简介；音视频正文待阅读 |
| [B32 · 🐳让你家大肥鱼发自拍给你的插件？！一条视频讲清楚！！🐳](dsh/B32.md) | 收藏列表及简介；音视频正文待阅读 |
| [B34 · 给大肥鱼装五官：看视频刷B站，一期搭完](dsh/B34.md) | 全段本地ASR审读、时间轴关键帧、原尺寸能力表；补读三个官方项目README相关章节 |
| [B37 · 用尽可能更低的上下文水位，去保持尽可能高的模型注意力——DSH Live Compact的设计初衷及实现方案详解～](dsh/B37.md) | 收藏列表及简介；音视频正文待阅读 |
| [B38 · 想要给她完整的一生？试试这招！](dsh/B38.md) | 已读取收藏列表与简介；音视频待阅读 |
| [B39 · 想给她完整的一生？视频通话功能正式预告！【B站AI创造公开赛】](dsh/B39.md) | 已读取收藏列表与简介；音视频待阅读 |

</details>

<details>
<summary>工具与工作流 · 5项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B08 · 别随便让AI替你选技术栈！](workflows/B08.md) | 页面简介＋完整本地ASR审读 |
| [X14 · 分享几款我们团队在用的AI工具](workflows/X14.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X17 · 释放双手，让AI全权接管电脑](workflows/X17.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X18 · Harness深度解析（上）：从工作几秒到连续数周](workflows/X18.md) | 完整正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [X20 · Codex使用必做动作](workflows/X20.md) | 正文标签＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |

</details>

<details>
<summary>Agent与记忆 · 3项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B22 · 致B站所有AI的第一课：记忆、人格、自进化、多agent协作](agents/B22.md) | 页面详细简介 |
| [X23 · 文科生如何成为Grok负责人？](agents/X23.md) | 正文标签＋平台AI评论片段＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [B31 · 一镜到底，让我的AI带你游览她的小镇——SoullinkLife直播功能实机演示【B站AI创造公开赛】](agents/B31.md) | 收藏列表及简介；音视频正文待阅读 |

</details>

<details>
<summary>科研与模型训练 · 9项素材</summary>

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
| [B33 · JoVox：轻量性生成高保真 3D 体素， MACaQ：快、小、好的量化模型](research-training/B33.md) | 全段本地ASR审读、覆盖时间轴关键帧拼图、JoVox与MACaQ官方README |

</details>

<details>
<summary>设计与内容制作 · 4项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
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
<summary>3D与动画 · 14项素材</summary>

| 素材记录 | 实际阅读范围 |
| --- | --- |
| [B03 · Blender卡提希娅3D角色建模教程](animation/B03.md) | 页面元信息 |
| [B04 · 一键制作MMD真的实现了！震惊瘫坐！](animation/B04.md) | 页面简介 |
| [B09 · 开源：全AI模型生成工作流](animation/B09.md) | 页面元信息 |
| [B10 · HairDeck单张生成风格化发片整合包](animation/B10.md) | 页面详细简介与原项目链接 |
| [B11 · 仅需24MB内存！轻量化的ADRY实时AI动画方案](animation/B11.md) | 页面简介 |
| [B16 · 如何丝滑地解决AI视频的衔接问题](animation/B16.md) | 页面简介 |
| [B17 · HAST-SEC：0.8B让3D角色听懂中文并实时行动](animation/B17.md) | 页面简介 |
| [B19 · MMD模型物理优化2.0：RGBA与史莱姆物理](animation/B19.md) | 页面简介与插件链接 |
| [B23 · 自然语言驱动的LumenACT表情系统](animation/B23.md) | 页面简介＋一个演示画面 |
| [X02 · 立绘转可动形象，一张插画变直播分身](animation/X02.md) | 正文＋本地视频关键帧抽样＋完整音频本地ASR审读 |
| [X15 · 又一个参数化工具](animation/X15.md) | 正文＋本地视频关键帧抽样＋全段本地ASR审读/音轨检查 |
| [B28 · Blender 角色接触变形插件！Fleshy 实现逼真皮肤挤压肉感效果](animation/B28.md) | 简介＋全段本地ASR审读＋全时长分布抽帧与关键帧原尺寸核对 |
| [B35 · 用AI做日系2D动画，日常番的感觉是怎么做出来的？](animation/B35.md) | 收藏列表及简介；关联官方README与七步流程已阅读；视频音轨及画面待阅读 |
| [B36 · 【开源】震撼首推：高拟真动作控制模型发布！【B站AI创造公开赛】](animation/B36.md) | 收藏列表及简介；音视频正文待阅读 |

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
