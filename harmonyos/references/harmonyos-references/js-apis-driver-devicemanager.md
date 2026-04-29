---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-driver-devicemanager
title: @ohos.driver.deviceManager (外设管理)
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > @ohos.driver.deviceManager (外设管理)
category: harmonyos-references
scraped_at: 2026-04-29T14:01:19+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6b0cefef124b3ee754f1c00455cd31f463e386c7d9f706ecf6e21988c269686e
---

本模块主要提供管理外部设备的相关功能，包括查询设备列表、绑定设备和解除绑定设备。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## deviceManager.queryDevices

PC/2in1

queryDevices(busType?: number): Array<Readonly<Device>>

获取接入主设备的外部设备列表。如果没有设备接入，那么将会返回一个空的列表。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| busType | number | 否 | 由[BusType](js-apis-driver-devicemanager.md#bustype)约定的设备总线类型，不填则查找所有类型设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<Readonly<[Device](js-apis-driver-devicemanager.md#device)>> | 设备信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 22900001 | ExternalDeviceManager service exception or busType parameter error. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';

3. try {
4. let devices : Array<deviceManager.Device> = deviceManager.queryDevices(deviceManager.BusType.USB);
5. for (let item of devices) {
6. let device : deviceManager.USBDevice = item as deviceManager.USBDevice;
7. console.info(`Device id is ${device.deviceId}`);
8. }
9. } catch (error) {
10. console.error(`Failed to query device. Code is ${error.code}, message is ${error.message}`);
11. }
```

## deviceManager.bindDriverWithDeviceId19+

PC/2in1

bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

根据queryDevices()返回的设备信息绑定设备。使用Promise异步回调。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**需要权限：** ohos.permission.ACCESS\_DDK\_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RemoteDeviceDriver](js-apis-driver-devicemanager.md#remotedevicedriver11)> | Promise对象，返回RemoteDeviceDriver对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300002 | The driver service does not allow any client to bind. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.bindDriverWithDeviceId(12345678, (error : BusinessError, data : number) => {
7. console.error(`Device is disconnected`);
8. }).then((data: deviceManager.RemoteDeviceDriver) => {
9. console.info(`bindDriverWithDeviceId success, Device_Id is ${data.deviceId}.
10. remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
11. }, (error: BusinessError) => {
12. console.error(`bindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`bindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
16. }
```

## deviceManager.unbindDriverWithDeviceId19+

PC/2in1

unbindDriverWithDeviceId(deviceId: number): Promise<number>

解除设备绑定。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS\_DDK\_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回解除绑定的设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300003 | There is no binding relationship. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.unbindDriverWithDeviceId(12345678).then((data : number) => {
7. console.info(`unbindDriverWithDeviceId success, Device_Id is ${data}.`);
8. }, (error : BusinessError) => {
9. console.error(`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
10. });
11. } catch (error) {
12. console.error(`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
13. }
```

## deviceManager.bindDevice(deprecated)

PC/2in1

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{deviceId: number; remote: rpc.IRemoteObject;}>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息以及device。

说明

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |
| callback | AsyncCallback<{deviceId: number; remote: [rpc.IRemoteObject](js-apis-rpc.md#iremoteobject);}> | 是 | 回调函数。当绑定设备成功时，err为undefined，data包含设备ID和绑定设备驱动通信对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { rpc } from '@kit.IPCKit';

5. interface DataType {
6. deviceId : number;
7. remote : rpc.IRemoteObject;
8. }

10. try {
11. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
12. deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
13. console.error(`Device is disconnected`);
14. }, (error : BusinessError, data : DataType) => {
15. if (error) {
16. console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
17. return;
18. }
19. console.info(`bindDevice success`);
20. });
21. } catch (error) {
22. console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
23. }
```

## deviceManager.bindDeviceDriver(deprecated)

PC/2in1

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices()](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息以及device。

说明

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |
| callback | AsyncCallback<[RemoteDeviceDriver](js-apis-driver-devicemanager.md#remotedevicedriver11)> | 是 | 回调函数。当绑定设备驱动成功时，err为undefined，data为包括设备ID和远程对象的[RemoteDeviceDriver](js-apis-driver-devicemanager.md#remotedevicedriver11)对象；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
7. console.error(`Device is disconnected`);
8. }, (error : BusinessError, data : deviceManager.RemoteDeviceDriver) => {
9. if (error) {
10. console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
11. return;
12. }
13. console.info(`bindDeviceDriver success`);
14. });
15. } catch (error) {
16. console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
17. }
```

## deviceManager.bindDevice(deprecated)

PC/2in1

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{deviceId: number; remote: rpc.IRemoteObject;}>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息以及device。

说明

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<{deviceId: number; remote: [rpc.IRemoteObject](js-apis-rpc.md#iremoteobject);}> | Promise对象，返回一个包含设备ID和IRemoteObject的对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
7. console.error(`Device is disconnected`);
8. }).then(data => {
9. console.info(`bindDevice success, Device_Id is ${data.deviceId}.
10. remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
11. }, (error: BusinessError) => {
12. console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
16. }
```

## deviceManager.bindDeviceDriver(deprecated)

PC/2in1

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;

根据queryDevices()返回的设备信息绑定设备。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息以及device。

说明

从 API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| onDisconnect | AsyncCallback<number> | 是 | 回调函数。当绑定设备断开时，err为undefined，data为解绑的设备ID；否则为错误对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RemoteDeviceDriver](js-apis-driver-devicemanager.md#remotedevicedriver11)> | Promise对象，返回RemoteDeviceDriver对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
7. console.error(`Device is disconnected`);
8. }).then((data: deviceManager.RemoteDeviceDriver) => {
9. console.info(`bindDeviceDriver success, Device_Id is ${data.deviceId}.
10. remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}`);
11. }, (error: BusinessError) => {
12. console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
13. });
14. } catch (error) {
15. console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
16. }
```

## deviceManager.unbindDevice(deprecated)

PC/2in1

unbindDevice(deviceId: number, callback: AsyncCallback<number>): void

解除设备绑定。

说明

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当解绑设备成功时，err为undefined，data为设备ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.unbindDevice(12345678, (error : BusinessError, data : number) => {
7. if (error) {
8. console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
9. return;
10. }
11. console.info(`unbindDevice success`);
12. });
13. } catch (error) {
14. console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
15. }
```

## deviceManager.unbindDevice(deprecated)

PC/2in1

unbindDevice(deviceId: number): Promise<number>

解除设备绑定。该接口使用一个Promise对象来返回结果。

说明

从 API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限**：ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过queryDevices获得。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回解除绑定的设备ID。 |

**示例：**

```
1. import { deviceManager } from '@kit.DriverDevelopmentKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
6. deviceManager.unbindDevice(12345678).then((data : number) => {
7. console.info(`unbindDevice success, Device_Id is ${data}.`);
8. }, (error : BusinessError) => {
9. console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
10. });
11. } catch (error) {
12. console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
13. }
```

## Device

PC/2in1

外设信息。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| busType | [BusType](js-apis-driver-devicemanager.md#bustype) | 否 | 否 | 总线类型。 |
| deviceId | number | 否 | 否 | 设备ID。 |
| description | string | 否 | 否 | 设备描述。 |

## USBDevice

PC/2in1

USB设备信息，继承自[Device](js-apis-driver-devicemanager.md#device)。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | USB设备Vendor ID。 |
| productId | number | 否 | 否 | USB设备Product ID。 |

## BusType

PC/2in1

设备总线类型。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB | 1 | USB总线类型。 |

## RemoteDeviceDriver11+

PC/2in1

远程设备驱动。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId11+ | number | 否 | 否 | 设备ID。 |
| remote11+ | [rpc.IRemoteObject](js-apis-rpc.md#iremoteobject) | 否 | 否 | 远程驱动程序对象。 |
