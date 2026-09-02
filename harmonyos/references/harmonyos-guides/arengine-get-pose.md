---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-pose
title: 获取设备位姿（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 运动跟踪 > 获取设备位姿（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:12e7b51be79063a088f864dac7fe614a243d0a95c751e58f918a95630e963a24
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，获取设备位姿支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

获取设备位姿可以通过[ARCamera](../harmonyos-references/arengine-api-arengine.md#arcamera)相机对象获取，以下接口为获取设备位姿接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARCamera.getPose](../harmonyos-references/arengine-api-arengine.md#arcameragetpose) | 获取设备在世界空间中的位姿信息。 |

## 开发步骤

### 导入模块

获取设备位姿能力需要依赖以下模块。

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

Vec3是一个三维向量，用于存储设备的位姿信息。

### 定义变量

定义两个变量pose和stateReason，用于接收pose位姿信息和追踪失败原因。

```typescript
let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;
```

### 显示预览流及设备位姿信息

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

在设备界面上显示设备位姿信息及追踪失败原因，使用重复调用函数方法在设备界面上实时更新位姿和追踪失败原因的信息。

```typescript
@Builder
export function ARPoseBuilder() {
  ARPose()
}
let pose: arEngine.ARPose;
let stateReason: arEngine.ARTrackingStateReason;
@Component
struct ARPose {
  pageInfos: NavPathStack = new NavPathStack();
  @State arContext?: arViewController.ARViewContext = undefined;
  private intervalId: number = -1;
  private delayInterval: number = 33;
  private params: arEngine.ARConfig = { type: arEngine.ARType.WORLD };
  @State translation: Vec3 = {
    x: 0,
    y: 0,
    z: 0
  };
  @State currentTimeStamp: Date = new Date();
  @State reason: arEngine.ARTrackingStateReason = stateReason;

  build() {
    NavDestination() {
      RelativeContainer() {
        if (this.arContext) {
          ARView({ context: this.arContext })
            .height('100%')
            .width('100%')
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })

          Column() {
            Text(`x: ${this.translation.x.toFixed(4)}`)
              .infoStyles()
            Text(`y: ${this.translation.y.toFixed(4)}`)
              .infoStyles()
            Text(`z: ${this.translation.z.toFixed(4)}`)
              .infoStyles()
            Text(`reason: ${this.reason}`)
              .infoStyles()
            Text(`time: ${this.getCurrentTime(this.currentTimeStamp)}`)
              .infoStyles()
          }
          .alignItems(HorizontalAlign.Start)
          .margin({ left: '28vp' })
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },
            left: { anchor: '__container__', align: HorizontalAlign.Start }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView()

      this.intervalId = setInterval(() => {
        if (pose !== undefined) {
          this.translation = pose.translation
          this.reason = stateReason
          this.currentTimeStamp = new Date()
        }
      }, this.delayInterval);
    })
    .onWillDisappear(() => {
      clearInterval(this.intervalId);
      this.arContext?.destroy();
    })
    .onShown(() => {
      this.resumeARView()
    })
    .onHidden(() => {
      this.pauseARView()
    })
    .onReady(ctx => {
      this.params = ctx.pathInfo.param as arEngine.ARConfig;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private pauseARView(): void {
    // ...
  }

  private resumeARView(): void {
    // ...
  }

  private initARView(): void {
    // ...
  }
  // ...
  }
}
@Extend(Text)
function infoStyles() {
  .fontColor(Color.Yellow)
  .fontSize(20)
  .textShadow({
    radius: 10,
    color: Color.Black,
    offsetX: 0,
    offsetY: 0
  })
  .textAlign(TextAlign.Start)
}
```

### 获取设备位姿信息

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法获取AR会话对象arSession，之后通过AR会话对象arSession获取每一帧对应的设备位姿信息。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    try {
      let frame = session.getFrame();
      pose = frame.getCamera().getPose();
      stateReason = frame.getCamera().stateReason;
      releaseFrame(frame);
    } catch (error) {
      const err = error as BusinessError;
      // ...
    }
  }
}
```
