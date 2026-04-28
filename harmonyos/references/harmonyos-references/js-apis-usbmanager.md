---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usbmanager
title: @ohos.usbManager (USB管理)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 设备管理 > @ohos.usbManager (USB管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:30+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:42408ee703ca427fe3588905a5d948e4129bb7ac83572f02ef7050331ae89e3c
---

本模块主要提供管理USB设备的相关功能，包括主设备上查询USB设备列表、批量数据传输、控制命令传输、权限控制等；从设备上端口管理、功能切换及查询等。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { usbManager } from '@kit.BasicServicesKit';
```

## 使用说明

PhonePC/2in1TabletTV

凡是参数类型为[USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe)的接口,都需要执行如下操作：

**在使用接口前：**

1. 调用[usbManager.getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备列表。
2. 调用[usbManager.requestRight](js-apis-usbmanager.md#usbmanagerrequestright)获取请求权限。
3. 调用[usbManager.connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)得到USBDevicePipe作为参数。

**在使用接口后：**

调用[usbManager.closePipe](js-apis-usbmanager.md#usbmanagerclosepipe)关闭设备消息控制通道。

## usbManager.getDevices

PhonePC/2in1TabletTV

getDevices(): Array<Readonly<USBDevice>>

获取接入主设备的USB设备列表。

说明

三方应用没有权限获取serial字段读取设备序列号，需要通过[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)申请权限后，自行发起控制传输获取。

**系统能力：** SystemCapability.USB.USBManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Readonly<[USBDevice](js-apis-usbmanager.md#usbdevice)>> | 设备信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
2. console.info(`devicesList = ${devicesList}`);
3. /*
4. devicesList 返回的数据结构,此处提供一个简单的示例，如下
5. [
6. {
7. name: "1-1",
8. serial: "",
9. manufacturerName: "",
10. productName: "",
11. version: "",
12. vendorId: 7531,
13. productId: 2,
14. clazz: 9,
15. subClass: 0,
16. protocol: 1,
17. devAddress: 1,
18. busNum: 1,
19. configs: [
20. {
21. id: 1,
22. attributes: 224,
23. isRemoteWakeup: true,
24. isSelfPowered: true,
25. maxPower: 0,
26. name: "1-1",
27. interfaces: [
28. {
29. id: 0,
30. protocol: 0,
31. clazz: 9,
32. subClass: 0,
33. alternateSetting: 0,
34. name: "1-1",
35. endpoints: [
36. {
37. address: 129,
38. attributes: 3,
39. interval: 12,
40. maxPacketSize: 4,
41. direction: 128,
42. number: 1,
43. type: 3,
44. interfaceId: 0,
45. },
46. ],
47. },
48. ],
49. },
50. ],
51. },
52. ]
53. */
```

## usbManager.connectDevice

PhonePC/2in1TabletTV

connectDevice(device: USBDevice): Readonly<USBDevicePipe>

根据getDevices()返回的设备信息打开USB设备。如果USB服务异常，可能返回undefined，注意需要对接口返回值做判空处理。

1. 需要调用[usbManager.getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息以及device;
2. 调用[usbManager.requestRight](js-apis-usbmanager.md#usbmanagerrequestright)请求使用该设备的权限。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | [USBDevice](js-apis-usbmanager.md#usbdevice) | 是 | USB设备信息，用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取的busNum和devAddress确定设备，当前其它属性不做处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Readonly<[USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe)> | 指定的传输通道对象。 |

**错误码：**

以下错误码的详细介绍参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400001 | Access right denied. Call requestRight to get the USBDevicePipe access right first. |

**示例：**

```
1. function connectDevice() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
11. console.info(`devicepipe = ${devicepipe}`);
12. }
```

## usbManager.hasRight

PhonePC/2in1TabletTV

hasRight(deviceName: string): boolean

判断是否有权访问该设备。

如果“使用者”（如各种App或系统）有权访问设备则返回true；无权访问设备则返回false。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceName | string | 是 | 来自[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取的设备列表USBDevice里的name。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示有访问设备的权限，false表示没有访问设备的权限。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function hasRight(): boolean {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return false;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let right: boolean = usbManager.hasRight(device.name);
11. console.info(`${right}`);
12. return right;
13. }
```

## usbManager.requestRight

PhonePC/2in1TabletTV

requestRight(deviceName: string): Promise<boolean>

请求软件包的临时权限以访问设备。使用Promise异步回调。系统应用默认拥有访问设备权限，无需调用此接口申请。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceName | string | 是 | 设备名称，来自[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取的设备列表USBDevice里的name。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回临时权限的申请结果。返回true表示临时权限申请成功；返回false则表示临时权限申请失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function requestRight() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name).then(ret => {
10. console.info(`requestRight = ${ret}`);
11. }).catch((error: BusinessError) => {
12. console.error(`requestRight failed : ${error}`);
13. });
14. }
```

## usbManager.removeRight

PhonePC/2in1TabletTV

removeRight(deviceName: string): boolean

移除软件包访问设备的权限。系统应用默认拥有访问设备权限，调用此接口不会产生影响。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceName | string | 是 | 来自[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取的设备列表USBDevice里的name。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回权限移除结果。返回true表示权限移除成功；返回false则表示权限移除失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function removeRight(): boolean {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return false;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. if (usbManager.removeRight(device.name)) {
10. console.info(`Succeed in removing right`);
11. return true;
12. }
13. return false;
14. }
```

## usbManager.claimInterface

PhonePC/2in1TabletTV

claimInterface(pipe: USBDevicePipe, iface: USBInterface, force ?: boolean): number

声明对USB设备某个接口的控制权。

说明

在USB编程中，claim interface是一个常见操作，指的是应用程序请求操作系统将某个USB接口从内核驱动中释放并交由用户空间程序控制。

下面用到的claim通信接口都表示claim interface操作。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| iface | [USBInterface](js-apis-usbmanager.md#usbinterface) | 是 | 用于确定需要获取接口的索引，需要调用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息并通过id确定唯一接口。 |
| force | boolean | 否 | 可选参数，是否强制获取。默认值为false ，表示不强制获取，用户按需选择。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | claim通信接口成功返回0；claim通信接口失败返回其它错误码如下：  - 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。  - 88080486：服务初始化中，请稍后重试。  - 88080488：无设备访问权限，请先调用[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)接口申请授权。  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function claimInterface() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
11. let interfaces: usbManager.USBInterface = device.configs?.[0]?.interfaces?.[0];
12. let ret: number= usbManager.claimInterface(devicepipe, interfaces);
13. console.info(`claimInterface = ${ret}`);
14. }
```

## usbManager.releaseInterface

PhonePC/2in1TabletTV

releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number

释放claim过的通信接口。

说明

在调用该接口前需要通过[usbManager.claimInterface](js-apis-usbmanager.md#usbmanagerclaiminterface) claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| iface | [USBInterface](js-apis-usbmanager.md#usbinterface) | 是 | 用于确定需要释放接口的索引，需要调用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息并通过id确定唯一接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 释放接口成功返回0；释放接口失败返回其它错误码如下：  - 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。  - 88080486：服务初始化中，请稍后重试。  - 88080488：无设备访问权限，请先调用[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)接口申请授权。  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function releaseInterface() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
11. let interfaces: usbManager.USBInterface = device.configs?.[0]?.interfaces?.[0];
12. let ret: number = usbManager.claimInterface(devicepipe, interfaces);
13. ret = usbManager.releaseInterface(devicepipe, interfaces);
14. console.info(`releaseInterface = ${ret}`);
15. }
```

## usbManager.setConfiguration

PhonePC/2in1TabletTV

setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number

设置设备配置。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| config | [USBConfiguration](js-apis-usbmanager.md#usbconfiguration) | 是 | 用于确定需要设置的配置，需要调用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息并通过id用于确定唯一设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 设置设备配置成功返回0；设置设备配置失败返回其它错误码如下：  - 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。  - 88080486：服务初始化中，请稍后重试。  - 88080488：无设备访问权限，请先调用[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)接口申请授权。  - -1：驱动异常。  - -17：I/O失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function setConfiguration() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
11. let config: usbManager.USBConfiguration = device.configs?.[0];
12. let ret: number= usbManager.setConfiguration(devicepipe, config);
13. console.info(`setConfiguration = ${ret}`);
14. }
```

## usbManager.setInterface

PhonePC/2in1TabletTV

setInterface(pipe: USBDevicePipe, iface: USBInterface): number

设置设备接口。

说明

一个USB接口可能存在多重选择模式，支持动态切换。使用的场景：数据传输时，通过该接口可重新设置端点，使端点与传输类型匹配。

在调用该接口前需要通过[usbManager.claimInterface](js-apis-usbmanager.md#usbmanagerclaiminterface) claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| iface | [USBInterface](js-apis-usbmanager.md#usbinterface) | 是 | 用于确定需要设置的接口，需要调用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息并通过id和alternateSetting确定唯一接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 设置设备接口成功返回0；设置设备接口失败返回其它错误码如下：  - 88080389：服务未启动，可能原因：1.无设备插入；2.服务异常退出。  - 88080486：服务初始化中，请稍后重试。  - 88080488：无设备访问权限，请先调用[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)接口申请授权。  - -1：驱动异常 。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function setInterface() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. let device: usbManager.USBDevice = devicesList?.[0];
9. usbManager.requestRight(device.name);
10. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
11. let interfaces: usbManager.USBInterface = device.configs?.[0]?.interfaces?.[0];
12. let ret: number = usbManager.claimInterface(devicepipe, interfaces);
13. ret = usbManager.setInterface(devicepipe, interfaces);
14. console.info(`setInterface = ${ret}`);
15. }
```

## usbManager.getRawDescriptor

PhonePC/2in1TabletTV

getRawDescriptor(pipe: USBDevicePipe): Uint8Array

获取原始的USB描述符。如果USB服务异常，可能返回undefined，注意需要对接口返回值做判空处理。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回获取的原始数据；失败返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function getRawDescriptor() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. usbManager.requestRight(devicesList?.[0]?.name);
9. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
10. let ret: Uint8Array = usbManager.getRawDescriptor(devicepipe);
11. }
```

## usbManager.getFileDescriptor

PhonePC/2in1TabletTV

getFileDescriptor(pipe: USBDevicePipe): number

获取文件描述符。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回设备对应的文件描述符，失败返回其它错误码如下：  - 88080486：服务初始化中，请稍后重试。  - 88080488：无设备访问权限，请先调用[requestRight](js-apis-usbmanager.md#usbmanagerrequestright)接口申请授权。  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function getFileDescriptor() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. usbManager.requestRight(devicesList?.[0]?.name);
9. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
10. let ret: number = usbManager.getFileDescriptor(devicepipe);
11. console.info(`getFileDescriptor = ${ret}`);
12. let closeRet: number = usbManager.closePipe(devicepipe);
13. console.info(`closePipe = ${closeRet}`);
14. }
```

## usbManager.usbControlTransfer12+

PhonePC/2in1TabletTV

usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout ?: number): Promise<number>

控制传输。使用Promise异步回调。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定设备，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| requestparam | [USBDeviceRequestParams](js-apis-usbmanager.md#usbdevicerequestparams12) | 是 | 控制传输参数，按需设置参数，参数传参类型请参考USB协议。 |
| timeout | number | 否 | 超时时间（单位：ms），可选参数，指定时间内等待控制传输完成，若在指定时间内传输完成则正常返回，否则返回超时；默认为0时无限等待直到传输完成。用户按需选择。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，获取传输或接收到的数据块大小。失败返回其它错误码如下：  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. class PARA {
2. bmRequestType: number = 0
3. bRequest: number = 0
4. wValue: number = 0
5. wIndex: number = 0
6. wLength: number = 0
7. data: Uint8Array = new Uint8Array()
8. }

10. let param: PARA = {
11. bmRequestType: 0x80,
12. bRequest: 0x06,

14. wValue:0x01 << 8 | 0,
15. wIndex: 0,
16. wLength: 18,
17. data: new Uint8Array(18)
18. };

20. function usbControlTransfer() {
21. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
22. if (!devicesList || devicesList.length == 0) {
23. console.info(`device list is empty`);
24. return;
25. }

27. usbManager.requestRight(devicesList?.[0]?.name);
28. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
29. usbManager.usbControlTransfer(devicepipe, param).then((ret: number) => {
30. console.info(`usbControlTransfer = ${ret}`);
31. })
32. }
```

## usbManager.bulkTransfer

PhonePC/2in1TabletTV

bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout ?: number): Promise<number>

批量传输。使用Promise异步回调。

说明

单次批量传输的传输数据总量（包括pipe、endpoint、buffer、timeout）请控制在200KB以下，数据总量过大会导致传输失败返回-1。

在调用接口前需要通过[usbManager.claimInterface](js-apis-usbmanager.md#usbmanagerclaiminterface) claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定设备，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| endpoint | [USBEndpoint](js-apis-usbmanager.md#usbendpoint) | 是 | 用于确定传输的端口，需要调用[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备信息列表以及endpoint，address用于确定端点地址，direction用于确定端点的方向，interfaceId用于确定所属接口，当前其它属性不做处理。 |
| buffer | Uint8Array | 是 | 用于写入或读取数据的缓冲区。 |
| timeout | number | 否 | 超时时间（单位：ms），可选参数，指定时间内等待批量传输完成，若在指定时间内传输完成则正常返回，否则返回超时；默认为0时无限等待直到传输完成。用户按需选择。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，获取传输或接收到的数据块大小。失败返回其它错误码如下：  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

说明

以下示例代码只是调用bulkTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```
1. // usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
2. // 把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
3. // 才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
4. function bulkTransfer() {
5. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
6. if (!devicesList || devicesList.length == 0) {
7. console.info(`device list is empty`);
8. return;
9. }

11. let device: usbManager.USBDevice = devicesList?.[0];
12. usbManager.requestRight(device.name);
13. if (!usbManager.hasRight(device.name)) {
14. console.error(`request right fail`);
15. return;
16. }
17. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
18. for (let i = 0; i < device.configs?.[0]?.interfaces.length; i++) {
19. if (device.configs?.[0]?.interfaces?.[i]?.endpoints?.[0]?.attributes == 2) {
20. let endpoint: usbManager.USBEndpoint = device.configs?.[0]?.interfaces?.[i]?.endpoints?.[0];
21. let interfaces: usbManager.USBInterface = device.configs?.[0]?.interfaces?.[i];
22. let ret: number = usbManager.claimInterface(devicepipe, interfaces);
23. let buffer =  new Uint8Array(128);
24. usbManager.bulkTransfer(devicepipe, endpoint, buffer).then((ret: number) => {
25. console.info(`bulkTransfer = ${ret}`);
26. }).catch((error: BusinessError) => {
27. console.error(`bulkTransfer failed : ${error}`);
28. });
29. }
30. }
31. }
```

## usbManager.usbSubmitTransfer18+

PhonePC/2in1TabletTV

usbSubmitTransfer(transfer: UsbDataTransferParams): void

提交异步传输请求。

说明

本接口为异步接口，调用后立刻返回，实际读写操作的结果以回调的方式返回。

在调用该接口前需要通过[usbManager.claimInterface](js-apis-usbmanager.md#usbmanagerclaiminterface) claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transfer | [UsbDataTransferParams](js-apis-usbmanager.md#usbdatatransferparams18) | 是 | 作为通用USB数据传输接口，客户端需要填充这个对象中的参数，用以发起传输请求。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14400001 | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| 14400007 | Resource busy. Possible causes: 1. The transfer has already been submitted. 2. The interface is claimed by another program or driver. |
| 14400008 | No such device (it may have been disconnected). |
| 14400009 | Insufficient memory. Possible causes: 1. Memory allocation failed. |
| 14400012 | Transmission I/O error. |

**示例：**

说明

以下示例代码需要放入具体的方法中执行，只是调用usbSubmitTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```
1. // usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
2. // 把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
3. // 才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
4. function usbSubmitTransfer() {
5. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
6. if (!devicesList || devicesList.length == 0) {
7. console.info(`device list is empty`);
8. return;
9. }
10. let device: usbManager.USBDevice = devicesList?.[0];
11. usbManager.requestRight(device.name);
12. if (!usbManager.hasRight(device.name)) {
13. console.info(`request right fail`);
14. return;
15. }
16. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
17. // 获取endpoint端点地址。
18. let endpoint = device.configs?.[0]?.interfaces?.[0]?.endpoints.find((value) => {
19. return value.direction === 0 && value.type === 2
20. })
21. // 获取设备的第一个id。
22. let ret: number = usbManager.claimInterface(devicepipe, device.configs?.[0]?.interfaces?.[0], true);

24. let transferParams: usbManager.UsbDataTransferParams = {
25. devPipe: devicepipe,
26. flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
27. endpoint: 1,
28. type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_BULK,
29. timeout: 2000,
30. length: 10,
31. callback: () => {},
32. userData: new Uint8Array(10),
33. buffer: new Uint8Array(10),
34. isoPacketCount: 0,
35. };
36. try {
37. transferParams.endpoint=endpoint?.address as number;
38. transferParams.callback=(err, callBackData: usbManager.SubmitTransferCallback)=>{
39. console.info('callBackData =' +JSON.stringify(callBackData));
40. }
41. usbManager.usbSubmitTransfer(transferParams);
42. console.info('USB transfer request submitted.');
43. } catch (error) {
44. console.error('USB transfer failed:', error);
45. }
46. }
```

## usbManager.usbCancelTransfer18+

PhonePC/2in1TabletTV

usbCancelTransfer(transfer: UsbDataTransferParams): void

取消异步传输请求。

说明

该接口的主要作用是主动取消尚未完成的USB数据传输请求（如usbSubmitTransfer提交的传输）。

在调用该接口前需要通过[usbManager.claimInterface](js-apis-usbmanager.md#usbmanagerclaiminterface) claim通信接口。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transfer | [UsbDataTransferParams](js-apis-usbmanager.md#usbdatatransferparams18) | 是 | 在取消传输的接口中，该参数同[usbManager.usbSubmitTransfer](js-apis-usbmanager.md#usbmanagerusbsubmittransfer18)接口的入参对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14400001 | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| 14400008 | No such device (it may have been disconnected). |
| 14400010 | Other USB error. Possible causes:  1.Unrecognized discard error code. |
| 14400011 | The transfer is not in progress, or is already complete or cancelled. |

**示例：**

说明

以下示例代码需要放入具体的方法中执行，只是调用usbCancelTransfer接口的必要流程，实际调用时，设备开发者需要遵循设备相关协议进行调用，确保数据的正确传输和设备的兼容性。

```
1. // usbManager.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限。
2. // 把获取到的设备对象作为参数传入usbManager.connectDevice;当usbManager.connectDevice接口成功返回之后；
3. // 才可以调用第三个接口usbManager.claimInterface.当usbManager.claimInterface 调用成功以后,再调用该接口。
4. function usbCancelTransfer() {
5. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
6. if (!devicesList || devicesList.length == 0) {
7. console.info(`device list is empty`);
8. return;
9. }
10. let device: usbManager.USBDevice = devicesList?.[0];
11. usbManager.requestRight(device.name);
12. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(device);
13. if (devicepipe === undefined) {
14. console.info(`connect device fail`);
15. return;
16. }
17. // 获取endpoint端点地址。
18. let endpoint = device.configs?.[0]?.interfaces?.[0]?.endpoints.find((value) => {
19. return value.direction === 0 && value.type === 2
20. })
21. if (endpoint === undefined) {
22. console.info(`invalid endpoint`);
23. return;
24. }
25. // 获取设备的第一个id。
26. let ret: number = usbManager.claimInterface(devicepipe, device.configs?.[0]?.interfaces?.[0], true);
27. let transferParams: usbManager.UsbDataTransferParams = {
28. devPipe: devicepipe,
29. flags: usbManager.UsbTransferFlags.USB_TRANSFER_SHORT_NOT_OK,
30. endpoint: 1,
31. type: usbManager.UsbEndpointTransferType.TRANSFER_TYPE_BULK,
32. timeout: 2000,
33. length: 10,
34. callback: () => {},
35. userData: new Uint8Array(10),
36. buffer: new Uint8Array(10),
37. isoPacketCount: 0,
38. };
39. try {
40. transferParams.endpoint=endpoint?.address as number;
41. transferParams.callback=(err, callBackData: usbManager.SubmitTransferCallback)=>{
42. console.info('callBackData =' +JSON.stringify(callBackData));
43. }
44. usbManager.usbSubmitTransfer(transferParams);
45. usbManager.usbCancelTransfer(transferParams);
46. console.info('USB transfer request submitted.');
47. } catch (error) {
48. console.error('USB transfer failed:', error);
49. }
50. }
```

## usbManager.closePipe

PhonePC/2in1TabletTV

closePipe(pipe: USBDevicePipe): number

关闭设备消息控制通道。

1. 需要调用[usbManager.getDevices](js-apis-usbmanager.md#usbmanagergetdevices)获取设备列表；
2. 调用[usbManager.requestRight](js-apis-usbmanager.md#usbmanagerrequestright)获取设备请求权限；
3. 调用[usbManager.connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)得到devicepipe作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定USB设备消息控制通道，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 关闭设备消息控制通道成功返回0；关闭设备消息控制通道失败返回其它错误码如下：  - 22：服务异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. function closePipe() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.info(`device list is empty`);
5. return;
6. }

8. usbManager.requestRight(devicesList?.[0]?.name);
9. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
10. let ret: number = usbManager.closePipe(devicepipe);
11. console.info(`closePipe = ${ret}`);
12. }
```

## usbManager.hasAccessoryRight14+

PhonePC/2in1TabletTV

hasAccessoryRight(accessory: USBAccessory): boolean

检查应用程序是否有权访问USB配件。

需要调用[usbManager.getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](js-apis-usbmanager.md#usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessory | [USBAccessory](js-apis-usbmanager.md#usbaccessory14) | 是 | USB配件，需要通过[getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示应用程序有权访问USB配件，false表示应用程序无权访问USB配件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |
| 14400005 | Database operation exception. |
| 14401001 | The target USBAccessory not matched. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. try {
3. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
4. let flag = usbManager.hasAccessoryRight(accList?.[0])
5. hilog.info(0, 'testTag ui', `hasAccessoryRight success, ret:${flag}`)
6. } catch (error) {
7. hilog.error(0, 'testTag ui', `hasAccessoryRight error ${error.code}, message is ${error.message}`)
8. }
```

## usbManager.requestAccessoryRight14+

PhonePC/2in1TabletTV

requestAccessoryRight(accessory: USBAccessory): Promise<boolean>

为指定应用程序申请访问USB配件的访问权限。使用Promise异步回调。

需要调用[usbManager.getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](js-apis-usbmanager.md#usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessory | [USBAccessory](js-apis-usbmanager.md#usbaccessory14) | 是 | USB配件，需要通过[getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回应用程序访问配件权限的申请结果。返回true表示权限申请成功；返回false表示权限申请失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |
| 14400005 | Database operation exception. |
| 14401001 | The target USBAccessory not matched. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. try {
3. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
4. let flag = usbManager.requestAccessoryRight(accList?.[0])
5. hilog.info(0, 'testTag ui', `requestAccessoryRight success, ret:${flag}`)
6. } catch (error) {
7. hilog.error(0, 'testTag ui', `requestAccessoryRight error ${error.code}, message is ${error.message}`)
8. }
```

## usbManager.cancelAccessoryRight14+

PhonePC/2in1TabletTV

cancelAccessoryRight(accessory: USBAccessory): void

取消当前应用程序访问USB配件的权限。

需要调用[usbManager.getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](js-apis-usbmanager.md#usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessory | [USBAccessory](js-apis-usbmanager.md#usbaccessory14) | 是 | USB配件，需要通过[getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |
| 14400005 | Database operation exception. |
| 14401001 | The target USBAccessory not matched. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. try {
3. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
4. let flag = usbManager.requestAccessoryRight(accList?.[0])
5. usbManager.cancelAccessoryRight(accList?.[0])
6. hilog.info(0, 'testTag ui', `cancelAccessoryRight success`)
7. } catch (error) {
8. hilog.error(0, 'testTag ui', `cancelAccessoryRight error ${error.code}, message is ${error.message}`)
9. }
```

## usbManager.getAccessoryList14+

PhonePC/2in1TabletTV

getAccessoryList(): Array<Readonly<USBAccessory>>

获取当前已接入主机的USB配件列表。

**系统能力：** SystemCapability.USB.USBManager

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Readonly<[USBAccessory](js-apis-usbmanager.md#usbaccessory14)>> | 只读的USB配件列表。当前仅支持列表中包含1个USB配件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. try {
3. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
4. hilog.info(0, 'testTag ui', `getAccessoryList success, accList: ${JSON.stringify(accList)}`)
5. } catch (error) {
6. hilog.error(0, 'testTag ui', `getAccessoryList error ${error.code}, message is ${error.message}`)
7. }
```

## usbManager.openAccessory14+

PhonePC/2in1TabletTV

openAccessory(accessory: USBAccessory): USBAccessoryHandle

获取配件句柄并打开配件文件描述符。之后可以通过CoreFileKit提供的read/write接口和配件进行通信。

需要调用[usbManager.getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取配件列表，得到[USBAccessory](js-apis-usbmanager.md#usbaccessory14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessory | [USBAccessory](js-apis-usbmanager.md#usbaccessory14) | 是 | USB配件，需要通过[getAccessoryList](js-apis-usbmanager.md#usbmanagergetaccessorylist14)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [USBAccessoryHandle](js-apis-usbmanager.md#usbaccessoryhandle14) | USB配件句柄。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400001 | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |
| 14401001 | The target USBAccessory not matched. |
| 14401002 | Failed to open the native accessory node. |
| 14401003 | Cannot reopen the accessory. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. try {
4. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
5. let flag = usbManager.requestAccessoryRight(accList?.[0])
6. let handle = usbManager.openAccessory(accList?.[0])
7. hilog.info(0, 'testTag ui', `openAccessory success`)
8. let arrayBuffer = new ArrayBuffer(4096);
9. let readLength = fileIo.readSync(handle.accessoryFd, arrayBuffer, {offset: 0, length: 4096});
10. hilog.info(0, 'testTag ui', 'readSync ret: ' + readLength.toString(10));
11. } catch (error) {
12. hilog.error(0, 'testTag ui', `openAccessory error ${error.code}, message is ${error.message}`)
13. }
```

## usbManager.closeAccessory14+

PhonePC/2in1TabletTV

closeAccessory(accessoryHandle: USBAccessoryHandle): void

关闭配件文件描述符。

需要调用[usbManager.openAccessory](js-apis-usbmanager.md#usbmanageropenaccessory14)获取配件列表，得到[USBAccessoryHandle](js-apis-usbmanager.md#usbaccessoryhandle14)作为参数。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accessoryHandle | [USBAccessoryHandle](js-apis-usbmanager.md#usbaccessoryhandle14) | 是 | USB配件句柄。需要通过[openAccessory](js-apis-usbmanager.md#usbmanageropenaccessory14)获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. try {
3. let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList()
4. let flag = usbManager.requestAccessoryRight(accList?.[0])
5. let handle = usbManager.openAccessory(accList?.[0])
6. usbManager.closeAccessory(handle)
7. hilog.info(0, 'testTag ui', `closeAccessory success`)
8. } catch (error) {
9. hilog.error(0, 'testTag ui', `closeAccessory error ${error.code}, message is ${error.message}`)
10. }
```

## usbManager.resetUsbDevice20+

PhonePC/2in1TabletTV

resetUsbDevice(pipe: USBDevicePipe): boolean

重置USB外设。

说明

本接口调用后会重置此前设置的配置和替换接口，请在调用之前确认相关业务已结束。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示重置设备成功，false表示重置设备失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[USB服务错误码](errorcode-usb.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14400001 | Access right denied. Call requestRight to get the USBDevicePipe access right first. |
| 14400004 | Service exception. Possible causes: 1. No accessory is plugged in. |
| 14400008 | No such device (it may have been disconnected). |
| 14400010 | Other USB error. Possible causes:  1.Unrecognized discard error code. |
| 14400013 | The USBDevicePipe validity check failed. Possible causes:  1. The input parameters fail the validation check.  2. The call chain used to obtain the input parameters is not reasonable. |

**示例：**

```
1. function resetUsbDevice() {
2. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
3. if (!devicesList || devicesList.length == 0) {
4. console.error(`device list is empty`);
5. return;
6. }

8. usbManager.requestRight(devicesList?.[0]?.name);
9. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
10. try {
11. let ret: boolean = usbManager.resetUsbDevice(devicepipe);
12. console.info(`resetUsbDevice  = ${ret}`);
13. } catch (err) {
14. console.error(`resetUsbDevice failed: ` + err);
15. }
16. }
```

## usbManager.controlTransfer(deprecated)

PhonePC/2in1TabletTV

controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout ?: number): Promise<number>

控制传输。使用Promise异步回调。

说明

从 API version 9开始支持，从API version 12开始废弃。建议使用 [usbControlTransfer](js-apis-usbmanager.md#usbmanagerusbcontroltransfer12) 替代。

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 是 | 用于确定设备，需要调用connectDevice获取。 |
| controlparam | [USBControlParams](js-apis-usbmanager.md#usbcontrolparamsdeprecated) | 是 | 控制传输参数，按需设置参数，参数传参类型请参考USB协议。 |
| timeout | number | 否 | 超时时间（单位：ms），可选参数，指定时间内等待控制传输完成，若在指定时间内传输完成则正常返回，否则返回超时；默认为0时无限等待直到传输完成。用户按需选择。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，获取传输或接收到的数据块大小。失败返回其它错误码如下：  - -1：驱动异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

```
1. class PARA {
2. request: number = 0
3. reqType: usbManager.USBControlRequestType = 0
4. target: usbManager.USBRequestTargetType = 0
5. value: number = 0
6. index: number = 0
7. data: Uint8Array = new Uint8Array()
8. }

10. let param: PARA = {
11. request: 0x06,
12. reqType: 0x80,
13. target:0,
14. value: 0x01 << 8 | 0,
15. index: 0,
16. data: new Uint8Array(18)
17. };

19. function controlTransfer() {
20. let devicesList: Array<usbManager.USBDevice> = usbManager.getDevices();
21. if (!devicesList || devicesList.length == 0) {
22. console.info(`device list is empty`);
23. return;
24. }

26. usbManager.requestRight(devicesList?.[0]?.name);
27. let devicepipe: usbManager.USBDevicePipe = usbManager.connectDevice(devicesList?.[0]);
28. usbManager.controlTransfer(devicepipe, param).then((ret: number) => {
29. console.info(`controlTransfer = ${ret}`);
30. })
31. }
```

## USBEndpoint

PhonePC/2in1TabletTV

通过USB发送和接收数据的端口。通过[USBInterface](js-apis-usbmanager.md#usbinterface)获取。

说明

主机控制器按照Endpoint类型调度。

协议层打包时依赖type决定传输特性。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | number | 否 | 否 | 端点地址。 |
| attributes | number | 否 | 否 | 端点属性。 |
| interval | number | 否 | 否 | 端点间隔。 |
| maxPacketSize | number | 否 | 否 | 端点最大数据包大小。 |
| direction | [USBRequestDirection](js-apis-usbmanager.md#usbrequestdirection) | 否 | 否 | 端点的方向。 |
| number | number | 否 | 否 | 端点号。 |
| type | number | 否 | 否 | 端点类型。取值见[UsbEndpointTransferType](js-apis-usbmanager.md#usbendpointtransfertype18) |
| interfaceId | number | 否 | 否 | 端点所属的接口的唯一标识。 |

## USBInterface

PhonePC/2in1TabletTV

一个[USBConfiguration](js-apis-usbmanager.md#usbconfiguration)中可以含有多个USBInterface，每个USBInterface提供一个功能。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 接口的唯一标识。 |
| protocol | number | 否 | 否 | 接口的协议。 |
| clazz | number | 否 | 否 | 设备类型。 |
| subClass | number | 否 | 否 | 设备子类。 |
| alternateSetting | number | 否 | 否 | 在同一个接口中的多个描述符中进行切换设置。值的大小表示支持可选模式个数，其中0表示不支持可选模式。 |
| name | string | 否 | 否 | 接口名称。 |
| endpoints | Array<[USBEndpoint](js-apis-usbmanager.md#usbendpoint)> | 否 | 否 | 当前接口所包含的端点。 |

## USBConfiguration

PhonePC/2in1TabletTV

USB配置，一个[USBDevice](js-apis-usbmanager.md#usbdevice)中可以含有多个配置。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 配置的唯一标识。 |
| attributes | number | 否 | 否 | 配置的属性。 |
| maxPower | number | 否 | 否 | 最大功耗，以毫安为单位。 |
| name | string | 否 | 否 | 配置的名称，可以为空。 |
| isRemoteWakeup | boolean | 否 | 否 | 检查当前配置是否支持远程唤醒。true表示支持，false表示不支持。 |
| isSelfPowered | boolean | 否 | 否 | 检查当前配置是否支持独立电源。true表示支持，false表示不支持。 |
| interfaces | Array <[USBInterface](js-apis-usbmanager.md#usbinterface)> | 否 | 否 | 配置支持的接口属性。 |

## USBDevice

PhonePC/2in1TabletTV

USB设备信息。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| busNum | number | 否 | 否 | 总线地址。 |
| devAddress | number | 否 | 否 | 设备地址。 |
| serial | string | 否 | 否 | 序列号。 |
| name | string | 否 | 否 | 设备名字。 |
| manufacturerName | string | 否 | 否 | 产商信息。 |
| productName | string | 否 | 否 | 产品信息。 |
| version | string | 否 | 否 | 版本。 |
| vendorId | number | 否 | 否 | 厂商ID。 |
| productId | number | 否 | 否 | 产品ID。 |
| clazz | number | 否 | 否 | 设备类。 |
| subClass | number | 否 | 否 | 设备子类。 |
| protocol | number | 否 | 否 | 设备协议码。 |
| configs | Array<[USBConfiguration](js-apis-usbmanager.md#usbconfiguration)> | 否 | 否 | 设备配置描述符信息。 |

## USBDevicePipe

PhonePC/2in1TabletTV

USB设备消息传输通道，用于确定设备。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| busNum | number | 否 | 否 | 总线地址。 |
| devAddress | number | 否 | 否 | 设备地址。 |

## USBDeviceRequestParams12+

PhonePC/2in1TabletTV

控制传输参数。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bmRequestType | number | 否 | 否 | 请求控制类型。 |
| bRequest | number | 否 | 否 | 请求类型。 |
| wValue | number | 否 | 否 | 请求参数。 |
| wIndex | number | 否 | 否 | 请求参数value对应的索引值。 |
| wLength | number | 否 | 否 | 请求数据的长度。 |
| data | Uint8Array | 否 | 否 | 用于写入或读取的缓冲区。 |

## USBRequestTargetType

PhonePC/2in1TabletTV

请求目标类型。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB\_REQUEST\_TARGET\_DEVICE | 0 | 设备。 |
| USB\_REQUEST\_TARGET\_INTERFACE | 1 | 接口。 |
| USB\_REQUEST\_TARGET\_ENDPOINT | 2 | 端点。 |
| USB\_REQUEST\_TARGET\_OTHER | 3 | 其它。 |

## USBControlRequestType

PhonePC/2in1TabletTV

控制请求类型。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB\_REQUEST\_TYPE\_STANDARD | 0 | 标准。 |
| USB\_REQUEST\_TYPE\_CLASS | 1 | 类。 |
| USB\_REQUEST\_TYPE\_VENDOR | 2 | 厂商。 |

## USBRequestDirection

PhonePC/2in1TabletTV

请求方向。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB\_REQUEST\_DIR\_TO\_DEVICE | 0 | 写数据，主设备往从设备。 |
| USB\_REQUEST\_DIR\_FROM\_DEVICE | 0x80 | 读数据，从设备往主设备。 |

## USBAccessory14+

PhonePC/2in1TabletTV

USB配件信息。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufacturer | string | 否 | 否 | 配件的生产厂商。 |
| product | string | 否 | 否 | 配件的产品类型。 |
| description | string | 否 | 否 | 配件的描述。 |
| version | string | 否 | 否 | 配件的版本。 |
| serialNumber | string | 否 | 否 | 配件的SN号。 |

## USBAccessoryHandle14+

PhonePC/2in1TabletTV

USB配件句柄。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| accessoryFd | number | 否 | 否 | 配件文件描述符。合法的accessoryFd是正整数。 |

## UsbDataTransferParams18+

PhonePC/2in1TabletTV

作为通用USB数据传输接口，客户端需要填充这个对象中的参数，用以发起传输请求。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| devPipe | [USBDevicePipe](js-apis-usbmanager.md#usbdevicepipe) | 否 | 否 | 用于确定总线地址和设备地址，需要调用[connectDevice](js-apis-usbmanager.md#usbmanagerconnectdevice)获取。 |
| flags | [UsbTransferFlags](js-apis-usbmanager.md#usbtransferflags18) | 否 | 否 | USB传输标志。 |
| endpoint | number | 否 | 否 | 端点地址，正整数。 |
| type | [UsbEndpointTransferType](js-apis-usbmanager.md#usbendpointtransfertype18) | 否 | 否 | 传输类型。 |
| timeout | number | 否 | 否 | 超时时间，单位为毫秒。 |
| length | number | 否 | 否 | 数据缓冲区的长度，必须是非负数（期望长度），单位为字节。 |
| callback | AsyncCallback<[SubmitTransferCallback](js-apis-usbmanager.md#submittransfercallback18)> | 否 | 否 | 传输完成时的回调信息。 |
| userData | Uint8Array | 否 | 否 | 用户上下文数据。 |
| buffer | Uint8Array | 否 | 否 | 用于存储读或者写请求时的数据。 |
| isoPacketCount | number | 否 | 否 | 实时传输时数据包的数量，仅用于具有实时传输端点的I/O。必须是非负数，单位为个数。 |

## UsbTransferFlags18+

PhonePC/2in1TabletTV

USB传输标志。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB\_TRANSFER\_SHORT\_NOT\_OK | 0 | 将短帧报告为错误。 |
| USB\_TRANSFER\_FREE\_BUFFER | 1 | 自动释放传输缓冲区。 |
| USB\_TRANSFER\_FREE\_TRANSFER | 2 | 完成回调后自动传输。 |
| USB\_TRANSFER\_ADD\_ZERO\_PACKET | 3 | 传输将增加一个额外的数据包。 |

## UsbEndpointTransferType18+

PhonePC/2in1TabletTV

Usb传输类型。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRANSFER\_TYPE\_ISOCHRONOUS | 0x1 | 实时传输。 |
| TRANSFER\_TYPE\_BULK | 0x2 | 批量传输。 |
| TRANSFER\_TYPE\_INTERRUPT | 0x3 | 中断传输。 |

## SubmitTransferCallback18+

PhonePC/2in1TabletTV

Usb异步传输回调。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| actualLength | number | 否 | 否 | 读写操作的实际长度值，单位为字节。 |
| status | [UsbTransferStatus](js-apis-usbmanager.md#usbtransferstatus18) | 否 | 否 | 读写操作完成的状态。 |
| isoPacketDescs | Array<Readonly<[UsbIsoPacketDescriptor](js-apis-usbmanager.md#usbisopacketdescriptor18)>> | 否 | 否 | 实时传输的分包信息。 |

## UsbTransferStatus18+

PhonePC/2in1TabletTV

数据处理完成后通过回调返回的状态码。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRANSFER\_COMPLETED | 0 | 传输完成。 |
| TRANSFER\_ERROR | 1 | 传输失败。 |
| TRANSFER\_TIMED\_OUT | 2 | 传输超时。 |
| TRANSFER\_CANCELED | 3 | 传输已被取消。 |
| TRANSFER\_STALL | 4 | 检测到暂停（批量/中断端点）。 |
| TRANSFER\_NO\_DEVICE | 5 | 设备已断开。 |
| TRANSFER\_OVERFLOW | 6 | 设备发送的数据比请求的多。 |

## UsbIsoPacketDescriptor18+

PhonePC/2in1TabletTV

实时传输模式回调返回的分包信息。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 否 | 否 | 读写操作的期望长度值，单位为字节。 |
| actualLength | number | 否 | 否 | 读写操作的实际长度值，单位为字节。 |
| status | [UsbTransferStatus](js-apis-usbmanager.md#usbtransferstatus18) | 否 | 否 | 实时传输分包的状态码。 |

## USBControlParams(deprecated)

PhonePC/2in1TabletTV

控制传输参数。

说明

从 API version 9开始支持，从API version 18开始废弃。建议使用 [USBDeviceRequestParams](js-apis-usbmanager.md#usbdevicerequestparams12) 替代。

**系统能力：** SystemCapability.USB.USBManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| request | number | 否 | 否 | 请求类型。 |
| target | [USBRequestTargetType](js-apis-usbmanager.md#usbrequesttargettype) | 否 | 否 | 请求目标类型。 |
| reqType | [USBControlRequestType](js-apis-usbmanager.md#usbcontrolrequesttype) | 否 | 否 | 请求控制类型。 |
| value | number | 否 | 否 | 请求参数。 |
| index | number | 否 | 否 | 请求参数value对应的索引值。 |
| data | Uint8Array | 否 | 否 | 用于写入或读取的缓冲区。 |
