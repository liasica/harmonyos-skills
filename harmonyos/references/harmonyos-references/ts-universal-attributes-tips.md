---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-tips
title: Tips控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 弹窗控制 > Tips控制
category: harmonyos-references
scraped_at: 2026-04-29T13:51:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4221877d1034166fd1420476ecd8fb3f369f84807dd21ab12f9b1b21ea5bbdd3
---

为组件绑定Tips悬浮气泡，当鼠标悬浮在组件上时，自动显示提示信息；鼠标离开组件时，悬浮气泡自动隐藏。

说明

* 从API version 19开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 目前支持通过外接鼠标、手写笔以及触控板触发。

## bindTips

PhonePC/2in1TabletTVWearable

bindTips(message: TipsMessageType, options?: TipsOptions): T

为组件绑定Tips悬浮气泡。

说明

当绑定bindTips的组件设置通用属性[enable](ts-universal-attributes-enable.md#enabled)为false时，仍支持弹出悬浮气泡。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | [TipsMessageType](ts-universal-attributes-tips.md#tipsmessagetype) | 是 | 弹窗信息内容。 |
| options | [TipsOptions](ts-universal-attributes-tips.md#tipsoptions类型说明) | 否 | 配置悬浮气泡的参数。  默认值：  {  appearingTime: 700,  disappearingTime: 300,  appearingTimeWithContinuousOperation: 300,  disappearingTimeWithContinuousOperation: 0, enableArrow: true,  arrowPointPosition: ArrowPointPosition.CENTER,  arrowWidth: 16,arrowHeight: 8,  showAtAnchor: TipsAnchorType.TARGET  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## TipsOptions类型说明

PhonePC/2in1TabletTVWearable

悬浮气泡自定义参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appearingTime | number | 否 | 是 | 设置悬浮气泡的显示时延。显示时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。  默认值：700  单位：ms  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| disappearingTime | number | 否 | 是 | 设置悬浮气泡的隐藏时延。隐藏时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。  默认值：300  单位：ms  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| appearingTimeWithContinuousOperation | number | 否 | 是 | 多个组件连续弹出悬浮气泡时，悬浮气泡的显示时延。显示时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。  默认值：300  单位：ms  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| disappearingTimeWithContinuousOperation | number | 否 | 是 | 多个组件连续弹出悬浮气泡时，悬浮气泡的隐藏时延。隐藏时延的最大值为4000ms，设置超过4000ms的值以4000ms为准。  默认值：0  单位：ms  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| enableArrow | boolean | 否 | 是 | 设置是否显示气泡箭头。  默认值：true  true：显示箭头；false：不显示箭头。  **说明：**  当页面可用空间无法让气泡完全避让时，气泡会覆盖到组件上并且不显示气泡箭头。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| arrowPointPosition | [ArrowPointPosition](ts-appendix-enums.md#arrowpointposition11) | 否 | 是 | 气泡箭头相对于父组件显示位置，气泡箭头在垂直和水平方向上有 “Start”、“Center”、“End”三个位置点可选。所有位置点均位于父组件区域范围内，不会超出父组件的边界范围，也不会覆盖圆角范围。  默认值：ArrowPointPosition.CENTER  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| arrowWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置气泡箭头宽度。若所设置的宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。  默认值：16  单位：vp  **说明：**  不支持设置百分比。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| arrowHeight | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置气泡箭头高度。  默认值：8  单位：vp  **说明：**  不支持设置百分比。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| showAtAnchor20+ | [TipsAnchorType](ts-appendix-enums.md#tipsanchortype20) | 否 | 是 | 设置Tips跟随类型。  默认值：TipsAnchorType.TARGET  **说明：**  Tips的跟随类型为TipsAnchorType.CURSOR时，Tips不显示箭头。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## TipsMessageType

PhonePC/2in1TabletTVWearable

type TipsMessageType = ResourceStr | StyledString

悬浮气泡弹窗信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ResourceStr](ts-types.md#resourcestr) | 字符串类型，用于描述字符串入参可以使用的类型。 |
| [StyledString](ts-universal-styled-string.md#styledstring) | 属性字符串。 |

## 示例

PhonePC/2in1TabletTVWearable

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

### 示例1（悬浮气泡的显示和消失）

此示例为bindTips通过绑定Button产生悬浮气泡。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TipsExample {
5. build() {
6. Flex({ direction: FlexDirection.Column }) {
7. Button('Hover Tips')
8. .bindTips("Tips", {
9. appearingTime: 700,
10. disappearingTime: 300,
11. appearingTimeWithContinuousOperation: 300,
12. disappearingTimeWithContinuousOperation: 0,
13. enableArrow: true,
14. })
15. .position({ x: 100, y: 250 })
16. }.width('100%').padding({ top: 5 })
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/bv5gcQjeTtaoCFzRYtHnEQ/zh-cn_image_0000002589325941.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055126Z&HW-CC-Expire=86400&HW-CC-Sign=13D1AE920F068B4A5242B1D20DD054888363A2F606CC2FE9C577F056531B213A)

### 示例2（多个悬浮气泡的显示和消失）

此示例展示了如何使用bindTips配置多个悬浮气泡依次显示和消失。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct TipsExample {
6. build() {
7. Flex({ direction: FlexDirection.Column }) {
8. Button('Hover Tips')
9. .bindTips("Tips", {
10. appearingTime: 700,
11. disappearingTime: 300,
12. appearingTimeWithContinuousOperation: 300,
13. disappearingTimeWithContinuousOperation: 0,
14. enableArrow: true,
15. })
16. .position({ x: 100, y: 250 })

18. Button('Hover Tips')
19. .bindTips("Tips", {
20. appearingTime: 700,
21. disappearingTime: 300,
22. appearingTimeWithContinuousOperation: 300,
23. disappearingTimeWithContinuousOperation: 0,
24. enableArrow: true,
25. })
26. .position({ x: 100, y: 350 })

29. }.width('100%').padding({ top: 5 })
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/gLRJGZynQluyNKHHQMNvgA/zh-cn_image_0000002589245883.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055126Z&HW-CC-Expire=86400&HW-CC-Sign=3DEC4187DEC44D9302BB38CE7CB968A6E2C58C09616F8FA909C712B8489EBBA9)
