---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-depth
title: 获取深度估计信息（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 深度估计 > 获取深度估计信息（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:cfa985299e287d17c5b995ea79c9e056a058db10f8ec28b669746b21a4c12e06
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，获取深度估计信息能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持深度估计特性（[ARENGINE\_FEATURE\_TYPE\_DEPTH](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

获取深度估计信息可以通过[ARFrame](../harmonyos-references/arengine-api-arengine.md#arframe)帧对象获取，以下接口为深度估计相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARFrame.acquireDepthImage16Bits](../harmonyos-references/arengine-api-arengine.md#arframeacquiredepthimage16bits) | 获取当前帧对应的深度图像对象。 |
| [ARFrame.acquireDepthConfidenceImage](../harmonyos-references/arengine-api-arengine.md#arframeacquiredepthconfidenceimage) | 获取当前帧的深度置信度图像。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

获取深度估计信息能力所需的模块导入方法如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import { arrayBufferInt32ToNumber } from '../utils/Utils';
```

### 定义变量

定义变量centerDistance深度估计距离和centerConfidence深度置信度。

```typescript
let centerDistance: number;
let centerConfidence: number;
```

### 显示深度估计信息

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

在设备界面上显示深度估计信息及深度置信度信息，使用重复调用函数方法在设备界面上实时更新深度估计信息及置信度信息。

```typescript
@Builder
export function ARDepthBuilder(): void {
  ARDepth();
}
let centerDistance: number;
let centerConfidence: number;
@Component
struct ARDepth {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State depthConfidence: number = 0;
  @State depthDistance: string = '0';
  private delayInterval: number = 33;
  private intervalId: number = -1;

  build(): void {
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
          Text('●')
            .fontSize(8)
            .fontColor(Color.Red)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })

          Column() {
            Text(`${this.depthDistance} | ${this.depthConfidence}`)
              .fontColor(Color.Yellow)
              .fontSize(24)
              .textShadow({
                radius: 10,
                color: Color.Black,
                offsetX: 0,
                offsetY: 0
              })
          }
          .alignItems(HorizontalAlign.Center)
          .margin({ bottom: 10 })
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      this.renderDepthMsg();
    })
    .onWillDisappear(() => {
      this.stopARView();
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private initARView(): void {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      viewContext.callback = new ARViewCallbackImpl();
      viewContext.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.AUTOMATIC,
        meshMode: arEngine.ARMeshMode.DISABLED,
        focusMode: arEngine.ARFocusMode.AUTO
      }
      viewContext.init().then(() => {
        this.arContext = viewContext;
        logger.info('Succeeded in initting ARView.');
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}`);
      })
    })
  }

  private renderDepthMsg(): void {
    this.intervalId = setInterval(() => {
      if (centerDistance === undefined || centerConfidence === undefined) {
        return;
      }
      this.depthDistance = centerDistance.toFixed(4);
      this.depthConfidence = centerConfidence;
    }, this.delayInterval)
  }

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    clearInterval(this.intervalId);
    try {
      await this.arContext.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }

    centerDistance = 0;
    centerConfidence = 0;
  }

  private resumeARView(): void {
    // ...
  }

  private pauseARView(): void {
    // ...
  }
}
```

### 获取深度估计信息

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法获取到AR会话对象后进行深度估计，获取深度信息、置信度信息。

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
      let frame: arEngine.ARFrame = session.getFrame();
      let depthImage: arEngine.ARImage = frame.acquireDepthImage16Bits();
      let confidenceImage: arEngine.ARImage = frame.acquireDepthConfidenceImage();
      let depthPlane: number[] = arrayBufferInt32ToNumber(depthImage.planes[0].buffer);
      let confidencePlane: number[] = arrayBufferInt32ToNumber(confidenceImage.planes[0].buffer);
      const index: number = depthImage.height * depthImage.width / 2 + depthImage.width / 2;

      centerDistance = depthPlane[index] / 1000;
      centerConfidence = confidencePlane[index];
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire depth information. Code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

### 获取深度估计信息的自定义方法

自定义数据转换方法arrayBufferInt32ToNumber可参考[数据类型转换说明](arengine-arraybuffer-info.md)。
