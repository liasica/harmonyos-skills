---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scanbarcode-api
title: scanBarcode (默认界面扫码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > scanBarcode (默认界面扫码)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8467400f11d3f5ccedae084ab0cf7e4996744845c89d25749b608c040a1b6f1
---

## 模块概述

scanBarcode模块提供系统级体验一致的扫码界面，包含相机预览流，相册扫码入口，暗光环境闪光灯开启提示。Scan Kit默认界面扫码对系统相机权限进行了预授权且调用期间处于安全访问状态，无需开发者再次申请相机权限。

为便于开发者快速上手，建议参考官方提供的[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { scanBarcode } from '@kit.ScanKit';
```

## ScanResult

扫码结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scanType | scanCore.[ScanType](scan-scancore.md#scantype) | 否 | 否 | 码类型。  **元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| originalValue | string | 否 | 否 | 码识别内容结果。  **元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| scanCodeRect | [ScanCodeRect](scan-scanbarcode-api.md#scancoderect) | 否 | 是 | 码识别位置信息。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 4.1.0(11) |
| cornerPoints | Array<[Point](scan-scanbarcode-api.md#point)> | 否 | 是 | 码识别角点位置信息，返回QR Code四个角点。此参数仅图像识码接口[decodeImage](scan-imagedecode.md#decodeimage)返回。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。  **起始版本：** 5.0.0(12) |
| isGS1 | boolean | 否 | 是 | 码图是否携带GS1（Global Standards 1）数据。  true表示码图携带GS1数据；false表示码图不携带GS1数据。默认值是false。  **元服务API：** 从API版本6.0.2(22)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.2(22) |
| source | scanCore.[ScanSource](scan-scancore.md#scansource) | 否 | 是 | 扫码结果来源。此参数仅默认界面扫码接口返回。用于区分扫码结果来源于相机预览流还是相册图片，以便进行不同的业务处理。  **元服务API：** 从API版本6.0.2(22)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.2(22) |

## ScanCodeRect

码的位置信息。使用默认界面扫码（startScan和startScanForResult）不返回码位置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 码外接矩形左上角的x坐标。单位：px。 |
| top | number | 否 | 否 | 码外接矩形左上角的y坐标。单位：px。 |
| right | number | 否 | 否 | 码外接矩形右下角的x坐标。单位：px。 |
| bottom | number | 否 | 否 | 码外接矩形右下角的y坐标。单位：px。 |

**说明** 

自定义界面扫码返回的坐标单位与传入参数[ViewControl](scan-customscan-api.md#viewcontrol)中width、height单位一致。

## Point

点坐标，该坐标系左上角为{0，0}，此坐标系是以设备充电口在右侧时的横向设备方向为基准的。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | X轴坐标，单位：px。 |
| y | number | 否 | 否 | Y轴坐标，单位：px。 |

## ScanOptions

扫码配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.0.0(10)

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scanTypes | Array<scanCore.[ScanType](scan-scancore.md#scantype)> | 否 | 是 | 设置扫码类型。  **默认值：** ALL（全部码类型）。  从API版本6.1.0(23)开始，默认界面扫码的标题支持根据此参数进行动态显示。  在API版本6.1.0(23)之前，标题统一显示为“扫描二维码/条形码”。  在API版本6.1.0(23)及之后：  - scanTypes为ALL、FORMAT\_UNKNOWN，或同时包含条形码和二维码类型，标题显示为“扫描二维码/条形码”。  - scanTypes未设置，标题显示为“扫描二维码/条形码”。  - scanTypes仅包含条形码类型，标题显示为“扫描条形码”。  - scanTypes仅包含二维码类型，标题显示为“扫描二维码”。 |
| enableMultiMode | boolean | 否 | 是 | 是否开启多码识别。  **默认值：** false。  - true：多码识别。  - false：单码识别。 |
| enableAlbum | boolean | 否 | 是 | 是否开启相册。  **默认值：** true。  - true：开启相册扫码。  - false：关闭相册扫码。  此参数只控制默认界面扫码能力中的相册识码且相册识码只支持单码识别。 |

**示例：**

```typescript
import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext: UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((data: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, scanType: ${data.scanType}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## startScanForResult

startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 扫码配置参数。  **默认值：** 参考ScanOptions的默认值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScanResult](scan-scanbarcode-api.md#scanresult)> | Promise对象，返回扫码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning.  适用版本：5.0.0(12)+ |

**示例：**

```typescript
import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext: UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((data: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, scanType: ${data.scanType}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## startScanForResult

startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning.  适用版本：5.0.0(12)+ |

**示例：**

```typescript
import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 启动扫码，拉起扫码界面
function loadPage(uiContext: UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(),
      (err: BusinessError, data: scanBarcode.ScanResult) => {
        if (err) {
          hilog.error(0x0001, '[Scan Sample]',
            `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        hilog.info(0x0001, '[Scan Sample]',
          `Succeeded in getting ScanResult by callback, scanType: ${data.scanType}`);
      });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## startScanForResult

startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 扫码配置参数。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning.  适用版本：5.0.0(12)+ |

**示例：**

```typescript
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义扫码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

// 启动扫码，拉起扫码界面
function loadPage(uiContext: UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options,
      (err: BusinessError, data: scanBarcode.ScanResult) => {
        if (err) {
          hilog.error(0x0001, '[Scan Sample]',
            `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        hilog.info(0x0001, '[Scan Sample]',
          `Succeeded in getting ScanResult by callback with options, scanType: ${data.scanType}`);
      });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
  }
}
```

## startScan(deprecated)

startScan(options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，返回扫码结果。使用Promise异步回调。

**废弃说明：** 从API版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#startscanforresult)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动扫码配置参数。  **默认值：** 参考ScanOptions的默认值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScanResult](scan-scanbarcode-api.md#scanresult)> | Promise对象，返回扫码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```typescript
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造启动扫码的入参options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options).then((data: scanBarcode.ScanResult) => {
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by promise with options, scanType: ${data.scanType}`);
  }).catch((err: BusinessError) => {
    // 当扫码过程中出现错误，打印并返回报错
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
}
```

## startScan(deprecated)

startScan(callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，返回扫码结果。使用callback异步回调。

**废弃说明：** 从API版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#startscanforresult-1)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```typescript
import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  scanBarcode.startScan((err: BusinessError, data: scanBarcode.ScanResult) => {
    // error回调监听，当扫码过程中出现错误，打印并返回报错
    if (err) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by callback, scanType: ${data.scanType}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
}
```

## startScan(deprecated)

startScan(options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，返回扫码结果。使用callback异步回调。

**废弃说明：** 从API版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#startscanforresult-2)替代。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 在API版本6.0.2(22)及之前，该接口在Phone、Tablet中可正常调用。在API版本6.1.0(23)及之后，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 扫码配置参数。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数，当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```typescript
import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 构造启动扫码的入参options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options, (err: BusinessError, data: scanBarcode.ScanResult) => {
    // error回调监听，当扫码过程中出现错误，打印并返回报错
    if (err) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting ScanResult by callback with options, scanType: ${data.scanType}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
}
```
