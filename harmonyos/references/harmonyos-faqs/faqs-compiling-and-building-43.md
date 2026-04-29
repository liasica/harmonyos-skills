---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-43
title: 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c3aa11d52783c6c4e29f2b10b8ecce8b1a2ac167a130dc6a602ecc6e94dd85c3
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/32M4YfF5T4yJqlkY9sDqnA/zh-cn_image_0000002229604385.png?HW-CC-KV=V1&HW-CC-Date=20260429T062029Z&HW-CC-Expire=86400&HW-CC-Sign=26193B38785DC187D60312987ADFA15581E384BCDAB11B6EAA7BD0542680D2D5 "点击放大")

**问题分析**

报该错误，可能是build-profile.json5文件中未添加“targets”配置，Module Target下为空，工程同步失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/VDHphnLZQRWjCeQEkGrmkA/zh-cn_image_0000002272490329.png?HW-CC-KV=V1&HW-CC-Date=20260429T062029Z&HW-CC-Expire=86400&HW-CC-Sign=6142C25E3ECDA657CB241771E21B7B91C293C98839A34947748D857DE4FE22BF)

**解决措施**

需要在模块级build-profile.json5文件中添加“targets”配置，点击“Sync Now”，待完成同步后，即可解决该问题（确保工程同步成功）。具体配置如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/fC-uMlBKQs6pT2DsWm6Xsw/zh-cn_image_0000002229758873.png?HW-CC-KV=V1&HW-CC-Date=20260429T062029Z&HW-CC-Expire=86400&HW-CC-Sign=10FC35E345040BEEAA8466943E39AC229120F2C036DF4CA626DBDAACC06DC3C0 "点击放大")
