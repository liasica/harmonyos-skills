---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-adminmanager
title: "@ohos.enterprise.adminManager（admin权限管理）"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.adminManager（admin权限管理）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:3ca961e1d70c931bf33ce8b1d541bc2cf46323d273e1fb11006c6c44118784db
---

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

```ts
import { adminManager } from '@kit.MDMKit';
```

## adminManager.disableAdmin

disableAdmin(admin: Want, userId?: number): Promise<void>

解除激活指定用户的设备管理应用。使用Promise异步回调。调用成功后，指定的设备管理应用将被解除激活，不再具备设备管理能力。

**需要权限：** ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN（仅系统应用支持申请）或ohos.permission.START\_PROVISIONING\_MESSAGE或ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN

- 从API version 23开始，支持申请ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN权限，仅当[SDA](../harmonyos-guides/mdm-kit-term.md#super-device-admin-sda超级设备管理员)或[DA](../harmonyos-guides/mdm-kit-term.md#device-admin-da普通设备管理员)设备管理应用解除激活自身时，可以申请该权限。

- 从API version 20开始，支持申请ohos.permission.START\_PROVISIONING\_MESSAGE权限。仅当[BYOD](../harmonyos-guides/mdm-kit-term.md#bring-your-own-device-byod自带设备办公)设备管理应用解除激活自身时，可以申请该权限。

- API version 19及之前的版本，需要申请ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN（仅系统应用支持申请）。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。解除激活BYOD设备管理应用时，仅支持传入当前应用的企业设备管理扩展组件。 |
| userId | number | 否 | 用户ID，取值范围：大于等于0。  - 调用接口时，若传入userId，表示指定用户。  - 调用接口时，若未传入userId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当解除激活设备管理应用失败时，会抛出错误对象。 |

**错误码**:

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200005 | Failed to deactivate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例**：

```ts
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.disableAdmin(wantTemp, 100).catch((err: BusinessError) => {
  console.error(`Failed to disable admin. Code: ${err.code}, message: ${err.message}`);
});
```

## adminManager.isByodAdmin20+

isByodAdmin(admin: Want): boolean

根据企业设备管理扩展组件查询当前应用是否被激活为BYOD设备管理应用。

**需要权限：** ohos.permission.START\_PROVISIONING\_MESSAGE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。仅支持传入当前应用的企业设备管理扩展组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示被激活为BYOD设备管理应用，返回false表示没有被激活为BYOD设备管理应用。 |

**错误码**:

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200012 | Parameter verification failed. |

**示例**：

```ts
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 请根据实际情况替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: boolean = adminManager.isByodAdmin(wantTemp);
  console.info(`Succeeded in querying admin is byod admin or not : ${result}`);
} catch (error) {
  console.error(`Failed to query admin is byod admin or not. Code is ${error.code}, message is ${error.message}`);
}
```

## adminManager.subscribeManagedEventSync

subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

订阅系统管理事件。调用成功后，当已订阅的系统管理事件发生时，设备管理应用将收到相应的通知。

从API版本26.0.0开始，非超级设备管理应用调用该接口订阅[MANAGED\_EVENT\_POLICIES\_CHANGED](js-apis-enterprise-adminmanager.md#managedevent)事件时返回9200002错误码。

**需要权限：** ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)> | 是 | 订阅事件数组，用于指定需要订阅的系统管理事件。数组元素为[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)枚举值，可订阅多个事件类型，如应用安装/卸载/启动/停止事件/系统更新事件等。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device.  适用版本：26.0.0+ |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED,
  adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

try {
  adminManager.subscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in subscribing managed event.');
} catch (err) {
  console.error(`Failed to subscribe managed event. Code: ${err.code}, message: ${err.message}`);
}
```

## adminManager.unsubscribeManagedEventSync

unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

取消订阅系统管理事件。调用成功后，将不再收到已取消订阅的系统管理事件通知。

**需要权限：** ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)> | 是 | 取消订阅事件数组，用于指定需要取消订阅的系统管理事件。数组元素为[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)枚举值，应与订阅时传入的事件类型一致。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED,
  adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

try {
  adminManager.unsubscribeManagedEventSync(wantTemp, events);
  console.info('Succeeded in unsubscribing managed event.');
} catch (err) {
  console.error(`Failed to unsubscribe managed event. Code: ${err.code}, message: ${err.message}`);
}
```

## adminManager.setDelegatedPolicies14+

setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void

委托其他应用来设置设备的管控策略。被委托的其他应用需申请委托策略对应接口所需权限。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被委托应用包名。被委托应用的分发类型需为enterprise\_normal和enterprise\_mdm，可以通过[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口查询应用自身的[BundleInfo](js-apis-bundlemanager-bundleinfo.md)，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |
| policies | Array<string> | 是 | [委托策略列表](../harmonyos-guides/mdm-kit-appendix.md#可委托策略列表)。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200009 | Failed to grant the permission to the application. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let policies: Array<string> = ["disabled_hdc"];

try {
  // 参数需根据实际情况进行替换
  adminManager.setDelegatedPolicies(admin, "com.example.enterprise.xxx", policies);
  console.info('Succeeded in setting delegated policies.');
} catch (err) {
  console.error(`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```

## adminManager.getDelegatedPolicies14+

getDelegatedPolicies(admin: Want, bundleName: string): Array<string>

查询被委托应用可访问的策略列表。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被委托应用包名。被委托应用的分发类型需为enterprise\_normal和enterprise\_mdm，可以通过[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口查询应用自身的[BundleInfo](js-apis-bundlemanager-bundleinfo.md)，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 委托策略列表。 |

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
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let policies: Array<string> = adminManager.getDelegatedPolicies(admin, "com.example.enterprise.xxx");
  console.info(`Succeeded in getting delegated policies.${JSON.stringify(policies)}`);
} catch (err) {
  console.error(`Failed to get delegated policies. Code: ${err.code}, message: ${err.message}`);
}
```

## adminManager.getDelegatedBundleNames14+

getDelegatedBundleNames(admin: Want, policy: string): Array<string>

查询可以访问某个委托策略的被委托应用，输出被委托应用列表。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | string | 是 | [委托策略](../harmonyos-guides/mdm-kit-appendix.md#可委托策略列表)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 被委托应用列表。 |

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
import { adminManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let admin: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  let bundleNames: Array<string> = adminManager.getDelegatedBundleNames(admin, "disabled_hdc");
  console.info(`Succeeded in getting delegated bundles.${JSON.stringify(bundleNames)}`);
} catch (err) {
  console.error(`Failed to get delegated bundles. Code: ${err.code}, message: ${err.message}`);
}
```

## adminManager.startAdminProvision15+

startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void

设备管理应用拉起BYOD管理员激活页面进行激活。

**需要权限：** ohos.permission.START\_PROVISIONING\_MESSAGE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| type | [AdminType](js-apis-enterprise-adminmanager.md#admintype15) | 是 | 激活的设备管理应用类型，仅支持ADMIN\_TYPE\_BYOD类型。 |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 管理应用的上下文信息。 |
| parameters | Record<string, string> | 是 | 自定义参数信息，其中Key值必须包含："activateId"，可以包含"customizedInfo"、"localDeactivationPolicy"。  - activateId：项目激活ID。  - customizedInfo：企业自定义信息。  - localDeactivationPolicy：本地延迟取消激活时间（单位：小时），端侧传入时长要小于等于云侧配置时长，否则会激活失败并提示为无效的激活参数，实际生效以端侧传入时长为准，从API version 22开始支持。 |

**注意** 

1、此接口只能在企业设备上生效。

2、参数credential为激活凭证，该激活凭证支持管理员通过HEM平台申请，[申请指导](https://developer.huawei.com/business/cn/doc/HEM/hem_developer_faq_emmwenti_pc_mdmazhjh-0000002540608338#section184382913281)。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { adminManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let recordParameters: Record<string, string> = {
  // 需根据实际情况进行替换
  "activateId": "activateId testValue",
  "customizedInfo": "customizedInfo testValue"
};
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  console.info('context:' + JSON.stringify(context));
  adminManager.startAdminProvision(wantTemp, adminManager.AdminType.ADMIN_TYPE_BYOD, context, recordParameters);
  console.info('Succeeded in starting Admin Provision');
} catch (error) {
  console.error('Failed to start Admin Provision::errorCode: ' + error.code + ' errorMessage: ' + error.message);
}
```

## adminManager.enableDeviceAdmin23+

enableDeviceAdmin(admin: Want): Promise<void>

[SDA](../harmonyos-guides/mdm-kit-term.md#super-device-admin-sda超级设备管理员)应用通过该接口可以激活其他[DA](../harmonyos-guides/mdm-kit-term.md#device-admin-da普通设备管理员)应用，使用Promise异步回调。调用成功后，指定的DA应用将被激活并具备设备管理能力。该接口仅支持超级设备管理应用调用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DEVICE\_ADMIN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当激活设备管理应用失败时，会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200003 | The administrator ability component is invalid. |
| 9200004 | Failed to activate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.enableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
  console.error(`Failed to enable device admin. Code: ${err.code}, message: ${err.message}`);
});
```

## adminManager.disableDeviceAdmin23+

disableDeviceAdmin(admin: Want): Promise<void>

[SDA](../harmonyos-guides/mdm-kit-term.md#super-device-admin-sda超级设备管理员)应用通过该接口可以解除激活其他[DA](../harmonyos-guides/mdm-kit-term.md#device-admin-da普通设备管理员)应用，使用Promise异步回调。调用成功后，指定的DA应用将被解除激活，不再具备设备管理能力。该接口仅支持超级设备管理应用调用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DEVICE\_ADMIN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当解除激活设备管理应用失败时，会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200005 | Failed to deactivate the administrator application of the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

adminManager.disableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
  console.error(`Failed to disable device admin. Code: ${err.code}, message: ${err.message}`);
});
```

## adminManager.enableSelfDeviceAdmin

enableSelfDeviceAdmin(admin: Want, credential: string): void

在企业设备中，MDM应用没有预置激活的场景下，MDM应用可以通过该接口实现自激活。该接口仅支持激活MDM应用自身，不支持激活其他MDM应用；支持的激活类型包括超级设备管理应用和普通设备管理应用。

**注意** 

1、此接口只能在企业设备上生效。

2、参数credential为激活凭证，该激活凭证支持管理员通过HEM平台申请，[申请指导](https://developer.huawei.com/business/cn/doc/HEM/hem_developer_faq_emmwenti_pc_mdmazhjh-0000002540608338#section184382913281)。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_ACTIVATE\_DEVICE\_ADMIN

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| credential | string | 是 | 激活凭证。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200003 | The administrator ability component is invalid. |
| 9200004 | Failed to activate the administrator application of the device. |
| 9200012 | Parameter verification failed. |
| 9200017 | The self-activation credential of the enterprise device administrator is invalid. |
| 9200018 | This device is not an enterprise device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// 需根据实际情况进行替换
let credential: string = '{"enterpriseId": "123456", "appIdentifier": "123456", "type": "SDA", "sign": "", "certs": []}';

try {
  adminManager.enableSelfDeviceAdmin(wantTemp, credential);
  console.info(`succeed in enabling self device admin.`);
} catch (err) {
  console.error(`Failed to enable self device admin. Code: ${err.code}, message: ${err.message}`);
}
```

## ManagedEvent

可订阅的系统管理事件。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MANAGED\_EVENT\_BUNDLE\_ADDED | 0 | 应用安装事件。 |
| MANAGED\_EVENT\_BUNDLE\_REMOVED | 1 | 应用卸载事件。 |
| MANAGED\_EVENT\_APP\_START | 2 | 应用启动事件。 |
| MANAGED\_EVENT\_APP\_STOP | 3 | 应用停止事件。 |
| MANAGED\_EVENT\_SYSTEM\_UPDATE | 4 | 系统更新事件。 |
| MANAGED\_EVENT\_ACCOUNT\_ADDED18+ | 5 | 账号新增事件。 |
| MANAGED\_EVENT\_ACCOUNT\_SWITCHED18+ | 6 | 账号切换事件。 |
| MANAGED\_EVENT\_ACCOUNT\_REMOVED18+ | 7 | 账号删除事件。 |
| MANAGED\_EVENT\_STARTUP\_GUIDE\_COMPLETED24+ | 8 | 开机向导完成事件。  **模型约束**：此接口仅可在Stage模型下使用。 |
| MANAGED\_EVENT\_BOOT\_COMPLETED24+ | 9 | 设备启动完成事件。  **模型约束**：此接口仅可在Stage模型下使用。 |
| MANAGED\_EVENT\_BUNDLE\_UPDATED | 10 | 应用更新事件。  **起始版本**：26.0.0  **模型约束**：此接口仅可在Stage模型下使用。 |
| MANAGED\_EVENT\_POLICIES\_CHANGED | 11 | 策略变更事件。仅支持超级设备管理应用订阅该事件，其他类型设备管理应用订阅该事件时返回9200002错误码。  **起始版本**：26.0.0  **模型约束**：此接口仅可在Stage模型下使用。 |

## AdminType15+

设备管理应用的类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN\_TYPE\_BYOD | 0x02 | BYOD设备管理应用。 |

## Policy20+

允许或禁用名单的策略类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLOCK\_LIST | 0 | 禁用名单。 |
| TRUST\_LIST | 1 | 允许名单。 |
