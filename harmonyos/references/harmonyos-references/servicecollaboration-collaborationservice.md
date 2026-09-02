---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationservice
title: CollaborationService (跨设备互通组件)
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS组件 > CollaborationService (跨设备互通组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:283663b691b245b31426fdaa6d799360976119b68921aa056d90a129226b2e27
---

该模块提供了组件[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)和[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)，两者需要配合使用，完成分布式跨端能力，如在PC/2in1端跨端调用Phone端拍照。

通过[createCollaborationServiceMenuItems](servicecollaboration-collaborationservice.md#createcollaborationservicemenuitems)组件，可以获取组网内具有对应能力的设备列表。用户选择对应的设备后，拉起应用。调用[CollaborationServiceStateDialog](servicecollaboration-collaborationservice.md#collaborationservicestatedialog)，应用将弹出提示框，提示对端应用状态。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { CollaborationServiceStateDialog, createCollaborationServiceMenuItems, CollaborationServiceFilter} from '@kit.ServiceCollaborationKit';
```

## createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter?: Array<CollaborationServiceFilter>): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 否 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL]);
  }
}
```

## createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveNumber: number): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表，此接口支持自定义对端图库能力图片选择的数量。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**设备行为差异：** 该接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 是 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |
| canReceiveNumber | number | 是 | 传入照片最大张数，数量1到50，小于等于0时不会拉起被调用设备的能力，大于50默认为50。 |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30);
  }
}
```

## createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveMaxCount: number, deviceTypeFilter: Array<CollaborationDeviceFilterType> ): void

设备列表选择器，需要在[Menu](ts-basic-components-menu.md)组件内调用。用于显示组网内具有对应能力的设备列表，此接口支持自定义对端图库能力图片选择的数量和支持自定义选择对端的设备类型Phone、Tablet和PC/2in1设备。

具体调用策略：PC/2in1设备可以调用Tablet和Phone，Tablet可以调用Phone，并且在6.1.0(23)及以上版本支持Phone、Tablet或PC/2in1设备调用支持拍照、扫描、选择图库能力的Phone，支持拍照、扫描、选择图库能力的Tablet，以及支持选择图库能力的PC/2in1设备。

该方法为自定义构建函数，开发者在使用前需要先了解[@Builder](../harmonyos-guides/arkts-builder.md)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Builder

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| businessFilter | Array<[CollaborationServiceFilter](servicecollaboration-collaborationservice.md#collaborationservicefilter)> | 是 | 传入能力类型。默认值为ALL，匹配跨端拍照、文档扫描和图库选择器。  对于API 6.0.0(20)及之后版本，支持匹配跨端拍照、文档扫描、图库选择器、视频选择器、图片和视频选择器；对于API 6.0.0(20)之前版本，仅支持匹配跨端拍照、文档扫描、图库选择器。 |
| canReceiveMaxCount | number | 是 | 传入照片最大张数，数量1到50，小于等于0时不会拉起被调用设备的能力，大于50默认为50。 |
| deviceTypeFilter | Array<[CollaborationDeviceFilterType](servicecollaboration-collaborationservice.md#collaborationdevicefiltertype)> | 是 | 传入调用的设备类型，传入为空或传入非法值时不会调用设备。 |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30, [CollaborationDeviceFilterType.PHONE, CollaborationDeviceFilterType.TABLET]);
  }
}
```

## CollaborationServiceFilter

能力类型枚举值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | 0 | 匹配跨端拍照、文档扫描和图库选择器。 |
| TAKE\_PHOTO | 1 | 匹配跨端拍照。 |
| SCAN\_DOCUMENT | 2 | 匹配文档扫描。 |
| IMAGE\_PICKER | 3 | 匹配图库选择器。 |
| VIDEO\_PICKER | 5 | 匹配视频选择器。  **起始版本：** 6.0.0(20) |
| IMAGE\_VIDEO\_PICKER | 6 | 匹配图片和视频选择器。  **起始版本：** 6.0.0(20) |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30);
  }
}
```

## CollaborationDeviceFilterType

设备类型枚举值。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHONE | 1 | Phone。 |
| TABLET | 2 | Tablet。 |
| PC\_2IN1 | 3 | PC/2in1。 |

**示例：**

```typescript
@Builder
myTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30, [CollaborationDeviceFilterType.PHONE, CollaborationDeviceFilterType.TABLET]);
  }
}
```

## CollaborationServiceStateDialog

弹窗组件，用于提示对端应用状态。

您需要实现[onState](servicecollaboration-collaborationservice.md#onstate)方法，并且在页面中定义这个组件，在业务开始后，此方法将被协同框架调用。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**装饰器类型：** @Component

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

### onState

onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer) => void

接收数据的回调函数，其中传入的stateCode是完成状态，bufferType是回传的数据类型，buffer是回传的数据内容，开发者可通过状态和数据结合自身的业务逻辑实现onState方法。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateCode | number | 是 | 标识业务完成状态，含义详见下面状态码。 |
| bufferType | string | 是 | 标识回传数据类型。  "general.image"：图片类型。  "general.fileName"：文件名称。  "general.video"：视频，从6.1.0(23)开始支持此类型。 |
| buffer | ArrayBuffer | 是 | 当bufferType为"general.image"，成功则返回对应数据，失败则返回空。  当bufferType为"general.video"，成功则返回对应存在应用沙箱视频uri路径，失败则返回空。 |

**状态码：**

以下部分错误状态的详细介绍请参见[错误码](errorcode-servicecollaboration.md)。

| 状态码ID | 错误信息 |
| --- | --- |
| 0 | Success. |
| 1001202001 | The peer end cancels the operation. |
| 1001202002 | An error occurred within the collaborative framework. |
| 1001202003 | The local end cancels the operation. |
| 1001202004 | The device interconnectivity has been established. |
| 1001202005 | All images have been successfully sent back. |
| 1001202006 | Multiple images are being sent back. |
| 1001202007 | The number of input custom images is less than or equal to 0. |
| 1001202015 | All videos have been successfully sent back. |
| 1001202016 | Multiple videos are being sent back. |
| 1001202017 | Out of memory, video send back failed. |

### build

build(): void

struct的默认构造函数，开发者无法直接调用此方法。

**模型约束：** 此模块的接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**示例1：**

6.0.0(20)之前的版本，参考以下示例，可以完成一次调用对端应用的获取图片操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](../harmonyos-guides/servicecollaboration-service-overview.md)。

```typescript
import {
  createCollaborationServiceMenuItems,
  CollaborationServiceStateDialog,
  CollaborationServiceFilter
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
      createCollaborationServiceMenuItems([CollaborationServiceFilter.ALL], 30);
    }
  }

  build() {
    Column({ space: 20 }) {
      CollaborationServiceStateDialog({
        onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode,
          bufferType, buffer)
      })
      Button('使用远端设备进行拍照')
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

  doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
    if (stateCode != 0) {
      return;
    }
    if (bufferType == 'general.image') {
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
}
```

**示例2：**

6.0.0(20)及之后的版本，参考以下示例，可以完成一次调用对端应用的获取图片和视频操作。

跨设备互通详细介绍可参考[跨设备互通特性简介](../harmonyos-guides/servicecollaboration-service-overview.md)。

```typescript
import {
  createCollaborationServiceMenuItems, CollaborationServiceStateDialog
} from '@kit.ServiceCollaborationKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

class VideoItem {
  id: string;
  src: string;

  constructor(id: string, src: string) {
    this.id = id;
    this.src = src;
  }
}

@Entry
@Component
struct Index {
  @State picture: PixelMap | undefined = undefined;
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };
  @State videoSrc: string = '';
  @State videoItems: VideoItem[] = [];
  refreshId: number = 0;

  @Builder
  myToolBarMenu() {
    Menu() {
      // create collaboration camera menuItems to show camera devices.
      createCollaborationServiceMenuItems([0, 5], 50);
    }
  }

  aboutToAppear(): void {
    hilog.info(0, 'MEMOMOCK', 'aboutToAppear ');
  }

  aboutToDisappear(): void {
    hilog.info(0, 'MEMOMOCK', 'aboutToDisappear ');
  }

  build() {
    Column({ space: 20 }) {
      CollaborationServiceStateDialog({
        onState: (stateCode: number, dataType?: string, buffer?: ArrayBuffer): void =>
        this.doInsertPicture(stateCode, dataType, buffer)
      })
      Button('使用远端设备进行拍照')
        .type(ButtonType.Normal)
        .borderRadius(10)
        .bindMenu(this.myToolBarMenu)
      RichEditor(this.options)
        .onReady(() => {
          hilog.info(0x0000, 'MEMOMOCK', 'RichEditor');
        }
        )
      Column() {
        List() {
          ForEach(this.videoItems, (item: VideoItem) => {
            ListItem() {
              Video({
                src: item.src,
                controller: new VideoController()
              })
                .objectFit(ImageFit.Auto)
                .width('20%')
                .height('20%')
                .margin({ top: 10, right: 10 })
                .onError((err) => {
                  hilog.error(0, 'MEMOMOCK', `code is ${err.code}, message is ${err.message}`);
                })
            }
          }, (item: VideoItem) => {
            hilog.info(0, 'MEMOMOCK', 'item id ' + item.id);
            hilog.info(0, 'MEMOMOCK', 'item src' + item.src);
            return item.id;
          });
        }
      }.padding({ bottom: '120vp' })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center);
  }

  doInsertPicture(stateCode: number, dataType?: string, buffer?: ArrayBuffer): void {
    hilog.info(0, 'MEMOMOCK', 'doInsertPicture is ' + stateCode)
    if (dataType == 'general.video') {
      let decoder = util.TextDecoder.create('utf-8');
      let uriStr = decoder.decodeToString(new Uint8Array(buffer));
      hilog.info(0, 'MEMOMOCK', 'Received URI: ' + uriStr);
      const newId = String(++this.refreshId);
      this.videoItems.push(new VideoItem(newId, uriStr));
    } else if (dataType == 'general.image') {
      let imageSource = image.createImageSource(buffer);
      imageSource && imageSource.createPixelMap().then((pixelMap) => {
        this.picture = pixelMap;
        if (this.controller) {
          this.controller.addImageSpan(pixelMap,
            {
              imageStyle:
              {
                size: ['200px', '200px']
              }
            });
        }
      }).catch((error: Error) => {
        hilog.error(0, 'MEMOMOCK', 'Create pixel map failed: ' + error);
      }).finally(() => {
        imageSource.release();
      });
    }
  }
}
```
