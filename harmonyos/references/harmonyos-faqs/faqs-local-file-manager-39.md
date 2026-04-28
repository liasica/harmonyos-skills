---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-39
title: fileIo.write返回的长度和本身content长度不一致
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > fileIo.write返回的长度和本身content长度不一致
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:29+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:e9f628283b2e21d21be7597e5cc587398cc337f1c27913db46d5a229cd0b4f48
---

fileIo.write返回的是实际写入的数据长度，单位字节。String.length返回的是字符串的长度，两者返回的单位不一样，所以在比较长度时也是不一致的。String.length返回UTF-16编码单元数，当字符串包含非ASCII字符时，其字节长度可能大于该值（如中文通常占3字节）。

参考文档：[fileIo.write](../harmonyos-references/js-apis-file-fs.md#write)
