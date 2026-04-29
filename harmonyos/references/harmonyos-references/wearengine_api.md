---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearengine_api
title: wearEngine(穿戴设备能力开放)
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > ArkTS API > wearEngine(穿戴设备能力开放)
category: harmonyos-references
scraped_at: 2026-04-29T14:01:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5ba0d0637cd466fa06ab1c5853016bd0207d6704a9b34479b280739e054f9487
---

本模块提供手机与穿戴设备侧的交互能力。应用可调用模块内接口实现如下功能：

* 获取与当前设备已连接配对的设备列表、与对端设备互通消息互送文件等。
* 查询穿戴设备状态、向穿戴设备发送模板化通知、接收穿戴设备传感器的相关数据等。

说明

针对系统能力SystemCapability.Health.WearEngine，请先使用[canIUse()](js-apis-syscap.md#caniuse)接口判断当前设备是否支持此syscap及对应接口。

**起始版本**：5.0.0(12)

## 导入模块

PhoneTabletWearable

```
1. import { wearEngine } from '@kit.WearEngine';
```

## wearEngine.getAuthClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting auth client`);
```

## AuthClient

PhoneTabletWearable

权限管理客户端类，由[wearEngine.getAuthClient](wearengine_api.md#wearenginegetauthclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### requestAuthorization

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

6. let request: wearEngine.AuthorizationRequest = {
7. permissions: [wearEngine.Permission.USER_STATUS]
8. }

10. authClient.requestAuthorization(request).then(result => {
11. console.info(`Succeeded in requesting authorize, authorized permissions is ${result.permissions}`);
12. }).catch((error: BusinessError) => {
13. console.error(`Failed to request authorize. Code is ${error.code}, message is ${error.message}`);
14. })
```

### getAuthorization

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

6. authClient.getAuthorization().then(result => {
7. console.info(`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}`);
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}`);
10. })
```

## AuthorizationBase

PhoneTabletWearable

权限控制模块输入输出的基类。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| permissions | [Permission](wearengine_api.md#permission)[] | 否 | 否 | 权限枚举类型的数组。 |

## Permission

PhoneTabletWearable

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

PhoneTabletWearable

权限请求类，继承自[AuthorizationBase](wearengine_api.md#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

## AuthorizationResponse

PhoneTabletWearable

权限响应类，继承自[AuthorizationBase](wearengine_api.md#authorizationbase)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

## wearEngine.getDeviceClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting device client.`);
```

## DeviceClient

PhoneTabletWearable

Device客户端类。由接口[wearEngine.getDeviceClient](wearengine_api.md#wearenginegetdeviceclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### getConnectedDevices

PhoneTabletWearable

getConnectedDevices(): Promise<Device[]>

获取当前已连接且支持wearEngine能力集的设备。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Device](wearengine_api.md#device)[]> | Promise对象，返回设备列表。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. deviceClient.getConnectedDevices().then((devices) => {
6. console.info(`Succeeded in getting devices, devices number is ${devices.length}.`);
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to get devices. Code is ${error.code}, message is ${error.message}.`);
9. })
```

## Device

PhoneTabletWearable

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

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

7. if (devices.length > 0) {
8. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
9. let device: wearEngine.Device = devices[0];

11. device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P_COMMUNICATION).then((isSupportP2P) => {
12. console.info(`Succeeded in checking p2p capability, result is ${isSupportP2P}`);
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}`);
15. })
16. }
```

### isDeviceCapabilitySupported

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

7. if (devices.length > 0) {
8. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
9. let device: wearEngine.Device = devices[0];

11. device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.CBT_I).then((isSupportCBTI) => {
12. console.info(`Succeeded in checking CBTI capability, result is ${isSupportCBTI}`);
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to check CBTI capability. Code is ${error.code}, message is ${error.message}`);
15. })
16. }
```

### getSerialNumber

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

7. if (devices.length > 0) {
8. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
9. let device: wearEngine.Device = devices[0];

11. device.getSerialNumber().then((sn) => {
12. console.info(`Succeeded in getting device SN, result is ${sn}`);
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to get device SN. Code is ${error.code}, message is ${error.message}`);
15. })
16. }
```

## WearEngineCapability

PhoneTabletWearable

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

PhoneTabletWearable

Device能力集枚举类型。

**系统能力：** SystemCapability.Health.WearEngine

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP\_INSTALLATION | 14 | 支持应用安装能力。 |
| CBT\_I | 128 | CBTI数字疗法能力。 |

## DeviceCategory

PhoneTabletWearable

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

PhoneTabletWearable

设备的操作系统类型枚举类。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在wearable中正常调用，在其他设备类型中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HARMONYOS | 1 | HarmonyOS |
| IOS | 2 | IOS |
| OTHER\_OS | 255 | 其他类型 |

## wearEngine.getMonitorClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting monitor client.`);
```

## MonitorClient

PhoneTabletWearable

Monitor客户端类。由接口[wearEngine.getMonitorClient](wearengine_api.md#wearenginegetmonitorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### queryStatus

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
10. let device: wearEngine.Device = devices[0];

12. monitorClient.queryStatus(device.randomId, wearEngine.MonitorItem.WEAR_STATUS).then((result) => {
13. console.info(`Succeeded in querying wear status, result is ${result.code}.`);
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to query wear status. Code is ${error.code}, message is ${error.message}.`);
16. })
17. }
```

### subscribeEvent

PhoneTabletWearable

subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>

监听指定设备的指定状态变化事件，当状态发生变化时使用callback异步回调，订阅成功与否使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用，在其他设备类型中无法使用该能力。对于6.1.0(23)及之后版本，该接口在Phone、Tablet中可正常调用，在Wearable中可以订阅设备连接状态变化事件，订阅其他事件返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| type | [MonitorEvent](wearengine_api.md#monitorevent) | 是 | 可订阅的设备状态枚举，用于指定本次订阅监听的设备状态。 |
| callback | Callback<[MonitorEventData](wearengine_api.md#monitoreventdata)> | 是 | 回调函数，状态发生变化后执行，传入[MonitorEventData](wearengine_api.md#monitoreventdata)类。建议保证回调函数的生命周期延长至取消监听时，详情请见[unsubscribeEvent](wearengine_api.md#unsubscribeevent)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](wearengine_api_error_code.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
10. let device: wearEngine.Device = devices[0];

12. let callback = (monitorEventData: wearEngine.MonitorEventData) => {
13. console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`)
14. }
15. monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
16. console.info(`Succeeded in subscribing wear status.`);
17. }).catch((error: BusinessError) => {
18. console.error(`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.`);
19. })
20. }
```

### unsubscribeEvent

PhoneTabletWearable

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
| callback | Callback<[MonitorEventData](wearengine_api.md#monitoreventdata)> | 是 | 回调函数。此处需保证传入的对象与调用[subscribeEvent](wearengine_api.md#subscribeevent)接口时传入的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();
6. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
10. let device: wearEngine.Device = devices[0];

12. // 解注册时回调函数需要保证和注册时为同一个对象
13. let callback = (monitorEventData: wearEngine.MonitorEventData) => {
14. console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`)
15. }
16. // 创建待删除的订阅任务
17. await monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback);
18. // 删除之前创建的订阅任务
19. monitorClient.unsubscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
20. console.info(`Succeeded in unsubscribing wear status`);
21. }).catch((error: BusinessError) => {
22. console.error(`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.`);
23. })
24. }
```

## MonitorItem

PhoneTabletWearable

设备状态的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WEAR\_STATUS | wearStatus | 佩戴状态。返回值含义：  1：佩戴  2：未佩戴 |
| POWER\_STATUS | powerStatus | 电量状态。返回值含义：剩余电量百分比（0~100）。 |
| CHARGE\_STATUS | chargeStatus | 充电状态。返回值含义：  1：正在充电  2：未充电  3：电量已充满 |
| AVAILABLE\_STORAGE\_SPACE | availableStorageSpace | 可用存储空间。返回值含义：用户可用空间（KB）。 |
| POWER\_MODE | powerMode | 电源模式。返回值含义：  -1：设备不区分电源模式  0：智能模式  1：超长续航模式 |

## MonitorEvent

PhoneTabletWearable

设备状态变化事件的枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EVENT\_CONNECTION\_STATUS\_CHANGED | connectionStatus | 设备连接状态变化。  返回值含义：2：连接成功；3：连接断开；5：设备解绑 |
| EVENT\_BATTERY\_LEVEL\_DROPPED | lowPower | 设备电量降低。  返回值含义：剩余电量百分比（0~100）。 |
| EVENT\_WEAR\_STATUS\_CHANGED | wearStatus | 设备佩戴状态变化。  返回值含义：1：佩戴，2：未佩戴。 |
| EVENT\_HEART\_RATE\_ALARM | heartRateAlarm | 心率告警。  返回值含义：1：静态心率过高，2：静态心率过低，3：运动心率过高，4：运动心率过低。 |
| EVENT\_CHARGE\_STATUS\_CHANGED | chargeStatus | 充电状态变化。  返回值含义：1：充电开始，2：充电结束，3：充电完成。 |
| EVENT\_POWER\_MODE\_CHANGED | powerMode | 电源模式切换。  返回值含义：0：切换至智能模式，1：切换至超长续航模式。 |

## MonitorData

PhoneTabletWearable

作为[queryStatus](wearengine_api.md#querystatus)接口的返回值与[subscribeEvent](wearengine_api.md#subscribeevent)接口回调函数的入参，返回设备的状态信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 当使用[queryStatus](wearengine_api.md#querystatus)接口查询设备状态时，返回值含义请见[MonitorItem](wearengine_api.md#monitoritem)。  当使用[subscribeEvent](wearengine_api.md#subscribeevent)接口订阅监听时，返回值含义请见[MonitorEvent](wearengine_api.md#monitorevent)。 |
| data | string | 否 | 是 | 扩展字段。 |

## MonitorEventData

PhoneTabletWearable

作为[subscribeEvent](wearengine_api.md#subscribeevent)接口的返回值，当订阅监听的事件触发时，作为入参将设备对应状态变化后的信息传递给回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | [MonitorEvent](wearengine_api.md#monitorevent) | 否 | 否 | 回调函数注册的订阅监听事件枚举值。 |
| data | [MonitorData](wearengine_api.md#monitordata) | 否 | 否 | 设备状态发生变化后的状态信息。 |

## wearEngine.getP2pClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting p2p client.`);
```

## P2pClient

PhoneTabletWearable

P2p客户端类。由接口[wearEngine.getP2pClient](wearengine_api.md#wearenginegetp2pclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### isRemoteAppInstalled

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 将设备侧应用包名定义为remoteBundleName
12. let remoteBundleName: string = '';

14. p2pClient.isRemoteAppInstalled(device.randomId, remoteBundleName).then((isInstall) => {
15. console.info(`Succeeded in checking remote app install, result is ${isInstall}.`);
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.`);
18. })
19. }
20. if (idx === deviceList.length - 1) {
21. // 若不存在目标设备则抛出错误
22. throw new Error('cannot find target device');
23. }
24. })
```

### getRemoteAppVersion

PhoneTabletWearable

getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise<number>

获取穿戴设备指定应用的版本号，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceRandomId | string | 是 | [Device](wearengine_api.md#device)的随机标识符，用于指定本次订阅的设备。 |
| remoteBundleName | string | 是 | 待查询版本号的设备侧应用名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。表示设备侧应用的版本号。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 将设备侧应用包名定义为remoteBundleName
12. let remoteBundleName: string = '';

14. p2pClient.getRemoteAppVersion(device.randomId, remoteBundleName).then((version) => {
15. console.info(`Succeeded in getting remote app version, version is ${version}.`);
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.`);
18. })
19. }
20. if (idx === deviceList.length - 1) {
21. // 若不存在目标设备则抛出错误
22. throw new Error('cannot find target device');
23. }
24. })
```

### startRemoteApp

PhoneTabletWearable

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
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象。属性中的code字段表示本次拉起应用的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 将设备侧应用包名定义为remoteBundleName
12. let remoteBundleName: string = '';

14. // transformLocalBundleName不传入参数时，默认为false
15. p2pClient.startRemoteApp(device.randomId, remoteBundleName).then((p2pResult) => {
16. console.info(`Succeeded in starting remote app, result is ${p2pResult.code}.`);
17. }).catch((error: BusinessError) => {
18. console.error(`Failed to start remote app. Code is ${error.code}, message is ${error.message}.`);
19. })
20. }
21. if (idx === deviceList.length - 1) {
22. // 若不存在目标设备则抛出错误
23. throw new Error('cannot find target device');
24. }
25. })
```

### sendMessage

PhoneTabletWearable

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
| message | [P2pMessage](wearengine_api.md#p2pmessage) | 是 | 需要传输的消息内容，取值范围：[1，4096)，单位字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象。返回[P2pResult](wearengine_api.md#p2presult)对象，其属性中的code字段表示本次消息发送的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';

5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
7. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

9. deviceList.forEach(async (device, idx, arr) => {
10. // 挑选支持应用安装的设备
11. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
12. // 设置设备侧应用的应用信息：包名与指纹
13. let appInfo: wearEngine.AppInfo = {
14. bundleName: '',
15. fingerprint: ''
16. }
17. // 将设备侧应用参数类定义为appParam
18. let appParam: wearEngine.P2pAppParam = {
19. remoteApp: appInfo
20. // transformLocalAppInfo默认为false，不转换包名指纹
21. }

23. // 设置需要发送的消息内容
24. let messageContent: string = 'this is message';
25. let textEncoder: util.TextEncoder = new util.TextEncoder;
26. let message: wearEngine.P2pMessage = {
27. content: textEncoder.encodeInto(messageContent)
28. }

30. p2pClient.sendMessage(device.randomId, appParam, message).then((p2pResult) => {
31. console.info(`Succeeded in sending message, result is ${p2pResult.code}.`);
32. }).catch((error: BusinessError) => {
33. console.error(`Failed to send message. Code is ${error.code}, message is ${error.message}.`);
34. })
35. }
36. if (idx === deviceList.length - 1) {
37. // 若不存在目标设备则抛出错误
38. throw new Error('cannot find target device');
39. }
40. })
```

### transferFile

PhoneTabletWearable

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
| callback | AsyncCallback<[P2pResult](wearengine_api.md#p2presult)> | 是 | 通用回调函数，携带错误参数和异步返回值。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500011](wearengine_api_error_code.md#section1008500011-无效文件) | File is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';

5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
7. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

9. deviceList.forEach(async (device, idx, arr) => {
10. // 挑选支持应用安装的设备
11. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
12. // 设置设备侧应用的应用信息：包名与指纹
13. let appInfo: wearEngine.AppInfo = {
14. bundleName: '',
15. fingerprint: ''
16. }
17. // 将设备侧应用参数类定义为appParam
18. let appParam: wearEngine.P2pAppParam = {
19. remoteApp: appInfo
20. // transformLocalAppInfo默认为false，不转换包名指纹
21. }
22. // 设置需要发送的文件
23. let p2pFile: wearEngine.P2pFile = {
24. file: fileIo.openSync('')
25. }

27. p2pClient.transferFile(device.randomId, appParam, p2pFile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
28. // callback处理逻辑
29. if (error) {
30. console.error(`Failed to transfer file. Code is ${error.code}, message is ${error.message}.`);
31. return;
32. }
33. if (p2pResult.code) {
34. if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
35. console.info(`Succeeded in transfering file, the result is ${p2pResult.code}.`);
36. }
37. console.info(`Failed to transfer file, the error code is ${p2pResult.code}.`);
38. }
39. if (p2pResult.progress) {
40. console.info(`Succeeded in transfering file, the progress is ${p2pResult.progress}.`);
41. }
42. });
43. fileIo.close(p2pFile.file);
44. }
45. if (idx === deviceList.length - 1) {
46. // 若不存在目标设备则抛出错误
47. throw new Error('cannot find target device');
48. }
49. })
```

### cancelFileTransfer

PhoneTabletWearable

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
| Promise<[P2pResult](wearengine_api.md#p2presult)> | Promise对象。属性中的code字段表示本次取消文件发送的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500011](wearengine_api_error_code.md#section1008500011-无效文件) | File is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';

5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
7. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

9. deviceList.forEach(async (device, idx, arr) => {
10. // 挑选支持应用安装的设备
11. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
12. // 设置设备侧应用的应用信息：包名与指纹
13. let appInfo: wearEngine.AppInfo = {
14. bundleName: '',
15. fingerprint: ''
16. }
17. // 将设备侧应用参数类定义为appParam
18. let appParam: wearEngine.P2pAppParam = {
19. remoteApp: appInfo
20. // transformLocalAppInfo默认为false，不转换包名指纹
21. }
22. // 设置需要发送的文件信息
23. let p2pFile: wearEngine.P2pFile = {
24. file: fileIo.openSync('')
25. }

27. p2pClient.transferFile(device.randomId, appParam, p2pFile, () => {
28. // 回调函数执行逻辑
29. })

31. p2pClient.cancelFileTransfer(device.randomId, appParam, p2pFile).then((p2pResult) => {
32. if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION_SUCCESS) {
33. console.info(`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.`);
34. }
35. }).catch((error: BusinessError) => {
36. console.error(`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.`);
37. })
38. fileIo.close(p2pFile.file);
39. }
40. if (idx === deviceList.length - 1) {
41. // 若不存在目标设备则抛出错误
42. throw new Error('cannot find target device');
43. }
44. })
```

### registerMessageReceiver

PhoneTabletWearable

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
| callback | Callback<[P2pMessage](wearengine_api.md#p2pmessage)> | 是 | 接收到设备侧应用发送的消息后执行的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](wearengine_api_error_code.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 设置设备侧应用的应用信息：包名与指纹
12. let appInfo: wearEngine.AppInfo = {
13. bundleName: '',
14. fingerprint: ''
15. }
16. // 将设备侧应用参数类定义为appParam
17. let appParam: wearEngine.P2pAppParam = {
18. remoteApp: appInfo
19. // transformLocalAppInfo默认为false，不转换包名
20. }
21. // 设置需要发送的文件信息
22. let callback = (p2pMessage: wearEngine.P2pMessage) => {
23. console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`)
24. }

26. p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
27. console.info(`Succeeded in registering message receiver.`);
28. }).catch((error: BusinessError) => {
29. console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
30. })
31. }
32. if (idx === deviceList.length - 1) {
33. // 若不存在目标设备则抛出错误
34. throw new Error('cannot find target device');
35. }
36. })
```

### registerFileReceiver

PhoneTabletWearable

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
| callback | Callback<[P2pFile](wearengine_api.md#p2pfile)> | 是 | 接收到设备侧应用发送的文件后执行的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](wearengine_api_error_code.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 设置设备侧应用的应用信息：包名与指纹
12. let appInfo: wearEngine.AppInfo = {
13. bundleName: '',
14. fingerprint: ''
15. }
16. // 将设备侧应用参数类定义为appParam
17. let appParam: wearEngine.P2pAppParam = {
18. remoteApp: appInfo
19. // transformLocalAppInfo默认为false，不转换包名指纹
20. }
21. // 设置需要发送的文件信息
22. let callback = (p2pMessage: wearEngine.P2pFile) => {
23. console.info(`Succeeded in receiving file.`)
24. }

26. p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
27. console.info(`Succeeded in registering file receiver.`)
28. }).catch((error: BusinessError) => {
29. console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
30. })
31. }
32. if (idx === deviceList.length - 1) {
33. // 若不存在目标设备则抛出错误
34. throw new Error('cannot find target device');
35. }
36. })
```

### unregisterMessageReceiver

PhoneTabletWearable

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
| callback | Callback<[P2pMessage](wearengine_api.md#p2pmessage)> | 是 | 回调函数，需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 设置设备侧应用的应用信息：包名与指纹
12. let appInfo: wearEngine.AppInfo = {
13. bundleName: '',
14. fingerprint: ''
15. }
16. // 将设备侧应用参数类定义为appParam
17. let appParam: wearEngine.P2pAppParam = {
18. remoteApp: appInfo
19. // transformLocalAppInfo默认为false，不转换包名指纹
20. }
21. // 设置需要发送的文件信息
22. let callback = (p2pMessage: wearEngine.P2pMessage) => {
23. console.info(`Succeeded in receiving message, the message is ${p2pMessage.content}.`)
24. }

26. p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
27. console.info(`Succeeded in registering message receiver.`)
28. }).catch((error: BusinessError) => {
29. console.error(`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.`);
30. })

32. p2pClient.unregisterMessageReceiver(device.randomId, appParam, callback).then(() => {
33. console.info(`Succeeded in unregistering message receiver.`)
34. }).catch((error: BusinessError) => {
35. console.error(`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.`);
36. })
37. }
38. if (idx === deviceList.length - 1) {
39. // 若不存在目标设备则抛出错误
40. throw new Error('cannot find target device');
41. }
42. })
```

### unregisterFileReceiver

PhoneTabletWearable

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
| callback | Callback<[P2pFile](wearengine_api.md#p2pfile)> | 是 | 回调函数，需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
5. let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
6. let deviceList: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. deviceList.forEach(async (device, idx, arr) => {
9. // 挑选支持应用安装的设备
10. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
11. // 设置设备侧应用的应用信息：包名与指纹
12. let appInfo: wearEngine.AppInfo = {
13. bundleName: '',
14. fingerprint: ''
15. }
16. // 将设备侧应用参数类定义为appParam
17. let appParam: wearEngine.P2pAppParam = {
18. remoteApp: appInfo
19. // transformLocalAppInfo默认为false，不转换包名指纹
20. }
21. // 设置需要发送的文件信息
22. let callback = (p2pMessage: wearEngine.P2pFile) => {
23. console.info(`Succeeded in receiving file.`)
24. }

26. p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
27. console.info(`Succeeded in registering file receiver.`);
28. }).catch((error: BusinessError) => {
29. console.error(`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.`);
30. })

32. p2pClient.unregisterFileReceiver(device.randomId, appParam, callback).then(() => {
33. console.info(`Succeeded in unregistering file receiver.`);
34. }).catch((error: BusinessError) => {
35. console.error(`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.`);
36. })
37. }
38. if (idx === deviceList.length - 1) {
39. // 若不存在目标设备则抛出错误
40. throw new Error('cannot find target device');
41. }
42. })
```

## AppInfo

PhoneTabletWearable

设备侧应用信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用名称。 |
| fingerprint | string | 否 | 否 | [应用指纹，用于标识应用的唯一身份。](../harmonyos-guides/wearengine_faq-9.md) |

## P2pResultCode

PhoneTabletWearable

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

PhoneTabletWearable

存储P2p通信的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 是 | 用于返回除文件传输外的P2p通信结果，返回值含义见[P2pResultCode](wearengine_api.md#p2presultcode)。 |
| progress | number | 否 | 是 | 仅用于上报文件传输进度，返回值范围：0-100。 |

## P2pMessage

PhoneTabletWearable

本端设备应用向对端设备应用发送的消息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | Uint8Array | 否 | 否 | 传输消息的内容，格式为Uint8Array（二进制字节数组）类型数据。 |

## P2pFile

PhoneTabletWearable

本端设备应用向对端设备应用发送的文件类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| file | [fs.File](js-apis-file-fs.md#file) | 否 | 否 | 文件对象。 |

## P2pAppParam

PhoneTabletWearable

P2p通信过程中可用的设备侧应用参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| remoteApp | [AppInfo](wearengine_api.md#appinfo) | 否 | 否 | 设备侧应用信息类。 |
| transformLocalAppInfo | boolean | 否 | 是 | 是否需要将本地包名和指纹转换为兼容应用在云端存储的包名和指纹。默认值：false。  true：转换；false：不转换。  待兼容应用设置请参考[申请接入Wear Engine服务](../harmonyos-guides/wearengine_apply.md)。 |

## wearEngine.getNotifyClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting notify client`);
```

## NotifyClient

PhoneTabletWearable

Notify客户端类，由[wearEngine.getNotifyClient](wearengine_api.md#wearenginegetnotifyclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### notify

PhoneTabletWearable

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
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
10. let device: wearEngine.Device = devices[0];

12. let button1: wearEngine.NotificationButton = {
13. buttonId: wearEngine.ButtonId.FIRST_BUTTON,
14. content: 'button_1'
15. }
16. let type1Notification: wearEngine.Notification = {
17. type: wearEngine.NotificationType.NOTIFICATION_WITH_ONE_BUTTON,
18. bundleName: 'bundleName',
19. title: 'title',
20. text: 'text',
21. buttons: [button1]
22. }
23. let options: wearEngine.NotificationOptions = {
24. notification: type1Notification,
25. onAction: (feedback: wearEngine.NotificationFeedback) => {
26. console.info(`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}`);
27. }
28. }

30. notifyClient.notify(device.randomId, options).then(result => {
31. console.info(`Succeeded in sending notification.`);
32. }).catch((error: BusinessError) => {
33. console.error(`Failed to send notification. Code is ${error.code}, message is ${error.message}`);
34. })
35. }
```

## NotificationOptions

PhoneTabletWearable

模板化通知的配置参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notification | [Notification](wearengine_api.md#notification) | 否 | 否 | 模板化通知的通知体参数类。 |

### onAction

PhoneTabletWearable

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

PhoneTabletWearable

模板化通知的通知体参数类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [NotificationType](wearengine_api.md#notificationtype) | 否 | 否 | 通知的模板类型。 |
| bundleName | string | 否 | 否 | 发送通知应用的包名。 |
| title | string | 否 | 否 | 通知的标题，取值范围：[1，28)，单位字节。 |
| text | string | 否 | 否 | 通知的内容，取值范围：[1，400)，单位字节。 |
| buttons | [NotificationButton](wearengine_api.md#notificationbutton)[] | 否 | 是 | 通知按钮信息类，若未填写，默认为空。 |

## NotificationType

PhoneTabletWearable

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

PhoneTabletWearable

通知按钮信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| buttonId | [ButtonId](wearengine_api.md#buttonid) | 否 | 否 | 按钮Id枚举类。 |
| content | string | 否 | 否 | 按钮上的文字内容，取值范围：[1，12)，单位字节。 |

## ButtonId

PhoneTabletWearable

模板化通知的按钮Id枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRST\_BUTTON | firstButton | 第一个按钮的Id。 |
| SECOND\_BUTTON | secondButton | 第二个按钮的Id。 |
| THIRD\_BUTTON | thirdButton | 第三个按钮的Id。 |

## NotificationFeedback

PhoneTabletWearable

设备侧操作通知的反馈类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [NotificationAction](wearengine_api.md#notificationaction) | 否 | 是 | 设备侧对通知的操作反馈枚举类。 |
| errorCode | number | 否 | 是 | 错误码，含义请见[NotificationErrorCode](wearengine_api.md#notificationerrorcode)。 |

## NotificationAction

PhoneTabletWearable

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

PhoneTabletWearable

通知在设备侧发生错误的反馈枚举类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL\_ERROR | 255 | Wear Engine内部错误。通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。 |

## wearEngine.getSensorClient

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';

3. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
4. console.info(`Succeeded in getting sensor client`);
```

## SensorClient

PhoneTabletWearable

Sensor客户端类。由接口[wearEngine.getSensorClient](wearengine_api.md#wearenginegetsensorclient)返回得到。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

### getSensorList

PhoneTabletWearable

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

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
10. let device: wearEngine.Device = devices[0];

12. sensorClient.getSensorList(device.randomId).then((sensorList) => {
13. console.info(`Succeeded in getting sensor list, result is ${sensorList}`);
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
16. })
17. }
```

### subscribeSensor

PhoneTabletWearable

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
| callback | Callback<[SensorResult](wearengine_api.md#sensorresult)> | 是 | 回调函数，用于处理传感器上报的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008500012](wearengine_api_error_code.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备,第一位即为目标设备且具备相关能力)
10. let device: wearEngine.Device = devices[0];
11. let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
12. sensorList.forEach((sensor, idx, arr) => {
13. if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
14. let callback = (sensorResult: wearEngine.SensorResult) => {
15. console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
16. }
17. // 订阅加速度传感器数据上报
18. sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
19. console.info(`Succeeded in subscribing sensor data.`);
20. }).catch((error: BusinessError) => {
21. console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
22. })
23. }
24. })
25. }
```

### unsubscribeSensor

PhoneTabletWearable

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
| callback | Callback<[SensorResult](wearengine_api.md#sensorresult)> | 是 | 回调函数，用于处理传感器上报的数据，需要同订阅监听时的回调函数为同一个对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1008500001](wearengine_api_error_code.md#section1008500001-网络错误) | Network error. The network is unavailable. |
| [1008500002](wearengine_api_error_code.md#section1008500002-无绑定设备) | No device is bound. |
| [1008500003](wearengine_api_error_code.md#section1008500003-设备未连接) | Device disconnected. |
| [1008500004](wearengine_api_error_code.md#section1008500004-应用未申请wear-engine服务) | App has not applied for the Wear Engine service. |
| [1008500005](wearengine_api_error_code.md#section1008500005-用户未授权) | The HUAWEI ID is not authorized. |
| [1008500006](wearengine_api_error_code.md#section1008500006-用户未同意隐私授权) | User privacy is not agreed. |
| [1008500007](wearengine_api_error_code.md#section1008500007-穿戴设备侧能力不支持) | The device capability is not supported. |
| [1008500008](wearengine_api_error_code.md#section1008500008-账号未登录) | Account error. The user has not logged in with HUAWEI ID. |
| [1008500009](wearengine_api_error_code.md#section1008500009-账号异常) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1008500010](wearengine_api_error_code.md#section1008500010-无效设备id) | Device ID is invalid. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
5. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
6. let devices: wearEngine.Device[] = await deviceClient.getConnectedDevices();

8. if (devices.length > 0) {
9. // 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备,第一位即为目标设备且具备相关能力)
10. let device: wearEngine.Device = devices[0];
11. let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(device.randomId);
12. sensorList.forEach((sensor, idx, arr) => {
13. if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
14. let callback = (sensorResult: wearEngine.SensorResult) => {
15. console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
16. }
17. // 订阅加速度传感器数据上报
18. sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
19. console.info(`Succeeded in subscribing sensor data.`);
20. }).catch((error: BusinessError) => {
21. console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
22. })
23. // 取消加速度传感器数据上报, 注意传入的回调函数需与订阅时为同一对象
24. sensorClient.unsubscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
25. console.info(`Succeeded in unsubscribing sensor data.`);
26. }).catch((error: BusinessError) => {
27. console.error(`Failed to unsubscribe sensor data. Code is ${error.code}, message is ${error.message}`);
28. })
29. }
30. })
31. }
```

## SensorType

PhoneTabletWearable

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

PhoneTabletWearable

传感器信息类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 传感器名称。 |
| id | number | 否 | 否 | 传感器ID。 |
| type | [SensorType](wearengine_api.md#sensortype) | 否 | 否 | 传感器类型。 |
| accuracy | number | 否 | 是 | 传感器采样周期，单位毫秒。 |
| resolution | number | 否 | 是 | 传感器分辨率，当前仅作为Sensor对象的返回值信息。 |
| isUtcTimestampSupported | boolean | 否 | 否 | 传感器是否支持UTC（ Coordinated Universal Time）时间戳。true：支持，false：不支持。 |

## SensorData

PhoneTabletWearable

传感器上报数据类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorType | [SensorType](wearengine_api.md#sensortype) | 否 | 否 | 传感器类型。 |
| data | number[] | 否 | 否 | 数据内容，格式及含义请参考[穿戴设备传感器数据格式及样例](../harmonyos-guides/device_sensor.md#穿戴设备传感器数据格式及样例)。 |
| channel | number | 否 | 是 | 传感器通道ID，为大于0的整数。 |
| timestamp | number | 否 | 是 | 计时时间戳。 |
| utcTimestamp | number | 否 | 是 | UTC时间戳。 |

## SensorErrorCode

PhoneTabletWearable

传感器类型。

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

PhoneTabletWearable

传感器上报结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | [SensorData](wearengine_api.md#sensordata)[] | 否 | 是 | 传感器正常上报的数据内容。 |
| errorCode | number | 否 | 是 | 错误码，含义请见[SensorErrorCode](wearengine_api.md#sensorerrorcode)。 |

## on/off订阅事件

PhoneTabletWearable

### wearEngine.on

PhoneTabletWearable

on(type: 'serviceDie', callback: Callback<void>): void

订阅服务端消亡事件，调用[wearEngine.destroy](wearengine_api.md#wearenginedestroy)接口主动发起的消亡事件不会触发执行回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie(服务端消亡事件)。 |
| callback | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008500012](wearengine_api_error_code.md#section1008500012-回调函数过多) | Too many callbacks of the same type. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callback = () => {
5. console.info(`The service destruction event`);
6. }
7. try {
8. wearEngine.on('serviceDie', callback);
9. console.info(`Succeeded in subscribing the service destruction event.`);
10. } catch (error) {
11. const err: BusinessError = error as BusinessError;
12. console.error(`Failed to subscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
13. }
```

### wearEngine.off

PhoneTabletWearable

off(type: 'serviceDie', callback?: Callback<void>): void

取消订阅服务端消亡事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，仅支持serviceDie(服务端消亡事件)。 |
| callback | Callback<void> | 否 | 回调函数，需要同订阅监听时的回调函数为同一个对象。  当该参数为空时，会取消掉之前所有的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callback = () => {
5. console.info(`The service destruction event`);
6. }
7. wearEngine.on('serviceDie', callback);

9. try {
10. wearEngine.off('serviceDie', callback);
11. console.info(`Succeeded in unsubscribing the service destruction event.`);
12. } catch (error) {
13. const err: BusinessError = error as BusinessError;
14. console.error(`Failed to unsubscribe the service destruction event. Code is ${err.code}, message is ${err.message}.`);
15. }
```

## wearEngine.destroy

PhoneTabletWearable

destroy(): Promise<void>

主动销毁服务端，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Health.WearEngine

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Wear Engine ArkTS API错误码](wearengine_api_error_code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1008509999](wearengine_api_error_code.md#section1008509999-内部错误) | Internal error. |

**示例：**

```
1. import { wearEngine } from '@kit.WearEngine';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. wearEngine.destroy().then(() => {
5. console.info(`Succeeded in destroying wear engine channel.`);
6. }).catch((error: BusinessError) => {
7. console.error(`Failed to destroy wear engine channel. Code is ${error.code}, message is ${error.message}.`);
8. })
```
