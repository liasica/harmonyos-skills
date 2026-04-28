---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events
title: 通用事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 组件通用信息 > 通用事件
category: harmonyos-references
scraped_at: 2026-04-28T08:02:53+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:0c4ffaba9e9afe686f31023cbe50d1ad961292c98fa01b04e5b5d70717c273b0
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 事件说明

PhonePC/2in1TabletTVWearable

* 事件绑定在组件上，当组件达到事件触发条件时，会执行JS中对应的事件回调函数，实现页面UI视图和页面JS逻辑层的交互。
* 事件回调函数中通过参数可以携带额外的信息，如组件上的数据对象[dataSet](js-components-common-events.md#target对象6)、事件特有的回调参数。

相对于私有事件，大部分组件都可以绑定如下事件。

| 名称 | 参数 | 描述 | 是否支持冒泡 | 是否支持捕获 |
| --- | --- | --- | --- | --- |
| touchstart | TouchEvent | 手指刚触摸屏幕时触发该事件。TouchEvent具体可参考表2。 | 是5+ | 是5+ |
| touchmove | TouchEvent | 手指触摸屏幕后移动时触发该事件。 | 是5+ | 是5+ |
| touchcancel | TouchEvent | 手指触摸屏幕中动作被打断时触发该事件。 | 是5+ | 是5+ |
| touchend | TouchEvent | 手指触摸结束离开屏幕时触发该事件。 | 是5+ | 是5+ |
| click | BaseEvent | 点击动作触发该事件。 | 是6+ | 否 |
| doubleclick7+ | BaseEvent | 双击动作触发该事件。 | 否  从API version 9 开始支持冒泡。 | 否 |
| longpress | BaseEvent | 长按动作触发该事件。 | 否  从API version 9 开始支持冒泡。 | 否 |
| swipe5+ | SwipeEvent | 组件上快速滑动后触发该事件。 SwipeEvent具体可参考表4 。 | 否  从API version 9 开始支持冒泡。 | 否 |
| attached6+ | - | 当前组件节点挂载在渲染树后触发。 | 否 | 否 |
| detached6+ | - | 当前组件节点从渲染树中移除后触发。 | 否 | 否 |
| pinchstart7+ | PinchEvent | 手指开始执行捏合操作时触发该事件。  PinchEvent具体可参考表5。 | 否 | 否 |
| pinchupdate7+ | PinchEvent | 手指执行捏合操作过程中触发该事件。 | 否 | 否 |
| pinchend7+ | PinchEvent | 手指捏合操作结束离开屏幕时触发该事件。 | 否 | 否 |
| pinchcancel7+ | PinchEvent | 手指捏合操作被打断时触发该事件。 | 否 | 否 |
| dragstart7+ | DragEvent | 用户开始拖拽时触发该事件。  DragEvent具体可参考表6。 | 否 | 否 |
| drag7+ | DragEvent | 拖拽过程中触发该事件。 | 否 | 否 |
| dragend7+ | DragEvent | 用户拖拽完成后触发。 | 否 | 否 |
| dragenter7+ | DragEvent | 进入释放目标时触发该事件。 | 否 | 否 |
| dragover7+ | DragEvent | 在释放目标内拖动时触发。 | 否 | 否 |
| dragleave7+ | DragEvent | 离开释放目标区域时触发。 | 否 | 否 |
| drop7+ | DragEvent | 在可释放目标区域内释放时触发。 | 否 | 否 |

说明

除上述事件外，其他事件均为非冒泡事件，如[input的change事件](js-components-basic-input.md#事件)，详见各个组件。

**表1** BaseEvent对象属性列表

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 当前事件的类型，比如click、longpress等。 |
| timestamp | number | 该事件触发时的时间戳。 |
| deviceId8+ | number | 触发该事件的设备ID信息。 |
| target12+ | [Target](js-components-common-events.md#target对象6) | 触发该事件的目标对象。 |

**表2** TouchEvent对象属性列表(继承BaseEvent)

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array<TouchInfo> | 触摸事件时的属性集合，包含屏幕触摸点的信息数组。 |
| changedTouches | Array<TouchInfo> | 触摸事件时的属性集合，包括产生变化的屏幕触摸点的信息数组。数据格式和touches一样。该属性表示有变化的触摸点，如从无变有，位置变化，从有变无。例如用户手指刚接触屏幕时，touches数组中有数据，但changedTouches无数据。 |

**表3** TouchInfo

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| globalX | number | 距离屏幕左上角（不包括状态栏）横向距离。屏幕的左上角为原点。 |
| globalY | number | 距离屏幕左上角（不包括状态栏）纵向距离。屏幕的左上角为原点。 |
| localX | number | 距离被触摸组件左上角横向距离。组件的左上角为原点。 |
| localY | number | 距离被触摸组件左上角纵向距离。组件的左上角为原点。 |
| size | number | 触摸接触面积。 |
| force6+ | number | 接触力信息。 |

**表4** SwipeEvent 基础事件对象属性列表（继承BaseEvent）

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| direction | string | 滑动方向，可能值有：  - left：向左滑动；  - right：向右滑动；  - up：向上滑动；  - down：向下滑动。 |
| distance6+ | number | 在滑动方向上的滑动距离。 |

**表5** PinchEvent 对象属性列表7+

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| scale | number | 缩放比例。 |
| pinchCenterX | number | 捏合中心点X轴坐标，单位px。 |
| pinchCenterY | number | 捏合中心点Y轴坐标，单位px。 |

**表6** DragEvent对象属性列表(继承BaseEvent)7+

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | string | 事件名称。 |
| globalX | number | 距离屏幕左上角坐标原点横向距离。 |
| globalY | number | 距离屏幕左上角坐标原点纵向距离。 |
| timestamp | number | 时间戳。 |
| dataTransfer9+ | [DataTransfer](js-components-common-events.md#datatransfer对象9) | 用于传输数据。 |

## Target对象6+

PhonePC/2in1TabletTVWearable

当组件触发事件后，事件回调函数默认会收到一个事件对象，通过该事件对象可以获取相应的信息。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| dataSet6+ | Object | 组件上通过通用属性设置的[data-\*](js-components-common-attributes.md#常规属性)的自定义属性组成的集合。 |

**示例：**

```
1. <!-- xxx.hml -->
2. <div>
3. <div data-a="dataA" data-b="dataB"
4. style="width: 100%; height: 50%; background-color: saddlebrown;"@touchstart='touchstartfunc'></div>
5. </div>
```

```
1. // xxx.js
2. export default {
3. touchstartfunc(msg) {
4. console.info(`on touch start, point is: ${msg.touches[0].globalX}`);
5. console.info(`on touch start, data is: ${msg.target.dataSet.a}`);
6. }
7. }
```

## DataTransfer对象9+

PhonePC/2in1TabletTVWearable

在拖拽操作的过程中，可以通过dataTransfer对象来传输数据，以便在拖拽操作结束的时候对数据进行其他操作。

### setData9+

PhonePC/2in1TabletTVWearable

setData(key: string, value: object): boolean

设置给定key关联的数据。如果没有与该key关联的数据，则将其添加到末尾。如果该key关联的数据已经存在，则在相同位置替换现有数据。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| key | string | 是 | 数据键值。 |
| value | object | 是 | 要存储的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 执行结果，true表示成功，false表示失败。 |

**示例：**

```
1. // setData的value参数，可以是基本数据类型。
2. dragStart(e) {
3. var isSetOK = e.dataTransfer.setData('name', 1);
4. },
5. // setData的value参数，也可以是对象类型。
6. dragStart(e) {
7. var person = new Object();
8. person.name = "tom";
9. person.age = 21;
10. var isSetOK = e.dataTransfer.setData('person', person);
11. }
```

### getData9+

PhonePC/2in1TabletTVWearable

getData(key: string): object

获取给定key关联的数据，如果没有与该key关联的数据，则返回空字符串。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| key | string | 是 | 数据键值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| object | 获取的数据。 |

**示例：**

```
1. dragStart(e) {
2. var person = new Object();
3. person.name = "tom";
4. person.age = 21;
5. e.dataTransfer.setData('person', person);
6. },
7. dragEnd(e){
8. var person = e.dataTransfer.getData('person');
9. },
```

### clearData9+

PhonePC/2in1TabletTVWearable

clearData(key?: string): boolean

删除给定key关联的数据。如果没有与该key关联的数据，则该方法不会产生任何效果。

如果key为空，则删除所有数据。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| key | string | 否 | 数据键值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 执行结果，true表示成功，false表示失败。 |

**示例：**

```
1. dragEnd(e) {
2. var isSuccess = e.dataTransfer.clearData('name');
3. }
```

### setDragImage9+

PhonePC/2in1TabletTVWearable

setDragImage(pixelMap: PixelMap, offsetX: number,offsetY: number): boolean

用于设置自定义的拖动图像。

**参数：**

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| pixelMap | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 前端传入的图片资源。 |
| offsetX | number | 是 | 相对于图片的横向偏移量。 |
| offsetY | number | 是 | 相对于图片的纵向偏移量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 执行结果，true表示成功，false表示失败。 |

**示例：**

```
1. import image from '@ohos.multimedia.image';

3. export default {
4. // 生成96x96尺寸的PixelMap，创建颜色缓冲区并填充随机色值，配置PixelMap参数后生成实例
5. createPixelMap() {
6. let color = new ArrayBuffer(4 * 96 * 96);
7. var buffer = new Uint8Array(color);
8. // 循环填充缓冲区色值
9. for (var i = 0; i < buffer.length; i++) {
10. buffer[i] = (i + 1) % 255;
11. }
12. let opts = {
13. alphaType: 0,
14. editable: true,
15. pixelFormat: 4,
16. scaleMode: 1,
17. size: {
18. height: 96, width: 96
19. }
20. }
21. // 调用image.createPixelMap生成PixelMap实例
22. const promise = image.createPixelMap(color, opts);
23. promise.then((data) => {
24. console.error('-create pixelMap has info message:' + JSON.stringify(data));
25. this.pixelMap = data;
26. this.pixelMapReader = data;
27. })
28. },

30. // 初始化方法，调用createPixelMap生成PixelMap
31. onInit() {
32. this.createPixelMap()
33. },

35. // 拖拽开始回调，设置拖拽预览图为生成的PixelMap，偏移量为(50, 50)
36. dragStart(e) {
37. e.dataTransfer.setDragImage(this.pixelMapReader, 50, 50);
38. }
39. }
```
