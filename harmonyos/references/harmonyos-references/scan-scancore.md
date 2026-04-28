---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scancore
title: scanCore (扫码公共信息)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > scanCore (扫码公共信息)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a365a6b5fcca37e7220130040c1d6f49f93e550ac02aedf5009afa16793a8ce
---

本模块提供扫码公共信息。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { scanCore } from '@kit.ScanKit';
```

## ScanType

PhonePC/2in1TabletTVWearable

枚举，码类型。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 4.0.0(10)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FORMAT\_UNKNOWN | 0 | 未知类型，用于事先不知道要扫哪种类型码的场景，此参数不可用作码图生成 |
| AZTEC\_CODE | 1 | AZTEC |
| CODABAR\_CODE | 2 | CODABAR |
| CODE39\_CODE | 3 | CODE 39 |
| CODE93\_CODE | 4 | CODE 93 |
| CODE128\_CODE | 5 | CODE 128 |
| DATAMATRIX\_CODE | 6 | DATA MATRIX |
| EAN8\_CODE | 7 | EAN-8 |
| EAN13\_CODE | 8 | EAN-13 |
| ITF14\_CODE | 9 | ITF-14 |
| PDF417\_CODE | 10 | PDF417 |
| QR\_CODE | 11 | QR CODE |
| UPC\_A\_CODE | 12 | UPC-A |
| UPC\_E\_CODE | 13 | UPC-E |
| MULTIFUNCTIONAL\_CODE | 14 | MULTIFUNCTIONAL CODE，暂不支持码图生成 |
| ONE\_D\_CODE | 100 | 条形码，包含：CODABAR、CODE 39、CODE 93、CODE 128、EAN-8、EAN-13、ITF-14、UPC-A、UPC-E，此参数不可用作码图生成 |
| TWO\_D\_CODE | 101 | 二维码，包含：AZTEC、DATA MATRIX、PDF417、QR CODE、MULTIFUNCTIONAL CODE，此参数不可用作码图生成 |
| ALL | 1001 | 以上所有类型，此参数不可用作码图生成 |

## ScanErrorCode

PhonePC/2in1TabletTVWearable

枚举，扫码错误码类型。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 4.1.0(11)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| INTERNAL\_ERROR | 1000500001 | Internal error.  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| SCAN\_SERVICE\_CANCELED | 1000500002 | The user canceled the barcode scanning.  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。  **起始版本：** 5.0.0(12) |

## ScanSource

PhonePC/2in1TabletTVWearable

枚举，扫码结果来源。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.Core

**起始版本：** 6.0.2(22)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| CAMERA | 0 | 表示相机流扫码。 |
| PHOTO | 1 | 表示照片扫码。 |
