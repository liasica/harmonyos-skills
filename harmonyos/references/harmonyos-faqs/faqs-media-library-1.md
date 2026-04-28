---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-1
title: 如何监听文件或文件目录的变化
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何监听文件或文件目录的变化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:31+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:d5e7005b8eb77c94c1cd56a17ad6ffbd3e3653a950cfc8447cd7e1dc3e9ced5a
---

使用fileIo.createWatcher监听文件或目录的变化，并通过回调函数异步处理变化事件。应用需要根据业务需求控制通知处理策略，可以将变化信息存储到消息队列中，并定期刷新。

**参考链接**

[fileIo.createWatcher](../harmonyos-references/js-apis-file-fs.md#fileiocreatewatcher10)
