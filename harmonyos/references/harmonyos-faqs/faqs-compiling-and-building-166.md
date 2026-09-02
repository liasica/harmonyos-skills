---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166
title: 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:272bcc0c523b14dc789133194f86f379d3bf11e48d99054f79db0ee1511bc0e6
---

**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/No-RpGWRQHqWyjOCuopDAw/zh-cn_image_0000002654798007.png)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/B9ms2pQDT5ufbgv4iMr_lA/zh-cn_image_0000002624638558.png)

**参考链接**

[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)
