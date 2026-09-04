---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-manager
title: manager（星闪开关能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > manager（星闪开关能力）
category: harmonyos-references
scraped_at: 2026-09-05T06:18:55+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:6745d9b6dbb6f06c664b7e6b502e078dbbd33c84009721ee2fdd24b16428a43e
---

本模块提供了管理星闪基础能力，包括获取设备信息、订阅状态变化事件等。

**起始版本：** 5.0.1(13)

## 导入模块

```typescript
import { manager } from '@kit.NearLinkKit';
```

## PairingState

type PairingState = constant.PairingState

表示和远端设备的配对状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.PairingState](nearlink-constant.md#pairingstate) | 和远端设备的配对状态。 |

## ConnectionState

type ConnectionState = constant.ConnectionState

表示和远端设备的连接状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## AcbState

type AcbState = constant.AcbState

表示和远端设备的逻辑链路连接状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

## getState

getState(): NearlinkState

查询星闪开关状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NearlinkState](nearlink-manager.md#nearlinkstate) | 表示星闪开关状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let state: manager.NearlinkState = manager.getState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## isNearLinkSupported

isNearLinkSupported(): boolean

查询当前设备是否支持星闪服务。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示设备支持星闪。false表示设备不支持星闪。 |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupported: boolean = manager.isNearLinkSupported();
  if (isSupported) {
    console.info('NearLink is supported on this device.');
  } else {
    console.info('NearLink is not supported on this device.');
  }
} catch (err) {
  console.error('Error occurred: ' + (err as BusinessError).code + ', ' + (err as BusinessError).message);
}
```

## getLocalName

getLocalName(): string

查询本机星闪名称。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示星闪设备本地名称。最大长度为30。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let name: string = manager.getLocalName();
  console.info('name:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## getPairedDevices

getPairedDevices(): Array<string>

获取与当前设备配对的设备列表。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.0.1(21)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 配对设备地址的列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let pairedDevices: Array<string> = manager.getPairedDevices();
  if (pairedDevices.length > 0) {
        console.info('getPairedDevices return: ' + JSON.stringify(pairedDevices));
    } else {
        console.info('No Paired Devices found.');
    }
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on( 'stateChange')

on(type: 'stateChange', callback: Callback<NearlinkState>): void

订阅星闪开关状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，表示星闪开关状态变化事件。  当星闪被开启或关闭时，可触发该事件。 |
| callback | Callback<[NearlinkState](nearlink-manager.md#nearlinkstate)> | 是 | 回调函数，返回星闪的开关状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.NearlinkState> = (data: manager.NearlinkState) => {
  if (data === manager.NearlinkState.STATE_TURNING_ON) {
    console.info('nearlink STATE_TURNING_ON');
  } else if (data === manager.NearlinkState.STATE_ON) {
    console.info('nearlink STATE_ON');
  } else if (data === manager.NearlinkState.STATE_TURNING_OFF) {
    console.info('nearlink STATE_TURNING_OFF');
  } else if (data === manager.NearlinkState.STATE_OFF) {
    console.info('nearlink STATE_OFF');
  }
};
try {
  manager.on('stateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off( 'stateChange')

off(type: 'stateChange', callback?: Callback<NearlinkState>): void

取消订阅星闪开关状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'stateChange'，表示星闪开关状态变化事件。 |
| callback | Callback<[NearlinkState](nearlink-manager.md#nearlinkstate)> | 否 | 回调函数，返回星闪的开关状态。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('stateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on( 'pairingStateChange')

on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void

订阅配对状态变化事件。。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pairingStateChange'，表示配对状态变化事件。  当调用[remoteDevice.startPairing](nearlink-remote-device.md#startpairing)发起主动配对，或者本机设备收到其他设备的配对请求时，触发该事件。 |
| callback | Callback<[PairingStateParam](nearlink-manager.md#pairingstateparam)> | 是 | 回调函数，返回订阅的配对状态变化结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPairingStateEvent:(data: manager.PairingStateParam) => void = (data: manager.PairingStateParam) => {
  console.info('onPairStateChange addr: ' + data.address + ', state: ' + data.state);
};
try {
  manager.on('pairingStateChange', onPairingStateEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off( 'pairingStateChange')

off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void

取消订阅配对状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pairingStateChange'，表示配对状态变化事件。 |
| callback | Callback<[PairingStateParam](nearlink-manager.md#pairingstateparam)> | 否 | 回调函数，返回订阅的配对状态变化结果。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('pairingStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on( 'connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void

订阅连接状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。  和远端设备之间的连接状态发生变化时，触发该事件。 |
| callback | Callback<[ConnectionStateParam](nearlink-manager.md#connectionstateparam)> | 是 | 回调函数，返回订阅的连接状态变化事件上报结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.ConnectionStateParam> = (data: manager.ConnectionStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('connectionStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void

取消订阅连接状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示连接状态变化事件。 |
| callback | Callback<[ConnectionStateParam](nearlink-manager.md#connectionstateparam)> | 否 | 回调函数，返回订阅的连接状态变化事件上报结果。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('connectionStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on('acbStateChange')

on(type: 'acbStateChange', callback: Callback<AcbStateParam>): void

订阅逻辑链路连接状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'acbStateChange'，表示逻辑链路连接状态变化事件。  和远端设备之间的逻辑链路连接状态发生变化时，触发该事件。 |
| callback | Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)> | 是 | 回调函数，返回订阅的逻辑链路连接状态变化事件上报结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.AcbStateParam> = (data: manager.AcbStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('acbStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off( 'acbStateChange')

off(type: 'acbStateChange', callback?: Callback<AcbStateParam>): void

取消订阅逻辑链路连接状态变化事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'acbStateChange'，表示逻辑链路连接状态变化事件。 |
| callback | Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)> | 否 | 回调函数，返回订阅的逻辑链路连接状态变化事件上报结果。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('acbStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## PairingStateParam

订阅的配对状态变化结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的配对状态发生变化。地址格式参考：11:22:33:AA:BB:FF。 |
| preState | [PairingState](nearlink-constant.md#pairingstate) | 否 | 否 | 本次上报之前的配对状态。 |
| state | [PairingState](nearlink-constant.md#pairingstate) | 否 | 否 | 当前配对状态。 |
| reason | [PairingReason](nearlink-manager.md#pairingreason) | 否 | 否 | 原因值。 |
| reasonMsg | string | 否 | 是 | 原因详情。该字段仅用于日志信息，不应用于逻辑处理。  **起始版本：** 26.0.0 |

## PairingRequestParam

表示订阅的配对请求事件上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示收到该设备的配对请求上报。地址格式参考：11:22:33:AA:BB:FF。 |
| passkey | string | 否 | 否 | 表示配对交互的配对码，显示给用户确认。长度固定为6，字符串内容为数字。 |
| pairingType | [PairingType](nearlink-manager.md#pairingtype) | 否 | 否 | 表示配对类型。 |

## ConnectionStateParam

订阅的连接状态变化事件上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的连接状态发生变化。地址格式参考：11:22:33:AA:BB:FF。 |
| preState | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 本次上报之前的连接状态。 |
| state | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 当前连接状态。 |
| connectionReason | [ConnectionReason](nearlink-manager.md#connectionreason) | 否 | 否 | 原因值。 |
| reasonMsg | string | 否 | 是 | 原因详情。该字段仅用于日志信息，不应用于逻辑处理。  **起始版本：** 26.0.0 |

## NearlinkState

星闪的开关状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_TURNING\_ON | 0 | 表示星闪正在打开。 |
| STATE\_ON | 1 | 表示星闪已打开。 |
| STATE\_TURNING\_OFF | 2 | 表示星闪正在关闭。 |
| STATE\_OFF | 3 | 表示星闪已关闭。 |

## PairingReason

表示星闪配对状态变化结果的原因值，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAIRING\_REASON\_SUCCESS | 0 | 表示配对成功。 |
| PAIRING\_REASON\_FAILURE | 1 | 表示配对失败。 |
| PAIRING\_REASON\_PROFILE\_UNSUPPORTED | 2 | 表示对端设备不支持服务导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_EXCEED\_ACB\_MAX | 3 | 表示连接设备数已达上限导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_REMOTE\_CANCELED | 4 | 表示对端设备取消配对导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_LOCAL\_CANCELED | 5 | 表示本端设备取消配对导致配对失败。  **起始版本：** 5.1.0(18) |

## PairingType

星闪配对类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_PASSKEY\_CONFIRMATION | 0 | 表示不需要passkey的配对方式，用户无需检查配对码。 |
| PAIRING\_TYPE\_PASSCODE | 1 | 表示通行码鉴权方式，用户需在一端设备输入另一端设备显示的配对码。  **起始版本：** 5.1.0(18) |
| PAIRING\_TYPE\_NUMBER\_COMPARE | 2 | 表示数字比较鉴权方式，用户需在两端设备确认配对码一致。  **起始版本：** 5.1.0(18) |

## ConnectionReason

星闪连接状态变化结果的原因值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTION\_SUCCESS | 0 | 表示连接成功。 |
| CONNECTION\_FAILURE | 1 | 表示连接失败。 |

## AcbStateParam

订阅的逻辑链路连接状态变化事件上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的逻辑链路连接状态发生变化。地址格式参考：11:22:33:AA:BB:FF。 |
| state | [AcbState](nearlink-constant.md#acbstate) | 否 | 否 | 当前逻辑链路连接状态。 |
