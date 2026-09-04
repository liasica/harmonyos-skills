---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api
title: customScan (自定义界面扫码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > customScan (自定义界面扫码)
category: harmonyos-references
scraped_at: 2026-09-05T06:20:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4aa81a5d38ff48b44b87766edd673317b2222af80c201fb8a5e70dad5d83130d
---

## 模块概述

customScan模块提供自定义界面扫码能力，允许开发者根据自身需求自定义扫码界面，通过[XComponent](ts-basic-components-xcomponent.md)组件渲染相机预览流，并获取扫码结果。

### 基础扫码流程

使用customScan模块进行扫码，需要按以下顺序调用API：

1. **初始化**：调用[init](scan-customscan-api.md#init)配置扫码参数。
2. **启动扫码**：调用[start](scan-customscan-api.md#start-1)启动相机流并开始扫码。
3. **处理结果**：在回调中获取[ScanResult](scan-scanbarcode-api.md#scanresult)并进行业务处理。
4. **暂停**：调用[stop](scan-customscan-api.md#stop)暂停相机流。
5. **释放**：调用[release](scan-customscan-api.md#release)释放资源。

流程伪代码如下：

```typescript
// 1. 初始化扫码参数
let options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: true
};
customScan.init(options);

// 2. 创建XComponent并获取XComponent的surface的ID，构建ViewControl，启动扫码
let surfaceId: string = xComponentController.getXComponentSurfaceId();
// 相机控制参数，包含width、height、surfaceId三个属性，用于配置自定义界面扫码的相机预览流尺寸和渲染的目标surface
let viewControl: customScan.ViewControl = {
  width: 360,
  height: 640,
  surfaceId: surfaceId
};

customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
  // 3. 从data中获取扫码结果，并进行业务处理
  // ...
});

// 4. 扫码完成后暂停相机流
await customScan.stop();

// 5. 退出扫码时释放资源
await customScan.release();
```

### 生命周期和状态机

customScan模块的扫码全流程包含：初始化（init）、启动相机流扫码（start）、暂停相机流（stop）、释放资源（release），状态图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/VTyakDVHTTmJqvPVC5WhXg/zh-cn_image_0000002742126271.png)

**状态说明**

| 状态 | 可用API | 说明 |
| --- | --- | --- |
| Initialized | start | 扫码已初始化，可启动相机流进行扫码。 |
| Running | getFlashLightStatus、openFlashLight、closeFlashLight、setZoom、getZoom、setFocusPoint、resetFocus、setAutoZoomEnabled、rescan、on('lightingFlash')、off('lightingFlash')、stop | 扫码进行中，可进行闪光灯控制、变焦调节、对焦设置、重新触发扫码、暂停扫码。 |
| Paused | off('lightingFlash')、release、start | 扫码已暂停，可释放资源或重新启动扫码。 |

为便于开发者快速上手，建议参考官方提供的[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { customScan } from '@kit.ScanKit';
```

## ViewControl

相机控制参数，用于配置自定义界面扫码的相机预览流尺寸和渲染的目标surface。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | [XComponent](ts-basic-components-xcomponent.md)组件的宽度，默认使用单位为vp，支持px、lpx和vp。建议在不同屏幕密度下统一使用vp单位以保证兼容性。 |
| height | number | 否 | 否 | XComponent组件的高度，默认使用单位为vp，支持px、lpx和vp。建议在不同屏幕密度下统一使用vp单位以保证兼容性。 |
| surfaceId | string | 否 | 否 | XComponent持有surface的ID。 用于指定相机预览流渲染的目标surface。 |

**说明** 

1. ViewControl的width和height需和XComponent的保持一致，start接口根据设置宽高值会匹配最接近的相机分辨率，如果宽高比例与相机的分辨率比例相差过大会影响预览流体验。XComponent组件为预览流提供的surface，而XComponent的能力由UI提供，相关介绍可参见[XComponent](ts-basic-components-xcomponent.md)。
2. 当开发设备为折叠屏时，折叠态切换时需自行调整XComponent的宽高，start接口会重新适配相机分辨率比例。

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, 'viewControl', `onLoad surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '[Scan Sample]',
                `Succeeded in getting ScanResult by promise, scanResult length: ${scanResult.length}`);
            }).catch((err: BusinessError) => {
              hilog.error(0x0001, '[Scan Sample]',
                `Failed to get ScanResult by promise. Code: ${err.code}, message: ${err.message}`);
            });
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

## ScanFrame

相机预览流（YUV）。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| byteBuffer | ArrayBuffer | 否 | 否 | 相机预览流的ArrayBuffer数组，数据格式为YUV（NV21格式，基于4:2:0采样）。 |
| width | number | 否 | 否 | 相机预览流的宽度，单位：px。 |
| height | number | 否 | 否 | 相机预览流的高度，单位：px。 |
| scanCodeRects | Array<scanBarcode.[ScanCodeRect](scan-scanbarcode-api.md#scancoderect)> | 否 | 是 | 相机预览流（byteBuffer）中检测到的码图位置信息。  **设备行为差异：** 该属性在带有Kirin NPU（Neural-network Processing Unit，神经网络处理器）的设备可正常返回，在不带有Kirin NPU的设备上返回undefined。 |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  private callback: AsyncCallback<scanBarcode.ScanResult[]> =
    (err: BusinessError, data: scanBarcode.ScanResult[]) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result length: ${data.length}`);
    };
  // 回调获取ScanFrame
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    (err: BusinessError, frameResult: customScan.ScanFrame) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanFrame by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanFrame. ByteLength: ${frameResult.byteBuffer.byteLength}, width: ${frameResult.width}, height: ${frameResult.height}.`);
    };

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

## init

init(options?: scanBarcode.ScanOptions): void

初始化自定义界面扫码。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 自定义界面扫码配置参数。  **默认值：** 参考ScanOptions的默认值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

从API版本5.0.2(14)开始，customScan模块的init接口新增错误码201。

* 在API版本5.0.2(14)之前，未申请相机权限时调用customScan模块init接口，返回错误码1000500001。
* 在API版本5.0.2(14)及之后，未申请相机权限时调用customScan模块init接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API.  适用版本：5.0.2(14)+ |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { scanBarcode, scanCore, customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 定义扫码配置参数
let options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: true
};
try {
  customScan.init(options);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to init customScan. Code: ${err.code}, message: ${err.message}`);
}
```

## start

start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>

启动扫码相机流获取扫码结果。使用Promise异步回调。

**说明** 

1. 此接口需要在init接口调用后才能使用，否则会抛出错误码1000500001。
2. 此接口为长期占用相机资源操作，扫码完成后应及时调用stop、release释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| viewControl | [ViewControl](scan-customscan-api.md#viewcontrol) | 是 | 相机控制参数，用于配置自定义界面扫码的相机预览流尺寸和渲染的目标surface。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | Promise对象，返回启动相机流扫码结果对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

从API版本5.0.2(14)开始，customScan模块的start接口新增错误码201。

* 在API版本5.0.2(14)之前，未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
* 在API版本5.0.2(14)及之后，未申请相机权限时调用customScan模块start接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API.  适用版本：5.0.2(14)+ |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '[Scan Sample]',
                `Succeeded in getting ScanResult by promise, scanResult length: ${scanResult.length}`);
            }).catch((err: BusinessError) => {
              hilog.error(0x0001, '[Scan Sample]',
                `Failed to get ScanResult by promise. Code: ${err.code}, message: ${err.message}`);
            });
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

## start

start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void

启动扫码相机流获取扫码结果、相机预览流（YUV-图像格式NV21基于4:2:0采样）。使用callback异步回调。

**说明** 

1. 此接口需要在init接口调用后才能使用，否则会抛出错误码1000500001。
2. 此接口为长期占用相机资源操作，扫码完成后应及时调用stop、release释放资源。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| viewControl | [ViewControl](scan-customscan-api.md#viewcontrol) | 是 | 相机控制参数，用于配置自定义界面扫码的相机预览流尺寸和渲染的目标surface。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当启动相机流扫码成功，err为undefined，data为获取到的Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>；否则为错误对象。 |
| frameCallback | AsyncCallback<[ScanFrame](scan-customscan-api.md#scanframe)> | 否 | 回调函数，当启动相机流成功会持续返回预览流数据，err为undefined，data为获取到的相机预览流（YUV）[ScanFrame](scan-customscan-api.md#scanframe)；否则为错误对象。  **起始版本：** 5.0.0(12) |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

从API版本5.0.2(14)开始，customScan模块的start接口新增错误码201。

* 在API版本5.0.2(14)之前，未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
* 在API版本5.0.2(14)及之后，未申请相机权限时调用customScan模块start接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API.  适用版本：5.0.2(14)+ |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // 返回自定义扫描结果的回调
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, scanResult length: ${data.length}`);
    };
  // 回调获取ScanFrame
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    (err: BusinessError, frameResult: customScan.ScanFrame) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanFrame by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanFrame. ByteLength: ${frameResult.byteBuffer.byteLength}, width: ${frameResult.width}, height: ${frameResult.height}.`);
    };

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

## getFlashLightStatus

getFlashLightStatus(): boolean

获取当前相机闪光灯状态。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回当前相机闪光灯状态。true代表开启，false代表关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // 根据当前闪光灯状态，选择开启或关闭闪光灯
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (err) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (err) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
    }
  }
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
}
```

## openFlashLight

openFlashLight(): void

开启相机闪光灯。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // 根据当前闪光灯状态，选择开启或关闭闪光灯
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (err) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (err) {
      hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
    }
  }
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
}
```

## closeFlashLight

closeFlashLight(): void

关闭相机闪光灯。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
}
// 根据当前闪光灯状态，选择开启或关闭闪光灯
if (flashLightStatus) {
  try {
    customScan.closeFlashLight();
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
  }
} else {
  try {
    customScan.openFlashLight();
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## setZoom

setZoom(zoomValue: number): void

设置变焦比。变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| zoomValue | number | 是 | 相机变焦比，精度最高为小数点后两位（例如1.45）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 设置变焦比
let zoomValue = 2.0;
try {
  customScan.setZoom(zoomValue);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setZoom. Code: ${err.code}, message: ${err.message}`);
}
```

## getZoom

getZoom(): number

获取当前的变焦比。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 返回当前的变焦比。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

try {
  // 获取变焦比
  let zoomValue = customScan.getZoom();
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting zoomValue, zoomValue is ${zoomValue}`);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to get zoomValue. Code: ${err.code}, message: ${err.message}`);
}
```

## setFocusPoint

setFocusPoint(point: scanBarcode.Point): void

设置相机焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| point | scanBarcode.[Point](scan-scanbarcode-api.md#point) | 是 | 焦点。x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 设置对焦点
  customScan.setFocusPoint({ x: 0.5, y: 0.5 });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setFocusPoint. Code: ${err.code}, message: ${err.message}`);
}
```

## resetFocus

resetFocus(): void

设置连续自动对焦模式。

**说明** 

1. 本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。
2. 可与setFocusPoint配合使用：setFocusPoint设置对焦点后，可调用resetFocus恢复连续自动对焦。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 设置连续自动对焦模式
  customScan.resetFocus();
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to resetFocus. Code: ${err.code}, message: ${err.message}`);
}
```

## on('lightingFlash')

on(type: 'lightingFlash', callback: AsyncCallback<boolean>): void

订阅环境亮度变化事件，当环境暗、亮状态变化时返回闪光灯开启或关闭提示。使用callback异步回调。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'lightingFlash'，当环境亮度发生变化时触发。可用于提示用户开启或关闭闪光灯。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前环境暗，可以提示用户开启闪光灯，false表示环境亮，可以提示用户关闭闪光灯。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (err: BusinessError, bool: boolean) => {
  if (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to light Flash by callback. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in lighting Flash by callback, bool is ${bool}`);
};

try {
  customScan.on('lightingFlash', callback);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to listen lightingFlash. Code: ${err.code}, message: ${err.message}`);
}
```

## off('lightingFlash')

off(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void

注销环境亮度变化事件。使用callback异步回调。

**说明** 

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'lightingFlash'，当环境亮度发生变化时触发，可用于提示用户开启或关闭闪光灯。 |
| callback | AsyncCallback<boolean> | 否 | 回调函数，如果指定参数则必须和customScan.on中监听的事件保持一致，否则注销所有绑定在'lightingFlash'上的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (err: BusinessError, bool: boolean) => {
  if (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to cancel Flash by callback. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0001, '[Scan Sample]', `Succeeded in cancelling Flash by callback, bool is ${bool}`);
};
// 可以不填callback，取消lightingFlash所有监听。填写callback，必须和customScan.on中监听的事件保持一致
try {
  customScan.off('lightingFlash', callback);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to listen lightingFlash. Code: ${err.code}, message: ${err.message}`);
}
```

## rescan

rescan(): void

触发一次重新扫码。调用后，会重新检测预览画面中的码图，识别成功后会触发start接口传入的callback回调返回新的扫码结果。适用于扫码结果不是预期结果或连续扫码场景。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

仅对start接口的Callback异步回调有效，Promise异步回调接口无效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640;
  // 设置预览流宽度，默认单位：vp
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // 返回自定义扫描结果的回调
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, scanResult length: ${data.length}`);
      // 重新触发扫码。如需不重启相机并重新触发一次扫码，可以在start接口的Callback异步回调中，调用rescan接口。
      try {
        customScan.rescan();
      } catch (err) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to rescan customScan. Code: ${err.code}, message: ${err.message}`);
      }
    };

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
          // 获取XComponent的surfaceId
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
          // 设置ViewControl相应字段
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback);
          } catch (err) {
            hilog.error(0x0001, '[Scan Sample]',
              `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}
```

## setAutoZoomEnabled

setAutoZoomEnabled(enabled: boolean): void

设置自动变焦能力的开启和关闭。未调用时默认开启自动变焦。

**说明** 

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启自动变焦能力。true代表开启，false代表关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 开启或关闭自动变焦能力，true为开启，false为关闭
  customScan.setAutoZoomEnabled(false);
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to setAutoZoomEnabled. Code: ${err.code}, message: ${err.message}`);
}
```

## stop

stop(): Promise<void>

暂停扫码相机流。使用Promise异步回调。

**说明** 

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop().then(() => {
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by promise');
  }).catch((err: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to stop scan by promise. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
}
```

## stop

stop(callback: AsyncCallback<void>): void

暂停扫码相机流。使用callback异步回调。

**说明** 

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停相机流成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop((err: BusinessError) => {
    if (err) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to stop scan by callback. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by callback');
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
}
```

## release

release(): Promise<void>

释放扫码相机流。使用Promise异步回调。

**说明** 

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release().then(() => {
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by promise');
  }).catch((err: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to release scan by promise. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
}
```

## release

release(callback: AsyncCallback<void>): void

释放扫码相机流。使用callback异步回调。

**说明** 

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出错误码1000500001。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放相机流成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release((err: BusinessError) => {
    if (err) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to release scan by callback. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by callback');
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]',
    `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
}
```
