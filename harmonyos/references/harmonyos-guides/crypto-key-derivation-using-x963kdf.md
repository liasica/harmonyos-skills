---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf
title: 使用X963KDF进行密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥派生 > 使用X963KDF进行密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b091f0e2488480dd84f8ff74d6916acfc431ca0d7f7754c428c2b2dc214795d7
---

从API version 22开始，算法库支持使用该算法进行密钥派生操作。

对应的算法规格请查看[密钥派生算法规格：X963KDF](crypto-key-derivation-overview.md#x963kdf算法)。

## 开发步骤

1. 构造[X963KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#x963kdfspec22)对象，作为密钥派生参数进行密钥派生。

   X963KdfSpec是[KdfSpec](../harmonyos-references/js-apis-cryptoframework.md#kdfspec11)的子类，需要指定：

   * algName：指定算法'X963Kdf'。
   * key：原始密钥材料。

     如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。
   * info：可选的上下文与应用相关信息，可为空，用于拓展短密钥。
   * keySize：目标密钥的字节长度，需要为正整数。
2. 调用[cryptoFramework.createKdf](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekdf11)，指定字符串参数'X963KDF|SHA256'，创建密钥派生算法为X963KDF、HMAC函数摘要算法为SHA256的密钥派生函数对象（Kdf）。
3. 输入X963KdfSpec对象，调用[Kdf.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret11)进行密钥派生。

   Kdf.generateSecret的多种调用形式如表所示。

   | 接口名 | 返回方式 |
   | --- | --- |
   | generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void | callback异步生成。 |
   | generateSecret(params: KdfSpec): Promise<DataBlob> | Promise异步生成。 |
   | generateSecretSync(params: KdfSpec): DataBlob | 同步生成。 |

* 通过await返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function kdfAwait() {
  5. let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  6. let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  7. let spec: cryptoFramework.X963KdfSpec = {
  8. algName: 'X963KDF',
  9. key: keyData,
  10. info: infoData,
  11. keySize: 32
  12. };
  13. let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  14. let secret = await kdf.generateSecret(spec);
  15. console.info('key derivation output: ' + secret.data);
  16. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/X963KDFDerivation/entry/src/main/ets/pages/Await.ets#L16-L34)
* 通过Promise返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { buffer } from '@kit.ArkTS';

  5. function kdfPromise() {
  6. let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  7. let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  8. let spec: cryptoFramework.X963KdfSpec = {
  9. algName: 'X963KDF',
  10. key: keyData,
  11. info: infoData,
  12. keySize: 32
  13. };
  14. let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  15. let kdfPromise = kdf.generateSecret(spec);
  16. kdfPromise.then((secret) => {
  17. console.info('key derivation output: ' + secret.data);
  18. }).catch((error: BusinessError) => {
  19. console.error(`key derivation failed: errCode: ${error.code}, message: ${error.message}`);
  20. });
  21. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/X963KDFDerivation/entry/src/main/ets/pages/Promise.ets#L16-L40)
* 通过同步方式返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function kdfSync() {
  5. let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  6. let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  7. let spec: cryptoFramework.X963KdfSpec = {
  8. algName: 'X963KDF',
  9. key: keyData,
  10. info: infoData,
  11. keySize: 32
  12. };
  13. let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  14. let secret = kdf.generateSecretSync(spec);
  15. console.info('[Sync]key derivation output: ' + secret.data);
  16. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyDerivation/X963KDFDerivation/entry/src/main/ets/pages/Sync.ets#L15-L33)
