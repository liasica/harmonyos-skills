---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-volume-measurement
title: 高精几何重建（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 高精几何重建 > 高精几何重建（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:48+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:9becb596448c0402e596748efa2e8d3b44d372c20ebb5a8fb5435ff99812d2d8
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从6.0.0(20)开始，高精几何重建能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持高精几何重建特性（[ARENGINE\_FEATURE\_TYPE\_SEMANTIC\_DENSE](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AREngine高精几何重建相关接口，详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiresemanticdensedata) | 获取当前帧的高精几何重建对象数据。 |
| [HMS\_AREngine\_ARConfig\_GetSemanticDenseMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_getsemanticdensemode) | 获取已设置的高精几何重建模式。 |
| [HMS\_AREngine\_ARConfig\_SetSemanticDenseMode](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setsemanticdensemode) | 设置当前所需的高精几何重建模式。 |
| [HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata) | 获取识别到的高精几何重建对象数据中的立方体数据。 |
| [HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedatasize) | 获取识别到的高精几何重建对象数据中的立方体数量。 |
| [HMS\_AREngine\_ARSemanticDense\_Release](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_release) | 释放高精几何重建对象。 |

## 开发步骤

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个UI界面ARSemanticDense.ets，用于选择高精几何重建相关模式。

```typescript
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseBuilder() {
  ARSemanticDense();
}

@Component
struct ARSemanticDense {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {
    NavDestination() {
      Column() {
        Button($r('app.string.semantic_dense_normal'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 0).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 0. Code is ${err.code}, message is ${err.message}.`);
            });
          })

        Button($r('app.string.semantic_dense_cube_volume'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 1).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 1. Code is ${err.code}, message is ${err.message}.`);
            })
          })

        Button($r('app.string.semantic_dense_cube_space'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARSemanticDenseRender', 2).catch((err: BusinessError) => {
              logger.error(
                `ARSemanticDenseRender failed to pushDestinationByName 2. Code is ${err.code}, message is ${err.message}.`);
            })
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

最后创建一个ARSemanticDenseRender.ets，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件用于加载相机预览画面，并定时触发每一帧绘制。

```typescript
import { display } from '@kit.ArkUI';
import { systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARSemanticDenseRenderBuilder() {
  ARSemanticDenseRender();
}

@Component
struct ARSemanticDenseRender {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State showPage: boolean = true;
  @State rotation: number = 0;
  @State volume: string = '';
  private xComponentId: string = 'ARSemanticDense';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  private interval: number = -1;
  private inputInterval: number = -1;
  private getCubeInfoInterval: number = -1;
  private isUpdate: boolean = false;
  private semanticDenseMode: number = 0;
  aboutToAppear(): void {
    try {
      this.rotation = display.getDefaultDisplaySync().rotation
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
    }
  }
  build(): void {
    NavDestination() {
      RelativeContainer() {

        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .opacity(0.2)
          .width('100%')
          .height('100%')
          .zIndex(0.1)
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
                if (this.semanticDenseMode != 0) {
                  this.volume = arEngineDemo.getVolume(this.idStr);
                }
              }
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            if (this.interval !== -1) {
              clearInterval(this.interval);
              this.interval = -1;
            }

            if (this.inputInterval !== -1) {
              clearInterval(this.inputInterval);
              this.inputInterval = -1;
            }

            if (this.getCubeInfoInterval !== -1) {
              clearInterval(this.getCubeInfoInterval);
              this.getCubeInfoInterval = -1;
            }
          })

        Text(this.volume)
          .fontColor(Color.Red)
          .fontSize(14)
          .textAlign(TextAlign.Center)
          .alignRules({
            bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation, 2, this.semanticDenseMode]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(async () => {
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
      this.semanticDenseMode = context.pathInfo.param as number;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话并配置高精几何重建相关模式

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
SetSemanticDenseMode(params.semanticDenseMode, mArSession, arConfig);
AREngine_ARSemanticDenseMode outSemanticDenseMode = ARENGINE_SEMANTIC_DENSE_MODE_DISABLED;
HMS_AREngine_ARConfig_GetSemanticDenseMode(mArSession, arConfig, &outSemanticDenseMode);
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### 获取当前环境中的高精几何重建信息

创建一个帧对象，调用[HMS\_AREngine\_ARFrame\_AcquireSemanticDenseData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquiresemanticdensedata)函数，从当前帧中获取环境中的高精几何重建信息，其中包含了环境中的稠密点云信息和立方体信息。

```
AREngine_ARSemanticDenseData *arSemanticDense = nullptr;
auto ret = HMS_AREngine_ARFrame_AcquireSemanticDenseData(arSession, arFrame, &arSemanticDense);
```

### 获取高精几何重建信息中的立方体数据

1. 调用[HMS\_AREngine\_ARSemanticDense\_AcquireCubeData](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedata)函数，获取当前环境中的立方体数据，立方体的数据结构详情参考[AREngine\_ARSemanticDenseCubeData](../harmonyos-references/arengine-struct-arsemanticdensecubedata.md)。

   ```
   HMS_AREngine_ARSemanticDense_AcquireCubeData(arSession, arSemanticDense, &semanticDenseCubeData);
   ```
2. 调用[HMS\_AREngine\_ARSemanticDense\_AcquireCubeDataSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsemanticdense_acquirecubedatasize)函数，获取当前环境中的立方体数量，如果立方体数量大于0，即可从中获取单个立方体的数据进行绘制和体积计算。

   ```
   HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(arSession, arSemanticDense, &cubeDataSize);
   ```

### 绘制相关几何信息

1. 通过获取到的[AREngine\_ARSemanticDenseCubeData](../harmonyos-references/arengine-struct-arsemanticdensecubedata.md)对象来绘制立方体。

   ```
   if (semanticDenseCubeData != nullptr && cubeDataSize > 0) {
       mCubeRenderer.Draw(projectionMat, viewMat, semanticDenseCubeData);
   }
   ```
