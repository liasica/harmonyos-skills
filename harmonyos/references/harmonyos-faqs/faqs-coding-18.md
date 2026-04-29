---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-18
title: DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用ArcList组件时编辑器提示“The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cec546fe9334512a3781b55e9f661cc3cffcdb5d43aaf3000dcc50db43f30699
---

**问题现象**

使用ArcList组件时，编辑器报错，错误信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/07cXRZ2VT8SMoZTbMBwPsw/zh-cn_image_0000002459313966.png?HW-CC-KV=V1&HW-CC-Date=20260429T062016Z&HW-CC-Expire=86400&HW-CC-Sign=D7EA0BB1DFB33C7303A0D7D3A40717CE6BA072BC427FF6BBBD1FD9F6292FAE3A)

**解决措施**

1. 请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至6.0.1 Release及以上版本。
2. 若仍需使用当前版本，可在src/main目录下添加syscap.json配置文件。可参考[SysCap开发指导](../harmonyos-references/syscap.md#syscap开发指导)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vaI2nLaOTiiQ58W98Psd7w/zh-cn_image_0000002460277990.png?HW-CC-KV=V1&HW-CC-Date=20260429T062016Z&HW-CC-Expire=86400&HW-CC-Sign=9B71F475575D18898AFE3885184565750336BC5E41469BB5D9F4AE79C1722385)
