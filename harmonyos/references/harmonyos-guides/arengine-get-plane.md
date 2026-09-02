---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-plane
title: 检测环境中的平面（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面识别 > 检测环境中的平面（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:14e672726d0b9c76c0576bffc7a46b4341d67406a3e35cf3b8a4724d93c647e6
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，检测环境平面能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

检测平面通过[ARPlane](../harmonyos-references/arengine-api-arengine.md#arplane)平面对象进行，以下接口为平面相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARTrackable.getPose](../harmonyos-references/arengine-api-arengine.md#artrackablegetpose) | 获取追踪目标的位姿信息。 |
| [ARTrackable.getAnchors](../harmonyos-references/arengine-api-arengine.md#artrackablegetanchors) | 获取绑定到输入可跟踪对象的锚点对象。 |
| [ARPose.getMatrix](../harmonyos-references/arengine-api-arengine.md#arposegetmatrix) | 将位姿数据转换为一个4x4的矩阵。 |
| [ARPlane.getPolygonXZ](../harmonyos-references/arengine-api-arengine.md#arplanegetpolygonxz) | 获取检测到的平面2D顶点数组。 |
| [ARPlane.getSubsumedBy](../harmonyos-references/arengine-api-arengine.md#arplanegetsubsumedby) | 获取平面的父平面（当平面与另一个平面合并时会生成父平面）。 |
| [ARPlane.isPoseInExtents](../harmonyos-references/arengine-api-arengine.md#arplaneisposeinextents) | 检查给定位姿是否在平面的边界矩形内。 |
| [ARPlane.isPoseInPolygon](../harmonyos-references/arengine-api-arengine.md#arplaneisposeinpolygon) | 检查给定位姿是否在平面的边界多边形内。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

平面检测能力所需的模块导入如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CubeGeometry, CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node,
  PrimitiveTopology, Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
import { Matrix4, window } from '@kit.ArkUI';
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

```typescript
@Builder
export function ARWorldBuilder(): void {
  ARWorld();
}
// ...
@Component
struct ARWorld {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State statusBarHeight: number = 0;
  // ...
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
            // ...
        }
      }
    }
    .onAppear(async () => {
      this.initARView();
    })
    .onWillDisappear(async () => {
      await this.stopARView();
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
  // ...
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
        logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
      })
    })
  }
  // ...
}
```

### 检测环境平面

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，通过[ARSession.getAllTrackables](../harmonyos-references/arengine-api-arengine.md#arsessiongetalltrackables)方法获取所有识别到的平面。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
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
      let camera: arEngine.ARCamera = frame.getCamera();
      let trackables: arEngine.ARTrackable[] = [];

      if (camera.state === arEngine.ARTrackingState.TRACKING) {
        trackables = session.getAllTrackables(arEngine.ARTrackableType.PLANE);
        isDisplayCube = true;
      } else {
        isDisplayCube = false;
      }
      // ...
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```

### 检测平面的自定义方法

自定义方法获取顶点数据getVertices、创建索引generateMeshIndex、创建mesh数据generateMeshInput。

```typescript
export function getVertices(mat: Matrix4, point: number[]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < point.length; i += 2) {
    let single: Vec3 = {
      x: (mat[2] * point[i] + mat[6] * 0 + mat[10] * point[i + 1] + mat[14] * 1.0),
      y: mat[1] * point[i] + mat[5] * 0 + mat[9] * point[i + 1] + mat[13] * 1.0,
      z: -(mat[0] * point[i] + mat[4] * 0 + mat[8] * point[i + 1] + mat[12] * 1.0)
    }
    result.push(single);
  }
  return result;
}

/*
 * 创建ARWorld的meshIndex，
 * 由于平面是由三角形拼接而成，
 * 因此，每个平面上每个三角形的第一个顶点索引是相同的。
 */
export function generateMeshIndex(input: Vec3[][]): number[] {
  let result: number[] = [];
  let start: number = 0;

  for (let i = 0; i < input.length; i++) {
    let len: number = input[i].length;

    for (let j = start + 1; j < start + len - 1; j++) {
      result.push(start);
      result.push(j);
      result.push(j + 1);
    }
    start += len;
  }
  return result;
}

export function generateMeshInput(vex: Vec3[][]): Vec3[] {
  let result: Vec3[] = [];
  for (let i = 0; i < vex.length; i++) {
    let tmp: Vec3[] = vex[i];
    for (let j = 0; j < tmp.length; j++) {
      result.push(tmp[j]);
    }
  }
  return result;
}
```
