# DSH 专题资料表

初次搭建请从[DSH 学习正文](../lessons/dsh.md)开始。下表将四条视频与此前收藏的九条笔记按用途串起来。每条素材保留独立编号及阅读范围。

| 想了解什么 | 资料 | 可以据此判断什么 |
| --- | --- | --- |
| 工作台与角色搭建 | [B26 鲸鱼娘完整教学](../knowledge/dsh/B26.md) · [B01 工作台整合思路](../knowledge/dsh/B01.md) | B26 有章节和操作画面，可定位 QQ、语音和人格配置；B01 主要说明工作台整合方向。 |
| 插件与成本 | [B27 九个插件](../knowledge/dsh/B27.md) · [B02 dsh-ops](../knowledge/dsh/B02.md) · [B13 Live-Compact](../knowledge/dsh/B13.md) | B27 能区分上下文和账单读数，B02 讨论缩短工具输出，B13 提出增量压缩。节省比例、缓存命中率需要同任务对照。 |
| 角色设定与持续行为 | [B24 推理前缀](../knowledge/dsh/B24.md) · [B18 SurfCore](../knowledge/dsh/B18.md) · [B05 记忆](../knowledge/dsh/B05.md) · [B06 主动行为](../knowledge/dsh/B06.md) | B24 可看生成样例，B18 有渠道、身份和记忆的项目资料。B05、B06 目前只读到简介，内部实现仍待核实。 |
| 画面怎样进入对话 | [B25 手机视频通话](../knowledge/dsh/B25.md) · [B20 一起看视频](../knowledge/dsh/B20.md) | B25 展示角色回应手机所拍环境；B20 用播放器时间定位视频字幕和分镜，两者输入不同。 |
| 用视觉反馈验收作品 | [B12 Oil UI](../knowledge/dsh/B12.md) · [B15 Blender 直连](../knowledge/dsh/B15.md) | 网页设计可比较候选首屏和截图。Blender 场景可在修改后从多个视角检查实际渲染。 |

通用运行机制可延伸阅读[上下文、规则与外部记忆](../knowledge/workflows/X18.md)。要比较不同 Agent 的实现，可记录哪一层保管会话、选择工具、执行动作，以及如何把结果交回模型；这些问题也适用于分析 Momo 或 MaiBot。

2026-11-21：[video-watch-plus视频阅读说明](../lessons/video-watch-plus.md)，补充预分析、取帧与浏览器协作。

2026-11-22：[DSH感知与操作工具详解](../lessons/dsh-perception-tools.md)，对应B34；从分镜/ASR、实时陪看到Windows操作，附依赖、参数与最小验证案例。
