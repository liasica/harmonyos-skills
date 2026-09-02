---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenshot
title: "@ohos.screenshot (屏幕截图)"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 屏幕管理 > @ohos.screenshot (屏幕截图)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4b16dfbfd0052384c586da4d51c363be2a1ba0560d3efeebedc701e59a44a795
---

本模块提供屏幕截图的能力，支持区域截图和全屏截图两种模式，帮助开发者实现屏幕内容的获取功能。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { screenshot } from '@kit.ArkUI';
```

## Rect

表示截取图像的区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 表示截取图像区域的左边界，单位为px，该参数应为非负整数。 |
| top | number | 否 | 否 | 表示截取图像区域的上边界，单位为px，该参数应为非负整数。 |
| width | number | 否 | 否 | 表示截取图像区域的宽度，单位为px，该参数应为正整数。 |
| height | number | 否 | 否 | 表示截取图像区域的高度，单位为px，该参数应为正整数。 |

## CaptureOption14+

设置截取图像的信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| displayId | number | 否 | 是 | 表示截取图像的显示设备[Display](js-apis-display.md#display)的ID号，默认为0，该参数应为大于或等于0的整数，非整数会报参数错误，错误码为[401](errorcode-universal.md#section401-参数检查失败)。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| blackWindowIds21+ | Array<number> | 否 | 是 | 表示截取图像时不显示的窗口ID列表，默认为空。窗口ID应为大于0的整数，目前仅[闪控球窗口](js-apis-floatingball.md)生效，窗口ID为非闪控球窗口、非整数、小于等于0、或者不存在的窗口ID时报参数错误，错误码为[401](errorcode-universal.md#section401-参数检查失败)。推荐使用[getFloatingBallWindowInfo()](js-apis-floatingball.md#getfloatingballwindowinfo)方法获取闪控球窗口ID属性。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |

## PickInfo

截取图像的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pickRect | [Rect](js-apis-screenshot.md#rect) | 否 | 否 | 表示截取图像的区域。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 表示截取的图像PixelMap对象。 |

## screenshot.pick

pick(): Promise<PickInfo>

获取屏幕截图，当前仅支持获取displayId为0的屏幕截图（如果需要对扩展屏截图，可以通过[capture](js-apis-screenshot.md#screenshotcapture14)接口实现），使用Promise异步回调。

返回的PickInfo中的PixelMap对象需要手动释放，使用完毕后必须调用[release()](arkts-apis-image-pixelmap.md#release7)方法释放内存，否则可能导致内存泄漏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**接口对比：** [pick](js-apis-screenshot.md#screenshotpick)接口支持区域截屏，仅支持主屏幕（displayId为0），无需权限；[capture](js-apis-screenshot.md#screenshotcapture14)接口支持全屏截屏，支持主屏幕和扩展屏（通过displayId参数指定），需要权限。

**选取建议：** 需要区域截屏时使用[pick](js-apis-screenshot.md#screenshotpick)接口；需要全屏截屏或扩展屏截屏时使用[capture](js-apis-screenshot.md#screenshotcapture14)接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PickInfo](js-apis-screenshot.md#pickinfo)> | Promise对象。返回一个PickInfo对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[屏幕错误码](errorcode-display.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 调用pick接口获取屏幕截图
  let promise = screenshot.pick();
  promise.then((pickInfo: screenshot.PickInfo) => {
    console.info(`pick Pixel bytes number: ${pickInfo.pixelMap.getPixelBytesNumber()}`);
    console.info(`pick Rect: ${pickInfo.pickRect}`);
    pickInfo.pixelMap.release(); // PixelMap使用完后及时释放内存
  }).catch((err: BusinessError) => {
    console.error(`Failed to pick. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to pick. Code: ${exception.code}, message: ${exception.message}`);
}
```

## screenshot.capture14+

capture(options?: CaptureOption): Promise<image.PixelMap>

获取屏幕全屏截图，使用Promise异步回调。

此接口可以通过设置不同的displayId截取不同屏幕的截图，且只能截取全屏；[pick](js-apis-screenshot.md#screenshotpick)接口可实现区域截屏。

返回的PixelMap对象需要手动释放，使用完毕后必须调用[release()](arkts-apis-image-pixelmap.md#release7)方法释放内存，否则可能导致内存泄漏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**设备行为差异：** 在API version 21之前，该接口在PC/2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。从API version 21开始，该接口在Phone设备、PC/2in1设备、Tablet设备中可正常调用，在其他设备中返回801错误码。

**需要权限：**

* API版本22+：ohos.permission.CUSTOM\_SCREEN\_CAPTURE 或 ohos.permission.CUSTOM\_SCREEN\_RECORDING
* API版本14-21：ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CaptureOption](js-apis-screenshot.md#captureoption14) | 否 | 截取图像的相关信息。此参数不填时，默认截取displayId为0的屏幕截图。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[image.PixelMap](arkts-apis-image-pixelmap.md)> | Promise对象。返回一个PixelMap对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[屏幕错误码](errorcode-display.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| 801 | Capability not supported. |
| 1400003 | This display manager service works abnormally. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

// 配置截图参数，指定截取displayId为0的屏幕
let captureOption: screenshot.CaptureOption = {
  displayId: 0
};
try {
  // 调用capture接口获取全屏截图
  let promise = screenshot.capture(captureOption);
  promise.then((pixelMap: image.PixelMap) => {
    console.info(`Succeeded in saving screenshot. Pixel bytes number: ${pixelMap.getPixelBytesNumber()}`);
    pixelMap.release(); // PixelMap使用完后及时释放内存
  }).catch((err: BusinessError) => {
    console.error(`Failed to save screenshot. Code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to save screenshot. Code: ${exception.code}, message: ${exception.message}`);
}
```
