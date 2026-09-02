---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-volume-measurement
title: 高精几何重建（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 高精几何重建 > 高精几何重建（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:def4f40f9ee18429bcb21b8066b2a01e808f94909744079bc40bbb3811f38430
---

## 约束与限制

从6.0.0(20)开始，高精几何重建能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持高精几何重建特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

高精几何重建主要依赖[ARSemanticDenseData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedata)，以下接口为高精几何重建的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARFrame.acquireSemanticDense](../harmonyos-references/arengine-api-arengine.md#arframeacquiresemanticdense) | 返回当前帧的高精几何重建对象数据。 |
| [ARSemanticDenseData.acquireCubeData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedataacquirecubedata) | 返回一个高精几何重建对象的立方体数据信息的列表。 |
| [ARSemanticDenseData.release](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedatarelease) | 释放高精几何重建对象数据。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

高精几何重建能力所需要导入的模块如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import { Node, Scene, Vec3 } from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量cubeVertexData接收立方体顶点数据，定义变量cubeConfidence接收识别出立方体的置信度数据，定义变量cubeLabel接收立方体的语义信息。

```typescript
let cubeVertexData: number[];
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改semanticDenseMode为[ARSemanticDenseMode](../harmonyos-references/arengine-api-arengine.md#arsemanticdensemode).CUBE\_VOLUME，启用体积测量识别能力。

```typescript
@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense()
}

let arSession: arEngine.ARSession;
let frame: arEngine.ARFrame
let semanticData: arEngine.ARSemanticDenseData
let cubeVertexData: number[];
let cubeConfidence: number;
let cubeLabel: arEngine.ARSemanticPlaneLabel;

@Component
struct ARSemanticDense {
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
    .onAppear(() => {
      this.initARView()
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
    Scene.load().then(async (scene: Scene) => {
      let ret :boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE);
      logger.info('ARSemanticDense isARTypeSupported is' + ret);
      let context = new arViewController.ARViewContext()
      context.scene = scene
      context.callback = new ARViewCallbackImpl()
      context.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
        powerMode: this.params?.powerMode,
        semanticDenseMode: arEngine.ARSemanticDenseMode.CUBE_VOLUME
      };
      context.init().then(() => {
        this.arContext = context;
        // ...
      });
    })
  }
}
```

### 获取立方体体积数据

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧，通过[ARFrame.acquireSemanticDense](../harmonyos-references/arengine-api-arengine.md#arframeacquiresemanticdense)获得当前帧的高精几何重建对象数据，通过[ARSemanticDenseData.acquireCubeData](../harmonyos-references/arengine-api-arengine.md#arsemanticdensedataacquirecubedata)从高精几何重建对象数据中获取识别到的立方体顶点数据，经过计算可以得到立方体的体积信息，相关变量定义参考[定义变量](arengine-volume-measurement.md#定义变量)。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
    let session: arEngine.ARSession | undefined = ctx.session;
    if (session) {
      arSession = session;
      frame = session.getFrame()
      if (!frame){
        // ...
      } else {
        semanticData = frame.acquireSemanticDense();
        if(semanticData !== undefined){
          // ...
          if(semanticData.cubeDataSize>0){
            let semanticCubeData: arEngine.ARSemanticDenseCubeData = semanticData.acquireCubeData()[0];
            cubeVertexData = semanticCubeData.vertexData;
            cubeConfidence = semanticCubeData.confidence;
            cubeLabel = semanticCubeData.label;
            // ...
          }
        }
        semanticData.release()
        semanticData.timestamp
      }
      releaseFrame(frame);
    // ...
    }
  }
}
```
