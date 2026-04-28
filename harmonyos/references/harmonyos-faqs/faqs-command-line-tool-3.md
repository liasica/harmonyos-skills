---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-3
title: 编译时DevEco Studio报“ohpm ERROR: EINSTALL install failed, Error: Dependency node build failed Install failed”错
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 编译时DevEco Studio报“ohpm ERROR: EINSTALL install failed, Error: Dependency node build failed Install failed”错
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c1199c6c58ac2ead6c1dc803ccf3171052070351335671b92cc7d0fb0d71f049
---

**问题现象**

编译时报错：

ohpm ERROR: EFETCH Fetch local file package error, D:\dev\harmonyos\mgty-ohos-phone\oh\_modules.ohpm@ohos+mgkv@pediph1+Vjwini4jdg9r1s9hqaq=\oh\_modules@ohos\mgkv\libs\MMKV.har does not exist.

ohpm ERROR: missing: D:\dev\harmonyos\mgty-ohos-phone\oh\_modules.ohpm@ohos+mgkv@pediph1+Vjwini4jdg9r1s9hqaq=\oh\_modules@ohos\mgkv\libs\MMKV.har, required by @ohos/mgkVOD:/dev/harmony/mgtv-ohos-phone/baseLib/kv/Lib/ngkv.nde.

ohpm ERROR: ERUNNING execute tasks failed, Error: Dependency node build failed.

ohpm ERROR: EINSTALL install failed, Error: Dependency node build failed.

Install failed.

**可能原因**

ohpm 1.4.0之后，HAR中存在相对路径的依赖，在生成oh\_module时，未添加对应的依赖。

**解决措施**

1. 将依赖包上传至私仓，配置私仓依赖，具体配置可参考[ohpm-repo私仓搭建工具](../harmonyos-guides/ide-ohpm-repo.md)。
2. 或者在项目级别的oh-package.json5文件中添加[overrides](../harmonyos-guides/ide-oh-package-json5.md#zh-cn_topic_0000001792256137_overrides)配置，覆盖依赖信息，将依赖替换为另一个版本。
