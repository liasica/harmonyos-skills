---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166
title: 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:48c8d3c6f6729ec262a33a5793d9c065a8d6afc929935f317b0e089657e2a78f
---

**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/AbnliVEeSiO_VD9OZl4n_A/zh-cn_image_0000002194318416.png?HW-CC-KV=V1&HW-CC-Date=20260428T002944Z&HW-CC-Expire=86400&HW-CC-Sign=D8940F3699C1F9259A49E395723F7A06A4FF44329AEC9A197EBEDBEA11B91E62)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/WnJPRKIlQVSYODdmV8rxQg/zh-cn_image_0000002308297297.png?HW-CC-KV=V1&HW-CC-Date=20260428T002944Z&HW-CC-Expire=86400&HW-CC-Sign=14E82AAD191FC585CB1FC3BACA3A48884AF48CB885092ACC039BAAF582722591)

**参考链接**

[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)
