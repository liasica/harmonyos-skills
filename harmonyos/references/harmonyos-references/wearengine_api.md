---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api
title: wearEngine（穿戴设备能力开放）
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > ArkTS API > wearEngine（穿戴设备能力开放）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:80b4ce700de650bfee6a91d135befc98680f84fe4c8717630f1eef7d5255bb41
---

本模块提供手机与穿戴设备侧的交互能力。应用可调用模块内接口实现如下功能：

* 获取与当前设备已连接配对的设备列表、与对端设备互通消息互送文件等。
* 查询穿戴设备状态、向穿戴设备发送模板化通知、接收穿戴设备传感器的相关数据等。

**说明** 

针对系统能力SystemCapability.Health.WearEngine，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

**起始版本**：5.0.0(12)

## 导入模块

```typescript
import { wearEngine } from '@kit.WearEngine';
```

## wearEngine.getAuthClient

getAuthClient(context: common.Context): AuthClient

用于获取权限管理的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AuthClient](wearengine_api.md#authclient) | 权限管理客户端，存储了权限模块的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```ts
import { wearEngine } from '@kit.WearEngine';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting auth client`);
```

## AuthClient

权限管理客户端类，由[wearEngine.getAuthClient](wearengine_api.md#wearenginegetauthclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### requestAuthorization

requestAuthorization(request: AuthorizationRequest): Promise<AuthorizationResponse>

向手机用户申请需要授权的权限，返回申请的权限中用户已授权的权限，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [AuthorizationRequest](wearengine_api.md#authorizationrequest) | 是 | 权限请求类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthorizationResponse](wearengine_api.md#authorizationresponse)> | Promise对象，返回权限响应类。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

let request: wearEngine.AuthorizationRequest = {
  permissions: [wearEngine.Permission.USER_STATUS]
}

// 向手机用户申请需要授权的权限，返回申请的权限中用户已授权的权限，使用Promise异步回调。
authClient.requestAuthorization(request).then(result => {
  console.info(`Succeeded in requesting authorize, authorized permissions is ${result.permissions}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to request authorize. Code is ${error.code}, message is ${error.message}`);
})
```

### getAuthorization

getAuthorization(): Promise<AuthorizationResponse>

获取用户已授权的权限，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AuthorizationResponse](wearengine_api.md#authorizationresponse)> | Promise对象，返回权限响应类。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

// 获取用户已授权的权限，使用Promise异步回调。
authClient.getAuthorization().then(result => {
  console.info(`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}`);
})
```

## AuthorizationBase

权限控制模块输入输出的基类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | [Permission](wearengine_api.md#permission)[] | 否 | 否 | 权限枚举类型的数组。 |

## Permission

权限枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_STATUS | 2 | 获取用户状态权限。如：穿戴设备的佩戴状态。 |
| MOTION\_SENSOR | 3 | 获取对端设备运动传感器数据权限。如：加速度传感器数据。 |
| HEALTH\_SENSOR | 4 | 获取对端设备人体传感器数据权限。如：心率传感器数据。 |
| DEVICE\_IDENTIFIER | 6 | 获取已连接穿戴设备的序列号。 |

## AuthorizationRequest

权限请求类，继承自[AuthorizationBase](wearengine_api.md#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

## AuthorizationResponse

权限响应类，继承自[AuthorizationBase](wearengine_api.md#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

## wearEngine.getDeviceClient

getDeviceClient(context: common.Context): DeviceClient

用于获取Device模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClient](wearengine_api.md#deviceclient) | Device客户端，存储了Device模块的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting device client.`);
```

## DeviceClient

Device客户端类。由接口[wearEngine.getDeviceClient](wearengine_api.md#wearenginegetdeviceclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### getConnectedDevices

getConnectedDevices(): Promise<Device[]>

获取当前已连接且支持wearEngine能力集的设备，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Device](wearengine_api.md#device)[]> | Promise对象，返回设备列表。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
deviceClient.getConnectedDevices().then((devices) => {
  console.info(`Succeeded in getting devices, devices number is ${devices.length}.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get devices. Code is ${error.code}, message is ${error.message}.`);
})
```

## Device

穿戴设备信息类。由接口[getConnectedDevices](wearengine_api.md#getconnecteddevices)返回。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| randomId | string | 否 | 否 | 设备随机唯一标识符，每次绑定自动生成。 |
| category | [DeviceCategory](wearengine_api.md#devicecategory) | 否 | 是 | 设备类型。 |
| name | string | 否 | 是 | 设备名称。 |
| softwareVersion | string | 否 | 是 | 设备软件版本号。 |
| model | string | 否 | 是 | 设备型号。 |
| isSmartWatch | boolean | 否 | 是 | 设备是否为智能表。true：是，false：不是。 |
| osCategory | [OsCategory](wearengine_api.md#oscategory) | 否 | 是 | 设备的操作系统类别。  **起始版本：** 5.1.0(18) |

### isWearEngineCapabilitySupported

isWearEngineCapabilitySupported(capability: WearEngineCapability): Promise<boolean>

通过[getConnectedDevices](wearengine_api.md#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备是否支持指定的[WearEngineCapability](wearengine_api.md#wearenginecapability)，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capability | [WearEngineCapability](wearengine_api.md#wearenginecapability) | 是 | 指定的WearEngine能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否支持指定能力的查询结果。  true：支持，false：不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P_COMMUNICATION)
      .then((isSupportP2P) => {
        console.info(`Succeeded in checking p2p capability, result is ${isSupportP2P}`);
      }).catch((error: BusinessError) => {
      console.error(`Failed to check p2p capability. Code is ${error.code}, message is${error.message}`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is${error.message}`);
}
```

### isDeviceCapabilitySupported

isDeviceCapabilitySupported(capability: DeviceCapability): Promise<boolean>

通过[getConnectedDevices](wearengine_api.md#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备是否支持指定的[DeviceCapability](wearengine_api.md#devicecapability)，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capability | [DeviceCapability](wearengine_api.md#devicecapability) | 是 | 指定的Device能力。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否支持指定能力的查询结果。  true：支持，false：不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();
  
  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.CBT_I).then((isSupportCBTI) => {
      console.info(`Succeeded in checking CBTI capability, result is ${isSupportCBTI}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to check CBTI capability. Code is ${error.code}, message is ${error.message}`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### getSerialNumber

getSerialNumber(): Promise<string>

通过[getConnectedDevices](wearengine_api.md#getconnecteddevices)接口获取到已连接的穿戴设备后，查询设备的SN，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回设备SN。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    device.getSerialNumber().then((sn) => {
      console.info(`Succeeded in getting device SN, result is ${sn}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get device SN. Code is ${error.code}, message is ${error.message}`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

## WearEngineCapability

WearEngine能力集枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| P2P\_COMMUNICATION | 1 | P2p(peer-to-peer)能力。 |
| MONITOR | 2 | Monitor能力。 |
| NOTIFICATION | 3 | Notify能力。 |
| SENSOR | 4 | Sensor能力。 |

## DeviceCapability

Device能力集枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP\_INSTALLATION | 14 | 支持应用安装能力。 |
| CBT\_I | 128 | CBTI数字疗法能力。 |

## DeviceCategory

设备类型枚举类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 1 | 手机或平板类型。 |
| WATCH | 2 | 手表类型。 |
| BAND | 3 | 手环类型。 |
| OTHER\_DEVICES | 255 | 其它设备类型。 |

## OsCategory

设备的操作系统类型枚举类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HARMONYOS | 1 | HarmonyOS |
| IOS | 2 | IOS |
| OTHER\_OS | 255 | 其他类型 |

## wearEngine.getMonitorClient

getMonitorClient(context: common.Context): MonitorClient

用于获取Monitor模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MonitorClient](wearengine_api.md#monitorclient) | Monitor客户端，存储了Monitor模块的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';

let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting monitor client.`);
```

## MonitorClient

Monitor客户端类。由接口[wearEngine.getMonitorClient](wearengine_api.md#wearenginegetmonitorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### queryStatus

queryStatus(deviceRandomId: string, item: MonitorItem): Promise<MonitorData>

查询指定设备的指定状态，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次查询的设备。 |
| item | [MonitorItem](wearengine_api.md#monitoritem) | 是 | 可查询的设备状态枚举，用于指定本次查询的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MonitorData](wearengine_api.md#monitordata)> | Promise对象，返回查询的结果。不同状态返回值的含义请参考[MonitorItem](wearengine_api.md#monitoritem)。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | The wearable device does not support the capabilities.  适用版本：6.1.0(23)+ |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    monitorClient.queryStatus(device.randomId, wearEngine.MonitorItem.WEAR_STATUS).then((result) => {
      console.info(`Succeeded in querying wear status, result is ${result.code}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to query wear status. Code is ${error.code}, message is ${error.message}.`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### subscribeEvent

subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>

监听指定设备的指定状态变化事件，当状态发生变化时，使用callback异步回调，订阅成功与否，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在Wearable中可以订阅设备连接状态变化事件，订阅其他事件返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| type | [MonitorEvent](wearengine_api.md#monitorevent) | 是 | 可订阅的设备状态枚举，用于指定本次订阅监听的设备状态。 |
| callback | Callback<[MonitorEventData](wearengine_api.md#monitoreventdata)> | 是 | 回调函数，返回设备对应状态变化后的信息。  状态发生变化后执行，建议保证回调函数的生命周期延长至取消监听时。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | In Wearable, when subscribing to events other than changes in device connection status, this error code is returned.  适用版本：6.1.0(23)+ |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    let callback = (monitorEventData: wearEngine.MonitorEventData) => {
      console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`);
    }
    monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback)
      .then(() => {
        console.info(`Succeeded in subscribing wear status.`);
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.`);
      })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### unsubscribeEvent

unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>

取消订阅监听指定设备的指定状态变化事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在Wearable中可以取消订阅设备连接状态变化事件，取消订阅其他事件返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次取消订阅的设备。 |
| type | [MonitorEvent](wearengine_api.md#monitorevent) | 是 | 可订阅的设备状态枚举，用于指定本次取消订阅监听的设备状态。 |
| callback | Callback<[MonitorEventData](wearengine_api.md#monitoreventdata)> | 是 | 回调函数，返回设备对应状态变化后的信息。  此处需保证传入的对象与调用[subscribeEvent](wearengine_api.md#subscribeevent)接口时传入的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | In Wearable, when unsubscribing to events other than changes in device connection status, this error code is returned.  适用版本：6.1.0(23)+ |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    // 解注册时回调函数需要保证和注册时为同一个对象
    let callback = (monitorEventData: wearEngine.MonitorEventData) => {
      console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`);
    }

    // 创建待删除的订阅任务
    monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback)
      .then(() => {
        console.info(`Succeeded in subscribing wear status`);

        // 删除之前创建的订阅任务
        monitorClient.unsubscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback)
          .then(() => {
            console.info(`Succeeded in unsubscribing wear status`);
          })
          .catch((error: BusinessError) => {
            console.error(`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.`);
          })
      })
      .catch((error: BusinessError) => {
        console.error(`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.`);
      })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is${error.message}`);
}
```

## MonitorItem

设备状态的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WEAR\_STATUS | 'wearStatus' | 佩戴状态。返回值含义：  1：佩戴  2：未佩戴 |
| POWER\_STATUS | 'powerStatus' | 电量状态。返回值含义：剩余电量百分比（0~100）。 |
| CHARGE\_STATUS | 'chargeStatus' | 充电状态。返回值含义：  1：正在充电  2：未充电  3：电量已充满 |
| AVAILABLE\_STORAGE\_SPACE | 'availableStorageSpace' | 可用存储空间。返回值含义：用户可用空间（KB）。 |
| POWER\_MODE | 'powerMode' | 电源模式。返回值含义：  -1：设备不区分电源模式  0：智能模式  1：超长续航模式 |
| SPORT\_STATUS | 'sportStatus' | 运动状态。返回值含义：  3：运动开始  4：运动暂停  5：运动中  6：运动结束  **起始版本：** 6.1.1(24) |

## MonitorEvent

设备状态变化事件的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_CONNECTION\_STATUS\_CHANGED | 'connectionStatus' | 设备连接状态变化。  返回值含义：2：连接成功；3：连接断开；5：设备解绑 |
| EVENT\_BATTERY\_LEVEL\_DROPPED | 'lowPower' | 设备电量降低。  返回值含义：剩余电量百分比（0~100）。 |
| EVENT\_WEAR\_STATUS\_CHANGED | 'wearStatus' | 设备佩戴状态变化。  返回值含义：1：佩戴，2：未佩戴。 |
| EVENT\_HEART\_RATE\_ALARM | 'heartRateAlarm' | 心率告警。  返回值含义：1：静态心率过高，2：静态心率过低，3：运动心率过高，4：运动心率过低。 |
| EVENT\_CHARGE\_STATUS\_CHANGED | 'chargeStatus' | 充电状态变化。  返回值含义：1：充电开始，2：充电结束，3：充电完成。 |
| EVENT\_POWER\_MODE\_CHANGED | 'powerMode' | 电源模式切换。  返回值含义：0：切换至智能模式，1：切换至超长续航模式。 |

## MonitorData

作为[queryStatus](wearengine_api.md#querystatus)接口的返回值与[subscribeEvent](wearengine_api.md#subscribeevent)接口回调函数的入参，返回设备的状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 当使用[queryStatus](wearengine_api.md#querystatus)接口查询设备状态时，返回值含义请见[MonitorItem](wearengine_api.md#monitoritem)。  当使用[subscribeEvent](wearengine_api.md#subscribeevent)接口订阅监听时，返回值含义请见[MonitorEvent](wearengine_api.md#monitorevent)。 |
| data | string | 否 | 是 | 扩展字段。 |

## MonitorEventData

作为[subscribeEvent](wearengine_api.md#subscribeevent)接口的返回值，当订阅监听的事件触发时，作为入参将设备对应状态变化后的信息传递给回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [MonitorEvent](wearengine_api.md#monitorevent) | 否 | 否 | 回调函数注册的订阅监听事件枚举值。 |
| data | [MonitorData](wearengine_api.md#monitordata) | 否 | 否 | 设备状态发生变化后的状态信息。 |

## wearEngine.getP2pClient

getP2pClient(context: common.Context): P2pClient

用于获取P2p模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [P2pClient](wearengine_api.md#p2pclient) | P2p客户端，存储了P2p模块的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';

let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting p2p client.`);
```

## P2pClient

P2p客户端类。由接口[wearEngine.getP2pClient](wearengine_api.md#wearenginegetp2pclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### isRemoteAppInstalled

isRemoteAppInstalled(deviceRandomId: string, remoteBundleName: string): Promise<boolean>

判断穿戴设备是否已安装指定的应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待查询的设备侧指定应用名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示设备侧应用是否安装。true：已安装，false：未安装。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 将设备侧应用包名定义为remoteBundleName
        let remoteBundleName: string = '';

        p2pClient.isRemoteAppInstalled(device.randomId, remoteBundleName).then((isInstall) => {
          console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### getRemoteAppVersion

getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise<number>

获取穿戴设备指定应用的版本号，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.1.0(23)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。 对于6.1.1(24)及之后版本，该接口在Phone、Tablet、Wearable中可正常调用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待查询版本号的设备侧应用名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回设备侧应用的版本号。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 将设备侧应用包名定义为remoteBundleName
        let remoteBundleName: string = '';

        p2pClient.getRemoteAppVersion(device.randomId, remoteBundleName).then((version) => {
          console.info(`Succeeded in getting remote app version, version is ${version}.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to check get remote app version. Code is ${error.code}, message is${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is${error.message}`);
}
```

### startRemoteApp

startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>

拉起穿戴设备的指定应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待拉起的设备侧应用名称。 |
| transformLocalBundleName | boolean | 否 | 是否需要将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。默认值：false。  true：转换，false：不转换。  待兼容应用设置请参考[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象，返回P2p通信的结果。  属性中的code字段表示本次拉起应用的结果。其中，返回203表示穿戴设备应用未在module.json5文件的metadata字段中正确配置wearEngineRemoteAppNameList属性，配置方式请参考[对端应用通过startRemoteApp拉起穿戴侧应用](../harmonyos-guides/watch_p2p_communication.md#对端应用通过startremoteapp拉起穿戴侧应用)。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 将设备侧应用包名定义为remoteBundleName
        let remoteBundleName: string = '';

        // transformLocalBundleName不传入参数时，默认为false
        p2pClient.startRemoteApp(device.randomId, remoteBundleName).then((p2pResult) => {
          console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to start remote app. Code is ${error.code}, message is${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is${error.message}`);
}
```

### startRemoteApp

startRemoteApp(deviceRandomId: string, remoteApp: AppInfo, startConfig: StartConfig): Promise<P2pResult>

拉起对端设备的指定应用，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 在wearable中可正常调用，支持拉起Phone和Tablet设备中分布式组件或前台组件。HarmonyOS 6.1及以上版本，支持拉起[DISTRIBUTED\_SERVICE](wearengine_api.md#entrytype)组件；HarmonyOS 5.0之前版本（如HarmonyOS 2.x/3.x/4.x），支持拉起[SERVICE](wearengine_api.md#entrytype)组件；Android系统，支持拉起[SERVICE](wearengine_api.md#entrytype)组件。在其他系统和设备中不支持拉起。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| remoteApp | [AppInfo](wearengine_api.md#appinfo) | 是 | 待拉起的对端设备的应用信息。 |
| startConfig | [StartConfig](wearengine_api.md#startconfig) | 是 | 待拉起的对端设备应用的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象，返回[P2pResult](wearengine_api.md#p2presult)对象。  其属性中的code字段表示本次消息发送的结果。其中，返回203表示[entryName](wearengine_api.md#startconfig)不符合规范要求。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备，第一位即为目标设备且具备相关能力）
    let device: wearEngine.Device = devices[0];
    // 设置设备侧应用的应用信息：包名与指纹
    let remoteApp: wearEngine.AppInfo = {
      bundleName: 'example_bundleName',
      fingerprint: 'example_fingerprint'
    };

    // 设置拉起对端设备侧应用的组件类型
    let startConfig: wearEngine.StartConfig = {
      entryType: wearEngine.EntryType.DISTRIBUTED_SERVICE,
      entryName: 'example_entryName'
    };

    p2pClient.startRemoteApp(device.randomId, remoteApp, startConfig).then((p2pResult) => {
      console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to start remote app. Code is ${error.code}, message is${error.message}.`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is${error.message}`);
}
```

### sendMessage

sendMessage(deviceRandomId: string, appParam: P2pAppParam, message: P2pMessage): Promise<P2pResult>

向对端设备的指定应用发送消息，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 指定的设备侧应用参数。 |
| message | [P2pMessage](wearengine_api.md#p2pmessage) | 是 | 需要传输的消息内容，取值范围：[1，4096)，单位Byte。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象，返回[P2pResult](wearengine_api.md#p2presult)对象。  其属性中的code字段表示本次消息发送的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的消息内容
        let messageContent: string = 'this is message';
        let textEncoder: util.TextEncoder = new util.TextEncoder;
        let message: wearEngine.P2pMessage = {
          content: textEncoder.encodeInto(messageContent)
        }

        p2pClient.sendMessage(device.randomId, appParam, message).then((p2pResult) => {
          console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### transferFile

transferFile(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile, callback: AsyncCallback<P2pResult>): void

向对端设备的指定应用发送文件，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 指定的设备侧应用参数。 |
| file | [P2pFile](wearengine_api.md#p2pfile) | 是 | 需要传输的文件。 |
| callback | AsyncCallback<[P2pResult](wearengine_api.md#p2presult)> | 是 | 回调函数，向对端设备的指定应用发送文件成功，err为undefined，data为返回P2p通信的结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500011](errorcode-wearengine.md#section1008500011-无效文件) | File is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        let file: fileIo.File | null = null;
        try {
          // 设置需要发送的文件
          file = fileIo.openSync('');
          let p2pFile: wearEngine.P2pFile = {
            file: file
          }
          const closeFile = () => {
            try {
              if (file) {
                fileIo.closeSync(file);
                console.info('File closed successfully.');
              }
            } catch (closeErr) {
              console.error(`Failed to close file. Code is ${closeErr.code}, message is${closeErr.message}.`);
            }
          };

          p2pClient.transferFile(device.randomId, appParam, p2pFile,
            (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
              // callback处理逻辑
              if (error) {
                console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
                closeFile();
                return;
              }
              if (p2pResult.code) {
                if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
                  console.info(`Succeeded in transferring file, the result is ${p2pResult.code}.`);
                } else {
                  console.error(`Failed to transfer file, the error code is ${p2pResult.code}.`);
                }
                closeFile();
              }
              if (p2pResult.progress) {
                console.info(`Succeeded in transferring file, the progress is ${p2pResult.progress}.`);
              }
            });
          } catch (fileErr) {
            console.error(`Failed to open file. Code is ${fileErr.code}, message is${fileErr.message}`);
            if (file) fileIo.closeSync(file);
          }
        }
      } catch (error) {
        console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### cancelFileTransfer

cancelFileTransfer(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile): Promise<P2pResult>

取消向对端设备的指定应用发送文件，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 指定设备侧应用参数。 |
| file | [P2pFile](wearengine_api.md#p2pfile) | 是 | 需要传输的文件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象，返回P2p通信的结果。  属性中的code字段表示本次取消文件发送的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500011](errorcode-wearengine.md#section1008500011-无效文件) | File is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的文件信息
        let p2pFile: wearEngine.P2pFile = {
          file: fileIo.openSync('')
        }

        p2pClient.transferFile(device.randomId, appParam, p2pFile, () => {
          // 回调函数执行逻辑
        })

        p2pClient.cancelFileTransfer(device.randomId, appParam, p2pFile).then((p2pResult) => {
          if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
            console.info(`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.`);
          }
        }).catch((error: BusinessError) => {
          console.error(`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.`);
        })
        fileIo.close(p2pFile.file);
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### registerMessageReceiver

registerMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pMessage>): Promise<void>

订阅对端设备应用向本端设备发送消息的事件，接收到对端应用发送的消息时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 设备侧应用参数。 |
| callback | Callback<[P2pMessage](wearengine_api.md#p2pmessage)> | 是 | 回调函数，返回对端设备应用发送的消息。  接收到设备侧应用发送的消息后执行的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名
        }
        // 设置需要发送的消息
        let callback = (p2pMessage: wearEngine.P2pMessage) => {
          console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
        }

        p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
          console.info(`Succeeded in registering message receiver.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### registerFileReceiver

registerFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>

订阅对端设备向本端设备发送文件的事件，接收到对端设备发送的文件时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 设备侧应用参数。 |
| callback | Callback<[P2pFile](wearengine_api.md#p2pfile)> | 是 | 回调函数，返回对端设备应用发送的文件。  接收到设备侧应用发送的文件后执行的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的文件信息
        let callback = (p2pMessage: wearEngine.P2pFile) => {
          console.info(`Succeeded in receiving file.`);
        }

        p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
          console.info(`Succeeded in registering file receiver.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### registerFileReceiverWithProgress

registerFileReceiverWithProgress(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>

订阅对端设备向本端设备发送文件和文件传输进度的事件，接收到对端设备发送的文件和文件传输进度时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.1.1(24)及之前版本，本接口实际支持的设备类型范围(Phone、Tablet）小于其所属系统能力支持的设备类型范围（Phone、Tablet、Wearable)。因硬件能力限制，该接口在Wearable设备中无法使用该能力。 对于26.0.0及之后版本，本接口实际支持的设备类型范围与其所属系统能力支持的设备类型范围一致（Phone、Tablet、Wearable)。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 设备侧应用参数。 |
| callback | Callback<[P2pFile](wearengine_api.md#p2pfile)> | 是 | 回调函数，返回对端设备应用发送的文件类。  接收到设备侧应用发送的文件或者传输进度后执行的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的文件信息和传输进度
        let callback = (p2pMessage: wearEngine.P2pFile) => {
          if (!p2pMessage.file) {
            console.info(`progress is ${p2pMessage.progress}`);
          } else {
            console.info(`Succeeded in receiving file.`);
          }
        }

        p2pClient.registerFileReceiverWithProgress(device.randomId, appParam, callback).then(() => {
          console.info(`Succeeded in registering file receiver.`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### unregisterMessageReceiver

unregisterMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pMessage>): Promise<void>

取消订阅对端应用向本端应用发送消息的事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 设备侧应用参数。 |
| callback | Callback<[P2pMessage](wearengine_api.md#p2pmessage)> | 是 | 回调函数，返回对端设备应用发送的消息。  需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的消息
        let callback = (p2pMessage: wearEngine.P2pMessage) => {
          console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`);
        }

        p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
          console.info(`Succeeded in registering message receiver.`);

          p2pClient.unregisterMessageReceiver(device.randomId, appParam, callback).then(() => {
            console.info(`Succeeded in unregistering message receiver.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
          })
        }).catch((error: BusinessError) => {
          console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### unregisterFileReceiver

unregisterFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>

取消订阅对端应用向本端应用发送文件的事件，取消订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| appParam | [P2pAppParam](wearengine_api.md#p2pappparam) | 是 | 设备侧应用参数。 |
| callback | Callback<[P2pFile](wearengine_api.md#p2pfile)> | 是 | 回调函数，返回对端设备应用发送的文件。  需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());

try {
  let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  deviceList.forEach(async (device, idx) => {
    try {
      // 挑选支持应用安装的设备
      if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        // 设置设备侧应用的应用信息：包名与指纹
        // 包名与指纹，可在华为开发者联盟获取
        let appInfo: wearEngine.AppInfo = {
          bundleName: '',
          fingerprint: ''
        }
        // 将设备侧应用参数类定义为appParam
        let appParam: wearEngine.P2pAppParam = {
          remoteApp: appInfo
          // transformLocalAppInfo默认为false，不转换包名指纹
        }
        // 设置需要发送的文件信息
        let callback = (p2pMessage: wearEngine.P2pFile) => {
          console.info(`Succeeded in receiving file.`);
        }

        p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
          console.info(`Succeeded in registering file receiver.`);

          p2pClient.unregisterFileReceiver(device.randomId, appParam, callback).then(() => {
            console.info(`Succeeded in unregistering file receiver.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
          })
        }).catch((error: BusinessError) => {
          console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
        })
      }
    } catch (error) {
      console.error(`Failed to check device capability. Code is ${error.code}, message is ${error.message}.`);
    }

    if (idx === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  })
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

## AppInfo

设备侧应用信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用名称。 |
| fingerprint | string | 否 | 否 | 应用指纹，用于标识应用的唯一身份。  应用指纹获取请参考[如何获取应用指纹。](../harmonyos-guides/wearengine_faq-9.md#harmonyos-50及之后版本设备的应用) |

## P2pResultCode

存储P2p通信的返回值枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REMOTE\_APP\_NOT\_INSTALLED | 200 | 设备侧应用未安装。 |
| REMOTE\_APP\_NOT\_RUNNING | 201 | 设备侧应用未运行。 |
| REMOTE\_APP\_RUNNING | 202 | 设备侧应用运行中。 |
| UNKNOWN\_ERROR | 203 | 未知错误。 |
| COMMUNICATION\_FAILURE | 206 | 与设备侧应用通信失败。 |
| COMMUNICATION\_SUCCESS | 207 | 与设备侧应用通信成功。 |

## P2pResult

存储P2p通信的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 是 | 用于返回除文件传输外的P2p通信结果，返回值含义见[P2pResultCode](wearengine_api.md#p2presultcode)。 |
| progress | number | 否 | 是 | 仅用于上报文件传输进度，返回值范围：0-100。 |

## P2pMessage

本端设备应用向对端设备应用发送的消息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | Uint8Array | 否 | 否 | 传输消息的内容，格式为Uint8Array（二进制字节数组）类型数据。 |

## P2pFile

本端设备应用向对端设备应用发送的文件类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| file | [fs.File](js-apis-file-fs.md#file) | 否 | 否 | 文件对象。 |
| progress | number | 否 | 是 | 文件传输进度。  **起始版本：** 6.1.1(24) |

## P2pAppParam

P2p通信过程中可用的设备侧应用参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remoteApp | [AppInfo](wearengine_api.md#appinfo) | 否 | 否 | 设备侧应用信息类。 |
| transformLocalAppInfo | boolean | 否 | 是 | 是否需要将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。默认值：false。  true：转换；false：不转换。  待兼容应用设置请参考[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。 |

## StartConfig

待拉起的对端设备应用的配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entryType | [EntryType](wearengine_api.md#entrytype) | 否 | 否 | 需要拉起的对端设备应用的组件类型。 |
| entryName | string | 否 | 是 | 需要拉起对端设备（Phone/Tablet）应用的组件名称或全限定名称。  对端设备为HarmonyOS 6.1及以上版本时，该属性为组件名称，即"moduleName/abilityName"，如"entry/HiWearAbility"；对端设备为HarmonyOS 5.0之前版本（如HarmonyOS 2.x/3.x/4.x）时，该属性为全限定名称，即"包名.类名"，如"com.huawei.test.demo.FgService"。 |

## EntryType

待拉起的对端设备应用的组件类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISTRIBUTED\_SERVICE | 'DistributedService' | 分布式服务组件，当要启动分布式服务组件时需设置此值。 |
| SERVICE | 'Service' | 服务组件，当要拉起前台服务时需设置此值。 |
| UI | 'UI' | UI组件，当要启动UI组件时需要设置此值。 |

## wearEngine.getNotifyClient

getNotifyClient(context: common.Context): NotifyClient

用于获取Notify模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NotifyClient](wearengine_api.md#notifyclient) | 模板化通知客户端，存储了发送模板化通知的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting notify client`);
```

## NotifyClient

Notify客户端类，由[wearEngine.getNotifyClient](wearengine_api.md#wearenginegetnotifyclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### notify

notify(deviceRandomId: string, options: NotificationOptions): Promise<void>

向穿戴设备发送模板化通知，返回是否发送成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次查询的设备。 |
| options | [NotificationOptions](wearengine_api.md#notificationoptions) | 是 | 模板化通知配置参数类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    let button1: wearEngine.NotificationButton = {
      buttonId: wearEngine.ButtonId.FIRST_BUTTON,
      content: 'button_1'
    }
    let type1Notification: wearEngine.Notification = {
      type: wearEngine.NotificationType.NOTIFICATION_WITH_ONE_BUTTON,
      bundleName: 'bundleName',
      title: 'title',
      text: 'text',
      buttons: [button1]
    }
    let options: wearEngine.NotificationOptions = {
      notification: type1Notification,
      onAction: (feedback: wearEngine.NotificationFeedback) => {
        console.info(`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}`);
      }
    }

    notifyClient.notify(device.randomId, options).then(result => {
      console.info(`Succeeded in sending notification.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to send notification. Code is ${error.code}, message is ${error.message}`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

## NotificationOptions

模板化通知的配置参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notification | [Notification](wearengine_api.md#notification) | 否 | 否 | 模板化通知的通知体参数类。 |

### onAction

onAction(feedback: NotificationFeedback): void

设备侧对应用发出的通知做相关操作后执行的回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feedback | [NotificationFeedback](wearengine_api.md#notificationfeedback) | 是 | 设备侧操作通知的反馈类。 |

## Notification

模板化通知的通知体参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotificationType](wearengine_api.md#notificationtype) | 否 | 否 | 通知的模板类型。 |
| bundleName | string | 否 | 否 | 发送通知应用的包名，取值范围：[1，28]，单位Byte。 |
| title | string | 否 | 否 | 通知的标题，取值范围：[1，28)，单位Byte。 |
| text | string | 否 | 否 | 通知的内容，取值范围：[1，400)，单位Byte。 |
| buttons | [NotificationButton](wearengine_api.md#notificationbutton)[] | 否 | 是 | 通知按钮信息类，若未填写，默认为空。 |

## NotificationType

模板化通知的模板类型枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION\_WITHOUT\_BUTTONS | 50 | 没有按钮的通知类型。 |
| NOTIFICATION\_WITH\_ONE\_BUTTON | 51 | 拥有一个按钮的通知类型。 |
| NOTIFICATION\_WITH\_TWO\_BUTTONS | 52 | 拥有两个按钮的通知类型。 |
| NOTIFICATION\_WITH\_THREE\_BUTTONS | 53 | 拥有三个按钮的通知类型。 |

## NotificationButton

通知按钮信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttonId | [ButtonId](wearengine_api.md#buttonid) | 否 | 否 | 按钮Id枚举类。 |
| content | string | 否 | 否 | 按钮上的文字内容，取值范围：[1，12)，单位Byte。 |

## ButtonId

模板化通知的按钮Id枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRST\_BUTTON | 'firstButton' | 第一个按钮的Id。 |
| SECOND\_BUTTON | 'secondButton' | 第二个按钮的Id。 |
| THIRD\_BUTTON | 'thirdButton' | 第三个按钮的Id。 |

## NotificationFeedback

设备侧操作通知的反馈类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [NotificationAction](wearengine_api.md#notificationaction) | 否 | 是 | 设备侧对通知的操作反馈枚举类。 |
| errorCode | number | 否 | 是 | 错误码，含义请见[NotificationErrorCode](wearengine_api.md#notificationerrorcode)。 |

## NotificationAction

设备侧对通知的操作反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOTIFICATION\_SWITCHED\_TO\_BACKGROUND | 0 | 用户使用Home键退出或熄屏，通知退回后台。 |
| NOTIFICATION\_DELETED | 1 | 通知被用户删除。 |
| FIRST\_BUTTON\_CLICKED | 2 | 用户点击通知的第一个按钮。 |
| SECOND\_BUTTON\_CLICKED | 3 | 用户点击通知的第二个按钮。 |
| THIRD\_BUTTON\_CLICKED | 4 | 用户点击通知的第三个按钮。 |

## NotificationErrorCode

通知在设备侧发生错误的反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL\_ERROR | 255 | Wear Engine内部错误。通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。 |

## wearEngine.getSensorClient

getSensorClient(context: common.Context): SensorClient

用于获取Sensor模块的客户端。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md#context) | 是 | Context上下文，仅支持包含connectServiceExtensionAbility方法的Context（例：[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SensorClient](wearengine_api.md#sensorclient) | Sensor客户端，存储了Sensor模块的相关方法。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
console.info(`Succeeded in getting sensor client`);
```

## SensorClient

Sensor客户端类。由接口[wearEngine.getSensorClient](wearengine_api.md#wearenginegetsensorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### getSensorList

getSensorList(deviceRandomId: string): Promise<Sensor[]>

获取设备侧可用的传感器列表，返回对应的传感器列表，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Sensor](wearengine_api.md#sensor)[]> | Promise对象，返回设备侧可用的传感器列表。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备且第一位即为目标设备）
    let device: wearEngine.Device = devices[0];

    sensorClient.getSensorList(device.randomId).then((sensorList) => {
      console.info(`Succeeded in getting sensor list, result is ${sensorList}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
    })
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### subscribeSensor

subscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback<SensorResult>): Promise<void>

订阅指定的传感器数据上报，返回是否订阅成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| type | [SensorType](wearengine_api.md#sensortype) | 是 | 传感器类别，用于指定本次订阅的传感器。 |
| callback | Callback<[SensorResult](wearengine_api.md#sensorresult)> | 是 | 回调函数，返回传感器上报结果。  用于处理传感器上报的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备，第一位即为目标设备且具备相关能力）
    let device: wearEngine.Device = devices[0];
    try {
      let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
      sensorList.forEach((sensor) => {
        if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
          let callback = (sensorResult: wearEngine.SensorResult) => {
            console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
          }
          // 订阅加速度传感器数据上报
          sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
            console.info(`Succeeded in subscribing sensor data.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
          })
        }
      })
    } catch (error) {
      console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
    }
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

### unsubscribeSensor

unsubscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback<SensorResult>): Promise<void>

取消订阅指定的传感器数据上报，返回是否取消成功，使用Promise异步回调。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次取消订阅的设备。 |
| type | [SensorType](wearengine_api.md#sensortype) | 是 | 传感器类别，用于指定本次取消订阅的传感器。 |
| callback | Callback<[SensorResult](wearengine_api.md#sensorresult)> | 是 | 回调函数，返回传感器上报结果。  需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](errorcode-wearengine.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](errorcode-wearengine.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](errorcode-wearengine.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](errorcode-wearengine.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](errorcode-wearengine.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](errorcode-wearengine.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](errorcode-wearengine.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](errorcode-wearengine.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](errorcode-wearengine.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](errorcode-wearengine.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());

try {
  let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

  if (devices.length > 0) {
    // 从得到的设备列表中选取目标设备，并定义为device（假设数组中存在已连接设备，第一位即为目标设备且具备相关能力）
    let device: wearEngine.Device = devices[0];
    try {
      let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
      sensorList.forEach((sensor) => {
        if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
          let callback = (sensorResult: wearEngine.SensorResult) => {
            console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
          }
          // 订阅加速度传感器数据上报
          sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback)
            .then(() => {
              console.info(`Succeeded in subscribing sensor data.`);

              // 取消加速度传感器数据上报，注意传入的回调函数需与订阅时为同一对象
              sensorClient.unsubscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback)
                .then(() => {
                  console.info(`Succeeded in unsubscribing sensor data.`);
                })
                .catch((error: BusinessError) => {
                  console.error(`Failed to unsubscribe sensor data. Code is ${error.code}, message is ${error.message}`);
                })
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
            })
        }
      })
    } catch (error) {
      console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
    }
  }
} catch (error) {
  console.error(`Failed to get connected devices. Code is ${error.code}, message is ${error.message}`);
}
```

## SensorType

传感器类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ELECTROCARDIOGRAPHY | 0 | ECG（electrocardiograph）传感器。 |
| PHOTOPLETHYSMOGRAPHY | 1 | PPG（photoplethysmogram）传感器。 |
| ACCELEROMETER | 2 | 加速度传感器。 |
| GYROSCOPE | 3 | 陀螺仪传感器。 |
| MAGNETIC\_FIELD | 4 | 磁力传感器。 |
| HEART\_RATE | 6 | 心率传感器。 |

## Sensor

传感器信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 传感器名称。 |
| id | number | 否 | 否 | 传感器ID。 |
| type | [SensorType](wearengine_api.md#sensortype) | 否 | 否 | 传感器类型。 |
| accuracy | number | 否 | 是 | 传感器采样周期，单位ms。 |
| resolution | number | 否 | 是 | 传感器分辨率，当前仅作为Sensor对象的返回值信息。 |
| isUtcTimestampSupported | boolean | 否 | 否 | 传感器是否支持UTC（ Coordinated Universal Time）时间戳。true：支持，false：不支持。 |

## SensorData

传感器上报数据类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorType | [SensorType](wearengine_api.md#sensortype) | 否 | 否 | 传感器类型。 |
| data | number[] | 否 | 否 | 数据内容，格式及含义请参考[穿戴设备传感器数据格式及样例](../harmonyos-guides/device_sensor.md#穿戴设备传感器数据格式及样例)。 |
| channel | number | 否 | 是 | 传感器通道ID，为大于0的整数。 |
| timestamp | number | 否 | 是 | 计时时间戳，单位ms。 |
| utcTimestamp | number | 否 | 是 | UTC时间戳，单位ms。 |

## SensorErrorCode

传感器上报在设备侧发生错误的反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_NOT\_BEING\_WORN | 300 | 设备未佩戴。 |
| DEVICE\_LEAD\_OFF | 301 | 设备引线脱落。 |
| SENSOR\_TURNED\_OFF\_MANUALLY | 302 | 传感器被手动关闭。 |
| SENSOR\_OCCUPIED | 303 | 传感器被占用。 |
| SENSOR\_NOT\_SUPPORTED | 304 | 传感器不支持。 |

## SensorResult

传感器上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | [SensorData](wearengine_api.md#sensordata)[] | 否 | 是 | 传感器正常上报的数据内容。 |
| errorCode | number | 否 | 是 | 错误码，含义请见[SensorErrorCode](wearengine_api.md#sensorerrorcode)。 |

## on/off订阅事件

### wearEngine.on

on(type: 'serviceDie', callback: Callback<void>): void

订阅服务端消亡事件。使用callback异步回调。调用[wearEngine.destroy](wearengine_api.md#wearenginedestroy)接口主动发起的消亡事件不会触发执行回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie，表示服务端消亡事件。 |
| callback | Callback<void> | 是 | 回调函数，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008500012](errorcode-wearengine.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(`The service destruction event`);
}
try {
  wearEngine.on('serviceDie', callback);
  console.info(`Succeeded in subscribing the service destruction event.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to subscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
}
```

### wearEngine.off

off(type: 'serviceDie', callback?: Callback<void>): void

取消订阅服务端消亡事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie，表示服务端消亡事件。 |
| callback | Callback<void> | 否 | 回调函数，无返回结果。  需要同订阅监听时的回调函数为同一个对象。  当该参数为空时，会取消掉之前所有的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(`The service destruction event`);
}
wearEngine.on('serviceDie', callback);

try {
  wearEngine.off('serviceDie', callback);
  console.info(`Succeeded in unsubscribing the service destruction event.`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed to unsubscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
}
```

## wearEngine.destroy

destroy(): Promise<void>

主动销毁服务端，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](errorcode-wearengine.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008509999](errorcode-wearengine.md#section1008509999-内部错误) | Internal error. |

**示例：**

```typescript
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

wearEngine.destroy().then(() => {
  console.info(`Succeeded in destroying wear engine channel.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to destroy wear engine channel. Code is ${error.code}, message is ${error.message}.`);
})
```
