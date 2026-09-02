---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scancore
title: scanCore (扫码公共信息)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > scanCore (扫码公共信息)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4be37f355225525440af2dfa90baff646961afd0cebe66e21a7367fb63c7a16a
---

## 模块概述

scanCore模块是Scan Kit的公共数据类型模块，提供扫码场景中使用的码类型枚举、错误码、默认界面扫码结果来源等公共数据类型定义。该模块不直接提供扫码能力，而是作为scanBarcode（默认界面扫码）、customScan（自定义界面扫码）、detectBarcode（图像识码）、generateBarcode（码图生成）功能模块的基础数据类型支撑。同时提供了isDefaultScanSupported和isCustomScanSupported两个能力查询接口，用于在调用扫码功能前检查当前设备是否支持相应能力。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { scanCore } from '@kit.ScanKit';
```

## ScanType

枚举，码类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FORMAT\_UNKNOWN | 0 | 未知类型，用于事先不知道要扫哪种类型码的场景，此参数不可用作码图生成。 |
| AZTEC\_CODE | 1 | 码类型：Aztec。 |
| CODABAR\_CODE | 2 | 码类型：Codabar。 |
| CODE39\_CODE | 3 | 码类型：Code 39。 |
| CODE93\_CODE | 4 | 码类型：Code 93。 |
| CODE128\_CODE | 5 | 码类型：Code 128。 |
| DATAMATRIX\_CODE | 6 | 码类型：Data Matrix。 |
| EAN8\_CODE | 7 | 码类型：EAN-8。 |
| EAN13\_CODE | 8 | 码类型：EAN-13。 |
| ITF14\_CODE | 9 | 码类型：ITF-14。 |
| PDF417\_CODE | 10 | 码类型：PDF417。 |
| QR\_CODE | 11 | 码类型：QR Code。 |
| UPC\_A\_CODE | 12 | 码类型：UPC-A。 |
| UPC\_E\_CODE | 13 | 码类型：UPC-E。 |
| MULTIFUNCTIONAL\_CODE | 14 | 码类型：MULTIFUNCTIONAL CODE，暂不支持码图生成。 |
| ONE\_D\_CODE | 100 | 条形码集合类型，包含：Codabar、Code 39、Code 93、Code 128、EAN-8、EAN-13、ITF-14、UPC-A、UPC-E，此参数不可用作码图生成。 |
| TWO\_D\_CODE | 101 | 二维码集合类型，包含：Aztec、Data Matrix、PDF417、QR Code、MULTIFUNCTIONAL CODE，此参数不可用作码图生成。 |
| ALL | 1001 | 以上所有类型，此参数不可用作码图生成。 |

## ScanErrorCode

枚举，扫码错误码类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 4.1.0(11)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | 1000500001 | 内部错误。详细介绍参见[1000500001 内部错误](errorcode-scan.md#section1000500001-内部错误)。  **元服务API：** 从API版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCAN\_SERVICE\_CANCELED | 1000500002 | 用户取消扫码。详细介绍请参见[1000500002 用户取消扫码](errorcode-scan.md#section1000500002-用户取消扫码)。  **元服务API：** 从API版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.0(12) |

## ScanSource

枚举，扫码结果来源，表示默认界面扫码结果来源是相机预览流还是相册图片。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 6.0.2(22)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| CAMERA | 0 | 默认界面扫码结果来源是相机预览流。 |
| PHOTO | 1 | 默认界面扫码结果来源是相册图片。 |

## isDefaultScanSupported

isDefaultScanSupported(): boolean

查询当前设备是否支持默认界面扫码。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 26.0.0

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回查询结果。true代表支持默认界面扫码，false代表不支持默认界面扫码。 |

**示例：**

```typescript
import { scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSupported: boolean = scanCore.isDefaultScanSupported();
if (isSupported) {
  hilog.info(0x0001, '[Scan Sample]', 'Default scan is supported on this device.');
  // 当前设备支持默认界面扫码，可以调用接口拉起扫码页面或进行下一步处理
  // ...
} else {
  // 当前设备不支持默认界面扫码
  hilog.info(0x0001, '[Scan Sample]', 'Default scan is not supported on this device.');
}
```

## isCustomScanSupported

isCustomScanSupported(): boolean

查询当前设备是否支持自定义界面扫码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 26.0.0

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回查询结果。true代表支持自定义界面扫码，false代表不支持自定义界面扫码。 |

**示例：**

```typescript
import { scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSupported: boolean = scanCore.isCustomScanSupported();
if (isSupported) {
  hilog.info(0x0001, '[Scan Sample]', 'Custom scan is supported on this device.');
  // 当前设备支持自定义界面扫码，可以拉起扫码页面或进行下一步处理
  // ...
} else {
  // 当前设备不支持自定义界面扫码
  hilog.info(0x0001, '[Scan Sample]', 'Custom scan is not supported on this device.');
}
```
