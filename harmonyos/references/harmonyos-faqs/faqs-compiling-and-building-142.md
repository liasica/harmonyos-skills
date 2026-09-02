---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-142
title: 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e38da95b1b375de690de1fcd395d779076ae776f6a94c7f02ec1fa4cfbead0f4
---

**错误描述**

仅当兼容SDK版本为5.0.0(12)及以上版本时，useNormalizedOHMUrl才可以设置为true。

**可能原因**

当compatibleSdkVersion为5.0.0(12)以下版本时，设置useNormalizedOHMUrl为true导致。

**解决措施**

检查工程级build-profile.json5文件中的compatibleSdkVersion配置。如果compatibleSdkVersion为 4.1.0(11) 及之前版本，请将[useNormalizedOHMUrl](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)设置为false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Y21BUUFSTwaMxnh7TqJnfw/zh-cn_image_0000002363676020.png)
