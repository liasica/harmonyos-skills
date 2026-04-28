---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-3
title: 如何实现文件不存在则创建文件
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何实现文件不存在则创建文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:25848b04d2559848eb17e0eda01dc797d472d6d3e2261863910b42deb5d609e2
---

可以通过调用fs.open函数来实现，open(path: string, mode?: number)，指定第二个参数mode为 fs.OpenMode.CREATE，表示如果文件不存在，则创建文件。

**参考链接**

[文件管理](../harmonyos-references/js-apis-file-fs.md)
