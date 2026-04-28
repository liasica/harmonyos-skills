---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment
title: 使用RSA密钥对分段签名验签（PKCS1模式）(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签 > 签名验签开发指导 > 使用RSA密钥对分段签名验签（PKCS1模式）(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:14b7ca84b3958a3734bddcc557ad372b3ab921e815c47a3945d24bdcd8550b6b
---

对应的算法规格请查看[签名验签算法规格：RSA](crypto-sign-sig-verify-overview.md#rsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

   如何生成RSA非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'RSA1024|PKCS1|SHA256'，创建非对称密钥类型为RSA1024、填充模式为PKCS1、摘要算法为SHA256的Sign实例，用于完成签名操作。
3. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。
4. 将一次传入数据量设置为64字节，多次调用[Sign.update](../harmonyos-references/js-apis-cryptoframework.md#update-3)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
5. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'RSA1024|PKCS1|SHA256'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。
2. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。
3. 调用[Verify.update](../harmonyos-references/js-apis-cryptoframework.md#update-5)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
4. 调用[Verify.verify](../harmonyos-references/js-apis-cryptoframework.md#verify-1)，对数据进行验签。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function signMessageBySegment(priKey: cryptoFramework.PriKey, plainText: Uint8Array) {
  5. let signAlg = 'RSA1024|PKCS1|SHA256';
  6. let signer = cryptoFramework.createSign(signAlg);
  7. await signer.init(priKey);
  8. let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  9. for (let i = 0; i < plainText.length; i += textSplitLen) {
  10. let updateMessage = plainText.subarray(i, i + textSplitLen);
  11. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  12. // 分段update
  13. await signer.update(updateMessageBlob);
  14. }
  15. // 已通过分段传入所有明文，故此处sign传入null
  16. let signData = await signer.sign(null);
  17. return signData;
  18. }

  20. async function verifyMessageBySegment(pubKey: cryptoFramework.PubKey, plainText: Uint8Array,
  21. signMessageBlob: cryptoFramework.DataBlob) {
  22. let verifyAlg = 'RSA1024|PKCS1|SHA256';
  23. let verifier = cryptoFramework.createVerify(verifyAlg);
  24. await verifier.init(pubKey);
  25. let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  26. for (let i = 0; i < plainText.length; i += textSplitLen) {
  27. let updateMessage = plainText.subarray(i, i + textSplitLen);
  28. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  29. // 分段update
  30. await verifier.update(updateMessageBlob);
  31. }
  32. // 已通过分段传入所有明文，故此处verify第一个参数传入null
  33. let res = await verifier.verify(null, signMessageBlob);
  34. console.info('verify result: ' + res);
  35. return res;
  36. }

  38. async function rsaSignatureBySegment() {
  39. let message = 'This is a long plainText! This is a long plainText! This is a long plainText!' +
  40. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  41. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  42. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  43. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  44. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  45. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  46. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!';
  47. let keyGenAlg = 'RSA1024';
  48. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  49. let keyPair = await generator.generateKeyPair();
  50. let messageData = new Uint8Array(buffer.from(message, 'utf-8').buffer);
  51. let signData = await signMessageBySegment(keyPair.priKey, messageData);
  52. let verifyResult = await verifyMessageBySegment(keyPair.pubKey, messageData, signData);
  53. if (verifyResult === true) {
  54. console.info('verify result: success.');
  55. } else {
  56. console.error('verify result: failed.');
  57. }
  58. }
  ```

  [rsa\_pkcs1\_segment\_signature\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_segment_signature/rsa_pkcs1_segment_signature_asynchronous.ets#L16-L76)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function signMessageBySegment(priKey: cryptoFramework.PriKey, plainText: Uint8Array) {
  5. let signAlg = 'RSA1024|PKCS1|SHA256';
  6. let signer = cryptoFramework.createSign(signAlg);
  7. signer.initSync(priKey);
  8. let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  9. for (let i = 0; i < plainText.length; i += textSplitLen) {
  10. let updateMessage = plainText.subarray(i, i + textSplitLen);
  11. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  12. // 分段update
  13. signer.updateSync(updateMessageBlob);
  14. }
  15. // 已通过分段传入所有明文，故此处sign传入null
  16. let signData = signer.signSync(null);
  17. return signData;
  18. }

  20. function verifyMessageBySegment(pubKey: cryptoFramework.PubKey, plainText: Uint8Array,
  21. signMessageBlob: cryptoFramework.DataBlob) {
  22. let verifyAlg = 'RSA1024|PKCS1|SHA256';
  23. let verifier = cryptoFramework.createVerify(verifyAlg);
  24. verifier.initSync(pubKey);
  25. let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  26. for (let i = 0; i < plainText.length; i += textSplitLen) {
  27. let updateMessage = plainText.subarray(i, i + textSplitLen);
  28. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  29. // 分段update
  30. verifier.updateSync(updateMessageBlob);
  31. }
  32. // 已通过分段传入所有明文，故此处verify第一个参数传入null
  33. let res = verifier.verifySync(null, signMessageBlob);
  34. console.info('verify result: ' + res);
  35. return res;
  36. }

  38. function rsaSignatureBySegment() {
  39. let message = 'This is a long plainText! This is a long plainText! This is a long plainText!' +
  40. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  41. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  42. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  43. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  44. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  45. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
  46. 'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!';
  47. let keyGenAlg = 'RSA1024';
  48. let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  49. let keyPair = generator.generateKeyPairSync();
  50. let messageData = new Uint8Array(buffer.from(message, 'utf-8').buffer);
  51. let signData = signMessageBySegment(keyPair.priKey, messageData);
  52. let verifyResult = verifyMessageBySegment(keyPair.pubKey, messageData, signData);
  53. if (verifyResult === true) {
  54. console.info('verify result: success.');
  55. } else {
  56. console.error('verify result: failed.');
  57. }
  58. }
  ```

  [rsa\_pkcs1\_segment\_signature\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SignatureVerification/SigningSignatureVerificationArkTs/entry/src/main/ets/pages/rsa_pkcs1_segment_signature/rsa_pkcs1_segment_signature_synchronous.ets#L16-L76)
