---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-114
title: 混淆后的映射文件具体在哪个路径下
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 混淆后的映射文件具体在哪个路径下
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:be0bbbcc7ee8e02def0607fb70d7f172edb8a9cc3cc1a74cdd4d72ad41cd7f2e
---

1. obfuscation.txt：打包后放置混淆规则的 consumer-rules.txt 文件。

   目录：build/default/intermediates/obfuscation/default/obfuscation.txt
2. nameCache.json：记录源码名称混淆映射关系的文件。

   目录：build/default/cache/default@CompileArkTS/esmodule/release/obfuscation/nameCache.json
3. 混淆后的d.ets和js文件。

   目录：build/default/intermediates/loader\_out/default/...
4. sourceMaps.json：关联编译后的代码和源码，通过行列号映射。

   目录：build/default/cache/default@CompileArkTS/esmodule/release/sourceMaps.json

**参考链接：**

[ArkGuard混淆原理及功能](../harmonyos-guides/source-obfuscation.md)
