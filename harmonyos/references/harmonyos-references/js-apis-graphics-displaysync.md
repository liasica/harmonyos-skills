---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-displaysync
title: @ohos.graphics.displaySync (可变帧率)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.displaySync (可变帧率)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c41cec8395d7b03f0a6564c6cff57fde687cf5ddde7735c20d192c5ed6122f00
---

可变帧率支持让开发者以指定帧率来运行UI业务，一般用于开发者自绘制UI，并且对于帧率有特定诉求的场景。

说明

本模块首批接口和数据定义从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { displaySync } from '@kit.ArkGraphics2D';
```

## displaySync.create

PhonePC/2in1TabletTVWearable

create(): DisplaySync

创建DisplaySync对象，通过此对象设置UI自绘制内容帧率。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DisplaySync](js-apis-graphics-displaysync.md#displaysync) | 返回当前创建的DisplaySync对象实例。 |

**示例：**

```
1. let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```

## IntervalInfo

PhonePC/2in1TabletTVWearable

开发者可以从订阅函数中获取帧绘制的时间戳信息，包含当前帧到达的时间timestamp和下一帧预期到达的时间targetTimestamp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 当前帧到达的时间（单位：纳秒）。 |
| targetTimestamp | number | 否 | 否 | 下一帧预期到达的时间（单位：纳秒）。 |

## DisplaySync

PhonePC/2in1TabletTVWearable

帧率和回调函数设置实例。用于帧率设置和回调函数的注册，以及启动和停止回调函数的调用。

下列API示例中都需先使用[displaySync.create()](js-apis-graphics-displaysync.md#displaysynccreate)方法获取到DisplaySync实例，再通过此实例调用对应方法。

### setExpectedFrameRateRange

PhonePC/2in1TabletTVWearable

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange) : void

设置期望的帧率范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 是 | 设置DisplaySync期望的帧率。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.Incorrect parameters types. 3. Parameter verification failed. or check ExpectedFrameRateRange if valid. |

**示例：**

```
1. let range : ExpectedFrameRateRange = {
2. expected: 10,
3. min:0,
4. max:120
5. };

7. // 设置DisplaySync期望的帧率
8. backDisplaySync?.setExpectedFrameRateRange(range)
```

### on('frame')

PhonePC/2in1TabletTVWearable

on(type: 'frame', callback: Callback<IntervalInfo>): void

订阅每一帧的变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'frame' | 是 | 设置注册回调的类型（只能是'frame'类型）。 |
| callback | Callback<[IntervalInfo](js-apis-graphics-displaysync.md#intervalinfo)> | 是 | 订阅函数。 |

**示例：**

```
1. let callback = (frameInfo: displaySync.IntervalInfo) => {
2. console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
3. }

5. // 注册订阅函数
6. backDisplaySync?.on("frame", callback)
```

### off('frame')

PhonePC/2in1TabletTVWearable

off(type: 'frame', callback?: Callback<IntervalInfo>): void

取消订阅每一帧的变化。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'frame' | 是 | 设置注册回调的类型（只能是'frame'类型）。 |
| callback | Callback<[IntervalInfo](js-apis-graphics-displaysync.md#intervalinfo)> | 否 | 订阅函数，参数不填时，默认取消全部订阅函数。 |

**示例：**

```
1. let callback = (frameInfo: displaySync.IntervalInfo) => {
2. console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
3. }

5. backDisplaySync?.on("frame", callback)

7. // 取消订阅函数
8. backDisplaySync?.off("frame", callback)
```

### start

PhonePC/2in1TabletTVWearable

start(): void

开始每帧回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. let range : ExpectedFrameRateRange = {
2. expected: 10,
3. min:0,
4. max:120
5. };

7. backDisplaySync?.setExpectedFrameRateRange(range)

9. let callback = (frameInfo: displaySync.IntervalInfo) => {
10. console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
11. }

13. backDisplaySync?.on("frame", callback)

15. // 开始每帧回调
16. backDisplaySync?.start()
```

说明

start接口是将DisplaySync关联到UI实例和窗口，若在非UI页面中或者一些异步回调中进行start操作，可能无法跟踪到当前UI的上下文，导致start接口失败，会进一步导致订阅函数无法执行。

因此可以使用UIContext的[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口来指定start函数执行的UI上下文。

**示例：**

```
1. import { displaySync } from '@kit.ArkGraphics2D';
2. import { UIContext } from '@kit.ArkUI';

4. // xxx.ets
5. @Entry
6. @Component
7. struct Index {
8. // 创建DisplaySync实例
9. backDisplaySync: displaySync.DisplaySync = displaySync.create();

11. aboutToAppear() {
12. // 获取UIContext实例
13. let uiContext: UIContext = this.getUIContext();
14. // 在当前UI上下文中执行DisplaySync的start接口
15. uiContext?.runScopedTask(() => {
16. this.backDisplaySync?.start();
17. })
18. }

20. build() {
21. // ...
22. }
23. }
```

### stop

PhonePC/2in1TabletTVWearable

stop(): void

停止每帧回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. let range : ExpectedFrameRateRange = {
2. expected: 10,
3. min:0,
4. max:120
5. };

7. backDisplaySync?.setExpectedFrameRateRange(range)

9. let callback = (frameInfo: displaySync.IntervalInfo) => {
10. console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
11. }

13. backDisplaySync?.on("frame", callback)

15. backDisplaySync?.start()

17. // ...

19. // 停止每帧回调
20. backDisplaySync?.stop()
```
