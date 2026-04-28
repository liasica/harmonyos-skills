---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-telephonymanager
title: @ohos.enterprise.telephonyManager（通话管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.telephonyManager（通话管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b5de68acd58e993de74016559a35cd6f80180c0b9aa258d1f59815215a75646
---

本模块提供通话管理能力。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅适用于Stage模型。

本模块接口仅对设备管理应用开放，调用接口前需激活该应用，详情请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

全局通用限制类策略由restrictions提供，若要全局禁用通话，请参考[@ohos.enterprise.restrictions（限制类策略）](js-apis-enterprise-restrictions.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { telephonyManager } from '@kit.MDMKit';
```

## telephonyManager.setSimDisabled

PhonePC/2in1Tablet

setSimDisabled(admin: Want, slotId: number): void

禁用指定卡槽的SIM卡。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| slotId | number | 是 | 卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。 |

**错误码**：

请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let slotId: number = 0;
11. telephonyManager.setSimDisabled(wantTemp, slotId);
12. console.info(`Succeeded in setting slotId: ${slotId} disabled.`);
13. } catch (err) {
14. console.error(`Failed to set slotId disabled. Code: ${err.code}, message: ${err.message}`);
15. }
```

## telephonyManager.setSimEnabled

PhonePC/2in1Tablet

setSimEnabled(admin: Want, slotId: number): void

解除指定卡槽的SIM卡禁用。使用setSimDisabled禁用SIM卡后，再用setSimEnabled启用SIM卡，需要到设置-移动网络-SIM卡管理界面手动打开SIM卡开关。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| slotId | number | 是 | 卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。 |

**错误码**：

请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let slotId: number = 0;
11. telephonyManager.setSimEnabled(wantTemp, slotId);
12. console.info(`Succeeded in setting slotId: ${slotId} enabled.`);
13. } catch (err) {
14. console.error(`Failed to set slotId enabled. Code: ${err.code}, message: ${err.message}`);
15. }
```

## telephonyManager.isSimDisabled

PhonePC/2in1Tablet

isSimDisabled(admin: Want, slotId: number): boolean

查询指定卡槽是否禁用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| slotId | number | 是 | 卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 指定卡槽的禁用状态。true表示已被禁用，false表示未被禁用。 |

**错误码**：

请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let slotId: number = 0;
11. let result: boolean = telephonyManager.isSimDisabled(wantTemp, slotId);
12. console.info(`Succeeded in querying slotId: ${slotId} is disabled or not, result: ${result}`);
13. } catch (err) {
14. console.error(`Failed to query sim is disabled or not. Code: ${err.code}, message: ${err.message}`);
15. }
```

## telephonyManager.addOutgoingCallPolicyNumbers

PhonePC/2in1Tablet

addOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

添加通话呼出的允许或禁用名单，如果不添加名单，任意号码都可以呼出，添加后只有名单内的号码允许或禁止呼出。

以下情况下，通过本接口添加通话呼出的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口添加通话呼出的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。
2. 已经通过本接口设置了通话呼出的禁用名单，再通过本接口添加通话呼出允许名单，返回9200010错误码。通过[removeOutgoingCallPolicyNumbers](js-apis-enterprise-telephonymanager.md#telephonymanagerremoveoutgoingcallpolicynumbers)接口将之前设置的通话呼出禁用名单移除后，可解除冲突。
3. 已经通过本接口设置了通话呼出的允许名单，再通过本接口添加通话呼出禁用名单，返回9200010错误码。通过[removeOutgoingCallPolicyNumbers](js-apis-enterprise-telephonymanager.md#telephonymanagerremoveoutgoingcallpolicynumbers)接口将之前设置的通话呼出允许名单移除后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |
| numbers | Array<string> | 是 | 通话号码列表，当前仅支持全号码匹配。数组总长度不能超过1000。例如，若当前允许名单数组中已有100个号码，则最多支持通过该接口再添加900个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = [
13. // 需根据实际情况进行替换
14. "13112345678"
15. ];
16. telephonyManager.addOutgoingCallPolicyNumbers(wantTemp, policy, numbers);
17. console.info('Succeeded in adding outgoing call policy.');
18. } catch (err) {
19. console.error(`Failed to add outgoing call policy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## telephonyManager.removeOutgoingCallPolicyNumbers

PhonePC/2in1Tablet

removeOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

移除通话呼出的允许或禁用名单，若在该名单尚未设置时进行移除，则会移除失败。

以下情况下，通过本接口移除通话呼出的允许或禁用名单，会报策略冲突：

已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口移除通话呼出的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |
| numbers | Array<string> | 是 | 待移除的通话号码数组。数组总长度不能超过1000。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = [
13. // 需根据实际情况进行替换
14. "13112345678"
15. ];
16. telephonyManager.removeOutgoingCallPolicyNumbers(wantTemp, policy, numbers);
17. console.info('Succeeded in removing outgoing call policy.');
18. } catch (err) {
19. console.error(`Failed to remove outgoing call policy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## telephonyManager.getOutgoingCallPolicyNumbers

PhonePC/2in1Tablet

getOutgoingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>

获取通话呼出的允许或禁用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。 BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 通话呼出禁用或允许名单的号码数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = telephonyManager.getOutgoingCallPolicyNumbers(wantTemp, policy);
13. console.info(`Succeeded in getting outgoing call policy. result: ${JSON.stringify(numbers)}`);
14. } catch (err) {
15. console.error(`Failed to get outgoing call policy. Code: ${err.code}, message: ${err.message}`);
16. }
```

## telephonyManager.addIncomingCallPolicyNumbers

PhonePC/2in1Tablet

addIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

添加通话呼入的允许或禁用名单，如果不添加名单，则任意号码都可以呼入，添加后仅名单内的号码允许或禁止呼入。

以下情况下，通过本接口添加通话呼入的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口添加通话呼入的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。
2. 已经通过本接口设置了通话呼入的禁用名单，再通过本接口添加通话呼入允许名单，返回9200010错误码。通过[removeIncomingCallPolicyNumbers](js-apis-enterprise-telephonymanager.md#telephonymanagerremoveincomingcallpolicynumbers)接口将之前设置的通话呼入禁用名单移除后，可解除冲突。
3. 已经通过本接口设置了通话呼入的允许名单，再通过本接口添加通话呼入禁用名单，返回9200010错误码。通过[removeIncomingCallPolicyNumbers](js-apis-enterprise-telephonymanager.md#telephonymanagerremoveincomingcallpolicynumbers)接口将之前设置的通话呼入允许名单移除后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |
| numbers | Array<string> | 是 | 通话号码列表，当前仅支持全号码匹配。数组总长度不能超过1000。例如，若当前允许名单数组中已有100个号码，则最多支持通过该接口再添加900个。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = [
13. // 需根据实际情况进行替换
14. "13112345678"
15. ];
16. telephonyManager.addIncomingCallPolicyNumbers(wantTemp, policy, numbers);
17. console.info('Succeeded in adding incoming call policy.');
18. } catch (err) {
19. console.error(`Failed to add incoming call policy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## telephonyManager.removeIncomingCallPolicyNumbers

PhonePC/2in1Tablet

removeIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy, numbers: Array<string>): void

移除通话呼入的允许或禁用名单，若在该名单尚未设置时进行移除，则会移除失败。

以下情况下，通过本接口移除通话呼入的允许或禁用名单，会报策略冲突：

1. 已经通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口禁用了设备通话能力，再通过本接口移除通话呼入的禁用或允许名单，返回203错误码。通过[setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)接口解除禁用设备通话能力后，可解除冲突。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |
| numbers | Array<string> | 是 | 待移除的通话号码数组。数组总长度不能超过1000。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = [
13. // 需根据实际情况进行替换
14. "13112345678"
15. ];
16. telephonyManager.removeIncomingCallPolicyNumbers(wantTemp, policy, numbers);
17. console.info('Succeeded in removing incoming call policy.');
18. } catch (err) {
19. console.error(`Failed to remove incoming call policy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## telephonyManager.getIncomingCallPolicyNumbers

PhonePC/2in1Tablet

getIncomingCallPolicyNumbers(admin: Want, policy: adminManager.Policy): Array<string>

获取通话呼入的允许或禁用名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [adminManager.Policy](js-apis-enterprise-adminmanager.md#policy20) | 是 | 允许或禁用名单策略。BLOCK\_LIST为禁用名单，TRUST\_LIST为允许名单。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 通话呼入禁用或允许名单的号码数组。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';
3. import { adminManager } from '@kit.MDMKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. try {
11. let policy: adminManager.Policy = adminManager.Policy.BLOCK_LIST;
12. let numbers: Array<string> = telephonyManager.getIncomingCallPolicyNumbers(wantTemp, policy);
13. console.info(`Succeeded in getting incoming call policy. result: ${JSON.stringify(numbers)}`);
14. } catch (err) {
15. console.error(`Failed to get incoming call policy. Code: ${err.code}, message: ${err.message}`);
16. }
```

## telephonyManager.hangupCalling23+

PhonePC/2in1Tablet

hangupCalling(admin: Want): void

挂断当前通话。仅支持运营商通话，不包括畅联等。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_TELEPHONY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**错误码**：

请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { telephonyManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. telephonyManager.hangupCalling(wantTemp);
11. } catch (err) {
12. console.error(`Failed to hang up calling. Code: ${err.code}, message: ${err.message}`);
13. }
```
