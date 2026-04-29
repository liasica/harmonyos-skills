---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-systemmanager
title: @ohos.enterprise.systemManager （系统管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.systemManager （系统管理）
category: harmonyos-references
scraped_at: 2026-04-29T14:01:12+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5bf73fa55887e77b3322885573cbef11ec4044c03172924b8050279d2c1818c6
---

本模块提供系统管理能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { systemManager } from '@kit.MDMKit';
```

## systemManager.setNTPServer

PhonePC/2in1Tablet

setNTPServer(admin: Want, server: string): void

设置NTP时间服务器。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| server | string | 是 | NTP服务器地址（以","分隔，如"ntpserver1.com,ntpserver2.com"。最大长度96字节，包括结束符）。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let server: string = "ntpserver.com";
11. try {
12. systemManager.setNTPServer(wantTemp, server);
13. console.info('Succeeded in setting NTPserver.');
14. } catch (err) {
15. console.error(`Failed to set ntp server. Code is ${err.code}, message is ${err.message}`);
16. }
```

## systemManager.getNTPServer

PhonePC/2in1Tablet

getNTPServer(admin: Want): string

获取NTP时间服务器信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | string对象，返回NTP时间服务器信息。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. systemManager.getNTPServer(wantTemp);
11. console.info('Succeeded in getting NTP server.');
12. } catch (err) {
13. console.error(`Failed to get ntp server. Code is ${err.code}, message is ${err.message}`);
14. }
```

## systemManager.setOtaUpdatePolicy

PhonePC/2in1Tablet

setOtaUpdatePolicy(admin: Want, policy: OtaUpdatePolicy): void

设置升级策略。内网升级场景下，需要先调用[systemManager.notifyUpdatePackages](js-apis-enterprise-systemmanager.md#systemmanagernotifyupdatepackages)接口通知系统更新包，再调用该接口设置升级策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [OtaUpdatePolicy](js-apis-enterprise-systemmanager.md#otaupdatepolicy) | 是 | 升级策略。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 默认升级策略
10. let otaUpdatePolicy1: systemManager.OtaUpdatePolicy = {
11. "policyType": systemManager.PolicyType.DEFAULT,
12. "version": "version_1.0.0.0",
13. };
14. try {
15. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy1);
16. console.info('Succeeded in setting ota update policy.');
17. } catch (err) {
18. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
19. }
20. // 禁止升级
21. let otaUpdatePolicy2: systemManager.OtaUpdatePolicy = {
22. "policyType": systemManager.PolicyType.PROHIBIT,
23. "version": "version_1.0.0.1",
24. };
25. try {
26. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy2);
27. console.info('Succeeded in setting ota update policy.');
28. } catch (err) {
29. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
30. }
31. // 强制升级
32. let otaUpdatePolicy3: systemManager.OtaUpdatePolicy = {
33. "policyType": systemManager.PolicyType.UPDATE_TO_SPECIFIC_VERSION,
34. "version": "version_1.0.0.2",
35. "latestUpdateTime": 1716343200, // 时间戳
36. };
37. try {
38. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy3);
39. console.info('Succeeded in setting ota update policy.');
40. } catch (err) {
41. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
42. }
43. // 指定时间窗口升级
44. let otaUpdatePolicy4: systemManager.OtaUpdatePolicy = {
45. "policyType": systemManager.PolicyType.WINDOWS,
46. "version": "version_1.0.0.3",
47. "installStartTime": 1716281049, // 时间戳
48. "installEndTime": 1716343200, // 时间戳
49. };
50. try {
51. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy4);
52. console.info('Succeeded in setting ota update policy.');
53. } catch (err) {
54. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
55. }
56. // 延迟升级
57. let otaUpdatePolicy5: systemManager.OtaUpdatePolicy = {
58. "policyType": systemManager.PolicyType.POSTPONE,
59. "version": "version_1.0.0.4",
60. "delayUpdateTime": 5, // 单位（小时）
61. };
62. try {
63. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy5);
64. console.info('Succeeded in setting ota update policy.');
65. } catch (err) {
66. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
67. }
68. // 禁用公网升级
69. let otaUpdatePolicy6: systemManager.OtaUpdatePolicy = {
70. "policyType": systemManager.PolicyType.DEFAULT,
71. "version": "version_1.0.0.5",
72. "disableSystemOtaUpdate": true,
73. };
74. try {
75. systemManager.setOtaUpdatePolicy(wantTemp, otaUpdatePolicy6);
76. console.info('Succeeded in setting ota update policy.');
77. } catch (err) {
78. console.error(`Failed to set ota update policy. Code is ${err.code}, message is ${err.message}`);
79. }
```

## systemManager.getOtaUpdatePolicy

PhonePC/2in1Tablet

getOtaUpdatePolicy(admin: Want): OtaUpdatePolicy

查询升级策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OtaUpdatePolicy](js-apis-enterprise-systemmanager.md#otaupdatepolicy) | OtaUpdatePolicy对象，返回升级策略。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let policy: systemManager.OtaUpdatePolicy= systemManager.getOtaUpdatePolicy(wantTemp);
11. console.info(`Succeeded in getting update policy: ${JSON.stringify(policy)}`);
12. } catch (err) {
13. console.error(`Failed to get update policy. Code is ${err.code}, message is ${err.message}`);
14. }
```

## systemManager.notifyUpdatePackages

PhonePC/2in1Tablet

notifyUpdatePackages(admin: Want, packageInfo: UpdatePackageInfo): Promise<void>

通知系统更新包信息。内网升级场景下，需要先调用该接口通知系统更新包，再调用[systemManager.setOtaUpdatePolicy](js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)设置升级策略。

说明

该接口比较耗时，当调用此接口后，后续如果在应用主线程调用其他同步接口时需要等待该接口异步返回。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| packageInfo | [UpdatePackageInfo](js-apis-enterprise-systemmanager.md#updatepackageinfo) | 是 | 系统更新包信息。  **说明：** 传入的UpdatePackageInfo.packages.path必须是“update”开头的zip压缩包，传入其他形式的文件会报9201004错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当通知系统更新包失败时会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201004 | The update packages do not exist or analyzing failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { systemManager } from '@kit.MDMKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Want } from '@kit.AbilityKit';
4. import { fileIo as fs } from '@kit.CoreFileKit';

6. let wantTemp: Want = {
7. // 需根据实际情况进行替换
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EnterpriseAdminAbility'
10. };
11. let notify: systemManager.NotifyDescription = {
12. // 需根据实际情况进行替换
13. "installTips": "installTips",
14. "installTipsDetail": "installTips detail"
15. };
16. let description: systemManager.PackageDescription = {
17. // 需根据实际情况进行替换
18. "notify": notify
19. };
20. let updatePackages: Array<systemManager.Package> = [];
21. // 应用沙箱路径，需根据实际情况进行替换
22. let fileDir = "/xxxx/xxxx/";
23. let path1: string = "update_sd_base.zip";
24. let path2: string = "update_sd_cust_xxxxx_all_cn.zip";
25. let path3: string = "update_sd_preload_xxxxx_all_cn_R1.zip";
26. let fd1: number = fs.openSync(fileDir + path1, fs.OpenMode.READ_ONLY).fd;
27. let fd2: number = fs.openSync(fileDir + "xxxxx/" + path2, fs.OpenMode.READ_ONLY).fd;
28. let fd3: number = fs.openSync(fileDir + "xxxxx/" + path3, fs.OpenMode.READ_ONLY).fd;
29. let package1: systemManager.Package = {
30. // 需根据实际情况进行替换
31. "type": systemManager.PackageType.FIRMWARE,
32. "path": path1,
33. "fd": fd1
34. };
35. let package2: systemManager.Package = {
36. // 需根据实际情况进行替换
37. "type": systemManager.PackageType.FIRMWARE,
38. "path": path2,
39. "fd": fd2
40. };
41. let package3: systemManager.Package = {
42. // 需根据实际情况进行替换
43. "type": systemManager.PackageType.FIRMWARE,
44. "path": path3,
45. "fd": fd3
46. };
47. updatePackages.push(package1);
48. updatePackages.push(package2);
49. updatePackages.push(package3);
50. let updatePackageInfo: systemManager.UpdatePackageInfo = {
51. // 需根据实际情况进行替换
52. "version" : "1.0",
53. "packages" : updatePackages,
54. "description" : description
55. };
56. systemManager.notifyUpdatePackages(wantTemp, updatePackageInfo).then(() => {
57. console.info('Succeeded in notifying update packages.');
58. }).catch ((error: BusinessError) => {
59. console.error(`Failed to notify update packages. Code is ${error.code},message is ${error.message}`);
60. });
```

## systemManager.getUpdateResult

PhonePC/2in1Tablet

getUpdateResult(admin: Want, version: string): Promise<UpdateResult>

获取系统更新结果。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| version | string | 是 | 更新包版本号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UpdateResult](js-apis-enterprise-systemmanager.md#updateresult)> | Promise对象，返回系统更新结果。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Want } from '@kit.AbilityKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. systemManager.getUpdateResult(wantTemp, "1.0").then((result:systemManager.UpdateResult) => {
11. console.info(`Succeeded in getting update result: ${JSON.stringify(result)}`);
12. }).catch((error: BusinessError) => {
13. console.error(`Get update result failed. Code is ${error.code},message is ${error.message}`);
14. });
```

## systemManager.getUpdateAuthData19+

PhonePC/2in1Tablet

getUpdateAuthData(admin: Want): Promise<string>

获取系统更新的鉴权数据，用于校验系统更新信息。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回系统更新的鉴权数据。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { systemManager } from '@kit.MDMKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Want } from '@kit.AbilityKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. systemManager.getUpdateAuthData(wantTemp).then((result: string) => {
11. console.info(`Succeeded in getting update auth data: ${JSON.stringify(result)}`);
12. }).catch((error: BusinessError) => {
13. console.error(`Get update auth data failed. Code is ${error.code},message is ${error.message}`);
14. });
```

## systemManager.addDisallowedNearLinkProtocols20+

PhonePC/2in1Tablet

addDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void

为指定用户添加禁用的星闪协议名单。NearLink Kit（星闪服务）提供一种低功耗、高速率的短距离通信服务，支持星闪设备之间的连接、数据交互。具体请参考[NearLink Kit](../harmonyos-guides/nearlink-introduction.md)。本接口对键盘、手写笔等系统服务和系统应用不生效。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| protocols | Array<[NearLinkProtocol](js-apis-enterprise-systemmanager.md#nearlinkprotocol20)> | 是 | 星闪协议列表。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. // 需根据实际情况进行替换
11. let protocols: systemManager.NearLinkProtocol[] = [systemManager.NearLinkProtocol.SSAP,
12. systemManager.NearLinkProtocol.DATA_TRANSFER];

14. // 需根据实际情况进行替换
15. let accountId: number = 100;

17. try {
18. systemManager.addDisallowedNearLinkProtocols(wantTemp, protocols, accountId);
19. console.info('Succeeded in adding the disabled Starlink protocol list for the specified user.');
20. } catch (err) {
21. console.error(`Failed to add the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
22. }
```

## systemManager.removeDisallowedNearLinkProtocols20+

PhonePC/2in1Tablet

removeDisallowedNearLinkProtocols(admin: Want, protocols: Array<NearLinkProtocol>, accountId: number): void

为指定用户移除禁用的星闪协议名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| protocols | Array<[NearLinkProtocol](js-apis-enterprise-systemmanager.md#nearlinkprotocol20)> | 是 | 星闪协议列表。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. // 需根据实际情况进行替换
11. let protocols: systemManager.NearLinkProtocol[] = [systemManager.NearLinkProtocol.SSAP,
12. systemManager.NearLinkProtocol.DATA_TRANSFER];

14. // 需根据实际情况进行替换
15. let accountId: number = 100;
16. try {
17. systemManager.removeDisallowedNearLinkProtocols(wantTemp, protocols, accountId);
18. console.info('Succeeded in removing the disabled Starlink protocol list for the specified user.');
19. } catch (err) {
20. console.error(`Failed to remove the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
21. }
```

## systemManager.getDisallowedNearLinkProtocols20+

PhonePC/2in1Tablet

getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>

获取指定用户下禁用的星闪协议名单。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[NearLinkProtocol](js-apis-enterprise-systemmanager.md#nearlinkprotocol20)> | 指定用户下禁用的星闪协议名单。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. // 需根据实际情况进行替换
11. let accountId: number = 100;

13. try {
14. let result: systemManager.NearLinkProtocol[] = systemManager.getDisallowedNearLinkProtocols(wantTemp, accountId);
15. console.info(`Succeeded in querying the disabled Starlink protocol list for the specified user: ${result}`);
16. } catch (err) {
17. console.error(`Failed to query the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
18. }
```

## systemManager.setInstallLocalEnterpriseAppEnabled20+

PhonePC/2in1Tablet

setInstallLocalEnterpriseAppEnabled(admin: Want, isEnable: boolean): void

设置是否支持本地安装企业应用。设置为支持安装后，具备本地安装能力的PC/2in1企业设备可本地双击应用安装包，安装签名证书分发类型为enterprise\_normal的企业应用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1企业设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。任意一个MDM应用设置支持本地安装企业应用，则综合策略即为支持本地安装企业应用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isEnable | boolean | 是 | 是否支持本地安装企业应用。true表示支持，false表示不支持。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let isEnable: boolean = true;
11. try {
12. systemManager.setInstallLocalEnterpriseAppEnabled(wantTemp, isEnable);
13. console.info('Succeeded in setting InstallLocalEnterpriseAppEnabled.');
14. } catch (err) {
15. console.error(`Failed to set installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
16. }
```

## systemManager.getInstallLocalEnterpriseAppEnabled20+

PhonePC/2in1Tablet

getInstallLocalEnterpriseAppEnabled(admin: Want): boolean

查询是否支持本地安装企业应用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1企业设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持本地安装企业应用，true为支持，false为不支持。 |

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
1. import { systemManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. let isEnable: boolean = systemManager.getInstallLocalEnterpriseAppEnabled(wantTemp);
11. console.info('Succeeded in getting installLocalEnterpriseAppEnabled.');
12. } catch (err) {
13. console.error(`Failed to get installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
14. }
```

## systemManager.setAutoUnlockAfterReboot20+

PhonePC/2in1Tablet

setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void

设置设备重启自动解锁，仅针对无锁屏密码设备生效。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)，任意一个MDM应用设置设备重启自动解锁，则综合策略即为设备重启自动解锁。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isAllowed | boolean | 是 | true表示设备重启后自动解锁，false表示设备重启后不自动解锁。 |

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
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let isAllowed: boolean = true;
10. try {
11. systemManager.setAutoUnlockAfterReboot(wantTemp, isAllowed);
12. console.info('Succeeded in setting setAutoUnlockAfterReboot.');
13. } catch (err) {
14. console.error(`Failed to set auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
15. }
```

## systemManager.getAutoUnlockAfterReboot20+

PhonePC/2in1Tablet

getAutoUnlockAfterReboot(admin: Want): boolean

获取设备是否重启自动解锁。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

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
| boolean | 返回true表示设备重启后自动解锁，返回false表示设备重启后不自动解锁。 |

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
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. systemManager.getAutoUnlockAfterReboot(wantTemp);
11. console.info('Succeeded in getting auto unlock after reboot.');
12. } catch (err) {
13. console.error(`Failed to get auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
14. }
```

## systemManager.addKeyEventPolicies23+

PhonePC/2in1Tablet

addKeyEventPolicies(admin: Want, keyPolicies: Array<KeyEventPolicy>): void

添加按键事件处理策略。系统触发按键事件时，若匹配下发的按键事件策略，将通过[EnterpriseAdminExtensionAbility.onKeyEvent](js-apis-enterpriseadminextensionability.md#onkeyevent23)回调通知MDM应用，并携带匹配策略的按键事件信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| keyPolicies | Array<[KeyEventPolicy](js-apis-enterprise-systemmanager.md#keyeventpolicy23)> | 是 | 按键策略。支持物理按键（电源键、音量加、音量减），导航键（回退、主页、最近打开）。物理键支持任意组合为组合键，导航键不支持组合。组合键事件响应详见[按键事件回调](js-apis-enterpriseadminextensionability.md#onkeyevent23)接口。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let keypolicy: Array<systemManager.KeyEventPolicy> = [
11. {
12. "keyCode": systemManager.KeyCode.POWER,
13. "keyPolicy": systemManager.KeyPolicy.CUSTOM
14. },
15. {
16. "keyCode": systemManager.KeyCode.VOLUME_UP,
17. "keyPolicy": systemManager.KeyPolicy.CUSTOM
18. }
19. ];

21. try {
22. systemManager.addKeyEventPolicies(wantTemp, keypolicy);
23. console.info('Succeeded in adding key event policies.');
24. } catch (err) {
25. console.error(`Failed to add key event policies. Code is ${err.code}, message is ${err.message}`);
26. }
```

## systemManager.removeKeyEventPolicies23+

PhonePC/2in1Tablet

removeKeyEventPolicies(admin: Want, keyCodes: Array<KeyCode>): void

删除按键事件处理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| keyCodes | Array<[KeyCode](js-apis-enterprise-systemmanager.md#keycode23)> | 是 | 按键编码。支持一次删除多条按键策略，删除不支持按键时返回9200012错误码。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let keyCodes: Array<systemManager.KeyCode> = [
11. systemManager.KeyCode.POWER, systemManager.KeyCode.VOLUME_UP,
12. ];

14. try {
15. systemManager.removeKeyEventPolicies(wantTemp, keyCodes);
16. console.info('Succeeded in removing key event policies.');
17. } catch (err) {
18. console.error(`Failed to remove key event policies. Code is ${err.code}, message is ${err.message}`);
19. }
```

## systemManager.getKeyEventPolicies23+

PhonePC/2in1Tablet

getKeyEventPolicies(admin: Want): Array<KeyEventPolicy>

获取按键事件处理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SYSTEM

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[KeyEventPolicy](js-apis-enterprise-systemmanager.md#keyeventpolicy23)> | 返回当前配置的按键事件策略列表。 |

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
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let result: Array<systemManager.KeyEventPolicy> = [];
10. try {
11. result = systemManager.getKeyEventPolicies(wantTemp);
12. console.info('Succeeded in getting key event policies.');
13. } catch (err) {
14. console.error(`Failed to get key event policies. Code is ${err.code}, message is ${err.message}`);
15. }
```

## systemManager.startCollectLog23+

PhonePC/2in1Tablet

startCollectLog(admin: Want): Promise<void>

开始收集设备上已生成并存储至硬盘的[faultlog](js-apis-faultlogger.md#faulttype)日志，不支持收集未存储至硬盘的faultlog日志、应用业务日志和系统运行日志。

* 调用接口后，系统会启动一个日志收集任务，任务启动后接口立即返回。任务可能会因为系统性能等原因导致收集失败。
* 允许多个MDM应用调用，不同MDM应用在不同用户下收集的日志分开保存，互不影响。同一时间只允许一个MDM应用启动日志收集任务，在任务执行完成前调用本接口会返回错误码9201009，任务执行完成后，允许其他MDM应用调用。
* 任务执行完成后，通过[EnterpriseAdminExtensionAbility.onLogCollected](js-apis-enterpriseadminextensionability.md#onlogcollected23)回调函数通知给MDM应用，系统将已收集的日志文件挂载到MDM应用沙箱路径，MDM应用可以在回调函数中读取已收集的日志。
* 如果日志收集任务执行超过5分钟，[EnterpriseAdminExtensionAbility.onLogCollected](js-apis-enterpriseadminextensionability.md#onlogcollected23)回调函数会返回日志收集任务失败。
* 应用取走日志后，建议调用[systemManager.finishLogCollected](js-apis-enterprise-systemmanager.md#systemmanagerfinishlogcollected23)删除已收集到的日志。

**需要权限：** ohos.permission.ENTERPRISE\_READ\_LOG

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** 允许多个MDM应用调用，不同MDM应用在不同用户下收集的日志分开保存，互不影响。同一时间只允许一个MDM应用启动日志收集任务，在任务执行完成前调用本接口会返回错误码9201009，任务执行完成后，允许其他MDM应用调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当收集日志任务创建失败时，会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201009 | Collecting logs, please try again later. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```
1. import { Want } from '@kit.AbilityKit';
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. systemManager.startCollectLog(wantTemp).then(() => {
11. console.info('Succeeded in starting collect log');
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to start collect log. Code: ${err.code}, message: ${err.message}`);
14. });
```

## systemManager.finishLogCollected23+

PhonePC/2in1Tablet

finishLogCollected(admin: Want): void

删除本MDM应用在当前用户下收集到的设备日志。

说明

在应用调用[startCollectLog](js-apis-enterprise-systemmanager.md#systemmanagerstartcollectlog23)开始收集日志后，收到[EnterpriseAdminExtensionAbility.onLogCollected](js-apis-enterpriseadminextensionability.md#onlogcollected23)回调时，建议立即拷贝或者处理日志，并调用此接口删除收集到的日志。

若不调本接口，设备日志会占用系统存储空间，不影响下一次调用[startCollectLog](js-apis-enterprise-systemmanager.md#systemmanagerstartcollectlog23)启动日志收集任务。

**需要权限：** ohos.permission.ENTERPRISE\_READ\_LOG

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

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
2. import { systemManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. systemManager.finishLogCollected(wantTemp);
12. console.info('Succeeded in finishing log collected.');
13. } catch (err) {
14. console.error(`Failed to finish log collected. Code is ${err.code}, message is ${err.message}`);
15. }
```

## SystemUpdateInfo

PhonePC/2in1Tablet

待更新的系统版本信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| versionName | string | 否 | 否 | 待更新的系统版本名称。 |
| firstReceivedTime | number | 否 | 否 | 第一次收到系统更新包的时间。 |
| packageType | string | 否 | 否 | 待更新的系统更新包类型。 |

## OtaUpdatePolicy

PhonePC/2in1Tablet

升级策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| policyType | [PolicyType](js-apis-enterprise-systemmanager.md#policytype) | 否 | 否 | 表示升级策略类型。 |
| version | string | 否 | 否 | 表示待升级软件版本号。 |
| latestUpdateTime | number | 否 | 是 | 表示最晚升级时间（时间戳）。 |
| delayUpdateTime | number | 否 | 是 | 表示延迟升级时间（单位：小时）。 |
| installStartTime | number | 否 | 是 | 表示指定安装窗口起始时间（时间戳）。 |
| installEndTime | number | 否 | 是 | 表示指定安装窗口结束时间（时间戳）。 |
| disableSystemOtaUpdate20+ | boolean | 否 | 是 | 表示是否禁用在公网环境下升级。true表示禁用公网升级，false表示不禁用公网升级。如果作为[systemManager.setOtaUpdatePolicy](js-apis-enterprise-systemmanager.md#systemmanagersetotaupdatepolicy)的入参，该字段可缺省，缺省时保持当前配置不变。当前配置可通过[systemManager.getOtaUpdatePolicy](js-apis-enterprise-systemmanager.md#systemmanagergetotaupdatepolicy)接口获取。禁用公网升级后，可以采用内网升级。推荐使用[restrictions.setDisallowedPolicy](js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)禁用公网升级。 |

## PolicyType

PhonePC/2in1Tablet

升级策略类型枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认升级策略。周期提示用户，用户确认后升级。 |
| PROHIBIT | 1 | 禁止升级策略。 |
| UPDATE\_TO\_SPECIFIC\_VERSION | 2 | 强制升级策略。需指定最晚升级时间（latestUpdateTime）参数。 |
| WINDOWS | 3 | 指定时间窗口升级策略。需指定时间窗口参数（installStartTime、installEndTime）。 |
| POSTPONE | 4 | 延迟升级策略。延迟指定时间（delayUpdateTime）后进入DEFAULT模式，周期提示用户升级。 |

## UpdatePackageInfo

PhonePC/2in1Tablet

系统更新包信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | string | 否 | 否 | 系统更新包版本号。 |
| packages | Array<[Package](js-apis-enterprise-systemmanager.md#package)> | 否 | 否 | 系统更新包详情。 |
| description | [PackageDescription](js-apis-enterprise-systemmanager.md#packagedescription) | 否 | 是 | 系统更新包描述信息。 |
| authInfo19+ | string | 否 | 是 | 系统更新包的鉴权信息。 |

## Package

PhonePC/2in1Tablet

系统更新包详情。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PackageType](js-apis-enterprise-systemmanager.md#packagetype) | 否 | 否 | 系统更新包类型。 |
| path | string | 否 | 否 | 系统更新包文件路径。若传入fd参数，该参数传入更新包文件名。 |
| fd | number | 否 | 是 | 系统更新包文件句柄。当前不支持只传入path参数，需要传入fd。 |

## PackageDescription

PhonePC/2in1Tablet

系统更新包描述信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| notify | [NotifyDescription](js-apis-enterprise-systemmanager.md#notifydescription) | 否 | 是 | 企业自定义更新通知说明。 |

## NotifyDescription

PhonePC/2in1Tablet

企业自定义更新通知说明。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| installTips | string | 否 | 是 | 企业自定义更新提示。 |
| installTipsDetail | string | 否 | 是 | 企业自定义更新提示详情。 |

## UpdateResult

PhonePC/2in1Tablet

系统更新结果信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | string | 否 | 否 | 系统当前版本号。 |
| status | [UpdateStatus](js-apis-enterprise-systemmanager.md#updatestatus) | 否 | 否 | 系统更新状态。 |
| errorInfo | [ErrorInfo](js-apis-enterprise-systemmanager.md#errorinfo) | 否 | 否 | 系统更新错误信息。 |

## ErrorInfo

PhonePC/2in1Tablet

系统更新错误信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 错误码。 |
| message | string | 否 | 否 | 错误描述信息。 |

## PackageType

PhonePC/2in1Tablet

系统更新包类型。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FIRMWARE | 1 | 固件。 |

## UpdateStatus

PhonePC/2in1Tablet

系统更新状态。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_UPDATE\_PACKAGE | -4 | 指定版本系统更新包不存在。 |
| UPDATE\_WAITING | -3 | 系统更新包等待安装中。 |
| UPDATING | -2 | 正在更新。 |
| UPDATE\_FAILURE | -1 | 更新失败。 |
| UPDATE\_SUCCESS | 0 | 更新成功。 |

## NearLinkProtocol20+

PhonePC/2in1Tablet

星闪协议枚举。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SSAP | 0 | SSAP（SparkLink Service Access Protocol）协议。具体请参考[SSAP协议](../harmonyos-guides/nearlink-terminology.md#ssap)。 |
| DATA\_TRANSFER | 1 | 数据传输协议。具体请参考[Data Transfer协议](../harmonyos-guides/nearlink-terminology.md#data-transfer)。 |

## KeyEventPolicy23+

PhonePC/2in1Tablet

按键事件处理策略。按键事件发生时，仅拦截响应已下发按键事件处理策略的按键。对于未下发按键事件处理策略的按键事件，系统执行原先的响应逻辑。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | [KeyCode](js-apis-enterprise-systemmanager.md#keycode23) | 否 | 否 | 按键编码。 |
| keyPolicy | [KeyPolicy](js-apis-enterprise-systemmanager.md#keypolicy23) | 否 | 否 | 按键策略。 |

## KeyCode23+

PhonePC/2in1Tablet

按键编码。[添加按键事件策略](js-apis-enterprise-systemmanager.md#systemmanageraddkeyeventpolicies23)、[删除按键事件策略](js-apis-enterprise-systemmanager.md#systemmanagerremovekeyeventpolicies23)、[获取按键事件策略](js-apis-enterprise-systemmanager.md#systemmanagergetkeyeventpolicies23)和[按键事件回调](js-apis-enterpriseadminextensionability.md#onkeyevent23)接口通过按键编码映射到设备对应实际按键。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| POWER | 0 | 电源键。 |
| VOLUME\_UP | 1 | 音量加。 |
| VOLUME\_DOWN | 2 | 音量减。 |
| BACK | 3 | 导航键-回退。 |
| HOME | 4 | 导航键-主页。 |
| RECENT | 5 | 导航键-最近打开。 |

## KeyPolicy23+

PhonePC/2in1Tablet

按键策略。MDM应用下发按键策略的按键编码与系统按键事件匹配后的系统行为。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERCEPTION | 0 | 拦截消息。设置后仅会拦截当前按键事件，系统不会再处理该事件，按键回调接口也不会响应按键事件。例如：下发电源键拦截策略后，按电源键无任何响应，无法关机，无法锁屏，仅影响开机状态下电源键事件，关机时可通过电源键正常开机。 |
| CUSTOM | 1 | 拦截并转发消息。 设置后会拦截当前按键事件，系统不会再处理该事件，同时通过[EnterpriseAdminExtensionAbility.onKeyEvent](js-apis-enterpriseadminextensionability.md#onkeyevent23)回调接口将发生的按键事件通知给MDM应用，通知MDM应用处理该事件的过程不会阻塞系统后续的其他事件处理。 |

## KeyEvent23+

PhonePC/2in1Tablet

按键事件。[EnterpriseAdminExtensionAbility.onKeyEvent](js-apis-enterpriseadminextensionability.md#onkeyevent23)按键事件回调触发时，传递当前按键事件信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | [KeyCode](js-apis-enterprise-systemmanager.md#keycode23) | 否 | 否 | 按键编码。 |
| keyAction | [KeyAction](js-apis-enterprise-systemmanager.md#keyaction23) | 否 | 否 | 按键动作。 |
| actionTime | number | 否 | 否 | 按键动作发生时间，系统开机后微秒级时间戳。当按键长按时后续按键事件该参数不发生改变，应用可以通过该时间来判断该事件是否属于长按事件，以执行长按事件逻辑处理。 |
| keyItems | Array<[KeyItem](js-apis-enterprise-systemmanager.md#keyitem23)> | 否 | 否 | 其他按键信息，当前按键事件发生时，其他正在被按下的按键信息。 |

## KeyAction23+

PhonePC/2in1Tablet

按键动作。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | -1 | 除按下和抬起动作以外，其他按键动作。 |
| DOWN | 0 | 按键按下动作。 |
| UP | 1 | 按键抬起动作。 |

## KeyItem23+

PhonePC/2in1Tablet

其他按键信息。当前[KeyCode](js-apis-enterprise-systemmanager.md#keycode23)事件发生时，其他已被按下的按键信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| keyCode | [KeyCode](js-apis-enterprise-systemmanager.md#keycode23) | 否 | 否 | 按键编码。 |
| pressed | boolean | 否 | 否 | 按键动作。按键是否被按下。true：按下；false：抬起 |
| downTime | number | 否 | 否 | 按键动作发生时间，系统开机后微秒级时间戳。导航按键不支持组合扩展，发生时间显示为0。 |
