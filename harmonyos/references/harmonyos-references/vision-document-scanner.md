---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-document-scanner
title: DocumentScanner（文档扫描控件）
breadcrumb: API参考 > AI > Vision Kit（场景化视觉服务） > ArkTS组件 > DocumentScanner（文档扫描控件）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e47f064606d80487e4cde10f6efbf878628db77eda2f705168dc06b0113d977
---

文档扫描控件提供拍摄文档并转换为高清扫描件的服务。仅需使用手机拍摄文档，即可自动裁剪和优化，并支持jpeg图片、PDF格式保存和分享；同时支持拍摄拍照或图片识别表格，生成表格文档。

**起始版本：** 5.0.0(12)

## 导入模块

PhoneTablet

```
1. import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode, EditTab, DocumentScannerResultCallback } from "@kit.VisionKit";
```

## DocumentScanner

PhoneTablet

文档扫描控件，集成此控件可以实现文档扫描。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**装饰器类型：** [@Component](../harmonyos-guides/arkts-create-custom-components.md#component)

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| scannerConfig | [DocumentScannerConfig](vision-document-scanner.md#documentscannerconfig) | 是 | - | 文档扫描能力配置。 |
| onResult | [DocumentScannerResultCallback](vision-document-scanner.md#documentscannerresultcallback) | 是 | - | 文档扫描结果回调。 |

## DocumentScannerConfig

PhoneTablet

文档扫描配置项。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxShotCount | number | 否 | 是 | 文档扫描最大支持张数。默认值1，最大值50。  取值范围：[1,50]的整数。 |
| supportType | [DocType](vision-document-scanner.md#doctype)[] | 否 | 否 | 支持识别的文件类型。默认值：[DocType.DOC]。  **设备行为差异：** 部分机型仅支持配置[DocType.DOC]。若设备配置不支持的属性，此属性将采用默认值。 |
| isGallerySupported | boolean | 否 | 是 | 是否支持从图库进行选图。true：支持。false：不支持。默认值：true。 |
| defaultFilterId | [FilterId](vision-document-scanner.md#filterid) | 否 | 是 | 初始滤镜效果。默认增强。 |
| editTabs | [EditTab](vision-document-scanner.md#edittab)[] | 否 | 是 | Tab栏中展示的功能按钮。默认全部显示。 |
| defaultShootingMode | [ShootingMode](vision-document-scanner.md#shootingmode) | 否 | 是 | 初始拍摄模式。默认手动拍摄。 |
| isShareable | boolean | 否 | 是 | 是否支持分享功能。true：支持。false：不支持。默认支持。 |
| saveOptions | [SaveOption](vision-document-scanner.md#saveoption)[] | 否 | 是 | 保存选项。supportType为[DOC]时，默认值为[SaveOption.JPG]，supportType为[SHEET]时，默认值为[SaveOption.EXCEL]，supportType为[DOC,SHEET]时，默认值为[SaveOption.JPG, SaveOption.EXCEL]，DOC和SHEET类型的保存选项互相独立，互不影响。 |
| originalUris | string[] | 否 | 是 | 初始提供的[图片URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)列表，若此值不为空，则直接使用这里的值跳转编辑页面。默认值为空，数组最大长度为50。不符合规格的图片将被剔除，图片规格如下（单位px）：  1、单边长度最小224，最大8000。  2、宽高之积小于等于 6000\*8000。  3、高宽比或宽高比小于等于3。  **说明：**  此参数实际功能于5.0.5(17)版本正式上线，此前版本为预留参数。 |

## DocType

PhoneTablet

支持识别的文件类型枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOC | 0 | 文档类型。 |
| SHEET | 1 | 表格类型。 |

## FilterId

PhoneTablet

给图片添加的滤镜枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIGINAL | 0 | 原图滤镜。 |
| MONOCHROME | 1 | 黑白滤镜。 |
| STRENGTHEN | 2 | 增强滤镜。 |

## ShootingMode

PhoneTablet

拍照模式枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 自动拍照模式。 |
| MANUAL | 1 | 手动拍照模式。 |

## EditTab

PhoneTablet

Tab栏按钮枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ROTATE\_TAB | 0 | 旋转按钮。 |
| DELETE\_TAB | 1 | 删除按钮。 |
| RESHOOT\_TAB | 2 | 重拍按钮。 |

## SaveOption

PhoneTablet

保存选项枚举。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| JPG | 0 | JPEG格式。（仅用于文档类型的保存格式） |
| PDF | 1 | PDF格式。（仅用于文档类型的保存格式） |
| EXCEL | 2 | EXCEL格式。（仅用于表格类型的保存格式） |

## DocumentScannerResultCallback

PhoneTablet

type DocumentScannerResultCallback = (code: number, saveType: SaveOption, uris: string[]) => void

文档扫描结果回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.DocScan

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 返回的结果码：  -1：无结果返回  200：识别成功  1008601001：uris无效  **说明：**  从5.0.5(17)开始支持状态码1008601001 |
| saveType | [SaveOption](vision-document-scanner.md#saveoption) | 是 | 结果保存格式。 |
| uris | string[] | 是 | 文档uri列表。 |
