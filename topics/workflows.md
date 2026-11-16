# 工作台与工具闭环

## 已读内容给出的主线

先用需求决定技术选型（B08），再补齐执行工具（B02）、上下文管理（B13）、视觉反馈（B12/B15/B20）。X18给出了理解这些模块的课程概念表。B01提供工作台整合方向，具体配置尚需视频。

| 模块 | 解决的问题 | 可迁移做法 | 当前证据 |
| --- | --- | --- | --- |
| architect | AI默认堆复杂技术栈 | 写清约束，比较简单方案与替代方案 | [nagi README](https://github.com/nagi-studio/skills) |
| dsh-ops | 工具输出过长与重复调用 | 精简输出、结构化结果、批处理 | [官方README](https://github.com/T-Auto/dsh-ops) |
| Live-Compact | 长任务上下文集中压缩 | 增量压缩是候选方向，须检查事实保留 | B13简介；源码待补 |
| Oil UI | 一次生成后缺少设计比较与验收 | 多方向首屏→选择→实现→截图检查 | [官方README](https://github.com/oil-oil/dsh-oil-ui) |
| Blender直连 | 修改后没有及时看到结果 | 观察→修改→渲染/截图→验收 | [官方README](https://github.com/sixtysevenlf/dsh-blender-plugin) |
| 一起看 | 模型不知当前播放到哪里 | 播放时间对齐字幕与分镜，局部放大 | [官方README](https://github.com/SAOS-3624/dsh-watch-together) |

## 对学习库的应用

每条视频先记录素材ID、分P、时长和获取状态，再建立字幕与画面的共同时间轴。课程操作步骤需要同时看到命令、界面状态和讲解；标题与简介只负责定位主题。B20尤其值得借鉴，但实时一起看与整批离线摘要的调度不同。

迁移到YonWORK时，选型问题、摘要格式、阶段验收可以写成Skill；下载、ASR、抽帧、浏览器截图和文件存储依赖实际工具。DSH原生插件不能仅复制说明文字就视为兼容。当前未部署YonWORK、未安装这些项目、未验证具体DS/Qwen模型表现。

## 最小实践

选一个小任务，固定输入、验收条件和模型配置。记录成功率、工具次数、输入输出tokens、耗时与返工原因。先用这些指标判断插件是否有价值，再对照40%节省、20倍速度等宣传数字。

关联：[B01](../sources/bilibili/B01.md)、[B02](../sources/bilibili/B02.md)、[B08](../sources/bilibili/B08.md)、[B13](../sources/bilibili/B13.md)、[B20](../sources/bilibili/B20.md)、[X18](../sources/xiaohongshu/X18.md)。
