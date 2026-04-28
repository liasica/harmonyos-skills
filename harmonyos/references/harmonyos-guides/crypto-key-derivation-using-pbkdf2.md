---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-pbkdf2
title: 使用PBKDF2进行密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用PBKDF2进行密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34a4e320cf69d9b98a2d5c82c7355f1fde5b8e26d53088568d94a3aa3038bf55
---

对应的算法规格请查看[密钥派生算法规格：PBKDF2](crypto-key-derivation-overview.md#pbkdf2算法)。

## 开发步骤

1. 构造[PBKDF2Spec](../harmonyos-references/js-apis-cryptoframework.md#pbkdf2spec11)对象，作为密钥派生参数进行密钥派生。

   PBKDF2Spec是[KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#kdfspec11)的子类，需要指定：

   * algName：指定算法'PBKDF2'。
   * password：用于生成派生密钥的原始密码。

     如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
   * salt：盐值。
   * iterations：重复运算的次数，需要为正整数。
   * keySize：目标密钥的字节长度，需要为正整数。
2. 调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)，指定字符串参数'PBKDF2|SHA256'，创建密钥派生算法为PBKDF2、HMAC函数摘要算法为SHA256的密钥派生函数对象（Kdf）。
3. 输入PBKDF2Spec对象，调用[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)进行密钥派生。

   Kdf.generateSecret的多种调用形式如表所示。

   | 接口名 | 返回方式 |
   | --- | --- |
   | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | callback异步生成。 |
   | generateSecret(params: KdfSpec): Promise<DataBlob> | Promise异步生成。 |
   | generateSecretSync(params: KdfSpec): DataBlob | 同步生成。 |

* 通过await返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function kdfAwait() {
  4. let spec: cryptoFramework.PBKDF2Spec = {
  5. algName: 'PBKDF2',
  6. password: '123456',
  7. salt: new Uint8Array(16),
  8. iterations: 10000,
  9. keySize: 32
  10. };
  11. let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
  12. let secret = await kdf.generateSecret(spec);
  13. console.info('key derivation output: ' + secret.data);
  14. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/PBKDF2Derivation/entry/src/main/ets/pages/Await.ets#L15-L31)
* 通过Promise返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function kdfPromise() {
  5. let spec: cryptoFramework.PBKDF2Spec = {
  6. algName: 'PBKDF2',
  7. password: '123456',
  8. salt: new Uint8Array(16),
  9. iterations: 10000,
  10. keySize: 32
  11. };
  12. let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
  13. let kdfPromise = kdf.generateSecret(spec);
  14. kdfPromise.then((secret) => {
  15. console.info('key derivation output: ' + secret.data);
  16. }).catch((error: BusinessError) => {
  17. console.error(`key derivation failed: errCode: ${error.code}, message: ${error.message}`);
  18. });
  19. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/PBKDF2Derivation/entry/src/main/ets/pages/Promise.ets#L15-L35)
* 通过同步方式返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function kdfSync() {
  4. let spec: cryptoFramework.PBKDF2Spec = {
  5. algName: 'PBKDF2',
  6. password: '123456',
  7. salt: new Uint8Array(16),
  8. iterations: 10000,
  9. keySize: 32
  10. };
  11. let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
  12. let secret = kdf.generateSecretSync(spec);
  13. console.info('[Sync]key derivation output: ' + secret.data);
  14. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/PBKDF2Derivation/entry/src/main/ets/pages/Sync.ets#L15-L31)
