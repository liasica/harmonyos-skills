---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-agreement-using-dh
title: 使用DH进行密钥协商(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥协商 > 密钥协商开发指导 > 使用DH进行密钥协商(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50af95173d8f63bd242983356e03fd0cd303377aad741079e4701e81f54ca671
---

对应的算法规格请查看[密钥协商算法规格：DH](crypto-key-agreement-overview.md#dh)。

## 开发步骤

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)生成密钥算法为DH、采用知名安全素数群modp1536的非对称密钥（KeyPair）。

   如何生成DH非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：DH](crypto-asym-key-generation-conversion-spec.md#dh)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createKeyAgreement](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatekeyagreement)，指定字符串参数'DH\_modp1536'，创建密钥算法为DH、采用知名安全素数群modp1536的密钥协议生成器（KeyAgreement）。
3. 调用[KeyAgreement.generateSecret](../harmonyos-references/js-apis-cryptoframework.md#generatesecret-1)，基于传入的私钥（KeyPair.priKey）与公钥（KeyPair.pubKey）进行密钥协商，返回共享秘密。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function dhAwait() {
  4. let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
  5. // 随机生成公私钥对A
  6. let keyPairA = await keyGen.generateKeyPair();
  7. // 随机生成规格一致的公私钥对B
  8. let keyPairB = await keyGen.generateKeyPair();
  9. let keyAgreement = cryptoFramework.createKeyAgreement('DH_modp1536');
  10. // 使用A的公钥和B的私钥进行密钥协商
  11. let secret1 = await keyAgreement.generateSecret(keyPairB.priKey, keyPairA.pubKey);
  12. // 使用A的私钥和B的公钥进行密钥协商
  13. let secret2 = await keyAgreement.generateSecret(keyPairA.priKey, keyPairB.pubKey);
  14. // 两种协商的结果应当一致
  15. if (secret1.data.toString() === secret2.data.toString()) {
  16. console.info('DH result: success.');
  17. console.info('DH output: ' + secret1.data);
  18. } else {
  19. console.error('DH result is not equal.');
  20. }
  21. }
  ```

  [DHAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/DH/DHAsync.ets#L15-L37)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. function dhAwait() {
  4. let keyGen = cryptoFramework.createAsyKeyGenerator('DH_modp1536');
  5. // 随机生成公私钥对A
  6. let keyPairA = keyGen.generateKeyPairSync();
  7. // 随机生成规格一致的公私钥对B
  8. let keyPairB = keyGen.generateKeyPairSync();
  9. let keyAgreement = cryptoFramework.createKeyAgreement('DH_modp1536');
  10. // 使用A的公钥和B的私钥进行密钥协商
  11. let secret1 = keyAgreement.generateSecretSync(keyPairB.priKey, keyPairA.pubKey);
  12. // 使用A的私钥和B的公钥进行密钥协商
  13. let secret2 = keyAgreement.generateSecretSync(keyPairA.priKey, keyPairB.pubKey);
  14. // 两种协商的结果应当一致
  15. if (secret1.data.toString() === secret2.data.toString()) {
  16. console.info('DH result: success.');
  17. console.info('DH output: ' + secret1.data);
  18. } else {
  19. console.error('DH result is not equal.');
  20. }
  21. }
  ```

  [DHSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyNegotiation/entry/src/main/ets/pages/DH/DHSync.ets#L17-L39)
