# 视频学习 Skill / MCP 初步调研

日期：2026-11-11。依据官方文档与项目 README；未安装、未做视频实测。下列能力为项目文档声明，选型顺序为本项目的初步判断。

## 结论

视频学习需要结合带时间戳的语音转写、画面读取和关键片段复查。无字幕可使用 ASR；屏幕操作、代码、图表和无旁白演示需要视觉分析。Skill 编排学习流程，MCP 提供可调用工具，具体理解能力仍取决于模型与输入覆盖。

## 候选

| 项目 | 形式与能力 | 本项目用途 / 待验证项 |
| --- | --- | --- |
| [qinghui316/video-understander](https://github.com/qinghui316/video-understander) | Skill；声明支持 B 站、小红书、抖音、YouTube、本地文件；字幕或 SiliconFlow / 豆包 ASR；场景感知抽帧、时间戳及 Markdown 归档 | 优先测试国内平台获取、中文术语、关键操作覆盖；无字幕路径需要云端 ASR 配置 |
| [Paldom/video-to-skill](https://github.com/Paldom/video-to-skill) | video-notes、video-transcribe、video-keyframes 三个 Skill；字幕回退本地 Whisper；场景截图、可选 OCR、带截图和时间戳的笔记 | 适合课程及知识笔记；优先测试 YouTube / 本地文件；依赖 ffmpeg、yt-dlp，转写另需 whisper.cpp 或 faster-whisper |
| [KitDevUA/video-vision-mcp](https://github.com/KitDevUA/video-vision-mcp) | MCP；本地抽帧和 whisper.cpp、云 ASR、Gemini 三条后端路线；支持指定时间点取帧 | 适合按需补看、局部精读；输入是本地文件或直接视频 URL，平台页面获取需另处理 |
| [oxbshw/watch-skill](https://github.com/oxbshw/watch-skill) | Skill / MCP / CLI；视频处理、检索、OCR、本地转写等 | 适合后续可检索视频库；standard 包含抽帧、检索及 MCP，OCR 与 Whisper 为额外依赖；初期不必引入整个 DeepWatch 工作区 |
| [Gemini 视频理解 API](https://ai.google.dev/gemini-api/docs/video-understanding) | 原生视频输入，可上传文件、使用公开 YouTube URL，按时间戳提问 | 复杂动作和时序片段的候选后端；需要 API 配置及实际费用评估，本身不是 Skill 或 MCP |

## 建议工作流

获取视频 → 获取字幕或 ASR 转写 → 粗览全片与场景抽帧 → 对齐语言和画面 → 对关键操作、密集代码、图表及疑点局部补帧或提交短视频片段 → 生成有时间戳和关键截图的学习笔记。

局部精读应覆盖操作前、操作中和操作后；OCR 用于检索和辅助读取，界面关系、图表和演示结果仍需读图。拿到视频后才能判断获取、转写、视觉分析和总结各环节的实际表现。平台支持声明不等于每个链接都可下载。

本地抽帧和本地转写只说明这些处理步骤在本机；若随后把截图交给云端模型，视觉分析仍然使用云服务。

## 建议验证

先测试 video-understander 的跨平台流程，以 video-vision-mcp 作为按时间点精读的备选。用四类短素材检验：无字幕中文讲解、代码/界面操作、图表或架构讲解、无旁白演示。

记录：获取是否成功、语音关键术语是否正确、是否捕捉只出现在画面中的信息、操作顺序是否正确、是否能返回对应时间戳、耗时与调用成本。将“仅转写总结”和“转写加视觉总结”对照，确认视觉分析带来的实际增益。
