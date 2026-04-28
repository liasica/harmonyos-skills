---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt
title: 使用SCRYPT进行密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用SCRYPT进行密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ad4eea339fb79a9ae3151b1a523e48e7a207e430e4632b75a41e753bf31d5a7
---

对应的算法规格请查看[密钥派生算法规格：SCRYPT](crypto-key-derivation-overview.md#scrypt算法)。

## 开发步骤

1. 构造[ScryptSpec](../harmonyos-references/js-apis-cryptoframework.md#scryptspec18)对象，作为密钥派生参数进行密钥派生。

   ScryptSpec是[KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#kdfspec11)的子类，需要指定：

   * algName：指定算法名为'SCRYPT'。
   * passphrase：用于生成派生密钥的原始密码。

     如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
   * salt：盐值。
   * n：迭代次数，需要为正整数。
   * p：并行化参数，需要为正整数。
   * r：块大小参数，需要为正整数。
   * maxMemory：最大内存限制参数，需要为正整数。
   * keySize：目标密钥的字节长度，需要为正整数。
2. 调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)，指定字符串参数'SCRYPT'，创建密钥派生算法为SCRYPT的密钥派生函数对象（Kdf）。
3. 输入SCRYPT对象，调用[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)进行密钥派生。

   Kdf.generateSecret的多种调用形式如表所示。

   | 接口名 | 返回方式 |
   | --- | --- |
   | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | callback异步生成。 |
   | generateSecret(params: KdfSpec): Promise<DataBlob> | Promise异步生成。 |
   | generateSecretSync(params: KdfSpec): DataBlob | 同步生成。 |

* 通过await返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { buffer } from '@kit.ArkTS';

  5. async function scryptAwait() {
  6. try {
  7. let spec: cryptoFramework.ScryptSpec = {
  8. algName: 'SCRYPT',
  9. salt: new Uint8Array(16),
  10. passphrase: 'password',
  11. n:1024,
  12. p:16,
  13. r:8,
  14. maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
  15. keySize: 64
  16. };
  17. let kdf = cryptoFramework.createKdf('SCRYPT');
  18. let secret = await kdf.generateSecret(spec);
  19. console.info('key derivation output: ' + secret.data);
  20. } catch(error) {
  21. let e: BusinessError = error as BusinessError;
  22. console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
  23. }
  24. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/SCRYPTDerivation/entry/src/main/ets/pages/Await.ets#L16-L42)
* 通过Promise返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { buffer } from '@kit.ArkTS';

  5. function scryptPromise() {
  6. let spec: cryptoFramework.ScryptSpec = {
  7. algName: 'SCRYPT',
  8. passphrase: '123456',
  9. salt: new Uint8Array(16),
  10. n:1024,
  11. p:16,
  12. r:8,
  13. maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
  14. keySize: 64
  15. };
  16. let kdf = cryptoFramework.createKdf('SCRYPT');
  17. let kdfPromise = kdf.generateSecret(spec);
  18. kdfPromise.then((secret) => {
  19. console.info('key derivation output: ' + secret.data);
  20. }).catch((error: BusinessError) => {
  21. console.error(`key derivation failed: errCode: ${error.code}, message: ${error.message}`);
  22. });
  23. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/SCRYPTDerivation/entry/src/main/ets/pages/Promise.ets#L16-L42)
* 通过同步方式返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { buffer } from '@kit.ArkTS';

  5. function kdfSync() {
  6. try {
  7. let spec: cryptoFramework.ScryptSpec = {
  8. algName: 'SCRYPT',
  9. passphrase: '123456',
  10. salt: new Uint8Array(16),
  11. n:1024,
  12. p:16,
  13. r:8,
  14. maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
  15. keySize: 64
  16. };
  17. let kdf = cryptoFramework.createKdf('SCRYPT');
  18. let secret = kdf.generateSecretSync(spec);
  19. console.info('[Sync]key derivation output: ' + secret.data);
  20. } catch(error) {
  21. let e: BusinessError = error as BusinessError;
  22. console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
  23. }
  24. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/SCRYPTDerivation/entry/src/main/ets/pages/Sync.ets#L15-L41)
