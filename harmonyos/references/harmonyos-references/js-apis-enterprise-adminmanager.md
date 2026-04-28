---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-adminmanager
title: @ohos.enterprise.adminManager（admin权限管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.adminManager（admin权限管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f42649b9bb716f33b9e93dae312b1c066beaced74ab2fa97de43949578eb796
---

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { adminManager } from '@kit.MDMKit';
```

## adminManager.disableAdmin

PhonePC/2in1Tablet

disableAdmin(admin: Want, userId?: number): Promise<void>

解除激活指定用户的设备管理应用。使用Promise异步回调。

**需要权限：** ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN（仅系统应用支持申请）或ohos.permission.START\_PROVISIONING\_MESSAGE或ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN

- 从API version 23开始，支持申请ohos.permission.ENTERPRISE\_DEACTIVATE\_DEVICE\_ADMIN权限。仅当SDA或DA设备管理应用解除激活自身时，可以申请该权限。

- 从API version 20开始，支持申请ohos.permission.START\_PROVISIONING\_MESSAGE权限。仅当BYOD设备管理应用解除激活自身时，可以申请该权限。

- API 19及之前的版本，需要申请ohos.permission.MANAGE\_ENTERPRISE\_DEVICE\_ADMIN（仅系统应用支持申请）。

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

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. adminManager.disableAdmin(wantTemp, 100).catch((err: BusinessError) => {
12. console.error(`Failed to disable admin. Code: ${err.code}, message: ${err.message}`);
13. });
```

## adminManager.isByodAdmin20+

PhonePC/2in1Tablet

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

```
1. import { Want } from '@kit.AbilityKit';
2. import { adminManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 请根据实际情况替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: boolean = adminManager.isByodAdmin(wantTemp);
12. console.info(`Succeeded in querying admin is byod admin or not : ${result}`);
13. } catch (error) {
14. console.error(`Failed to query admin is byod admin or not. Code is ${error.code}, message is ${error.message}`);
15. }
```

## adminManager.subscribeManagedEventSync

PhonePC/2in1Tablet

subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

订阅系统管理事件。

**需要权限：** ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)> | 是 | 订阅事件数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED, adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

11. try {
12. adminManager.subscribeManagedEventSync(wantTemp, events);
13. console.info('Succeeded in subscribing managed event.');
14. } catch (err) {
15. console.error(`Failed to subscribe managed event. Code: ${err.code}, message: ${err.message}`);
16. }
```

## adminManager.unsubscribeManagedEventSync

PhonePC/2in1Tablet

unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void

取消订阅系统管理事件。

**需要权限：** ohos.permission.ENTERPRISE\_SUBSCRIBE\_MANAGED\_EVENT

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| managedEvents | Array<[ManagedEvent](js-apis-enterprise-adminmanager.md#managedevent)> | 是 | 取消订阅事件数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200008 | The specified system event is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let events: Array<adminManager.ManagedEvent> = [adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_ADDED, adminManager.ManagedEvent.MANAGED_EVENT_BUNDLE_REMOVED];

11. try {
12. adminManager.unsubscribeManagedEventSync(wantTemp, events);
13. console.info('Succeeded in unsubscribing managed event.');
14. } catch (err) {
15. console.error(`Failed to unsubscribe managed event. Code: ${err.code}, message: ${err.message}`);
16. }
```

## adminManager.setDelegatedPolicies14+

PhonePC/2in1Tablet

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
| policies | Array<string> | 是 | [委托策略列表](js-apis-enterprise-adminmanager.md#可委托策略列表)。 |

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

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let admin: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let policies: Array<string> = ["disabled_hdc"];

12. try {
13. // 参数需根据实际情况进行替换
14. adminManager.setDelegatedPolicies(admin, "com.example.enterprise.xxx", policies);
15. console.info('Succeeded in setting delegated policies.');
16. } catch (err) {
17. console.error(`Failed to set delegated policies. Code: ${err.code}, message: ${err.message}`);
18. }
```

## adminManager.getDelegatedPolicies14+

PhonePC/2in1Tablet

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

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let admin: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let policies: Array<string> = adminManager.getDelegatedPolicies(admin, "com.example.enterprise.xxx");
13. console.info(`Succeeded in getting delegated policies.${JSON.stringify(policies)}`);
14. } catch (err) {
15. console.error(`Failed to get delegated policies. Code: ${err.code}, message: ${err.message}`);
16. }
```

## adminManager.getDelegatedBundleNames14+

PhonePC/2in1Tablet

getDelegatedBundleNames(admin: Want, policy: string): Array<string>

查询可以访问某个委托策略的被委托应用，输出被委托应用列表。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_DELEGATED\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | string | 是 | 委托策略。 |

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

```
1. import { adminManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let admin: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let bundleNames: Array<string> = adminManager.getDelegatedBundleNames(admin, "disabled_hdc");
13. console.info(`Succeeded in getting delegated bundles.${JSON.stringify(bundleNames)}`);
14. } catch (err) {
15. console.error(`Failed to get delegated bundles. Code: ${err.code}, message: ${err.message}`);
16. }
```

## adminManager.startAdminProvision15+

PhonePC/2in1Tablet

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
| parameters | Record<string, string> | 是 | 自定义参数信息，其中Key值必须包含："activateId"，可以包含"customizedInfo"、"localDeactivationPolicy"。  - activateId：项目激活ID。  - customizedInfo：企业自定义信息。  - localDeactivationPolicy：从API version 22开始支持，本地延迟取消激活时间（单位：小时）。 |

**错误码**：

以下的错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { adminManager } from '@kit.MDMKit';
2. import { common, Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let recordParameters: Record<string, string> = {
10. // 需根据实际情况进行替换
11. "activateId": "activateId testValue",
12. "customizedInfo": "customizedInfo testValue"
13. };
14. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
15. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. try {
17. console.info('context:' + JSON.stringify(context));
18. adminManager.startAdminProvision(wantTemp, adminManager.AdminType.ADMIN_TYPE_BYOD, context, recordParameters);
19. console.info('startAdminProvision::success');
20. } catch (error) {
21. console.error('startAdminProvision::errorCode: ' + error.code + ' errorMessage: ' + error.message);
22. }
```

## adminManager.enableDeviceAdmin23+

PhonePC/2in1Tablet

enableDeviceAdmin(admin: Want): Promise<void>

[超级设备管理应用](../harmonyos-guides/mdm-kit-term.md#sda)通过该接口可以激活其他[普通设备管理应用](../harmonyos-guides/mdm-kit-term.md#da)，使用Promise异步回调。该接口仅支持超级设备管理应用调用。

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

```
1. import { Want } from '@kit.AbilityKit';
2. import { adminManager } from '@kit.MDMKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. adminManager.enableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
12. console.error(`Failed to enable device admin. Code: ${err.code}, message: ${err.message}`);
13. });
```

## adminManager.disableDeviceAdmin23+

PhonePC/2in1Tablet

disableDeviceAdmin(admin: Want): Promise<void>

[超级设备管理应用](../harmonyos-guides/mdm-kit-term.md#sda)通过该接口可以解除激活其他[普通设备管理应用](../harmonyos-guides/mdm-kit-term.md#da)，使用Promise异步回调。该接口仅支持超级设备管理应用调用。

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

```
1. import { Want } from '@kit.AbilityKit';
2. import { adminManager } from '@kit.MDMKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. adminManager.disableDeviceAdmin(wantTemp).catch((err: BusinessError) => {
12. console.error(`Failed to disable device admin. Code: ${err.code}, message: ${err.message}`);
13. });
```

## ManagedEvent

PhonePC/2in1Tablet

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

## AdminType15+

PhonePC/2in1Tablet

设备管理应用的类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ADMIN\_TYPE\_BYOD | 0x02 | BYOD设备管理应用。 |

## Policy20+

PhonePC/2in1Tablet

允许或禁用名单的策略类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLOCK\_LIST | 0 | 禁用名单。 |
| TRUST\_LIST | 1 | 允许名单。 |

## 附录

PhonePC/2in1Tablet

### 可委托策略列表

| 策略名称 | 对应接口 | 说明 |
| --- | --- | --- |
| disallow\_add\_local\_account | [accountManager.disallowOsAccountAddition](js-apis-enterprise-accountmanager.md#accountmanagerdisallowosaccountaddition)  [accountManager.isOsAccountAdditionDisallowed](js-apis-enterprise-accountmanager.md#accountmanagerisosaccountadditiondisallowed) | 不传accountId参数，禁止设备创建本地用户。  不传accountId参数，查询是否禁止设备创建本地用户。 |
| disallow\_add\_os\_account\_by\_user | [accountManager.disallowOsAccountAddition](js-apis-enterprise-accountmanager.md#accountmanagerdisallowosaccountaddition)  [accountManager.isOsAccountAdditionDisallowed](js-apis-enterprise-accountmanager.md#accountmanagerisosaccountadditiondisallowed) | 需传入accountId参数，禁止指定用户添加账号。  需传入accountId参数，查询是否禁止指定用户添加账号。 |
| disallow\_running\_bundles | [applicationManager.addDisallowedRunningBundlesSync](js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)  [applicationManager.removeDisallowedRunningBundlesSync](js-apis-enterprise-applicationmanager.md#applicationmanagerremovedisallowedrunningbundlessync)  [applicationManager.getDisallowedRunningBundlesSync](js-apis-enterprise-applicationmanager.md#applicationmanagergetdisallowedrunningbundlessync) | 添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。  从应用运行禁止名单中移除应用。  获取当前/指定用户下的应用运行禁止名单。 |
| manage\_auto\_start\_apps | [applicationManager.addAutoStartApps](js-apis-enterprise-applicationmanager.md#applicationmanageraddautostartapps)  [applicationManager.removeAutoStartApps](js-apis-enterprise-applicationmanager.md#applicationmanagerremoveautostartapps)  [applicationManager.getAutoStartApps](js-apis-enterprise-applicationmanager.md#applicationmanagergetautostartapps) | 添加开机自启动应用名单。  从开机自启动应用名单中移除应用。  查询开机自启动应用名单。 |
| allowed\_bluetooth\_devices | [bluetoothManager.addAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanageraddallowedbluetoothdevices)  [bluetoothManager.removeAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanagerremoveallowedbluetoothdevices)  [bluetoothManager.getAllowedBluetoothDevices](js-apis-enterprise-bluetoothmanager.md#bluetoothmanagergetallowedbluetoothdevices) | 添加蓝牙设备可用名单。  从蓝牙设备可用名单中移除。  查询蓝牙设备可用名单。 |
| set\_browser\_policies | [browser.setPolicySync](js-apis-enterprise-browser.md#browsersetpolicysync)  [browser.getPoliciesSync](js-apis-enterprise-browser.md#browsergetpoliciessync) | 为指定的浏览器设置浏览器子策略。  获取指定浏览器的策略。 |
| allowed\_install\_bundles | [bundleManager.addAllowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanageraddallowedinstallbundlessync)  [bundleManager.removeAllowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagerremoveallowedinstallbundlessync)  [bundleManager.getAllowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagergetallowedinstallbundlessync) | 添加应用至应用程序包安装允许名单，添加至允许名单的应用允许在当前/指定用户下安装，否则不允许安装。  从应用程序包安装允许名单中移除应用。  获取当前/指定用户下的应用程序包安装允许名单。 |
| disallowed\_install\_bundles | [bundleManager.addDisallowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanageradddisallowedinstallbundlessync)  [bundleManager.removeDisallowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagerremovedisallowedinstallbundlessync)  [bundleManager.getDisallowedInstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagergetdisallowedinstallbundlessync) | 添加应用至应用程序包安装禁止名单，添加至禁止名单的应用不允许在当前/指定用户下安装。  从应用程序包安装禁止名单中移除应用。  获取当前/指定用户下的应用程序包安装禁止名单。 |
| disallowed\_uninstall\_bundles | [bundleManager.addDisallowedUninstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanageradddisalloweduninstallbundlessync)  [bundleManager.removeDisallowedUninstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagerremovedisalloweduninstallbundlessync)  [bundleManager.getDisallowedUninstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanagergetdisalloweduninstallbundlessync) | 添加应用至应用程序包卸载禁止名单，添加至禁止名单的应用不允许在当前/指定用户下卸载。  从应用程序包卸载禁止名单中移除应用。  获取当前/指定用户下的应用包程序卸载禁止名单。 |
| get\_device\_info | [deviceInfo.getDeviceInfo](js-apis-enterprise-deviceinfo.md#deviceinfogetdeviceinfo) | 获取设备信息。 |
| location\_policy | [locationManager.setLocationPolicy](js-apis-enterprise-locationmanager.md#locationmanagersetlocationpolicy)  [locationManager.getLocationPolicy](js-apis-enterprise-locationmanager.md#locationmanagergetlocationpolicy) | 设置位置服务管理策略。  查询位置服务策略。 |
| disabled\_network\_interface | [networkManager.setNetworkInterfaceDisabledSync](js-apis-enterprise-networkmanager.md#networkmanagersetnetworkinterfacedisabledsync)  [networkManager.isNetworkInterfaceDisabledSync](js-apis-enterprise-networkmanager.md#networkmanagerisnetworkinterfacedisabledsync) | 禁止设备使用指定网络。  查询指定网络接口是否被禁用。 |
| global\_proxy | [networkManager.setGlobalProxySync](js-apis-enterprise-networkmanager.md#networkmanagersetglobalproxysync)  [networkManager.getGlobalProxySync](js-apis-enterprise-networkmanager.md#networkmanagergetglobalproxysync) | 设置网络全局代理。  获取网络全局代理。 |
| disabled\_bluetooth | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入bluetooth，禁用/启用蓝牙能力。  feature传入bluetooth，查询是否禁用蓝牙能力。 |
| disallow\_modify\_datetime | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入modifyDateTime，禁用/启用设置系统时间能力。  feature传入modifyDateTime，查询是否禁用修改系统时间能力。 |
| disabled\_printer | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入printer，禁用/启用打印能力。  feature传入printer，查询是否禁用打印能力。 |
| disabled\_hdc | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入hdc，禁用/启用被其他设备通过hdc连接、调试的能力。  feature传入hdc，查询是否禁用被其他设备通过hdc连接、调试的能力。 |
| disable\_microphone | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入microphone，禁用/启用麦克风能力。  feature传入microphone，查询是否禁用麦克风能力。 |
| fingerprint\_auth | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy)  [restrictions.setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14)  [restrictions.getDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicyforaccount14) | feature传入fingerprint，禁用/启用指纹认证能力。  feature传入fingerprint，查询是否禁用指纹认证能力。  feature传入fingerprint，禁用/启用指定用户的指纹认证能力。  feature传入fingerprint，查询是否禁用指定用户的指纹认证能力。 |
| disable\_usb | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入usb，禁用/启用USB能力。  feature传入usb，查询是否禁用USB能力。 |
| disable\_wifi | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入wifi，禁用/启用Wi-Fi能力。  feature传入wifi，查询是否禁用Wi-Fi能力。 |
| disallowed\_tethering | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入tethering，禁用/启用网络共享能力。  feature传入tethering，查询是否禁用网络共享能力。 |
| inactive\_user\_freeze | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入inactiveUserFreeze，禁用/启用非活跃用户运行能力。  feature传入inactiveUserFreeze，查询是否禁用非活跃用户运行能力。 |
| snapshot\_skip | [restrictions.addDisallowedListForAccount](js-apis-enterprise-restrictions.md#restrictionsadddisallowedlistforaccount14)  [restrictions.removeDisallowedListForAccount](js-apis-enterprise-restrictions.md#restrictionsremovedisallowedlistforaccount14)  [restrictions.getDisallowedListForAccount](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedlistforaccount14) | feature传入snapshotSkip，禁用屏幕快照能力的应用名单。  feature传入snapshotSkip，从禁用屏幕快照能力的应用名单中移除。  feature传入snapshotSkip，查询禁用屏幕快照能力的应用名单。 |
| password\_policy | [securityManager.setPasswordPolicy](js-apis-enterprise-securitymanager.md#securitymanagersetpasswordpolicy)  [securityManager.getPasswordPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetpasswordpolicy) | 设置设备锁屏口令策略。  获取设备锁屏口令策略。 |
| clipboard\_policy | [securityManager.setAppClipboardPolicy](js-apis-enterprise-securitymanager.md#securitymanagersetappclipboardpolicy)  [securityManager.getAppClipboardPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetappclipboardpolicy) | 设置设备剪贴板策略。  获取设备剪贴板策略。 |
| watermark\_image\_policy | [securityManager.setWatermarkImage](js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)  [securityManager.cancelWatermarkImage](js-apis-enterprise-securitymanager.md#securitymanagercancelwatermarkimage14) | 设置水印策略，当前仅支持PC/2in1使用。  取消水印策略，当前仅支持PC/2in1使用。 |
| ntp\_server | [systemManager.setNTPServer](js-apis-enterprise-systemmanager.md#systemmanagersetntpserver)  [systemManager.getNTPServer](js-apis-enterprise-systemmanager.md#systemmanagergetntpserver) | 设置NTP服务器的策略。  获取NTP服务器信息。 |
| set\_update\_policy | [systemManager.setOtaUpdatePolicy](js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)  [systemManager.getOtaUpdatePolicy](js-apis-enterprise-systemmanager.md#systemmanagergetotaupdatepolicy) | 设置升级策略。  查询升级策略。 |
| notify\_upgrade\_packages | [systemManager.notifyUpdatePackages](js-apis-enterprise-systemmanager.md#systemmanagernotifyupdatepackages)  [systemManager.getUpdateResult](js-apis-enterprise-systemmanager.md#systemmanagergetupdateresult) | 通知系统更新包信息。  获取系统更新结果。 |
| allowed\_usb\_devices | [usbManager.addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)  [usbManager.removeAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremoveallowedusbdevices)  [usbManager.getAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagergetallowedusbdevices) | 添加USB设备可用名单。  移除USB设备可用名单。  获取USB设备可用名单。 |
| usb\_read\_only | [usbManager.setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)  [usbManager.getUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagergetusbstoragedeviceaccesspolicy) | 设置USB存储设备访问策略。  获取USB存储设备访问策略。 |
| disallowed\_usb\_devices | [usbManager.addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)  [usbManager.removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)  [usbManager.getDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagergetdisallowedusbdevices14) | 添加禁止使用的USB设备类型。  移除禁止使用的USB设备类型。  获取禁止使用的USB设备类型。 |
| disallowed\_sms | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入sms，禁用/启用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。  feature传入sms，查询是否禁用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 |
| disallowed\_mms | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入mms，禁用/启用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。  feature传入mms，查询是否禁用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 |
| disable\_backup\_and\_restore | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入backupAndRestore，禁用/启用备份和恢复能力，当前仅支持手机、平板使用。  feature传入backupAndRestore，查询是否禁用备份和恢复能力，当前仅支持手机、平板使用。 |
| installed\_bundle\_info\_list | [bundleManager.getInstalledBundleList](js-apis-enterprise-bundlemanager.md#bundlemanagergetinstalledbundlelist20) | 获取设备指定用户下已安装应用列表。 |
| clear\_up\_application\_data | [applicationManager.clearUpApplicationData](js-apis-enterprise-applicationmanager.md#applicationmanagerclearupapplicationdata20) | 清除应用产生的所有数据。 |
| disallow\_unmute\_device | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入unmuteDevice，禁用/启用设备媒体播放声音能力。  feature传入unmuteDevice，查询是否禁用设备媒体播放声音能力。 |
| disabled\_hdc\_remote | [restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)  [restrictions.getDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionsgetdisallowedpolicy) | feature传入hdcRemote，禁用/启用设备通过hdc调试其他设备的能力。  feature传入hdcRemote，查询是否禁用设备通过hdc调试其他设备的能力。 |
