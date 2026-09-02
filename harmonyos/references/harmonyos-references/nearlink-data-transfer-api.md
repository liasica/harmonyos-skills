---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-data-transfer-api
title: dataTransfer（星闪数传能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > dataTransfer（星闪数传能力）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:368cacd0677f8d9cc4cc0da95885f981da1716906c599637822dccb8f5ade1be
---

本模块提供了星闪数据传输的功能。

**起始版本：** 5.1.0(18)

## 导入模块

```typescript
import { dataTransfer } from '@kit.NearLinkKit';
```

## ConnectionState

type ConnectionState = constant.ConnectionState

表示和远端设备的连接状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## createPort

createPort(uuid: string): void

注册端口通道。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uuid | string | 是 | 可填写16字节星闪服务UUID，或填写2字节支持数传的星闪标准服务UUID。UUID格式参考“[星闪标准服务标识](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)”。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700020 | The UUID is already registered. |
| 1009700021 | The number of ports exceeds the upper limit. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID
  dataTransfer.createPort(uuid);
  console.info('create port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## destroyPort

destroyPort(uuid: string): void

销毁端口通道。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uuid | string | 是 | 可填写16字节星闪服务UUID，或填写2字节支持数传的星闪标准服务UUID。UUID格式参考“[星闪标准服务](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)”。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700022 | The UUID is not registered. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let uuid: string = 'FFFFFFFF-FC70-11EA-B720-000078951234'; // 星闪服务UUID
  dataTransfer.destroyPort(uuid);
  console.info('destroy port success');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## connect

connect(params: ConnectionParams): Promise<void>

连接远端设备，建立端口通道。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionParams](nearlink-data-transfer-api.md#connectionparams) | 是 | 指明端口的连接参数。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 构造端口通道建立的参数
  let connectionParams:dataTransfer.ConnectionParams = {
    address: '01:02:03:04:05:06', // 星闪远端设备地址
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
    mtu: 1024 // 期望发送数据包的字节大小，可选参数
  };
  dataTransfer.connect(connectionParams).then(()=>{
    console.info('connect success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## disconnect

disconnect(params: ConnectionParams): Promise<void>

断连远端设备，销毁端口通道。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionParams](nearlink-data-transfer-api.md#connectionparams) | 是 | 指明端口的连接参数。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 构造端口通道建立的参数
  let connectionParams:dataTransfer.ConnectionParams = {
    address: '01:02:03:04:05:06', // 星闪远端设备地址
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
    mtu: 1024 // 期望发送数据包的字节大小，可选参数
  };
  dataTransfer.disconnect(connectionParams).then(()=>{
    console.info('disconnect success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on('connectionStateChanged')

on(type: 'connectionStateChanged', callback: Callback<ConnectionResult>): void

订阅端口通道连接状态变更事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChanged'，表示连接状态发生变化的事件。  当端口通道连接状态发生变化时，触发该事件。  当调用[datatransfer.connect](nearlink-data-transfer-api.md#connect)或[datatransfer.disconnect](nearlink-data-transfer-api.md#disconnect)时，可能引起连接状态发生变化。 |
| callback | Callback<[ConnectionResult](nearlink-data-transfer-api.md#connectionresult)> | 是 | 回调函数，返回与远端设备端口连接参数的协商结果。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<dataTransfer.ConnectionResult> = (data: dataTransfer.ConnectionResult) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('connectionStateChanged', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off('connectionStateChanged')

off(type: 'connectionStateChanged', callback?: Callback<ConnectionResult>): void

取消订阅端口通道连接状态变更事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChanged'，表示数传连接状态发生变化的事件。 |
| callback | Callback<[ConnectionResult](nearlink-data-transfer-api.md#connectionresult)> | 否 | 回调函数，返回与远端设备端口连接参数的协商结果。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dataTransfer.off('connectionStateChanged');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## getConnectionState

getConnectionState(params: ConnectionStateParams): ConnectionState

获取与远端设备之间的端口通道连接状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [ConnectionStateParams](nearlink-data-transfer-api.md#connectionstateparams) | 是 | 指明端口的连接参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的星闪端口通道连接状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 1009700003 | NearLink is off. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let connectionStateParams:dataTransfer.ConnectionStateParams = {
    address: '01:02:03:04:05:06', // 扫描获取到的远端设备地址
    uuid: 'FFFFFFFF-FC70-11EA-B720-000078951234' // 星闪服务UUID示例
  };
  let state:dataTransfer.ConnectionState = dataTransfer.getConnectionState(connectionStateParams);
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## writeData

writeData(params: DataParams): Promise<void>

通过设备地址和uuid向远端设备发数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [DataParams](nearlink-data-transfer-api.md#dataparams) | 是 | 指明发送数据的参数，包含远端设备地址、服务UUID以及发送的数据包。 |

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
| 1009700023 | The data writing process is congested. |
| 1009700099 | Operation failed. |

**示例：**

```typescript
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 构造发送数据参数
  let transferValueBuffer: Uint8Array = new Uint8Array(4);
  transferValueBuffer[0] = 1;
  transferValueBuffer[1] = 2;
  transferValueBuffer[2] = 3;
  transferValueBuffer[3] = 4;
  let dataParams: dataTransfer.DataParams = {
    address: '01:02:03:04:05:06', // 星闪远端设备地址
    uuid: '37BEA880-FC70-11EA-B720-00000000060D', // 星闪服务UUID
    data: transferValueBuffer.buffer // 星闪设备间传输的数据
  };
  dataTransfer.writeData(dataParams).then(() => {
    console.info('writeData success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## on('readData')

on(type: 'readData', callback: Callback<DataParams>): void

订阅端口通道数据接收事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readData'，表示端口通道数据接收事件。  当收到远端设备的端口数据时，触发该事件。 |
| callback | Callback<[DataParams](nearlink-data-transfer-api.md#dataparams)> | 是 | 回调函数，返回端口数据发送和接收的参数。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError, Callback } from '@kit.BasicServicesKit';

let callback: Callback<dataTransfer.DataParams> = (data: dataTransfer.DataParams) => {
  console.info('data: ' + JSON.stringify(data));
};
try {
  dataTransfer.on('readData', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## off('readData')

off(type: 'readData', callback?: Callback<DataParams>): void

取消订阅端口通道数据接收事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'readData'，表示端口通道数据接收事件。 |
| callback | Callback<[DataParams](nearlink-data-transfer-api.md#dataparams)> | 否 | 回调函数，返回端口数据发送和接收的参数。  填写该参数则取消当前callback订阅。不填写该参数则取消该type对应的所有回调。 |

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
import { dataTransfer } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dataTransfer.off('readData');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## ConnectionParams

发起端口连接的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考：11:22:33:AA:BB:FF。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| mtu | number | 否 | 是 | 期望发送数据的包长，单位为byte。范围[0, 65535]，默认值为512。 |
| transferMode | [TransferMode](nearlink-data-transfer-api.md#transfermode) | 否 | 是 | 表示和远端设备的数据传输模式。默认值是BASIC。 |

## DataParams

端口数据发送和接收的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考：11:22:33:AA:BB:FF。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| data | ArrayBuffer | 否 | 否 | 发送的数据包。 |

## ConnectionResult

与远端设备端口连接参数的协商结果

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考：11:22:33:AA:BB:FF。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |
| mtu | number | 否 | 否 | 协商后的发送和接收数据的包长，单位为byte，范围[0, 65535]。 |
| state | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 与远端设备的连接状态。 |

## ConnectionStateParams

获取端口通道连接状态所需参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 远端设备的星闪地址。地址格式参考：11:22:33:AA:BB:FF。 |
| uuid | string | 否 | 否 | 星闪服务UUID，例如：37bea880-fc70-11ea-b720-000000004386。UUID格式参考[星闪标准服务UUID](../harmonyos-guides/nearlink-faq.md#星闪标准服务uuid的格式)。 |

## TransferMode

表示和远端设备的数据传输模式，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC | 0 | 表示基础模式，无数据重传机制。 |
| RELIABLE | 1 | 表示可靠模式，有数据重传机制。 |
