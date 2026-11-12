---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-166
title: 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“byteCodeHar not supported when useNormalizedOHMUrl is not true.”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b3ba4b205bb9fb84b0379706675c6b1942e2855e192fc6cb3af3eae7441d04c7
---

**错误描述**

当useNormalizedOHMUrl配置为false时，不支持编译字节码HAR。

**可能原因**

当HAR模块的build-profile.json5文件中的byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段未配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/OiGyDtXNSxiEvjG7tNGdug/zh-cn_image_0000002654798007.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=D49C12492E9DFFD34E656B85080AC9A72CFB29727A43AB95A251460E488904FB)

**解决措施**

当HAR模块的build-profile.json5文件中byteCodeHar字段配置为true时，工程级build-profile.json5文件中的useNormalizedOHMUrl字段也必须配置为true。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/CtcdtpI5QfOu_p1ZyTJpVw/zh-cn_image_0000002624638558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1793C1FFF9206301E904E6ADA6F8138AE8323C4E58CEEBB6308D15FA274CC86)

**参考链接**

[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)
