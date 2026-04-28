---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-43
title: 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ba83cf1dd23bbc29c52a544db40ac1e8bc0af73bf6da4df34af87b8723765ba6
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/32M4YfF5T4yJqlkY9sDqnA/zh-cn_image_0000002229604385.png?HW-CC-KV=V1&HW-CC-Date=20260428T002915Z&HW-CC-Expire=86400&HW-CC-Sign=5488BEEB5DCBE68CECE055272DD66F2B6C59ABE54F1DAEFAEE24A2CA701733B5 "点击放大")

**问题分析**

报该错误，可能是build-profile.json5文件中未添加“targets”配置，Module Target下为空，工程同步失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/VDHphnLZQRWjCeQEkGrmkA/zh-cn_image_0000002272490329.png?HW-CC-KV=V1&HW-CC-Date=20260428T002915Z&HW-CC-Expire=86400&HW-CC-Sign=4486FE672B0CE82B652648C970AC9D1AA7E748B60232444254B5019E0799B55D)

**解决措施**

需要在模块级build-profile.json5文件中添加“targets”配置，点击“Sync Now”，待完成同步后，即可解决该问题（确保工程同步成功）。具体配置如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/fC-uMlBKQs6pT2DsWm6Xsw/zh-cn_image_0000002229758873.png?HW-CC-KV=V1&HW-CC-Date=20260428T002915Z&HW-CC-Expire=86400&HW-CC-Sign=01ADB3D017D6C4DF4B878935A319AEEA4A94BB098B33C3D218389E08D57FC658 "点击放大")
