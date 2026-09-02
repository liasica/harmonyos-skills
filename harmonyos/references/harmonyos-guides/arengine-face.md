---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-face
title: 人脸跟踪（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人脸识别与跟踪 > 人脸跟踪（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:b3999664b699c801bf798d929ad54fd52787a98cfa2902145e348be1698762a5
---

## 约束与限制

从6.1.0(23)开始，人脸跟踪能力支持部分Phone、部分Tablet、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持人脸识别与跟踪特性（[ARENGINE\_FEATURE\_TYPE\_FACE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

人脸跟踪主要依赖ARFace，以下接口为人脸跟踪的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables) | 获取当前session中包含的人脸对象。 |
| [ARFace.getGeometry](../harmonyos-references/arengine-api-arengine.md#arfacegetgeometry) | 返回一个人脸几何对象。 |
| [ARFace.getBlendShapes](../harmonyos-references/arengine-api-arengine.md#arfacegetblendshapes) | 返回一个人脸微表情对象。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要参考[AR特性检查](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口检查当前设备是否支持该特性。若设备支持，创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

人脸跟踪能力所需要导入的模块如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node, PrimitiveTopology,
  Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';
import {arrayBufferFloat32ToNumber, arrayBufferInt32ToNumber, generateFaceMeshIndex,
  generateMeshInput, getFaceFrontVertices} from '../utils/Utils';
```

### 定义变量

定义变量face接收人脸对象，定义变量faceGeometry接收人脸几何对象，定义变量faceBlendShapes接收人脸微表情对象。

```typescript
let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
// ...
// 数据处理。
let faceGeometry: arEngine.ARGeometry = face.getGeometry();
let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改type为[ARType](../harmonyos-references/arengine-api-arengine.md#artype).FACE，更改cameraLensFacing为[ARCameraLensFacing](../harmonyos-references/arengine-api-arengine.md#arcameralensfacing).FRONT，更改multiFaceMode为[ARMultiFaceMode](../harmonyos-references/arengine-api-arengine.md#armultifacemode).MULTIFACE\_ENABLE，启用前置相机的人脸跟踪能力。

```typescript
@Builder
export function ARFaceBuilder() {
  ARFace();
}
// ...
@Component
export struct ARFace {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State arContext?: arViewController.ARViewContext = undefined;

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
        }
      }
    }
    .onAppear(async () => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
      this.clearGlobalVariables();
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

  private async stopARView(): Promise<void> {
    if (!this.arContext) {
      return;
    }
    try {
      await this.arContext.destroy();
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
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
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}`);
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
      logger.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private initARView(): void {
    Scene.load().then(async (result: Scene) => {
      try {
        let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
        logger.info(`ARFace isARTypeSupported is ${ret}`);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(
          `Failed to get whether the device is support ARFace. Code is ${err.code}, message is ${err.message}`);
      }

      let context = new arViewController.ARViewContext();
      context.scene = result;
      context.callback = new ARViewCallbackImpl();
      context.config = {
        type: arEngine.ARType.FACE,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: arEngine.ARPowerMode.NORMAL,
        focusMode: arEngine.ARFocusMode.AUTO,
        cameraLensFacing: arEngine.ARCameraLensFacing.FRONT,
        multiFaceMode: arEngine.ARMultiFaceMode.MULTIFACE_ENABLE,
      };
      context.init().then(() => {
        this.arContext = context;
      }).catch((err: BusinessError) => {
        logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}`);
      });
    })
  }
  // ...
}
```

### 获取人脸几何数据和微表情数据

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧，通过[ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables)获得当前会话包含的人脸对象数据，通过[ARFace.getGeometry](../harmonyos-references/arengine-api-arengine.md#arfacegetgeometry)和[ARFace.getBlendShapes](../harmonyos-references/arengine-api-arengine.md#arfacegetblendshapes)从人脸对象数据中获取识别到的几何信息和微表情信息，相关变量定义参考[定义变量](arengine-face.md#定义变量)。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      logger.error('arSession is undefined');
      return;
    }

    let session: arEngine.ARSession = ctx.session;
    // ...
    try {
      let mesh = new CustomGeometry();
      let geometry: Geometry | null = null;
      if (session == null) {
        logger.error('session is null');
      }

      let vertexArray: Vec3[][] = [];
      let indexArray: Map<number, number[]> = new Map;

      // 获取人脸数据。
      let trackables: arEngine.ARTrackable[] = session.getAllTrackables(arEngine.ARTrackableType.FACE);
      logger.debug(`the faceList length is ${trackables.length}`);
      for (let i = 0; i < trackables.length; ++i) {
        let face: arEngine.ARFace = trackables[i] as arEngine.ARFace;
        let centerPose = face.getPose();
        let viewMatrix = centerPose.getMatrix();

        if (trackables[i].state !== arEngine.ARTrackingState.TRACKING) {
          logger.error(`Face not in tracking state`);
          continue;
        }
        // 数据处理。
        let faceGeometry: arEngine.ARGeometry = face.getGeometry();
        let faceBlendShapes: arEngine.ARBlendShapes = face.getBlendShapes();
        let tmpVert = faceGeometry.getVertices();
        let tmpIndices = faceGeometry.getIndices();
        faceVertices = arrayBufferFloat32ToNumber(tmpVert);
        let faceIndices: number[] = arrayBufferInt32ToNumber(tmpIndices);
        vertexArray.push(getFaceFrontVertices(viewMatrix, faceVertices));
        indexArray.set(i, faceIndices);

        // BlendShapes打印。
        logger.info('the count of blendShapes is' + faceBlendShapes.count);
        logger.info('the data of blendShapes is' + arrayBufferFloat32ToNumber(faceBlendShapes.getData()));
        logger.info('the types of blendShapes is' + faceBlendShapes.getTypes());
      }

      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to acquire face information. Code is ${err.code}, message is ${err.message}`)
    }
  }
}
```
