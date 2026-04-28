---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol
title: GridCol
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 栅格与分栏 > GridCol
category: harmonyos-references
scraped_at: 2026-04-28T08:01:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ecd70600c1fb92dd401610d81edb40ed64ac1eb8e3f3015245bef5b596d8d8ee
---

栅格子组件，必须作为栅格容器组件([GridRow](ts-container-gridrow.md))的子组件使用。

说明

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

GridCol(option?: GridColOptions)

栅格列布局组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| option | [GridColOptions](ts-container-gridcol.md#gridcoloptions对象说明) | 否 | 栅格布局子组件参数。 |

## GridColOptions对象说明

PhonePC/2in1TabletTVWearable

设置栅格列布局组件布局选项。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| span | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 否 | 是 | 栅格子组件占用栅格容器组件的列数。span为0表示该元素不参与布局计算，即不会被渲染。  取值为非负整数，默认值为1  非法值：按默认值处理。 |
| offset | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 否 | 是 | 栅格子组件相对于原本位置偏移的列数。  取值为非负整数，默认值为0  非法值：按默认值处理。 |
| order | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 否 | 是 | 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。  取值为非负整数，默认值为0。  非法值：按默认值处理。  **说明：**  当子组件不设置order或者设置相同的order，子组件按照代码顺序展示。  当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。 |

span、offset、order属性按照xs、sm、md、lg、xl、xxl的顺序具有“继承性”，未设置值的断点将会从前一个断点取值。

API version 20之后，span的继承规则见[GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption)。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### span

PhonePC/2in1TabletTVWearable

span(value: number | GridColColumnOption)

设置占用列数。span为0，意味着该元素不参与布局计算，即不会被渲染。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 是 | 占用列数。  取值为非负整数，默认值为1。  非法值：按默认值处理。 |

### gridColOffset

PhonePC/2in1TabletTVWearable

gridColOffset(value: number | GridColColumnOption)

设置相对于前一个栅格子组件偏移的列数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 是 | 相对于前一个栅格子组件偏移的列数。  取值为非负整数，默认值：0  非法值：按默认值处理。 |

### order

PhonePC/2in1TabletTVWearable

order(value: number | GridColColumnOption)

设置栅格子组件的序号，根据序号从小到大对栅格子组件进行排序。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [GridColColumnOption](ts-container-gridcol.md#gridcolcolumnoption) | 是 | 元素的序号，根据栅格子组件的序号，从小到大对栅格子组件做排序。  取值为非负整数，默认值：0  非法值：按默认值处理。 |

## GridColColumnOption

PhonePC/2in1TabletTVWearable

用于自定义指定在不同宽度设备类型上，栅格子组件占据的栅格数量单位。

* API version 20之前，仅配置部分断点下GridCol组件所占列数，取已配置的更小断点的列数补全未配置的列数。若未配置更小断点的列数，取默认值1。

  ```
  1. span: {xs:2, md:4, lg:8} // 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
  2. span: {md:4, lg:8} // 等于配置 span: {xs:1, sm:1, md:4, lg:8, xl:8, xxl:8}
  ```
* API version 20及以后，仅配置部分断点下GridCol组件所占列数，取已配置的更小断点的列数补全未配置的列数。若未配置更小断点的列数，取已配置的更大断点的列数补全未配置的列数。

  ```
  1. span: {xs:2, md:4, lg:8} // 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}
  2. span: {md:4, lg:8} // 等于配置 span: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8}
  ```
* 建议手动配置不同断点下GridCol组件所占列数，避免默认补全列数的布局效果不符合预期。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xs | number | 否 | 是 | 在栅格大小为xs的设备上，栅格容器组件的栅格列数。 |
| sm | number | 否 | 是 | 在栅格大小为sm的设备上，栅格容器组件的栅格列数。 |
| md | number | 否 | 是 | 在栅格大小为md的设备上，栅格容器组件的栅格列数。 |
| lg | number | 否 | 是 | 在栅格大小为lg的设备上，栅格容器组件的栅格列数。 |
| xl | number | 否 | 是 | 在栅格大小为xl的设备上，栅格容器组件的栅格列数。 |
| xxl | number | 否 | 是 | 在栅格大小为xxl的设备上，栅格容器组件的栅格列数。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

GridCol的基本用法示例。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridColExample {
5. @State bgColors: Color[] =
6. [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]
7. @State currentBp: string = 'unknown'

9. build() {
10. Column() {
11. GridRow({
12. columns: 5,
13. gutter: { x: 5, y: 10 },
14. breakpoints: {
15. value: ['400vp', '600vp', '800vp'],
16. reference: BreakpointsReference.WindowSize
17. },
18. direction: GridRowDirection.Row
19. }) {
20. ForEach(this.bgColors, (color: Color) => {
21. GridCol({
22. span: { xs: 1, sm: 2, md: 3, lg: 4 },
23. offset: 0,
24. order: 0
25. }) {
26. Row().width('100%').height('20vp')
27. }.borderColor(color).borderWidth(2)
28. })
29. }.width('100%').height('100%')
30. .onBreakpointChange((breakpoint) => {
31. this.currentBp = breakpoint
32. })
33. }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200)
34. .border({ color: '#880606', width: 2 })
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Uw-SaTrnRkGA4kS4EEiC5g/zh-cn_image_0000002583439647.png?HW-CC-KV=V1&HW-CC-Date=20260428T000125Z&HW-CC-Expire=86400&HW-CC-Sign=39E55980102868727AF9D9CDE3D2A233172A0A5FF2C66E9F3164AF730C5C1621)
