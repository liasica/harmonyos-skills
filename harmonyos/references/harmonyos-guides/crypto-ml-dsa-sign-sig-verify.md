---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ml-dsa-sign-sig-verify
title: 使用ML-DSA密钥对签名验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签介绍及算法规格 > 使用ML-DSA密钥对签名验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ed85aa2ac8df082fbc8d2d26d8bed1e433969768c6c82bfa51f91a1b40d09393
---

从API版本26.0.0开始，签名验签支持ML-DSA算法。对应的算法规格请查看[签名验签算法规格：ML-DSA](crypto-sign-sig-verify-overview.md#ml-dsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成非对称密钥算法为ML-DSA的密钥对（KeyPair）。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'ML-DSA'，创建非对称密钥类型为ML-DSA的Sign实例，用于完成签名操作。
3. （可选）调用[Sign.setSignSpec](../harmonyos-references/js-apis-cryptoframework.md#setsignspec)，设置ML-DSA签名参数，如确定性签名（ML\_DSA\_DETERMINISTIC\_BOOL）、外部μ哈希模式（ML\_DSA\_MU\_BOOL）或上下文字符串（ML\_DSA\_CONTEXT\_UINT8ARR），当设置外部μ哈希模式（ML\_DSA\_MU\_BOOL）为true时，上下文字符串（ML\_DSA\_CONTEXT\_UINT8ARR）无效。
4. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。

   ML-DSA签名算法不支持update接口。
5. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'ML-DSA'，创建非对称密钥类型为ML-DSA的Verify实例，用于完成验签操作。
2. （可选）调用[Verify.setVerifySpec](../harmonyos-references/js-apis-cryptoframework.md#setverifyspec)，设置ML-DSA验签参数，如外部μ哈希模式（ML\_DSA\_MU\_BOOL）或上下文字符串（ML\_DSA\_CONTEXT\_UINT8ARR）。验签的参数应当与签名的参数保持一致，验签时无需设置确定性签名（ML\_DSA\_DETERMINISTIC\_BOOL）。
3. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。

   ML-DSA验签算法不支持update接口。
4. 调用[Verify.verify](../harmonyos-references/js-apis-cryptoframework.md#verify-1)，对数据进行验签。

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';
  import { BusinessError } from '@kit.BasicServicesKit';

  let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan', 'utf-8').buffer) };
  let context: Uint8Array = new Uint8Array(buffer.from('test', 'utf-8').buffer);

  async function signMessagePromise(priKey: cryptoFramework.PriKey) {
    let signer = cryptoFramework.createSign('ML-DSA');
    signer.setSignSpec(cryptoFramework.SignSpecItem.ML_DSA_DETERMINISTIC_BOOL, true);
    signer.setSignSpec(cryptoFramework.SignSpecItem.ML_DSA_CONTEXT_UINT8ARR, context);
    await signer.init(priKey);
    let signData = await signer.sign(input);
    return signData;
  }

  async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifier = cryptoFramework.createVerify('ML-DSA');
    verifier.setVerifySpec(cryptoFramework.SignSpecItem.ML_DSA_CONTEXT_UINT8ARR, context);
    await verifier.init(pubKey);
    let res = await verifier.verify(input, signMessageBlob);
    console.info('verify result: ' + res);
    return res;
  }

  async function main() {
    try {
      let generator = cryptoFramework.createAsyKeyGenerator('ML-DSA-87');
      let keyPair = await generator.generateKeyPair();
      let signData = await signMessagePromise(keyPair.priKey);
      let verifyResult = await verifyMessagePromise(signData, keyPair.pubKey);
      if (verifyResult === true) {
        console.info('verify result: success.');
        return 'Success';
      } else {
        console.error('verify result: failed.');
        return 'Fail';
      }
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`verify failed: errCode: ${e.code}, errMessage: ${e.message}`);
      return 'Fail';
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';
  import { BusinessError } from '@kit.BasicServicesKit';

  let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan', 'utf-8').buffer) };
  let context: Uint8Array = new Uint8Array(buffer.from('test', 'utf-8').buffer);

  function signMessageSync(priKey: cryptoFramework.PriKey) {
    let signer = cryptoFramework.createSign('ML-DSA');
    signer.setSignSpec(cryptoFramework.SignSpecItem.ML_DSA_DETERMINISTIC_BOOL, true);
    signer.setSignSpec(cryptoFramework.SignSpecItem.ML_DSA_CONTEXT_UINT8ARR, context);
    signer.initSync(priKey);
    let signData = signer.signSync(input);
    return signData;
  }

  function verifyMessageSync(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifier = cryptoFramework.createVerify('ML-DSA');
    verifier.setVerifySpec(cryptoFramework.SignSpecItem.ML_DSA_CONTEXT_UINT8ARR, context);
    verifier.initSync(pubKey);
    let res = verifier.verifySync(input, signMessageBlob);
    console.info('verify result: ' + res);
    return res;
  }

  function main() {
    try {
      let generator = cryptoFramework.createAsyKeyGenerator('ML-DSA-87');
      let keyPair = generator.generateKeyPairSync();
      let signData = signMessageSync(keyPair.priKey);
      let verifyResult = verifyMessageSync(signData, keyPair.pubKey);
      if (verifyResult === true) {
        console.info('verify result: success.');
        return 'Success';
      } else {
        console.error('verify result: failed.');
        return 'Fail';
      }
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`verify failed: errCode: ${e.code}, errMessage: ${e.message}`);
      return 'Fail';
    }
  }
  ```
