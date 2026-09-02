---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arworld
title: 物体摆放（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 命中检测 > 物体摆放（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:365a035aca31e828e844d86b89aeb0e1b8e850c13c0d8aafabdb193cee268471
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，物体摆放能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_SLAM](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

AR物体摆放主要依赖[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，以下接口为AR物体摆放相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARViewContext.init](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextinit) | 初始化[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，初始化AR会话和设置AR渲染场景等。 |
| [ARViewContext.pause](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextpause) | 暂停相机跟踪与AR场景渲染。 |
| [ARViewContext.destroy](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextdestroy) | 销毁[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，释放ARView使用资源，包括AR会话与呈现场景销毁，在退出ARView场景时使用。 |
| [ARViewContext.resume](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextresume) | 用于恢复暂停的相机跟踪与AR场景渲染。 |
| [ARViewContext.scene](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextscene) | 设置ARView的AR场景。 |
| [ARViewContext.scene](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextscene-1) | 获得的AR呈现场景，用于管理空间节点。 |
| [ARViewContext.session](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextsession) | 获取AR会话，用于获取相关AR环境跟踪、相机跟踪、命中检测等能力，如相机位姿、平面信息、创建锚点等。 |
| [ARViewContext.config](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextconfig) | 设置AR会话的配置文件，如北向坐标、性能模式等。 |
| [ARViewContext.callback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextcallback) | 设置回调函数，可根据回调功能实现对应业务逻辑。 |
| [ARFrame.getCamera](../harmonyos-references/arengine-api-arengine.md#arframegetcamera) | 获取当前帧的摄像机参数对象。 |
| [ARFrame.getUpdatedTrackables](../harmonyos-references/arengine-api-arengine.md#arframegetupdatedtrackables) | 获取更新后的指定类型的可追踪对象。 |
| [ARFrame.hitTest](../harmonyos-references/arengine-api-arengine.md#arframehittest) | 根据相机投射光线，获取预览区域中的像素坐标（pixelX和pixelY）来确定射线方向，然后检测这个射线在平面或点云中是否有交点。 |
| [ARAnchor.getPose](../harmonyos-references/arengine-api-arengine.md#aranchorgetpose) | 获取锚点在世界坐标系中的位姿信息。 |
| [ARHitResult.getHitPose](../harmonyos-references/arengine-api-arengine.md#arhitresultgethitpose) | 获取交点位姿。 |
| [ARHitResult.getTrackable](../harmonyos-references/arengine-api-arengine.md#arhitresultgettrackable) | 获取被命中的可追踪对象。 |
| [ARPose.getMatrix](../harmonyos-references/arengine-api-arengine.md#arposegetmatrix) | 将位姿数据转换为一个4x4的矩阵。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

AR物体摆放所需要导入的模块如下。

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CubeGeometry, CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node,
  PrimitiveTopology, Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 定义变量

定义变量hitAnchorList存储放置物体处的锚点信息、hitPoseList存储放置物体处的位姿信息和statusBarHeight设备状态栏高度。

```typescript
let frame: arEngine.ARFrame;
let hitPoseList: Vec3[] = [];
let hitAnchorList: arEngine.ARAnchor[] = [];
```

### 显示预览流

在ARView中加入点击事件，进行碰撞检测，获取锚点位姿数据加入列表。

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
            .onClick((event: ClickEvent) => {
              this.objectCollisionDetection(event);
            })
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
  private objectCollisionDetection(event: ClickEvent): void {
    let x: number = this.getUIContext().vp2px(event.windowX);
    let y: number = this.getUIContext().vp2px(event.windowY) - this.statusBarHeight;
    logger.info(`Get onclick position, x: ${x} y: ${y}.`);

    try {
      let result: arEngine.ARHitResult[] = frame.hitTest(x, y);
      logger.info(`The hitresult size is: ${result.length}.`);
      if (!result) {
        return;
      }

      for (let i = 0; i < result.length; i++) {
        let hitResult: arEngine.ARHitResult = result[i];
        let trackable: arEngine.ARTrackable = hitResult.getTrackable();

        if (trackable.type !== arEngine.ARTrackableType.PLANE) {
          continue;
        }

        let hitPlane: arEngine.ARPlane = trackable as arEngine.ARPlane;
        let hitPose: arEngine.ARPose = hitResult.getHitPose();
        let inPolygon: boolean = hitPlane.isPoseInPolygon(hitPose);
        let distance: number = hitResult.distance;
        logger.info(`The hitresult inPolygon is: ${inPolygon}, distance is: ${distance}.`);

        if (!inPolygon || distance <= 0) {
          continue;
        }

        let hitAnchor: arEngine.ARAnchor = hitResult.createAnchor();
        let pos: Vec3 = hitAnchor.getPose().translation;

        hitPoseList.push(pos);
        hitAnchorList.push(hitAnchor);

        if (hitPoseList.length > 10) {
          hitPoseList.splice(0, 1);
          hitAnchorList.splice(0, 1);
        }
      }
      logger.info('Succeeded in getting hit result.');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to get hitResults. Code is ${err.code}, message is ${err.message}.`);
    }
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
  private resumeARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.resume();
      isStopFrameUpdate = false;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}.`);
    }
  }
  private pauseARView(): void {
    if (!this.arContext) {
      return;
    }
    try {
      this.arContext.pause();
      isStopFrameUpdate = true;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}.`);
    }
  }
}
```

### 渲染识别的平面和放置的物体

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，获取平面信息。

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
      frame = session.getFrame();
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
