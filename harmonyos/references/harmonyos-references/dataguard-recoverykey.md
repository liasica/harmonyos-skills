---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-recoverykey
title: recoveryKey（企业恢复密钥）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2785c33b72a46098a61afe493b7d3b15201a8b823e7034e13ee89634f76c30cb
---

在确保用户数据安全性的基础上，提供用于加密硬盘数据的安全解密机制和和重置锁屏密码的企业恢复密钥。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 5.0.3(15)

## 导入模块

PC/2in1

```
1. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
```

## EnterpriseRecoveryKeyInfo

PC/2in1

企业恢复密钥及相关加密参数。

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterpriseRecoveryKey | Uint8Array | 否 | 否 | AES-GCM-256加密后的企业恢复密钥。 |
| exportPublicKey | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的临时公钥。 |
| iv | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的iv。 |
| tag | Uint8Array | 否 | 否 | AES-GCM-256加密时使用的tag。 |

## getEnterpriseRecoveryKey

PC/2in1

getEnterpriseRecoveryKey(userId: number): Promise<EnterpriseRecoveryKeyInfo>

获取企业恢复密钥。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 1014400001 | System service exception. |
| 1014400201 | Invalid device type, current device is not enterprise device. |
| 1014400202 | Invalid userId. |
| 1014400203 | Enterprise recovery key is already existed. |

**示例：**

```
1. import { buffer } from '@kit.ArkTS';
2. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
3. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

5. async function getEnterpriseRecoveryKey() {
6. try {
7. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
8. let userId: number = await accountManager.getOsAccountLocalId();
9. recoveryKey.getEnterpriseRecoveryKey(userId).then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
10. console.info(`Succeeded in getting enterprise recovery key.`);
11. console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
12. .toString('hex')}`);
13. console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey).toString('hex')}`);
14. console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
15. console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to get enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
18. });
19. } catch (e) {
20. console.error(`Failed to testGetEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
21. }
22. }
```

## getAuthChallenge

PC/2in1

getAuthChallenge(): Promise<Uint8Array>

获取挑战值，在发起更新企业公钥证书、删除企业恢复密钥数据流程前，需要先获取挑战值。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回用于更新企业公钥证书或删除企业恢复密钥数据时的挑战值。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1014400001 | System service exception. |
| 1014400201 | Invalid device type, current device is not enterprise device. |

**示例：**

```
1. import { buffer } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

5. recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
6. console.info(`Succeeded in getting challenge. challenge is: ${buffer.from(challenge).toString('hex')}`);
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to get challenge. Code: ${error.code}, message: ${error.message}`);
9. });
```

## updateEnterpriseCertificate

PC/2in1

updateEnterpriseCertificate(signature: Uint8Array, cert: Uint8Array): Promise<number>

更新企业公钥证书流程，需要先调[getAuthChallenge](dataguard-recoverykey.md#getauthchallenge)接口获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 1014400001 | System service exception. |
| 1014400201 | Invalid device type, current device is not enterprise device. |
| 1014400204 | Invalid signature. |
| 1014400205 | Invalid cert. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

4. // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
5. let signature: Uint8Array = new Uint8Array([0]);
6. // 在实际应用中，cert 应需替换为企业证书数据。
7. let cert: Uint8Array = new Uint8Array([0]);
8. recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number)=>{
9. console.info(`Succeeded in updating certificate. result is: ${ret}`);
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
12. });
```

## deleteEnterpriseRecoveryKey

PC/2in1

deleteEnterpriseRecoveryKey(userId: number, signature: Uint8Array): Promise<number>

删除企业恢复密钥相关数据，需要先调[getAuthChallenge](dataguard-recoverykey.md#getauthchallenge)接口获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。使用Promise异步回调。

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

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 1014400001 | System service exception. |
| 1014400201 | Invalid device type, current device is not enterprise device. |
| 1014400202 | Invalid userId. |
| 1014400204 | Invalid signature. |

**示例：**

```
1. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
2. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

4. async function deleteEnterpriseRecoveryKey() {
5. try {
6. // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
7. let signature: Uint8Array = new Uint8Array([0]);
8. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
9. let userId: number = await accountManager.getOsAccountLocalId();
10. recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number)=>{
11. console.info(`Succeeded in deleting enterprise recovery key. result is: ${ret}`);
12. }).catch((error: BusinessError)=>{
13. console.error(`Failed to delete enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
14. });
15. } catch (e) {
16. console.error(`Failed to deleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}`);
17. }
18. }
```

## verifyUserIdentityEnterprise

PC/2in1

verifyUserIdentityEnterprise(userId: number, userType: number, pinCode: string): Promise<void>

验证企业用户身份。在导出企业恢复密钥以重置锁屏密码之前，请先验证用户的锁屏密码。使用Promise异步回调。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要导出企业恢复密钥的用户ID。 |
| userType | number | 是 | [用户类型](js-apis-osaccount.md#osaccounttype) 。可以通过调用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9)获取。 |
| pinCode | string | 是 | 用户锁屏密码，字符长度不超过64位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1014400001 | System service exception. |
| 1014400103 | Authentication is failed. |
| 1014400201 | Invalid device type, current device is not enterprise device. |
| 1014400202 | Invalid userId. |

**示例：**

```
1. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
2. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

4. /**
5. * @param pinCode 用户输入的锁屏密码
6. */
7. async function verifyUserIdentityEnterprise(pinCode: string) {
8. try {
9. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
10. let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();

12. let userId: number = await accountManager.getOsAccountLocalId();
13. let userType: number = accountType.valueOf();
14. recoveryKey.verifyUserIdentityEnterprise(userId, userType, pinCode).then(() => {
15. console.info(`Succeeded in verifying user identity.`);
16. }).catch((error: BusinessError) => {
17. console.error(`Failed to verified user identity. Code: ${error.code}, message: ${error.message}`);
18. })
19. } catch (e) {
20. console.error(`Failed to verifyUserIdentityEnterprise. Code: ${e.code}, message: ${e.message}`);
21. }
22. }
```

## getEnterpriseRecoveryKeyForResettingPin

PC/2in1

getEnterpriseRecoveryKeyForResettingPin(userId: number, userType: number): Promise<EnterpriseRecoveryKeyInfo>

导出用于重置锁屏密码的企业恢复密钥。先需要调用[verifyUserIdentityEnterprise](dataguard-recoverykey.md#verifyuseridentityenterprise)接口验证身份，并在30秒内调用此接口。若超时后调用，系统会返回异常代码[1014400001](dataguard-error-code.md#section1014400001-系统内部错误)。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_RECOVERY\_KEY

**系统能力：** SystemCapability.PCService.RecoveryKeyService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 是 | 需要导出企业恢复密钥的用户ID。 |
| userType | number | 是 | [用户类型](js-apis-osaccount.md#osaccounttype) 。可以通过调用[getOsAccountType](js-apis-osaccount.md#getosaccounttype9)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EnterpriseRecoveryKeyInfo](dataguard-recoverykey.md#enterpriserecoverykeyinfo)> | Promise对象，返回企业恢复密钥及相关加密参数的对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](dataguard-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 1014400001 | System service exception. |
| 1014400201 | Invalid device type, current device is not enterprise device. |
| 1014400202 | Invalid userId. |

**示例：**

```
1. import { buffer } from '@kit.ArkTS';
2. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
3. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';

5. async function getEnterpriseRecoveryKeyForResettingPin() {
6. try {
7. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
8. let accountType: osAccount.OsAccountType = await accountManager.getOsAccountType();
9. // 获取用户ID
10. let userId: number = await accountManager.getOsAccountLocalId();
11. // 获取用户类型
12. let userType: number = accountType.valueOf();
13. recoveryKey.getEnterpriseRecoveryKeyForResettingPin(userId, userType)
14. .then((info: recoveryKey.EnterpriseRecoveryKeyInfo) => {
15. console.info(`Succeeded in getting enterprise recovery key for resetting pin.`);
16. // 打印企业恢复密钥及相关加密参数
17. console.info(`EnterpriseRecoveryKeyInfo enterpriseRecoveryKey: ${buffer.from(info.enterpriseRecoveryKey)
18. .toString('hex')}`);
19. console.info(`EnterpriseRecoveryKeyInfo exportPublicKey: ${buffer.from(info.exportPublicKey)
20. .toString('hex')}`);
21. console.info(`EnterpriseRecoveryKeyInfo iv: ${buffer.from(info.iv).toString('hex')}`);
22. console.info(`EnterpriseRecoveryKeyInfo tag: ${buffer.from(info.tag).toString('hex')}`);
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to get enterprise recovery key for resetting pin. Code: ${err.code}, message: ${err.message}`);
25. })
26. } catch (e) {
27. console.error(`Failed to getEnterpriseRecoveryKeyForResettingPin. Code: ${e.code}, message: ${e.message}`);
28. }
29. }
```
