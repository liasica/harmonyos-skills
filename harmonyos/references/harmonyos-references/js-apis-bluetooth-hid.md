---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-hid
title: @ohos.bluetooth.hid (蓝牙hid模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.hid (蓝牙hid模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6bc572ecb2d466dde2fd733c624183e335d30c7e5e5626c5fe39e8fed92001cf
---

本模块提供基于人机接口协议（Human Interface Device Profile，[HID](../harmonyos-guides/terminology.md#hid)）技术的蓝牙人机交互能力，支持获取连接状态等方法。

当本端设备被注册为HID设备的角色时，可以使用[HidDeviceProfile](js-apis-bluetooth-hid.md#hiddeviceprofile23)相关接口，且仅支持与传统蓝牙类型设备连接和交互。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { hid } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供订阅连接状态和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## BluetoothAddress23+

PhonePC/2in1TabletTVWearable

type BluetoothAddress = common.BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [common.BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 蓝牙设备的地址信息。 |

## hid.createHidHostProfile

PhonePC/2in1TabletTVWearable

createHidHostProfile(): HidHostProfile

创建蓝牙[HID Host](../harmonyos-guides/terminology.md#hid-host)实例。通过该实例可使用本端作为HID Host的接口，如：获取和其他设备间的蓝牙HID连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| HidHostProfile | 返回HID Host实例。  - 该类继承于[BaseProfile](js-apis-bluetooth-hid.md#baseprofile)，因此可以使用其父类中的方法。  - 和该实例角色相对应的是[HID Device](../harmonyos-guides/terminology.md#hid-device)角色。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. try {
2. let hidHostProfile = hid.createHidHostProfile();
3. console.info('hidHost success');
4. } catch (err) {
5. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
6. }
```

## hid.createHidDeviceProfile23+

PhonePC/2in1TabletTVWearable

createHidDeviceProfile(): HidDeviceProfile

创建蓝牙[HID Device](../harmonyos-guides/terminology.md#hid-device)实例。通过该实例可使用本端作为HID Device的接口，如：获取和其他设备间的蓝牙HID连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HidDeviceProfile](js-apis-bluetooth-hid.md#hiddeviceprofile23) | 返回HID Device实例。  - 该类继承于[BaseProfile](js-apis-bluetooth-hid.md#baseprofile)，因此可以使用其父类中的方法。  - 和该实例角色相对应的是[HID Host](../harmonyos-guides/terminology.md#hid-host)角色。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. try {
2. let hidDeviceProfile = hid.createHidDeviceProfile();
3. console.info('hidDevice success');
4. } catch (err) {
5. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
6. }
```

## HidDeviceProfile23+

PhonePC/2in1TabletTVWearable

该实例表示蓝牙HID通信中的[HID Device](../harmonyos-guides/terminology.md#hid-device)角色。

* 该类继承于[BaseProfile](js-apis-bluetooth-hid.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的方法前，需通过[createHidDeviceProfile](js-apis-bluetooth-hid.md#hidcreatehiddeviceprofile23)方法构造该类的实例。
* 通过该实例可以操作设备端的行为，如注册HID设备([registerHidDevice](js-apis-bluetooth-hid.md#registerhiddevice23))，发送报告([sendReport](js-apis-bluetooth-hid.md#sendreport23))等。
* 和该实例角色相对应的是[HID Host](../harmonyos-guides/terminology.md#hid-host)。

### registerHidDevice23+

PhonePC/2in1TabletTVWearable

registerHidDevice(sdp: HidDeviceSdp, inQos: HidDeviceQos, outQos: HidDeviceQos, callback: Callback<boolean>): void

应用注册HID设备能力，以便与HID主机(如电脑、手机)进行通信。使用callback异步回调。

* 当应用调用该接口并注册成功后，可以通过调用[connect](js-apis-bluetooth-hid.md#connect23)接口连接HID主机。
* 同一时间仅允许一个应用成功注册HID设备能力，同一应用重复注册将失败，注册成功后其他应用注册也将失败。
* 当应用不再需要HID设备能力时，需要主动调用[unregisterHidDevice](js-apis-bluetooth-hid.md#unregisterhiddevice23)接口解除注册HID设备能力。
* 调用该接口时，应用必须处于前台，否则无法注册成功。
* 应用注册成功之后，若切换到后台，HID设备会自动解除注册，注册状态变化将通过回调上报给上层应用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sdp | [HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23) | 是 | HID设备的服务能力记录，定义了设备类型、描述符等具体信息。 |
| inQos | [HidDeviceQos](js-apis-bluetooth-hid.md#hiddeviceqos23) | 是 | 输入通道的Qos配置，用于定义对端到本端的数据流参数。 |
| outQos | [HidDeviceQos](js-apis-bluetooth-hid.md#hiddeviceqos23) | 是 | 输出通道的Qos配置，用于定义本端到对端的数据流参数。 |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示HID设备当前为注册状态；返回false表示HID设备当前为解注册状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2903050 | Application is not in the foreground. |
| 2903051 | Any app has been registered. |

**示例：**

```
1. let descriptors: Uint8Array = new Uint8Array([
2. // 描述符示例，需要遵循USB HID规范
3. 0x05, 0x01,        // 指定设备类别为通用桌面控制
4. 0x09, 0x06,        // 具体设备为键盘
5. 0xA1, 0x01,        // 应用集合开始

7. // 按键字段定义
8. 0x05, 0x07,        // 切换到键盘/键区
9. 0x19, 0x00,        // 定义最小按键码为0（无按键）
10. 0x29, 0x01,        // 定义最大按键码为1（只支持2个值）
11. 0x15, 0x00,        // 逻辑最小值0（数据范围下限）
12. 0x25, 0x01,        // 逻辑最大值1（数据范围上限）
13. 0x75, 0x08,        // 每个字段八位
14. 0x95, 0x01,        // 只有一个字段
15. 0x81, 0x00,        // 定义输入字段：数据字段，值为按键数组

17. // 结束设备定义
18. 0xC0               // 应用集合结束
19. ]);
20. // 以键盘为例
21. let sdp: hid.HidDeviceSdp = {
22. "name": "testName",
23. "description": "testDescription",
24. "provider": "testProvider",
25. "subclass": hid.Subclass.SUBCLASS_KEYBOARD,
26. "descriptors": descriptors,
27. };
28. let inqos: hid.HidDeviceQos = {
29. "serviceType": hid.ServiceType.SERVICE_BEST_EFFORT,
30. "tokenRate": 0,
31. "tokenBucketSize": 0,
32. "peakBandwidth": 0,
33. "latency": -1,
34. "delayVariation": -1,
35. };
36. let outqos: hid.HidDeviceQos = {};
37. function registerStateCallback(callback: boolean) {
38. console.info(`state: ${callback}`);
39. }

41. try {
42. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
43. hidDevice.registerHidDevice(sdp, inqos, outqos, registerStateCallback)
44. } catch (err) {
45. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
46. }
```

### unregisterHidDevice23+

PhonePC/2in1TabletTVWearable

unregisterHidDevice(): void

解除注册本端作为HID设备的能力，并释放所有相关资源。

* 若调用该接口前，本端已通过调用[connect](js-apis-bluetooth-hid.md#connect23)建立与HID主机的连接，调用后本端与HID主机的连接会被断开。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. try {
2. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
3. hidDevice.unregisterHidDevice();
4. } catch (err) {
5. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
6. }
```

### connect23+

PhonePC/2in1TabletTVWearable

connect(deviceId: BluetoothAddress): void

向指定的HID主机发起连接。

* 调用该接口前需要先调用[registerHidDevice](js-apis-bluetooth-hid.md#registerhiddevice23)完成HID设备能力注册。
* 可通过订阅[on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)事件来感知连接是否成功。
* 当不需要连接时需调用[disconnect](js-apis-bluetooth-hid.md#disconnect23)断开连接。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | [BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 是 | 需要连接的对端蓝牙设备地址信息，HID设备中不涉及rawAddressType，无需给定该参数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Remote Device profile not supported. |
| 2900099 | Operation failed. |
| 2903052 | App not register. |

**示例：**

```
1. import { common } from '@kit.ConnectivityKit';

3. let device: common.BluetoothAddress = {
4. "address": "11:22:33:44:55:66",
5. "addressType": common.BluetoothAddressType.REAL,
6. }
7. try {
8. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
9. hidDevice.connect(device);
10. } catch (err) {
11. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
12. }
```

### disconnect23+

PhonePC/2in1TabletTVWearable

disconnect(): void

断开与当前HID主机的连接，并释放相关的资源。

* 调用成功后不影响当前HID设备的注册状态，应用仍处于已注册状态，可以再次调用[connect](js-apis-bluetooth-hid.md#connect23)连接新的HID主机。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2903052 | App not register. |

**示例：**

```
1. try {
2. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
3. hidDevice.disconnect();
4. } catch (err) {
5. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
6. }
```

### sendReport23+

PhonePC/2in1TabletTVWearable

sendReport(id: number, reportData: Uint8Array): void

向已连接的HID主机发送报告数据。

* 调用该接口前必须已调用[registerHidDevice](js-apis-bluetooth-hid.md#registerhiddevice23)完成注册，并通过[connect](js-apis-bluetooth-hid.md#connect23)建立与HID主机的连接。
* 报告数据的长度和内容必须与HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)所定义的规范保持一致，否则HID主机将无法正确解析。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 对应HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中定义的报告ID，用于标识报告类型，对于不带ID的简单设备，此参数应设置为0。对于定义了多个报告ID的设备，此处应传入对应的ID值，该ID值必须与描述符中定义的值保持一致。 |
| reportData | Uint8Array | 是 | 报告数据。其内容长度和解析方式必须严格匹配描述符中为该报告ID定义的格式。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2903052 | App not register. |
| 2903053 | Device not connected. |

**示例：**

```
1. let reportData: Uint8Array = new Uint8Array([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77]);
2. let id: number = 0;
3. try {
4. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
5. hidDevice.sendReport(id, reportData);
6. } catch (err) {
7. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
8. }
```

### replyReport23+

PhonePC/2in1TabletTVWearable

replyReport(type: ReportType, id: number, reportData: Uint8Array): void

回复已连接HID主机的特定请求。

* 调用该接口前必须已调用[registerHidDevice](js-apis-bluetooth-hid.md#registerhiddevice23)完成注册，并通过[connect](js-apis-bluetooth-hid.md#connect23)建立与HID主机的连接。
* 通过订阅[onGetReport](js-apis-bluetooth-hid.md#ongetreport23)应用可以接收主机的请求。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ReportType](js-apis-bluetooth-hid.md#reporttype23) | 是 | 回复的报告类型。 |
| id | number | 是 | 对应HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中定义的报告ID，用于标识报告类型，对于不带ID的简单设备，此参数应设置为0。对于定义了多个报告ID的设备，此处应传入对应的ID值，该ID值必须与描述符中定义的值保持一致。 |
| reportData | Uint8Array | 是 | 报告数据。其内容长度和解析方式必须严格匹配描述符中为该报告ID定义的格式。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2903052 | App not register. |
| 2903053 | Device not connected. |

**示例：**

```
1. let type = hid.ReportType.REPORT_TYPE_INPUT;
2. let id: number = 0;
3. let reportData: Uint8Array = new Uint8Array([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77]);
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.replyReport(type, id, reportData);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### reportError23+

PhonePC/2in1TabletTVWearable

reportError(error: ErrorReason): void

向已连接的HID主机报告特定的错误类型。

* 调用该接口前必须已调用[registerHidDevice](js-apis-bluetooth-hid.md#registerhiddevice23)完成注册，并通过[connect](js-apis-bluetooth-hid.md#connect23)建立与HID主机的连接。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [ErrorReason](js-apis-bluetooth-hid.md#errorreason23) | 是 | 表示要报告给HID主机的具体错误类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2903052 | App not register. |
| 2903053 | Device not connected. |

**示例：**

```
1. let error = hid.ErrorReason.RSP_SUCCESS;
2. try {
3. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
4. hidDevice.reportError(error);
5. } catch (err) {
6. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
7. }
```

### onGetReport23+

PhonePC/2in1TabletTVWearable

onGetReport(callback: Callback<GetReportData>): void

订阅HID主机向HID设备发送的[GET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件，使用callback异步回调。收到回调后可以通过调用接口[replyReport](js-apis-bluetooth-hid.md#replyreport23)进行回复。当收到的数据不符合预期时，可以通过调用接口[reportError](js-apis-bluetooth-hid.md#reporterror23)进行回复。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[GetReportData](js-apis-bluetooth-hid.md#getreportdata23)> | 是 | 回调函数，返回收到的报告数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.GetReportData) {
2. console.info(`type: ${callback.type}, id: ${callback.id}, bufferSize: ${callback.bufferSize}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onGetReport(onReceiveEvent);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offGetReport23+

PhonePC/2in1TabletTVWearable

offGetReport(callback?: Callback<GetReportData>): void

取消订阅主机向HID设备发出的[GET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[GetReportData](js-apis-bluetooth-hid.md#getreportdata23)> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[onGetReport](js-apis-bluetooth-hid.md#ongetreport23)中的回调函数一致；若无传参，则取消订阅所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.GetReportData) {
2. console.info(`type: ${callback.type}, id: ${callback.id}, bufferSize: ${callback.bufferSize}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onGetReport(onReceiveEvent);
7. hidDevice.offGetReport(onReceiveEvent);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

### onSetReport23+

PhonePC/2in1TabletTVWearable

onSetReport(callback: Callback<SetReportData>): void

订阅HID主机向HID设备发送的[SET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件，使用callback异步回调。当收到的数据不符合预期时，可以通过调用接口[reportError](js-apis-bluetooth-hid.md#reporterror23)进行回复。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SetReportData](js-apis-bluetooth-hid.md#setreportdata23)> | 是 | 回调函数，返回收到的报告数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.SetReportData) {
2. console.info(`type: ${callback.type}, id: ${callback.id}, dataSize: ${callback.data.length}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onSetReport(onReceiveEvent);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offSetReport23+

PhonePC/2in1TabletTVWearable

offSetReport(callback?: Callback<SetReportData>): void

取消订阅主机向HID设备发出的[SET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SetReportData](js-apis-bluetooth-hid.md#setreportdata23)> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[onSetReport](js-apis-bluetooth-hid.md#onsetreport23)中的回调函数一致；若无传参，则取消订阅所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.SetReportData) {
2. console.info(`type: ${callback.type}, id: ${callback.id}, dataSize: ${callback.data.length}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onSetReport(onReceiveEvent);
7. hidDevice.offSetReport(onReceiveEvent);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

### onInterruptDataReceived23+

PhonePC/2in1TabletTVWearable

onInterruptDataReceived(callback: Callback<InterruptData>): void

订阅HID主机通过中断传输通道发送数据的事件的回调，使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InterruptData](js-apis-bluetooth-hid.md#interruptdata23)> | 是 | 回调函数，返回收到的中断数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.InterruptData) {
2. console.info(`id: ${callback.id}, dataSize: ${callback.data.length}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onInterruptDataReceived(onReceiveEvent);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offInterruptDataReceived23+

PhonePC/2in1TabletTVWearable

offInterruptDataReceived(callback?: Callback<InterruptData>): void

取消订阅主机通过中断传输通道发送数据事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[InterruptData](js-apis-bluetooth-hid.md#interruptdata23)> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[onInterruptDataReceived](js-apis-bluetooth-hid.md#oninterruptdatareceived23)中的回调函数一致；若无传参，则取消订阅所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.InterruptData) {
2. console.info(`id: ${callback.id}, dataSize: ${callback.data.length}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onInterruptDataReceived(onReceiveEvent);
7. hidDevice.offInterruptDataReceived(onReceiveEvent);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

### onSetProtocol23+

PhonePC/2in1TabletTVWearable

onSetProtocol(callback: Callback<ProtocolData>): void

订阅HID主机向HID设备发送的[SET\_PROTOCOL](../harmonyos-guides/terminology.md#hid)请求事件，使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ProtocolData](js-apis-bluetooth-hid.md#protocoldata23)> | 是 | 回调函数。返回收到的协议数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.ProtocolData) {
2. console.info(`protocol: ${callback.protocol}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onSetProtocol(onReceiveEvent);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offSetProtocol23+

PhonePC/2in1TabletTVWearable

offSetProtocol(callback?: Callback<ProtocolData>): void

取消订阅主机向HID设备发送的[SET\_PROTOCOL](../harmonyos-guides/terminology.md#hid)请求事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ProtocolData](js-apis-bluetooth-hid.md#protocoldata23)> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[onSetProtocol](js-apis-bluetooth-hid.md#onsetprotocol23)中的回调函数一致；若无传参，则取消订阅所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent(callback: hid.ProtocolData) {
2. console.info(`protocol: ${callback.protocol}`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onSetProtocol(onReceiveEvent);
7. hidDevice.offSetProtocol(onReceiveEvent);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

### onVirtualCableUnplug23+

PhonePC/2in1TabletTVWearable

onVirtualCableUnplug(callback: Callback<void>): void

订阅主机断开HID虚拟链路事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数。当主机断开虚拟链路时返回。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent() {
2. console.info(`onVirtualCableUnplug`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onVirtualCableUnplug(onReceiveEvent);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offVirtualCableUnplug23+

PhonePC/2in1TabletTVWearable

offVirtualCableUnplug(callback?: Callback<void>): void

取消订阅主机断开HID虚拟链路事件的回调。使用callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[onVirtualCableUnplug](js-apis-bluetooth-hid.md#onvirtualcableunplug23)中的回调函数一致；若无传参，则取消订阅所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function onReceiveEvent() {
2. console.info(`onVirtualCableUnplug`);
3. }
4. try {
5. let hidDevice: hid.HidDeviceProfile = hid.createHidDeviceProfile();
6. hidDevice.onVirtualCableUnplug(onReceiveEvent);
7. hidDevice.offVirtualCableUnplug(onReceiveEvent);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

## HidDeviceSdp23+

PhonePC/2in1TabletTVWearable

描述HID设备在服务发现协议([SDP](../harmonyos-guides/terminology.md#sdp))中的服务注册配置。该结构定义了HID设备的身份标识、能力描述和协议特征，是HID主机发现、识别和连接HID设备的关键参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | HID设备的名称，要求长度范围：[1, 50]，单位：Byte。 |
| description | string | 否 | 否 | HID设备的描述信息，要求长度范围：[1, 50]，单位：Byte。 |
| provider | string | 否 | 否 | 描述HID设备的制造商信息，要求长度范围：[1, 50]，单位：Byte。 |
| subclass | [Subclass](js-apis-bluetooth-hid.md#subclass23) | 否 | 否 | 表示HID设备具体类型。 |
| descriptors | Uint8Array | 否 | 否 | 标识与蓝牙HID设备功能定义描述符。描述符会为每个支持的报告分配一个唯一的ID， 并详细定义该ID下报告的长度、结构与各字段含义。填写时需要遵循[USB HID](https://www.usb.org/hid)规范。 |

## HidDeviceQos23+

PhonePC/2in1TabletTVWearable

描述HID设备服务质量(Qos)参数。该结构定义了HID数据传输通道的流量控制、延迟保证和可靠性策略，用于优化蓝牙传输性能，确保设备的实时响应性。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceType | [ServiceType](js-apis-bluetooth-hid.md#servicetype23) | 否 | 是 | 服务类型，默认为SERVICE\_BEST\_EFFORT。 |
| tokenRate | number | 否 | 是 | 单位时间内允许传输的平均数据量，单位为Byte/s，默认为0，表示没有平均数据量限制。 |
| tokenBucketSize | number | 否 | 是 | 允许短时间内超过tokenRate的最大数据量，默认为0，表示没有最大数据量限制。 |
| peakBandwidth | number | 否 | 是 | 最大传输速率限制，单位为Byte/s，默认为0，表示没有传输速率限制。 |
| latency | number | 否 | 是 | 最大允许延迟时间，单位为μs，默认为-1，表示没有延迟限制。 |
| delayVariation | number | 否 | 是 | 允许的延迟波动范围，单位为μs，默认为-1，表示没有延迟波动范围限制。 |

## GetReportData23+

PhonePC/2in1TabletTVWearable

描述HID主机向HID设备发送的[GET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件的信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ReportType](js-apis-bluetooth-hid.md#reporttype23) | 否 | 否 | 报告类型。 |
| id | number | 否 | 否 | 对应HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中定义的报告ID，用于标识报告类型，对于不带ID的简单设备，此参数应设置为0。对于定义了多个报告ID的设备，此处应传入对应的ID值，该ID值必须与描述符中定义的值保持一致。 |
| bufferSize | number | 否 | 否 | 收到数据的长度，单位为Byte。 |

## SetReportData23+

PhonePC/2in1TabletTVWearable

描述HID主机向HID设备发送的[SET\_REPORT](../harmonyos-guides/terminology.md#hid)传输请求事件的信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ReportType](js-apis-bluetooth-hid.md#reporttype23) | 否 | 否 | 报告类型。 |
| id | number | 否 | 否 | 对应HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中定义的报告ID，用于标识报告类型，对于不带ID的简单设备，此参数应设置为0。对于定义了多个报告ID的设备，此处应传入对应的ID值，该ID值必须与描述符中定义的值保持一致。 |
| data | Uint8Array | 否 | 否 | 配置数据。其内容长度和解析方式必须严格匹配描述符中为该报告ID定义的格式。 |

## InterruptData23+

PhonePC/2in1TabletTVWearable

描述从主机收到的中断数据。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 对应HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中定义的报告ID，用于标识报告类型，对于不带ID的简单设备，此参数应设置为0。对于定义了多个报告ID的设备，此处应传入对应的ID值，该ID值必须与描述符中定义的值保持一致。 |
| data | Uint8Array | 否 | 否 | 中断数据。其内容长度和解析方式必须严格匹配HID设备注册时通过[HidDeviceSdp](js-apis-bluetooth-hid.md#hiddevicesdp23)提供的描述符中为该报告ID定义的格式。 |

## ProtocolData23+

PhonePC/2in1TabletTVWearable

描述从HID主机接收的通信协议数据。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| protocol | [ProtocolType](js-apis-bluetooth-hid.md#protocoltype23) | 否 | 否 | 主机的不同通信协议类型。 |

## Subclass23+

PhonePC/2in1TabletTVWearable

枚举，HID设备的具体类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBCLASS\_UNCATEGORIZED | 0 | 未分类HID设备。 |
| SUBCLASS\_JOYSTICK | 1 | 摇杆设备。 |
| SUBCLASS\_GAMEPAD | 2 | 游戏手柄设备。 |
| SUBCLASS\_REMOTE\_CONTROL | 3 | 遥控器设备。 |
| SUBCLASS\_SENSING\_DEVICE | 4 | 传感设备。 |
| SUBCLASS\_DIGITIZER\_TABLET | 5 | 数位板设备。 |
| SUBCLASS\_CARD\_READER | 6 | 读卡器设备。 |
| SUBCLASS\_KEYBOARD | 64 | 标准键盘设备。 |
| SUBCLASS\_MOUSE | 128 | 标准鼠标设备。 |
| SUBCLASS\_COMBO | 192 | 组合输入设备。 |

## ReportType23+

PhonePC/2in1TabletTVWearable

枚举，报告类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REPORT\_TYPE\_INPUT | 1 | 输入报告，表示由本端向HID主机发送的数据。 |
| REPORT\_TYPE\_OUTPUT | 2 | 输出报告，表示HID这几向本端发送的数据。 |
| REPORT\_TYPE\_FEATURE | 3 | 特征报告，表示双向传输的配置数据。 |

## ServiceType23+

PhonePC/2in1TabletTVWearable

枚举，描述HID设备与主机之间连接的服务类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SERVICE\_NO\_TRAFFIC | 0 | 低功耗模式，仅维持连接，不传输应用数据，功耗最低。 |
| SERVICE\_BEST\_EFFORT | 1 | 高速模式，传输速率最快，但是数据包可能丢失或乱序，适用于对延迟敏感但对丢包不敏感的场景。 |
| SERVICE\_GUARANTEED | 2 | 可靠模式，传输速度稍慢，但是保证数据正确送达，适用于文件传输等场景。 |

## ErrorReason23+

PhonePC/2in1TabletTVWearable

枚举，描述错误原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RSP\_SUCCESS | 0 | 成功无异常。 |
| RSP\_NOT\_READY | 1 | 设备未准备好处理请求。建议主机稍后重试。 |
| RSP\_INVALID\_REPORT\_ID | 2 | 无效的报告ID。建议主机确认当前支持的ID列表，并使用正确的ID重发消息。 |
| RSP\_UNSUPPORTED\_REQ | 3 | 当前请求不支持，建议主机检查当前请求类型或报告类型是否在当前协议模式下被本端支持。 |
| RSP\_INVALID\_PARAM | 4 | 无效参数。建议主机检查请求中的参数是否超出本端声明的范围或不符合报告描述符的定义。 |
| RSP\_UNKNOWN | 14 | 未知错误原因。建议主机记录错误上下文并重试。 |

## ProtocolType23+

PhonePC/2in1TabletTVWearable

枚举，HID设备与主机的通信协议类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROTOCOL\_BOOT\_MODE | 0 | 兼容模式，确保设备在系统启动阶段和所有平台都能被识别为基本输入设备，兼容性最好但功能有限，适用于如键盘鼠标简单外设开发。 |
| PROTOCOL\_REPORT\_MODE | 1 | 完整的报告协议模式，允许设备使用完整的HID描述符和所有报告类型，适用于如游戏手柄、触摸屏等需要丰富功能与自定义数据格式的复杂外设。 |
