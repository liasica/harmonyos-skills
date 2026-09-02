---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-body
title: 人体跟踪与骨骼关键点识别（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人体骨骼点识别与跟踪 > 人体跟踪与骨骼关键点识别（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:d4696f02345fe59f8a5610f36426b04dee0fc42d7d059b93b7f74c2f04606259
---

## 约束与限制

从6.1.0(23)开始，人体骨骼点识别与跟踪能力支持部分Phone、部分Tablet、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持人体骨骼点识别与跟踪特性（[ARENGINE\_FEATURE\_TYPE\_BODY](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

人体跟踪与骨骼关键点识别主要依赖ARBody，以下接口为人体跟踪与骨骼关键点识别的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARFrame.acquireBodySkeleton](../harmonyos-references/arengine-api-arengine.md#arframeacquirebodyskeleton) | 返回人体跟踪的人体对象数组。 |
| [ARBody.getLandmarks2D](../harmonyos-references/arengine-api-arengine.md#arbodygetlandmarks2d) | 返回一个人体对象的骨骼关键点数组。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

人体跟踪与骨骼关键点识别能力需要导入的模块如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene } from '@kit.ArkGraphics3D';
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
```

### 结构定义

```typescript
interface BodyInfo {
  trackId: number,
  landmarks: arEngine.ARBodyLandmark2D[]
}

function arLandmarksToMap(
  arLandmarks: arEngine.ARBodyLandmark2D[]): Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D> {
  let typeToLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D> = new Map();
  for (let arLandmark of arLandmarks) {
    typeToLandmarks.set(arLandmark.type, arLandmark);
  }
  return typeToLandmarks;
}

type OnBodyInfoCallback = (bodyInfo: arEngine.ARBody[]) => void;

const DEFAULT_WIDTH: number = 1440;
const DEFAULT_HEIGHT: number = 1080;
const DEFAULT_CONVERT_FACTOR: number = 4 / 3;
const FULL_SCREEN_SIZE: string = '100%';
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改type为[ARType](../harmonyos-references/arengine-api-arengine.md#artype).BODY。

```typescript
@Builder
export function ARBodyBuilder() {
  ARBody();
}

@ComponentV2
struct ARBody {
  @Local arContext?: arViewController.ARViewContext = undefined;
  @Local bodyInfos: BodyInfo[] = [];
  @Local displayWidth: number = DEFAULT_WIDTH;
  @Local displayHeight: number = DEFAULT_HEIGHT;
  private uiContext: UIContext = this.getUIContext();

  build() {
    NavDestination() {
      Stack() {
        Column() {
          RelativeContainer() {
            if (this.arContext) {
              ARView({ context: this.arContext })
                .height(FULL_SCREEN_SIZE)
                .width(FULL_SCREEN_SIZE)
                .alignRules({
                  center: { anchor: '__container__', align: VerticalAlign.Center },
                  middle: { anchor: '__container__', align: HorizontalAlign.Center }
                })
            }
          }
        }
        .width(this.uiContext.px2vp(this.displayWidth))
        .height(this.uiContext.px2vp(this.displayHeight))
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)

        this.drawBodyPerception()
      }
      .width(FULL_SCREEN_SIZE)
      .height(FULL_SCREEN_SIZE)
    }
    .onAppear(() => {
      this.initARView();
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

  @Builder
  drawBodyPerception() {
    Shape() {
      ForEach(this.bodyInfos, (bodyInfo: BodyInfo) => {
        this.drawBodyBones(arLandmarksToMap(bodyInfo.landmarks));
        this.drawBodyLandmarks(bodyInfo.landmarks);
      })
    }
    .width(this.uiContext.px2vp(this.displayWidth))
    .height(this.uiContext.px2vp(this.displayHeight))
  }

  @Builder
  drawBodyLandmarks(bodyLandmarks: arEngine.ARBodyLandmark2D[]) {
    ForEach(bodyLandmarks, (landmark: arEngine.ARBodyLandmark2D) => {
      Circle({ width: 4, height: 4 })
        .position({
          x: this.uiContext.px2vp(landmark.x),
          y: this.uiContext.px2vp(landmark.y)
        })
        .fillOpacity(1)
        .fill(Color.White)
    })
  }

  @Builder
  drawBodyBones(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>) {
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
      Color.Orange);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
      Color.Orange);

    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
      arEngine.ARBodyLandmarkType.RIGHT_SHOULDER, Color.Orange);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
      arEngine.ARBodyLandmarkType.RIGHT_HIP, Color.Orange);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.LEFT_HIP,
      Color.Orange);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP,
      arEngine.ARBodyLandmarkType.LEFT_SHOULDER, Color.Orange);

    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
      arEngine.ARBodyLandmarkType.LEFT_ELBOW, Color.Green);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_ELBOW, arEngine.ARBodyLandmarkType.LEFT_WRIST,
      Color.Green);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP, arEngine.ARBodyLandmarkType.LEFT_KNEE,
      Color.Green);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_KNEE, arEngine.ARBodyLandmarkType.LEFT_ANKLE,
      Color.Green);

    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
      arEngine.ARBodyLandmarkType.RIGHT_ELBOW, Color.Blue);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_ELBOW,
      arEngine.ARBodyLandmarkType.RIGHT_WRIST, Color.Blue);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
      Color.Blue);
    this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
      arEngine.ARBodyLandmarkType.RIGHT_ANKLE, Color.Blue);
  }

  @Builder
  drawBodyBoneLine(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>,
    start: arEngine.ARBodyLandmarkType, end: arEngine.ARBodyLandmarkType, color: Color) {
    if (bodyLandmarks.has(start) && bodyLandmarks.has(end)) {
      Line()
        .startPoint([this.uiContext.px2vp(bodyLandmarks.get(start)?.x),
          this.uiContext.px2vp(bodyLandmarks.get(start)?.y)])
        .endPoint([this.uiContext.px2vp(bodyLandmarks.get(end)?.x), this.uiContext.px2vp(bodyLandmarks.get(end)?.y)])
        .stroke(color)
        .strokeWidth(3)
    }
  }

  private onBodyInfoCb: OnBodyInfoCallback = (bodyInfos: arEngine.ARBody[]) => {
    let preWidth = this.displayWidth;
    let preHeight = this.displayHeight;
    try {
      if (display.getDefaultDisplaySync().availableWidth < display.getDefaultDisplaySync().availableHeight) {
        this.displayWidth = display.getDefaultDisplaySync().availableWidth;
        this.displayHeight = this.displayWidth * DEFAULT_CONVERT_FACTOR;
      } else {
        this.displayHeight = display.getDefaultDisplaySync().availableHeight;
        this.displayWidth = this.displayHeight * DEFAULT_CONVERT_FACTOR;
      }
    } catch (e) {
      logger.error(`display.getDefaultDisplaySync failed error.message:${e?.message}, error.code:${e?.code}`);
      this.displayWidth = preWidth;
      this.displayHeight = preHeight;
    }

    this.bodyInfos = bodyInfos.map((value: arEngine.ARBody) => {
      let landmarks: arEngine.ARBodyLandmark2D[] = [];
      try {
        landmarks = value.getLandmarks2D();
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(`Failed to get Landmarks2D. Code is ${err.code}, message is ${err.message}`);
      }
      landmarks.forEach((value: arEngine.ARBodyLandmark2D) => {
        value.x = value.x * this.displayWidth;
        value.y = value.y * this.displayHeight;
      })
      let info: BodyInfo = {
        trackId: value.trackId,
        landmarks: landmarks
      }
      return info;
    })
  }

  private async initARView(): Promise<void> {
    Scene.load().then(async (scene: Scene) => {
      let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
      viewContext.scene = scene;
      let callback = new ARViewCallbackImpl();
      callback.setCallback(this.onBodyInfoCb);
      viewContext.callback = callback;
      viewContext.config = {
        type: arEngine.ARType.BODY,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: arEngine.ARPowerMode.NORMAL,
        semanticMode: arEngine.ARSemanticMode.NONE,
        poseMode: arEngine.ARPoseMode.GRAVITY,
        depthMode: arEngine.ARDepthMode.DISABLED,
        meshMode: arEngine.ARMeshMode.DISABLED,
        focusMode: arEngine.ARFocusMode.AUTO,
        maxDetectedBodyNum: 1,
        cameraLensFacing: 0
      };
      viewContext.init().then(() => {
        this.arContext = viewContext;
        logger.info('Succeeded in initializing ARView.');
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
      })
    })
  }

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      await this.arContext.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private pauseARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.pause();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}.`);
    }
  }

  private resumeARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.resume();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```

### 获取人体跟踪对象数组和人体骨骼关键点数据

1. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新。
2. 通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧。
3. 通过[ARFrame.acquireBodySkeleton](../harmonyos-references/arengine-api-arengine.md#arframeacquirebodyskeleton)获得当前会话包含的人体对象数组。
4. 通过[ARBody.getLandmarks2D](../harmonyos-references/arengine-api-arengine.md#arbodygetlandmarks2d)获取人体对象骨骼关键点数组。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  private callback?: OnBodyInfoCallback;

  setCallback(cb: OnBodyInfoCallback) {
    this.callback = cb;
  }

  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      return;
    }
    logger.info('onFrameUpdate enter');
    const arSession: arEngine.ARSession = ctx.session;
    try {
      const frame: arEngine.ARFrame = arSession.getFrame();
      const bodies: arEngine.ARBody[] = frame.acquireBodySkeleton();
      this.callback ? this.callback(bodies) : logger.error(`callback not set`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```
