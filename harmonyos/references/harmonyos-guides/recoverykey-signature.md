---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/recoverykey-signature
title: 挑战值签名
breadcrumb: 指南 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > 企业恢复密钥 > 挑战值签名
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:08+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a4246350bcf0c629f89c8c89d34b2c62150d395532d04b5f299d52e0b7e9ddc1
---

## 背景

挑战值是一个32字节的随机数，用于防止签名重放攻击。在企业恢复密钥提供[更新企业公钥证书](recoverykey-update.md)和[删除企业恢复密钥](recoverykey-delete.md)场景下，均会使用挑战值来确保签名是企业对当前操作进行授权。签名使用ECC算法，是企业利用企业证书对应的私钥，对挑战值进行签名的。接口传入的挑战值签名必须是只包含原始ECDSA签名值的64字节内容，不能包含任何格式前缀。

## 自定义签名工具类SignUtil生成挑战值的签名

[updateEnterpriseCertificate](../harmonyos-references/dataguard-recoverykey.md#updateenterprisecertificate)和[deleteEnterpriseRecoveryKey](../harmonyos-references/dataguard-recoverykey.md#deleteenterpriserecoverykey)在生成挑战值的签名时可使用自定义签名工具类。使用时，请将SignUtil里的privateKey、publicKey，替换为企业的公私钥对。

```
1. import { cryptoFramework } from "@kit.CryptoArchitectureKit";

3. export class SignUtil {
4. public static async signInner(data: Uint8Array) : Promise<Uint8Array> {
5. // 替换成企业的私钥
6. let privateKey: string = "-----BEGIN EC PARAMETERS-----\n" +
7. "************\n" +
8. "-----END EC PARAMETERS-----\n" +
9. "-----BEGIN EC PRIVATE KEY-----\n" +
10. "**********************************************************************"  +
11. "-----END EC PRIVATE KEY-----";
12. // 替换成企业的公钥
13. let publicKey: string = "-----BEGIN PUBLIC KEY-----\n" +
14. "****************************************************************\n" +
15. "************************************************************\n" +
16. "-----END PUBLIC KEY-----\n" +
17. "-----BEGIN CERTIFICATE-----\n" +
18. "****************************************************************\n" +
19. "*******\n" +
20. "-----END CERTIFICATE-----\n";
21. let input1: cryptoFramework.DataBlob = { data };
22. let signAlg = "ECC_BrainPoolP256r1|SHA256";
23. let signer = cryptoFramework.createSign(signAlg);
24. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator("ECC_BrainPoolP256r1");
25. let keyPair = await asyKeyGenerator.convertPemKey(publicKey, privateKey);
26. await signer.init(keyPair.priKey);
27. let signData = await signer.sign(input1);
28. // 对签名的数据进行验签
29. let verifier = cryptoFramework.createVerify(signAlg);
30. verifier.initSync(keyPair.pubKey);
31. let res = verifier.verifySync(input1, signData);
32. console.info(`signature verify result: ${res}.`);
33. return signData.data;
34. }

36. public static async sign(data: Uint8Array) : Promise<Uint8Array> {
37. let signInnerResult = await SignUtil.signInner(data);
38. let result: Uint8Array = new Uint8Array(64);

40. let index = 0;
41. let length = 0;
42. let offset = 0;
43. while (index < signInnerResult.length) {
44. if (signInnerResult[index] === 0x02) {
45. length = index + 1 < signInnerResult.length ? signInnerResult[index + 1] : 0;
46. let end = index + 2 + length;
47. if (end <= signInnerResult.length) {
48. let copyArr = signInnerResult.subarray(end - 32, end);
49. result.set(copyArr, offset);
50. offset += 32;
51. }
52. index += 34;
53. } else {
54. index++;
55. }
56. }
57. return result;
58. }
59. }
```

## 生成挑战值的签名（更新企业公钥）

在更新企业公钥证书场景下，先获取挑战值，将下面方法中的certificate和ecPubNewStrBase64替换为企业的新证书和新公钥，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

```
1. import { util } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
4. import { SignUtil } from './SignUtil';

6. async function updateEnterpriseCertificate() {
7. // 替换成企业的新证书
8. const certificate =
9. "-----BEGIN CERTIFICATE-----\n" +
10. "****************************************************************\n" +
11. "*******\n" +
12. "-----END CERTIFICATE-----\n";

14. const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
15. const buffer = new ArrayBuffer(4);
16. const view = new DataView(buffer);
17. view.setUint32(0, 0x98010000);
18. const command: Uint8Array = new Uint8Array(buffer);
19. // 替换成企业的新公钥
20. const ecPubNewStrBase64 =
21. "****************************************************************\n";
22. let publicKey: Uint8Array = base64ToStringUint8Array(ecPubNewStrBase64);
23. publicKey = publicKey.subarray(publicKey.length - 65, publicKey.length);
24. let signData: Uint8Array = new Uint8Array(challenge.length + command.length + publicKey.length);
25. signData.set(challenge, 0);
26. signData.set(command, challenge.length);
27. signData.set(publicKey, challenge.length + command.length);
28. let signature: Uint8Array = await SignUtil.sign(signData);

30. const cert: Uint8Array = stringToUint8(certificate!);
31. recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
32. console.info(`Succeeded in updating certificate.`);
33. }).catch((error: BusinessError) => {
34. console.error(`Failed to update certificate. Code: ${error.code}, message: ${error.message}.`);
35. });
36. }

38. function stringToUint8(str: string): Uint8Array {
39. let result: Uint8Array = new Uint8Array([]);
40. try {
41. result = new util.TextEncoder('utf-8').encodeInto(str);
42. } catch (error) {
43. console.error(`Failed to encode to uint8. Code: ${error.code}, message: ${error.message}`);
44. }
45. return result;
46. }

48. function base64ToStringUint8Array(base64String: string): Uint8Array {
49. let base64 = new util.Base64Helper();
50. let uint8Array = base64.decodeSync(base64String, util.Type.BASIC);
51. return uint8Array;
52. }
```

## 生成挑战值的签名（删除企业恢复密钥）

在删除企业恢复密钥场景下，先获取挑战，然后调用自定义工具类SignUtil的sign签名方法生成挑战值的签名。

```
1. import { BusinessError, osAccount } from '@kit.BasicServicesKit';
2. import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
3. import { SignUtil } from './SignUtil';

5. async function deleteEnterpriseRecoveryKey() {
6. const challenge: Uint8Array = await recoveryKey.getAuthChallenge();
7. let signResult = await SignUtil.sign(challenge);
8. let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
9. let userId = await accountManager.getOsAccountLocalId();
10. recoveryKey.deleteEnterpriseRecoveryKey(userId, signResult).then((ret: number) => {
11. console.info(`Succeeded in deleting enterprise recovery key.`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to delete enterprise recovery key. Code: ${err.code}, message: ${err.message}.`);
14. });
15. }
```
