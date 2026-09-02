---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-framecallback
title: Class (FrameCallback)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (FrameCallback)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5fcd6d986f7f811a13af10ff4cf26207939e30fe6f890341e7206f1520440abd
---

用于定义帧回调任务，可在下一帧渲染阶段或帧渲染任务结束后的空闲阶段执行。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 本模块接口仅可在Stage模型下使用。
* 以下API需要配合[UIContext](arkts-apis-uicontext-uicontext.md)中的[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)和[postDelayedFrameCallback](arkts-apis-uicontext-uicontext.md#postdelayedframecallback12)使用。开发者需要继承该类并重写[onFrame](arkts-apis-uicontext-framecallback.md#onframe12)或[onIdle](arkts-apis-uicontext-framecallback.md#onidle12)方法，实现具体的业务逻辑。

## onFrame12+

onFrame(frameTimeInNano: number): void

在下一帧进行渲染时，该方法将被执行。

继承FrameCallback类并重写该方法后，可配合[UIContext](arkts-apis-uicontext-uicontext.md)中的[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)或[postDelayedFrameCallback](arkts-apis-uicontext-uicontext.md#postdelayedframecallback12)使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameTimeInNano | number | 是 | 下一帧渲染开始执行的时间，以纳秒为单位，由系统回调时传入，开发者无需手动传入。  取值范围：[0, +∞) |

**示例：**

```ts
import { FrameCallback } from '@kit.ArkUI';

class MyFrameCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onFrame(frameTimeInNano: number) {
    console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeInNano.toString());
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('点击触发postFrameCallback')
          .onClick(() => {
            this.getUIContext().postFrameCallback(new MyFrameCallback('normTask'));
          })
        Button('点击触发postDelayedFrameCallback')
          .onClick(() => {
            this.getUIContext().postDelayedFrameCallback(new MyFrameCallback('delayTask'), 5);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## onIdle12+

onIdle(timeLeftInNano: number): void

下一帧渲染任务结束后，若当前时间到下一个VSync信号的剩余时间大于1ms，则执行该回调；若剩余时间小于等于1ms，则将回调顺延至后续某一帧，待当前时间到下一个VSync信号的剩余时间大于1ms时执行。若当前没有已请求的下一帧，系统会自动请求一帧。

继承FrameCallback类并重写该方法后，可配合[UIContext](arkts-apis-uicontext-uicontext.md)中的[postFrameCallback](arkts-apis-uicontext-uicontext.md#postframecallback12)或[postDelayedFrameCallback](arkts-apis-uicontext-uicontext.md#postdelayedframecallback12)使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeLeftInNano | number | 是 | 这一帧剩余的空闲时间，以纳秒为单位，由系统回调时传入，开发者无需手动传入。  取值范围：[0, +∞) |

**示例：**

```ts
import { FrameCallback } from '@kit.ArkUI';

class MyIdleCallback extends FrameCallback {
  private tag: string;

  constructor(tag: string) {
    super();
    this.tag = tag;
  }

  onIdle(timeLeftInNano: number) {
    console.info('MyIdleCallback ' + this.tag + ' ' + timeLeftInNano.toString());
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('点击触发postFrameCallback')
          .onClick(() => {
            this.getUIContext().postFrameCallback(new MyIdleCallback('normTask'));
          })
        Button('点击触发postDelayedFrameCallback')
          .onClick(() => {
            this.getUIContext().postDelayedFrameCallback(new MyIdleCallback('delayTask'), 5);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
