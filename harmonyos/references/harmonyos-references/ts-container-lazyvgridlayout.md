---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvgridlayout
title: LazyVGridLayout
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > LazyVGridLayout
category: harmonyos-references
scraped_at: 2026-04-29T13:51:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aab654a3b1c71d8471dcaa7f4ace4d76c11b79256c7e5b7efecf411f97cd481c
---

该组件用于实现支持懒加载的网格布局，其父组件仅限于[WaterFlow](ts-container-waterflow.md)或[FlowItem](ts-container-flowitem.md)，并支持使用自定义组件、[NodeContainer](ts-basic-components-nodecontainer.md)组件封装后，在WaterFlow或FlowItem组件下应用。

该组件仅在WaterFlow组件的单列模式或分段布局中的单列分段，并且布局方向[FlexDirection](ts-appendix-enums.md#flexdirection)设置为FlexDirection.Column的情况下支持懒加载。在WaterFlow的多列模式或布局方向为FlexDirection.Row或FlexDirection.RowReverse的情况下使用该组件，则不支持懒加载。此外，在布局方向为FlexDirection.ColumnReverse的WaterFlow组件下使用该组件会导致显示异常。当懒加载功能生效时，该组件仅加载WaterFlow显示区域内的子组件，并在帧间空闲时隙预加载显示区域上方和下方各半屏的内容。

说明

* 该组件从API version 19开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* LazyVGridLayout组件高度默认自适应内容，不建议设置高度、高度约束或宽高比，设置后会导致显示异常。

## 接口

PhonePC/2in1TabletTVWearable

LazyVGridLayout()

创建垂直方向懒加载网格布局容器。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### columnsTemplate

PhonePC/2in1TabletTVWearable

columnsTemplate(value: string)

设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第一列占1份，第二列占1份，第三列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包含一个有效列宽。

auto-fit模式和auto-stretch模式只支持track-size为一个有效列宽值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效列宽，如columnsTemplate('repeat(auto-fill, 20)')、columnsTemplate('repeat(auto-fill, 20 80px)')。

设置为'0fr'时，该列的列宽为0，不显示子组件。设置为其他非法值时，子组件显示为固定1列。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局列的数量或最小列宽值。 |

### columnsGap

PhonePC/2in1TabletTVWearable

columnsGap(value: LengthMetrics): T

设置列与列的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 列与列的间距。  默认值：0vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件。 |

### rowsGap

PhonePC/2in1TabletTVWearable

rowsGap(value: LengthMetrics): T

设置行与行的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 行与行的间距。  默认值：0vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件。 |

## 事件

PhonePC/2in1TabletTVWearable

仅支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过WaterFlow和LazyVGridLayout实现懒加载网格布局。

MyDataSource实现了[LazyForEach](ts-rendering-control-lazyforeach.md)数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给LazyVGridLayout提供子组件。

```
1. import { LengthMetrics } from '@kit.ArkUI'
2. import { MyDataSource } from './MyDataSource'

4. @Entry
5. @Component
6. struct LazyVGridLayoutSample1 {
7. private arr1:MyDataSource<number> = new MyDataSource<number>();
8. private arr2:MyDataSource<number> = new MyDataSource<number>();
9. build() {
10. Column() {
11. WaterFlow() {
12. LazyVGridLayout() {
13. LazyForEach(this.arr1, (item:number)=>{
14. Text('item' + item.toString())
15. .height(64)
16. .width('100%')
17. .borderRadius(5)
18. .backgroundColor(Color.White)
19. .textAlign(TextAlign.Center)
20. })
21. }
22. .columnsTemplate('1fr')
23. .rowsGap(LengthMetrics.vp(10))

25. LazyVGridLayout() {
26. LazyForEach(this.arr2, (item:number)=>{
27. Text('item' + item.toString())
28. .height(128)
29. .width('100%')
30. .borderRadius(5)
31. .backgroundColor(Color.White)
32. .textAlign(TextAlign.Center)
33. })
34. }
35. .columnsTemplate('1fr 1fr')
36. .rowsGap(LengthMetrics.vp(10))
37. .columnsGap(LengthMetrics.vp(10))
38. }.padding(10)
39. .rowsGap(10)
40. }
41. .width('100%').height('100%')
42. .backgroundColor('#DCDCDC')
43. }

45. aboutToAppear(): void {
46. for (let i = 0; i < 6; i++) {
47. this.arr1.pushData(i);
48. }
49. for (let i = 0; i < 100; i++) {
50. this.arr2.pushData(i);
51. }
52. }
53. }
```

```
1. // MyDataSource.ets
2. export class BasicDataSource<T> implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. protected dataArray: T[] = [];

6. public totalCount(): number {
7. return this.dataArray.length;
8. }

10. public getData(index: number): T {
11. return this.dataArray[index];
12. }

14. registerDataChangeListener(listener: DataChangeListener): void {
15. if (this.listeners.indexOf(listener) < 0) {
16. console.info('add listener');
17. this.listeners.push(listener);
18. }
19. }

21. unregisterDataChangeListener(listener: DataChangeListener): void {
22. const pos = this.listeners.indexOf(listener);
23. if (pos >= 0) {
24. console.info('remove listener');
25. this.listeners.splice(pos, 1);
26. }
27. }

29. notifyDataReload(): void {
30. this.listeners.forEach(listener => {
31. listener.onDataReloaded();
32. })
33. }

35. notifyDataAdd(index: number): void {
36. this.listeners.forEach(listener => {
37. listener.onDataAdd(index);
38. })
39. }

41. notifyDataChange(index: number): void {
42. this.listeners.forEach(listener => {
43. listener.onDataChange(index);
44. })
45. }

47. notifyDataDelete(index: number): void {
48. this.listeners.forEach(listener => {
49. listener.onDataDelete(index);
50. })
51. }

53. notifyDataMove(from: number, to: number): void {
54. this.listeners.forEach(listener => {
55. listener.onDataMove(from, to);
56. })
57. }

59. notifyDatasetChange(operations: DataOperation[]): void {
60. this.listeners.forEach(listener => {
61. listener.onDatasetChange(operations);
62. })
63. }
64. }

66. export class MyDataSource<T> extends BasicDataSource<T> {
67. public shiftData(): void {
68. this.dataArray.shift();
69. this.notifyDataDelete(0);
70. }
71. public unshiftData(data: T): void {
72. this.dataArray.unshift(data);
73. this.notifyDataAdd(0);
74. }
75. public pushData(data: T): void {
76. this.dataArray.push(data);
77. this.notifyDataAdd(this.dataArray.length - 1);
78. }
79. public popData(): void {
80. this.dataArray.pop();
81. this.notifyDataDelete(this.dataArray.length);
82. }
83. public clearData(): void {
84. this.dataArray = [];
85. this.notifyDataReload();
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/Xbq50YwlQnOxSXQ9grx1zg/zh-cn_image_0000002589245983.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055145Z&HW-CC-Expire=86400&HW-CC-Sign=EA425BBD53343EEB7B58D4F496EDAE7087698727EE9A7A3875D4319FA0CFE4A3)
