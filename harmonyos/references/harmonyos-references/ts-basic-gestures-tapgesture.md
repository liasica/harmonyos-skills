---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture
title: TapGesture
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 手势处理 > 基础手势 > TapGesture
category: harmonyos-references
scraped_at: 2026-04-29T13:51:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ceb6b65ca9309e60065529da231dd31ec80a0c5d450182744be4004e4aeeff11
---

支持单击、双击和多次点击事件的识别。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当组件同时绑定双击和单击手势且双击手势先绑定时，单击手势会有300ms的延时。

## 接口

PhonePC/2in1TabletTVWearable

TapGesture(value?: TapGestureParameters)

创建点击手势对象。继承自[GestureInterface<T>](ts-gesture-common.md#gestureinterfacet11)。

触发点击手势事件的设备类型为键盘或手柄时，事件的[SourceTool](ts-gesture-settings.md#sourcetool枚举说明9)值为Unknown，事件的[SourceType](ts-gesture-settings.md#sourcetype枚举说明8)值为KEY，JOYSTICK。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TapGestureParameters](ts-basic-gestures-tapgesture.md#tapgestureparameters12对象说明) | 否 | 点击手势的相关参数。 |

## TapGestureParameters12+对象说明

PhonePC/2in1TabletTVWearable

说明

为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

点击手势参数。继承自[BaseHandlerOptions](ts-gesturehandler.md#basehandleroptions15)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count11+ | number | 否 | 是 | 识别的连续点击次数。当设置的值小于1或不设置时，会被转化为默认值。  默认值：1  取值范围：[0, +∞)  **说明：**  1. 当配置多击时，上一次的最后一根手指抬起和下一次的第一根手指按下的超时时间为300毫秒。  2. 当上次点击的位置与当前点击的位置距离超过60vp时，手势识别失败。在多指情况下，点击的位置为所有参与手势响应手指的平均位置。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fingers11+ | number | 否 | 是 | 触发点击的手指数，最小为1指， 最大为10指。当设置小于1的值或不设置时，会被转化为默认值。  默认值：1  **说明：**  1. 当配置多指时，第一根手指按下后300毫秒内未有足够的手指数按下，手势识别失败；手指抬起时，抬起后剩余的手指数小于阈值时开始计时，如300ms内未全部抬起则手势识别失败。  2. 实际点击手指数超过配置值，手势识别成功。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| distanceThreshold | number | 否 | 是 | 点击手势移动阈值。当设置的值小于等于0或不设置时，会被转化为默认值。  默认值：2³¹-1  单位：vp  **说明：**  当手指的移动距离超出开发者预设的移动阈值时，点击识别失败。如果初始化为默认阈值时，手指移动超过组件热区范围，点击识别失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

说明

组件通过手势事件绑定不同GestureType的手势对象，各手势对象在响应手势操作的事件回调中提供手势相关信息。下面通过TapGesture手势对象的[onAction](ts-basic-gestures-tapgesture.md#onaction)事件响应点击事件，获取事件相关信息。其余手势对象的事件定义见各个手势对象章节。 若需绑定多种手势，请使用[组合手势](ts-combined-gestures.md)。

在[GestureEvent](ts-gesture-common.md#gestureevent对象说明)的fingerList元素中，手指索引编号与位置相对应，即fingerList[index]的id为index。对于先按下但未参与当前手势触发的手指，fingerList中对应的位置为空。建议优先使用fingerInfos。

### onAction

PhonePC/2in1TabletTVWearable

onAction(event: (event: GestureEvent) => void)

点击手势识别成功回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [GestureEvent](ts-gesture-common.md#gestureevent对象说明)) => void | 是 | 手势事件回调函数。 |

## EventLocationInfo20+

PhonePC/2in1TabletTVWearable

用于点击手势获取点击位置坐标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 相对于组件左上角的X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 相对于组件左上角的Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| windowX | number | 否 | 否 | 相对于窗口的左上角X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| windowY | number | 否 | 否 | 相对于窗口的左上角Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| displayX | number | 否 | 否 | 相对于屏幕的左上角X坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| displayY | number | 否 | 否 | 相对于屏幕的左上角Y坐标。  取值范围：[0, +∞)  单位：vp  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| globalDisplayX23+ | number | 否 | 是 | 相对于主屏幕左上角为原点的坐标系中的X坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| globalDisplayY23+ | number | 否 | 是 | 相对于主屏幕左上角为原点的坐标系中的Y坐标。  单位：vp  取值范围：[0, +∞)  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（双击手势识别）

该示例通过TapGesture实现了双击手势的识别。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TapGestureExample {
5. @State value: string = '';

7. build() {
8. Column() {
9. // 单指双击文本触发手势事件
10. Text('Click twice').fontSize(28)
11. .gesture(
12. TapGesture({ count: 2 })
13. .onAction((event: GestureEvent) => {
14. if (event) {
15. this.value = JSON.stringify(event.fingerList[0])
16. }
17. })
18. )
19. Text(this.value)
20. }
21. .height(300)
22. .width(300)
23. .padding(20)
24. .border({ width: 3 })
25. .margin(30)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Y95QQA8UQBCLrsrDY_GG-A/zh-cn_image_0000002558606444.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=162AA0D30AE2E2F7970CA14ED1843E6D7F022DBABBD9D56B20FDD3CA6D0AB743)

### 示例2（获取单击手势坐标）

该示例通过TapGesture获取单击手势点击位置的坐标。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TapGestureExample {

6. build() {
7. Column() {
8. Text('Click Once').fontSize(28)
9. .gesture(
10. TapGesture({ count: 1, fingers: 1 })
11. .onAction((event: GestureEvent | undefined) => {
12. if (event) {
13. console.info(`x = ${JSON.stringify(event.tapLocation?.x)}`)
14. console.info(`y = ${JSON.stringify(event.tapLocation?.y)}`)
15. console.info(`windowX = ${JSON.stringify(event.tapLocation?.windowX)}`)
16. console.info(`windowY = ${JSON.stringify(event.tapLocation?.windowY)}`)
17. console.info(`displayX = ${JSON.stringify(event.tapLocation?.displayX)}`)
18. console.info(`displayY = ${JSON.stringify(event.tapLocation?.displayY)}`)
19. // 从API version 23开始，新增globalDisplayX和globalDisplayY属性。
20. console.info(`globalDisplayX = ${JSON.stringify(event.tapLocation?.globalDisplayX)}`)
21. console.info(`globalDisplayY = ${JSON.stringify(event.tapLocation?.globalDisplayY)}`)
22. }
23. })
24. )
25. }
26. .height(200)
27. .width(300)
28. .padding(20)
29. .border({ width: 3 })
30. .margin(30)
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/84jqV7NpR1eFABiw2311yA/zh-cn_image_0000002589325971.png?HW-CC-KV=V1&HW-CC-Date=20260429T055134Z&HW-CC-Expire=86400&HW-CC-Sign=F01D0A17E415D17B66C095D72FC5754D2258D216F6E03A94BC4E36EA8C7C1426)
