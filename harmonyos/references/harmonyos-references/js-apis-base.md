---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base
title: @ohos.base (公共回调信息)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.base (公共回调信息)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6a4e15ce37adb3d71617284ed88e70f838898691c1911de9755fde4b93203d2
---

本模块定义了HarmonyOS ArkTS接口的公共回调类型，包括接口调用时出现的公共回调和公共错误信息。

说明

* 本模块首批接口从 API version 6 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API version 12开始，本模块接口支持在ArkTS卡片中使用。

## 导入模块

PhonePC/2in1TabletTVWearableLite Wearable

ArkTS示例：

```
1. import { AsyncCallback, BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
```

JS示例：

```
1. import base from '@ohos.base';
```

## Callback

PhonePC/2in1TabletTVWearableLite Wearable

Callback<T> {

(data: T): void;

}

通用回调函数。

开发者在使用时，可自定义data的类型，回调将返回对应类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 接口调用时的公共回调信息。 |

## ErrorCallback

PhonePC/2in1TabletTVWearableLite Wearable

ErrorCallback<T extends Error = BusinessError> {

(err: T): void;

}

通用回调函数，携带错误参数。

回调返回的信息为[BusinessError](js-apis-base.md#businesserror)类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | T | 是 | 接口调用失败的公共错误信息。 |

## AsyncCallback

PhonePC/2in1TabletTVWearableLite Wearable

AsyncCallback<T, E = void> {

(err: BusinessError<E>, data: T): void;

}

通用回调函数，携带错误参数和异步返回值。

错误参数为[BusinessError](js-apis-base.md#businesserror)类型的信息。

异步返回值的类型由开发者自定义，回调将返回对应类型的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| err | [BusinessError](js-apis-base.md#businesserror) | 是 | 接口调用失败的公共错误信息。 |
| data | T | 是 | 接口调用时的公共回调信息。 |

## BusinessError

PhonePC/2in1TabletTVWearableLite Wearable

BusinessError<T = void> extends Error { code: number; data?: T; }

错误参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Base

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 接口调用失败返回的错误码信息。 |
| data | T | 否 | 接口调用时的公共回调信息。如果不填，则回调不返回相关信息。 |
