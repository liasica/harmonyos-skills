---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-driver-devicemanager
title: "@ohos.driver.deviceManager (外设管理)"
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > @ohos.driver.deviceManager (外设管理)
category: harmonyos-references
scraped_at: 2026-09-05T06:19:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9db0211b0d901a06eb2b60aeec925912efc0eb2c45d41ba68948f29ef112751
---

本模块是驱动开发套件提供的设备管理接口集合，提供外接设备信息的查询能力、应用与外设驱动之间的绑定与解绑能力。本模块的接口可用于实现以下功能：

* 查询系统中已接入的外设设备列表。
* 绑定指定外设设备并获取远程驱动通信对象，从而能通过跨进程通信与外设驱动进行数据交互。
* 使用完毕后解绑设备，释放资源。

本模块的外设访问能力需要多个 API 组合完成，典型调用流程为：**查询设备 → 绑定设备获取通信对象 → 通过通信对象与驱动交互 → 解绑设备释放资源**。设备绑定的生命周期视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/7sRXFPDdR2iv4Gw0C0h8JA/zh-cn_image_0000002712407318.png)

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。调用本模块接口需要申请权限 ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER（查询/绑定/解绑）或 ohos.permission.ACCESS\_DDK\_DRIVERS（新版本的绑定/解绑接口）。

## 导入模块

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
```

## deviceManager.queryDevices

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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';

try {
  let devices: Array<deviceManager.Device> = deviceManager.queryDevices(deviceManager.BusType.USB);
  for (let item of devices) {
    let device: deviceManager.USBDevice = item as deviceManager.USBDevice;
    console.info(`Device id is ${device.deviceId}`);
  }
} catch (error) {
  console.error(`Failed to query device. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.bindDriverWithDeviceId19+

bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

根据queryDevices()返回的设备信息绑定设备，必须与unbindDriverWithDeviceId接口成对使用。使用Promise异步回调。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**需要权限：** ohos.permission.ACCESS\_DDK\_DRIVERS

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDriverWithDeviceId(12345678, (error: BusinessError, data: number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDriverWithDeviceId success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor(): "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.unbindDriverWithDeviceId19+

unbindDriverWithDeviceId(deviceId: number): Promise<number>

解除设备绑定，调用前需要先通过bindDriverWithDeviceId绑定设备。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_DDK\_DRIVERS

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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDriverWithDeviceId(12345678).then((data: number) => {
    console.info(`unbindDriverWithDeviceId success, Device_Id is ${data}.`);
  }, (error: BusinessError) => {
    console.error(`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{deviceId: number; remote: rpc.IRemoteObject;}>): void

根据queryDevices()返回的设备信息绑定设备。必须和unbindDevice接口成对使用。

需要调用[deviceManager.queryDevices()](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**说明** 

从API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

interface DataType {
  deviceId: number;
  remote: rpc.IRemoteObject;
}

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error: BusinessError, data: number) => {
    console.error(`Device is disconnected`);
  }, (error: BusinessError, data: DataType) => {
    if (error) {
      console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDevice success`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void

根据queryDevices()返回的设备信息绑定设备。必须与unbindDevice接口成对使用。

需要调用[deviceManager.queryDevices()](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**说明** 

从API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error: BusinessError, data: number) => {
    console.error(`Device is disconnected`);
  }, (error: BusinessError, data: deviceManager.RemoteDeviceDriver) => {
    if (error) {
      console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`bindDeviceDriver success`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{deviceId: number; remote: rpc.IRemoteObject;}>

根据queryDevices()返回的设备信息绑定设备。必须和unbindDevice接口成对使用。使用Promise异步回调。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**说明** 

从API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDevice(12345678, (error: BusinessError, data: number) => {
    console.error(`Device is disconnected`);
  }).then(data => {
    console.info(`bindDevice success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor(): "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

根据queryDevices()返回的设备信息绑定设备。必须与unbindDevice接口成对使用。使用Promise异步回调。

需要调用[deviceManager.queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获取设备信息列表。

**说明** 

从API version 11开始支持，从API version 19开始废弃。建议使用[deviceManager.bindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.bindDeviceDriver(12345678, (error: BusinessError, data: number) => {
    console.error(`Device is disconnected`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(`bindDeviceDriver success, Device_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor(): "null"}`);
  }, (error: BusinessError) => {
    console.error(`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number, callback: AsyncCallback<number>): void

解除设备绑定。必须先通过bindDevice接口绑定设备。

**说明** 

从API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当解绑设备成功时，err为undefined，data为设备ID；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[驱动错误码](errorcode-devicemanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 22900001 | ExternalDeviceManager service exception. |

**示例：**

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678, (error: BusinessError, data: number) => {
    if (error) {
      console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
      return;
    }
    console.info(`unbindDevice success`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

## deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number): Promise<number>

解除设备绑定。必须先通过bindDevice接口绑定设备。使用Promise异步回调。

**说明** 

从API version 10开始支持，从API version 19开始废弃。建议使用[deviceManager.unbindDriverWithDeviceId](js-apis-driver-devicemanager.md#devicemanagerunbinddriverwithdeviceid19)替代。

**需要权限：** ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**系统能力：** SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 设备ID，通过[queryDevices](js-apis-driver-devicemanager.md#devicemanagerquerydevices)获得。 |

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

```ts
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 12345678为示例deviceId，应用开发时可通过queryDevices查询到相应设备的deviceId作为入参
  deviceManager.unbindDevice(12345678).then((data: number) => {
    console.info(`unbindDevice success, Device_Id is ${data}.`);
  }, (error: BusinessError) => {
    console.error(`unbindDevice async fail. Code is ${error.code}, message is ${error.message}`);
  });
} catch (error) {
  console.error(`unbindDevice fail. Code is ${error.code}, message is ${error.message}`);
}
```

## Device

外设信息。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| busType | [BusType](js-apis-driver-devicemanager.md#bustype) | 否 | 否 | 总线类型。 |
| deviceId | number | 否 | 否 | 设备ID。 |
| description | string | 否 | 否 | 设备描述。 |

## USBDevice

USB设备信息，继承自[Device](js-apis-driver-devicemanager.md#device)。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | USB设备Vendor ID。 |
| productId | number | 否 | 否 | USB设备Product ID。 |

## BusType

设备总线类型。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USB | 1 | USB总线类型。 |

## RemoteDeviceDriver11+

远程设备驱动。

**系统能力：** SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId11+ | number | 否 | 否 | 设备ID。 |
| remote11+ | [rpc.IRemoteObject](js-apis-rpc.md#iremoteobject) | 否 | 否 | 远程驱动通信对象。 |
