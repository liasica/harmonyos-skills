---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifimanagerext
title: @ohos.wifiManagerExt (WLAN扩展接口)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.wifiManagerExt (WLAN扩展接口)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de19ddec7001a66f969d0b0503c7a801c843f64f9d3d7bd6e962bb846e2c98da
---

该模块主要提供WLAN扩展接口，供非通用类型产品使用。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

该文档中的接口只供非通用类型产品使用，如路由器等，对于常规类型产品，不应该使用这些接口。

## 导入模块

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## wifiManagerExt.enableHotspot(deprecated)

enableHotspot(): void

使能WLAN热点。

说明

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. try {
4. wifiManagerExt.enableHotspot();
5. }catch(error){
6. console.error("failed: " + JSON.stringify(error));
7. }
```

## wifiManagerExt.disableHotspot(deprecated)

disableHotspot(): void

去使能WLAN热点。

说明

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. try {
4. wifiManagerExt.disableHotspot();
5. }catch(error){
6. console.error("failed: " + JSON.stringify(error));
7. }
```

## wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(): Promise<Array<PowerMode>>

获取支持的功率模式。使用Promise异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[PowerMode](js-apis-wifimanagerext.md#powermode)>> | Promise对象。表示功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

## PowerMode

表示功率模式的枚举。

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SLEEPING | 0 | 睡眠模式。 |
| GENERAL | 1 | 常规模式。 |
| THROUGH\_WALL | 2 | 穿墙模式。 |

## wifiManagerExt.getSupportedPowerMode

getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void

获取支持的功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[PowerMode](js-apis-wifimanagerext.md#powermode)>> | 是 | 回调函数。当操作成功时，err为0，data表示支持的功率模式。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. wifiManagerExt.getSupportedPowerMode((err, data: wifiManagerExt.PowerMode[]) => {
4. if (err) {
5. console.error("get supported power mode info error: ", err);
6. return;
7. }
8. console.info("get supported power mode info: " + JSON.stringify(data));
9. });
```

## wifiManagerExt.getPowerMode

getPowerMode(): Promise<PowerMode>

获取功率模式，使用Promise异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PowerMode](js-apis-wifimanagerext.md#powermode)> | Promise对象。表示功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. async function getWifiPowerMode() {
4. try {
5. // 1. 使用 await 等待 Promise 解析完成
6. let model = await wifiManagerExt.getPowerMode();

8. console.info("model info: " + model);
9. } catch (error) {
10. // 2. 捕获 Promise 拒绝时的错误
11. console.error("failed: " + JSON.stringify(error));
12. }
13. }
```

## wifiManagerExt.getPowerMode

getPowerMode(callback: AsyncCallback<PowerMode>): void

获取功率模式。使用callback异步回调。

**需要权限：** ohos.permission.GET\_WIFI\_INFO

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[PowerMode](js-apis-wifimanagerext.md#powermode)> | 是 | 回调函数。当操作成功时，err为0，data表示功率模式。如果err为非0，表示处理出现错误。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. wifiManagerExt.getPowerMode((err, data:wifiManagerExt.PowerMode) => {
4. if (err) {
5. console.error("Failed to get linked information");
6. return;
7. }
8. console.info("get power mode info: " + JSON.stringify(data));
9. });

11. wifiManagerExt.getPowerMode().then(data => {
12. console.info("get power mode info: " + JSON.stringify(data));
13. }).catch((error:number) => {
14. console.error("get power mode error");
15. });
```

## wifiManagerExt.setPowerMode(deprecated)

setPowerMode(mode: PowerMode) : void

设置功率模式。

说明

从API version 9开始支持，从API version 10开始废弃。

**需要权限：** ohos.permission.MANAGE\_WIFI\_HOTSPOT\_EXT

**系统能力：** SystemCapability.Communication.WiFi.AP.Extension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PowerMode](js-apis-wifimanagerext.md#powermode) | 是 | 功率模式。 |

**错误码：**

以下错误码的详细介绍请参见[WIFI错误码](errorcode-wifi.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2701000 | Operation failed. |

**示例：**

```
1. import { wifiManagerExt } from '@kit.ConnectivityKit';

3. try {
4. let model = 0;
5. wifiManagerExt.setPowerMode(model);
6. }catch(error){
7. console.error("failed: " + JSON.stringify(error));
8. }
```
