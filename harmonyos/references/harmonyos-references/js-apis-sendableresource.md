---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableresource
title: SendableResource
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > ArkTS API > global > SendableResource
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eaa124c592cdf2d8d158f2153ffe5d93893b2d21e1e797d19a02819df20e91c0
---

本模块提供SendableResource资源相关信息，包括应用包名、应用模块名、资源类型等。SendableResource实现了[ISendable](../harmonyos-guides/arkts-sendable.md#isendable)接口，支持跨线程传输，用于在多线程场景下访问应用资源。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { resourceManager } from '@kit.LocalizationKit';
```

## SendableResource

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用包名。 |
| moduleName | string | 否 | 否 | 应用模块名。 |
| id | number | 否 | 否 | 资源ID，取值如下：  - 应用资源区间：[0x01000000, 0x06FFFFFF] 和 [0x08000000, 0xFFFFFFFF]，表示应用自身的资源ID。  - 系统资源区间：[0x07000000, 0x07FFFFFF]，表示系统预置的资源ID。 |
| params | collections.Array<string | number> | 否 | 是 | 资源参数，包括：资源名（string类型）、格式化接口替换值（按占位符顺序提供string或number）、复数接口量词（number类型，表示数量）。格式化接口的替换值用于字符串格式化时的参数替换，复数接口的量词用于选择多语言环境下的复数形式。 |
| type | number | 否 | 是 | 资源类型，取值如下：  - 10001：color  - 10002：float  - 10003：string  - 10004：plural  - 10005：boolean  - 10006：intarray  - 10007：integer  - 10008：pattern  - 10009：strarray  - 20000：media  - 30000：rawfile  - 40000：symbol |
