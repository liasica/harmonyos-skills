---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem
title: ListItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ListItem
category: harmonyos-references
scraped_at: 2026-04-28T08:01:29+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:b7c8b70be86f5f43a569ec4b004767f2964bb4caeec89052a52c740b981279de
---

用来展示列表具体item，必须配合List来使用。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件的父组件只能是[List](ts-container-list.md)或者[ListItemGroup](ts-container-listitemgroup.md)。
* 当ListItem配合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)使用时，ListItem子组件在ListItem创建时创建。配合[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)使用时，或父组件为List/ListItemGroup时，ListItem子组件在ListItem布局时创建。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

### ListItem10+

PhonePC/2in1TabletTVWearable

ListItem(value?: ListItemOptions)

创建ListItem组件。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListItemOptions](ts-container-listitem.md#listitemoptions10对象说明) | 否 | 为ListItem提供可选参数，该对象内含有[ListItemStyle](ts-container-listitem.md#listitemstyle10枚举说明)枚举类型的style参数。  默认值：{ style: ListItemStyle.NONE } |

### ListItem(deprecated)

PhonePC/2in1TabletTVWearable

ListItem(value?: string)

创建ListItem组件。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[ListItem10+](ts-container-listitem.md#listitem10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 否 | 无 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### sticky(deprecated)

PhonePC/2in1TabletTVWearable

sticky(value: Sticky)

设置ListItem吸顶效果。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[sticky](ts-container-list.md#sticky9)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Sticky](ts-container-listitem.md#stickydeprecated枚举说明) | 是 | ListItem吸顶效果。  默认值：Sticky.None |

### editable(deprecated)

PhonePC/2in1TabletTVWearable

editable(value: boolean | EditMode)

设置当前ListItem元素是否可编辑，进入编辑模式后可删除或移动列表项。

说明

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | [EditMode](ts-container-listitem.md#editmodedeprecated枚举说明) | 是 | ListItem元素是否可编辑。  默认值：false |

### selectable8+

PhonePC/2in1TabletTVWearable

selectable(value: boolean)

设置当前ListItem元素是否可以被鼠标框选。外层List容器的鼠标框选开启时，ListItem的框选才生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | ListItem元素是否可以被鼠标框选。设置为true时可以被鼠标框选，设置为false时无法被鼠标框选。  默认值：true |

### selected10+

PhonePC/2in1TabletTVWearable

selected(value: boolean)

设置当前ListItem选中状态。该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。该属性需要在设置[多态样式](ts-universal-attributes-polymorphic-style.md)前使用才能生效选中态样式。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前ListItem选中状态。设置为true时为选中状态，设置为false时为默认状态。  默认值：false |

### swipeAction9+

PhonePC/2in1TabletTVWearable

swipeAction(value: SwipeActionOptions)

用于设置ListItem的划出组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SwipeActionOptions](ts-container-listitem.md#swipeactionoptions9对象说明) | 是 | ListItem的划出组件。 |

## Sticky(deprecated)枚举说明

PhonePC/2in1TabletTVWearable

ListItem吸顶效果枚举。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用List组件的[stickyStyle枚举](ts-container-list.md#stickystyle9枚举说明)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | - | 无吸顶效果。 |
| Normal | - | 当前item吸顶。 |
| Opacity | - | 当前item吸顶显示透明度变化效果。 |

## EditMode(deprecated)枚举说明

PhonePC/2in1TabletTVWearable

ListItem元素编辑模式枚举。

说明

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | - | 编辑操作不限制。 |
| Deletable | - | 可删除。 |
| Movable | - | 可移动。 |

## SwipeEdgeEffect9+枚举说明

PhonePC/2in1TabletTVWearable

滑动效果枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Spring | - | ListItem划动距离超过划出组件大小后可以继续划动。  如果设置了删除区域，ListItem划动距离超过删除阈值后可以继续划动，  松手后按照弹簧阻尼曲线回弹。 |
| None | - | ListItem划动距离不能超过划出组件大小。  如果设置了删除区域，ListItem划动距离不能超过删除阈值，  并且在设置删除回调的情况下，达到删除阈值后松手触发删除回调。 |

## SwipeActionOptions9+对象说明

PhonePC/2in1TabletTVWearable

start和end对应的@builder函数中顶层必须是单个组件，否则会引发未定义行为。如果@builder函数中顶层是if/else、ForEach等语句，那么需要保证if/else、ForEach等语句必须能生成单个组件。

滑动手势只在listItem区域上，如果子组件划出ListItem区域外，在ListItem以外部分不会响应划动手势。所以在多列模式下，建议不要将划出组件设置太宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | [CustomBuilder](ts-types.md#custombuilder8) | [SwipeActionItem](ts-container-listitem.md#swipeactionitem10对象说明) | 否 | 是 | ListItem向右划动时item左边的组件（List垂直布局时）或ListItem向下划动时item上方的组件（List水平布局时）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| end | [CustomBuilder](ts-types.md#custombuilder8) | [SwipeActionItem](ts-container-listitem.md#swipeactionitem10对象说明) | 否 | 是 | ListItem向左划动时item右边的组件（List垂直布局时）或ListItem向上划动时item下方的组件（List水平布局时）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| edgeEffect | [SwipeEdgeEffect](ts-container-listitem.md#swipeedgeeffect9枚举说明) | 否 | 是 | 滑动效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onOffsetChange11+ | (offset: number) => void | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）位置发生变化触发，以vp为单位。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## SwipeActionItem10+对象说明

PhonePC/2in1TabletTVWearable

List垂直布局，ListItem向右滑动时，item左边的长距离滑动删除选项。向左滑动时，item右边的长距离滑动删除选项。

List水平布局，ListItem向上滑动时，item下边的长距离滑动删除选项。向下滑动时，item上边的长距离滑动删除选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actionAreaDistance | [Length](ts-types.md#length) | 否 | 是 | 设置组件长距离滑动删除距离阈值。即划出组件被完全滑进视窗后，继续滑动触发删除的距离阈值。  默认值：56vp  **说明：**  不支持设置百分比。  删除距离阈值大于item宽度减去划出组件宽度，或删除距离阈值小于等于0就不会设置删除区域。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAction | () => void | 否 | 是 | 组件进入长距删除区后抬手时触发。  **说明：**  滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才会触发。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onEnterActionArea | () => void | 否 | 是 | 在滑动条目进入删除区域时调用，只触发一次，当再次进入时仍触发。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onExitActionArea | () => void | 否 | 是 | 当滑动条目退出删除区域时调用，只触发一次，当再次退出时仍触发。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）时显示的操作项。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| builderComponent18+ | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 当列表项向左或向右滑动（当列表方向为“垂直”时），向上或向下滑动（当列表方向为“水平”时）时显示的操作项。  **说明：**  该参数的优先级高于参数builder。即同时设置builder和builderComponent时，以builderComponent设置的值为准。  同一个builderComponent不推荐同时给不同的start/end使用，否则会导致显示问题。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onStateChange11+ | (state:[SwipeActionState](ts-container-listitem.md#swipeactionstate11枚举说明)) => void | 否 | 是 | 当列表项滑动状态变化时候触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ListItemOptions10+对象说明

PhonePC/2in1TabletTVWearable

ListItem组件参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [ListItemStyle](ts-container-listitem.md#listitemstyle10枚举说明) | 否 | 是 | 设置List组件卡片样式。  默认值：ListItemStyle.NONE  设置为ListItemStyle.NONE时无样式。  设置为ListItemStyle.CARD时，建议配合[ListItemGroup](ts-container-listitemgroup.md)的ListItemGroupStyle.CARD同时使用，显示默认卡片样式。  卡片样式下，ListItem默认规格：高度48vp，宽度100%，左右内边距8vp。如果需要实现ListItem高度自适应，可以把height设置为undefined。  卡片样式下，为卡片内的列表选项提供了默认的focus、hover、press、selected和disable样式。  **说明：**  当设置为ListItemStyle.CARD时，List的listDirection属性值须为Axis.Vertical，如果设置为Axis.Horizontal，会导致显示混乱；List属性alignListItem默认为ListItemAlign.Center，居中对齐显示。 |

## ListItemStyle10+枚举说明

PhonePC/2in1TabletTVWearable

List组件卡片样式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无样式。 |
| CARD | 1 | 显示默认卡片样式。 |

## SwipeActionState11+枚举说明

PhonePC/2in1TabletTVWearable

列表项滑动状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLLAPSED | 0 | 收起状态，当ListItem向左或向右滑动（当列表方向为“垂直”时），  向上或向下滑动（当列表方向为“水平”时）时操作项处于隐藏状态。 |
| EXPANDED | 1 | 展开状态，当ListItem向左或向右滑动（当列表方向为“垂直”时），  向上或向下滑动（当列表方向为“水平”时）时操作项处于显示状态。  **说明：**  需要ListItem设置向左或向右滑动（当列表方向为“垂直”时），  向上或向下滑动（当列表方向为“水平”时）时显示的操作项。 |
| ACTIONING | 2 | 长距离状态，当ListItem进入长距删除区后删除ListItem的状态。  **说明：**  滑动后松手的位置超过或等于设置的距离阈值，并且设置的距离阈值有效时才能进入该状态。 |

## 事件

PhonePC/2in1TabletTVWearable

### onSelect8+

PhonePC/2in1TabletTVWearable

onSelect(event: (isSelected: boolean) => void)

ListItem元素被鼠标框选的状态改变时触发回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | boolean | 是 | 进入鼠标框选范围即被选中返回true， 移出鼠标框选范围即未被选中返回false。 |

## ListItemSwipeActionManager21+

PhonePC/2in1TabletTVWearable

ListItem划出菜单的管理器。

### expand21+

PhonePC/2in1TabletTVWearable

expand(node: FrameNode, direction: ListItemSwipeActionDirection): void

展开指定ListItem的划出菜单。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | ListItem节点对象。 |
| direction | [ListItemSwipeActionDirection](ts-container-listitem.md#listitemswipeactiondirection21枚举说明) | 是 | ListItem划出菜单的展开方向。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |

说明

* 如果List组件cachedCount属性isShow参数设置为true，List显示区域外已预加载完成的ListItem支持展开，否则List显示区域外节点不支持展开。

### collapse21+

PhonePC/2in1TabletTVWearable

collapse(node: FrameNode): void

收起指定ListItem的划出菜单。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md) | 是 | ListItem节点对象。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100023 | The component type of the node is incorrect. |
| 106203 | The node not mounted to component tree. |

## ListItemSwipeActionDirection21+枚举说明

PhonePC/2in1TabletTVWearable

ListItem划出菜单的展开方向。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 当列表方向是垂直方向时，LTR模式下表示ListItem的左边，RTL模式下表示ListItem的右边。当列表是水平方向时，表示ListItem的上边。 |
| END | 1 | 当列表方向是垂直方向时，LTR模式下表示ListItem的右边，RTL模式下表示ListItem的左边。当列表是水平方向时，表示ListItem的下边。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（创建ListItem）

该示例实现了创建ListItem的基本用法。

```
1. // xxx.ets
2. export class ListDataSource implements IDataSource {
3. private list: number[] = [];

5. constructor(list: number[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): number {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. }

20. unregisterDataChangeListener(listener: DataChangeListener): void {
21. }
22. }

24. @Entry
25. @Component
26. struct ListItemExample {
27. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

29. build() {
30. Column() {
31. List({ space: 20, initialIndex: 0 }) {
32. LazyForEach(this.arr, (item: number) => {
33. ListItem() {
34. Text('' + item)
35. .width('100%')
36. .height(100)
37. .fontSize(16)
38. .textAlign(TextAlign.Center)
39. .borderRadius(10)
40. .backgroundColor(0xFFFFFF)
41. }
42. }, (item: string) => item)
43. }.width('90%')
44. .scrollBar(BarState.Off)
45. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yey_TmZ4S5KUm8wINLdS8w/zh-cn_image_0000002552959614.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=3A544FFEE4B30B2FB8BE07C99EF8C3A0FC10125E306341847921944E635B69F4)

### 示例2（设置划出组件）

该示例展示了ListItem设置了swipeAction的横滑效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemExample2 {
5. @State arr: number[] = [0, 1, 2, 3, 4];
6. @State enterEndDeleteAreaString: string = 'not enterEndDeleteArea';
7. @State exitEndDeleteAreaString: string = 'not exitEndDeleteArea';
8. private scroller: ListScroller = new ListScroller();

10. @Builder
11. itemEnd() {
12. Row() {
13. Button('Delete').margin('4vp')
14. Button('Set').margin('4vp').onClick(() => {
15. this.scroller.closeAllSwipeActions();
16. })
17. }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
18. }

20. build() {
21. Column() {
22. List({ space: 10, scroller: this.scroller }) {
23. ForEach(this.arr, (item: number) => {
24. ListItem() {
25. Text('item' + item)
26. .width('100%')
27. .height(100)
28. .fontSize(16)
29. .textAlign(TextAlign.Center)
30. .borderRadius(10)
31. .backgroundColor(0xFFFFFF)
32. }
33. .transition(TransitionEffect.OPACITY)
34. .swipeAction({
35. end: {
36. builder: () => {
37. this.itemEnd()
38. },
39. onAction: () => {
40. this.getUIContext()?.animateTo({ duration: 1000 }, () => {
41. let index = this.arr.indexOf(item);
42. this.arr.splice(index, 1);
43. });
44. },
45. actionAreaDistance: 56,
46. onEnterActionArea: () => {
47. this.enterEndDeleteAreaString = 'enterEndDeleteArea';
48. this.exitEndDeleteAreaString = 'not exitEndDeleteArea';
49. },
50. onExitActionArea: () => {
51. this.enterEndDeleteAreaString = 'not enterEndDeleteArea';
52. this.exitEndDeleteAreaString = 'exitEndDeleteArea';
53. }
54. }
55. })
56. }, (item: number) => item.toString())
57. }

59. Text(this.enterEndDeleteAreaString).fontSize(20)
60. Text(this.exitEndDeleteAreaString).fontSize(20)
61. }
62. .padding(10)
63. .backgroundColor(0xDCDCDC)
64. .width('100%')
65. .height('100%')
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/xXSpsp2zTeOKyChNqyvNMQ/zh-cn_image_0000002583479615.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=612367F43382E4BDD488F2FB52F8B642ED60C8574E2452EE4602F50E734B4CD7)

### 示例3（设置卡片样式）

该示例展示了ListItem的卡片样式效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemExample3 {
5. build() {
6. Column() {
7. List({ space: '4vp', initialIndex: 0 }) {
8. ListItemGroup({ style: ListItemGroupStyle.CARD }) {
9. ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {
10. ListItem({ style: itemStyle }) {
11. Text('' + index)
12. .width('100%')
13. .textAlign(TextAlign.Center)
14. }
15. })
16. }

18. ForEach([ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE], (itemStyle: number, index?: number) => {
19. ListItem({ style: itemStyle }) {
20. Text('' + index)
21. .width('100%')
22. .textAlign(TextAlign.Center)
23. }
24. })
25. }
26. .width('100%')
27. .multiSelectable(true)
28. .backgroundColor(0xDCDCDC)
29. }
30. .width('100%')
31. .padding({ top: 5 })
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/5kZ-9HAVTHOdJ9hYm9kpew/zh-cn_image_0000002552799966.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=6DB594C65C5C4ED3CF5B24167DD123FAAB5FFA1B2C15A071203139E66A0539CE)

### 示例4（通过ComponentContent设置划出组件）

该示例通过[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)设置ListItem中的划出组件操作时显示的操作项。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. class BuilderParams {
5. text: string | Resource;
6. scroller: ListScroller;

8. constructor(text: string | Resource, scroller: ListScroller) {
9. this.text = text;
10. this.scroller = scroller;
11. }
12. }

14. @Builder
15. function itemBuilder(params: BuilderParams) {
16. Row() {
17. Button(params.text).margin('4vp')
18. Button('Set').margin('4vp').onClick(() => {
19. params.scroller.closeAllSwipeActions()
20. })
21. }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
22. }

24. @Component
25. struct MyListItem {
26. scroller: ListScroller = new ListScroller();
27. @State arr: number[] = [0, 1, 2, 3, 4];
28. @State project ?: number = 0;
29. startBuilder ?: ComponentContent<BuilderParams> = undefined;
30. endBuilder ?: ComponentContent<BuilderParams> = undefined;
31. builderParam = new BuilderParams('delete', this.scroller);

33. aboutToAppear(): void {
34. this.startBuilder = new ComponentContent(this.getUIContext(), wrapBuilder(itemBuilder), this.builderParam);
35. this.endBuilder = new ComponentContent(this.getUIContext(), wrapBuilder(itemBuilder), this.builderParam);
36. }

38. GetStartBuilder() {
39. this.startBuilder?.update(new BuilderParams('StartDelete', this.scroller));
40. return this.startBuilder;
41. }

43. GetEndBuilder() {
44. this.endBuilder?.update(new BuilderParams('EndDelete', this.scroller));
45. return this.endBuilder;
46. }

48. build() {
49. ListItem() {
50. Text('item' + this.project)
51. .width('100%')
52. .height(100)
53. .fontSize(16)
54. .textAlign(TextAlign.Center)
55. .borderRadius(10)
56. .backgroundColor(0xFFFFFF)
57. }
58. .transition(TransitionEffect.OPACITY)
59. .swipeAction({
60. end: {
61. builderComponent: this.GetEndBuilder(),
62. onAction: () => {
63. this.getUIContext()?.animateTo({ duration: 1000 }, () => {
64. let index = this.arr.indexOf(this.project);
65. this.arr.splice(index, 1);
66. });
67. },
68. actionAreaDistance: 56
69. },
70. start: {
71. builderComponent: this.GetStartBuilder(),
72. onAction: () => {
73. this.getUIContext()?.animateTo({ duration: 1000 }, () => {
74. let index = this.arr.indexOf(this.project);
75. this.arr.splice(index, 1);
76. });
77. },
78. actionAreaDistance: 56
79. }
80. })
81. .padding(5)
82. }
83. }

85. @Entry
86. @Component
87. struct ListItemExample {
88. @State arr: number[] = [0, 1, 2, 3, 4];
89. private scroller: ListScroller = new ListScroller();

91. build() {
92. Column() {
93. List({ space: 10, scroller: this.scroller }) {
94. ListItemGroup() {
95. ForEach(this.arr, (project: number) => {
96. MyListItem({ scroller: this.scroller, project: project, arr: this.arr })
97. }, (item: string) => item)
98. }
99. }
100. }
101. .padding(10)
102. .backgroundColor(0xDCDCDC)
103. .width('100%')
104. .height('100%')
105. }
106. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/7KECZPGkRCGTh0jkwxebTw/zh-cn_image_0000002583439661.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=3D74F003FD4DEE5CD47FA8D5D9FC94AC4F011F26CE6BC3001D7C0015023996A2)

### 示例5（通过ListItemSwipeActionManager管理划出菜单）

从API version 21开始，该示例通过[ListItemSwipeActionManager](ts-container-listitem.md#listitemswipeactionmanager21)管理ListItem的划出菜单。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ListItemExample5 {
7. @Builder
8. itemAction(str: string) {
9. Row() {
10. Button(str).margin('4vp')
11. }.padding('4vp').justifyContent(FlexAlign.SpaceEvenly)
12. }

14. build() {
15. Flex({ wrap: FlexWrap.Wrap }) {
16. Flex({ wrap: FlexWrap.Wrap, justifyContent: FlexAlign.SpaceBetween }) {
17. Button('expand start')
18. .onClick(() => {
19. try {
20. let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
21. ListItemSwipeActionManager.expand(node, ListItemSwipeActionDirection.START)
22. } catch (error) {
23. console.error('Error expand item:', (error as BusinessError).code, (error as BusinessError).message);
24. }
25. })
26. Button('expand end')
27. .onClick(() => {
28. try {
29. let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
30. ListItemSwipeActionManager.expand(node, ListItemSwipeActionDirection.END)
31. } catch (error) {
32. console.error('Error expand item:', (error as BusinessError).code, (error as BusinessError).message);
33. }
34. })
35. Button('collapse')
36. .onClick(() => {
37. try {
38. let node: FrameNode | null = this.getUIContext().getAttachedFrameNodeById('listItem');
39. ListItemSwipeActionManager.collapse(node)
40. } catch (error) {
41. console.error('Error collapse item:', (error as BusinessError).code, (error as BusinessError).message);
42. }
43. })
44. }
45. .margin({ bottom: 10 })

47. List({ space: 10 }) {
48. ListItem() {
49. Text('item')
50. .width('100%')
51. .height(100)
52. .fontSize(16)
53. .textAlign(TextAlign.Center)
54. .borderRadius(10)
55. .backgroundColor(0xFFFFFF)
56. }
57. .id('listItem')
58. .transition(TransitionEffect.OPACITY)
59. .swipeAction({
60. start: {
61. builder: () => {
62. this.itemAction('start')
63. },
64. },
65. end: {
66. builder: () => {
67. this.itemAction('end')
68. },
69. }
70. })
71. }
72. .height('80%')

74. }
75. .padding(10)
76. .backgroundColor(0xDCDCDC)
77. .width('100%')
78. .height('100%')
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/BuDw14v3Sj6rLsSiJKZIVw/zh-cn_image_0000002552959616.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=A94D9B3FAB05E774C3B786C0B823FC4F4CAA72560CB77F146CA7216A1B5B049D)
