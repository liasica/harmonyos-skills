---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-18
title: DevEco Studio上使用使用api或组件时编辑器提示各种报错与告警
breadcrumb: FAQ > DevEco Studio > 代码编辑 > DevEco Studio上使用使用api或组件时编辑器提示各种报错与告警
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:5ff6034ccc157c8a9794d3573419c9c28737b2d9efadbf8667e30ffd6e361eff
---

## 场景1

使用ArcList组件时编辑器提示"The default system capabilities of devices wearable do not include SystemCapability.ArkUI.ArkUI.Circle"。

**问题现象**

使用ArcList组件时，编辑器报错，错误信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/1tcYOqomRQqHM6CWtnWNJw/zh-cn_image_0000002665790183.png "点击放大")

**解决措施**

请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至6.0.1 Release及以上版本。

## 场景2

使用被@test标注的api或组件属性时编辑报错："This API can only be used for unit test code"。

**问题现象**

使用被@test标注的api或组件属性时，例如通用组件属性key时，编辑器会报错，错误信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/S4fMQ1P5TSOLc7_L6GiOeA/zh-cn_image_0000002635896056.png "点击放大")

**原因说明**

HarmonyOS目前采用jsdoc系统来标记各个api与组件属性能力与限制，被@test标注的api或组件属性表示该api或组件属性应当在测试目录下使用，因此编辑器在检查到被@test标注的api或组件属性在非测试代码中使用时会进行报错提示。

**解决措施**

请前往[下载中心](https://developer.huawei.com/consumer/cn/download/)将DevEco Studio更新至26.0.0 Beta2及以上版本。
