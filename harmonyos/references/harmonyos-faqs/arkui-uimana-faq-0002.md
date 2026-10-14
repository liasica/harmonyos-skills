---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0002
title: 穿戴侧应用开发方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 穿戴侧应用开发方案
category: harmonyos-faqs
scraped_at: 2026-10-15T07:14:31+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:8bd8e6efd581f94ca2aa28a4e75c002afc63e23a3abd2461d1ae82e054aa54ba
---

**Q：穿戴侧应用开发目前只能用JS实现吗，请问是否有ArkTS实现方案？**

**A**：根据穿戴设备类型不同，采用不同实现方案进行应用开发：

* 智能穿戴：支持HarmonyOS 5及以上的智能穿戴设备主要有[Watch 5](../doccenter-multi-device/bpta-smartwatch.md#section0753201313919)，使用ArkTS语言开发，可以参考[穿戴侧应用开发](../connectivity-Guides/watch-dev-0000001119195134.md)。
* 轻量级智能穿戴：如HUAWEI Watch GT系列、Watch D系列、Fit系列，可以参考[兼容JS的类Web开发范式（ArkUI.Lite）](../harmonyos-references/arkui-js-lite-comp.md)进行开发。
* 智能穿戴设备兼容FA模型，可以将使用JS构建的轻量级智能穿戴项目迁移到智能穿戴设备上继续使用，实现功能的延续与适配。详细参考[FA工程迁移指导](../best-practices/bpta-smartwatch.md#section14111733132515)。

**Q：ArkTS是否有支持手表类的特有显示效果的UI组件？**

**A**：可在UI文档中查找命名为Arc开头的组件，例如[ArcList](../harmonyos-references/ts-container-arclist.md)等。

**Q：Watch5手表设备是否能用于GT5端APP的测试和调试？**

**A**：Watch5手表无法调试GT5端APP，GT5属于轻量级智能穿戴而Watch5属于智能穿戴两者在功能和硬件能力上有一定的区别。

**Q：如果想开发轻量级智能穿戴HarmonyOS应用，需要用什么版本的API开发？**

**A**：API版本详细参考[轻量级智能穿戴产品系列支持API表](../lite-wearable-guides/lite-wearable-bpta-guide.md)。

**Q：Watch5系列，支持低功耗蓝牙开发吗？**

**A**：Watch5系列是支持的。当前Watch5系列已支持ArkTS开发，并且在[低功耗蓝牙](../harmonyos-references/js-apis-bluetooth-ble.md)文档的支持设备中有Wearable设备。

**Q：如何将使用JS构建的轻量级智能穿戴项目迁移到智能穿戴设备上继续使用，实现功能的延续与适配？**

**A**：以轻量级智能穿戴开发实践同源工程为例，按照如下步骤，可以将使用JS构建的项目迁移到智能穿戴设备上：[FA工程迁移指导](../best-practices/bpta-smartwatch.md#section14111733132515)。

**Q：智能穿戴设备上可以开发哪些场景的APP功能？**

**A**：可以在智能穿戴设备上实现[地图应用](https://gitcode.com/HarmonyOS_Samples/SmartWatchMap)、[短视频应用](https://gitcode.com/HarmonyOS_Samples/SmartWatchShortVideo)、[车控应用](https://gitcode.com/HarmonyOS_Samples/SmartWatchCarControl)等。更多场景可以参考[项目](https://gitcode.com/HarmonyOS_Samples)。

**Q：是否所有华为手表都支持ArkWeb？**

**A**：并非所有手表都支持ArkWeb。Wearable智能表在HarmonyOS 5+上支持ArkTS语言和ArkWeb；Lite Wearable运动表在HarmonyOS 5+上仅支持JS语言和部分ArkUI开发，不支持ArkWeb。具体支持请参考[兼容JS的类Web开发范式](../harmonyos-references/arkui-js-lite-comp.md)和[最佳实践](../lite-wearable-guides/lite-wearable-bpta-guide.md)。

**Q：穿戴侧应用如何获取心率和步数等健康数据？**

**A**：可以接入[@ohos.sensor（传感器）](../harmonyos-references/js-apis-sensor.md)订阅对应传感器数据。使用[sensor.on(SensorId.HEART\_RATE)](../harmonyos-references/js-apis-sensor.md#sensoron)订阅心率传感器数据，调用后系统会按设定频率通过callback持续上报心率数据，从回调函数返回的[HeartRateResponse](../harmonyos-references/js-apis-sensor.md#heartrateresponse)中获取心率值。使用[sensor.on(SensorId.PEDOMETER)](../harmonyos-references/js-apis-sensor.md#pedometer9)订阅计步器传感器数据，从回调函数返回的[PedometerResponse](../harmonyos-references/js-apis-sensor.md#pedometerresponse)中获取行走步数。

**Q：轻量级智能穿戴设备是否支持通过蓝牙传输数据？**

**A**：支持。如Watch FIT 5支持[低功耗蓝牙](../harmonyos-references/js-apis-bluetooth-ble.md)，可以在手表端创建蓝牙连接进行数据传输。

**Q：华为Watch和GT系列是否支持第三方应用上架？个人开发者开发的应用能否通过审核在GT系列使用？**

**A**：华为Watch和GT系列均支持第三方应用上架。个人开发者完成实名认证后开发的应用可以通过审核在GT系列上架使用。
