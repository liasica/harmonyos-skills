---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture
title: PanGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > PanGesture
category: harmonyos-references
scraped_at: 2026-04-29T13:51:35+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:4a282c96fc9540ba75daec0d1f2e0b890e970c087e1abba558edcbbc6cbb2fab
---

滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

以下场景可以触发滑动手势：

| 触发方式 | 输入源类型 | 输入设备类型 | 备注 |
| --- | --- | --- | --- |
| 手指按下滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).Finger | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).TouchScreen | axisVertical和axisHorizontal均为0。 |
| 鼠标左键按下滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical和axisHorizontal均为0。 |
| 鼠标滚轮滚动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical或axisHorizontal不为0。 |
| 触摸板按下左键后滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical和axisHorizontal均为0。 |
| 触摸板双指滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).TOUCHPAD | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical或axisHorizontal不为0。 |
| 手写笔滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).Pen | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).TouchScreen | axisVertical和axisHorizontal均为0。 |

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 接口

PhonePC/2in1TabletTVWearable

### PanGesture

PhonePC/2in1TabletTVWearable

PanGesture(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions)

创建滑动手势对象。继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明); distance?: number } | [PanGestureOptions](ts-basic-gestures-pangesture.md#pangestureoptions) | 否 | 滑动手势参数。  - fingers：用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。  默认值：1  取值范围：[1, 10]  **说明：**  当设置的值小于1或不设置时，会被转化为默认值。  - direction：用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All  - distance：用于指定触发滑动手势事件的最小滑动距离，单位为vp。  取值范围：[0, +∞)  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs](ts-container-tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。  当设定的值小于0时，按默认值处理。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### PanGesture15+

PhonePC/2in1TabletTVWearable

PanGesture(options?: PanGestureHandlerOptions)

创建滑动手势对象。与[PanGesture](ts-basic-gestures-pangesture.md#pangesture-1)相比，options参数新增了对isFingerCountLimited和distanceMap参数，分别表示是否检查触摸屏幕的手指数量以及指定不同输入源触发滑动手势事件的最小滑动距离。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](ts-gesturehandler.md#pangesturehandleroptions) | 否 | 滑动手势处理器配置参数。 |

## PanDirection枚举说明

PhonePC/2in1TabletTVWearable

与SwipeDirection不同，PanDirection没有角度限制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| All | - | 所有方向。 |
| Horizontal | - | 水平方向。 |
| Vertical | - | 竖直方向。 |
| Left | - | 向左滑动。 |
| Right | - | 向右滑动。 |
| Up | - | 向上滑动。 |
| Down | - | 向下滑动。 |
| None | - | 任何方向都不可触发滑动手势事件。 |

## PanGestureOptions

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })

创建滑动手势配置参数对象。通过PanGestureOptions对象接口可以动态修改滑动手势的属性，从而避免通过状态变量修改属性（状态变量修改会导致UI刷新）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明); distance?: number } | 否 | 滑动手势配置参数对象。  fingers用于指定触发滑动的最少手指数，最小为1指， 最大取值为10指。  默认值：1  direction用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All  distance用于指定触发滑动手势事件的最小滑动距离，单位为vp。  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs](ts-container-tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。  当设定的值小于0时，按默认值处理。  建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### setDirection

PhonePC/2in1TabletTVWearable

setDirection(value: PanDirection)

设置滑动方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明) | 是 | 用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All |

### setDistance

PhonePC/2in1TabletTVWearable

setDistance(value: number)

设置触发滑动手势事件的最小滑动距离，单位为vp。距离值不宜设置过大，避免因滑动脱手、响应时延过大等问题导致性能劣化，最佳实践请参考：[减小拖动识别距离](../best-practices/bpta-application-latency-optimization-cases.md#section1116134115286)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 触发滑动手势事件的最小滑动距离，单位为vp。  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs组件](ts-container-tabs.md)滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。  当设定的值小于0时，按默认值处理。  建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### setFingers

PhonePC/2in1TabletTVWearable

setFingers(value: number)

设置触发滑动的最少手指数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 触发滑动的最少手指数，最小为1指， 最大取值为10指。  默认值：1 |

### getDirection12+

PhonePC/2in1TabletTVWearable

getDirection(): PanDirection

获取滑动方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明) | 滑动方向。 |

### getDistance18+

PhonePC/2in1TabletTVWearable

getDistance(): number

获取触发滑动手势事件的最小滑动距离。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 滑动手势事件的最小滑动距离。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

### onActionStart

PhonePC/2in1TabletTVWearable

onActionStart(event: (event: GestureEvent) => void)

设置滑动手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势识别成功回调。 |

### onActionUpdate

PhonePC/2in1TabletTVWearable

onActionUpdate(event: (event: GestureEvent) => void)

设置滑动手势更新回调。fingerList为多根手指时，该回调监听每次只会更新一根手指的位置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势更新回调。 |

### onActionEnd

PhonePC/2in1TabletTVWearable

onActionEnd(event: (event: GestureEvent) => void)

设置滑动手势结束回调。滑动手势识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势结束回调。 |

### onActionCancel

PhonePC/2in1TabletTVWearable

onActionCancel(event: () => void)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滑动手势取消回调。 |

### onActionCancel18+

PhonePC/2in1TabletTVWearable

onActionCancel(event: Callback<GestureEvent>)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势取消回调。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过PanGesture实现了单指/双指滑动手势的识别。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PanGestureExample {
5. @State offsetX: number = 0;
6. @State offsetY: number = 0;
7. @State positionX: number = 0;
8. @State positionY: number = 0;
9. private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

11. build() {
12. Column() {
13. Column() {
14. Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
15. }
16. .height(200)
17. .width(300)
18. .padding(20)
19. .border({ width: 3 })
20. .margin(50)
21. .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
22. // 左右滑动触发该手势事件
23. .gesture(
24. PanGesture(this.panOption)
25. .onActionStart((event: GestureEvent) => {
26. console.info('Pan start');
27. console.info(`Pan start timeStamp is: ${event.timestamp}`);
28. })
29. .onActionUpdate((event: GestureEvent) => {
30. if (event) {
31. this.offsetX = this.positionX + event.offsetX;
32. this.offsetY = this.positionY + event.offsetY;
33. }
34. })
35. .onActionEnd((event: GestureEvent) => {
36. this.positionX = this.offsetX;
37. this.positionY = this.offsetY;
38. console.info('Pan end');
39. console.info(`Pan end timeStamp is: ${event.timestamp}`);
40. })
41. )

43. Button('修改PanGesture触发条件')
44. .onClick(() => {
45. // 将PanGesture手势事件触发条件改为双指以任意方向滑动
46. this.panOption.setDirection(PanDirection.All);
47. this.panOption.setFingers(2);
48. })
49. }
50. }
51. }
```

示意图：

向左滑动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QGXoloy3QlCMOy0sop2SGw/zh-cn_image_0000002558766104.png?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=D0DCC8A43BD032062FDEC8D999785556C5A919CFE69C2FB2FDA2C8CB1CC5EE6E)

点击按钮时，修改PanGesture触发条件为双指向左下方滑动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Mrjbvn5ySbK_DZndWKn8tQ/zh-cn_image_0000002558606446.png?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=2E3554CAD26E9FC3659E2D7A01F875518F42AF54EDD56E11B2B825665B45FDD0)
