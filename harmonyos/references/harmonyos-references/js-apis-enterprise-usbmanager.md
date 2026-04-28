---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-usbmanager
title: @ohos.enterprise.usbManager（USB管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.usbManager（USB管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2bec89b3ed542816727ed3e3d3f2fc37f3027e0be87d92e52ebb4c2d9704623
---

本模块提供USB管理能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

全局通用限制类策略由restrictions统一提供，若要全局禁用USB，请参考[@ohos.enterprise.restrictions（限制类策略）](js-apis-enterprise-restrictions.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { usbManager } from '@kit.MDMKit';
```

## usbManager.addAllowedUsbDevices

PhonePC/2in1Tablet

addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

添加USB设备可用名单。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
2. 已经通过[setUsbStorageDeviceAccessPolicy](js-apis-enterprise-usbmanager.md#usbmanagersetusbstoragedeviceaccesspolicy)接口设置了USB存储设备访问策略为禁用。
3. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加了禁止使用的USB设备类型。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

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
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
11. vendorId: 1,
12. productId: 1
13. }];
14. usbManager.addAllowedUsbDevices(wantTemp, usbDeviceIds);
15. console.info(`Succeeded in adding allowed USB devices.`);
16. } catch (err) {
17. console.error(`Failed to add allowed USB devices. Code: ${err.code}, message: ${err.message}`);
18. }
```

## usbManager.removeAllowedUsbDevices

PhonePC/2in1Tablet

removeAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void

移除USB设备可用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

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

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let usbDeviceIds: Array<usbManager.UsbDeviceId> = [{
11. vendorId: 1,
12. productId: 1
13. }];
14. usbManager.removeAllowedUsbDevices(wantTemp, usbDeviceIds);
15. console.info(`Succeeded in removing allowed USB devices.`);
16. } catch (err) {
17. console.error(`Failed to remove allowed USB devices. Code: ${err.code}, message: ${err.message}`);
18. }
```

## usbManager.getAllowedUsbDevices

PhonePC/2in1Tablet

getAllowedUsbDevices(admin: Want): Array<UsbDeviceId>

获取USB设备可用名单。

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
| Array<[UsbDeviceId](js-apis-enterprise-usbmanager.md#usbdeviceid)> | 可用USB允许名单设备ID数组。 |

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
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: Array<usbManager.UsbDeviceId> = usbManager.getAllowedUsbDevices(wantTemp);
11. console.info(`Succeeded in getting allowed USB devices. Result: ${JSON.stringify(result)}`);
12. } catch (err) {
13. console.error(`Failed to get allowed USB devices. Code: ${err.code}, message: ${err.message}`);
14. }
```

## usbManager.setUsbStorageDeviceAccessPolicy

PhonePC/2in1Tablet

setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void

设置USB存储设备访问策略。

说明

在调用接口前，确保已暂停USB存储设备的读写操作，保证操作的稳定性和数据的完整性，否则可能出现不可预期的异常。

以下情况下，通过本接口设置USB存储设备访问策略为可读可写/只读，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
2. 已经通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口将存储类型的USB设备添加为禁止使用的USB设备类型。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

以下情况下，通过本接口设置USB存储设备访问策略为禁用，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
2. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

通过本接口设置，或者通过[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)接口添加存储类型的USB设备，均可禁用USB存储设备。推荐使用后者。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控), 严格优先级： 禁用 > 只读 > 可读可写。

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
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let policy: usbManager.UsbPolicy = usbManager.UsbPolicy.DISABLED;
11. usbManager.setUsbStorageDeviceAccessPolicy(wantTemp, policy);
12. console.info(`Succeeded in setting USB storage device access policy.`);
13. } catch (err) {
14. console.error(`Failed to set USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
15. }
```

## usbManager.getUsbStorageDeviceAccessPolicy

PhonePC/2in1Tablet

getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy

获取USB存储设备访问策略。

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
| [UsbPolicy](js-apis-enterprise-usbmanager.md#usbpolicy) | USB存储设备访问策略。 |

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
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(wantTemp);
11. console.info(`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}`);
12. } catch (err) {
13. console.error(`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
14. }
```

## usbManager.addDisallowedUsbDevices14+

PhonePC/2in1Tablet

addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

添加禁止使用的USB设备类型。

以下情况下，调用本接口会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备USB能力。
2. 已经通过[addAllowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageraddallowedusbdevices)接口添加了USB设备可用名单。
3. 已经通过[setDisallowedPolicyForAccount](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14)接口禁用了某用户USB存储设备写入能力。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

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

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let usbDevices: Array<usbManager.UsbDeviceType> = [{
11. baseClass: 8,
12. subClass: 0,
13. protocol: 0,
14. descriptor: usbManager.Descriptor.INTERFACE
15. }];
16. usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
17. console.info(`Succeeded in adding disallowed USB devices.`);
18. } catch (err) {
19. console.error(`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
20. }
```

## usbManager.removeDisallowedUsbDevices14+

PhonePC/2in1Tablet

removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void

移除禁止使用的USB设备类型。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USB

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

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

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let usbDevices: Array<usbManager.UsbDeviceType> = [{
11. baseClass: 8,
12. subClass: 0,
13. protocol: 0,
14. descriptor: usbManager.Descriptor.INTERFACE
15. }];
16. usbManager.removeDisallowedUsbDevices(wantTemp, usbDevices);
17. console.info(`Succeeded in removing disallowed USB devices.`);
18. } catch (err) {
19. console.error(`Failed to remove disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
20. }
```

## usbManager.getDisallowedUsbDevices14+

PhonePC/2in1Tablet

getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>

获取禁止使用的USB设备类型。

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

```
1. import { usbManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: Array<usbManager.UsbDeviceType> = usbManager.getDisallowedUsbDevices(wantTemp);
11. console.info(`Succeeded in getting disallowed USB devices. Result: ${JSON.stringify(result)}`);
12. } catch (err) {
13. console.error(`Failed to get disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
14. }
```

## UsbDeviceId

PhonePC/2in1Tablet

USB设备ID信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| vendorId | number | 否 | 否 | 厂商ID。 |
| productId | number | 否 | 否 | 产品ID。 |

## UsbDeviceType14+

PhonePC/2in1Tablet

USB设备类型信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| baseClass | number | 否 | 否 | 类型编码。  可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。  先根据此值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.clazz字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.clazz字段值。  若字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| subClass | number | 否 | 否 | 子类型编码。  可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。  先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.subClass字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.subClass字段值。  若字段值为255，表示此设备的子类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| protocol | number | 否 | 否 | 协议编码。  可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。  先根据baseClass的值确定descriptor应该传入的类型。若descriptor为DEVICE，则本字段取USBDevice.protocol字段值，若descriptor为INTERFACE，则本字段取USBDevice.configs.interfaces.protocol字段值。  若字段值为255，表示此设备的协议编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若字段值未在[defined-class-codes](https://www.usb.org/defined-class-codes)中定义，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效。 |
| descriptor | [Descriptor](js-apis-enterprise-usbmanager.md#descriptor14) | 否 | 否 | USB描述符。  可通过[getDevices](js-apis-usbmanager.md#usbmanagergetdevices)接口获取已接入主设备的USB设备列表，需在返回值列表中查找当前设备，查看其值。  若此值USBDevice.clazz字段值为0，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找此值USBDevice.configs.interfaces.clazz字段值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）;  若此值USBDevice.clazz字段值为255，表示此设备的类型编码是厂商自定义编码，则使用[addDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)/[removeDisallowedUsbDevices](js-apis-enterprise-usbmanager.md#usbmanagerremovedisallowedusbdevices14)接口禁用/解禁该设备不生效；若此值USBDevice.clazz字段值为其他值，则须在[defined-class-codes](https://www.usb.org/defined-class-codes)中的Base Class列查找该值，查找结果所在行所对应的Descriptor Usage列就表示当前应该传入的descriptor类型（若Descriptor Usage列为Both，表示两种类型都可以传入，需要设备级禁用时传入DEVICE，需要接口级禁用时传入INTERFACE）。 |

## UsbPolicy

PhonePC/2in1Tablet

USB读写策略的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| READ\_WRITE | 0 | 可读可写。 |
| READ\_ONLY | 1 | 只读。 |
| DISABLED | 2 | 禁用。 |

## Descriptor14+

PhonePC/2in1Tablet

USB描述符的枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERFACE | 0 | 接口描述符。 |
| DEVICE | 1 | 设备描述符。 |
