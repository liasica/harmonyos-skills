---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiext
title: @ohos.wifiext (WLAN扩展接口)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 已停止维护的接口 > @ohos.wifiext (WLAN扩展接口)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9c1467338372f56940b945235383ef50d76192d455edfe395e0bbefc771d69c
---

该模块主要提供WLAN扩展接口，供非通用类型产品使用。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该文档中的接口只供非通用类型产品使用，如路由器等，对于常规类型产品，不应该使用这些接口。

从API Version 9开始，该接口不再维护，推荐使用[@ohos.wifiManagerExt（WLAN扩展接口）](js-apis-wifimanagerext.md)等相关接口。

## 导入模块

```
1. import wifiext from '@ohos.wifiext';
```

## wifiext.enableHotspot(deprecated)

enableHotspot(): boolean;

使能WLAN热点。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.enableHotspot](js-apis-wifimanagerext.md#wifimanagerextenablehotspotdeprecated)替代。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 操作结果， true: 成功， false: 失败。 |

## wifiext.disableHotspot(deprecated)

disableHotspot(): boolean;

去使能WLAN热点。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.disableHotspot](js-apis-wifimanagerext.md#wifimanagerextdisablehotspotdeprecated)替代。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 操作结果， true: 成功， false: 失败。 |

## wifiext.getSupportedPowerModel(deprecated)

getSupportedPowerModel(): Promise<Array<PowerModel>>

获取支持的功率模式。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](js-apis-wifimanagerext.md#wifimanagerextgetsupportedpowermode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[PowerModel](js-apis-wifiext.md#powermodel)>> | Promise对象。表示功率模式。 |

## PowerModel

表示功率模式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SLEEPING | 0 | 睡眠模式。 |
| GENERAL | 1 | 常规模式。 |
| THROUGH\_WALL | 2 | 穿墙模式。 |

## wifiext.getSupportedPowerModel

getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void

获取支持的功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[PowerModel](js-apis-wifiext.md#powermodel)>> | 是 | 回调函数。当操作成功时，err为0，data表示支持的功率模式。如果err为非0，表示处理出现错误。 |

## wifiext.getPowerModel(deprecated)

getPowerModel(): Promise<PowerModel>

获取功率模式，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](js-apis-wifimanagerext.md#wifimanagerextgetpowermode)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PowerModel](js-apis-wifiext.md#powermodel)> | Promise对象。表示功率模式。 |

## wifiext.getPowerModel(deprecated)

getPowerModel(callback: AsyncCallback<PowerModel>): void

获取功率模式。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[wifiManagerExt.getSupportedPowerModel](js-apis-wifimanagerext.md#wifimanagerextgetpowermode-1)替代。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PowerModel](js-apis-wifiext.md#powermodel)> | 是 | 回调函数。当操作成功时，err为0，data表示功率模式。如果err为非0，表示处理出现错误。 |

## wifiext.setPowerModel

setPowerModel(model: PowerModel) : boolean;

设置功率模式。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | [PowerModel](js-apis-wifiext.md#powermodel) | 是 | 功率模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 操作结果， true: 成功， false: 失败。 |
