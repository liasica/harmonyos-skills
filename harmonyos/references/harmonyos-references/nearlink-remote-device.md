---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-remote-device
title: remoteDevice（对端设备的连接能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > remoteDevice（对端设备的连接能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05472805b65a1a5bb46fc24774f8071f143a6ace5a44eabc2598f5e24760ed22
---

本模块提供了查询远端设备信息、发起配对等功能。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { remoteDevice } from '@kit.NearLinkKit';
```

## PairingState

PhonePC/2in1TabletTVWearable

type PairingState = [constant.PairingState](nearlink-constant.md#pairingstate)

表示和远端设备的配对状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.PairingState](nearlink-constant.md#pairingstate) | 和远端设备的配对状态。 |

## ConnectionState

PhonePC/2in1TabletTVWearable

type ConnectionState = [constant.ConnectionState](nearlink-constant.md#connectionstate)

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## DeviceClass

PhonePC/2in1TabletTVWearable

type DeviceClass = [constant.DeviceClass](nearlink-constant.md#deviceclass)

表示设备类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.DeviceClass](nearlink-constant.md#deviceclass) | 设备类型。 |

## AcbState

PhonePC/2in1TabletTVWearable

type AcbState = [constant.AcbState](nearlink-constant.md#acbstate)

表示和远端设备的逻辑链路连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

## createRemoteDevice

PhonePC/2in1TabletTVWearable

createRemoteDevice(address: string): RemoteDevice

创建远端设备实例。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | 是 | 远端设备地址。地址格式参考："11:22:33:AA:BB:FF"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RemoteDevice](nearlink-remote-device.md#remotedevice) | 远端设备实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter |
| 801 | Capability not supported |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. console.info('device: ' + JSON.stringify(device));
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## RemoteDevice

PhonePC/2in1TabletTVWearable

说明

提供远端设备的操作方法，使用前需要使用[remoteDevice.createRemoteDevice](nearlink-remote-device.md#createremotedevice)方法创建一个远端设备[RemoteDevice](nearlink-remote-device.md#remotedevice)实例。一个设备只需要创建一次，无需多次创建。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

### startPairing

PhonePC/2in1TabletTVWearable

startPairing(): Promise<void>

发起与远端设备的配对。使用Promise异步回调。发起配对后，将依据本端与远端设备的输入输出能力标识弹出不同类型的弹窗，需使用者进一步确认。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. device.startPairing().then(()=>{
9. console.info('start pairing success');
10. });
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### getPairingState

PhonePC/2in1TabletTVWearable

getPairingState(): PairingState

获取和远端设备的配对状态。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PairingState](nearlink-constant.md#pairingstate) | 和远端设备的配对状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. let state: remoteDevice.PairingState = device.getPairingState();
9. console.info('state:' + JSON.stringify(state));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getDeviceName

PhonePC/2in1TabletTVWearable

getDeviceName(): string

获取远端设备名称。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 远端设备名称。最大长度为30。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. let name: string = device.getDeviceName();
9. console.info('state:' + JSON.stringify(name));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getDeviceClass

PhonePC/2in1TabletTVWearable

getDeviceClass(): DeviceClass

获取远端设备类型。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](nearlink-constant.md#deviceclass) | 远端设备类型。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. let type: remoteDevice.DeviceClass = device.getDeviceClass();
9. console.info('type:' + JSON.stringify(type));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getConnectionState

PhonePC/2in1TabletTVWearable

getConnectionState(): ConnectionState

获取本端设备和远端设备的连接状态。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConnectionState](nearlink-constant.md#connectionstate) | 本端设备和远端设备的连接状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. let state: remoteDevice.ConnectionState = device.getConnectionState();
9. console.info('state:' + JSON.stringify(state));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getAcbState

PhonePC/2in1TabletTVWearable

getAcbState(): AcbState

获取和远端设备的逻辑链路连接状态。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { remoteDevice } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let addr: string = '00:11:22:33:AA:FF'; // 扫描获取到的远端设备地址
5. let device: remoteDevice.RemoteDevice;
6. try {
7. device = remoteDevice.createRemoteDevice(addr);
8. let state: remoteDevice.AcbState = device.getAcbState();
9. console.info('state:' + JSON.stringify(state));
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```
