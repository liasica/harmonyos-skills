---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-46
title: 解决冷启动picker选择器无权限问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 解决冷启动picker选择器无权限问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:31+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:844501e5750ecf9e01f0931d6fbed46b6434dfd7649eb7a44f9008b9b1d1d457
---

在APP冷启动后，由于没有uri的读取权限，可以通过保存草稿操作将对应的文件复制到沙箱路径下，然后在冷启动时获取这些文件。

**参考链接**

[fileIo.copyFile](../harmonyos-references/js-apis-file-fs.md#fileiocopyfile)

[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)
