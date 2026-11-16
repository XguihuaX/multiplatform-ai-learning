# 视频下载与阅读管线：2026-11-16 实测

## 工具分工

- yt-dlp：识别平台页面，解析并下载视频/音频；支持批处理和保存元数据。[官方文档](https://github.com/yt-dlp/yt-dlp)
- wget/curl：下载已知文件地址。给它笔记网页通常得到HTML，不能据此取得视频。
- ffmpeg：解码音频、抽帧、合并分离的音视频。
- Whisper medium：本地音频转文字；当前Mac采用MLX实现。faster-whisper CPU也已准备，但本机速度不理想。
- 学习笔记：结合正文、带时间戳的转写、关键帧和原始项目资料，人工式审读归纳。

## 已验证结果

小红书指定区间共27条，全部视频已下载，目录`.cache/video-retry/`，约786 MiB。每条提取6或12张关键帧，已阅读全部概览图；详细观察见[画面记录](2026-11-16-visual-observations.json)。本轮检查已完成X01–X09转写及审读，X10处理中。完整音频逐条转写中，成功结果写入`.cache/transcripts/Xnn.json`。自动转写包含错别字，工具名需对照画面。

关键发现：小红书嵌套个人主页笔记链接不适合直接提取；改用网页实际链接中的笔记ID和签名参数构成标准explore链接后成功。签名参数保留本地，不写入仓库。

```sh
uv tool run --from yt-dlp yt-dlp --ignore-errors --no-playlist \
  --no-progress --write-info-json --batch-file .cache/xhs-download-urls.txt \
  -o '.cache/video-retry/%(id)s.%(ext)s'

python3 scripts/keyframe_sheets.py
uv run --python 3.12 --with mlx-whisper python scripts/transcribe_mlx.py
```

本次yt-dlp版本2026.10.26。批量文件须使用当前可访问的链接；历史签名可能失效。

## B站当前未解决的问题

网页及API提取返回HTTP 412；从已登录播放器读取的媒体地址用curl下载，一条域名返回567、另一条返回403；浏览器video媒体导出失败。网页可读、播放可用不等于命令行可下载。暂未获得本地完整媒体，23条保留正文和原项目资料阅读范围。

不把失败推广为所有B站视频均无法下载。后续可在可用的官方客户端下载路径或适配当前平台的下载器上继续小样本验证，再扩展批量。

## 后续复用

Skill可以编排上述步骤；MCP可以把下载、转写和取帧包装成工具接口。DS/Qwen负责审读与总结时，需要宿主提供工具执行和文件读写能力；仅粘贴提示词不会自动获得ASR或视频视觉能力。当前脚本在这台Mac已验证部分流程，尚未部署到YonWORK。
