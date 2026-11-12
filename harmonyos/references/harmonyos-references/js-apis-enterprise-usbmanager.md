---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-usbmanager
title: "@ohos.enterprise.usbManager (USB管理)"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.usbManager (USB管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:07c25e75c68e0355d7126de37a137fe1b0b7778b9408a47f12961d0404702e31
---

本模块提供USB管理能力。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考[@ohos.enterprise.restrictions (限制类策略)](js-apis-enterprise-restrictions.md)。

## 导入模块

```ts
import { usbManager } from '@kit.MDMKit';
```

## usbManager.addAllowedUsbDevices

addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

添加USB设备可用名单。

**使用场景**：

* 企业安全管理场景，需要限制只有特定的USB设备可以接入设备
* 设备管理员需要精确控制哪些USB设备能够被识别和使用
* 配合[removeAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremoveallowedusbdevices)接口实现USB设备的动态管理

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB或者USB转串口能力。
2. 已经通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为禁用。
3. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。
4. 已经通过[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口添加了禁止使用的USB设备类型。
5. 已经通过[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)接口启用了外置存储设备挂载拦截。

**说明** 

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDeviceIds | Array<[UsbDeviceId](js-apis-enterprise-usbmanager.md#usbdeviceid)> | 是 | USB设备ID数组，UsbDeviceId信息可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。USB设备可用名单数组长度上限为1000，若当前允许名单中已有300个USB设备ID，则只允许再添加700个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200007 | The system ability works abnormally. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
    vendorId: 1,
    productId: 1
  }];
  usbManager.addAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(`Succeeded in adding allowed USB devices.`);
} catch (err) {
  console.error(`Failed to add allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.removeAllowedUsbDevices

removeAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

移除USB设备可用名单。

**使用场景**：

* 企业安全管理场景，需要撤销某些USB设备的访问权限
* 设备管理员需要动态调整允许使用的USB设备列表
* 当USB设备不再需要或存在安全风险时，从允许名单中移除

**说明** 

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDeviceIds | Array<[UsbDeviceId](js-apis-enterprise-usbmanager.md#usbdeviceid)> | 是 | USB设备ID数组，UsbDeviceId信息可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
    vendorId: 1,
    productId: 1
  }];
  usbManager.removeAllowedUsbDevices(wantTemp, usbDeviceIds);
  console.info(`Succeeded in removing allowed USB devices.`);
} catch (err) {
  console.error(`Failed to remove allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getAllowedUsbDevices

getAllowedUsbDevices(admin: Want): Array<UsbDeviceId>

获取USB设备可用名单。一般使用场景：在修改策略前，需要先获取现有策略进行评估；管理界面需要展示当前的USB存储设备访问控制状态。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[usbManager.getAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagergetallowedusbdevices-1)接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[UsbDeviceId](js-apis-enterprise-usbmanager.md#usbdeviceid)> | USB设备可用名单的设备ID数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceId> = usbManager.getAllowedUsbDevices(wantTemp);
  console.info(`Succeeded in getting allowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getAllowedUsbDevices

getAllowedUsbDevices(admin: Want | null): Array<UsbDeviceId>

获取USB设备可用名单。一般使用场景：在修改策略前，需要先获取现有策略进行评估；管理界面需要展示当前的USB存储设备访问控制状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[UsbDeviceId](js-apis-enterprise-usbmanager.md#usbdeviceid)> | USB设备可用名单的设备ID数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: Array<usbManager.UsbDeviceId> = usbManager.getAllowedUsbDevices(null);
  console.info(`Succeeded in getting allowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.setUsbStorageDeviceAccessPolicy

setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void

设置USB存储设备（baseClass = 0x08）访问策略。

**说明** 

在调用接口前，确保已暂停USB存储设备的读写操作，保证操作的稳定性和数据的完整性，否则可能出现不可预期的异常。

在多个MDM应用场景下，遵循[从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)规则。严格优先级：禁用 > 只读 > 可读可写。

以下情况下，通过本接口设置USB存储设备访问策略为可读可写/只读，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB能力。
2. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口将存储类型的USB设备添加为禁止使用的USB设备类型。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。
4. 已经通过[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)接口启用了外置存储设备挂载拦截。

以下情况下，通过本接口设置USB存储设备访问策略为禁用，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB能力。
2. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。
4. 已经通过[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)接口启用了外置存储设备挂载拦截。

通过本接口设置，或者通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加存储类型的USB设备，均可禁用USB存储设备。推荐使用后者。

**需要权限：**

* API版本26.0.0之前：ohos.permission.ENTERPRISE\_MANAGE\_USB
* API版本26.0.0开始：ohos.permission.ENTERPRISE\_MANAGE\_USB 或者 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS（应用调用[adminManager.startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)接口激活为自带设备管理应用）。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbPolicy | [UsbPolicy](js-apis-enterprise-usbmanager.md#usbpolicy) | 是 | USB存储设备访问策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200007 | The system ability works abnormally. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let policy: usbManager.UsbPolicy = usbManager.UsbPolicy.DISABLED;
  usbManager.setUsbStorageDeviceAccessPolicy(wantTemp, policy);
  console.info(`Succeeded in setting USB storage device access policy.`);
} catch (err) {
  console.error(`Failed to set USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getUsbStorageDeviceAccessPolicy

getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy

获取USB存储设备（baseClass = 0x08）访问策略。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[usbManager.getUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagergetusbstoragedeviceaccesspolicy-1)接口。

**需要权限：**

* API版本26.0.0之前：ohos.permission.ENTERPRISE\_MANAGE\_USB
* API版本26.0.0开始：ohos.permission.ENTERPRISE\_MANAGE\_USB 或者 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS（应用调用[adminManager.startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)接口激活为自带设备管理应用）。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UsbPolicy](js-apis-enterprise-usbmanager.md#usbpolicy) | USB存储设备访问策略。设置为READ\_WRITE表示允许读写USB存储设备；设置为READ\_ONLY表示仅允许读取USB存储设备，禁止写入；设置为DISABLED表示完全禁止访问USB存储设备。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(wantTemp);
  console.info(`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getUsbStorageDeviceAccessPolicy

getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy

获取USB存储设备（baseClass = 0x08）访问策略。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB 或者 ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS（应用调用[adminManager.startAdminProvision](js-apis-enterprise-adminmanager.md#adminmanagerstartadminprovision15)接口激活为自带设备管理应用）。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UsbPolicy](js-apis-enterprise-usbmanager.md#usbpolicy) | USB存储设备访问策略。设置为READ\_WRITE表示允许读写USB存储设备；设置为READ\_ONLY表示仅允许读取USB存储设备，禁止写入；设置为DISABLED表示完全禁止访问USB存储设备。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(null);
  console.info(`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.addDisallowedUsbDevices14+

addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

添加禁止使用的USB设备类型。一般使用场景：企业安全管理场景，需要禁用特定类型的USB设备；防止数据泄露：禁用USB存储设备类型；设备管理员需要根据安全策略，禁止使用某些类型的USB设备；配合[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口实现USB设备类型的动态管理。

**说明** 

推荐使用[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口。

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB能力。
2. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。
4. 已经通过[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口添加了禁止使用的USB设备类型。
5. 已经通过[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)接口启用了外置存储设备挂载拦截。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDevices | Array<[UsbDeviceType](js-apis-enterprise-usbmanager.md#usbdevicetype14)> | 是 | 要添加的USB设备类型的数组，UsbDeviceType信息可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。USB设备禁用名单数组长度上限为200，若当前禁用名单中已有100个USB设备ID，则只允许再添加100个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
    baseClass: 8,
    subClass: 0,
    protocol: 0,
    descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in adding disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.removeDisallowedUsbDevices14+

removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

移除禁止使用的USB设备类型。

**使用场景**：

* 企业安全管理场景，需要解除对某些USB设备类型的禁用
* 设备管理员需要动态调整禁止使用的USB设备类型列表
* 当某些USB设备类型不再存在安全风险时，从禁用名单中移除

**说明** 

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDevices | Array<[UsbDeviceType](js-apis-enterprise-usbmanager.md#usbdevicetype14)> | 是 | 要移除的USB设备类型的数组，UsbDeviceType信息可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
    baseClass: 8,
    subClass: 0,
    protocol: 0,
    descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.removeDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in removing disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to remove disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getDisallowedUsbDevices14+

getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>

获取禁止使用的USB设备类型。一般使用场景：设备管理员需要查看当前禁止使用的USB设备类型列表；在修改禁用名单前，需要先获取现有名单进行比对；管理界面需要展示当前的USB设备类型禁用策略配置。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[usbManager.getDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagergetdisallowedusbdevices)接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[UsbDeviceType](js-apis-enterprise-usbmanager.md#usbdevicetype14)> | 禁止使用的USB设备类型。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.UsbDeviceType> = usbManager.getDisallowedUsbDevices(wantTemp);
  console.info(`Succeeded in getting disallowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getDisallowedUsbDevices

getDisallowedUsbDevices(admin: Want | null): Array<UsbDeviceType>

获取禁止使用的USB设备类型。一般使用场景：设备管理员需要查看当前禁止使用的USB设备类型列表；在修改禁用名单前，需要先获取现有名单进行比对；管理界面需要展示当前的USB设备类型禁用策略配置。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[UsbDeviceType](js-apis-enterprise-usbmanager.md#usbdevicetype14)> | 禁止使用的USB设备类型。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: Array<usbManager.UsbDeviceType> = usbManager.getDisallowedUsbDevices(null);
  console.info(`Succeeded in getting disallowed USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.addDisallowedPermissiveUsbDevices

addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void

添加禁止使用的USB设备类型。与[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口不同的是，本接口可以不按照[defined-class-codes](https://www.usb.org/defined-class-codes)标准进行匹配。对已连接的USB设备热生效，无需重新插拔，例如USB线控耳机正常使用时，调用本接口禁用该耳机，会导致耳机不可用。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。
2. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB能力。
3. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
4. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。
5. 已经通过[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)接口启用了外置存储设备挂载拦截。

**起始版本：** 26.0.0

**说明** 

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDevices | Array<[PermissiveUsbDeviceType](js-apis-enterprise-usbmanager.md#permissiveusbdevicetype)> | 是 | 要添加的USB设备类型的数组，支持部分字段匹配。USB设备禁用名单数组长度上限为1000，若当前禁用名单中已有500个USB设备ID，则只允许再添加500个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  // 禁用USB存储设备（以实际USB设备类型参数为准）
  let usbDevices1: Array<usbManager.PermissiveUsbDeviceType> = [{
    baseClass: 8
  }];
  usbManager.addDisallowedPermissiveUsbDevices(wantTemp, usbDevices1);

  // 禁用USB线控耳机（以实际USB设备类型参数为准）
  let usbDevices2: Array<usbManager.PermissiveUsbDeviceType> = [{
    baseClass: 0,
    subClass: 0,
    protocol: 0,
    descriptor: usbManager.Descriptor.DEVICE
  }];
  usbManager.addDisallowedPermissiveUsbDevices(wantTemp, usbDevices2);

  // 禁用USB线控键盘输入（以实际USB设备类型参数为准）
  let usbDevices3: Array<usbManager.PermissiveUsbDeviceType> = [{
    baseClass: 3,
    subClass: 1,
    protocol: 1,
    descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.addDisallowedPermissiveUsbDevices(wantTemp, usbDevices3);
  console.info(`Succeeded in adding disallowed permissive USB devices.`);
} catch (err) {
  console.error(`Failed to add disallowed permissive USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.removeDisallowedPermissiveUsbDevices

removeDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void

移除通过[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口禁用的USB设备类型。被移除的USB设备类型可恢复正常使用。

**起始版本：** 26.0.0

**说明** 

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| usbDevices | Array<[PermissiveUsbDeviceType](js-apis-enterprise-usbmanager.md#permissiveusbdevicetype)> | 是 | 要移除的USB设备类型的数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.PermissiveUsbDeviceType> = [{
    baseClass: 8
  }];
  usbManager.removeDisallowedPermissiveUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in removing disallowed permissive USB devices.`);
} catch (err) {
  console.error(`Failed to remove disallowed permissive USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getDisallowedPermissiveUsbDevices

getDisallowedPermissiveUsbDevices(admin: Want | null): Array<PermissiveUsbDeviceType>

获取通过[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口禁用的USB设备类型。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。当取值为null时，表示获取当前设备禁止使用的USB设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[PermissiveUsbDeviceType](js-apis-enterprise-usbmanager.md#permissiveusbdevicetype)> | 禁止使用的USB设备类型数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<usbManager.PermissiveUsbDeviceType> = usbManager.getDisallowedPermissiveUsbDevices(wantTemp);
  console.info(`Succeeded in getting disallowed permissive USB devices. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed permissive USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getUsbSerialNumber

getUsbSerialNumber(busNum: number, devAddress: number): string

获取USB设备的序列号。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| busNum | number | 是 | USB设备的总线号，可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。 |
| devAddress | number | 是 | USB设备的地址，可以通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | USB设备的序列号。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9201055 | Failed to obtain the USB serial number. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { usbManager as baseUsbManager } from '@kit.BasicServicesKit';

// 获取已接入主设备的USB设备列表
let devicesList: Array<baseUsbManager.USBDevice> = baseUsbManager.getDevices();
console.info(`devicesList = ${devicesList}`);

// 选取目标USB设备（此处以第一个设备为例），取出busNum和devAddress作为入参
let device: baseUsbManager.USBDevice = devicesList[0];

try {
  let result: string = usbManager.getUsbSerialNumber(device.busNum, device.devAddress);
  console.info(`Succeeded in getting USB serial number. Result: ${result}`);
} catch (err) {
  console.error(`Failed to get USB serial number. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.addAllowedOpticalDiscDriveBurnUsbDevices

addAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>

添加外置USB光驱刻录设备可用名单，单次最多添加10000条可用名单数据。调用此接口前，此设备必须通过[HEM商用部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。添加时不影响正在进行光驱刻录的设备。策略热生效，无需重新插拔光驱设备即可对光驱刻录进行管控。可用名单添加完成后，仅允许可用名单中的设备类型进行刻录。当光驱刻录设备可用名单为空时，不对光驱刻录进行管控。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| usbDevices | Array<[UsbDevice](js-apis-enterprise-usbmanager.md#usbdevice)> | 是 | 待添加的外置USB光驱设备数组。数组长度上限为10000，且不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability.  2. The chip does not support the capability.  3. A dependent service feature is not supported. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9200019 | The policy list has exceeded the limit. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let usbDevices: Array<usbManager.UsbDevice> = [{
  vendorId: 1234,
  productId: 5678,
  serial: 'SN123456789'
}];
usbManager.addAllowedOpticalDiscDriveBurnUsbDevices(usbDevices).then(() => {
  console.info('Succeeded in adding allowed optical disc drive burn USB devices.');
}).catch((err: BusinessError) => {
  console.error(`Failed to add allowed optical disc drive burn USB devices. Code is ${err.code}, message is ${err.message}`);
});
```

## usbManager.removeAllowedOpticalDiscDriveBurnUsbDevices

removeAllowedOpticalDiscDriveBurnUsbDevices(usbDevices: Array<UsbDevice>): Promise<void>

移除外置USB光驱刻录设备可用名单，单次最多移除10000条可用名单数据。移除时不影响正在进行光驱刻录的设备。策略热生效，无需重新插拔光驱设备即可对光驱刻录进行管控。移除后，被移除的设备类型不再允许刻录。当光驱刻录设备可用名单为空时，不对光驱刻录进行管控。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| usbDevices | Array<[UsbDevice](js-apis-enterprise-usbmanager.md#usbdevice)> | 是 | 要移除的USB设备数组。数组长度上限为10000，且不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Possible causes:  1. The hardware does not support the capability.  2. The chip does not support the capability.  3. A dependent service feature is not supported. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9200019 | The policy list has exceeded the limit. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let usbDevices: Array<usbManager.UsbDevice> = [{
  vendorId: 1234,
  productId: 5678,
  serial: 'SN123456789'
}];
usbManager.removeAllowedOpticalDiscDriveBurnUsbDevices(usbDevices).then(() => {
  console.info('Succeeded in removing allowed optical disc drive burn USB devices.');
}).catch((err: BusinessError) => {
  console.error(`Failed to remove allowed optical disc drive burn USB devices. Code is ${err.code}, message is ${err.message}`);
});
```

## usbManager.getAllowedOpticalDiscDriveBurnUsbDevices

getAllowedOpticalDiscDriveBurnUsbDevices(queryPolicy?: common.QueryPolicy): Promise<Array<UsbDevice>>

获取外置USB光驱刻录设备可用名单。可在修改策略前获取现有可用名单进行评估，或在管理界面展示当前可用名单状态。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryPolicy | [common.QueryPolicy](js-apis-enterprise-common.md#querypolicy) | 否 | 查询策略。通过queryPolicy指定查询策略，默认值为common.QueryPolicy.SELF，表示查询当前设备管理应用设置的策略；传入common.QueryPolicy.ALL时，可查询当前设备设置的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[UsbDevice](js-apis-enterprise-usbmanager.md#usbdevice)>> | Promise对象，返回支持CD/DVD刻录的USB设备数组。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200016 | Service timeout. |

**示例：**

```ts
import { usbManager, common } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

usbManager.getAllowedOpticalDiscDriveBurnUsbDevices(common.QueryPolicy.SELF).then((result: Array<usbManager.UsbDevice>) => {
  console.info(`Succeeded in getting allowed optical disc drive burn USB devices. Result: ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get allowed optical disc drive burn USB devices. Code is ${err.code}, message is ${err.message}`);
});
```

## usbManager.setExternalStorageInterceptEnable

setExternalStorageInterceptEnable(enable: boolean): void

设置外置存储设备挂载拦截的启用状态。调用此接口前，此设备必须通过[HEM商用部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。设置拦截使能成功后，不会影响已经挂载的外置存储设备；新插入的外置存储设备将不再自动挂载，需调用[usbManager.setExternalStorageDeviceMountPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstoragedevicemountpolicy)接口对其进行挂载。取消拦截使能后，未挂载的外置存储设备需重新插拔才能挂载成功。拦截的外置存储设备仅支持[common.DiskType](js-apis-enterprise-common.md#disktype)对应类型。

**说明** 

在多个MDM应用场景下，遵循[从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)规则。只要任一MDM应用设置拦截使能，系统即保持拦截使能。

以下情况下，启用外置存储设备挂载拦截（enable为true）会报策略冲突：

1. 已经通过[addDisallowedPermissiveUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedpermissiveusbdevices)接口添加了禁止使用的USB设备类型。
2. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。
3. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicydeprecated)接口禁用了设备USB能力。
4. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
5. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccountdeprecated)接口禁用了某用户USB存储设备写入能力。
6. 已经通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为禁用。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用外置存储设备挂载拦截。true表示启用，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200016 | Service timeout. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';

try {
  usbManager.setExternalStorageInterceptEnable(true);
  console.info(`Succeeded in setting external storage intercept enable.`);
} catch (err) {
  console.error(`Failed to set external storage intercept enable. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.isExternalStorageInterceptEnable

isExternalStorageInterceptEnable(queryPolicy?: common.QueryPolicy): boolean

查询外置存储设备挂载拦截的启用状态。可在调用[setExternalStorageInterceptEnable](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstorageinterceptenable)设置拦截前查询当前状态，或在管理界面展示当前拦截状态。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryPolicy | [common.QueryPolicy](js-apis-enterprise-common.md#querypolicy) | 否 | 查询策略。通过queryPolicy指定查询策略，默认值为common.QueryPolicy.SELF，表示查询当前设备管理应用设置的策略；传入common.QueryPolicy.ALL时，可查询当前设备设置的策略。返回true表示已启用外置存储设备挂载拦截；返回false表示未启用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示已启用外置存储设备挂载拦截；返回false表示未启用。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200016 | Service timeout. |

**示例：**

```ts
import { usbManager, common } from '@kit.MDMKit';

try {
  let result: boolean = usbManager.isExternalStorageInterceptEnable(common.QueryPolicy.SELF);
  console.info(`Succeeded in querying external storage intercept enable. Result: ${result}`);
} catch (err) {
  console.error(`Failed to query external storage intercept enable. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.setExternalStorageDeviceMountPolicy

setExternalStorageDeviceMountPolicy(volumeId: string, policy: MountPolicy): void

设置外置存储设备的挂载策略，可对外置存储设备进行挂载或卸载。针对光驱类型的外置存储设备（[common.DiskType](js-apis-enterprise-common.md#disktype)为CD\_DVD\_BD），无论设置可读可写挂载（[MountPolicy](js-apis-enterprise-usbmanager.md#mountpolicy).MOUNT\_READ\_WRITE）还是只读挂载（[MountPolicy](js-apis-enterprise-usbmanager.md#mountpolicy).MOUNT\_READ\_ONLY），最终生效的都是只读挂载。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volumeId | string | 是 | 卷ID，可以通过[getExternalStorageDeviceInfos](js-apis-enterprise-usbmanager.md#usbmanagergetexternalstoragedeviceinfos)接口获取。 |
| policy | [MountPolicy](js-apis-enterprise-usbmanager.md#mountpolicy) | 是 | 挂载策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9201056 | Invalid external storage mount policy. |

**示例：**

```ts
import { usbManager } from '@kit.MDMKit';

try {
  // 卷ID需根据实际情况进行替换
  let volumeId: string = 'public:123456,1';
  let policy: usbManager.MountPolicy = usbManager.MountPolicy.MOUNT_READ_WRITE;
  usbManager.setExternalStorageDeviceMountPolicy(volumeId, policy);
  console.info(`Succeeded in setting external storage device mount policy.`);
} catch (err) {
  console.error(`Failed to set external storage device mount policy. Code: ${err.code}, message: ${err.message}`);
}
```

## usbManager.getExternalStorageDeviceInfos

getExternalStorageDeviceInfos(): Array<common.ExternalStorageDeviceInfo>

获取当前设备的外置存储设备信息。可在调用[setExternalStorageDeviceMountPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetexternalstoragedevicemountpolicy)设置挂载策略前，通过本接口获取外置存储设备的卷ID（volumeId）及挂载状态；也可在管理界面展示当前已接入的外置存储设备列表。返回外置存储设备信息数组，包含设备类型、挂载路径、卷ID、挂载状态、厂商ID、产品ID和序列号。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common.ExternalStorageDeviceInfo](js-apis-enterprise-common.md#externalstoragedeviceinfo)> | 外置存储设备信息数组。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200016 | Service timeout. |

**示例：**

```ts
import { usbManager, common } from '@kit.MDMKit';

try {
  let result: Array<common.ExternalStorageDeviceInfo> = usbManager.getExternalStorageDeviceInfos();
  console.info(`Succeeded in getting external storage device infos. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get external storage device infos. Code: ${err.code}, message: ${err.message}`);
}
```

## UsbDeviceId

USB设备ID信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | 厂商ID。 |
| productId | number | 否 | 否 | 产品ID。 |

## UsbDeviceType14+

USB设备类型信息。

可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，并从返回值列表中查找当前设备的类型信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseClass | number | 否 | 否 | 类型编码。  先根据此值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.clazz字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.clazz字段值。  若字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| subClass | number | 否 | 否 | 子类型编码。  先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.subClass字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.subClass字段值。  若字段值为255，表示此设备的子类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| protocol | number | 否 | 否 | 协议编码。  先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.protocol字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.protocol字段值。  若字段值为255，表示此设备的协议编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| descriptor | [Descriptor](js-apis-enterprise-usbmanager.md#descriptor14) | 否 | 否 | USB描述符。  若此值USBDevice.clazz字段值为0，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找此值USBDevice.configs.interfaces.clazz字段值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）;  若此值USBDevice.clazz字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若此值USBDevice.clazz字段值为其他值，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找该值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）。 |

## UsbPolicy

USB读写策略的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READ\_WRITE | 0 | 可读可写。 |
| READ\_ONLY | 1 | 只读。 |
| DISABLED | 2 | 禁用。 |

## Descriptor14+

USB存储设备访问策略的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERFACE | 0 | 接口描述符。 |
| DEVICE | 1 | 设备描述符。 |

## PermissiveUsbDeviceType

USB设备类型信息，支持部分字段匹配。

* 与[UsbDeviceType](js-apis-enterprise-usbmanager.md#usbdevicetype14)相比，本接口的subClass、protocol、descriptor字段为可选字段，实现更灵活的USB设备禁用策略。
* 支持仅根据baseClass字段进行匹配。
* 支持配置多个字段，多个字段同时满足才匹配。
* 可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，并从返回值列表中查找当前设备的类型信息。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseClass | number | 否 | 否 | 类型编码。取值范围为[0, 255]。  若descriptor为DEVICE，则本字段取USBDevice.clazz字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.clazz字段值。 |
| subClass | number | 否 | 是 | 子类型编码。取值范围为[0, 255]。  若descriptor为DEVICE，则本字段取USBDevice.subClass字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.subClass字段值。 |
| protocol | number | 否 | 是 | 协议编码。取值范围为[0, 255]。  若descriptor为DEVICE，则本字段取USBDevice.protocol字段值；若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.protocol字段值。 |
| descriptor | [Descriptor](js-apis-enterprise-usbmanager.md#descriptor14) | 否 | 是 | USB描述符。  若USBDevice.clazz字段值为0，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找USBDevice.configs.interfaces.clazz字段值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）；若USBDevice.clazz字段值为其他值，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找该值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）。 |

## UsbDevice

外置光驱设备标识信息。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | 厂商ID。 |
| productId | number | 否 | 否 | 产品ID。 |
| serial | string | 否 | 是 | 序列号。 |

## MountPolicy

外置存储设备挂载策略的枚举。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MOUNT\_READ\_WRITE | 0 | 可读可写挂载。 |
| MOUNT\_READ\_ONLY | 1 | 只读挂载。 |
| UNMOUNT | 2 | 卸载。 |
