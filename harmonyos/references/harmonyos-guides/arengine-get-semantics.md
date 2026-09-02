---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-semantics
title: 识别平面语义（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 平面语义 > 识别平面语义（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:2a8a95d8578cf7327b903b403d351717eafe94cf8b8241252612856cb391b33e
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，识别平面语义能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持平面及物体语义特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

获取平面语义信息可以通过[ARPlane](../harmonyos-references/arengine-api-arengine.md#arplane)平面对象获取，以下接口为平面相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

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

识别平面语义之前需要先检测识别环境中的平面，如何检测识别环境中的平面请参考[检测环境中的平面](arengine-get-plane.md)。

### 导入模块

识别平面语义能力所需要导入的模块如下：

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {Camera, CustomGeometry, Geometry, Image, Material, MaterialType, Node, PrimitiveTopology,
  Scene, SceneResourceFactory, Shader, ShaderMaterial} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量planeLabel接收平面类型标签信息。

```typescript
let arSession: arEngine.ARSession;
let planeLabel: arEngine.ARSemanticPlaneLabel;
```

### 显示平面语义信息

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改semanticMode为[ARSemanticMode](../harmonyos-references/arengine-api-arengine.md#arsemanticmode).PLANE，启用平面语义识别能力。

在设备界面上显示识别到平面的信息，使用重复调用函数方法在设备界面上实时更新识别到的平面语义信息。

```typescript
@Builder
export function ARTargetBuilder() {
  ARTarget()
}
// ...

@Component
struct ARTarget {
  @State arContext?: arViewController.ARViewContext = undefined;
  @State targetPlaneLabel: arEngine.ARSemanticPlaneLabel = planeLabel;
  private intervalId: number = -1;
  private delayInterval: number = 33;
  private params: arEngine.ARConfig = { type: arEngine.ARType.WORLD };
  // ...

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
            Text(`Label: ${convertSemanticLabel(this.targetPlaneLabel)}`)
              .infoStyles()
          }
          .alignItems(HorizontalAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
        }
      }
    }
    .onAppear(() => {
      this.initARView();
      this.intervalId = setInterval(async () => {
        this.targetPlaneLabel = planeLabel;
        // ...
      }, this.delayInterval);
    })
    .onWillDisappear(() => {
      // ...
    })
    .onShown(() => {
      this.resumeARView();
    })
    .onHidden(() => {
      this.pauseARView();
    })
    // ...
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
    Scene.load().then(async (scene) => {
      let context = new arViewController.ARViewContext();
      context.scene = scene;
      context.callback = new ARViewCallbackImpl();
      context.config = {
        type: arEngine.ARType.WORLD,
        planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
        powerMode: this.params?.powerMode,
        semanticMode: 3,
        poseMode: this.params?.poseMode,
        depthMode: this.params?.depthMode,
        meshMode: this.params?.meshMode,
      };
      context.init().then(() => {
        this.arContext = context;
        // ...
      });
      // ...
    });
  }
}
```

### 获取语义信息

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，在设备界面上显示识别到的平面类型。

增加获取语义信息的方法plane.label，获取每一帧识别到的平面语义信息。

```typescript
class ARViewCallbackImpl extends arViewController.ARViewCallback {
  // ...
  onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
  }

  async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
    if (!ctx.session) {
      // ...
      return;
    }
    arSession = ctx.session;

    let frame = arSession.getFrame();
    let camera = frame.getCamera();
    if (!camera) {
      // ...
    } else {
      // 更新帧数据。
      let trackables: arEngine.ARTrackable[] = arSession.getAllTrackables(arEngine.ARTrackableType.PLANE);
      for (let i = 0; i < trackables.length; ++i) {
        let plane: arEngine.ARPlane = trackables[i] as arEngine.ARPlane;
        // ...
        planeLabel = plane.label;
        // ...
      }
    }
    // ...
  }
}
```

### 识别平面语义的自定义方法

自定义方法获取顶点数据getVertices、创建索引generateMeshIndex、创建mesh数据generateMeshInput，可参考[检测平面的自定义方法](arengine-get-plane.md#检测平面的自定义方法)。

arrayBufferFloat32ToNumber可以参考[数据类型转换说明](arengine-arraybuffer-info.md)。

平面语义标签转换convertSemanticLabel可参考如下。

```typescript
export function convertSemanticLabel(obj: number): string {
  let res: string = '';
  if (obj === 0) {
    res = 'UNKNOWN';
  } else if (obj === 1) {
    res = 'WALL';
  } else if (obj === 2) {
    res = 'FLOOR';
  } else if (obj === 3) {
    res = 'SEAT';
  } else if (obj === 4) {
    res = 'TABLE';
  } else if (obj === 5) {
    res = 'CEILING';
  } else if (obj === 6) {
    res = 'DOOR';
  } else if (obj === 7) {
    res = 'WINDOW';
  } else if (obj === 8) {
    res = 'BED';
  } else if (obj === 9) {
    res = 'PLANE SPACE';
  } else if (obj === 10) {
    res = 'CUBE VOLUME';
  } else if (obj === 11) {
    res = 'CUBE SPACE';
  }
  return res;
}
```
