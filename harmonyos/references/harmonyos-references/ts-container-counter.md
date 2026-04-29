---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter
title: Counter
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > Counter
category: harmonyos-references
scraped_at: 2026-04-29T13:52:20+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3617b2208e14216d4939457ad76415158dacad93a7383c15bb46cd8be97afc0f
---

计数器组件，提供相应的增加或者减少的计数操作。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

Counter()

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性。

### enableInc10+

PhonePC/2in1TabletTVWearable

enableInc(value: boolean)

设置“增加”按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | “增加”按钮禁用或使能。  默认值：true，true表示使能“增加”按钮，false表示禁用“增加”按钮。 |

### enableDec10+

PhonePC/2in1TabletTVWearable

enableDec(value: boolean)

设置“减少”按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | “减少”按钮禁用或使能。  默认值：true，true表示使能“减少”按钮，false表示禁用“减少”按钮。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onInc

PhonePC/2in1TabletTVWearable

onInc(event: VoidCallback)

监听数值增加事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | Counter数值增加的回调函数。 |

### onDec

PhonePC/2in1TabletTVWearable

onDec(event: VoidCallback)

监听数值减少事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | Counter数值减少的回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示了Counter组件的基本使用方法。点击+、-按钮可以修改value值。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CounterExample {
5. @State value1: number = 0;
6. @State value2: number = 0;

8. build() {
9. Column({ space: 50 }) {
10. Counter() {
11. Text(this.value1.toString())
12. }
13. .onInc(() => {
14. this.value1++;
15. })
16. .onDec(() => {
17. this.value1--;
18. })

20. Counter() {
21. Text(this.value2.toString())
22. }
23. .onInc(() => {
24. this.value2++;
25. })
26. .onDec(() => {
27. this.value2--;
28. })
29. .enableInc(true)
30. .enableDec(false)
31. }
32. .width('100%')
33. .height('100%')
34. .justifyContent(FlexAlign.Center)
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/goDz_BeAQkO-o7B5FHAffA/zh-cn_image_0000002558606768.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055217Z&HW-CC-Expire=86400&HW-CC-Sign=E1196F3AC1CB074881B6D5B9CBBDED610E71B4CC0823001955FDD3C500BE5F1B)
