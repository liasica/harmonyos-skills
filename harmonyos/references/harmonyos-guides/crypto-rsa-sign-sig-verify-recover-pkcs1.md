---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-recover-pkcs1
title: 使用RSA密钥对（PKCS1模式）签名及签名恢复(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用RSA密钥对（PKCS1模式）签名及签名恢复(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d618d30c93f65cebdaba4723e80a2f1185cff577cb8f8bf6a3b5148b629e1e1b
---

对应的算法规格请查看[签名验签算法规格：RSA](crypto-sign-sig-verify-overview.md#rsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

   如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'RSA1024|PKCS1|SHA256|SignOnly'，创建非对称密钥类型为RSA1024、填充模式为PKCS1、摘要算法为SHA256的Sign实例，用于完成仅签名操作。
3. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。
4. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'RSA1024|PKCS1|SHA256|Recover'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。
2. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。
3. 调用[Verify.recover](../harmonyos-references/js-apis-cryptoframework.md#recover12)，对数据进行签名恢复。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 完整的明文被拆分为input1和input2
  5. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };

  7. async function signMessagePromise(priKey: cryptoFramework.PriKey) {
  8. let signAlg = 'RSA1024|PKCS1|NoHash|OnlySign';
  9. let signer = cryptoFramework.createSign(signAlg);
  10. await signer.init(priKey);
  11. let signData = await signer.sign(input1);
  12. return signData;
  13. }

  15. async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  16. let verifyAlg = 'RSA1024|PKCS1|NoHash|Recover';
  17. let verifier = cryptoFramework.createVerify(verifyAlg);
  18. await verifier.init(pubKey);
  19. let rawSignData = await verifier.recover(signMessageBlob);
  20. return rawSignData;
  21. }

  23. async function main() {
  24. let keyGenAlg = 'RSA1024';
  25. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  26. let keyPair = await generator.generateKeyPair();
  27. let signData = await signMessagePromise(keyPair.priKey);
  28. let rawSignData = await verifyMessagePromise(signData, keyPair.pubKey);
  29. if (rawSignData != null) {
  30. console.info('recover result: ' + rawSignData.data);
  31. } else {
  32. console.error('get verify recover result: fail!');
  33. }
  34. }
  ```

  [rsa\_pkcs1\_signature\_restoration\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_signature_restoration/rsa_pkcs1_signature_restoration_asynchronous.ets#L16-L51)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 完整的明文被拆分为input1和input2
  5. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };

  7. function signMessagePromise(priKey: cryptoFramework.PriKey) {
  8. let signAlg = 'RSA1024|PKCS1|NoHash|OnlySign';
  9. let signer = cryptoFramework.createSign(signAlg);
  10. signer.initSync(priKey);
  11. let signData = signer.signSync(input1);
  12. return signData;
  13. }

  15. function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  16. let verifyAlg = 'RSA1024|PKCS1|NoHash|Recover';
  17. let verifier = cryptoFramework.createVerify(verifyAlg);
  18. verifier.initSync(pubKey);
  19. let rawSignData = verifier.recoverSync(signMessageBlob);
  20. return rawSignData;
  21. }

  23. function main() {
  24. let keyGenAlg = 'RSA1024';
  25. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  26. let keyPair = generator.generateKeyPairSync();
  27. let signData = signMessagePromise(keyPair.priKey);
  28. let rawSignData = verifyMessagePromise(signData, keyPair.pubKey);
  29. if (rawSignData != null) {
  30. console.info('recover result: ' + rawSignData.data);
  31. } else {
  32. console.error('get verify recover result: fail!');
  33. }
  34. }
  ```

  [rsa\_pkcs1\_signature\_restoration\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_signature_restoration/rsa_pkcs1_signature_restoration_synchronous.ets#L16-L51)
