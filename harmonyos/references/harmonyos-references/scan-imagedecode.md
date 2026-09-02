---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-imagedecode
title: detectBarcode (图像识码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > detectBarcode (图像识码)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75b61ef55324340560b90161c720fe5615b9c4547073eb1bc2eb834ba69ccb05
---

## 模块概述

detectBarcode模块提供图像识码能力，支持通过本地图片路径或字节数组两种方式输入图像，对图像中的条形码、二维码、MULTIFUNCTIONAL CODE进行识别。适用于需要从相册图片或其他图像数据（例如相机预览流）中提取码图信息的场景。

为便于开发者快速上手，建议参考官方提供的[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { detectBarcode } from '@kit.ScanKit';
```

## InputImage

待识别的图片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 图片路径，例如file://media/Photo/x/xxx.jpg。 |

**示例：**

可通过[PhotoViewPicker](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)获取图片路径。

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoSelectOptions.maxSelectNumber = 1;
photoSelectOptions.isPhotoTakingSupported = false;
photoSelectOptions.isEditSupported = false;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoSelectOptions).then((data: photoAccessHelper.PhotoSelectResult) => {
  if (!data || (data.photoUris && data.photoUris.length === 0)) {
    hilog.error(0x0001, 'picker', 'Failed to get PhotoSelectResult by promise');
    return;
  }
  hilog.info(0x0001, 'picker', `Succeeded in getting PhotoSelectResult by promise.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
});
```

## decode

decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>

通过配置参数调用图片识码返回识码结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动图片识码参数。  **默认值：** 参考ScanOptions的默认值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | Promise对象，返回识码结果对象数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义识码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
// 通过PhotoViewPicker拉起图库并选择图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((data) => {
  // 定义识码参数inputImage，其中uri为PhotoViewPicker选择的图片路径
  let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, options).then((data: Array<scanBarcode.ScanResult>) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise with options, result length: ${data.length}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
  }
}).catch((err: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}.`);
});
```

## decode

decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

通过配置参数调用图片识码返回识码结果。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 启动图片识码参数。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义识码参数options
let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
// 通过PhotoViewPicker拉起图库并选择图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((data) => {
  // 定义识码参数inputImage，其中uri为PhotoViewPicker选择的图片路径
  let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, options, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err && err.code) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback with options, result length: ${data.length}`);
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
  }
}).catch((err: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
});
```

## decode

decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

图片识码返回识码结果。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```typescript
import { scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 通过PhotoViewPicker拉起图库并选择图片
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((data) => {
  // 定义识码参数inputImage，其中uri为PhotoViewPicker选择的图片路径
  let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
  try {
    // 调用图片识码接口
    detectBarcode.decode(inputImage, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
      if (err && err.code) {
        hilog.error(0x0001, '[Scan Sample]',
          `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by callback, result length: ${data.length}`);
    });
  } catch (err) {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
  }
}).catch((err: BusinessError) => {
  hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
});
```

## ByteImage

待识别的图像数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| byteBuffer | ArrayBuffer | 否 | 否 | 图像数据。存放图像的字节数组。 |
| width | number | 否 | 否 | 图像宽度，单位：px。 |
| height | number | 否 | 否 | 图像高度，单位：px。 |
| format | [ImageFormat](scan-imagedecode.md#imageformat) | 否 | 否 | 图像数据（byteBuffer）的类型。目前仅支持NV21像素格式。 |

**示例：**

示例中的buffer可通过相机预览流数据获取，参见[双路预览](../harmonyos-guides/camera-dual-channel-preview.md)。

```typescript
import { detectBarcode } from '@kit.ScanKit';

// 图像的buffer, height, width数据，可通过相机预览流数据获取，比如获取宽高是1920*1080时
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: buffer,
  width: 1920,
  height: 1080,
  format: detectBarcode.ImageFormat.NV21
};
```

## ImageFormat

枚举，图像数据类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NV21 | 0 | 图像的像素格式为NV21。 |

## DetectResult

识别结果。decodeImage接口的返回值，包含码的识别结果以及相机变焦建议。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanResults | Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)> | 否 | 否 | 扫码结果。 |
| zoomValue | number | 否 | 否 | 期望图像放大倍数，在值大于1时，可通过[setZoomRatio](arkts-apis-camera-zoom.md#setzoomratio11)控制相机进行变焦放大图像。  **说明：**  1. 使用Camera Kit [getZoomRatio](arkts-apis-camera-zoom.md#getzoomratio11)接口获取相机当前变焦比zoomRatio。  2. 使用Camera Kit [setZoomRatio](arkts-apis-camera-zoom.md#setzoomratio11)接口设置targetRatio，目标值为zoomRatio \* zoomValue。 |

## decodeImage

decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise<DetectResult>

通过配置参数调用图像数据识码能力返回识码结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ByteImage](scan-imagedecode.md#byteimage) | 是 | 待识别的图像数据。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动图像数据识码参数。  **默认值：** 参考ScanOptions的默认值。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[DetectResult](scan-imagedecode.md#detectresult)> | Promise对象，返回图像数据识码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-scan.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

示例中的buffer可通过相机预览流数据获取，参见[双路预览](../harmonyos-guides/camera-dual-channel-preview.md)。

```typescript
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 图像的buffer, height, width数据，可通过相机预览流数据获取，比如获取宽高是1920*1080时
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: buffer,
  width: 1920,
  height: 1080,
  format: detectBarcode.ImageFormat.NV21
};
let options: scanBarcode.ScanOptions = {
  scanTypes: [scanCore.ScanType.ALL],
  enableMultiMode: true,
  enableAlbum: false
};
try {
  detectBarcode.decodeImage(byteImg, options).then((data: detectBarcode.DetectResult) => {
    hilog.info(0x0001, '[Scan Sample]',
      `Succeeded in getting DetectResult by promise with options, result length: ${data.scanResults.length}, zoomValue: ${data.zoomValue}`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0001, '[Scan Sample]',
      `Failed to get DetectResult by promise with options. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0001, '[Scan Sample]', `Failed to decode Image. Code: ${err.code}, message: ${err.message}`);
}
```
