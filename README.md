# 多平台新知识学习教材

把收藏的视频、文章和项目整理成可以直接阅读、复习，并据此开发新东西的中文教材。按知识类型组织；同一个主题整合多个平台的内容。

**[从教程索引开始学习](knowledge/README.md)**

## DSH 专区

从[DSH：从工作台到陪伴角色](lessons/dsh.md)开始，按步骤读鲸鱼娘搭建、九个插件、手机视觉和推理前缀。查旧笔记可用[DSH 专题资料表](topics/dsh.md)，回看原片可用[四条视频的章节时间戳](reports/2026-11-19-dsh-videos.md)。

## 先读这三章

- **[低延迟 GPT-SoVITS 与语音应用](lessons/speech.md)**：AnifLive-TTS的优化原理、74.6ms指标、真实API、流式PCM、短句队列、插话取消，以及“学习笔记语音讲解器”开发任务书。
- **[网页设计：从需求到可执行设计](lessons/design.md)**：完整设计brief、页面结构、文案、CSS示例、交互验收、可复制Prompt与练习答案。
- **[把需求变成Skill与工作流](lessons/workflows.md)**：工具能力、视频输入、任务拆分、Skill示例、YonWORK迁移接口与技术选型。

其余五章讲解[Agent与记忆](lessons/agents.md)、[科研与训练](lessons/research-training.md)、[角色与动画](lessons/animation.md)、[业务流程](lessons/business.md)、[资源检索](lessons/resources.md)，包含概念、设计案例和自测。具体项目的完整操作细节继续补充。

## 当前内容范围

当前共 54 项素材、9 个分类。首批包括 B 站「学习_llm」23 项和小红书 27 项，后续补入 4 条与 DSH 相关的视频。DSH 分类收录其中 13 条。

2026-11-17 的教学重写为首批素材编写了 8 篇主题正文，重点展开语音、网页设计和工作流。B 站长课程、部分具体插件的操作过程仍待逐章补齐。详见[该轮改写记录](reports/2026-11-17-teaching-rewrite.md)。

小红书27项已有全段ASR检查和关键帧抽样记录。B站23项/26分P媒体已取得，尚有4个分P待转写；原转写进程已退出，当前没有持续运行的转写任务。转写完成、材料读完、教程写完和用户实际掌握分别记录。

## 文档如何供人和 AI 使用

1. 从[知识类型索引](knowledge/README.md)选择章节，先理解原理与贯穿例子。
2. 用章内任务书或操作步骤做最小作品；遇到具体版本问题，沿文末官方链接核对。
3. AI读取时先读主题正文，再按素材ID追溯来源，区分原视频内容、官方补充与教学设计。
4. 来源页保留实际阅读范围；截图中的[X27](knowledge/design/X27.md)和[B07](knowledge/speech/B07.md)、[B08](knowledge/workflows/B08.md)已直接内嵌详细教程，处理记录折叠在文末。

## 仓库维护

- `lessons/`：手写教学正文，不被索引生成器覆盖。
- `knowledge/`：主阅读索引和唯一素材页，按知识类型归档。
- `sources/catalog.json`：稳定ID、原始链接、阅读证据、素材页路径。
- `sources/categories.json`：教程路径、学习目标、章节深度。
- `topics/`：跨来源专题记录；`reports/`：处理进度与核查记录。

更新目录或教程后运行 `python3 scripts/build_index.py`。正文应有机制解释、具体步骤、完整实例、应用方向及验证方法；来源与阅读日志放在文末。媒体、登录信息、签名链接和原始长篇转写只留本地缓存，不提交。

已配置每日B站学习汇总，见文末每日入口。项目历史与发现阶段方案见[更新记录](CHANGELOG.md)和[筛选试运行方案](筛选试运行方案.md)。

## 每日B站学习汇总

每天北京时间20:00检查「学习_llm」收藏夹，详见[每日入口](reports/daily/README.md)。[2026-11-21首轮报告](reports/daily/2026-11-21-bilibili.md)包含36项时间清单与新增内容。
