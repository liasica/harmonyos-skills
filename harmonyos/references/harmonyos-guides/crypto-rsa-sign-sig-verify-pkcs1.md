---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1
title: 使用RSA密钥对（PKCS1模式）签名验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用RSA密钥对（PKCS1模式）签名验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fbac8171dcdf9a4674b22fef7c6b8ec7478e716c7d3150dcc98d64ef312d96c3
---

对应的算法规格请查看[签名验签算法规格：RSA](crypto-sign-sig-verify-overview.md#rsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

   如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'RSA1024|PKCS1|SHA256'，创建非对称密钥类型为RSA1024、填充模式为PKCS1、摘要算法为SHA256的Sign实例，用于完成签名操作。
3. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。
4. 调用[Sign.update](../harmonyos-references/js-apis-cryptoframework.md#update-3)，传入待签名的数据。

   当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

   * 当待签名的数据较短时，可以在init完成后直接调用sign。
   * 当数据量较大时，可以多次调用update，即[分段签名验签](crypto-rsa-sign-sig-verify-pkcs1-by-segment.md)。
5. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'RSA1024|PKCS1|SHA256'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。
2. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。
3. 调用[Verify.update](../harmonyos-references/js-apis-cryptoframework.md#update-5)，传入待验证的数据。

   当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

   * 当待签名的数据较短时，可以在init完成后直接调用verify。
   * 当数据量较大时，可以多次调用update，即[分段签名验签](crypto-rsa-sign-sig-verify-pkcs1-by-segment.md)。
4. 调用[Verify.verify](../harmonyos-references/js-apis-cryptoframework.md#verify-1)，对数据进行验签。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 完整的明文被拆分为input1和input2
  5. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  6. let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };

  8. async function signMessagePromise(priKey: cryptoFramework.PriKey) {
  9. let signAlg = 'RSA1024|PKCS1|SHA256';
  10. let signer = cryptoFramework.createSign(signAlg);
  11. await signer.init(priKey);
  12. await signer.update(input1); // 如果明文较短，可以直接调用sign接口一次性传入
  13. let signData = await signer.sign(input2);
  14. return signData;
  15. }

  17. async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  18. let verifyAlg = 'RSA1024|PKCS1|SHA256';
  19. let verifier = cryptoFramework.createVerify(verifyAlg);
  20. await verifier.init(pubKey);
  21. await verifier.update(input1); // 如果明文较短，可以直接调用verify接口一次性传入
  22. let res = await verifier.verify(input2, signMessageBlob);
  23. console.info('verify result: ' + res);
  24. return res;
  25. }

  27. async function main() {
  28. let keyGenAlg = 'RSA1024';
  29. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  30. let keyPair = await generator.generateKeyPair();
  31. let signData = await signMessagePromise(keyPair.priKey);
  32. let verifyResult = await verifyMessagePromise(signData, keyPair.pubKey);
  33. if (verifyResult === true) {
  34. console.info('verify result: success.');
  35. } else {
  36. console.error('verify result: failed.');
  37. }
  38. }
  ```

  [rsa\_pkcs1\_signature\_validator\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_signature_validator/rsa_pkcs1_signature_validator_asynchronous.ets#L16-L55)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. // 完整的明文被拆分为input1和input2
  5. let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  6. let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };

  8. function signMessagePromise(priKey: cryptoFramework.PriKey) {
  9. let signAlg = 'RSA1024|PKCS1|SHA256';
  10. let signer = cryptoFramework.createSign(signAlg);
  11. signer.initSync(priKey);
  12. signer.updateSync(input1); // 如果明文较短，可以直接调用sign接口一次性传入
  13. let signData = signer.signSync(input2);
  14. return signData;
  15. }

  17. function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  18. let verifyAlg = 'RSA1024|PKCS1|SHA256';
  19. let verifier = cryptoFramework.createVerify(verifyAlg);
  20. verifier.initSync(pubKey);
  21. verifier.updateSync(input1); // 如果明文较短，可以直接调用verify接口一次性传入
  22. let res = verifier.verifySync(input2, signMessageBlob);
  23. console.info('verify result: ' + res);
  24. return res;
  25. }

  27. function main() {
  28. let keyGenAlg = 'RSA1024';
  29. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  30. let keyPair = generator.generateKeyPairSync();
  31. let signData = signMessagePromise(keyPair.priKey);
  32. let verifyResult = verifyMessagePromise(signData, keyPair.pubKey);
  33. if (verifyResult === true) {
  34. console.info('verify result: success.');
  35. } else {
  36. console.error('verify result: failed.');
  37. }
  38. }
  ```

  [rsa\_pkcs1\_signature\_validator\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_signature_validator/rsa_pkcs1_signature_validator_synchronous.ets#L16-L55)
