---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-advertising
title: advertising（星闪广播能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > advertising（星闪广播能力）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b241de7863d52417ea86c869e5d04f7e05807feb7fc37e07c3c49080c3259850
---

本模块提供了发送星闪广播的相关功能，包括启动广播、停止广播、订阅广播状态等。

**起始版本：** 5.0.1(13)

## 导入模块

```typescript
import { advertising } from '@kit.NearLinkKit';
```

## AdvertisingParams

表示发送广播携带的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingSettings | [AdvertisingSettings](nearlink-advertising.md#advertisingsettings) | 否 | 否 | 广播配置参数。 |
| advertisingData | [AdvertisingData](nearlink-advertising.md#advertisingdata) | 否 | 否 | 广播数据包。 |

## AdvertisingSettings

表示广播配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 广播间隔配置参数。单位slot，范围160-16777215，默认值为5000。1个slot对应的时间长度是0.125ms，例如：5000\*0.125=625ms。 |
| power | [TxPowerMode](nearlink-advertising.md#txpowermode) | 否 | 是 | 广播发射功率配置参数。如果不配置，则默认值为ADV\_TX\_POWER\_LOW。 |
| isConnectable | boolean | 否 | 是 | true: 表示可连接的广播。false：表示不可连接的广播。默认值为true。 |

## AdvertisingData

表示广播数据包。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 是 | 服务UUID列表。若未配置则默认不携带该字段。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| manufacturerData | Array<[ManufacturerData](nearlink-advertising.md#manufacturerdata)> | 否 | 是 | 厂商数据。若未配置则默认不携带该字段。 |
| serviceData | Array<[ServiceData](nearlink-advertising.md#servicedata)> | 否 | 是 | 服务数据。若未配置则默认不携带该字段。 |
| includeDeviceName | boolean | 否 | 是 | 指示广播数据中是否携带本机设备名。true：表示包含设备名称。false：表示不包含设备名称。默认值为false。 |

## ManufacturerData

表示厂商数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturerId | number | 否 | 否 | 厂商ID。取值范围[1, 65535]。 |
| manufacturerData | ArrayBuffer | 否 | 否 | 厂商数据。 |

## ServiceData

表示服务相关数据。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| serviceData | ArrayBuffer | 否 | 否 | 表示服务数据。 |

## AdvertisingStateChangeInfo

表示广播启停状态变化信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingId | number | 否 | 否 | 表示广播ID。取值范围[0, 255]。 |
| state | [AdvertisingState](nearlink-advertising.md#advertisingstate) | 否 | 否 | 表示当前广播状态。 |

## TxPowerMode

表示广播发送模式，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADV\_TX\_POWER\_LOW | 1 | 表示低功耗模式。 |
| ADV\_TX\_POWER\_MEDIUM | 2 | 表示中等功耗模式。 |
| ADV\_TX\_POWER\_HIGH | 3 | 表示高功耗模式。 |

## AdvertisingState

表示广播状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED | 1 | 表示广播已启动。 |
| STOPPED | 2 | 表示广播已停止。 |

## startAdvertising

startAdvertising(advertisingParams: AdvertisingParams): Promise<number>

发送星闪广播。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;
let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = ' + JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = ' + JSON.stringify(serviceValueBuffer));
let setting: advertising.AdvertisingSettings = {
  interval:5000,
  power:advertising.TxPowerMode.ADV_TX_POWER_LOW
};
let manufactureDataUnit: advertising.ManufacturerData = {
  manufacturerId:4567,
  manufacturerData:manufactureValueBuffer.buffer
};
let serviceDataUnit: advertising.ServiceData = {
  serviceUuid:'37bea880-fc70-11ea-b720-000000001234',
  serviceData:serviceValueBuffer.buffer
};
let advData: advertising.AdvertisingData = {
  serviceUuids:['37bea880-fc70-11ea-b720-000000001234'],
  manufacturerData:[manufactureDataUnit],
  serviceData:[serviceDataUnit]
};
let advertisingParams: advertising.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData
};
let advId = -1;
try {
  advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
    advId = advertisingId;
    console.info('advertising id:' + JSON.stringify(advId));
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## stopAdvertising

stopAdvertising(advertisingId: number): Promise<void>

停止发送星闪广播。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let advId: number = 1; // advId在开启广播时获取，参考startAdvertising接口返回值
  advertising.stopAdvertising(advId).then(() => {
    console.info('stop advertising success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on( 'advertisingStateChange')

on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

订阅星闪广播状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示星闪广播状态事件。  当调用[advertising.startAdvertising](nearlink-advertising.md#startadvertising)、[advertising.stopAdvertising](nearlink-advertising.md#stopadvertising)时，均会触发该事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](nearlink-advertising.md#advertisingstatechangeinfo)> | 是 | 回调函数，返回广播状态变化数据。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void =
  (data: advertising.AdvertisingStateChangeInfo) => {
  console.info('advertisingId:' + data.advertisingId);
  console.info('advertisingState:' + data.state);
};
try {
  advertising.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off( 'advertisingStateChange')

off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

取消订阅星闪广播状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示广播状态事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](nearlink-advertising.md#advertisingstatechangeinfo)> | 否 | 回调函数，返回广播启停状态变化信息。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  advertising.off('advertisingStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
