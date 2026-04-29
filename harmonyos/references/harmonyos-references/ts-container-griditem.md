---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem
title: GridItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > GridItem
category: harmonyos-references
scraped_at: 2026-04-29T13:51:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c2cf5deb6536b1e31f924bf3a387f378be69be8486eee6b4cfcd8149c2ba57b
---

网格容器中单项内容容器。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 仅支持作为[Grid](ts-container-grid.md)组件的子组件使用。
* 当GridItem配合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)使用时，GridItem子组件在GridItem创建时创建。配合[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)使用时，或父组件为Grid时，GridItem子组件在GridItem布局时创建。
* 当Grid中存在大量GridItem时，使用[columnStart](ts-container-griditem.md#columnstart)/[columnEnd](ts-container-griditem.md#columnend)、[rowStart](ts-container-griditem.md#rowstart)/[rowEnd](ts-container-griditem.md#rowend)设置GridItem大小会导致在使用scrollToIndex滑动到指定Index时，依次遍历GridItem节点，耗时较长。建议使用[GridLayoutOptions](ts-container-grid.md#gridlayoutoptions10对象说明)布局，以提高查找GridItem位置的效率。最佳实践请参考[优化Grid组件加载慢丢帧问题](../best-practices/bpta-improve_grid_performance.md)。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

GridItem(value?: GridItemOptions)

创建网格容器中单项内容容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value11+ | [GridItemOptions](ts-container-griditem.md#griditemoptions11对象说明) | 否 | 为GridItem提供可选参数，该对象内含有[GridItemStyle](ts-container-griditem.md#griditemstyle11枚举说明)枚举类型的style参数。 |

## 属性

PhonePC/2in1TabletTVWearable

### rowStart

PhonePC/2in1TabletTVWearable

rowStart(value: number)

设置当前元素起始行号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素起始行号。  需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。  取值范围：[0, 总行数-1] |

### rowEnd

PhonePC/2in1TabletTVWearable

rowEnd(value: number)

设置当前元素终点行号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素终点行号。  需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。  取值范围：[0, 总行数-1] |

### columnStart

PhonePC/2in1TabletTVWearable

columnStart(value: number)

设置当前元素起始列号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素起始列号。  需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。  取值范围：[0, 总列数-1] |

### columnEnd

PhonePC/2in1TabletTVWearable

columnEnd(value: number)

设置当前元素终点列号。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前元素终点列号。  需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。  取值范围：[0, 总列数-1] |

需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。

起始行号、终点行号、起始列号、终点列号生效规则如下：

* rowStart/rowEnd合理取值范围为0~总行数-1，columnStart/columnEnd合理取值范围为0~总列数-1。
* 如果设置了rowStart/rowEnd/columnStart/columnEnd，GridItem会占据指定的行数(rowEnd-rowStart+1)或列数(columnEnd-columnStart+1)。
* 只有在设置columnsTemplate和rowsTemplate的Grid中，设置合理的rowStart/rowEnd/columnStart/columnEnd四个属性的GridItem才能按照指定的行列号布局。
* 在设置columnsTemplate和rowsTemplate的Grid中，单独设置行号rowStart/rowEnd或列号columnStart/columnEnd的GridItem会按照一行一列进行布局。
* 在只设置columnsTemplate的Grid中设置列号columnStart/columnEnd的GridItem按照列数布局。在该区域位置存在GridItem布局，则直接换行进行放置。
* 在只设置rowsTemplate的Grid中设置行号rowStart/rowEnd的GridItem按照行数布局。在该区域位置存在GridItem布局，则直接换列进行放置。
* columnsTemplate和rowsTemplate都不设置的Grid中GridItem的行列号属性无效。

以下是GridItem行列号异常值的处理规则：

| 属性设置情况 | 异常类型 | 修正后布局规则 |
| --- | --- | --- |
| 仅设置columnsTemplate | 任意行列异常 | 按一行一列布局。 |
| 仅设置rowsTemplate | 任意行列异常 | 按一行一列布局。 |
| 同时设置rows/columnsTemplate | rowStart < rowEnd | 行跨度 = min(rowEnd-rowStart+1, 总行数)。 |
| 同时设置rows/columnsTemplate | rowStart > rowEnd | 按一行一列布局。 |
| 同时设置rows/columnsTemplate | columnStart < columnEnd | 列跨度 = min(columnEnd-columnStart+1, 总列数)。 |
| 同时设置rows/columnsTemplate | columnStart > columnEnd | 按一行一列布局。 |

### forceRebuild(deprecated)

PhonePC/2in1TabletTVWearable

forceRebuild(value: boolean)

设置在触发组件build时是否重新创建此节点。

说明

从API version 7开始支持，从API version 9开始废弃。GridItem会根据自身属性和子组件变化自行决定是否需要重新创建，无需设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 在触发组件build时是否重新创建此节点。  默认值：false |

### selectable8+

PhonePC/2in1TabletTVWearable

selectable(value: boolean)

设置当前GridItem元素是否可以被鼠标框选。外层Grid容器的鼠标框选开启时，GridItem的框选才生效。

该属性需要在设置[多态样式](ts-universal-attributes-polymorphic-style.md)前使用才能生效选中态样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前GridItem元素是否可以被鼠标框选。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。  默认值：true |

### selected10+

PhonePC/2in1TabletTVWearable

selected(value: boolean)

设置当前GridItem选中状态。该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

该属性需要在设置[多态样式](ts-universal-attributes-polymorphic-style.md)前使用才能生效选中态样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前GridItem选中状态。设置为true时为选中状态，设置为false时为默认状态。  默认值：false |

## GridItemOptions11+对象说明

PhonePC/2in1TabletTVWearable

GridItem样式对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [GridItemStyle](ts-container-griditem.md#griditemstyle11枚举说明) | 否 | 是 | 设置GridItem样式。  默认值：GridItemStyle.NONE  设置为GridItemStyle.NONE时无样式。  设置为GridItemStyle.PLAIN时，显示Hover、Press态样式。 |

## GridItemStyle11+枚举说明

PhonePC/2in1TabletTVWearable

GridItem样式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无样式。 |
| PLAIN | 1 | 显示Hover、Press态样式。 |

说明

GridItem焦点态样式设置：Grid组件需要设置4vp规格以上的内边距，用于显示GridItem的焦点框。

## 事件

PhonePC/2in1TabletTVWearable

### onSelect8+

PhonePC/2in1TabletTVWearable

onSelect(event: (isSelected: boolean) => void)

GridItem元素被鼠标框选的状态改变时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | boolean | 是 | 进入鼠标框选范围即被选中返回true， 移出鼠标框选范围即未被选中返回false。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（GridItem设置自身位置）

GridItem通过设置合理的ColumnStart、ColumnEnd、RowStart、RowEnd属性来设置自身位置。需要指定GridItem起始行列号和所占行列数的场景推荐使用[Grid的layoutOptions参数](ts-container-grid.md#gridlayoutoptions10对象说明)，详细可参考[Grid的示例1](ts-container-grid.md#示例1固定行列grid)和[Grid的示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridItemExample {
5. @State numbers: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];

7. build() {
8. Column() {
9. Grid() {
10. GridItem() {
11. Text('4')
12. .fontSize(16)
13. .backgroundColor(0xFAEEE0)
14. .width('100%')
15. .height('100%')
16. .textAlign(TextAlign.Center)
17. }.rowStart(1).rowEnd(2).columnStart(1).columnEnd(2) // 同时设置合理的行列号

19. ForEach(this.numbers, (item: string) => {
20. GridItem() {
21. Text(item)
22. .fontSize(16)
23. .backgroundColor(0xF9CF93)
24. .width('100%')
25. .height('100%')
26. .textAlign(TextAlign.Center)
27. }
28. }, (item: string) => item)

30. GridItem() {
31. Text('5')
32. .fontSize(16)
33. .backgroundColor(0xDBD0C0)
34. .width('100%')
35. .height('100%')
36. .textAlign(TextAlign.Center)
37. }.columnStart(1).columnEnd(4) // 只设置列号，不会从第1列开始布局
38. }
39. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
40. .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
41. .width('90%').height(300)
42. }.width('100%').margin({ top: 5 })
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_GkRUXkYRySFcRtSc4aCcA/zh-cn_image_0000002558766154.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055143Z&HW-CC-Expire=86400&HW-CC-Sign=EE44178900D6FBD1701A56EE6FAB2B2AE143B76050AF1BC69BDF28BE559E3515)

### 示例2（设置GridItem样式）

使用GridItemOptions设置GridItem样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridItemExample {
5. @State numbers: String[] = ['0', '1', '2'];

7. build() {
8. Column({ space: 5 }) {
9. Grid() {
10. ForEach(this.numbers, (day: string) => {
11. ForEach(this.numbers, (day: string) => {
12. GridItem({style:GridItemStyle.NONE}) {
13. Text(day)
14. .fontSize(16)
15. .width('100%')
16. .height('100%')
17. .textAlign(TextAlign.Center)
18. .focusable(true)
19. }
20. .backgroundColor(0xF9CF93)
21. }, (day: string) => day)
22. }, (day: string) => day)
23. }
24. .columnsTemplate('1fr 1fr 1fr')
25. .rowsTemplate('1fr 1fr')
26. .columnsGap(4)
27. .rowsGap(4)
28. .width('60%')
29. .backgroundColor(0xFAEEE0)
30. .height(150)
31. .padding('4vp')

33. Grid() {
34. ForEach(this.numbers, (day: string) => {
35. ForEach(this.numbers, (day: string) => {
36. GridItem({style:GridItemStyle.PLAIN}) {
37. Text(day)
38. .fontSize(16)
39. .width('100%')
40. .height('100%')
41. .textAlign(TextAlign.Center)
42. .focusable(true)
43. }
44. .backgroundColor(0xF9CF93)
45. }, (day: string) => day)
46. }, (day: string) => day)
47. }
48. .columnsTemplate('1fr 1fr 1fr')
49. .rowsTemplate('1fr 1fr')
50. .columnsGap(4)
51. .rowsGap(4)
52. .width('60%')
53. .backgroundColor(0xFAEEE0)
54. .height(150)
55. .padding('4vp')
56. }.width('100%').margin({ top: 5 })
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/FyIgAo4-TLGhvk5VjB5fSw/zh-cn_image_0000002558606496.png?HW-CC-KV=V1&HW-CC-Date=20260429T055143Z&HW-CC-Expire=86400&HW-CC-Sign=A3B1700BEF55A99BEE9389297381B757B97D2A5814F88EE034EA14274C24429F)
