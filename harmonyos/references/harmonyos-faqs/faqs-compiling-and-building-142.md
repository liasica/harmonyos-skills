---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-142
title: 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“useNormalizedOHMUrl can be true only when Compatible SDK Version is 5.0.0 (12) or later”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:3b0a9fef93ad3e4793dbf36d5df8d470bddb707ffb1e65da19a02173fbd1fd8b
---

**错误描述**

仅当兼容SDK版本为5.0.0(12)及以上版本时，useNormalizedOHMUrl才可以设置为true。

**可能原因**

当compatibleSdkVersion为5.0.0(12)以下版本时，设置useNormalizedOHMUrl为true导致。

**解决措施**

检查工程级build-profile.json5文件中的compatibleSdkVersion配置。如果compatibleSdkVersion为 4.1.0(11) 及之前版本，请将[useNormalizedOHMUrl](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)设置为false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/nO-k1nqJRpuByY0YHTQ8ag/zh-cn_image_0000002654837939.png)
