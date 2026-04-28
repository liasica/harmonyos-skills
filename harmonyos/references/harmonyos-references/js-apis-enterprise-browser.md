---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-browser
title: @ohos.enterprise.browser（浏览器管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.browser（浏览器管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9ae859fb294ed602c4e76a1381bd3b17af5897e513683d285f547fc9869492b
---

本模块提供浏览器管理能力，包括设置/取消浏览器策略、获取浏览器策略等。

浏览器策略指通过配置或管理浏览器行为的一系列规则和设置，以确保安全性、合规性、性能优化和用户体验的一致性。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { browser } from '@kit.MDMKit';
```

## browser.setPolicySync

PhonePC/2in1Tablet

setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void

为指定的浏览器设置浏览器子策略。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BROWSER\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appId | string | 是 | 应用ID，用于指定浏览器。 |
| policyName | string | 是 | 浏览器子策略名。当此值为空字符串时，表示设置应用ID对应的浏览器策略。 |
| policyValue | string | 是 | 浏览器子策略值。当此值为空字符串时，表示取消浏览器策略名对应浏览器子策略。 |

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
1. import { browser } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. // 此处参数appId的赋值应替换为开发者自己指定的浏览器的应用ID
11. let appId: string = 'com.example.******_******/******5t5CoBM=';
12. let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
13. let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

15. try {
16. browser.setPolicySync(wantTemp, appId, policyName, policyValue);
17. console.info('Succeeded in setting browser policies.');
18. } catch (err) {
19. console.error(`Failed to set browser policies. Code is ${err.code}, message is ${err.message}`);
20. }
```

## browser.getPoliciesSync

PhonePC/2in1Tablet

getPoliciesSync(admin: Want, appId: string): string

通过appid获取指定浏览器设置的策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| appId | string | 是 | 应用ID，用于指定浏览器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 浏览器策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { browser } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. // 此处参数appId的赋值应替换为开发者自己指定的浏览器的应用ID
11. let appId: string = 'com.example.******_******/******5t5CoBM=';

13. try {
14. let result: string = browser.getPoliciesSync(wantTemp, appId);
15. console.info(`Succeeded in getting browser policies, result : ${JSON.stringify(result)}`);
16. } catch(err) {
17. console.error(`Failed to get browser policies. Code is ${err.code}, message is ${err.message}`);
18. }
```

## browser.setManagedBrowserPolicy15+

PhonePC/2in1Tablet

setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void

为指定的浏览器设置浏览器策略，成功后会发布系统公共事件[COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED](commoneventmanager-definitions.md#common_event_managed_browser_policy_changed)。

**需要权限：** ohos.permission.ENTERPRISE\_SET\_BROWSER\_POLICY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，用于指定浏览器。 |
| policyName | string | 是 | 浏览器策略名。 |
| policyValue | string | 是 | 浏览器策略值。当此值为空字符串时，表示取消浏览器策略名对应浏览器子策略。 |

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
1. import { browser } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleName: string = 'com.example.testbrowser';
11. let policyName: string = 'InsecurePrivateNetworkRequestsAllowed';
12. let policyValue: string = '{"level":"mandatory","scope":"machine","source":"platform","value":true}';

14. try {
15. browser.setManagedBrowserPolicy(wantTemp, bundleName, policyName, policyValue);
16. console.info('Succeeded in setting managed browser policy.');
17. } catch (err) {
18. console.error(`Failed to set managed browser policy. Code is ${err.code}, message is ${err.message}`);
19. }
```

## browser.getManagedBrowserPolicy15+

PhonePC/2in1Tablet

getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer

通过应用包名获取指定浏览器的浏览器策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 应用包名，用于指定浏览器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 浏览器策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { browser } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { util } from '@kit.ArkTS';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. // 需根据实际情况进行替换
11. let bundleName: string = 'com.example.testbrowser';

13. try {
14. let buffer: ArrayBuffer = browser.getManagedBrowserPolicy(wantTemp, bundleName);
15. let intBuffer: Uint8Array = new Uint8Array(buffer);
16. let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
17. let stringData: string = decoder.decodeToString(intBuffer);
18. console.info(`Succeeded in getting managed browser policy, result : ${stringData}`);
19. } catch(err) {
20. console.error(`Failed to get managed browser policy. Code is ${err.code}, message is ${err.message}`);
21. }
```

## browser.getSelfManagedBrowserPolicyVersion15+

PhonePC/2in1Tablet

getSelfManagedBrowserPolicyVersion(): string

获取指定浏览器的浏览器策略版本。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 浏览器策略版本。 |

**示例：**

```
1. import { browser } from '@kit.MDMKit';

3. try {
4. let version: string = browser.getSelfManagedBrowserPolicyVersion();
5. console.info(`Succeeded in getting self managed browser policy version, result : ${version}`);
6. } catch(err) {
7. console.error(`Failed to get self managed browser policy version. Code is ${err.code}, message is ${err.message}`);
8. }
```

## browser.getSelfManagedBrowserPolicy15+

PhonePC/2in1Tablet

getSelfManagedBrowserPolicy(): ArrayBuffer

获取当前设备浏览器策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 浏览器策略。 |

**示例：**

```
1. import { browser } from '@kit.MDMKit';
2. import { util } from '@kit.ArkTS';

4. try {
5. let buffer: ArrayBuffer = browser.getSelfManagedBrowserPolicy();
6. let intBuffer: Uint8Array = new Uint8Array(buffer);
7. let decoder: util.TextDecoder = util.TextDecoder.create('utf-8');
8. let stringData: string = decoder.decodeToString(intBuffer);
9. console.info(`Succeeded in getting self managed browser policy, result : ${stringData}`);
10. } catch(err) {
11. console.error(`Failed to get self managed browser policy. Code is ${err.code}, message is ${err.message}`);
12. }
```
