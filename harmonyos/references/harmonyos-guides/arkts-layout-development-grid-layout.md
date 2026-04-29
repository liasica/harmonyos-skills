---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout
title: 栅格布局 (GridRow/GridCol)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 栅格布局 (GridRow/GridCol)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:42+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:969e443d8417712974a13c943e8d1a9152983b698308896ef8778086252f8ab4
---

## 概述

栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

[GridRow](../harmonyos-references/ts-container-gridrow.md)为栅格容器组件，需与栅格子组件[GridCol](../harmonyos-references/ts-container-gridcol.md)在栅格布局场景中联合使用。

## 栅格容器GridRow

### 栅格容器断点

栅格容器以设备的水平宽度（[像素单位](../harmonyos-references/ts-pixel-units.md)，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。

栅格容器默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：

| 断点名称 | 取值范围（vp） | 设备描述 |
| --- | --- | --- |
| xs | [0, 320） | 最小宽度类型设备。 |
| sm | [320, 600) | 小宽度类型设备。 |
| md | [600, 840) | 中等宽度类型设备。 |
| lg | [840, +∞) | 大宽度类型设备。 |

在GridRow栅格组件中，允许开发者使用[BreakPoints](../harmonyos-references/ts-container-gridrow.md#breakpoints)自定义修改断点的取值范围，最多支持6个断点，除了默认的4个断点外，还可以启用xl和xxl断点，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的布局设置。

| 断点名称 | 设备描述 |
| --- | --- |
| xs | 最小宽度类型设备。 |
| sm | 小宽度类型设备。 |
| md | 中等宽度类型设备。 |
| lg | 大宽度类型设备。 |
| xl | 特大宽度类型设备。 |
| xxl | 超大宽度类型设备。 |

* 开发者可根据实际使用场景，通过一个单调递增数组设置断点位置。由于栅格容器默认支持4个断点，在不设置断点位置时，系统为默认断点配置的单调递增数组为["320vp", "600vp", "840vp"]。开发者使用[BreakPoints](../harmonyos-references/ts-container-gridrow.md#breakpoints)最多可支持6个断点，因此此单调递增数组最大长度为5。

  假设传入的数组是[n0, n1, n2, n3, n4]，则各个断点取值如下：

  | 断点 | 取值范围 |
  | --- | --- |
  | xs | [0, n0) |
  | sm | [n0, n1) |
  | md | [n1, n2) |
  | lg | [n2, n3) |
  | xl | [n3, n4) |
  | xxl | [n4, INF) |

  ```
  1. breakpoints: {value: ['100vp', '200vp']} // 表示xs、sm、md共3个断点被使用，小于100vp为xs，100vp-200vp为sm，大于200vp为md。
  2. breakpoints: {value: ['320vp', '600vp']} // 表示xs、sm、md共3个断点被使用，小于320vp为xs，320vp-600vp为sm，大于600vp为md。
  3. breakpoints: {value: ['320vp', '600vp', '840vp', '1440vp']} // 表示xs、sm、md、lg、xl共5个断点被使用，小于320vp为xs，320vp-600vp为sm，  600vp-840vp为md，840vp-1440vp为lg，大于1440vp为xl。
  ```
* 栅格容器通过监听窗口或容器的尺寸变化进行断点，通过[reference](../harmonyos-references/ts-container-gridrow.md#breakpoints)设置断点切换参考物。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。

  例如，通过断点设置将应用宽度分成6个区间，通过[columns](../harmonyos-references/ts-container-gridrow.md#gridrowoptions对象说明)配置各断点下栅格容器的栅格列数。

  ```
  1. @Entry
  2. @Component
  3. struct WindowRefGridLayout {
  4. @State currentBp: string = "unknown"
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. Column({ space: 6 }) {
  11. Text(this.currentBp)

  13. GridRow({
  14. columns: {
  15. xs: 2, // 窗口宽度落入xs断点上，栅格容器分为2列。
  16. sm: 4, // 窗口宽度落入sm断点上，栅格容器分为4列。
  17. md: 8, // 窗口宽度落入md断点上，栅格容器分为8列。
  18. lg: 12, // 窗口宽度落入lg断点上，栅格容器分为12列。
  19. xl: 12, // 窗口宽度落入xl断点上，栅格容器分为12列。
  20. xxl: 12 // 窗口宽度落入xxl断点上，栅格容器分为12列。
  21. },
  22. breakpoints: {
  23. value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'], // 表示在保留默认断点['320vp', '600vp', '840vp']的同时自定义增加'1440vp', '1600vp'的断点，实际开发中需要根据实际使用场景，合理设置断点值实现一次开发多端适配。
  24. reference: BreakpointsReference.WindowSize
  25. }
  26. }) {
  27. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
  28. GridCol({ span: 1 }) { // 所有子组件占一列。
  29. Row() {
  30. Text(`${index}`)
  31. }.width('100%').height('50vp')
  32. }.backgroundColor(color)
  33. })
  34. }
  35. .height(200)
  36. .border({ color: 'rgb(39,135,217)', width: 2 })
  37. .onBreakpointChange((breakPoint) => {
  38. this.currentBp = breakPoint
  39. })
  40. }
  41. }
  42. }
  ```

  [GridLayoutReference.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutReference.ets#L15-L48)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/jc_Xc08_Rky1hxjcSbs9oA/zh-cn_image_0000002589324097.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=E26BABA072AAC1AD95446E8D5B884B5EC510C86A13B313E5E216F2C0057F6CD1)

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

* API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
* API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct GridColumnsWithDefaults {
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)', 'rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)'];

  9. build() {
  10. GridRow() {
  11. ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {
  12. GridCol({ span: 1 }) {
  13. Row() {
  14. Text(`${index}`)
  15. }.width('100%').height('50')
  16. }.backgroundColor(item)
  17. })
  18. }
  19. }
  20. }
  ```

  [GridLayoutColumns.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumns.ets#L15-L36)

  API version 20之前布局显示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/-28TfmS3QKaXfkA0T4jrdQ/zh-cn_image_0000002589244037.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=185385DE8A39C117C1B7B4C8423EBA8F3BF29F0B0AE28F3A6EFF88216F97FE04)

  API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/_kPdpw1tSom5VuffNa-Qcw/zh-cn_image_0000002558764230.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=18CC2BB49B12478B8257A1703098F0F3C1380B27DA6A0EC94E4030C9AEDEB837)

columns支持number和[GridRowColumnOption](../harmonyos-references/ts-container-gridrow.md#gridrowcolumnoption)两种类型, 可按两种方式设置栅格布局的总列数。

* 当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下：

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct FixedFourColumnGrid {
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. Column({ space: 6 }) {
  11. Text('columns：4').alignSelf(ItemAlign.Start)

  13. Row() {
  14. GridRow({ columns: 4 }) {
  15. ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {
  16. GridCol({ span: 1 }) {
  17. Row() {
  18. Text(`${index}`)
  19. }.width('100%').height('50')
  20. }.backgroundColor(item)
  21. })
  22. }
  23. .width('100%').height('100%')
  24. }
  25. .height(160)
  26. .border({ color: 'rgb(39,135,217)', width: 2 })
  27. .width('90%')
  28. }
  29. }
  30. }
  ```

  [GridLayoutColumnsToFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnsToFour.ets#L15-L42)

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct FixedEightColumnGrid {
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. Column({ space: 6 }) {
  11. Text('columns：8').alignSelf(ItemAlign.Start)

  13. Row() {
  14. GridRow({ columns: 8 }) {
  15. ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {
  16. GridCol({ span: 1 }) {
  17. Row() {
  18. Text(`${index}`)
  19. }.width('100%').height('50')
  20. }.backgroundColor(item)
  21. })
  22. }
  23. .width('100%').height('100%')
  24. }
  25. .height(160)
  26. .border({ color: 'rgb(39,135,217)', width: 2 })
  27. .width('90%')
  28. }
  29. }
  30. }
  ```

  [GridLayoutColumnsToEight.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnsToEight.ets#L15-L42)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/naHlr342SJ6TDhW7akdTzw/zh-cn_image_0000002558604574.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=0B1AEE8ED36A56BB970B2809403BB2C6D5B21F4E03063D9A24D6EF7AF032CC6E)
* 当columns类型为[GridRowColumnOption](../harmonyos-references/ts-container-gridrow.md#gridrowcolumnoption)时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。

  ```
  1. @Entry
  2. @Component
  3. struct GridRowColumnOptionLayout {
  4. @State bgColors: ResourceColor[] =
  5. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  6. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  8. build() {
  9. GridRow({
  10. columns: { sm: 4, md: 8 },
  11. breakpoints: {
  12. value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'] // 表示在保留默认断点['320vp', '600vp', '840vp']的同时自定义增加'1440vp', '1600vp'的断点，实际开发中需要根据实际使用场景，合理设置断点值实现一次开发多端适配。
  13. }
  14. }) {
  15. ForEach(this.bgColors, (item: ResourceColor, index?: number | undefined) => {
  16. GridCol({ span: 1 }) {
  17. Row() {
  18. Text(`${index}`)
  19. }.width('100%').height('50')
  20. }.backgroundColor(item)
  21. })
  22. }
  23. .height(200)
  24. .border({ color: 'rgb(39,135,217)', width: 2 })
  25. }
  26. }
  ```

  [GridLayoutColumnOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnOption.ets#L15-L42)

  API version 20之前布局显示（xs设备未配置栅格列数，取默认列数12）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/JJfxow1IRtGzFJsmsdCjew/zh-cn_image_0000002589324099.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=0F1B504F145416E0813EA052659890CDCE77214322EE950D17A283E9D943B625)

  API version 20及以后布局显示（xs设备继承sm设备栅格列数）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/HdL7PBp6RzSY_XNtaEU8cg/zh-cn_image_0000002589244039.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=1BF35A5855FD1B926BAC46AB4AE7A3C02CCFCB564560C0729258926C17F619B7)

  仅部分设置sm、md的栅格列数，未配置的xs、lg、xl、xxl设备根据[栅格列数补全](../harmonyos-references/ts-container-gridrow.md#gridrowcolumnoption)取默认值。

### 排列方向

栅格布局中，可以通过设置GridRow的[direction](../harmonyos-references/ts-container-gridrow.md#gridrowoptions对象说明)属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为[GridRowDirection](../harmonyos-references/ts-container-gridrow.md#gridrowdirection枚举说明).Row（从左往右排列）或[GridRowDirection](../harmonyos-references/ts-container-gridrow.md#gridrowdirection枚举说明).RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

* 子组件默认从左往右排列。

  ```
  1. GridRow({ direction: GridRowDirection.Row }) { /* ... */ }
  ```

  [GridLayoutDirectionRow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutDirectionRow.ets#L21-L23)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/q7ZyLxW-S42snuX7M0HJtw/zh-cn_image_0000002558764232.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=A4F5312EB83E917F359B1F7E82CCF1D14C801BA9D93B6E7A564EA9E229948685)
* 子组件从右往左排列。

  ```
  1. GridRow({ direction: GridRowDirection.RowReverse }) { /* ... */ }
  ```

  [GridLayoutDirectionRowReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutDirectionRowReverse.ets#L21-L23)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/b5wLp0gxSBm2JIfEU3k8sQ/zh-cn_image_0000002558604576.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=3F7FFA538D76BA1FAD1C26C1E0450E9177D81354726C3E057B40BD869AC97813)

### 子组件间距

GridRow中通过[gutter](../harmonyos-references/ts-container-gridrow.md#gridrowoptions对象说明)属性设置子元素在水平和垂直方向的间距。

* 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。

  ```
  1. GridRow({ gutter: 10 }) { /* ... */ }
  ```

  [GridLayoutGutterToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutGutterToNumber.ets#L21-L23)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/AbviaL8zSC6SL8kvQs0yfQ/zh-cn_image_0000002589324101.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=7851E102F9E70E80CD8E19E61CB70BA7EB046BA3EC86DA2881EAFA0963EC362B)
* 当gutter类型为[GutterOption](../harmonyos-references/ts-container-gridrow.md#gutteroption)时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。

  ```
  1. GridRow({ gutter: { x: 20, y: 50 } }) { /* ... */ }
  ```

  [GridLayoutGutterOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutGutterOption.ets#L21-L23)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/OBqwkZDCSR6LlzPz8YDs5w/zh-cn_image_0000002589244041.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=65DB5CB3DFF3636D7E36F65C096E78B66DC362E3357A27481B2BFA554262CABB)

## 子组件GridCol

[GridCol](../harmonyos-references/ts-container-gridcol.md)组件作为[GridRow](../harmonyos-references/ts-container-gridrow.md)组件的子组件，通过给GridCol传参或者设置属性两种方式，设置[span](../harmonyos-references/ts-container-gridcol.md#gridcoloptions对象说明)（占用列数），[offset](../harmonyos-references/ts-container-gridcol.md#gridcoloptions对象说明)（偏移列数），[order](../harmonyos-references/ts-container-gridcol.md#gridcoloptions对象说明)（元素序号）的值。

* 设置span。

  ```
  1. let gSpan:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
  ```

  [GridColSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpan.ets#L15-L17)

  ```
  1. GridCol({ span: 2 }){}
  2. GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){}
  3. GridCol(){}.span(2)
  4. GridCol(){}.span(gSpan)
  ```

  [GridColSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpan.ets#L24-L29)
* 设置offset。

  ```
  1. let gOffset:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
  ```

  [GridColOffset.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffset.ets#L15-L17)

  ```
  1. GridCol({ offset: 2, span: 1 }){}
  2. GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 }, span: 1 }){}
  3. GridCol({ span: 1 }){}.offset(gOffset)
  ```

  [GridColOffset.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffset.ets#L24-L28)
* 设置order。

  ```
  1. let gOrder:Record<string,number> = { 'xs': 1, 'sm': 2, 'md': 3, 'lg': 4 }
  ```

  [GridColOrder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrder.ets#L15-L17)

  ```
  1. GridCol({ order: 2, span: 1 }){}
  2. GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 }, span: 1 }){}
  3. GridCol({ span: 1 }){}.order(2)
  4. GridCol({ span: 1 }){}.order(gOrder)
  ```

  [GridColOrder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrder.ets#L24-L29)

### span

子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。

span支持number和[GridColColumnOption](../harmonyos-references/ts-container-gridcol.md#gridcolcolumnoption)两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。

* 当span类型为number时，子组件在所有尺寸设备下占用的列数相同。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct SpanNumberExample {
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. GridRow({ columns: 8 }) {
  11. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
  12. GridCol({ span: 2 }) {
  13. Row() {
  14. Text(`${index}`)
  15. }.width('100%').height('50vp')
  16. }
  17. .backgroundColor(color)
  18. })
  19. }
  20. .border({ color: 'rgb(39,135,217)', width: 2 })
  21. .height('150vp')
  22. }
  23. }
  ```

  [GridColSpanToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpanToNumber.ets#L15-L37)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/EJnIg883TO2Rv3Giw-VWJA/zh-cn_image_0000002558764234.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=EE7E2BEC184AD211040A04E0728E59CD18698680BC979467AFE7A06EB2BD4678)
* 当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据[列数补全](../harmonyos-references/ts-container-gridcol.md#gridcolcolumnoption)取默认值。

  ```
  1. @Entry
  2. @Component
  3. struct SpanColumnOptionExample {
  4. @State currentBp: string = "unknown"
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. Column({ space: 6 }) {
  11. GridRow({ columns: 8 }) {
  12. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
  13. GridCol({
  14. span: {
  15. xs: 1,
  16. sm: 2,
  17. md: 3,
  18. lg: 4
  19. }
  20. }) {
  21. Row() {
  22. Text(`${index}`)
  23. }.width('100%').height('50vp')
  24. }
  25. .backgroundColor(color)
  26. })
  27. }
  28. .border({ color: 'rgb(39,135,217)', width: 2 })
  29. .height('150vp')
  30. .onBreakpointChange((breakPoint) => {
  31. this.currentBp = breakPoint
  32. })

  34. Text(this.currentBp)
  35. }
  36. }
  37. }
  ```

  [GridColSpanToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpanToOption.ets#L15-L36)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/9HbIlUppTfa23JFlFsDWTg/zh-cn_image_0000002558604578.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=C9CB57F4943BE0EB81B42D6966E95D1A8C36BCBE3104720D9B173EABB5EA2719)

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

* 当offset类型为number时，子组件偏移相同列数。

  ```
  1. @Entry
  2. @Component
  3. struct OffsetNumberExample {
  4. @State bgColors: ResourceColor[] =
  5. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  6. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  8. build() {
  9. Column() {
  10. GridRow({ columns: 12 }) {
  11. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
  12. GridCol({ offset: 2, span: 1 }) {
  13. Row() {
  14. Text('' + index)
  15. }.width('100%').height('50vp')
  16. }
  17. .backgroundColor(color)
  18. })
  19. }

  21. Blank().width('100%').height(150)
  22. }.border({ color: 'rgb(39,135,217)', width: 2 })
  23. }
  24. }
  ```

  [GridColOffsetToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffsetToNumber.ets#L15-L36)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/oK7_8P4pSjyIzE0esAR6mA/zh-cn_image_0000002589324103.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=D4D5DFFDD58E4CF1FD26E418782CDBAB72D7974558BB5CD5B383D9E6B8E8D66B)

  在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
* 当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。

  ```
  1. @Entry
  2. @Component
  3. struct OffsetColumnOptionExample {
  4. @State currentBp: string = "unknown"
  5. @State bgColors: ResourceColor[] =
  6. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
  7. 'rgb(255,192,0)', 'rgb(170,10,33)'];

  9. build() {
  10. Column({ space: 6 }) {
  11. GridRow({ columns: 12 }) {
  12. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
  13. GridCol({
  14. offset: {
  15. xs: 1,
  16. sm: 2,
  17. md: 3,
  18. lg: 4
  19. },
  20. span: 1
  21. }) {
  22. Row() {
  23. Text('' + index)
  24. }.width('100%').height('50vp')
  25. }
  26. .backgroundColor(color)
  27. })
  28. }
  29. .height(200)
  30. .border({ color: 'rgb(39,135,217)', width: 2 })
  31. .onBreakpointChange((breakPoint) => {
  32. this.currentBp = breakPoint
  33. })

  35. Text(this.currentBp)
  36. }
  37. }
  38. }
  ```

  [GridColOffsetToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffsetToOption.ets#L15-L38)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/wFSTrr2KSWO361kDXBdKUg/zh-cn_image_0000002589244043.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=D17F35F62CA1A8D8B9556C1BA9C30450C86A8534D6DEC17FA54997940E7071F3)

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

* 当order类型为number时，子组件在任何尺寸下排序次序一致。

  ```
  1. GridRow({ columns: 12 }) {
  2. GridCol({ order: 4, span: 1 }) {
  3. Row() {
  4. Text('1')
  5. }.width('100%').height('50vp')
  6. }.backgroundColor('rgb(213,213,213)')

  8. GridCol({ order: 3, span: 1 }) {
  9. Row() {
  10. Text('2')
  11. }.width('100%').height('50vp')
  12. }.backgroundColor('rgb(150,150,150)')

  14. GridCol({ order: 2, span: 1 }) {
  15. Row() {
  16. Text('3')
  17. }.width('100%').height('50vp')
  18. }.backgroundColor('rgb(0,74,175)')

  20. GridCol({ order: 1, span: 1 }) {
  21. Row() {
  22. Text('4')
  23. }.width('100%').height('50vp')
  24. }.backgroundColor('rgb(39,135,217)')
  25. }.border({ width: 1, color: 'rgb(39,135,217)' }).height('200vp')
  ```

  [GridColOrderToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrderToNumber.ets#L20-L46)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/wJhTMzZjR6yq9v2uTOqthg/zh-cn_image_0000002558764236.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=93DE2D994504B71A9C0DC3B442EF8E23D50A9C030187C36ED8C3BD80949D7F8B)
* 当order类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。

  ```
  1. @Entry
  2. @Component
  3. struct OrderColumnOptionExample {
  4. @State currentBp: string = 'unknown'

  6. build() {
  7. Column({ space: 5 }) {
  8. GridRow({ columns: 12 }) {
  9. GridCol({
  10. order: { xs: 1, sm: 5, md: 3, lg: 7 }, span: 1 }) {
  11. Row() {
  12. Text('1')
  13. }.width('100%').height('50vp')
  14. }.backgroundColor('rgb(213,213,213)')

  16. GridCol({
  17. order: { xs: 2, sm: 2, md: 6, lg: 1 }, span: 1 }) {
  18. Row() {
  19. Text('2')
  20. }.width('100%').height('50vp')
  21. }.backgroundColor('rgb(150,150,150)')

  23. GridCol({ order: { xs: 3, sm: 3, md: 1, lg: 6 }, span: 1 }) {
  24. Row() {
  25. Text('3')
  26. }.width('100%').height('50vp')
  27. }.backgroundColor('rgb(0,74,175)')

  29. GridCol({ order: { xs: 4, sm: 4, md: 2, lg: 5 }, span: 1 }) {
  30. Row() {
  31. Text('4')
  32. }.width('100%').height('50vp')
  33. }.backgroundColor('rgb(39,135,217)')
  34. }.border({ width: 1, color: 'rgb(39,135,217)' }).height('200vp').onBreakpointChange((breakpoint) => {
  35. this.currentBp = breakpoint
  36. })

  38. Text(this.currentBp)
  39. }
  40. }
  41. }
  ```

  [GridColOrderToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrderToOption.ets#L15-L57)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/7XG9cSSrR_qhIrgg8wRyVA/zh-cn_image_0000002558604580.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=20A60808D1D82CCF278DA1FC637109CFE4CC05CFD649F13A894B0617DF382084)

## 栅格组件的嵌套使用

栅格组件也可以嵌套使用，完成一些复杂的布局。

以下示例中，栅格把整个空间分为12份。第一层GridRow嵌套GridCol，分为中间大区域以及“footer”区域。第二层GridRow嵌套GridCol，分为“left”和“right”区域。子组件空间按照上一层父组件的空间划分，粉色的区域是屏幕空间的12列，绿色和蓝色的区域是父组件GridCol的12列，依次进行空间的划分。

```
1. @Entry
2. @Component
3. struct GridRowExample {
4. build() {
5. GridRow({ columns: 12 }) {
6. GridCol({ span: 12 }) {
7. GridRow({ columns: 12 }) {
8. GridCol({ span: 2 }) {
9. Row() {
10. Text('left').fontSize(24)
11. }
12. .justifyContent(FlexAlign.Center)
13. .height('90%')
14. }.backgroundColor('#ff41dbaa')

16. GridCol({ span: 10 }) {
17. Row() {
18. Text('right').fontSize(24)
19. }
20. .justifyContent(FlexAlign.Center)
21. .height('90%')
22. }.backgroundColor('#ff4168db')
23. }
24. .backgroundColor('#19000000')
25. }

27. GridCol({ span: 12 }) {
28. Row() {
29. Text('footer').width('100%').textAlign(TextAlign.Center)
30. }.width('100%').height('10%').backgroundColor(Color.Pink)
31. }
32. }.width('100%').height(300)
33. }
34. }
```

[GridRowExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridRowExample.ets#L15-L50)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/niS5oNr0T16867QeLVYccQ/zh-cn_image_0000002589324105.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=EF5E7C9C3A4CBFADD74E4493F1955B49DA5635170D9E9387CBB490EEC6DEDF05)

综上所述，栅格组件提供了丰富的自定义能力，功能非常灵活和强大。只需要明确栅格在不同断点下的[columns](../harmonyos-references/ts-container-gridrow.md#gridrowoptions对象说明)、[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)、[gutter](../harmonyos-references/ts-container-gridrow.md#gridrowoptions对象说明)及[span](../harmonyos-references/ts-container-gridcol.md#gridcoloptions对象说明)等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。
