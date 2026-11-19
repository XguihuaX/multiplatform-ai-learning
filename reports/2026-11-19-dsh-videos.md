# 四位作者怎样做大肥鱼与陪伴角色

2026 年 11 月 19 日整理。WorkFisher 的 25:37 长片是从安装工作台讲到鲸鱼娘的完整教程。四条视频各自展示的输入、操作和结果如下。

| 视频与讲义 | 做了哪一步 | 能直接观察到的结果 | 定位原片 |
| --- | --- | --- | --- |
| 南竹0v0 · [推理前缀](../knowledge/dsh/B24.md) | 在 DeepSeek 的思考续写前缀中加入角色口吻，用简单问候触发生成 | 角色口吻进入展示的推理文本。并排示例中，正式回复的猫娘腔弱得多。 | [01:05 提出做法](https://www.bilibili.com/video/BV1Jhxx6ME8t/?t=65) · [02:19 两种输出](https://www.bilibili.com/video/BV1Jhxx6ME8t/?t=139) |
| 凌曦沫呀 · [给角色接手机镜头](../knowledge/dsh/B25.md) | 手机和电脑组网，使用按设备适配的视频通话实现参考 | 角色回应室外画面，屏幕出现组网工具和参考文件。 | [00:25 组网](https://www.bilibili.com/video/BV1RB4u6HE41/?t=25) · [00:39 参考文件](https://www.bilibili.com/video/BV1RB4u6HE41/?t=39) |
| WorkFisher · [DSH 工作区与鲸鱼娘搭建](../knowledge/dsh/B26.md) | 先跑通 DSH 工作区，再用 SurfCore 配置 QQ、声音、桌宠和场景人格卡 | 可从 QQ 来回对话，从桌宠发起语音，并用同一问题比较改卡前后的语气。 | [13:40 手机遥控](https://www.bilibili.com/video/BV1L7xm64EHP/?t=820) · [16:25 鲸鱼娘](https://www.bilibili.com/video/BV1L7xm64EHP/?t=985) · [22:25 人格对照](https://www.bilibili.com/video/BV1L7xm64EHP/?t=1345) |
| Git源宝 · [九个 DSH 插件与用途](../knowledge/dsh/B27.md) | 用插件增加工作台的观测、操作、撤回和审批能力 | 可以分别检查上下文与费用、执行浏览器任务、预览回退或请求确认。 | [00:29 第一个插件](https://www.bilibili.com/video/BV17LWq6cE53/?t=29) · [03:15 九项清单](https://www.bilibili.com/video/BV17LWq6cE53/?t=195) |

## 对 Momo 的含义

同一句“米饭和我谁更重要”，可以检验三个不同问题。把它发到 QQ，能收到回复，检验的是消息通道。固定通道后改人格卡，比较角色措辞，检验的是场景设定。再固定卡片和历史，只改思考续写的前缀，比较用户看到的答案，才能检验前缀有没有额外效果。如果关心角色会如何行动，还需要能触发工具选择的任务。

仅凭“先选工具、最后 ChatAgent 回复”可以识别一种工作流。要判断它所在的系统承担了哪些 harness 职责，还需要追踪是谁持有会话和工作区、注册工具、执行与审批、记录结果并交回模型。四条视频展示的是 DSH 生态与不同作者的角色实践，无法直接用来给 MaiBot 的实现下结论。

阅读依据包括章节、关键帧及画面内文字；技术字段另查 DeepSeek 与 SurfCore 项目文档。两条新增视频没有获得可供逐句核对的完整音轨。四条均未做本机安装或效果复测。
