---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pinchgesture
title: PinchGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > PinchGesture
category: harmonyos-references
scraped_at: 2026-04-29T13:51:35+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:8e31c8f4dcd38ed072c9805e4a94417077cd186b0f9f80306d222f1d014f94c6
---

用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。在支持鼠标和键盘输入的设备上，通过“Ctrl+鼠标滚轮”也可以触发捏合手势。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

捏合手势触发成功后，抬起手指直至不再满足触发条件。再次满足条件时，可重新触发捏合手势。

## 接口

PhonePC/2in1TabletTVWearable

### PinchGesture

PhonePC/2in1TabletTVWearable

PinchGesture(value?: { fingers?: number; distance?: number })

继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)，设置捏合手势事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; distance?: number } | 否 | 设置捏合手势事件参数。  - fingers：触发捏合的最少手指数，最小为2指，最大为5指。  默认值：2  取值范围：[2, 5]。当设置的值不在该范围内时，会被转化为默认值。  触发手势的手指数量可以多于fingers数目，但只有最先落下的与fingers相同数目的手指参与手势计算。  - distance：最小识别距离，单位为vp。该距离是指当前多根手指位置与手指中心位置的平均距离，与手指落下时的平均距离之间的差值。当这一差值大于或等于最小识别距离时，捏合手势被视为成功。  默认值：5  **说明：**  取值范围：[0, +∞)。当识别距离的值小于等于0时，会被转化为默认值。 |

### PinchGesture15+

PhonePC/2in1TabletTVWearable

PinchGesture(options?: PinchGestureHandlerOptions)

设置捏合手势事件。与[PinchGesture](ts-basic-gestures-pinchgesture.md#pinchgesture-1)相比，options参数新增isFingerCountLimited，表示是否检查触摸屏幕的手指数量。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PinchGestureHandlerOptions](ts-gesturehandler.md#pinchgesturehandleroptions) | 否 | 捏合手势处理器配置参数。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议开发者优先使用fingerInfos。

### onActionStart

PhonePC/2in1TabletTVWearable

onActionStart(event: (event: GestureEvent) => void)

Pinch手势识别成功后触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionUpdate

PhonePC/2in1TabletTVWearable

onActionUpdate(event: (event: GestureEvent) => void)

Pinch手势移动过程中回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionEnd

PhonePC/2in1TabletTVWearable

onActionEnd(event: (event: GestureEvent) => void)

Pinch手势识别成功，当抬起最后一根满足手势触发条件的手指后，触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

### onActionCancel

PhonePC/2in1TabletTVWearable

onActionCancel(event: () => void)

Pinch手势识别成功，接收到触摸取消事件触发的回调，不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 手势事件回调函数。 |

### onActionCancel18+

PhonePC/2in1TabletTVWearable

onActionCancel(event: Callback<GestureEvent>)

Pinch手势识别成功并接收到触摸取消事件的回调。与[onActionCancel](ts-basic-gestures-pinchgesture.md#onactioncancel)相比，该回调返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 手势事件回调函数。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（实现简单缩放）

该示例通过配置PinchGesture实现了三指捏合手势的识别功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PinchGestureExample {
5. @State scaleValue: number = 1;
6. @State pinchValue: number = 1;
7. @State pinchX: number = 0;
8. @State pinchY: number = 0;

10. build() {
11. Column() {
12. Column() {
13. Text('PinchGesture scale:\n' + this.scaleValue)
14. Text('PinchGesture center:\n(' + this.pinchX + ',' + this.pinchY + ')')
15. }
16. .height(200)
17. .width(300)
18. .padding(20)
19. .border({ width: 3 })
20. .margin({ top: 100 })
21. .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
22. // 三指捏合触发该手势事件
23. .gesture(
24. PinchGesture({ fingers: 3 }) // 三指捏合手势，用于缩放操作
25. .onActionStart((event: GestureEvent) => {
26. console.info('Pinch start')
27. })
28. .onActionUpdate((event: GestureEvent) => {
29. if (event) {
30. this.scaleValue = this.pinchValue * event.scale
31. this.pinchX = event.pinchCenterX
32. this.pinchY = event.pinchCenterY
33. }
34. })
35. .onActionEnd((event: GestureEvent) => {
36. this.pinchValue = this.scaleValue
37. console.info('Pinch end')
38. })
39. )
40. }.width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/su0_4dDKRsyBIR-qhPXfOA/zh-cn_image_0000002589325973.png?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=D410452436FAC35D10B9916428DFF3B7370BA7AEAD8965744C8F7685F42D4524)

### 示例2（实现图片跟手缩放）

通过配置PinchGesture，该示例实现了图片的跟手缩放效果。

```
1. // xxx.ets
2. import { UIContext, display, matrix4 } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct PinchGestureExample {
7. private uiContext: UIContext = new UIContext();
8. private contentWidth: number = 0;
9. private contentHeight: number = 0;
10. private scaleMin: number = 0.3;
11. private scaleMax: number = 30.0;
12. private screenWidth: number = 0;
13. private screenHeight: number = 0;
14. @State pntX: number = 0;
15. @State pntY: number = 0;
16. @State curScale: number = 1;
17. @State preScale: number = 1;
18. @State offsetX: number = 0;
19. @State offsetY: number = 0;
20. @State matrix: matrix4.Matrix4Transit = matrix4.identity()
21. .translate({ x: this.offsetX, y: this.offsetY })
22. .scale({ x: this.curScale, y: this.curScale });

24. public updateMatrix(): void {
25. this.matrix = matrix4.identity()
26. .scale({ x: this.curScale, y: this.curScale })
27. .translate({ x: this.uiContext.vp2px(this.offsetX), y: this.uiContext.vp2px(this.offsetY) });
28. }

30. aboutToAppear(): void {
31. this.uiContext = this.getUIContext();
32. let screenSize = display.getDefaultDisplaySync();
33. this.screenWidth = this.uiContext.px2vp(screenSize.width);
34. this.screenHeight = this.uiContext.px2vp(screenSize.height);
35. }

37. build() {
38. Column() {
39. // $r('app.media.img')需要替换为开发者所需的图像资源文件。
40. Image($r('app.media.img'))
41. .objectFit(ImageFit.Contain)
42. .draggable(false)
43. .onComplete((event) => {
44. this.contentWidth = this.uiContext.px2vp(event!.contentWidth);
45. this.contentHeight = this.uiContext.px2vp(event!.contentHeight);
46. })
47. .transform(this.matrix)
48. }
49. // 双指捏合触发该手势事件
50. .gesture(
51. PinchGesture({ fingers: 2 }) // 双指捏合手势，用于缩放图片
52. .onActionStart((event: GestureEvent) => {
53. // 图片本次缩放前展示大小
54. const displayWidth = this.contentWidth * this.curScale;
55. const displayHeight = this.contentHeight * this.curScale;
56. // 图片本次缩放前左上角顶点
57. const left = (this.screenWidth - displayWidth) / 2 + this.offsetX;
58. const top = (this.screenHeight - displayHeight) / 2 + this.offsetY;
59. // 本次缩放前手指终点相对图片左上角顶点尺寸占图片展示尺寸的百分比
60. this.pntX = (event.pinchCenterX - left) / displayWidth;
61. this.pntY = (event.pinchCenterY - top) / displayHeight;
62. // 图片本次缩放前的缩放比例
63. this.preScale = this.curScale;
64. })
65. .onActionUpdate((event: GestureEvent) => {
66. // 目标缩放比
67. this.curScale = this.preScale * event.scale;
68. let targetDisplayWidth = this.contentWidth * this.curScale;
69. let targetDisplayHeight = this.contentHeight * this.curScale;
70. // 本次缩放前手指中点在本次缩放后的坐标
71. const pointX = (this.screenWidth - targetDisplayWidth) / 2 + targetDisplayWidth * this.pntX;
72. const pointY = (this.screenHeight - targetDisplayHeight) / 2 + targetDisplayHeight * this.pntY;
73. // 将pointX、pointY移动到缩放后的手指中点，需要移动的距离
74. this.offsetX = event.pinchCenterX - pointX;
75. this.offsetY = event.pinchCenterY - pointY;
76. this.updateMatrix();
77. })
78. .onActionEnd((event: GestureEvent) => {
79. if (this.curScale < this.scaleMin || this.curScale > this.scaleMax) {
80. this.curScale = 1;
81. this.offsetX = 0;
82. this.offsetY = 0;
83. this.updateMatrix();
84. }
85. })
86. )
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/D-nDB6GcTSe7eQgG1XE8nQ/zh-cn_image_0000002589245915.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=97B06734D545A9F66D2689A272F6D9C9AC790BD1074A1F7D252DB682BBA8EFED)
