---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-45
title: 如何判断文件是不是目录
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何判断文件是不是目录
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:30+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:4e3eeb602291e9c2ab6ab04c1d2e5f138a5986fcd73b24f6b9899292ca275e3a
---

判断文件是否为目录可以使用方法 fileIo.statSync(dirPath).isDirectory()。返回结果为 true 表示是目录。

**参考链接**

[isDirectory](../harmonyos-references/js-apis-file-fs.md#isdirectory)
