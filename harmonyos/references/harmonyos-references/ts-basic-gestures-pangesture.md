---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture
title: PanGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > PanGesture
category: harmonyos-references
scraped_at: 2026-09-05T06:17:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:98ee8416f8bda273d41ea8d5ee70441dfdb45c9086d9ddc8859be5f961fca812
---

当滑动距离达到设定的最小值时，触发滑动手势事件。

以下场景可以触发滑动手势：

| 触发方式 | 输入源类型 | 输入设备类型 | 备注 |
| --- | --- | --- | --- |
| 手指按下滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).Finger | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).TouchScreen | axisVertical和axisHorizontal均为0。 |
| 鼠标左键按下滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical和axisHorizontal均为0。 |
| 鼠标滚轮滚动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical或axisHorizontal不为0。 |
| 触摸板按下左键后滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).MOUSE | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical和axisHorizontal均为0。 |
| 触摸板双指滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).TOUCHPAD | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).Mouse | axisVertical或axisHorizontal不为0。 |
| 手写笔滑动。 | [SourceTool](ts-gesture-settings.md#sourcetool枚举说明9).Pen | [SourceType](ts-gesture-settings.md#sourcetype枚举说明8).TouchScreen | axisVertical和axisHorizontal均为0。 |

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 接口

### PanGesture

PanGesture(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions)

创建滑动手势对象。继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明); distance?: number } | [PanGestureOptions](ts-basic-gestures-pangesture.md#pangestureoptions) | 否 | 滑动手势参数。  - fingers：用于指定触发滑动的最少手指数，最小为1指，最大取值为10指。  默认值：1  取值范围：[1, 10]  **说明：**  当设置的值小于1或不设置时，会被转化为默认值。  - direction：用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All  - distance：用于指定触发滑动手势事件的最小滑动距离，单位为vp。  取值范围：[0, +∞)  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs](ts-container-tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免滑动手势与Tabs组件滑动事件的响应结果不符合预期。  当设定的值小于0时，按默认值处理。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### PanGesture15+

PanGesture(options?: PanGestureHandlerOptions)

创建滑动手势对象。与[PanGesture](ts-basic-gestures-pangesture.md#pangesture-1)相比，options参数新增了isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量；distanceMap参数从API version 19开始支持，用于指定不同输入源触发滑动手势事件的最小滑动距离，单位为vp。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](ts-gesturehandler.md#pangesturehandleroptions) | 否 | 滑动手势处理器配置参数，用于配置触发滑动手势事件的条件，包括是否检查触摸屏幕的手指数量（isFingerCountLimited）以及为不同输入源指定触发滑动手势事件的最小滑动距离（distanceMap，API version 19开始支持，单位为vp）。当需要配置是否检查触摸屏幕的手指数量，或需要为不同输入源分别指定触发滑动手势事件的最小滑动距离时，传入该参数；不传入时，使用默认滑动手势处理器配置。 |

## PanDirection枚举说明

与SwipeDirection不同，PanDirection没有角度限制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | 任何方向都不可触发滑动手势事件。 |
| Left | 1 | 向左滑动。 |
| Right | 2 | 向右滑动。 |
| Horizontal | 3 | 水平方向。 |
| Up | 4 | 向上滑动。 |
| Down | 8 | 向下滑动。 |
| Vertical | 12 | 竖直方向。 |
| All | 15 | 所有方向。 |

## PanGestureOptions

### constructor

constructor(value?: { fingers?: number; direction?: PanDirection; distance?: number })

创建滑动手势配置参数对象。通过PanGestureOptions对象可以动态修改滑动手势的属性，从而避免通过状态变量修改属性导致UI刷新。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { fingers?: number; direction?: [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明); distance?: number } | 否 | 滑动手势配置参数对象。  fingers用于指定触发滑动的最少手指数，最小为1指， 最大取值为10指。  默认值：1  direction用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All  distance用于指定触发滑动手势事件的最小滑动距离，单位为vp。  取值范围：[0, +∞)  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs](ts-container-tabs.md)组件滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免造成事件错乱。  当设定的值小于0时，按默认值处理。  建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延增加）的问题。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### setDirection

setDirection(value: PanDirection)

设置滑动方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明) | 是 | 用于指定触发滑动的手势方向，此枚举值支持逻辑与(&)和逻辑或（|）运算。  默认值：PanDirection.All |

### setDistance

setDistance(value: number)

设置触发滑动手势事件的最小滑动距离，单位为vp。建议以手写笔8vp、其余输入源5vp为初始值，根据实际交互场景调整滑动距离；滑动距离增大时，可能出现手势跟随效果变差、响应时延增加等问题，导致性能劣化，最佳实践请参考：[减小拖动识别距离](../best-practices/bpta-application-latency-optimization-cases.md#section1116134115286)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 触发滑动手势事件的最小滑动距离，单位为vp。  取值范围：[0, +∞)  手写笔默认值：8，其余输入源默认值：5  **说明：**  [Tabs组件](ts-container-tabs.md)滑动与该滑动手势事件同时存在时，可将distance值设为1，使滑动更灵敏，避免滑动手势与Tabs组件滑动事件的响应结果不符合预期。  当设定的值小于0时，按默认值处理。  建议设置合理的滑动距离，滑动距离设置过大时会导致滑动不跟手（响应时延慢）的问题。  当组件应用了[scale](ts-universal-attributes-transformation.md#scale)缩放变换时，distance的实际识别距离会按照scale比例进行缩放。 |

### setFingers

setFingers(value: number)

设置触发滑动的最少手指数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 触发滑动的最少手指数，最小为1指， 最大取值为10指。  默认值：1 |

### getDirection12+

getDirection(): PanDirection

获取滑动方向。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PanDirection](ts-basic-gestures-pangesture.md#pandirection枚举说明) | 当前PanGestureOptions对象中配置的滑动触发方向。 |

### getDistance18+

getDistance(): number

获取触发滑动手势事件的最小滑动距离。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前PanGestureOptions对象中配置的触发滑动手势事件的最小滑动距离，单位为vp。 |

## 事件

**说明** 

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

### onActionStart

onActionStart(event: (event: GestureEvent) => void)

设置滑动手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势识别成功时触发的回调函数，回调参数event为GestureEvent对象，用于获取本次滑动手势的事件信息。 |

### onActionUpdate

onActionUpdate(event: (event: GestureEvent) => void)

设置滑动手势更新回调。fingerList包含多根手指时，每次触发该回调仅更新一根手指的位置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势更新时触发的回调函数，回调参数event为GestureEvent对象，用于获取滑动过程中的手势事件信息。 |

### onActionEnd

onActionEnd(event: (event: GestureEvent) => void)

设置滑动手势结束回调。滑动手势识别成功后，手指抬起时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 滑动手势结束时触发的回调函数，回调参数event为GestureEvent对象，用于获取滑动结束时的手势事件信息。 |

### onActionCancel

onActionCancel(event: () => void)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 滑动手势取消回调。 |

### onActionCancel18+

onActionCancel(event: Callback<GestureEvent>)

设置滑动手势取消回调。滑动手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[GestureEvent](ts-gesture-common.md#gestureevent对象说明)> | 是 | 滑动手势取消时触发的回调函数，回调参数为GestureEvent对象，用于获取滑动取消时的手势事件信息。 |

## 示例

该示例通过PanGesture实现了单指/双指滑动手势的识别。

```ts
// xxx.ets
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
      // 左右滑动触发该手势事件
      .gesture(
      PanGesture(this.panOption)
        .onActionStart((event: GestureEvent) => {
          console.info('Pan start');
          console.info(`Pan start timeStamp is: ${event.timestamp}`);
        })
        .onActionUpdate((event: GestureEvent) => {
          if (event) {
            // 根据滑动偏移量更新组件当前位置
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd((event: GestureEvent) => {
          // 滑动结束后保存当前位置，作为下一次滑动的起始位置
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
          console.info('Pan end');
          console.info(`Pan end timeStamp is: ${event.timestamp}`);
        })
      )

      Button('修改PanGesture触发条件')
        .onClick(() => {
          // 将PanGesture手势事件触发条件改为双指以任意方向滑动
          this.panOption.setDirection(PanDirection.All);
          this.panOption.setFingers(2);
        })
    }
  }
}
```

示意图：

向左滑动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/PKWgY-1ZSpyzzYeQh3eREw/zh-cn_image_0000002712245974.png)

点击按钮时，修改PanGesture触发条件为双指向任意方向滑动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/bugBe9LVS6WYdH1moHGHAA/zh-cn_image_0000002742004923.png)
