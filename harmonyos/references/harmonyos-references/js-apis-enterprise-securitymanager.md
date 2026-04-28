---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-securitymanager
title: @ohos.enterprise.securityManager（安全管理）
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.securityManager（安全管理）
category: harmonyos-references
scraped_at: 2026-04-28T08:10:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9dfdd46e8082ed569c4a163885ed932b8abd62133e6e50080f5db4d572eb22b4
---

本模块提供设备安全管理的能力，包括查询安全补丁状态、查询文件加密状态等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

PhonePC/2in1Tablet

```
1. import { securityManager } from '@kit.MDMKit';
```

## securityManager.uninstallUserCertificate

PhonePC/2in1Tablet

uninstallUserCertificate(admin: Want, certUri: string): Promise<void>

卸载用户证书，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| certUri | string | 是 | 证书uri，由安装用户证书接口[installUserCertificate](js-apis-enterprise-securitymanager.md#securitymanagerinstallusercertificate)设置返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。当卸载用户证书失败时会抛出错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. // 需根据实际情况进行替换
11. let aliasStr = "certName";
12. securityManager.uninstallUserCertificate(wantTemp, aliasStr).then(() => {
13. console.info(`Succeeded in uninstalling user certificate.`);
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to uninstall user certificate. Code is ${err.code}, message is ${err.message}`);
16. });
```

## securityManager.installUserCertificate

PhonePC/2in1Tablet

installUserCertificate(admin: Want, certificate: CertBlob): Promise<string>

安装用户证书，使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| certificate | [CertBlob](js-apis-enterprise-securitymanager.md#certblob) | 是 | 证书信息。证书文件应放在应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径下。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回当前证书安装后的uri，用于卸载证书。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let wantTemp: Want = {
6. // 需根据实际情况进行替换
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EnterpriseAdminAbility'
9. };
10. let certFileArray: Uint8Array = new Uint8Array();
11. // 变量context需要在MainAbility的onCreate回调函数中进行初始化
12. // test.cer需要放置在rawfile目录下
13. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
14. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. context.resourceManager.getRawFileContent("test.cer").then((value) => {
16. certFileArray = value;
17. securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert_alias_xts" })
18. .then((result) => {
19. console.info(`Succeeded in installing user certificate, result : ${JSON.stringify(result)}`);
20. }).catch((err: BusinessError) => {
21. console.error(`Failed to install user certificate. Code: ${err.code}, message: ${err.message}`);
22. })
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to get raw file content. message: ${err.message}`);
25. return;
26. });
```

## securityManager.installUserCertificate18+

PhonePC/2in1Tablet

installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string

支持按系统账户安装用户证书。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| certificate | [CertBlob](js-apis-enterprise-securitymanager.md#certblob) | 是 | 证书信息。证书文件应放在应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径下。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前证书安装后的uri，用于卸载证书。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201001 | Failed to manage the certificate. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { common, Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let certFileArray: Uint8Array = new Uint8Array();
10. let accountId: number = 100;
11. // 变量context需要在MainAbility的onCreate回调函数中进行初始化
12. // test.cer需要放置在rawfile目录下
13. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
14. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. context.resourceManager.getRawFileContent("test.cer").then((value) => {
16. certFileArray = value;
17. try {
18. let result: string = securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert_alias_xts" }, accountId);
19. console.info(`Succeeded in installing user certificate. result: ${result}`);
20. } catch (err) {
21. console.error(`Failed to install user certificate. Code: ${err.code}, message: ${err.message}`);
22. }
23. });
```

## securityManager.getUserCertificates18+

PhonePC/2in1Tablet

getUserCertificates(admin: Want, accountId: number): Array<string>

获取指定系统账户下的用户证书信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_CERTIFICATE

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回在指定用户ID下安装的所有用户证书。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let accountId: number = 100;
11. try {
12. let result: Array<string> = securityManager.getUserCertificates(wantTemp, accountId);
13. console.info(`Succeeded in getting the uri list of user Certificates. result: ${JSON.stringify(result)}`);
14. } catch (err) {
15. console.error(`Failed to get the uri list of user Certificates. Code: ${err.code}, message: ${err.message}`);
16. }
```

## securityManager.getSecurityStatus

PhonePC/2in1Tablet

getSecurityStatus(admin: Want, item: string): string

获取当前设备安全策略信息。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 安全策略名称。  - patch：设备安全补丁。  - encryption：设备文件系统加密。  - root：设备ROOT状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回安全策略状态值。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: string = securityManager.getSecurityStatus(wantTemp, 'patch');
12. console.info(`Succeeded in getting security patch tag. tag: ${result}`);
13. } catch (err) {
14. console.error(`Failed to get security patch tag. Code: ${err.code}, message: ${err.message}`);
15. }
```

## securityManager.setPasswordPolicy

PhonePC/2in1Tablet

setPasswordPolicy(admin: Want, policy: PasswordPolicy): void

设置设备锁屏口令策略。当用户设置锁屏口令时，如果设置的锁屏口令不符合要求，会有安全提示重新设置锁屏口令。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [PasswordPolicy](js-apis-enterprise-securitymanager.md#passwordpolicy) | 是 | 设备锁屏口令策略。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. let policy: securityManager.PasswordPolicy = {
11. complexityRegex: '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*])[a-zA-Z\\d!@#$%^&*]{8,}$',
12. validityPeriod: 1,
13. additionalDescription: '至少八个字符，至少一个大写字母，一个小写字母，一个数字和一个特殊字符',
14. };
15. try {
16. securityManager.setPasswordPolicy(wantTemp, policy);
17. console.info(`Succeeded in setting password policy.`);
18. } catch(err) {
19. console.error(`Failed to set password policy. Code: ${err.code}, message: ${err.message}`);
20. }
```

## securityManager.getPasswordPolicy

PhonePC/2in1Tablet

getPasswordPolicy(admin: Want): PasswordPolicy

获取设备锁屏口令策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PasswordPolicy](js-apis-enterprise-securitymanager.md#passwordpolicy) | 设备锁屏口令策略。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy(wantTemp);
12. console.info(`Succeeded in getting password policy, result : ${JSON.stringify(result)}`);
13. } catch(err) {
14. console.error(`Failed to get password policy. Code: ${err.code}, message: ${err.message}`);
15. }
```

## securityManager.setAppClipboardPolicy

PhonePC/2in1Tablet

setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void

设置设备剪贴板策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| tokenId | number | 是 | 目标应用的身份标识。可通过[bundleManager.getApplicationInfo](js-apis-bundlemanager-applicationinfo.md)获取accessTokenId。当前只支持最多100个tokenId被保存策略。 |
| policy | [ClipboardPolicy](js-apis-enterprise-securitymanager.md#clipboardpolicy) | 是 | 剪贴板策略。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let tokenId: number = 586874394;
11. try {
12. securityManager.setAppClipboardPolicy(wantTemp, tokenId, securityManager.ClipboardPolicy.IN_APP);
13. console.info(`Succeeded in setting clipboard policy.`);
14. } catch(err) {
15. console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
16. }
```

## securityManager.getAppClipboardPolicy

PhonePC/2in1Tablet

getAppClipboardPolicy(admin: Want, tokenId?: number): string

获取设备剪贴板策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| tokenId | number | 否 | 目标应用的身份标识。可通过[bundleManager.getApplicationInfo](js-apis-bundlemanager-applicationinfo.md)获取accessTokenId。当前只支持最多100个tokenId被保存策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回JSON字符串形式的设备剪贴板策略。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let tokenId: number = 586874394;
11. try {
12. let result: string = securityManager.getAppClipboardPolicy(wantTemp, tokenId);
13. console.info(`Succeeded in getting password policy, result : ${result}`);
14. } catch(err) {
15. console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
16. }
```

## securityManager.setAppClipboardPolicy18+

PhonePC/2in1Tablet

setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void

设置指定用户下指定应用的设备剪贴板策略。当前只支持最多保存100个策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被设置剪贴板策略的应用包名。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| policy | [ClipboardPolicy](js-apis-enterprise-securitymanager.md#clipboardpolicy) | 是 | 剪贴板策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleName: string = 'com.example.myapplication';
11. let accountId: number = 100;
12. try {
13. securityManager.setAppClipboardPolicy(wantTemp, bundleName, accountId, securityManager.ClipboardPolicy.IN_APP);
14. console.info(`Succeeded in setting clipboard policy.`);
15. } catch(err) {
16. console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
17. }
```

## securityManager.getAppClipboardPolicy18+

PhonePC/2in1Tablet

getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string

获取指定用户下指定应用的设备剪贴板策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被设置剪贴板策略的应用包名。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回JSON字符串形式的设备剪贴板策略。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleName: string = 'com.example.myapplication';
11. let accountId: number = 100;
12. try {
13. let result: string = securityManager.getAppClipboardPolicy(wantTemp, bundleName, accountId);
14. console.info(`Succeeded in getting password policy, result : ${result}`);
15. } catch(err) {
16. console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
17. }
```

## securityManager.setWatermarkImage14+

PhonePC/2in1Tablet

setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void

为指定用户的指定应用设置水印策略。当前只支持最多保存100个策略。

说明

本接口适用于企业场景下为三方应用设置水印，降低企业信息泄露风险。不建议为系统应用设置水印（如：桌面应用），可能存在未知异常。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占), 同一个用户下的同一个应用的水印独占。不同用户、不同应用的水印[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被设置水印的应用包名。 |
| source | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | string表示图像路径，图像路径为应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径。  image.PixelMap表示图像对象，图像像素占用大小不得超过500KB。  图像像素占用大小计算公式：图像宽度(像素)×图像高度 (像素)×每个像素占用的字节数（通常为4）。例如：一张 100x100 的图片，图像像素占用大小为100×100×4=40000字节。 |
| accountId | number | 是 | 用户ID。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleName: string = 'com.example.myapplication';
11. let source: string = '/data/storage/el1/base/test.png';
12. let accountId: number = 100;
13. try {
14. securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId);
15. console.info(`Succeeded in setting set watermarkImage policy.`);
16. } catch(err) {
17. console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
18. }
```

## securityManager.cancelWatermarkImage14+

PhonePC/2in1Tablet

cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void

取消指定用户的水印策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被取消水印的应用包名。 |
| accountId | number | 是 | 用户ID。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

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
1. import { securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. // 需根据实际情况进行替换
10. let bundleName: string = 'com.example.myapplication';
11. let accountId: number = 100;
12. try {
13. securityManager.cancelWatermarkImage(wantTemp, bundleName, accountId);
14. console.info(`Succeeded in setting cancel watermarkImage policy.`);
15. } catch(err) {
16. console.error(`Failed to cancel watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
17. }
```

## securityManager.setPermissionManagedState20+

PhonePC/2in1Tablet

setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void

设置指定应用的[user\_grant权限](../harmonyos-guides/permissions-for-all-user.md)的管理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** 同一个应用实例的同一个权限[独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)，不同应用实例不同权限[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstance | [ApplicationInstance](js-apis-enterprise-securitymanager.md#applicationinstance20) | 是 | 指定应用实例。 |
| permissions | Array<string> | 是 | 需要管理的权限名称列表，仅支持[user\_grant权限](../harmonyos-guides/permissions-for-all-user.md)。权限名称列表以[应用权限组](../harmonyos-guides/app-permission-group-list.md)为单位。列表中应包含应用在[module.json5](../harmonyos-guides/module-configuration-file.md)中声明的同一权限组内的所有权限。例如：应用如果在module.json5中声明需要ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR权限，则传入的权限名称列表必须同时包含ohos.permission.READ\_CALENDAR和ohos.permission.WRITE\_CALENDAR两个权限。 |
| managedState | [PermissionManagedState](js-apis-enterprise-securitymanager.md#permissionmanagedstate20) | 是 | 应用权限的管理策略。 |

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

```
1. import { Want } from '@kit.AbilityKit';
2. import { securityManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let appInstanceTemp: securityManager.ApplicationInstance = {
10. // 需根据实际情况进行替换
11. appIdentifier: '736498586',
12. appIndex: 0,
13. accountId: 100
14. };
15. let permissionsTemp: Array<string> = ['ohos.permission.CAMERA', 'ohos.permission.LOCATION'];
16. try {
17. securityManager.setPermissionManagedState(wantTemp, appInstanceTemp, permissionsTemp, securityManager.PermissionManagedState.GRANTED);
18. console.info('Succeeded in setting permission managed state.');
19. } catch(err) {
20. console.error(`Failed to set permission managed state.  Code: ${err.code}, message: ${err.message}`);
21. }
```

## securityManager.getPermissionManagedState20+

PhonePC/2in1Tablet

getPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permission: string): PermissionManagedState

获取指定应用的指定[user\_grant权限](../harmonyos-guides/permissions-for-all-user.md)的管理策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| applicationInstance | [ApplicationInstance](js-apis-enterprise-securitymanager.md#applicationinstance20) | 是 | 指定应用实例。 |
| permission | string | 是 | 需要获取管理策略的权限名称，仅支持user\_grant权限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PermissionManagedState](js-apis-enterprise-securitymanager.md#permissionmanagedstate20) | 应用权限的管理策略。 |

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
2. import { securityManager } from '@kit.MDMKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. let appInstanceTemp: securityManager.ApplicationInstance = {
10. // 需根据实际情况进行替换
11. appIdentifier: '736498586',
12. appIndex: 0,
13. accountId: 100
14. };
15. let permissionTemp: string = 'ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION';
16. try {
17. let result: securityManager.PermissionManagedState = securityManager.getPermissionManagedState(wantTemp, appInstanceTemp, permissionTemp);
18. console.info(`Succeeded in getting permission managed state, result : ${result}`);
19. } catch(err) {
20. console.error(`Failed to get permission managed state. Code: ${err.code}, message: ${err.message}`);
21. }
```

## securityManager.setExternalSourceExtensionsPolicy22+

PhonePC/2in1Tablet

setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void

设置外部来源扩展程序的管控策略。

* DEFAULT：

  默认，表示无管控策略，用户可以通过“设置-隐私与安全-高级”中的“运行外部来源的扩展程序”开关来设置是否允许扩展程序运行。
* DISALLOW：

  禁用。设置此策略后，禁止运行外部来源的扩展程序，运行中的扩展程序可继续运行，扩展程序关闭后无法启动运行。用户无法开启“设置-隐私和安全-高级”中的“运行外部来源的扩展程序”开关。
* FORCE\_OPEN：

  强制开启。设置此策略后，允许运行外部来源的扩展程序，用户无法关闭“设置-隐私和安全-高级”中的“运行外部来源的扩展程序”开关。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**冲突规则：** [独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md#want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| policy | [common.ManagedPolicy](js-apis-enterprise-common.md#managedpolicy) | 是 | 管控策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200010 | A conflict policy has been configured. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { common, securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };
9. try {
10. securityManager.setExternalSourceExtensionsPolicy(wantTemp, common.ManagedPolicy.FORCE_OPEN);
11. console.info(`Succeeded in setting managed policy.`);
12. } catch(err) {
13. console.error(`Failed to set managed policy. Code: ${err.code}, message: ${err.message}`);
14. }
```

## securityManager.getExternalSourceExtensionsPolicy22+

PhonePC/2in1Tablet

getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy

获取外部来源扩展程序的管控策略。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md#want) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [common.ManagedPolicy](js-apis-enterprise-common.md#managedpolicy) | 返回ManagedPolicy枚举类型的管控策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```
1. import { common, securityManager } from '@kit.MDMKit';
2. import { Want } from '@kit.AbilityKit';

4. let wantTemp: Want = {
5. // 需根据实际情况进行替换
6. bundleName: 'com.example.myapplication',
7. abilityName: 'EnterpriseAdminAbility'
8. };

10. try {
11. let result: common.ManagedPolicy = securityManager.getExternalSourceExtensionsPolicy(wantTemp);
12. console.info(`Succeeded in getting managed policy, result : ${result}`);
13. } catch(err) {
14. console.error(`Failed to get managed policy. Code: ${err.code}, message: ${err.message}`);
15. }
```

## CertBlob

PhonePC/2in1Tablet

证书信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inData | Uint8Array | 否 | 否 | 证书的二进制内容。 |
| alias | string | 否 | 否 | 证书别名，别名长度小于40个字符。 |

## PasswordPolicy

PhonePC/2in1Tablet

设备锁屏口令策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| complexityRegex | string | 否 | 是 | 口令复杂度正则表达式。 |
| validityPeriod | number | 否 | 是 | 密码有效期（单位：毫秒）。 |
| additionalDescription | string | 否 | 是 | 口令复杂度描述文本，例如：密码中必须包含字母、数字、特殊字符，至少8个字符，最多30个字符。 |

## ClipboardPolicy

PhonePC/2in1Tablet

设备剪贴板策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认，表示无策略。 |
| IN\_APP | 1 | 剪贴板可在同一应用使用。 |
| LOCAL\_DEVICE | 2 | 剪贴板可在同一设备使用。 |
| CROSS\_DEVICE | 3 | 剪贴板可跨设备使用。 |

## ApplicationInstance20+

PhonePC/2in1Tablet

应用实例。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](js-apis-bundlemanager-bundleinfo.md#signatureinfo)，如果应用没有appIdentifier可使用appId代替，可以通过接口[bundleManager.getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier和bundleInfo.signatureInfo.appId。 |
| accountId | number | 否 | 否 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| appIndex | number | 否 | 否 | 表示分身应用的索引，默认值为0。  appIndex为0时，表示主应用。appIndex大于0时，表示指定的分身应用。 |

## PermissionManagedState20+

PhonePC/2in1Tablet

应用权限的管理状态。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 1 | 默认由用户授予。 |
| GRANTED | 0 | 已静默授予。 |
| DENIED | -1 | 已静默拒绝。 |
