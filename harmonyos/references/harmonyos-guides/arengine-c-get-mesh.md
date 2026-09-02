---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-mesh
title: 获取网格扫描信息（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 环境Mesh识别 > 获取网格扫描信息（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:24cebcfd94c726bcf1179847c7bf47d7e191b1b14bc0551d251799ae6f057ed1
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从5.1.0(18)开始，获取网格扫描信息能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持环境Mesh识别特性（[ARENGINE\_FEATURE\_TYPE\_MESH](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR网格扫描相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到\*outFrame中。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的openGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARFrame\_AcquireSceneMesh](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirescenemesh) | 获取当前帧的mesh信息。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize) | 获取mesh的顶点个数。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexlist) | 获取mesh顶点集合。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize) | 获取mesh面片的索引个数。 |
| [HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlist) | 获取mesh面片的索引集合。 |
| [HMS\_AREngine\_ARSceneMesh\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_release) | 释放当前帧的mesh信息。 |

## 开发步骤

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

创建一个UI界面，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于显示相机预览画面，并定时触发每一帧绘制。

```typescript
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARMeshBuilder() {
  ARMesh();
}

@Component
struct ARMesh {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State rotation: number = 0;
  private interval: number = -1;
  private xComponentId: string = 'ARMesh';
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
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              // 调用Native API更新方法，使AR Engine更新每一帧的计算结果。
              arEngineDemo.update(this.idStr);
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置为开启mesh模式。

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
HMS_AREngine_ARConfig_SetMeshMode(mArSession, arConfig, ARENGINE_MESH_MODE_ENABLED);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### 获取当前环境中的mesh信息

调用[HMS\_AREngine\_ARFrame\_AcquireSceneMesh](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirescenemesh)函数，获取当前环境中的mesh信息，并将结果存放在sceneMesh中。

```
AREngine_ARSceneMesh *outSceneMesh = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireSceneMesh(arSession, arFrame, &outSceneMesh);
```

### 获取当前mesh信息对应的mesh顶点信息

1. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireVerticesSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireverticessize)函数，获取mesh顶点信息包含的浮点数数量，每三个浮点数组成一个mesh顶点，将结果存放在meshVerticesSize 中。

   ```
   int32_t meshVerticesSize = 0;
   HMS_AREngine_ARSceneMesh_AcquireVerticesSize(session, sceneMesh, &meshVerticesSize);
   ```
2. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireVertexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquirevertexlist)函数，获取mesh顶点信息，并将结果保存在meshVertices中。

   ```
   float *meshVertices = new float[meshVerticesSize];
   auto ret = HMS_AREngine_ARSceneMesh_AcquireVertexList(session, sceneMesh, meshVertices, meshVerticesSize);
   LOGD("HMS_AREngine_ARSceneMesh_AcquireVertexList result=%{public}d.", ret);
   mPointsNum = meshVerticesSize / FLOATS_PER_POINT;
   ```

### 获取当前mesh信息对应的mesh面片信息

1. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireIndexListSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlistsize)函数，获取mesh面片信息对应顶点的索引个数，每三个顶点索引表示一个mesh面片，将结果存放在triangleIndicesSize 中。

   ```
   int32_t triangleIndicesSize = 0;
   HMS_AREngine_ARSceneMesh_AcquireIndexListSize(session, sceneMesh, &triangleIndicesSize);
   ```
2. 调用[HMS\_AREngine\_ARSceneMesh\_AcquireIndexList](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arscenemesh_acquireindexlist)函数，获取mesh面片信息对应顶点的索引列表，并将结果保存在meshTriangleIndices中。

   ```
   int32_t *meshTriangleIndices = new int32_t[triangleIndicesSize];
   ret = HMS_AREngine_ARSceneMesh_AcquireIndexList(session, sceneMesh, meshTriangleIndices, triangleIndicesSize);
   LOGD("HMS_AREngine_ARSceneMesh_AcquireIndexList result=%{public}d.", ret);

   mTrianglesNum = triangleIndicesSize / INT_PER_TRIANGLE;
   ```

### 使用完毕后，销毁mesh信息

```cpp
HMS_AREngine_ARSceneMesh_Release(outSceneMesh);
```
