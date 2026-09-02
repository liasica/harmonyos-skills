---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-displaysync
title: "@ohos.graphics.displaySync (可变帧率)"
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.displaySync (可变帧率)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:06d89a1766e74d95c98a9d21ee2d46793d08b38dd9c9b9b84a5d2e198015d374
---

可变帧率支持让开发者以指定帧率来运行UI业务，一般用于开发者自绘制UI，并且对于帧率有特定需求的场景，系统会根据设置的期望帧率、最小帧率和最大帧率来调整绘制频率，以满足不同场景的需求。

**说明** 

本模块首批接口和数据定义从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { displaySync } from '@kit.ArkGraphics2D';
```

## displaySync.create

create(): DisplaySync

创建DisplaySync对象，通过此对象设置UI自绘制内容帧率。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DisplaySync](js-apis-graphics-displaysync.md#displaysync) | 返回DisplaySync对象实例，用于设置帧率范围、注册帧回调函数以及控制回调的启动和停止。 |

**示例：**

```ts
// 创建DisplaySync对象
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```

## IntervalInfo

开发者可以从回调函数中获取帧绘制的时间戳信息，包含当前帧到达的时间timestamp和下一帧预期到达的时间targetTimestamp。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 当前帧到达的时间（单位：纳秒）。系统启动以来的单调递增时间。 |
| targetTimestamp | number | 否 | 否 | 下一帧预期到达的时间（单位：纳秒）。系统启动以来的单调递增时间，值应大于timestamp。 |

## DisplaySync

期望帧率和回调函数设置实例。用于设置期望帧率范围、注册帧回调函数，以及启动和停止帧回调。下列API示例中都需先使用[displaySync.create()](js-apis-graphics-displaysync.md#displaysynccreate)方法获取到DisplaySync实例，再通过此实例调用对应方法。

### setExpectedFrameRateRange

setExpectedFrameRateRange(rateRange: ExpectedFrameRateRange): void

设置期望的帧率范围。设置的期望帧率范围将作为系统调度的参考，系统会尽量在此范围内调整绘制帧率。未调用该方法或传入ExpectedFrameRateRange(0, 0, 0)时将跟随应用当前运行的帧率。建议在调用[start](js-apis-graphics-displaysync.md#start)前设置，以便立即生效；调用[start](js-apis-graphics-displaysync.md#start)之后设置也可生效但可能存在延迟。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rateRange | [ExpectedFrameRateRange](ts-explicit-animation.md#expectedframeraterange11) | 是 | 设置DisplaySync期望的帧率范围，包含expected、min和max三个字段，单位为帧/秒（fps），字段需为非负整数，取值范围为[0, 设备最大帧率]，且满足min <= expected <= max。超出有效范围时会抛出401错误码。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2.Incorrect parameters types. 3. Parameter verification failed. or check if ExpectedFrameRateRange is valid. |

**示例：**

```ts
// 定义期望帧率范围
let range: ExpectedFrameRateRange = {
  expected: 10, // 期望帧率
  min: 0, // 最小帧率
  max: 120 // 最大帧率
};

// 设置DisplaySync期望帧率范围
backDisplaySync?.setExpectedFrameRateRange(range)

// 生效期望帧率范围
backDisplaySync?.start()
```

### on('frame')

on(type: 'frame', callback: Callback<IntervalInfo>): void

订阅每一帧的变化。注册回调函数后，还需调用[start](js-apis-graphics-displaysync.md#start)方法启动DisplaySync，系统才会在每一帧触发该回调。和[off('frame')](js-apis-graphics-displaysync.md#offframe)方法配对使用，用于取消注册回调函数。回调函数在UI主线程执行。回调频率受[setExpectedFrameRateRange](js-apis-graphics-displaysync.md#setexpectedframeraterange)设置的帧率范围影响。若回调执行耗时过长，可能导致卡顿，建议回调中只进行轻量业务逻辑。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'frame' | 是 | 设置回调的类型（只能是'frame'类型）。 |
| callback | Callback<[IntervalInfo](js-apis-graphics-displaysync.md#intervalinfo)> | 是 | 订阅帧变化的回调函数。[IntervalInfo](js-apis-graphics-displaysync.md#intervalinfo)包含timestamp（当前帧到达时间）和targetTimestamp（下一帧预期到达时间）两个属性，单位均为纳秒。 |

**示例：**

```ts
// 定义回调函数
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// 注册回调函数
backDisplaySync?.on("frame", callback)

// 生效回调函数
backDisplaySync?.start()
```

### off('frame')

off(type: 'frame', callback?: Callback<IntervalInfo>): void

取消订阅每一帧的变化。与[on('frame')](js-apis-graphics-displaysync.md#onframe)方法配对使用。取消成功后，将不再触发回调函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'frame' | 是 | 设置回调的类型（只能是'frame'类型）。 |
| callback | Callback<[IntervalInfo](js-apis-graphics-displaysync.md#intervalinfo)> | 否 | 传入调用[on('frame')](js-apis-graphics-displaysync.md#onframe)时注册的回调函数，用于取消订阅该回调函数。必须在已通过[on('frame')](js-apis-graphics-displaysync.md#onframe)注册回调后使用。 |

**示例：**

```ts
// 定义回调函数
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// 注册回调函数
backDisplaySync?.on("frame", callback)

// 取消回调函数
backDisplaySync?.off("frame", callback)
```

### start

start(): void

使通过[setExpectedFrameRateRange](js-apis-graphics-displaysync.md#setexpectedframeraterange)设置的期望帧率范围生效；如果通过[on('frame')](js-apis-graphics-displaysync.md#onframe)注册了回调函数，则开始请求VSync信号，触发已注册的回调，每帧执行一次。和[stop](js-apis-graphics-displaysync.md#stop)方法配对使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
// 定义期望帧率范围
let range: ExpectedFrameRateRange = {
  expected: 10, // 期望帧率
  min: 0, // 最小帧率
  max: 120 // 最大帧率
};
// 设置DisplaySync期望帧率范围
backDisplaySync?.setExpectedFrameRateRange(range)

// 定义回调函数
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// 注册回调函数
backDisplaySync?.on("frame", callback)

// 生效期望帧率范围并且开始每帧回调
backDisplaySync?.start()
```

**说明** 

start接口会将DisplaySync关联到UI上下文和窗口。若在非UI页面或异步回调中调用[start](js-apis-graphics-displaysync.md#start)，可能获取到错误的UI上下文，导致[start](js-apis-graphics-displaysync.md#start)功能异常，进而导致回调函数无法执行以及期望帧率范围无法生效。

此时可使用[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)接口指定UI上下文，确保[start](js-apis-graphics-displaysync.md#start)在正确的上下文中执行。

**示例：**

```ts
import { displaySync } from '@kit.ArkGraphics2D';
import { UIContext } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  // 创建DisplaySync实例
  backDisplaySync: displaySync.DisplaySync = displaySync.create();

  aboutToAppear() {
    // 获取UIContext实例
    let uiContext: UIContext = this.getUIContext();
    // 在当前UI上下文中执行DisplaySync的start接口
    uiContext?.runScopedTask(() => {
      this.backDisplaySync?.start();
    })
  }

  build() {
    // ...
  }
}
```

### stop

stop(): void

关闭期望帧率范围并且停止每帧回调。需在调用[start](js-apis-graphics-displaysync.md#start)后使用，停止后DisplaySync的配置（如期望帧率范围、回调函数）仍然保留，可随时通过[start](js-apis-graphics-displaysync.md#start)重新启动。[stop](js-apis-graphics-displaysync.md#stop)方法会解除DisplaySync与UI上下文和窗口的关联，通常无需特定的UI上下文。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
// 定义期望帧率范围
let range: ExpectedFrameRateRange = {
  expected: 10, // 期望帧率
  min: 0, // 最小帧率
  max: 120 // 最大帧率
};

// 设置DisplaySync期望帧率范围
backDisplaySync?.setExpectedFrameRateRange(range)

// 定义回调函数
let callback = (frameInfo: displaySync.IntervalInfo) => {
    console.info("DisplaySync", 'TimeStamp:' + frameInfo.timestamp + ' TargetTimeStamp: ' + frameInfo.targetTimestamp);
}

// 注册回调函数
backDisplaySync?.on("frame", callback)

// 生效期望帧率范围并且开始每帧回调
backDisplaySync?.start()

// ...

// 停止生效期望帧率范围并且停止每帧回调
backDisplaySync?.stop()
```
