---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arsession
title: 管理AR会话（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 管理AR会话 > 管理AR会话（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:76780b6e1d9b695053401937a192f8d1ad95a1e61361dba216a83acb11051be5
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，管理AR会话支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持。

## 接口说明

AR会话主要依赖[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，以下接口为AR会话相关接口。详细接口和说明，请参考[arViewController（AR场景管理能力）](../harmonyos-references/arengine-api-arviewcontroller.md)。

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

## 开发步骤

对于使用ArkTS的任何AR应用，从6.1.0(23)开始，AREngine对于任何AR特性，都可以通过[arViewController.isARTypeSupported](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口来查询当前设备是否支持该特性，当判断该设备支持特性后，进行之后的开发工作。

首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。

### 导入模块

导入AR Engine相关模块，导入方法如下。

```typescript
import { arEngine, ARView, arViewController } from '@kit.AREngine';
import {CubeGeometry, CustomGeometry, Geometry, Material, MaterialType, MeshResource, Node,
  PrimitiveTopology, Scene, SceneResourceFactory, Shader, ShaderMaterial, Vec3} from '@kit.ArkGraphics3D';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 初始化AR会话和AR场景

通过[ARViewContext.init](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextinit)方法初始化一个AR会话及场景。

在此之前请确保已获取相机权限，否则将不会加载AR场景，具体指导请参考[前置准备](arengine-preparations.md#前置准备)或者[申请权限](arengine-preparations.md#申请权限)。

AR会话及场景创建好后使用[组件导航（Navigation）](arkts-navigation-navigation.md)组件及[ARView](../harmonyos-references/arengine-api-component-arview.md#arview)组件在设备上显示AR场景，关于[组件导航（Navigation）](arkts-navigation-navigation.md)具体指导可参考[前置准备](arengine-preparations.md#前置准备)。

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

### 使用AR会话对象处理业务

调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法获取AR会话对象，之后可根据开发者所需的具体业务编写处理逻辑。

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
    // ...
  }
}
```

### 暂停AR会话

要暂停AR会话，开发者可以使用[ARViewContext.pause](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextpause)方法，在应用置为后台时可以暂停AR会话和暂停AR场景。

```typescript
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
```

### 恢复AR会话

要恢复暂停的AR会话和AR场景，开发者可以使用[ARViewContext.resume](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextresume)方法。

```typescript
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
```

### 销毁AR会话

退出AR会话和AR场景时，开发者可以使用[ARViewContext.destroy](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontextdestroy)方法同时销毁AR会话及AR场景。

```typescript
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
```

**说明** 

组件生命周期的方法，除[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)、[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)、[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)、[onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)外，还可以使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的[页面生命周期](arkts-navigation-navdestination.md#页面生命周期)所示方法，开发者可根据需要进行选择。
