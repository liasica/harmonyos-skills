---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-recoverykey
title: recoveryKey（企业恢复密钥）
breadcrumb: API参考 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > ArkTS API > recoveryKey（企业恢复密钥）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9606f906956e735af4b8496bf340c094c164c0936112275361f5b976297ff25c
---

在确保用户数据安全性的基础上，提供用于加密硬盘数据的安全解密机制和重置锁屏密码的企业恢复密钥。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 5.0.3(15)

## 导入模块

```typescript
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
```

## EnterpriseRecoveryKeyInfo

企业恢复密钥及相关加密参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterpriseRecoveryKey | Uint8Array | 否 | 否 | AES-GCM-256加密后的企业恢复密钥。 |
| exportPublicKey | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的临时公钥。 |
| iv | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的iv。 |
| tag | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的tag。 |

## recoveryKey.getEnterpriseRecoveryKey

getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>

获取企业恢复密钥。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要获取企业恢复密钥的用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EnterpriseRecoveryKeyInfo](dataguard-recoverykey.md#enterpriserecoverykeyinfo)> | Promise对象，返回企业恢复密钥及相关加密参数的对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400202 | Invalid userId. |
| 1014400203 | The enterprise recovery key already exists. |

**示例：**

```typescript
import { buffer } from '@kit.ArkTS';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

async function getEnterpriseRecoveryKey() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
      console.info(`Succeeded in getting enterprise recovery key.`);
      console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
        .toString('hex')}`);
      console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
      console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
      console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (e) {
    console.error(`Failed to testGetEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
  }
}
```

## recoveryKey.getAuthChallenge

getAuthChallenge(): Promise<Uint8Array>

获取挑战值，在发起更新企业公钥证书、删除企业恢复密钥数据流程前，需要先获取挑战值。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回用于更新企业公钥证书或删除企业恢复密钥数据时的挑战值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |

**示例：**

```typescript
import { buffer } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
  console.info(`Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
});
```

## recoveryKey.updateEnterpriseCertificate

updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>

更新企业公钥证书流程，需要先调用[getAuthChallenge](dataguard-recoverykey.md#recoverykeygetauthchallenge)接口获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| signature | Uint8Array | 是 | 挑战值的[签名](../harmonyos-guides/recoverykey-signature.md)。 |
| cert | Uint8Array | 是 | PEM格式的公钥证书，以二进制的格式完整传递。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回0表示更新企业公钥证书成功，失败无返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400204 | Invalid signature. |
| 1014400205 | Invalid certificate. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

// 在实际应用中，signature应替换为由企业的公钥、私钥和挑战值生成的签名。
let signature: Uint8Array = new Uint8Array([0]);
// 在实际应用中，cert应替换为企业证书数据。
let cert: Uint8Array = new Uint8Array([0]);
recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
  console.info(`Succeeded in updating certificate. result is: ${ret}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
});
```

## recoveryKey.deleteEnterpriseRecoveryKey

deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>

删除企业恢复密钥相关数据，需要先调[getAuthChallenge](dataguard-recoverykey.md#recoverykeygetauthchallenge)接口获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要删除企业恢复密钥的用户ID。 |
| signature | Uint8Array | 是 | 挑战值的[签名](../harmonyos-guides/recoverykey-signature.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回0表示删除企业恢复密钥成功，失败无返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400202 | Invalid userId. |
| 1014400204 | Invalid signature. |

**示例：**

```typescript
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

async function deleteEnterpriseRecoveryKey() {
  try {
    // 在实际应用中，signature应替换为由企业的公钥、私钥和挑战值生成的签名。
    let signature: Uint8Array = new Uint8Array([0]);
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number)=>{
      console.info(`Succeeded in deleting enterprise recovery key. result is: ${ret}`);
    }).catch((error: BusinessError)=>{
      console.error(`Failed to delete enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
    });
  } catch (e) {
    console.error(`Failed to deleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
  }
}
```

## recoveryKey.verifyUserIdentityEnterprise

verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>

验证企业用户身份。在导出企业恢复密钥以重置锁屏密码之前，请先验证用户的锁屏密码。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要导出企业恢复密钥的用户ID。 |
| userType | number | 是 | [用户类型](js-apis-osaccount.md#osaccounttype)。可以通过调用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9)获取。 |
| pinCode | string | 是 | 用户锁屏密码，字符长度不超过64个字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400103 | Identity authentication failed. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400202 | Invalid userId. |

**示例：**

```typescript
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

/**
 * @param pinCode 用户输入的锁屏密码
 */
async function verifyUserIdentityEnterprise(pinCode: string) {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

    let userId: number = await accountManager.getOsAccountLocalId();
    let userType: number = accountType.valueOf();
    recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
      console.info(`Succeeded in verifying user identity.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to verify user identity. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    console.error(`Failed to verifyUserIdentityEnterprise. Code: ${e.code}, message: ${e.message}`);
  }
}
```

## recoveryKey.verifyUserByDialog

verifyUserByDialog(userId: number): Promise<void>

通过弹框验证企业用户身份。在导出企业恢复密钥以重置锁屏密码之前，通过弹框验证企业用户身份。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要导出企业恢复密钥的用户ID，需为正整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400006 | The user canceled the identity verification process. |
| 1014400102 | User identity authentication timed out. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400202 | Invalid userId. |

**示例：**

```typescript
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

async function getEnterpriseRecoveryKeyForPinByDialog() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    recoveryKey.verifyUserByDialog(userId).then(() => {
      console.info(`Succeeded in verifying user identity by dialog.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to verify user identity by dialog. Code: ${error.code}, message: ${error.message}`);
    })
  } catch (e) {
    console.error(`Failed to getEnterpriseRecoveryKeyForPinByDialog. Code: ${e.code}, message: ${e.message}`);
  }
}
```

## recoveryKey.getEnterpriseRecoveryKeyForResettingPin

getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>

导出用于重置锁屏密码的企业恢复密钥。先需要调用[verifyUserIdentityEnterprise](dataguard-recoverykey.md#recoverykeyverifyuseridentityenterprise)或[verifyUserByDialog](dataguard-recoverykey.md#recoverykeyverifyuserbydialog)接口验证身份，并在30秒内调用此接口。若超时后调用，系统会返回异常代码[1014400001](errorcode-enterprise-dataguard.md#section1014400001-系统服务异常)。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要导出企业恢复密钥的用户ID。 |
| userType | number | 是 | [用户类型](js-apis-osaccount.md#osaccounttype)。可以通过调用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EnterpriseRecoveryKeyInfo](dataguard-recoverykey.md#enterpriserecoverykeyinfo)> | Promise对象，返回企业恢复密钥及相关加密参数的对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1014400001 | System service error. |
| 1014400201 | Invalid device type. The current device is not an enterprise device. |
| 1014400202 | Invalid userId. |

**示例：**

```typescript
import { buffer } from '@kit.ArkTS';
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

async function getEnterpriseRecoveryKeyForResettingPin() {
  try {
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
    // 获取用户ID
    let userId: number = await accountManager.getOsAccountLocalId();
    // 获取用户类型
    let userType: number = accountType.valueOf();
    recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
      .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
        console.info(`Succeeded in getting enterprise recovery key for resetting pin.`);
        // 打印企业恢复密钥及相关加密参数
        console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
          .toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey)
          .toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
        console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
      }).catch((err: BusinessError) => {
      console.error(`Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (e) {
    console.error(`Failed to getEnterpriseRecoveryKeyForResettingPin. Code: ${e.code}, message: ${e.message}`);
  }
}
```

## recoveryKey.isRecoveryKeySupported

isRecoveryKeySupported(): boolean

检查设备是否支持解密数据恢复密钥。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，返回true表示支持解密数据恢复密钥，否则返回false。 |

**示例：**

```typescript
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

try {
  let isSupported: boolean = recoveryKey.isRecoveryKeySupported();
  console.info(`Succeeded in determining whether the device supports RecoveryKey. isSupported: ${isSupported}`);
} catch (e) {
  console.error(`Failed to determine whether the device supports RecoveryKey. Code: ${e.code}, message: ${e.message}.`);
}
```

## recoveryKey.isRecoveryKeyForResettingPinSupported

isRecoveryKeyForResettingPinSupported(): boolean

检查设备是否支持重置锁屏密码恢复密钥。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，返回true表示支持重置锁屏密码恢复密钥，否则返回false。 |

**示例：**

```typescript
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

try {
  let isSupported: boolean = recoveryKey.isRecoveryKeyForResettingPinSupported();
  console.info(`Succeeded in determining whether the device supports RecoveryKey for reset pinCode. isSupported: ${isSupported}`);
} catch (e) {
  console.error(`Failed to determine whether the device supports RecoveryKey for reset pinCode. Code: ${e.code}, message: ${e.message}.`);
}
```

## recoveryKey.isDataVolumeRecoveryKeySupported

isDataVolumeRecoveryKeySupported(): boolean

检查设备是否支持数据盘恢复密钥。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，返回true表示支持数据盘恢复密钥，否则返回false。 |

**示例：**

```typescript
import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

try {
  let isSupported: boolean = recoveryKey.isDataVolumeRecoveryKeySupported();
  console.info(`Succeeded in determining whether the device supports data volume RecoveryKey. isSupported: ${isSupported}`);
} catch (e) {
  console.error(`Failed to determine whether the device supports data volume RecoveryKey. Code: ${e.code}, message: ${e.message}.`);
}
```
