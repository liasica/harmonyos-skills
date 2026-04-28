---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-bundlemanager
title: @ohos.enterprise.bundleManager（包管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.bundleManager（包管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38cb4eb3dc0df71779f84ae8867c09f1117cb4b39b74edc68c05f36eaf361f49
---

本模块提供包管理能力，包括添加包安装允许名单、获取包安装允许名单、移除包安装允许名单等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { bundleManager } from '@kit.MDMKit';
```

## bundleManager.addAllowedInstallBundlesSync

PhonePC/2in1Tablet

addAllowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

添加应用至应用程序包安装允许名单，添加至允许名单的应用允许在当前/指定用户下安装，其它非允许名单应用不允许安装。系统应用卸载后重新安装不会受到接口限制；而普通应用在卸载后重新安装时，则会受到接口限制。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  **说明：** 从API version 21版本开始，支持传入应用的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，推荐使用[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。API version 20及之前版本，仅支持[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. bundleManager.addAllowedInstallBundlesSync(wantTemp, appIds, 100);
14. console.info('Succeeded in adding allowed install bundles.');
15. } catch (err) {
16. console.error(`Failed to add allowed install bundles. Code is ${err.code}, message is ${err.message}`);
17. }
```

## bundleManager.removeAllowedInstallBundlesSync

PhonePC/2in1Tablet

removeAllowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

在应用程序包安装允许名单中移除应用，在允许名单存在的情况下，不在应用程序包安装允许名单中的应用不允许在当前/指定用户下安装。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  **说明：** 从API version 21版本开始，数组中的元素支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，仅移除传入的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)（或[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)），不会移除同一应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（或[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)）。API version 20及之前版本，数组中的元素只支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. bundleManager.removeAllowedInstallBundlesSync(wantTemp, appIds, 100);
14. console.info('Succeeded in removing allowed install bundles.');
15. } catch (err) {
16. console.error(`Failed to remove allowed install bundles. Code is ${err.code}, message is ${err.message}`);
17. }
```

## bundleManager.getAllowedInstallBundlesSync

PhonePC/2in1Tablet

getAllowedInstallBundlesSync(admin: Want, accountId?: number): Array<string>

获取当前/指定用户下的应用程序包安装允许名单。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前用户下的应用程序包安装允许名单。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: Array<string> = bundleManager.getAllowedInstallBundlesSync(wantTemp, 100);
12. console.info(`Succeeded in getting allowed install bundles, result : ${JSON.stringify(result)}`);
13. } catch (err) {
14. console.error(`Failed to get allowed install bundles. Code is ${err.code}, message is ${err.message}`);
15. }
```

## bundleManager.addDisallowedInstallBundlesSync

PhonePC/2in1Tablet

addDisallowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

添加应用至应用程序包安装禁止名单，添加至禁止名单的应用不允许在当前/指定用户下安装。系统应用卸载后重新安装不会受到接口限制；而普通应用在卸载后重新安装时，则会受到接口限制。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  **说明：** 从API version 21版本开始，支持传入应用的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，推荐使用[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。API version 20及之前版本，仅支持[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. bundleManager.addDisallowedInstallBundlesSync(wantTemp, appIds, 100);
14. console.info('Succeeded in adding disallowed install bundles.');
15. } catch (err) {
16. console.error(`Failed to add disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
17. }
```

## bundleManager.removeDisallowedInstallBundlesSync

PhonePC/2in1Tablet

removeDisallowedInstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

在应用程序包安装禁止名单中移除应用，在禁止名单存在的情况下，在应用程序包安装禁止名单中的应用不允许在当前/指定用户下安装。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  **说明：** 从API version 21版本开始，数组中的元素支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，仅移除传入的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)（或[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)），不会移除同一应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（或[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)）。API version 20及之前版本，数组中的元素只支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. bundleManager.removeDisallowedInstallBundlesSync(wantTemp, appIds, 100)
14. console.info('Succeeded in removing disallowed install bundles.');
15. } catch (err) {
16. console.error(`Failed to remove disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
17. }
```

## bundleManager.getDisallowedInstallBundlesSync

PhonePC/2in1Tablet

getDisallowedInstallBundlesSync(admin: Want, accountId?: number): Array<string>

获取当前/指定用户下的应用程序包安装禁止名单。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前用户下的应用程序包安装禁止名单。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: Array<string> = bundleManager.getDisallowedInstallBundlesSync(wantTemp, 100);
13. console.info(`Succeeded in getting disallowed install bundles, result : ${JSON.stringify(result)}`);
14. } catch (err) {
15. console.error(`Failed to get disallowed install bundles. Code is ${err.code}, message is ${err.message}`);
16. }
```

## bundleManager.addDisallowedUninstallBundlesSync

PhonePC/2in1Tablet

addDisallowedUninstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

添加应用至包卸载禁止名单，添加至禁止名单的应用不允许在当前/指定用户下卸载。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  取值范围：单个用户下该名单总数不能超过200。例如100用户下已经设置了50个、101用户未设置，则100用户还能再设置150个，101用户还能再设置200个。不建议一次性设置个数大于50个，可能引入性能问题。  **说明：** 从API version 21版本开始，支持传入应用的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，推荐使用[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。API version 20及之前版本，仅支持[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. // 参数需根据实际情况进行替换
14. bundleManager.addDisallowedUninstallBundlesSync(wantTemp, appIds, 100);
15. console.info('Succeeded in adding disallowed uninstall bundles.');
16. } catch (err) {
17. console.error(`Failed to add disallowed uninstall bundles. Code is ${err.code}, message is ${err.message}`);
18. }
```

## bundleManager.removeDisallowedUninstallBundlesSync

PhonePC/2in1Tablet

removeDisallowedUninstallBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void

在包卸载禁止名单中移除应用。在禁止名单存在的情况下，在包卸载禁止名单中的应用不允许在当前/指定用户下卸载。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appIds | Array<string> | 是 | 应用ID数组。  取值范围：不建议一次性设置个数大于50个，可能引入性能问题。  **说明：** 从API version 21版本开始，数组中的元素支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)，仅移除传入的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)（或[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)），不会移除同一应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（或[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)）。API version 20及之前版本，数组中的元素只支持使用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let appIds: Array<string> = ['com.example.******_******/******5t5CoBM='];

12. try {
13. // 参数需根据实际情况进行替换
14. bundleManager.removeDisallowedUninstallBundlesSync(wantTemp, appIds, 100);
15. console.info('Succeeded in removing disallowed uninstall bundles.');
16. } catch (err) {
17. console.error(`Failed to remove disallowed uninstall bundles. Code is ${err.code}, message is ${err.message}`);
18. }
```

## bundleManager.getDisallowedUninstallBundlesSync

PhonePC/2in1Tablet

getDisallowedUninstallBundlesSync(admin: Want, accountId?: number): Array<string>

获取当前/指定用户下包卸载禁止名单。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 否 | 用户ID，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。  - 调用接口时，若传入accountId，表示指定用户。  - 调用接口时，若未传入accountId，表示当前用户。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前用户下的包卸载禁止名单。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. // 参数需根据实际情况进行替换
12. let result: Array<String> = bundleManager.getDisallowedUninstallBundlesSync(wantTemp, 100);
13. console.info(`Succeeded in getting disallowed uninstall bundles, result : ${JSON.stringify(result)}`);
14. } catch (err) {
15. console.error(`Failed to get disallowed uninstall bundles. Code is ${err.code}, message is ${err.message}`);
16. }
```

## bundleManager.uninstall

PhonePC/2in1Tablet

uninstall(admin: Want, bundleName: string, userId?: number, isKeepData?: boolean): Promise<void>

卸载当前/指定用户下的指定包接口，选择是否保留包数据（由isKeepData指定）。使用promise异步回调。

说明

当应用为不可卸载的预置应用或者通过[addDisallowedUninstallBundlesSync](js-apis-enterprise-bundlemanager.md#bundlemanageradddisalloweduninstallbundlessync)接口设置了不允许卸载时，调用此接口卸载应用会返回401错误码。

**需要权限：** ohos.permission.ENTERPRISE\_INSTALL\_BUNDLE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用程序包名。 |
| userId | number | 否 | 用户ID，取值范围：大于等于0。  - 调用接口时，若传入userId，表示指定用户。  - 调用接口时，若未传入userId，表示当前用户。 |
| isKeepData | boolean | 否 | 是否保留包数据，true表示保留，false表示不保留。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当包卸载失败时抛出错误对象。 |

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
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };

11. // 参数需根据实际情况进行替换
12. bundleManager.uninstall(wantTemp, 'bundleName', 100, true).then(() => {
13. console.info('Succeeded in uninstalling bundles.');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to uninstall bundles. Code is ${err.code}, message is ${err.message}`);
16. });
```

## bundleManager.install

PhonePC/2in1Tablet

install(admin: Want, hapFilePaths: Array<string>, installParam?: InstallParam): Promise<void>

安装指定路径下的应用包。使用promise异步回调。

此接口只能安装分发类型为enterprise\_mdm（MDM应用）和enterprise\_normal（普通企业应用）类型的应用，可以通过[getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口查询应用自身的[BundleInfo](js-apis-bundlemanager-bundleinfo.md)，其中BundleInfo.appInfo.appDistributionType为应用的分发类型。

说明

该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**需要权限：** ohos.permission.ENTERPRISE\_INSTALL\_BUNDLE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| hapFilePaths | Array<string> | 是 | 待安装应用包路径数组。应用包路径为应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径。 |
| installParam | [InstallParam](js-apis-enterprise-bundlemanager.md#installparam) | 否 | 应用包安装参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当应用程序包安装失败时，抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201002 | Failed to install the application. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 为当前用户安装应用
6. let wantTemp: Want = {
7. // 需根据实际情况进行替换
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EnterpriseAdminAbility'
10. };
11. // 需根据实际情况进行替换
12. let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];

14. bundleManager.install(wantTemp, hapFilePaths).then(() => {
15. console.info('Succeeded in installing bundles.');
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
18. });
```

```
1. import { bundleManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 为所有用户安装应用
6. let wantTemp: Want = {
7. // 需根据实际情况进行替换
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EnterpriseAdminAbility'
10. };
11. // 需根据实际情况进行替换
12. let hapFilePaths: Array<string> = ['/data/storage/el2/base/haps/entry/testinstall/ExtensionTest.hap'];
13. const params: Record<string, string> = {
14. 'ohos.bms.param.enterpriseForAllUser': 'true'
15. };
16. let installParam: bundleManager.InstallParam = {
17. // 需根据实际情况进行替换
18. userId: 100,
19. installFlag: 0,
20. parameters: params
21. };
22. bundleManager.install(wantTemp, hapFilePaths, installParam).then(() => {
23. console.info('Succeeded in installing bundles.');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to install bundles. Code is ${err.code}, message is ${err.message}`);
26. });
```

## bundleManager.getInstalledBundleList20+

PhonePC/2in1Tablet

getInstalledBundleList(admin: Want, accountId: number): Promise<Array<BundleInfo>>

获取设备指定用户下已安装应用列表。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_GET\_ALL\_BUNDLE\_INFO

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值为正整数，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[BundleInfo](js-apis-enterprise-bundlemanager.md#bundleinfo20)>> | Promise对象，返回已安装应用包信息。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { bundleManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. // 需根据实际情况进行替换
11. let accountId: number = 100;
12. bundleManager.getInstalledBundleList(wantTemp, accountId).then((result) => {
13. console.info('Succeeded in getting installed bundle list.');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get installed bundle list. Code is ${err.code}, message is ${err.message}`);
16. });
```

## bundleManager.getInstalledBundleList23+

PhonePC/2in1Tablet

getInstalledBundleList(admin: Want, accountId: number, bundleInfoGetFlag: number): Promise<Array<BundleInfo>>

根据给定的bundleInfoGetFlag获取设备指定用户下已安装应用列表。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_GET\_ALL\_BUNDLE\_INFO

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值为正整数，取值范围：大于等于0。  accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| [bundleInfoGetFlag](js-apis-enterprise-bundlemanager.md#bundleinfogetflag23) | number | 是 | 指定返回的BundleInfo所包含的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[BundleInfo](js-apis-enterprise-bundlemanager.md#bundleinfo20)>> | Promise对象，返回已安装应用包信息。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { bundleManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. // 需根据实际情况进行替换
11. let accountId: number = 100;
12. let bundleInfoGetFlag: number = bundleManager.BundleInfoGetFlag.WITH_APPLICATION_INFO
13. | bundleManager.BundleInfoGetFlag.WITH_SIGNATURE_INFO;
14. bundleManager.getInstalledBundleList(wantTemp, accountId, bundleInfoGetFlag).then((result) => {
15. console.info('Succeeded in getting installed bundle list.');
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to get installed bundle list. Code is ${err.code}, message is ${err.message}`);
18. });
```

## bundleManager.addInstallationAllowedAppDistributionTypes20+

PhonePC/2in1Tablet

addInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void

添加可安装应用的分发类型。添加成功后，当前设备可以安装对应分发类型的应用，但无法安装[AppDistributionType](js-apis-enterprise-bundlemanager.md#appdistributiontype20)中未添加的分发类型的应用。

应用程序签名证书的分发类型详细介绍请参见[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)的appDistributionType属性。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appDistributionTypes | Array<[AppDistributionType](js-apis-enterprise-bundlemanager.md#appdistributiontype20)> | 是 | 应用程序签名证书的分发类型数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bundleManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let appDistributionTypes: Array<bundleManager.AppDistributionType> = [bundleManager.AppDistributionType.APP_GALLERY];
11. bundleManager.addInstallationAllowedAppDistributionTypes(wantTemp, appDistributionTypes);
12. console.info('Succeeded in adding allowed appDistributionTypes.');
13. } catch (err) {
14. console.error(`Failed to add allowed appDistributionTypes. Code: ${err.code}, message: ${err.message}`);
15. }
```

## bundleManager.removeInstallationAllowedAppDistributionTypes20+

PhonePC/2in1Tablet

removeInstallationAllowedAppDistributionTypes(admin: Want, appDistributionTypes: Array<AppDistributionType>): void

移除应用的分发类型。若只移除了数组中部分的分发类型，则当前设备可以安装数组中剩下的分发类型的应用，但无法安装[AppDistributionType](js-apis-enterprise-bundlemanager.md#appdistributiontype20)中未添加的分发类型的应用。

应用程序签名证书的分发类型详细介绍请参见[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)的appDistributionType属性。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appDistributionTypes | Array<[AppDistributionType](js-apis-enterprise-bundlemanager.md#appdistributiontype20)> | 是 | 应用程序签名证书的分发类型数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bundleManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let appDistributionTypes: Array<bundleManager.AppDistributionType> = [bundleManager.AppDistributionType.APP_GALLERY];
11. bundleManager.removeInstallationAllowedAppDistributionTypes(wantTemp, appDistributionTypes);
12. console.info('Succeeded in removing allowed appDistributionTypes.');
13. } catch (err) {
14. console.error(`Failed to remove allowed appDistributionTypes. Code: ${err.code}, message: ${err.message}`);
15. }
```

## bundleManager.getInstallationAllowedAppDistributionTypes20+

PhonePC/2in1Tablet

getInstallationAllowedAppDistributionTypes(admin: Want): Array<AppDistributionType>

获取可安装的应用程序签名证书的分发类型。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BUNDLE\_INSTALL\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[AppDistributionType](js-apis-enterprise-bundlemanager.md#appdistributiontype20)> | 应用程序签名证书的分发类型数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bundleManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.edmtest',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let result: Array<bundleManager.AppDistributionType> = bundleManager.getInstallationAllowedAppDistributionTypes(wantTemp);
11. console.info(`Succeeded in getting allowed appDistributionTypes. Result: ${JSON.stringify(result)}`);
12. } catch (err) {
13. console.error(`Failed to get allowed appDistributionTypes. Code: ${err.code}, message: ${err.message}`);
14. }
```

## bundleManager.installMarketApps22+

PhonePC/2in1Tablet

installMarketApps(admin: Want, bundleNames: Array<string>): void

下载并安装应用市场应用。

说明

本接口调用成功后会在桌面上生成应用下载任务，此任务与从应用市场下载所创建任务一致。下载安装结束后，安装结果会通过回调[EnterpriseAdminExtensionAbility.onMarketAppInstallResult](js-apis-enterpriseadminextensionability.md#onmarketappinstallresult22)返回。

**注意事项：**

1、调用该接口时必须保证网络畅通，否则会抛出9201002错误码。

2、传入的包名必须是应用市场已上架的应用包名，并且需要[在HEM平台上加入企业应用](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_equipment_app-management-0000002468952084)

3、调用此接口前，此设备必须通过[HEM部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。

**需要权限：** ohos.permission.ENTERPRISE\_INSTALL\_BUNDLE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleNames | Array<string> | 是 | 应用包名列表，一次最多传入10个。包名需与应用市场中包名一致，否则无法创建下载任务，并抛出错误码9201002。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201002 | Failed to install the application. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { bundleManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleNames: Array<string> = [ 'com.huaweicloud.m' ];
11. try {
12. bundleManager.installMarketApps(wantTemp, bundleNames);
13. console.info(`Succeeded in installing market apps.`);
14. } catch(err) {
15. console.error(`Failed to install market apps. Code: ${err.code}, message: ${err.message}`);
16. }
```

## InstallParam

PhonePC/2in1Tablet

应用包安装需指定的参数信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| userId | number | 否 | 是 | 指示用户id，默认值：调用方所在用户，取值范围：大于等于0。 |
| installFlag | number | 否 | 是 | 安装标志。枚举值：0：应用初次安装，1：应用覆盖安装，2：应用免安装，默认值为应用初次安装。 |
| parameters19+ | Record<string, string> | 否 | 是 | 扩展参数，默认值为空。key取值支持"ohos.bms.param.enterpriseForAllUser"，若对应的value值为"true"，表示为所有用户安装应用。 |

## AppDistributionType20+

PhonePC/2in1Tablet

应用程序签名证书的分发类型。详细介绍请参见[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)的appDistributionType属性。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP\_GALLERY | 1 | 应用市场安装的应用。 |
| ENTERPRISE | 2 | 企业应用。 |
| ENTERPRISE\_NORMAL | 3 | 普通企业应用。 |
| ENTERPRISE\_MDM | 4 | 企业MDM应用。 |
| INTERNALTESTING | 5 | 应用市场内测的应用。 |
| CROWDTESTING | 6 | 众包测试应用。 |

## BundleInfo20+

PhonePC/2in1Tablet

描述应用包信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 应用包的名称，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的bundleName字段。 |
| vendor | string | 是 | 否 | 应用包的供应商，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的vendor字段。 |
| versionCode | number | 是 | 否 | 应用包的版本号，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的versionCode字段。 |
| versionName | string | 是 | 否 | 应用包的版本文本描述信息，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的versionName字段。 |
| minCompatibleVersionCode | number | 是 | 否 | 分布式场景下的应用包兼容的最低版本，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的minCompatibleVersionCode字段。 |
| targetVersion | number | 是 | 否 | 应用运行目标版本，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的targetAPIVersion字段。 |
| appInfo | [ApplicationInfo](js-apis-enterprise-bundlemanager.md#applicationinfo20) | 是 | 否 | 应用程序的配置信息。 |
| signatureInfo | [SignatureInfo](js-apis-enterprise-bundlemanager.md#signatureinfo20) | 是 | 否 | 应用包的签名信息。 |
| installTime | number | 是 | 否 | 应用包安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。 |
| updateTime | number | 是 | 否 | 应用包更新时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒。 |
| appIndex | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。 |
| firstInstallTime | number | 是 | 是 | 应用在当前设备的首次安装时间戳，表示从1970-01-01 08:00:00 UTC+8逝去的毫秒数，单位毫秒，预置应用的首次安装时间戳为1533657660000。 |

## SignatureInfo20+

PhonePC/2in1Tablet

描述应用包的签名信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appId | string | 是 | 否 | 应用的appId，表示应用的唯一标识，详情信息可参考[什么是appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)。 |
| fingerprint | string | 是 | 否 | 应用包的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。 |
| appIdentifier | string | 是 | 否 | 应用的唯一标识。详情信息可参考[什么是appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。 |
| certificate | string | 是 | 是 | 应用的证书公钥。 |

## ApplicationInfo20+

PhonePC/2in1Tablet

应用程序信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 应用包的名称，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的bundleName字段。 |
| description | string | 是 | 否 | 标识应用的描述信息，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的description字段。关于description的详细信息详见本表中的descriptionResource字段说明。 |
| descriptionId | number | 是 | 否 | 标识应用的描述信息的资源id，是编译构建时根据应用配置的description自动生成的资源id。 |
| enabled | boolean | 是 | 否 | 判断应用程序是否可以使用，取值为true表示可以使用，取值为false表示不可使用。 |
| label | string | 是 | 否 | 标识应用的名称。 |
| labelId | number | 是 | 否 | 标识应用名称的资源id，是编译构建时根据应用配置的label自动生成的资源id。 |
| icon | string | 是 | 否 | 应用程序的图标，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的icon字段。关于icon的详细信息详见本表中的iconResource字段说明。 |
| iconData23+ | string | 是 | 否 | 应用程序的图标，为base64编码格式。 |
| iconId | number | 是 | 否 | 应用程序图标的资源id，是编译构建时根据应用配置的icon自动生成的资源id。 |
| process | string | 是 | 否 | 应用程序的进程名称。 |
| codePath | string | 是 | 否 | 应用程序的安装目录。 |
| removable | boolean | 是 | 否 | 应用程序是否可以被移除，取值为true表示可以被移除，取值为false表示不可以被移除。 |
| accessTokenId | number | 是 | 否 | 应用程序的accessTokenId，应用的身份标识，在[程序访问控制校验接口](js-apis-abilityaccessctrl.md#checkaccesstoken9)中使用。 |
| uid | number | 是 | 否 | 应用程序的UID。 |
| iconResource | [Resource](js-apis-enterprise-bundlemanager.md#resource20) | 是 | 否 | 应用程序的图标资源信息，包含了该资源的信息的bundleName、moduleName和id。 |
| labelResource | [Resource](js-apis-enterprise-bundlemanager.md#resource20) | 是 | 否 | 应用程序的标签资源信息，包含了该资源的信息的bundleName、moduleName和id。 |
| descriptionResource | [Resource](js-apis-enterprise-bundlemanager.md#resource20) | 是 | 否 | 应用程序的描述资源信息，包含了该资源的信息的bundleName、moduleName和id。 |
| appDistributionType | string | 是 | 否 | 应用程序签名证书的分发类型，详细信息请参考[ApplicationInfo](js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)的appProvisionType字段。 |
| appProvisionType | string | 是 | 否 | 应用程序签名证书文件的类型，分为debug和release两种类型。 |
| systemApp | boolean | 是 | 否 | 标识应用是否为系统应用，取值为true表示系统应用，取值为false表示非系统应用。 |
| debug | boolean | 是 | 否 | 标识应用是否处于调试模式，取值为true表示应用处于调试模式，取值为false表示应用处于非调试模式。 |
| dataUnclearable | boolean | 是 | 否 | 标识应用数据是否可被删除。true表示不可删除，false表示可以删除。 |
| nativeLibraryPath | string | 是 | 否 | 应用程序的本地库文件路径。 |
| appIndex | number | 是 | 否 | 应用包的分身索引标识，仅在分身应用中生效。 |
| installSource | string | 是 | 否 | 应用程序的安装来源，支持的取值如下：  - pre-installed表示应用为第一次开机时安装的预置应用。  - ota表示应用为系统升级时新增的预置应用。  - recovery表示卸载后再恢复的预置应用。  - bundleName表示应用由此包名对应的应用安装。  - unknown表示应用安装来源未知。 |
| releaseType | string | 是 | 否 | 标识应用打包时使用的SDK的发布类型。当前SDK的发布类型可能为Canary、Beta、Release，其中Canary和Beta可能通过序号进一步细分，例如Canary1、Canary2、Beta1、Beta2等。开发者可通过对比应用打包依赖的SDK发布类型和OS的发布类型（[deviceInfo.distributionOSReleaseType](js-apis-device-info.md)）来判断兼容性。 |

## Resource20+

PhonePC/2in1Tablet

资源相关信息，包括应用包名、应用模块名、资源id。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用的bundle名称。 |
| moduleName | string | 否 | 否 | 应用的module名称。 |
| id | number | 否 | 否 | 资源的id值。 |

## BundleInfoGetFlag23+

PhonePC/2in1Tablet

包信息获取标志，指示需要获取的包信息的内容。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 用于获取默认包信息，不包含applicationInfo、signatureInfo的信息。 |
| WITH\_APPLICATION\_INFO | 1 << 0 | 用于获取默认包信息和applicationInfo的信息，获取的applicationInfo中不包含iconData的信息。 |
| WITH\_SIGNATURE\_INFO | 1 << 1 | 用于获取默认包信息和signatureInfo的信息。 |
| WITH\_APPLICATION\_ICON\_INFO | 1 << 2 | 用于获取默认包信息和applicationInfo的iconData信息。 |
