---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units
title: 像素单位
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 公共定义 > 像素单位
category: harmonyos-references
scraped_at: 2026-04-28T08:02:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8dca89376f60013f392be9734f565e7c92ee74567c0bdeda39edf8b765884a81
---

ArkUI为开发者提供4种像素单位，采用vp为基准数据单位。

说明

* 本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 直接使用vp2px/px2vp/fp2px/px2fp/lpx2px/px2lpx可能存在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，以下接口从API version 18开始废弃，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，再使用UIContext下的[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)/[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)/[fp2px](arkts-apis-uicontext-uicontext.md#fp2px12)/[px2fp](arkts-apis-uicontext-uicontext.md#px2fp12)/[lpx2px](arkts-apis-uicontext-uicontext.md#lpx2px12)/[px2lpx](arkts-apis-uicontext-uicontext.md#px2lpx12)调用绑定实例的接口。
* 在UI实例未创建时，vp2px/px2vp使用默认屏幕的虚拟像素比进行转换。在该场景下，使用UIContext接口替换时，开发者可参考[像素单位转换接口替换为UIContext接口](../harmonyos-guides/arkts-global-interface.md#像素单位转换接口替换为uicontext接口)。

| 名称 | 描述 |
| --- | --- |
| px | 屏幕物理像素单位。 |
| vp | 屏幕密度相关像素，根据屏幕像素密度转换为屏幕物理像素，当数值不带单位时，默认单位vp。  **说明：**  vp与px的比例与屏幕像素密度有关。 |
| fp | 字体像素，与vp类似适用屏幕密度变化，随系统字体大小设置变化。 |
| lpx | 视窗逻辑像素单位，lpx单位为实际屏幕宽度与逻辑宽度（通过[designWidth](../harmonyos-guides/module-configuration-file.md#pages标签)配置）的比值，designWidth默认值为720。当designWidth为720时，在实际宽度为1440物理像素的屏幕上，1lpx为2px大小。 |

## vp2px(deprecated)

PhonePC/2in1TabletTVWearable

vp2px(value: number): number

将vp单位的数值转换为以px为单位的数值。

说明

默认使用当前UI实例所在屏幕的虚拟像素比进行转换，UI实例不明确时，使用默认屏幕的虚拟像素比进行转换，可能导致转换后结果与预期不一致的情况。

从API version 7开始支持，从API version 18开始废弃，建议使用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将vp单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## px2vp(deprecated)

PhonePC/2in1TabletTVWearable

px2vp(value: number): number

将px单位的数值转换为以vp为单位的数值。

说明

默认使用当前UI实例所在屏幕的虚拟像素比进行转换，UI实例不明确时，使用默认屏幕的虚拟像素比进行转换，可能导致转换后结果与预期不一致的情况。

从API version 7开始支持，从API version 18开始废弃，建议使用[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以vp为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## fp2px(deprecated)

PhonePC/2in1TabletTVWearable

fp2px(value: number): number

将fp单位的数值转换为以px为单位的数值。

说明

从API version 7开始支持，从API version 18开始废弃，建议使用[fp2px](arkts-apis-uicontext-uicontext.md#fp2px12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将fp单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## px2fp(deprecated)

PhonePC/2in1TabletTVWearable

px2fp(value: number): number

将px单位的数值转换为以fp为单位的数值。

说明

从API version 7开始支持，从API version 18开始废弃，建议使用[px2fp](arkts-apis-uicontext-uicontext.md#px2fp12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以fp为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## lpx2px(deprecated)

PhonePC/2in1TabletTVWearable

lpx2px(value: number): number

将lpx单位的数值转换为以px为单位的数值。

说明

从API version 7开始支持，从API version 18开始废弃，建议使用[lpx2px](arkts-apis-uicontext-uicontext.md#lpx2px12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将lpx单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## px2lpx(deprecated)

PhonePC/2in1TabletTVWearable

px2lpx(value: number): number

将px单位的数值转换为以lpx为单位的数值。

说明

从API version 7开始支持，从API version 18开始废弃，建议使用[px2lpx](arkts-apis-uicontext-uicontext.md#px2lpx12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以lpx为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example {
5. build() {
6. Column() {
7. Flex({ wrap: FlexWrap.Wrap }) {
8. Column() {
9. Text("width(220)")
10. .width(220)
11. .height(40)
12. .backgroundColor(0xF9CF93)
13. .textAlign(TextAlign.Center)
14. .fontColor(Color.White)
15. .fontSize('12vp')
16. }.margin(5)

18. Column() {
19. Text("width('220px')")
20. .width('220px')
21. .height(40)
22. .backgroundColor(0xF9CF93)
23. .textAlign(TextAlign.Center)
24. .fontColor(Color.White)
25. }.margin(5)

27. Column() {
28. Text("width('220vp')")
29. .width('220vp')
30. .height(40)
31. .backgroundColor(0xF9CF93)
32. .textAlign(TextAlign.Center)
33. .fontColor(Color.White)
34. .fontSize('12vp')
35. }.margin(5)

37. Column() {
38. Text("width('220lpx') designWidth:720")
39. .width('220lpx')
40. .height(40)
41. .backgroundColor(0xF9CF93)
42. .textAlign(TextAlign.Center)
43. .fontColor(Color.White)
44. .fontSize('12vp')
45. }.margin(5)

47. Column() {
48. Text("width(vp2px(220) + 'px')")
49. .width(this.getUIContext().vp2px(220) + 'px')
50. .height(40)
51. .backgroundColor(0xF9CF93)
52. .textAlign(TextAlign.Center)
53. .fontColor(Color.White)
54. .fontSize('12vp')
55. }.margin(5)

57. Column() {
58. Text("fontSize('12fp')")
59. .width(220)
60. .height(40)
61. .backgroundColor(0xF9CF93)
62. .textAlign(TextAlign.Center)
63. .fontColor(Color.White)
64. .fontSize('12fp')
65. }.margin(5)

67. Column() {
68. Text("width(px2vp(220))")
69. .width(this.getUIContext().px2vp(220))
70. .height(40)
71. .backgroundColor(0xF9CF93)
72. .textAlign(TextAlign.Center)
73. .fontColor(Color.White)
74. .fontSize('12fp')
75. }.margin(5)
76. }.width('100%')
77. }
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/ISDS3gVzTfCTPwurjMY6FQ/zh-cn_image_0000002552800494.png?HW-CC-KV=V1&HW-CC-Date=20260428T000245Z&HW-CC-Expire=86400&HW-CC-Sign=5F2C4A6E69F0A7717DD7C9DB168003E64C0D5A1042733142CD8980D0171A0D74)
