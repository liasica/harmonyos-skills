---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-securitymanager
title: "@ohos.enterprise.securityManager (安全管理)"
breadcrumb: API参考 > 系统 > 基础功能 > MDM Kit（企业设备管理服务） > ArkTS API > @ohos.enterprise.securityManager (安全管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:92b26207f2a3700e42760dd008e637fdf3b1d0fda9d28bd35ddd3730929e5957
---

本模块提供企业设备安全管理能力，支持证书管理、设备安全策略管理、口令策略管理、剪贴板策略管理、水印策略管理、权限管理等功能。企业可使用本模块实现设备安全状态的实时监控、企业证书的生命周期管理、设备口令策略的统一配置、应用剪贴板使用行为的管控、屏幕和应用水印的设置以防止信息泄露、以及应用权限的精细化管理等场景，帮助企业提升设备安全防护能力，降低数据泄露风险。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)。

## 导入模块

```ts
import { securityManager } from '@kit.MDMKit';
```

## securityManager.uninstallUserCertificate

uninstallUserCertificate(admin: Want, certUri: string): Promise<void>

卸载用户证书，使用Promise异步回调。适用于企业证书管理场景，如证书过期更换、撤销员工对企业资源的访问权限等。企业可在证书过期、更换或不再需要时调用此接口卸载证书，确保设备证书管理的灵活性和安全性。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let aliasStr = "certName";
securityManager.uninstallUserCertificate(wantTemp, aliasStr).then(() => {
  console.info(`Succeeded in uninstalling user certificate.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to uninstall user certificate. Code is ${err.code}, message is ${err.message}`);
});
```

## securityManager.installUserCertificate

installUserCertificate(admin: Want, certificate: CertBlob): Promise<string>

安装用户证书，使用Promise异步回调。企业可通过此接口将证书安装到设备上，用于企业VPN连接、安全认证、数字签名等场景，实现企业级的安全通信和数据保护。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let certFileArray: Uint8Array = new Uint8Array();
// 变量context需要在MainAbility的onCreate回调函数中进行初始化
// test.cer需要放置在rawfile目录下
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
context.resourceManager.getRawFileContent("test.cer").then((value) => {
  certFileArray = value;
  securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert_alias_xts" })
    .then((result) => {
      console.info(`Succeeded in installing user certificate, result : ${JSON.stringify(result)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to install user certificate. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to get raw file content. message: ${err.message}`);
  return;
});
```

## securityManager.installUserCertificate18+

installUserCertificate(admin: Want, certificate: CertBlob, accountId: number): string

支持按系统账户安装用户证书。企业可为不同用户账户安装独立的证书，实现多用户环境下的安全隔离和个性化证书管理，满足多用户设备的安全管控需求。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let certFileArray: Uint8Array = new Uint8Array();
let accountId: number = 100;
// 变量context需要在MainAbility的onCreate回调函数中进行初始化
// test.cer需要放置在rawfile目录下
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
context.resourceManager.getRawFileContent("test.cer").then((value) => {
  certFileArray = value;
  try {
    let result: string = securityManager.installUserCertificate(wantTemp, { inData: certFileArray, alias: "cert_alias_xts" }, accountId);
    console.info(`Succeeded in installing user certificate. result: ${result}`);
  } catch (err) {
    console.error(`Failed to install user certificate. Code: ${err.code}, message: ${err.message}`);
  }
});
```

## securityManager.getUserCertificates18+

getUserCertificates(admin: Want, accountId: number): Array<string>

获取指定系统账户下的用户证书信息。企业可通过此接口查询设备上已安装的用户证书列表，用于证书审计、证书有效期管理等场景，确保证书管理的可追溯性。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  let result: Array<string> = securityManager.getUserCertificates(wantTemp, accountId);
  console.info(`Succeeded in getting the uri list of user Certificates. result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get the uri list of user Certificates. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getSecurityStatus

getSecurityStatus(admin: Want, item: string): string

获取当前设备安全策略信息。适用于设备合规性检查、安全状态审计、策略执行效果验证等场景，帮助企业管理员确认设备是否符合安全要求。企业可通过此接口实时监控设备的安全补丁状态和文件加密状态，及时发现设备安全风险并采取相应措施，保障企业设备和数据安全。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| item | string | 是 | 安全策略名称。  - patch：设备安全补丁。  - encryption：设备文件系统加密。  - root：设备ROOT状态。  - fastboot24+：设备fastboot模式锁定状态。 |

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: string = securityManager.getSecurityStatus(wantTemp, 'patch');
  console.info(`Succeeded in getting security patch tag. tag: ${result}`);
} catch (err) {
  console.error(`Failed to get security patch tag. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setPasswordPolicy

setPasswordPolicy(admin: Want, policy: PasswordPolicy): void

设置设备锁屏口令策略。策略设置后，当用户设置锁屏口令时，如果设置的锁屏口令不符合要求，会有安全提示重新设置锁屏口令。适用于企业安全合规场景，如强制要求员工使用强密码、定期更换密码等，降低企业数据泄露风险。

**说明** 

在多个MDM应用场景下，遵循[配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)规则，任意MDM应用取消激活时，该应用设置的设备锁屏口令策略会被清除。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 9200007 | The system ability works abnormally. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let policy: securityManager.PasswordPolicy = {
  complexityRegex: '^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*])[a-zA-Z\\d!@#$%^&*]{8,}$',
  validityPeriod: 1,
  additionalDescription: '至少八个字符，至少一个大写字母，一个小写字母，一个数字和一个特殊字符',
  passwordAlgs: securityManager.PasswordAlgs.SCRYPT_HKDF_SM4
};
try {
  securityManager.setPasswordPolicy(wantTemp, policy);
  console.info(`Succeeded in setting password policy.`);
} catch (err) {
  console.error(`Failed to set password policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getPasswordPolicy

getPasswordPolicy(admin: Want): PasswordPolicy

获取设备锁屏口令策略。企业可通过此接口查询当前配置的口令策略，用于策略审计、合规性检查等场景，确保设备口令策略符合企业安全规范。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[securityManager.getPasswordPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetpasswordpolicy-1)接口。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy(wantTemp);
  console.info(`Succeeded in getting password policy, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get password policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getPasswordPolicy

getPasswordPolicy(admin: Want | null): PasswordPolicy

获取设备锁屏口令策略。企业可通过此接口查询当前配置的口令策略，用于策略审计、合规性检查等场景，确保设备口令策略符合企业安全规范。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

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

```ts
import { securityManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: securityManager.PasswordPolicy = securityManager.getPasswordPolicy(null);
  console.info(`Succeeded in getting password policy, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get password policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setScreenLockDisabledForAccount

setScreenLockDisabledForAccount(admin: Want, disable: boolean): void

禁用/启用当前用户的滑动解锁能力。启用时：设备灭屏后再亮屏，用户需要在屏幕上滑动后才能进入桌面。禁用时：设备灭屏后再亮屏会直接进入桌面。适用于企业设备管理场景，如在特定安全环境下禁用滑动解锁简化操作，或在通用场景下启用滑动解锁作为基础安全措施。

**说明** 

1. 该接口能力仅在设备无锁屏密码时生效。
2. 设备默认属于启用滑动解锁的状态。
3. 设备上存在密码时，设置禁用滑动解锁会失败，抛出9201021错误码。
4. 下发禁用滑动解锁的策略后，用户输入了设备密码，此时密码会生效，设备需要验证密码后才能进入桌面，之前下发的策略失效。
5. 在多个MDM应用场景下，遵循[配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)规则。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| disable | boolean | 是 | 是否禁用当前用户的滑动解锁能力。true表示禁用，false表示不禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201021 | A lock screen password has been set for the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  securityManager.setScreenLockDisabledForAccount(wantTemp, true);
  console.info(`Succeeded in setting screen lock disabled for account.`);
} catch (err) {
  console.error(`Failed to set screen lock disabled for account. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.isScreenLockDisabledForAccount

isScreenLockDisabledForAccount(admin: Want): boolean

查询当前用户的滑动解锁能力是否被禁用。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在Phone和Tablet中可正常调用，在其他设备中调用返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前用户的滑动解锁能力已禁用，false表示未禁用。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: boolean = securityManager.isScreenLockDisabledForAccount(wantTemp);
  console.info(`Succeeded in checking screen lock disabled for account, result : ${result}`);
} catch (err) {
  console.error(`Failed to check screen lock disabled for account. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setAppClipboardPolicy

setAppClipboardPolicy(admin: Want, tokenId: number, policy: ClipboardPolicy): void

设置设备剪贴板策略。策略设置后，应用将按照设置的策略限制剪贴板的使用范围。适用于企业数据防泄露场景，如限制敏感应用（如企业邮箱、财务系统）的剪贴板使用范围，防止敏感数据被复制到非授权应用，降低数据泄露风险。企业可通过此接口控制应用的剪贴板使用权限，防止敏感数据通过剪贴板泄露到未授权应用，增强企业数据安全防护能力。

**说明** 

在多个MDM应用场景下，遵循[从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| tokenId | number | 是 | 目标应用的身份标识。可通过[bundleManager.getApplicationInfo](js-apis-bundlemanager-applicationinfo.md)获取accessTokenId。 |
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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let tokenId: number = 586874394;
try {
  securityManager.setAppClipboardPolicy(wantTemp, tokenId, securityManager.ClipboardPolicy.IN_APP);
  console.info(`Succeeded in setting clipboard policy.`);
} catch (err) {
  console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getAppClipboardPolicy

getAppClipboardPolicy(admin: Want, tokenId?: number): string

获取设备剪贴板策略。企业可通过此接口查询当前配置的剪贴板策略，用于策略审计和合规性检查，确保剪贴板管控策略符合企业安全要求。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[securityManager.getAppClipboardPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetappclipboardpolicy-1)接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| tokenId | number | 否 | 目标应用的身份标识。可通过[bundleManager.getApplicationInfo](js-apis-bundlemanager-applicationinfo.md)获取accessTokenId。 |

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let tokenId: number = 586874394;
try {
  let result: string = securityManager.getAppClipboardPolicy(wantTemp, tokenId);
  console.info(`Succeeded in getting clipboard policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getAppClipboardPolicy

getAppClipboardPolicy(admin: Want | null, tokenId?: number): string

获取设备剪贴板策略。企业可通过此接口查询当前配置的剪贴板策略，用于策略审计和合规性检查，确保剪贴板管控策略符合企业安全要求。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |
| tokenId | number | 否 | 目标应用的身份标识。可通过[bundleManager.getApplicationInfo](js-apis-bundlemanager-applicationinfo.md)获取accessTokenId。 |

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

```ts
import { securityManager } from '@kit.MDMKit';

// 需根据实际情况进行替换
let tokenId: number = 586874394;
try {
  // 参数需根据实际情况进行替换
  let result: string = securityManager.getAppClipboardPolicy(null, tokenId);
  console.info(`Succeeded in getting clipboard policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setAppClipboardPolicy18+

setAppClipboardPolicy(admin: Want, bundleName: string, accountId: number, policy: ClipboardPolicy): void

设置指定用户下指定应用的设备剪贴板策略。策略设置后，指定应用的剪贴板将按照策略限制使用范围。企业可为不同用户的不同应用配置差异化的剪贴板使用权限，实现精细化的数据访问控制，满足多用户多应用场景下的安全管控需求。

**说明** 

在多个MDM应用场景下，遵循[从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
  securityManager.setAppClipboardPolicy(wantTemp, bundleName, accountId, securityManager.ClipboardPolicy.IN_APP);
  console.info(`Succeeded in setting clipboard policy.`);
} catch (err) {
  console.error(`Failed to set clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getAppClipboardPolicy18+

getAppClipboardPolicy(admin: Want, bundleName: string, accountId: number): string

获取指定用户下指定应用的设备剪贴板策略。企业可通过此接口查询特定应用的剪贴板使用权限配置，用于策略审计和合规性检查。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[securityManager.getAppClipboardPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetappclipboardpolicy-2)接口。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
  let result: string = securityManager.getAppClipboardPolicy(wantTemp, bundleName, accountId);
  console.info(`Succeeded in getting clipboard policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getAppClipboardPolicy

getAppClipboardPolicy(admin: Want | null, bundleName: string, accountId: number): string

获取指定用户下指定应用的设备剪贴板策略。企业可通过此接口查询特定应用的剪贴板使用权限配置，用于策略审计和合规性检查。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |
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

```ts
import { securityManager } from '@kit.MDMKit';

// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
  // 参数需根据实际情况进行替换
  let result: string = securityManager.getAppClipboardPolicy(null, bundleName, accountId);
  console.info(`Succeeded in getting clipboard policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get clipboard policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setWatermarkImage14+

setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number): void

为指定用户的指定应用设置水印策略。当前只支持最多保存100个策略。

**说明** 

1. 本接口适用于企业场景下为三方应用设置水印，降低企业信息泄露风险。不建议为系统应用设置水印（如：桌面应用），可能存在未知异常。
2. 水印图片会以平铺方式重复覆盖整个应用界面。
3. 在多个MDM应用场景下，同一个用户下的同一个应用的水印遵循[独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)规则。不同用户、不同应用的水印遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被设置水印的应用包名。 |
| source | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | string表示图像路径，图像路径为应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径。  image.PixelMap表示图像对象。  图像像素占用大小不得超过500KB。  图像像素占用大小计算公式：图像宽度(像素)×图像高度 (像素)×每个像素占用的字节数（通常为4）。例如：一张 100x100 的图片，图像像素占用大小为100×100×4=40000字节。 |
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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
try {
  securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId);
  console.info(`Succeeded in setting watermarkImage policy.`);
} catch (err) {
  console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.cancelWatermarkImage14+

cancelWatermarkImage(admin: Want, bundleName: string, accountId: number): void

取消指定用户的水印策略。当应用不再需要水印保护或需要更换水印时，企业可调用此接口取消水印策略。当使用[企业数字空间](../harmonyos-guides/enterprisespace-introduction.md)时，只能在当前用户下取消当前用户的水印。即可以在100用户下取消100用户的水印，不可以在100用户下取消101用户的水印。

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

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let accountId: number = 100;
try {
  securityManager.cancelWatermarkImage(wantTemp, bundleName, accountId);
  console.info(`Succeeded in cancelling watermarkImage policy.`);
} catch (err) {
  console.error(`Failed to cancel watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setPermissionManagedState20+

setPermissionManagedState(admin: Want, applicationInstance: ApplicationInstance, permissions: Array<string>, managedState: PermissionManagedState): void

设置指定应用的[user\_grant权限](../harmonyos-guides/permissions-for-all-user.md)的管理策略。适用于企业应用批量部署场景，如静默授权减少权限弹窗干扰、统一企业应用权限管理策略，提升员工使用体验和管理效率。

**说明** 

在多个MDM应用场景下，同一个应用实例的同一个权限[独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)，不同应用实例不同权限[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_USER\_GRANT\_PERMISSION

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

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

```ts
import { Want } from '@kit.AbilityKit';
import { securityManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let appInstanceTemp: securityManager.ApplicationInstance = {
  // 需根据实际情况进行替换
  appIdentifier: '736498586',
  appIndex: 0,
  accountId: 100
};
let permissionsTemp: Array<string> = ['ohos.permission.CAMERA', 'ohos.permission.LOCATION'];
try {
  securityManager.setPermissionManagedState(wantTemp, appInstanceTemp, permissionsTemp,
    securityManager.PermissionManagedState.GRANTED);
  console.info('Succeeded in setting permission managed state.');
} catch (err) {
  console.error(`Failed to set permission managed state.  Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getPermissionManagedState20+

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

```ts
import { Want } from '@kit.AbilityKit';
import { securityManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let appInstanceTemp: securityManager.ApplicationInstance = {
  // 需根据实际情况进行替换
  appIdentifier: '736498586',
  appIndex: 0,
  accountId: 100
};
let permissionTemp: string = 'ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION';
try {
  let result: securityManager.PermissionManagedState =
    securityManager.getPermissionManagedState(wantTemp, appInstanceTemp, permissionTemp);
  console.info(`Succeeded in getting permission managed state, result : ${result}`);
} catch (err) {
  console.error(`Failed to get permission managed state. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setExternalSourceExtensionsPolicy22+

setExternalSourceExtensionsPolicy(admin: Want, policy: common.ManagedPolicy): void

设置外部来源扩展程序的管控策略。策略设置后，系统将按照设置的策略控制外部来源扩展程序的运行行为。适用于企业安全管控场景，如防止员工安装非授权浏览器扩展程序，或强制开启企业批准的扩展程序功能，保障企业终端安全。

* DEFAULT：

  默认，表示无管控策略，用户可以通过“设置-隐私与安全-高级”中的“运行外部来源的扩展程序”开关来设置是否允许扩展程序运行。
* DISALLOW：

  禁用。设置此策略后，禁止运行外部来源的扩展程序，运行中的扩展程序可继续运行，扩展程序关闭后无法启动运行。用户无法开启“设置-隐私和安全-高级”中的“运行外部来源的扩展程序”开关。
* FORCE\_OPEN：

  强制开启。设置此策略后，允许运行外部来源的扩展程序，用户无法关闭“设置-隐私和安全-高级”中的“运行外部来源的扩展程序”开关。

**说明** 

在多个MDM应用场景下，遵循[独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  securityManager.setExternalSourceExtensionsPolicy(wantTemp, common.ManagedPolicy.FORCE_OPEN);
  console.info(`Succeeded in setting managed policy.`);
} catch (err) {
  console.error(`Failed to set managed policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getExternalSourceExtensionsPolicy22+

getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy

获取外部来源扩展程序的管控策略。

本接口通过传入Want查询对应企业设备管理应用设置的策略，如需查询实际生效的策略，请使用[securityManager.getExternalSourceExtensionsPolicy](js-apis-enterprise-securitymanager.md#securitymanagergetexternalsourceextensionspolicy)接口。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

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
| [common.ManagedPolicy](js-apis-enterprise-common.md#managedpolicy) | 返回ManagedPolicy枚举类型的管控策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: common.ManagedPolicy = securityManager.getExternalSourceExtensionsPolicy(wantTemp);
  console.info(`Succeeded in getting managed policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get managed policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getExternalSourceExtensionsPolicy

getExternalSourceExtensionsPolicy(admin: Want | null): common.ManagedPolicy

获取外部来源扩展程序的管控策略。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。  当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

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
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { common, securityManager } from '@kit.MDMKit';

try {
  // 参数需根据实际情况进行替换
  let result: common.ManagedPolicy = securityManager.getExternalSourceExtensionsPolicy(null);
  console.info(`Succeeded in getting managed policy, result : ${result}`);
} catch (err) {
  console.error(`Failed to get managed policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.installEnterpriseReSignatureCertificate24+

installEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, fd: number, accountId: number): void

安装企业应用重签名证书。安装成功后，企业可使用该证书对应用进行重签名。调用此接口前，此设备必须通过[HEM商用部署](https://developer.huawei.com/business/cn/doc/HEM/hem_user-guide_add-reseller_management-resellerr-0000002469112100)。

同一用户下最多可下发10本不同证书。证书别名作为证书的唯一标识，不支持重复下发相同别名的证书。如需更新同一别名的证书，需先调用[uninstallEnterpriseReSignatureCertificate](js-apis-enterprise-securitymanager.md#securitymanageruninstallenterpriseresignaturecertificate24)进行卸载。

在MDM应用卸载或admin取消激活场景下，已安装的证书会保留在设备上，不会被移除。

在企业应用分发场景下，由开发者到[华为AGC](https://developer.huawei.com/consumer/cn/agconnect)申请企业应用重签名证书，开发者可以使用重签名证书对企业应用进行二次签名，签名完成后将应用包提供给企业管理员。企业管理员可以将重签名后的应用安装在已部署重签名证书的企业设备上。

企业应用重签名证书使用流程：

首先，由开发者到[华为AGC](https://developer.huawei.com/consumer/cn/agconnect)申请企业应用重签名证书，然后依照以下步骤。

1.通过MDM应用安装企业应用重签名证书；

2.开发者利用签名工具（如ohos-signer或DevEco Studio签名插件），对原始HAP包进行二次签名；

3.安装重签名应用（可以通过企业私有应用市场安装）；

4.运行应用。

规格约束：

1.安装新的签名证书之后，使用旧签名证书的应用可以继续运行；

2.已经安装的企业应用，安装了新的企业签名证书后，已安装的应用如需更新，可以直接覆盖安装，无需先卸载原应用；

3.企业场景下，特别是在涉及信息安全的场景中，企业需要确保员工使用的移动设备中仅安装并运行特定的内部软件和工具。企业应用重签名证书通过统一的应用身份标识，与系统的应用管理与权限控制机制配合使用，可支持企业应用的静默安装、受控的系统能力调用及运行范围限制，从而实现企业软件在受控终端上的准入控制与安全管理。

**说明** 

在多个MDM应用场景下，遵循[配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)规则。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| certificateAlias | string | 是 | 证书别名，必须以'.cer'结尾。 |
| fd | number | 是 | 表示已存在的重签名证书文件描述符，证书文件需要放置于[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201006 | The number of certificates has reached the limit. |
| 9201007 | The certificate is invalid. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// test.cer证书文件需要放置在应用沙箱目录下，并确保是有效的企业应用重签名证书
// 需根据实际情况进行替换
const filePath = '/test.cer';
// 需根据实际情况进行替换
let certificateAlias: string = 'test.cer';
let fd: number = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY).fd;
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  securityManager.installEnterpriseReSignatureCertificate(
    wantTemp, certificateAlias, fd, accountId);
  console.info('Success in installing enterprise re signature certificate.');
} catch (err) {
  console.error(`Failed to install enterprise re signature certificate.
    Code: ${err.code}, message: ${err.message}`);
};
```

## securityManager.uninstallEnterpriseReSignatureCertificate24+

uninstallEnterpriseReSignatureCertificate(admin: Want, certificateAlias: string, accountId: number): void

卸载企业应用重签名证书。卸载企业重签名证书后，使用该证书签名的应用在设备重启前正常运行，设备重启后无法运行。

使用场景：

1.安装新证书：调用[installEnterpriseReSignatureCertificate](js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24)接口安装新证书后，经新证书重签名的应用可正常运行。如果旧签名证书对应的应用为超级设备管理应用，需先取消激活后才能卸载证书，否则卸载证书后该应用无法卸载且无法运行。

2.恢复误删证书：调用[installEnterpriseReSignatureCertificate](js-apis-enterprise-securitymanager.md#securitymanagerinstallenterpriseresignaturecertificate24)接口重新安装误删除的证书后，已重签名的应用可正常运行，不受影响。

**注意** 

删除证书常见证书过期和证书泄露场景，建议开发者在实现该功能时，强提示管理员谨慎删除证书，并确保删除证书前加载新的重签名证书，并完成所有应用更新切换到新的重签名证书，否则重启后历史安装的应用将无法运行。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| certificateAlias | string | 是 | 证书别名，必须以'.cer'结尾。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201008 | The certificate does not exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let certificateAlias: string = 'test.cer';
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  securityManager.uninstallEnterpriseReSignatureCertificate(
    wantTemp, certificateAlias, accountId);
  console.info('Success in uninstalling enterprise re signature certificate.');
} catch (err) {
  console.error(`Failed to uninstall enterprise re signature certificate.
    Code: ${err.code}, message: ${err.message}`);
};
```

## securityManager.setScreenWatermarkImage

setScreenWatermarkImage(admin: Want, pixelMap: image.PixelMap): void

设置屏幕水印策略，对所有用户生效。

**说明** 

1. 屏幕水印策略会将设置的图片平铺覆盖整个屏幕，建议使用带透明度的图片以确保设备屏幕内容可见。
2. 当水印图片尺寸小于屏幕时，图片会被拉伸；当水印图片尺寸大于屏幕时，图片会被压缩。该实现方式与应用级别水印的重复平铺方式不同。
3. 在多个MDM应用场景下，遵循[配置](../harmonyos-guides/mdm-kit-multi-mdm.md#规则3配置)规则。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图像对象。图片宽度不超过设备屏幕宽度的两倍，图片高度不超过设备屏幕高度的两倍。图片像素占用大小不得超过128MB。图片像素占用大小计算公式：图片宽度(像素)×图片高度(像素)×每个像素占用的字节数（通常为4）。例如：一张100×100的图片，像素占用大小为100×100×4=40000字节。对于1920×1080分辨率的屏幕，若使用相同分辨率的图片，像素占用大小为1920×1080×4=8294400字节（约7.9MB）。 |

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
import { securityManager } from '@kit.MDMKit';
import { common, Want } from '@kit.AbilityKit';
import { image } from '@kit.ImageKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
// 此处'test.png'仅作示例，请开发者自行替换
const path: string = context.filesDir + "/test.png";
// 创建ImageSource
const imageSource: image.ImageSource = image.createImageSource(path);
// 创建PixelMap
imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
  try {
    securityManager.setScreenWatermarkImage(wantTemp, pixelMap);
    console.info(`Succeeded in setting screen watermark image.`);
  } catch (err) {
    console.error(`Failed to set screen watermark image. Code: ${err.code}, message: ${err.message}`);
  }
}).catch((err: Error) => {
  console.error(`Failed to create PixelMap. message: ${err.message}`);
});
```

## securityManager.cancelScreenWatermarkImage

cancelScreenWatermarkImage(admin: Want): void

取消屏幕水印策略，对所有用户生效。取消成功后，设备屏幕上的水印消失。当设备不再需要屏幕水印保护时，企业可调用此接口取消水印策略。只有设置屏幕水印的用户才能取消该水印，例如用户100设置的屏幕水印，用户101无法取消。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

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

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
    securityManager.cancelScreenWatermarkImage(wantTemp);
    console.info(`Succeeded in canceling screen watermark image.`);
} catch (err) {
    console.error(`Failed to cancel screen watermark image. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setDisallowedPermission

setDisallowedPermission(admin: Want, permission: string, disallow: boolean, accountId: number): void

禁用指定用户下的指定权限，禁用后指定用户下的所有应用申请和使用指定权限时默认拒绝。适用于企业安全合规场景，如禁用相机、麦克风等高风险权限防止隐私泄露，或禁用特定功能（如蓝牙分享）防止企业数据外传。

**说明** 

1. 只能禁用[权限APL等级](../harmonyos-guides/app-permission-mgmt-overview.md#权限机制中的基本概念)为normal或system\_basic的权限，否则返回错误码9201045。
2. 单个用户下最多可以禁用200个权限。
3. 权限禁用后，仅影响应用（系统应用和普通应用）使用对应的权限，不影响系统SA使用对应的权限。
4. 在多个MDM应用场景下，针对同一个权限设置[从严管控](../harmonyos-guides/mdm-kit-multi-mdm.md#规则1从严管控)，不同权限设置[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| permission | string | 是 | 权限名称。 |
| disallow | boolean | 是 | 是否禁用。true表示禁用，false表示取消禁用。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201045 | This permission cannot be disallowed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let permission: string = 'ohos.permission.CAMERA';
let disallow: boolean = true;
let accountId: number = 100;
try {
  securityManager.setDisallowedPermission(wantTemp, permission, disallow, accountId);
  console.info(`Succeeded in setting disallowed permission.`);
} catch (err) {
  console.error(`Failed to set disallowed permission. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getDisallowedPermissions

getDisallowedPermissions(admin: Want | null, accountId: number): Array<string>

获取指定用户下禁用的权限列表。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。当admin为null时，表示获取所有企业设备管理应用下发的禁用权限列表，返回合并后的结果。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回禁用的权限列表。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  let result: Array<string> = securityManager.getDisallowedPermissions(wantTemp, accountId);
  console.info(`Succeeded in getting disallowed permissions, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get disallowed permissions. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.addAllowedPermissionBundle

addAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void

将应用添加至权限使用例外名单，例外名单中的应用不受[setDisallowedPermission](js-apis-enterprise-securitymanager.md#securitymanagersetdisallowedpermission)设置的权限禁用策略限制。适用于企业应用场景，如相机权限被禁用时，允许考勤应用、协作办公应用继续使用相机功能，保障企业关键业务正常运行。

**说明** 

1. 必须先通过[setDisallowedPermission](js-apis-enterprise-securitymanager.md#securitymanagersetdisallowedpermission)接口禁用权限后，才能添加应用到权限使用例外名单，否则返回错误码9201044。
2. 应用实际未申请指定权限时，不可将应用添加到权限使用例外名单中。例如相机权限被禁用时，A应用实际未申请相机权限，则不能添加A应用到相机权限使用例外名单中，返回错误码9200012。可以通过[bm dump](../harmonyos-guides/bm-tool.md#查询应用信息命令dump)命令查询应用是否申请指定权限。
3. 当指定权限通过[setDisallowedPermission](js-apis-enterprise-securitymanager.md#securitymanagersetdisallowedpermission)接口取消禁用后，该权限对应的权限使用例外名单会同步清理。
4. 所有用户下单个权限最多可以设置1024个应用到权限使用例外名单。
5. 系统应用和普通应用都可以添加。
6. 在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| permission | string | 是 | 权限名称。 |
| applicationInstance | [common.ApplicationInstance](js-apis-enterprise-common.md#applicationinstance) | 是 | 需添加到权限使用例外名单的应用实例信息。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201015 | The application is not installed. |
| 9201044 | This permission is not disallowed. Applications cannot be added to or removed from the trustlist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let permission: string = 'ohos.permission.CAMERA';
let disallow: boolean = true;
let accountId: number = 100;
// 该应用已经申请了ohos.permission.CAMERA权限
let appInstance: common.ApplicationInstance = {
  appIdentifier: '123456789',
  appIndex: 0,
  accountId: 100
};
try {
  // 禁用ohos.permission.CAMERA权限
  securityManager.setDisallowedPermission(wantTemp, permission, disallow, accountId);
  // 设置指定应用可以继续使用ohos.permission.CAMERA权限
  securityManager.addAllowedPermissionBundle(wantTemp, permission, appInstance);
  console.info(`Succeeded in adding allowed permission bundle.`);
} catch (err) {
  console.error(`Failed to add allowed permission bundle. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.removeAllowedPermissionBundle

removeAllowedPermissionBundle(admin: Want, permission: string, applicationInstance: common.ApplicationInstance): void

从权限使用例外名单中移除指定应用，移除后该应用不能继续使用对应的权限。

**说明** 

必须先通过[setDisallowedPermission](js-apis-enterprise-securitymanager.md#securitymanagersetdisallowedpermission)接口禁用权限后，才能从权限使用例外名单移除应用，否则返回错误码9201044。

在多个MDM应用场景下，遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| permission | string | 是 | 权限名称。 |
| applicationInstance | [common.ApplicationInstance](js-apis-enterprise-common.md#applicationinstance) | 是 | 需从权限使用例外名单移除的应用实例信息。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9201044 | This permission is not disallowed. Applications cannot be added to or removed from the trustlist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let permission: string = 'ohos.permission.CAMERA';
let appInstance: common.ApplicationInstance = {
  appIdentifier: '736498586',
  appIndex: 0,
  accountId: 100
};
try {
  securityManager.removeAllowedPermissionBundle(wantTemp, permission, appInstance);
  console.info(`Succeeded in removing allowed permission bundle.`);
} catch (err) {
  console.error(`Failed to remove allowed permission bundle. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getAllowedPermissionBundles

getAllowedPermissionBundles(admin: Want | null, permission: string, accountId: number): Array<common.ApplicationInstance>

获取权限使用例外名单的应用列表。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | null | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。当admin为null时，表示获取所有企业设备管理应用下发的权限使用例外应用名单，返回合并后的结果。 |
| permission | string | 是 | 权限名称。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[common.ApplicationInstance](js-apis-enterprise-common.md#applicationinstance)> | 返回权限使用例外名单列表。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager, common } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let permission: string = 'ohos.permission.CAMERA';
let accountId: number = 100;
try {
  let result: Array<common.ApplicationInstance> =
    securityManager.getAllowedPermissionBundles(wantTemp, permission, accountId);
  console.info(`Succeeded in getting allowed permission bundles, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed permission bundles. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setWatermarkImage

setWatermarkImage(admin: Want, bundleName: string, source: string | image.PixelMap, accountId: number, properties:WatermarkProperties): void

为指定用户的指定应用设置水印策略。当前只支持最多保存100个策略。

**说明** 

本接口适用于企业场景下为三方应用设置水印，降低企业信息泄露风险。不建议为系统应用设置水印（如：桌面应用），可能存在未知异常。

当水印属性[properties](js-apis-enterprise-securitymanager.md#watermarkproperties)行列参数的取值范围是[1, 255]内的整数。若传入小于1或大于255的值，接口会返回错误码9200012。

当水印属性行数和列数都为1时，居中显示单个水印图片。当水印属性行数为m，列数为n时，按m行n列的网格布局排列显示m\*n个水印图片。当水印属性行列参数过大，导致网格布局无法适应窗口大小时，水印会以窗口左上角为原点，以平铺方式重复覆盖整个应用窗口界面，水印图片超出界面右侧、下侧的部分会被裁剪（例如屏幕宽高是1260\*2720，水印图片宽高是100\*100，若设置的行数超过27，或设置的列数超过12，水印会以平铺方式重复覆盖整个应用窗口界面）。

在多个MDM应用场景下，同一个用户下的同一个应用的水印遵循[独占](../harmonyos-guides/mdm-kit-multi-mdm.md#规则2独占)规则。不同用户、不同应用的水印遵循[合并](../harmonyos-guides/mdm-kit-multi-mdm.md#规则4合并)规则。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](js-apis-app-ability-want.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | 是 | 被设置水印的应用包名。 |
| source | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | string表示图像路径，图像路径为应用沙箱路径(应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系))等应用有权限访问的路径。  image.PixelMap表示图像对象。  图像像素占用大小不得超过500KB。  图像像素占用大小计算公式：图像宽度(像素)×图像高度 (像素)×每个像素占用的字节数（通常为4）。例如：一张 100x100 的图片，图像像素占用大小为100×100×4=40000字节。 |
| accountId | number | 是 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| properties | [WatermarkProperties](js-apis-enterprise-securitymanager.md#watermarkproperties) | 是 | 配置水印的行列数。 |

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
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
// 需根据实际情况进行替换。示例代码水印属性行数和列数都设为1，会居中显示单个水印图片
let properties: securityManager.WatermarkProperties = {
  intervalsRow: 1,
  intervalsCol: 1
};
try {
  securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId, properties);
  console.info(`Succeeded in setting watermarkImage policy.`);
} catch (err) {
  console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
// 需根据实际情况进行替换。设备屏幕宽高是1260*2720，水印图片宽高是100*100，示例代码水印属性行数为27，列数为12，按27行12列的网格布局排列显示27*12个水印图片
let properties: securityManager.WatermarkProperties = {
  intervalsRow: 27,
  intervalsCol: 12
};
try {
  securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId, properties);
  console.info(`Succeeded in setting watermarkImage policy.`);
} catch (err) {
  console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let bundleName: string = 'com.example.myapplication';
let source: string = '/data/storage/el1/base/test.png';
let accountId: number = 100;
// 需根据实际情况进行替换。设备屏幕宽高是1260*2720，水印图片宽高是100*100，示例代码水印属性行数为28，列数为12，28 * 100 > 2720，网格布局无法适应窗口大小，水印会以窗口左上角为原点，以平铺方式重复覆盖整个应用窗口界面，超出界面右侧、下侧的水印图片会被裁剪
let properties: securityManager.WatermarkProperties = {
  intervalsRow: 28,
  intervalsCol: 12
};
try {
  securityManager.setWatermarkImage(wantTemp, bundleName, source, accountId, properties);
  console.info(`Succeeded in setting watermarkImage policy.`);
} catch (err) {
  console.error(`Failed to set watermarkImage policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getWatermarkImageApps

getWatermarkImageApps(admin: Want, accountId: number): Array<string>

获取指定用户下已设置水印的应用程序包名列表。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

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
| Array<string> | 返回已设置水印的应用程序包名列表。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// 需根据实际情况进行替换
let accountId: number = 100;
try {
  let result: Array<string> = securityManager.getWatermarkImageApps(wantTemp, accountId);
  console.info(`Succeeded in getting watermark image apps, result : ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get watermark image apps. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setWeakPinEnable

setWeakPinEnable(isEnable: boolean, fd?: number): void

设置锁屏弱密码校验的弱密码库。设置弱密码库后，用户设置锁屏密码时，系统会根据弱密码库中的弱密码列表对用户设置的密码进行校验，如果密码存在于弱密码列表中，将拒绝设置该密码，防止用户设置过于简单的密码。适用于企业安全合规场景，如防止员工使用常见弱密码（如123456、000000等），提升设备安全防护能力。取消弱密码库后，用户设置锁屏密码时将不再进行弱密码校验。弱密码校验是在已有密码校验逻辑基础上的补充，不会替代已有的校验规则（如密码长度、复杂度等），设置和取消弱密码库，都不会影响已有的密码校验逻辑。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnable | boolean | 是 | 是否设置弱密码库。true表示设置，false表示取消。 |
| fd | number | 否 | 弱密码库文件的文件描述符。设置弱密码库时必填，取消弱密码库时忽略。  弱密码库文件需要放置于应用沙箱路径（应用沙箱路径和真实路径的对应关系可参见：[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)）等应用有权限访问的路径下。  文件每行对应一个弱密码。  文件大小不能超过16MB。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |

**示例：**

弱密码库文件示例（weak\_pin.txt），每行对应一个弱密码：

```txt
123456
000000
111111
888888
666666
```

代码示例：

```ts
import { securityManager } from '@kit.MDMKit';
import { fileIo } from '@kit.CoreFileKit';
 
// 需根据实际情况进行替换，弱密码文件需要放置在应用沙箱目录下
// 弱密码文件格式：每行对应一个弱密码，如123456、000000等
const filePath = '/data/storage/el1/base/weak_pin.txt';
let fd: number = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY).fd;
try {
  securityManager.setWeakPinEnable(true, fd);
  console.info(`Succeeded in setting weak pin enable.`);
} catch (err) {
  console.error(`Failed to set weak pin enable. Code: ${err.code}, message: ${err.message}`);
} finally {
  fileIo.closeSync(fd);
}
```

## securityManager.isWeakPinEnabled

isWeakPinEnabled(): boolean

查询锁屏弱密码库是否已设置。企业可通过此接口查询当前弱密码库的状态，用于策略审计和合规性检查。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示弱密码库已设置，false表示未设置。 |

**错误码**：

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200016 | Service timeout. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
 
try {
  let result: boolean = securityManager.isWeakPinEnabled();
  console.info(`Succeeded in checking weak pin enabled, result: ${result}`);
} catch (err) {
  console.error(`Failed to check weak pin enabled. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.openSession

openSession(accountId: number): Promise<Uint8Array>

打开用户身份认证凭据变更会话，获取挑战值（challenge，用于后续身份认证的防重放校验）。使用Promise异步回调。

**说明** 

系统会话是唯一的，多次调用openSession开启会话，只有最后一次开启的会话生效，之前的会话会被自动关闭。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回挑战值。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 开发者需替换为实际的账户ID
let accountId: number = 100;
securityManager.openSession(accountId).then((challenge: Uint8Array) => {
  console.info(`Succeeded in opening session, challenge: ${JSON.stringify(challenge)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to open session. Code: ${err.code}, message: ${err.message}`);
});
```

## securityManager.closeSession

closeSession(accountId: number): void

关闭用户身份认证凭据变更会话。

**说明** 

系统会话是唯一的，同一时刻只有一个有效会话。会话在以下情况下会被关闭：

1. 主动调用closeSession关闭。
2. 再次调用openSession时，旧会话自动关闭。
3. 会话超期（默认10分钟）自动关闭。

会话关闭后，该会话对应的挑战值和authToken均失效，需重新获取。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';

let accountId: number = 100;
try {
  securityManager.closeSession(accountId);
  console.info('Succeeded in closing session.');
} catch(err) {
  console.error(`Failed to close session. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.addUserExtendCredential

addUserExtendCredential(info: AddCredentialInfo, accountId: number): Promise<Uint8Array>

为指定账户添加三方自定义身份认证凭据，传入认证插件信息和认证令牌（可选），并获取凭据ID。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AddCredentialInfo](js-apis-enterprise-securitymanager.md#addcredentialinfo) | 是 | 指示添加凭据的信息。 |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回凭据ID。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9201052 | USB key session time out. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: number = 100;
let info: securityManager.AddCredentialInfo = {
  pluginInfo: 'com.example.ukey_plugin'
};
securityManager.addUserExtendCredential(info, accountId).then((credentialId: Uint8Array) => {
  console.info(`Succeeded in adding credential, credentialId: ${JSON.stringify(credentialId)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add credential. Code: ${err.code}, message: ${err.message}`);
});
```

## securityManager.removeUserExtendCredential

removeUserExtendCredential(info: RemoveCredentialInfo, accountId: number): void

根据凭据ID删除三方自定义身份认证凭据，传入凭据ID和认证令牌（可选）。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [RemoveCredentialInfo](js-apis-enterprise-securitymanager.md#removecredentialinfo) | 是 | 指示删除凭据的信息。 |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 9201052 | USB key session time out. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';

let accountId: number = 100;
let credentialId: Uint8Array = new Uint8Array([1, 2, 3, 4]);
let info: securityManager.RemoveCredentialInfo = {
  credentialId: credentialId
};
try {
  securityManager.removeUserExtendCredential(info, accountId);
  console.info('Succeeded in removing credential.');
} catch(err) {
  console.error(`Failed to remove credential. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getUserExtendCredential

getUserExtendCredential(accountId: number): Promise<UserExtCredentialInfo[]>

获取指定账户的三方自定义身份认证凭据信息。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UserExtCredentialInfo](js-apis-enterprise-securitymanager.md#userextcredentialinfo)[]> | Promise对象，返回三方自定义身份认证凭据信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let accountId: number = 100;
securityManager.getUserExtendCredential(accountId).then((credentials: securityManager.UserExtCredentialInfo[]) => {
  console.info(`Succeeded in getting credentials: ${JSON.stringify(credentials)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get credentials. Code: ${err.code}, message: ${err.message}`);
});
```

## securityManager.setUnlockPolicy

setUnlockPolicy(policy: UnlockPolicy, accountId: number): void

设置指定账户的设备解锁策略。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | [UnlockPolicy](js-apis-enterprise-securitymanager.md#unlockpolicy) | 是 | 指示设备解锁策略。 |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';

let accountId: number = 100;
try {
  securityManager.setUnlockPolicy(securityManager.UnlockPolicy.EXTENDED_AUTH_REQUIRED, accountId);
  console.info('Succeeded in setting unlock policy.');
} catch(err) {
  console.error(`Failed to set unlock policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.getUnlockPolicy

getUnlockPolicy(accountId: number): UnlockPolicy

获取指定账户的设备解锁策略。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accountId | number | 是 | 操作系统账户ID。取值范围：大于等于0。  accountId可以通过[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9)等接口来获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UnlockPolicy](js-apis-enterprise-securitymanager.md#unlockpolicy) | 指示设备解锁策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';

let accountId: number = 100;
try {
  let policy = securityManager.getUnlockPolicy(accountId);
  console.info(`Succeeded in getting unlock policy: ${policy}`);
} catch(err) {
  console.error(`Failed to get unlock policy. Code: ${err.code}, message: ${err.message}`);
}
```

## securityManager.setDeviceSecurityLevelPolicy

setDeviceSecurityLevelPolicy(level: DeviceSecurityLevelPolicy): void

设置设备安全等级策略。适用于企业统一管控终端安全基线的场景，如要求设备仅保持在出厂默认安全等级。调用本接口前，可通过[common.isFeatureSupported](js-apis-enterprise-common.md#commonisfeaturesupported)接口（入参为common.ManagedFeature.DEVICE\_SECURITY\_LEVEL）查询设备是否支持设备安全等级特性。

**说明** 

1. 设备安全等级是在PC/2in1设备上提供的分级安全机制，按照对系统安全性的影响程度划分为不同等级，系统安全性由高到低依次为DSL0、DSL1、DSL2。
2. DSL0：出厂默认安全，设备保持出厂时的默认安全配置，未对系统安全能力做降级，安全性最高。
3. DSL1：降低安全性，在DSL0的基础上适度放宽部分系统安全管控，安全性低于DSL0。
4. DSL2：宽松安全性，在DSL1的基础上进一步放宽系统安全管控，安全性最低。
5. 本接口用于设置用户可选择的设备安全等级范围，各策略对应的可选等级请参见[DeviceSecurityLevelPolicy](js-apis-enterprise-securitymanager.md#devicesecuritylevelpolicy)。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**设备行为差异：** 该接口在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [DeviceSecurityLevelPolicy](js-apis-enterprise-securitymanager.md#devicesecuritylevelpolicy) | 是 | 设备安全等级策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200012 | Parameter verification failed. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |

**示例：**

```ts
import { common, securityManager } from '@kit.MDMKit';

// 调用本接口前，先查询设备是否支持设备安全等级特性
let isSupported: boolean = common.isFeatureSupported(common.ManagedFeature.DEVICE_SECURITY_LEVEL);
if (isSupported) {
  try {
    securityManager.setDeviceSecurityLevelPolicy(securityManager.DeviceSecurityLevelPolicy.ALLOW_BALANCED);
    console.info('setDeviceSecurityLevelPolicy success');
  } catch (err) {
    console.error('setDeviceSecurityLevelPolicy fail: ' + JSON.stringify(err));
  }
} else {
  console.info('The device security level feature is not supported.');
}
```

## securityManager.getDeviceSecurityLevelPolicy

getDeviceSecurityLevelPolicy(): DeviceSecurityLevelPolicy

获取设备安全等级策略。

**说明** 

1. 本接口返回的设备安全等级策略为用户可选择的设备安全等级范围，分级机制及各策略对应的可选等级请参见[setDeviceSecurityLevelPolicy](js-apis-enterprise-securitymanager.md#securitymanagersetdevicesecuritylevelpolicy)。
2. 设备未设置过该策略时，返回默认值DEFAULT\_ENFORCED。

**起始版本：** 26.0.1

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_SECURITY

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceSecurityLevelPolicy](js-apis-enterprise-securitymanager.md#devicesecuritylevelpolicy) | 设备安全等级策略。 |

**错误码：**

以下错误码的详细介绍请参见[企业设备管理错误码](errorcode-enterprisedevicemanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9200016 | Service timeout. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例：**

```ts
import { securityManager } from '@kit.MDMKit';

try {
  let policy = securityManager.getDeviceSecurityLevelPolicy();
  console.info('getDeviceSecurityLevelPolicy policy: ' + policy);
} catch (err) {
  console.error('getDeviceSecurityLevelPolicy fail: ' + JSON.stringify(err));
}
```

## CertBlob

证书信息。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inData | Uint8Array | 否 | 否 | 证书的二进制内容。 |
| alias | string | 否 | 否 | 证书别名，别名长度小于40个字符。 |

## PasswordPolicy

设备锁屏口令策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| complexityRegex | string | 否 | 是 | 口令复杂度正则表达式。 |
| validityPeriod | number | 否 | 是 | 密码有效期（单位：毫秒）。 |
| additionalDescription | string | 否 | 是 | 口令复杂度描述文本，例如：密码中必须包含字母、数字、特殊字符，至少8个字符，最多30个字符。 |
| passwordAlgs | [PasswordAlgs](js-apis-enterprise-securitymanager.md#passwordalgs) | 否 | 是 | 处理口令数据使用的加密算法。设置后，PC/2in1设备上将原始口令处理成口令凭据会使用该参数指定的加密算法，其他设备无效果。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

## ClipboardPolicy

设备剪贴板策略。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认，表示无策略。 |
| IN\_APP | 1 | 剪贴板可在同一应用使用。 |
| LOCAL\_DEVICE | 2 | 剪贴板可在同一设备使用。 |
| CROSS\_DEVICE | 3 | 剪贴板可跨设备使用。 |

## ApplicationInstance20+

应用实例。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appIdentifier | string | 否 | 否 | 应用[唯一标识符](js-apis-bundlemanager-bundleinfo.md#signatureinfo)，如果应用没有appIdentifier可使用appId代替，可以通过接口[bundleManager.getBundleInfo](js-apis-bundlemanager.md#bundlemanagergetbundleinfo14-2)获取bundleInfo.signatureInfo.appIdentifier和bundleInfo.signatureInfo.appId。 |
| accountId | number | 否 | 否 | 用户ID，指定具体用户，取值范围：大于等于0。accountId可以通过@ohos.account.osAccount中的[getOsAccountLocalId](js-apis-osaccount.md#getosaccountlocalid9-1)等接口来获取。 |
| appIndex | number | 否 | 否 | 表示分身应用的索引，默认值为0。  appIndex为0时，表示主应用。appIndex大于0时，表示指定的分身应用。 |

## PermissionManagedState20+

应用权限的管理状态。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 1 | 默认由用户授予。 |
| GRANTED | 0 | 已静默授予。 |
| DENIED | -1 | 已静默拒绝。 |

## WatermarkProperties

水印属性。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| intervalsRow | number | 否 | 否 | 显示水印的行数。 |
| intervalsCol | number | 否 | 否 | 显示水印的列数。 |

## PasswordAlgs

处理口令数据使用的加密算法。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCRYPT\_HKDF\_AES | 0 | SCRYPT-HKDF-AES组合加密算法。 |
| SCRYPT\_HKDF\_SM4 | 1 | SCRYPT-HKDF-SM4组合加密算法。 |

## AddCredentialInfo

表示添加凭据的信息。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pluginInfo | string | 否 | 否 | 指示认证插件信息。 |
| authToken | Uint8Array | 否 | 是 | 指示认证令牌。 |

## RemoveCredentialInfo

表示删除凭据的信息。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialId | Uint8Array | 否 | 否 | 指示凭据ID。 |
| authToken | Uint8Array | 否 | 是 | 指示认证令牌。 |

## UserExtCredentialInfo

表示三方自定义身份认证凭据的信息。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| credentialId | Uint8Array | 否 | 否 | 指示凭据ID。 |
| pluginInfo | string | 否 | 否 | 指示认证插件信息。 |

## UnlockPolicy

表示设备解锁策略。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 系统内置认证方式单独解锁，使用系统内置的锁屏认证方式解锁设备。 |
| EXTENDED\_AUTH\_ONLY | 1 | 三方自定义认证单独解锁，解锁设备时仅通过三方自定义认证方式进行身份验证，无需系统锁屏密码。 |
| EXTENDED\_AUTH\_REQUIRED | 2 | 三方自定义认证与系统内置认证融合解锁，解锁设备时需同时通过三方自定义认证方式和系统锁屏密码进行身份验证。 |

## DeviceSecurityLevelPolicy

设备安全等级策略枚举。

**起始版本：** 26.0.1

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_ENFORCED | 0 | 仅可选出厂默认安全（DSL0）。 |
| ALLOW\_BALANCED | 1 | 可选出厂默认安全（DSL0）和降低安全性（DSL1）。 |
| ALLOW\_FLEXIBLE | 2 | 可选出厂默认安全（DSL0）、降低安全性（DSL1）和宽松安全性（DSL2）。 |
