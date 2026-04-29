---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-panel
title: Panel
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > Panel
category: harmonyos-references
scraped_at: 2026-04-29T13:53:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9011eeb8af50974c5d168f1017067c285bbd8858963cbf6543cb67a9bbd38a3f
---

可滑动面板，提供一种轻量的内容展示窗口，方便在不同尺寸中切换。

说明

从API version 12开始，该组件不再维护，推荐使用通用属性[bindSheet](ts-universal-attributes-sheet-transition.md)。

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

说明

子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。

## 接口

PhonePC/2in1TabletTVWearable

Panel(show: boolean)

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| show | boolean | 是 | 控制Panel显示或隐藏。  **说明：**  如果设置为false时，则不占位隐藏。[Visible.None](ts-universal-attributes-visibility.md)或者show之间有一个生效时，都会生效不占位隐藏。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### type

PhonePC/2in1TabletTVWearable

type(value: PanelType)

可滑动面板的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PanelType](ts-container-panel.md#paneltype枚举说明) | 是 | 设置可滑动面板的类型。  默认值：PanelType.Foldable |

### mode

PhonePC/2in1TabletTVWearable

mode(value: PanelMode)

可滑动面板的初始状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PanelMode](ts-container-panel.md#panelmode枚举说明) | 是 | 设置可滑动面板的初始状态。  Minibar类型默认值：PanelMode.Mini；其余类型默认值：PanelMode.Half  从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。 |

### dragBar

PhonePC/2in1TabletTVWearable

dragBar(value: boolean)

设置是否存在控制条。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否存在控制条，true表示存在，false表示不存在。  默认值：true |

### customHeight10+

PhonePC/2in1TabletTVWearable

customHeight(value: Dimension | PanelHeight)

指定PanelType.CUSTOM状态下的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [PanelHeight](ts-container-panel.md#panelheight10枚举说明) | 是 | 指定PanelType.CUSTOM状态下的高度。  默认值：0  **说明：**  不支持设置百分比。 |

### fullHeight

PhonePC/2in1TabletTVWearable

fullHeight(value: number | string)

指定PanelType.Full状态下的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Full状态下的高度。  默认值：当前组件主轴大小减去8vp空白区  **说明：**  不支持设置百分比。 |

### halfHeight

PhonePC/2in1TabletTVWearable

halfHeight(value: number | string)

指定PanelMode.Half状态下的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Half状态下的高度。  默认值：当前组件主轴大小的一半。  **说明：**  不支持设置百分比。 |

### miniHeight

PhonePC/2in1TabletTVWearable

miniHeight(value: number | string)

指定PanelMode.Mini状态下的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 指定PanelMode.Mini状态下的高度。  默认值：48  单位：vp  **说明：**  不支持设置百分比。 |

### show

PhonePC/2in1TabletTVWearable

show(value: boolean)

当滑动面板弹出时调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当滑动面板弹出时调用，true显示面板，false不显示面板。  默认值：true  **说明：**  该属性的优先级高于参数show。 |

### backgroundMask9+

PhonePC/2in1TabletTVWearable

backgroundMask(color: ResourceColor)

指定Panel的背景蒙层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 指定Panel的背景蒙层。  默认值：'#08182431' |

### showCloseIcon10+

PhonePC/2in1TabletTVWearable

showCloseIcon(value: boolean)

设置是否显示关闭图标。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否显示关闭图标，true表示显示，false表示不显示。  默认值：false |

## PanelType枚举说明

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| Minibar | 提供minibar和类全屏展示切换效果。 |
| Foldable | 内容永久展示类，提供大（类全屏）、中（类半屏）、小三种尺寸展示切换效果。 |
| Temporary | 内容临时展示区，提供大（类全屏）、中（类半屏）两种尺寸展示切换效果。 |
| CUSTOM10+ | 配置自适应内容高度，不支持尺寸切换效果。 |

## PanelMode枚举说明

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Mini | 0 | 类型为minibar和foldable时，为最小状态；类型为temporary，则不生效。 |
| Half | 1 | 类型为foldable和temporary时，为类半屏状态；类型为minibar，则不生效。 |
| Full | 2 | 类全屏状态。 |

## PanelHeight10+枚举说明

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| WRAP\_CONTENT | 类型为CUSTOM时，自适应内容高度。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(event: (width: number, height: number, mode: PanelMode) => void)

当可滑动面板发生状态变化时触发。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 内容区的宽度值。 |
| height | number | 是 | 内容区的高度值。  当dragBar属性为true时，panel本身的高度值为dragBar高度加上内容区高度。 |
| mode | PanelMode | 是 | 面板的状态。 |

### onHeightChange9+

PhonePC/2in1TabletTVWearable

onHeightChange(callback: (value: number) => void)

当可滑动面板发生高度变化时触发。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区的高度值，默认返回值单位为px。  当dragBar属性为true时，panel本身的高度值为dragBar高度加上内容区高度。  因用户体验设计原因，panel最高只能滑到 fullHeight-8vp。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PanelExample {
5. @State show: boolean = false

7. build() {
8. Column() {
9. Text('2021-09-30    Today Calendar: 1.afternoon......Click for details')
10. .width('90%')
11. .height(50)
12. .borderRadius(10)
13. .backgroundColor(0xFFFFFF)
14. .padding({ left: 20 })
15. .onClick(() => {
16. this.show = !this.show
17. })
18. Panel(this.show) { // 展示日程
19. Column() {
20. Text('Today Calendar')
21. Divider()
22. Text('1. afternoon 4:00 The project meeting')
23. }
24. }
25. .type(PanelType.Foldable)
26. .mode(PanelMode.Half)
27. .dragBar(true) // 默认开启
28. .halfHeight(500) // 默认一半
29. .showCloseIcon(true) // 显示关闭图标
30. .onChange((width: number, height: number, mode: PanelMode) => {
31. console.info(`width:${width},height:${height},mode:${mode}`)
32. })
33. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/qEoeltmvRx6u58Bpe2uLFA/zh-cn_image_0000002589326557.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055311Z&HW-CC-Expire=86400&HW-CC-Sign=76B39C9FC39F8BA01E14AE98D1CA8628C0E4BA4F75463FEBC908D993759E7165)
