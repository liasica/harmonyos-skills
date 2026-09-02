---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-remote-device
title: remoteDevice（对端设备的连接能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API > remoteDevice（对端设备的连接能力）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95a23596457e9969069abcc2185c5fa8e190501c0956e22404679c929a3e4d9e
---

本模块提供了查询远端设备信息、发起配对等功能。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

## 导入模块

```typescript
import { remoteDevice } from '@kit.NearLinkKit';
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

## DeviceClass

type DeviceClass = constant.DeviceClass

表示设备类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.DeviceClass](nearlink-constant.md#deviceclass) | 设备类型。 |

## AcbState

type AcbState = constant.AcbState

表示和远端设备的逻辑链路连接状态，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

## createRemoteDevice

createRemoteDevice(address: string): RemoteDevice

创建远端设备实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 远端设备地址。地址格式参考：11:22:33:AA:BB:FF。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RemoteDevice](nearlink-remote-device.md#remotedevice) | 远端设备实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-nearlink.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```typescript
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  console.info('device: ' + JSON.stringify(device));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## RemoteDevice

**说明** 

提供远端设备的操作方法，使用前需要使用[remoteDevice.createRemoteDevice](nearlink-remote-device.md#createremotedevice)方法创建一个远端设备[RemoteDevice](nearlink-remote-device.md#remotedevice)实例。一个设备只需要创建一次，无需多次创建。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

### startPairing

startPairing(): Promise<void>

发起与远端设备的配对。使用Promise异步回调。发起配对后，将依据本端与远端设备的输入输出能力标识弹出不同类型的弹窗，需使用者进一步确认。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  device.startPairing().then(()=>{
    console.info('start pairing success');
  }).catch ((err: BusinessError) => {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getPairingState

getPairingState(): PairingState

获取和远端设备的配对状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PairingState](nearlink-constant.md#pairingstate) | 和远端设备的配对状态。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.PairingState = device.getPairingState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getDeviceName

getDeviceName(): string

获取远端设备名称。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 远端设备名称。最大长度为30。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let name: string = device.getDeviceName();
  console.info('name:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getDeviceClass

getDeviceClass(): DeviceClass

获取远端设备类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](nearlink-constant.md#deviceclass) | 远端设备类型。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let type: remoteDevice.DeviceClass = device.getDeviceClass();
  console.info('type:' + JSON.stringify(type));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getConnectionState

getConnectionState(): ConnectionState

获取本端设备和远端设备的连接状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionState](nearlink-constant.md#connectionstate) | 本端设备和远端设备的连接状态。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.ConnectionState = device.getConnectionState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getAcbState

getAcbState(): AcbState

获取和远端设备的逻辑链路连接状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let state: remoteDevice.AcbState = device.getAcbState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

### getDeviceInformation

getDeviceInformation(): DeviceInformation

获取远端设备的设备信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceInformation](nearlink-remote-device.md#deviceinformation) | 远端设备的设备信息。 |

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
import { remoteDevice } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
let device: remoteDevice.RemoteDevice;
try {
  device = remoteDevice.createRemoteDevice(addr);
  let deviceInfo: remoteDevice.DeviceInformation = device.getDeviceInformation();
  console.info('deviceInfo.manufacturerData:' + buffer.from(deviceInfo.manufacturerData, 'binary').toString('hex'));
  console.info('deviceInfo.modelData:' + buffer.from(deviceInfo.modelData, 'binary').toString('hex'));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## DeviceInformation

表示远端设备信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturerData | string | 否 | 否 | 厂商信息。 |
| modelData | string | 否 | 否 | 设备型号信息。 |
