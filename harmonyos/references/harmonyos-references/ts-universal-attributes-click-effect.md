---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-effect
title: 点击回弹效果
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 点击回弹效果
category: harmonyos-references
scraped_at: 2026-04-29T13:51:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b1be0e93d1934b501749e6b85b33b3a47227c374e19bedf923a5eb652a740707
---

设置组件点击时的回弹效果。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## clickEffect

PhonePC/2in1TabletTVWearable

clickEffect(value: ClickEffect | null): T

设置当前组件的点击回弹效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ClickEffect](ts-universal-attributes-click-effect.md#clickeffect对象说明) | null | 是 | 设置当前组件点击回弹效果。  **说明：**  可通过null取消点击回弹效果。  不建议在组件大小动态变化的场景中使用该功能。  当组件无法触发通用事件时，不支持该属性。  回弹触发缩放后可能造成触摸点不在控件上，控件上无法响应手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## clickEffect18+

PhonePC/2in1TabletTVWearable

clickEffect(effect: Optional<ClickEffect | null>): T

设置当前组件的点击回弹效果。与[clickEffect](ts-universal-attributes-click-effect.md#clickeffect)相比，新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ClickEffect](ts-universal-attributes-click-effect.md#clickeffect对象说明) | null> | 是 | 设置当前组件的点击回弹效果。  **说明：**  可通过undefined或者null取消点击回弹效果。  不建议在组件大小动态变化的场景中使用该功能。  当组件无法触发通用事件时，不支持该属性。  回弹触发缩放后可能造成触摸点不在控件上，控件上无法响应手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ClickEffect对象说明

PhonePC/2in1TabletTVWearable

定义点击效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| level | [ClickEffectLevel](ts-appendix-enums.md#clickeffectlevel10) | 否 | 否 | 设置当前组件的点击回弹效果。  默认值：ClickEffectLevel.LIGHT  **说明：**  当level为undefined或者null时， ClickEffect采用ClickEffectLevel.LIGHT对应的回弹效果，缩放比参照scale说明。 |
| scale | number | 否 | 是 | 回弹缩放比例，支持在设置ClickEffectLevel的基础上微调。  **说明：**  当level为ClickEffectLevel.LIGHT时，默认值：0.90  当level为ClickEffectLevel.MIDDLE或者ClickEffectLevel.HEAVY时，默认值：0.95  当level为undefined或者null时，level为ClickEffectLevel.LIGHT，默认值：0.90  当scale为undefined或者null时，使用当前level对应的默认缩放比例。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示不同组件的点击回弹效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ToggleExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
8. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
9. Toggle({ type: ToggleType.Switch, isOn: false })
10. .clickEffect({ level: ClickEffectLevel.LIGHT })
11. .selectedColor('#007DFF')
12. .switchPointColor('#FFFFFF')
13. .onChange((isOn: boolean) => {
14. console.info('Component status:' + isOn);
15. })

17. Toggle({ type: ToggleType.Switch, isOn: true })
18. .clickEffect({ level: ClickEffectLevel.LIGHT, scale: 0.5 })
19. .selectedColor('#007DFF')
20. .switchPointColor('#FFFFFF')
21. .onChange((isOn: boolean) => {
22. console.info('Component status:' + isOn);
23. })
24. }

26. Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
27. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
28. Toggle({ type: ToggleType.Checkbox, isOn: false })
29. .clickEffect({ level: ClickEffectLevel.MIDDLE })
30. .size({ width: 20, height: 20 })
31. .selectedColor('#007DFF')
32. .onChange((isOn: boolean) => {
33. console.info('Component status:' + isOn);
34. })

36. Toggle({ type: ToggleType.Checkbox, isOn: true })
37. .clickEffect({ level: ClickEffectLevel.MIDDLE, scale: 0.5 })
38. .size({ width: 20, height: 20 })
39. .selectedColor('#007DFF')
40. .onChange((isOn: boolean) => {
41. console.info('Component status:' + isOn);
42. })
43. }

45. Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
46. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
47. Toggle({ type: ToggleType.Button, isOn: false }) {
48. Text('status button').fontColor('#182431').fontSize(12)
49. }.width(106)
50. .clickEffect({ level: ClickEffectLevel.HEAVY })
51. .selectedColor('rgba(0,125,255,0.20)')
52. .onChange((isOn: boolean) => {
53. console.info('Component status:' + isOn);
54. })

56. Toggle({ type: ToggleType.Button, isOn: true }) {
57. Text('status button').fontColor('#182431').fontSize(12)
58. }.width(106)
59. .clickEffect({ level: ClickEffectLevel.HEAVY, scale: 0.5 })
60. .selectedColor('rgba(0,125,255,0.20)')
61. .onChange((isOn: boolean) => {
62. console.info('Component status:' + isOn);
63. })
64. }
65. }.width('100%').padding(24)
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/SNaMyonGQUSoK1XjkOI64Q/zh-cn_image_0000002558606388.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055120Z&HW-CC-Expire=86400&HW-CC-Sign=CFF33D46FC9AF4A089803E040B8D066BDC226294CF0240334D08A801AB2AF8F3)
