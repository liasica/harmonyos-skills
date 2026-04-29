---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166
title: 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ab86e26eaef0728bd36b8214509b7b456352a036fe8acd029c3ad175bfc64d58
---

**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/AbnliVEeSiO_VD9OZl4n_A/zh-cn_image_0000002194318416.png?HW-CC-KV=V1&HW-CC-Date=20260429T062059Z&HW-CC-Expire=86400&HW-CC-Sign=90B09716E2E64DBA82A7AB467B1206E94068F91607F732589D3730EE1A7107CF)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/WnJPRKIlQVSYODdmV8rxQg/zh-cn_image_0000002308297297.png?HW-CC-KV=V1&HW-CC-Date=20260429T062059Z&HW-CC-Expire=86400&HW-CC-Sign=0DDB2EB491E41C0E40E749E39C57B045CE26B364E967F65F25954B4B94F5B7EE)

**参考链接**

[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)
