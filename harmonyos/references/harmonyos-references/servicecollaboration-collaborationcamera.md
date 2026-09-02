---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationcamera
title: CollaborationCamera (跨设备互通组件)
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS组件 > CollaborationCamera (跨设备互通组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f624366030f5d4b7354ac67e14d40738591a61ab357c58a78a25a17e309edff2
---

该模块提供了组件[createCollaborationCameraMenuItems](servicecollaboration-collaborationcamera.md#createcollaborationcameramenuitemsdeprecated)和[CollaborationCameraStateDialog](servicecollaboration-collaborationcamera.md#collaborationcamerastatedialogdeprecated)，两者需要配合使用，完成分布式跨端能力，如在PC/2in1端跨端调用Phone端拍照。

通过[createCollaborationCameraMenuItems](servicecollaboration-collaborationcamera.md#createcollaborationcameramenuitemsdeprecated)组件，可以获取组网内具有对应能力的设备列表。用户选择对应的设备后，拉起应用。调用[CollaborationCameraStateDialog](servicecollaboration-collaborationcamera.md#collaborationcamerastatedialogdeprecated)，应用将弹出提示框，提示对端应用状态。

**废弃说明：** 从5.0.0(12)开始废弃，建议使用[CollaborationService](servicecollaboration-collaborationservice.md)替代。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { CollaborationCameraStateDialog, createCollaborationCameraMenuItems, CollaborationCameraBusinessFilter} from '@kit.ServiceCollaborationKit';
```

## createCollaborationCameraMenuItems(deprecated)

createCollaborationCameraMenuItems(businessFilter?: Array<CollaborationCameraBusinessFilter>): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**废弃说明：** 从5.0.0(12) 开始废弃，建议使用[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)替代。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Camera

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationCameraBusinessFilter](servicecollaboration-collaborationcamera.md#collaborationcamerabusinessfilterdeprecated)> | 否 | 传入能力类型，支持匹配跨端拍照、扫描、图库。  默认值为ALL，匹配所有业务。 |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationCameraMenuItems([CollaborationCameraBusinessFilter.ALL]);
  }
}
```

## CollaborationCameraBusinessFilter(deprecated)

能力类型枚举值。

**废弃说明：** 从5.0.0(12) 开始废弃，建议使用[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)替代。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Camera

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 匹配所有业务。 |
| TAKE\_PHOTO | 1 | 匹配跨端拍照。 |
| SCAN\_DOCUMENT | 2 | 匹配文档扫描。  **起始版本：** 4.1.0(11) |
| IMAGE\_PICKER | 3 | 匹配图库选择器。  **起始版本：** 4.1.0(11) |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationCameraMenuItems([CollaborationCameraBusinessFilter.ALL]);
  }
}
```

## CollaborationCameraStateDialog(deprecated)

弹窗组件，用于提示对端应用状态。

您需要实现[onState](servicecollaboration-collaborationcamera.md#onstatedeprecated)方法，并且在页面中定义这个组件，在业务开始后，此方法将被协同框架调用。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)。

**废弃说明：** 从5.0.0(12) 开始废弃，建议使用[CollaborationServiceStateDialog](servicecollaboration-collaborationservice.md#collaborationservicestatedialog)替代。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.Collaboration.Camera

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 4.0.0(10)

### onState(deprecated)

onState: (stateCode: number, buffer: ArrayBuffer) => void

接收数据的回调函数，其中传入的stateCode是完成状态，buffer是回传的图片数据，开发者可通过状态和图片数据结合自身的业务逻辑实现onState方法。

**废弃说明：** 从5.0.0(12) 开始废弃，建议使用[onState](servicecollaboration-collaborationservice.md#onstate)替代。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Camera

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateCode | number | 是 | 标识业务完成状态，含义详见下面错误码。 |
| buffer | ArrayBuffer | 是 | 成功则返回对应数据，失败则返回空。 |

**错误码：**

以下错误码的详细介绍请参见[错误码](errorcode-servicecollaboration.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 0 | Success. |
| 1001202001 | The peer end cancels the operation. |
| 1001202002 | An error occurred within the collaborative framework. |
| 1001202003 | The local end cancels the operation. |
| 1001202004 | The device interconnectivity has been established. |
| 1001202005 | All images have been successfully sent back. |
| 1001202006 | Multiple images are being sent back. |

### build(deprecated)

build(): void

struct的默认构造函数，开发者无法直接调用此方法。

**废弃说明：** 从5.0.0(12) 开始废弃，建议使用[build](servicecollaboration-collaborationservice.md#build)替代。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Camera

**设备行为差异：** 该接口在PC/2in1、Tablet可被组件正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 4.0.0(10)

**示例：**

参考以下示例，可以完成一次调用对端应用的操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](../harmonyos-guides/servicecollaboration-service-overview.md)。

```typescript
import {
  createCollaborationCameraMenuItems,
  CollaborationCameraStateDialog,
  CollaborationCameraBusinessFilter
} from '@kit.ServiceCollaborationKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State picture: PixelMap | undefined = undefined;

  @Builder
  myTestMenu() {
    Menu() {
      createCollaborationCameraMenuItems([CollaborationCameraBusinessFilter.ALL]);
    }
  }

  build() {
    Column({ space: 20 }) {
      CollaborationCameraStateDialog({
        onState: (stateCode: number, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, buffer)
      })
      Button('使用远端设备插入图片')
        .type(ButtonType.Normal)
        .borderRadius(10)
        .bindMenu(this.myTestMenu)

      if (this.picture) {
        Image(this.picture)
          .borderStyle(BorderStyle.Dotted)
          .borderWidth(1)
          .objectFit(ImageFit.Contain)
          .height('80%')
          .onComplete((event) => {
            if (event != undefined) {
              hilog.info(0, 'MEMOMOCK', 'onComplete ' + event.loadingStatus);
            }
          })
      }
    }
    .padding(20)
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }

  doInsertPicture(stateCode: number, buffer: ArrayBuffer): void {
    if (stateCode != 0) {
      return;
    }
    let imageSource = image.createImageSource(buffer);
    imageSource.createPixelMap().then((pixelMap) => {
      this.picture = pixelMap;
    }).catch((error: Error) => {
      hilog.error(0, 'MEMOMOCK', 'Create pixel map failed: ' + error);
    }).finally(() => {
      imageSource.release();
    });
  }
}
```
