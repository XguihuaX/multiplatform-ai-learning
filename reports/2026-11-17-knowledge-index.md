# 2026-11-17：按知识分类维护与B站进度

50条笔记已从平台目录迁入knowledge下的8个类别。主入口为[知识分类索引](../knowledge/README.md)，专题总结保存在topics。原始平台、视频ID和链接继续存于catalog和每条笔记；B/X编号保留以维持证据对应，不承担分类作用。

## B站进度

BBDown批量下载已结束，23项共26个分P均取得本地MP4，ffprobe逐个确认音频与视频轨道。B09、B17、B23各有两个分P，其余一项一个。B03为约2小时7分钟的长课程。

B14与B22检测到内嵌字幕并已提取；其余分P启动本地Whisper medium转写，短视频优先，长课程后处理。素材清单在本地.cache/bilibili-parts.json，转写/字幕在.cache/bilibili-transcripts，进度日志为.cache/bilibili-asr.log。

当前笔记仍以此前简介与原项目文档为主，新下载视频尚未完成音频审读和画面学习。下载完成、转写完成和笔记整理分别记录，不合并计数。
