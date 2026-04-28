---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting
title: 拖拽排序
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 拖拽排序
category: harmonyos-references
scraped_at: 2026-04-28T08:01:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b3dc47119ce2474c0cf02beed84a3f2f20199ced9a7241b72e767c8f1c55990d
---

在List组件下使用ForEach/LazyForEach/Repeat，并设置onMove事件，每次迭代生成一个ListItem时，可以使能拖拽排序。拖拽排序离手后，如果数据位置发生变化，将触发onMove事件，上报数据移动原始索引号和目标索引号。在onMove事件中，需要根据上报的起始索引号和目标索引号修改数据源。确保数据仅顺序发生变化，才能正常执行落位动画。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## onMove

PhonePC/2in1TabletTVWearable

onMove(handler: Optional<OnMoveHandler>): T

拖拽排序数据移动回调。当父容器组件为[List](ts-container-list.md)，并且ForEach/LazyForEach/Repeat每次迭代都生成一个ListItem组件时才生效。设置拖拽排序时可以定义不同的拖拽操作，并在响应事件发生时响应。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[OnMoveHandler](ts-universal-attributes-drag-sorting.md#onmovehandler)> | 是 | 拖拽动作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onMove20+

PhonePC/2in1TabletTVWearable

onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T

拖拽排序数据移动回调。当父容器组件为[List](ts-container-list.md)，并且ForEach/LazyForEach/Repeat每次迭代都生成一个ListItem组件时才生效。设置拖拽排序时可以定义不同的拖拽操作，并在响应事件发生时响应。与[onMove](ts-universal-attributes-drag-sorting.md#onmove)相比，新增eventHandler参数，可以监听拖拽时上报的回调事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<[OnMoveHandler](ts-universal-attributes-drag-sorting.md#onmovehandler)> | 是 | 拖拽动作。 |
| eventHandler | [ItemDragEventHandler](ts-universal-attributes-drag-sorting.md#itemdrageventhandler20) | 是 | 拖拽发生时产生的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## OnMoveHandler

PhonePC/2in1TabletTVWearable

type OnMoveHandler = (from: number, to: number) => void

定义数据源拖拽回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 数据源拖拽起始索引号。取值范围是[0, 数据源长度-1]。 |
| to | number | 是 | 数据源拖拽目标索引号。取值范围是[0, 数据源长度-1]。 |

## ItemDragEventHandler20+

PhonePC/2in1TabletTVWearable

定义数据源拖拽事件回调。用于响应不同的拖拽操作。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onLongPress | [Callback](js-apis-base.md#callback)<number> | 否 | 是 | 长按时触发的回调。  - 参数index为长按时当前目标的索引号。 |
| onDragStart | [Callback](js-apis-base.md#callback)<number> | 否 | 是 | 在页面跟手滑动开始时触发的回调。  - 参数index为拖拽开始时当前目标的索引号。 |
| onMoveThrough | [OnMoveHandler](ts-universal-attributes-drag-sorting.md#onmovehandler) | 否 | 是 | 在页面跟手滑动过程中经过其他组件时触发的回调。 |
| onDrop | [Callback](js-apis-base.md#callback)<number> | 否 | 是 | 在页面跟手滑动结束时触发的回调。  - 参数index为拖拽结束时当前目标的索引号。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用OnMove进行拖拽）

以下示例展示了ForEach在List组件内使用时的拖拽效果。

```
1. @Entry
2. @Component
3. struct ForEachSort {
4. @State arr: Array<string> = [];

6. build() {
7. Row() {
8. List() {
9. ForEach(this.arr, (item: string) => {
10. ListItem() {
11. Text(item.toString())
12. .fontSize(16)
13. .textAlign(TextAlign.Center)
14. .size({height: 100, width: '100%'})
15. }.margin(10)
16. .borderRadius(10)
17. .backgroundColor('#FFFFFFFF')
18. }, (item: string) => item)
19. .onMove((from:number, to:number) => {
20. let tmp = this.arr.splice(from, 1);
21. this.arr.splice(to, 0, tmp[0]);
22. })
23. }
24. .width('100%')
25. .height('100%')
26. .backgroundColor('#FFDCDCDC')
27. }
28. }
29. aboutToAppear(): void {
30. for (let i = 0; i < 100; i++) {
31. this.arr.push(i.toString());
32. }
33. }
34. }
```

### 示例2（使用OnMove进行拖拽，并设置拖拽事件回调）

从API version 20开始，以下示例展示了ForEach在List组件设置拖拽效果后触发的回调事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListOnMoveExample {
5. private arr: number[] = [0, 1, 2, 3, 4, 5, 6];

7. build() {
8. Column() {
9. List({ space: 20, initialIndex: 0 }) {
10. ForEach(this.arr, (item: number) => {
11. ListItem() {
12. Text('第一个List' + item)
13. .width('100%')
14. .height(80)
15. .fontSize(16)
16. .textAlign(TextAlign.Center)
17. .borderRadius(10)
18. .backgroundColor(0xFFFFFF)
19. }
20. }, (item: string) => item)
21. .onMove((from: number, to: number) => {
22. let tmp = this.arr.splice(from, 1);
23. this.arr.splice(to, 0, tmp[0]);
24. console.info('List onMove From: ' + from);
25. console.info('List onMove To: ' + to);
26. },
27. {
28. onLongPress: (index: number) => {
29. console.info('List onLongPress: ' + index);
30. },
31. onDrop: (index: number) => {
32. console.info('List onDrop: ' + index);
33. },
34. onDragStart: (index: number) => {
35. console.info('List onDragStart: ' + index);
36. },
37. onMoveThrough: (from: number, to: number) => {
38. console.info('List onMoveThrough From: ' + from);
39. console.info('List onMoveThrough To: ' + to);
40. }
41. }
42. )
43. }.width('90%')
44. .scrollBar(BarState.Off)
45. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
46. }
47. }
```
