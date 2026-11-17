# 素材登记

学习请从[教程索引](../knowledge/README.md)进入。

catalog.json保存50项素材的稳定ID、原链接、主分类、笔记路径和阅读证据。categories.json指定各类的手写教程路径、学习目标与深度。

lessons目录保存手写正文，生成器只读取它。指定lesson_body_path的素材页会内嵌对应教程，其余素材页链接到教程。媒体、原始长篇转写与签名链接留在本地缓存。
