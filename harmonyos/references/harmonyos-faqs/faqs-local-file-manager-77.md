---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-77
title: fs.write和fs.createStream区别及使用场景
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > fs.write和fs.createStream区别及使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a653e13240e7b5af9406127045b0e1457d9422b9c293402d4bbd903bf59c43a3
---

## 问题现象

@ohos.file.fs模块的fs.write和fs.createStream区别及使用场景是什么？

## 解决方案

在HarmonyOS的@ohos.file.fs模块中，[fs.write](../harmonyos-references/js-apis-file-fs.md#fileiowrite)和[fs.createStream](../harmonyos-references/js-apis-file-fs.md#fileiocreatestream)是两种不同的文件写入方式:

* fs.write适用于数据量不大且不需要高级流控制的场景。例如，配置文件的修改或小文本文件的写入。
* 与fs.write不同，fs.createStream提供了一种更高效的方式来处理大量数据，尤其是当数据量很大以至于不适合一次性加载到内存中时，使用流式处理，数据可以分块进行读取和写入，从而有效地管理内存使用。
