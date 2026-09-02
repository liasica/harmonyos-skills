---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature
title: 挑战值签名
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 挑战值签名
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1ca1900d9f2af297a428d275a618275a39cf9c67020a44798cc32f6637a23eff
---

## 背景

挑战值是一个32字节的随机数，用于防止签名重放攻击。在企业恢复密钥提供[更新企业公钥证书](recoverykey-update.md)和[删除企业恢复密钥](recoverykey-delete.md)场景下，均会使用挑战值来确保签名是企业对当前操作进行授权。签名使用ECC算法，是企业利用企业证书对应的私钥，对挑战值进行签名的。接口传入的挑战值签名必须是只包含原始ECDSA签名值的64字节内容，不能包含任何格式前缀。

## 自定义签名工具类SignUtil生成挑战值的签名

[updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#recoverykeyupdateenterprisecertificate)和[deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#recoverykeydeleteenterpriserecoverykey)在生成挑战值的签名时可使用自定义签名工具类。在“entry/src/main/ets/utils”目录下添加SignUtil.ets文件，使用时，将SignUtil里的privateKey、publicKey，替换为企业的公私钥对。

```typescript
import { util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export class SignUtil {
  private static TAG: string = 'EnterpriseRecoveryKey_Signature';
  private static DOMAIN: number = 0x0000;

  public static async signInner(data: Uint8Array): Promise<Uint8Array> {
    try {
      // 替换成企业的私钥
      let privateKey: string = '-----BEGIN EC PARAMETERS-----\n' +
        '******\n' +
        '-----END EC PARAMETERS-----\n' +
        '-----BEGIN EC PRIVATE KEY-----\n' +
        '******\n' +
        '-----END EC PRIVATE KEY-----';
      // 替换成企业的公钥
      let publicKey: string = '-----BEGIN PUBLIC KEY-----\n' +
        '******\n' +
        '-----END PUBLIC KEY-----\n' +
        '-----BEGIN CERTIFICATE-----\n' +
        '******\n' +
        '-----END CERTIFICATE-----\n';
      let input1: cryptoFramework.DataBlob = { data };
      let signAlg: string = 'ECC_BrainPoolP256r1|SHA256';
      let signer: cryptoFramework.Sign = cryptoFramework.createSign(signAlg);
      let asyKeyGenerator: cryptoFramework.AsyKeyGenerator =
        cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
      let keyPair: cryptoFramework.KeyPair = await asyKeyGenerator.convertPemKey(publicKey, privateKey);
      await signer.init(keyPair.priKey);
      let signData: cryptoFramework.DataBlob = await signer.sign(input1);
      // 对签名的数据进行验签
      let verifier: cryptoFramework.Verify = cryptoFramework.createVerify(signAlg);
      verifier.initSync(keyPair.pubKey);
      let res: boolean = verifier.verifySync(input1, signData);
      hilog.info(SignUtil.DOMAIN, SignUtil.TAG, `signature verify result: ${res}.`);
      return signData.data;
    } catch (e) {
      return Promise.reject(e);
    }
  }

  public static async sign(data: Uint8Array): Promise<Uint8Array> {
    let signInnerResult = await SignUtil.signInner(data);
    let result: Uint8Array = new Uint8Array(64);

    let index = 0;
    let length = 0;
    let offset = 0;
    while (index < signInnerResult.length) {
      if (signInnerResult[index] === 0x02 && index + 1 < signInnerResult.length) {
        length = signInnerResult[index + 1];
        let end = index + 2 + length;
        if (end <= signInnerResult.length && length === 32) {
          let copyArr = signInnerResult.subarray(end - 32, end);
          result.set(copyArr, offset);
          offset += 32;
        }
        index += 2 + length;
      } else {
        index++;
      }
    }
    return result;
  }

  public static stringToUint8(str: string): Uint8Array {
    let result: Uint8Array = new Uint8Array([]);
    try {
      let encoder = new util.TextEncoder('utf-8');
      result = encoder.encodeInto(str);
    } catch (error) {
      hilog.error(SignUtil.DOMAIN, SignUtil.TAG, `Failed to stringToUint8. Code: ${error.code}, message: ${error.message}`);
    }
    return result;
  }

  public static base64ToStringUint8Array(base64String: string): Uint8Array {
    let base64 = new util.Base64Helper();
    let uint8Array = base64.decodeSync(base64String, util.Type.BASIC);
    return uint8Array;
  }
}
```

## 生成挑战值的签名（更新企业公钥证书）

在更新企业公钥证书场景下，先获取挑战值，将下面方法中的certificate和ecPubNewStrBase64替换为企业的新证书和新公钥，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

1. 导入模块。

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { SignUtil } from '../SignUtil';
   ```
2. 使用企业公钥和私钥对挑战值进行签名，传入企业新证书，更新企业公钥证书。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_Update';
   const DOMAIN: number = 0x0000;

   // ...
   /**
    * 更新企业公钥证书
    */
   async function updateEnterpriseCertificate() {
     // 在实际应用中，certificate 应替换为企业证书数据。
     const certificate: string =
       '-----BEGIN CERTIFICATE-----\n' +
         '******\n' +
         '-----END CERTIFICATE-----\n';
     const cert: Uint8Array = SignUtil.stringToUint8(certificate);
     const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
     const buffer = new ArrayBuffer(4);
     const view = new DataView(buffer);
     view.setUint32(0, 0x98010000);
     const command: Uint8Array = new Uint8Array(buffer);
     // 替换成企业的新公钥
     const ecPubNewStrBase64 = '******\n';
     let publicKey: Uint8Array = SignUtil.base64ToStringUint8Array(ecPubNewStrBase64);
     publicKey = publicKey.subarray(publicKey.length - 65, publicKey.length);

     let signData: Uint8Array = new Uint8Array(challenge.length + command.length + publicKey.length);
     signData.set(challenge, 0);
     signData.set(command, challenge.length);
     signData.set(publicKey, challenge.length + command.length);
     // 在实际应用中，signature 应替换为由企业的公钥、私钥和挑战值生成的签名。
     let signature: Uint8Array = await SignUtil.sign(signData);

     recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
       hilog.info(DOMAIN, TAG, `Succeeded in updating certificate. result is: ${ret}`);
     }).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG, `Failed to update certificate. Code: ${error.code}, message: ${error.message}`);
     });
   }
   ```

## 生成挑战值的签名（删除企业恢复密钥）

在删除企业恢复密钥场景下，先获取挑战值，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

1. 导入模块。

   ```typescript
   import { BusinessError, osAccount } from '@kit.BasicServicesKit';
   import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { SignUtil } from '../SignUtil';
   ```
2. 使用企业公钥和私钥对挑战值进行签名，传入需要删除企业恢复密钥的用户ID，删除对应用户的企业恢复密钥。

   ```typescript
   const TAG: string = 'EnterpriseRecoveryKey_Delete';
   const DOMAIN: number = 0x0000;

   // ...
   /**
    * 删除企业恢复密钥
    */
   async function deleteEnterpriseRecoveryKey() {
     const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
     // 在实际应用中，signResult 应替换为由企业的公钥、私钥和挑战值生成的签名。
     let signResult = await SignUtil.sign(challenge);
     let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
     let userId = await accountManager.getOsAccountLocalId();

     recoveryKey.deleteEnterpriseRecoveryKey(userId, signResult).then((ret: number) => {
       hilog.info(DOMAIN, TAG, `Succeeded in deleting enterprise recovery key. result is: ${ret}`);
     }).catch((error: BusinessError) => {
       hilog.error(DOMAIN, TAG,
         `Failed to delete enterprise recovery key. Code: ${error.code}, message: ${error.message}`);
     });
   }
   ```
