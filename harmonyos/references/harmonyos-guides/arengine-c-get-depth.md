---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-depth
title: 获取深度图（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 深度估计 > 获取深度图（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:36249ee29dcfa8b7c50d029f297c3cc4f1c96bf099ca9d4f91901527162e0c83
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从5.0.5(17)开始，获取深度估计信息能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持深度估计特性（[ARENGINE\_FEATURE\_TYPE\_DEPTH](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR深度估计相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的OpenGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARConfig\_SetDepthMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setdepthmode) | 设置深度模式。 |
| [HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthimage16bits) | 获取当前帧的深度图像。 |
| [HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthconfidenceimage) | 获取当前帧的深度图像对应的置信度信息。 |

## 开发步骤

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个UI界面ARDepth.ets，用于选择是否开启深度图渲染模式。

```typescript
@Builder
export function ARDepthBuilder() {
  ARDepth();
}

@Component
struct ARDepth {
  pageInfos: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.close_depth_render'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushPathByName('ARDepthRender', 0);
          })

        Button($r('app.string.open_depth_render'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushPathByName('ARDepthRender', 1);
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

最后创建一个ARDepthRender.ets，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于加载相机预览画面，并定时触发每一帧绘制。

```typescript
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARDepthRenderBuilder() {
  ARDepthRender();
}

@Component
struct ARDepthRender {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State distance: string = '';
  @State rotation: number = 0;
  private interval: number = -1;
  private isUpdate: boolean = true;
  private params: number = 0;
  private xComponentId: string = 'ARDepth';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // 调用Native API更新方法，使AR Engine更新每一帧的计算结果。
                arEngineDemo.update(this.idStr);
                this.distance = arEngineDemo.getDistance(this.idStr);
              }
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })

        Text(this.distance)
          .fontColor(Color.Yellow)
          .fontSize(24)
          .textShadow({
            radius: 10,
            color: Color.Black,
            offsetX: 0,
            offsetY: 0
          })
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([0, this.params, 1, this.rotation]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.params = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置为开启深度模式。

```
// 创建一个AREngine_ARSession会话。
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
// 配置AREngine_ARSession。
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARConfig_SetDepthMode(mArSession, arConfig, ARENGINE_DEPTH_MODE_AUTOMATIC));
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### 获取当前环境中的深度图

调用[HMS\_AREngine\_ARFrame\_AcquireDepthImage16Bits](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthimage16bits)函数，获取当前环境中的深度信息，并将结果存放在depthImage中。

```
AREngine_ARImage *depthImage = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireDepthImage16Bits(arSession, arFrame, &depthImage);
```

### 获取当前深度图对应的深度置信度图

调用[HMS\_AREngine\_ARFrame\_AcquireDepthConfidenceImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiredepthconfidenceimage)函数，获取当前深度图对应的置信度图。

```
AREngine_ARImage *depthConfidenceImage = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(arSession, arFrame, &depthConfidenceImage);
```

### 获取深度图和深度置信度图中的值

深度图和深度置信度图包装为[AREngine\_ARImage](../harmonyos-references/arengine-capi-arengine.md#arengine_arimage)对象，可以通过此对象获取对应的深度图和深度置信度图。

```
AREngine_ARImageFormat format;
CHECK(HMS_AREngine_ARImage_GetFormat(arSession, depthConfidenceImage, &format));
int32_t depthWidth;
CHECK(HMS_AREngine_ARImage_GetWidth(arSession, depthConfidenceImage, &depthWidth));
 int32_t depthHeight;
CHECK(HMS_AREngine_ARImage_GetHeight(arSession, depthConfidenceImage, &depthHeight));
uint8_t *depthConfidenceData = nullptr;
int32_t depthConfidenceLength = 0;
CHECK(HMS_AREngine_ARImage_GetPlaneData(
    arSession, depthConfidenceImage, 0,
    reinterpret_cast<const uint8_t **>(static_cast<void *>(&depthConfidenceData)), &depthConfidenceLength));
```

### 使用完毕后，销毁深度图和深度置信度图

```cpp
HMS_AREngine_ARImage_Release(depthConfidenceImage);
```
