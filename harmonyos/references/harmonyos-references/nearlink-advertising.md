---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-advertising
title: advertising（星闪广播能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > advertising（星闪广播能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:efd7f314f5966078d65667b65cfd154a957e16f42f227bad6381268b4e70fb8a
---

本模块提供了发送星闪广播的相关功能，包括启动广播、停止广播、订阅广播状态等。

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { advertising } from '@kit.NearLinkKit';
```

## AdvertisingParams

PhonePC/2in1TabletTVWearable

表示发送广播携带的参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingSettings | [AdvertisingSettings](nearlink-advertising.md#advertisingsettings) | 否 | 否 | 广播配置参数。 |
| advertisingData | [AdvertisingData](nearlink-advertising.md#advertisingdata) | 否 | 否 | 广播数据包。 |

## AdvertisingSettings

PhonePC/2in1TabletTVWearable

表示广播配置参数。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 广播间隔配置参数。单位slot，范围160-16777215，默认值为5000。1个slot对应的时间长度是0.125ms，例如：5000\*0.125=625ms。 |
| power | [TxPowerMode](nearlink-advertising.md#txpowermode) | 否 | 是 | 广播发射功率配置参数。如果不配置，则默认值为ADV\_TX\_POWER\_LOW。 |
| isConnectable | boolean | 否 | 是 | true: 表示可连接的广播。false：表示不可连接的广播。默认值为true。 |

## AdvertisingData

PhonePC/2in1TabletTVWearable

表示广播数据包。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 是 | 服务UUID列表。若未配置则默认不携带该字段。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| manufacturerData | Array<[ManufacturerData](nearlink-advertising.md#manufacturerdata)> | 否 | 是 | 厂商数据。若未配置则默认不携带该字段。 |
| serviceData | Array<[ServiceData](nearlink-advertising.md#servicedata)> | 否 | 是 | 服务数据。若未配置则默认不携带该字段。 |
| includeDeviceName | boolean | 否 | 是 | 指示广播数据中是否携带本机设备名。true：表示包含设备名称。false：表示不包含设备名称。默认值为false。 |

## ManufacturerData

PhonePC/2in1TabletTVWearable

表示厂商数据。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturerId | number | 否 | 否 | 厂商ID。取值范围(0, 65535]。 |
| manufacturerData | ArrayBuffer | 否 | 否 | 厂商数据。 |

## ServiceData

PhonePC/2in1TabletTVWearable

表示服务相关数据。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| serviceData | ArrayBuffer | 否 | 否 | 表示服务数据。 |

## AdvertisingStateChangeInfo

PhonePC/2in1TabletTVWearable

表示广播启停状态变化信息。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingId | number | 否 | 否 | 表示广播ID。取值范围[0, 255]。 |
| state | [AdvertisingState](nearlink-advertising.md#advertisingstate) | 否 | 否 | 表示当前广播状态。 |

## TxPowerMode

PhonePC/2in1TabletTVWearable

表示广播发送模式，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADV\_TX\_POWER\_LOW | 1 | 表示低功耗模式。 |
| ADV\_TX\_POWER\_MEDIUM | 2 | 表示中等功耗模式。 |
| ADV\_TX\_POWER\_HIGH | 3 | 表示高功耗模式。 |

## AdvertisingState

PhonePC/2in1TabletTVWearable

表示广播状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED | 1 | 表示广播已启动。 |
| STOPPED | 2 | 表示广播已停止。 |

## startAdvertising

PhonePC/2in1TabletTVWearable

startAdvertising(advertisingParams: AdvertisingParams): Promise<number>

发送星闪广播。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingParams | [AdvertisingParams](nearlink-advertising.md#advertisingparams) | 是 | 广播相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回本次开启的广播ID。广播ID是随机分配的唯一标识值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { advertising } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let manufactureValueBuffer = new Uint8Array(4);
5. manufactureValueBuffer[0] = 1;
6. manufactureValueBuffer[1] = 2;
7. manufactureValueBuffer[2] = 3;
8. manufactureValueBuffer[3] = 4;
9. let serviceValueBuffer = new Uint8Array(4);
10. serviceValueBuffer[0] = 4;
11. serviceValueBuffer[1] = 6;
12. serviceValueBuffer[2] = 7;
13. serviceValueBuffer[3] = 8;
14. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
15. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
16. let setting: advertising.AdvertisingSettings = {
17. interval:5000,
18. power:advertising.TxPowerMode.ADV_TX_POWER_LOW
19. };
20. let manufactureDataUnit: advertising.ManufacturerData = {
21. manufacturerId:4567,
22. manufacturerData:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: advertising.ServiceData = {
25. serviceUuid:"37bea880-fc70-11ea-b720-000000001234",
26. serviceData:serviceValueBuffer.buffer
27. };
28. let advData: advertising.AdvertisingData = {
29. serviceUuids:["37bea880-fc70-11ea-b720-000000001234"],
30. manufacturerData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advertisingParams: advertising.AdvertisingParams = {
34. advertisingSettings: setting,
35. advertisingData: advData
36. }
37. let advId = -1;
38. try {
39. advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
40. advId = advertisingId;
41. console.info('advertising id:'+ JSON.stringify(advId));
42. });
43. } catch (err) {
44. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
45. }
```

## stopAdvertising

PhonePC/2in1TabletTVWearable

stopAdvertising(advertisingId: number): Promise<void>

停止发送星闪广播。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingId | number | 是 | 广播ID，开启广播时获取。取值范围[0, 255]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { advertising } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let advId: number = 1; // advId在开启广播时获取，参考startAdvertising接口返回值
6. advertising.stopAdvertising(advId).then(() => {
7. console.info("stop advertising success");
8. });
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## on( 'advertisingStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

订阅星闪广播状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"advertisingStateChange"字符串，表示星闪广播状态变化事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](nearlink-advertising.md#advertisingstatechangeinfo)> | 是 | 表示广播状态变化回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { advertising } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void = (data: advertising.AdvertisingStateChangeInfo) => {
5. console.info('advertisingId:'+ data.advertisingId);
6. console.info('advertisingState:'+ data.state);
7. }
8. try {
9. advertising.on('advertisingStateChange', onReceiveEvent);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## off( 'advertisingStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

取消订阅星闪广播状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"advertisingStateChange"字符串，表示星闪广播状态变化事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](nearlink-advertising.md#advertisingstatechangeinfo)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { advertising } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. advertising.off('advertisingStateChange');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```
