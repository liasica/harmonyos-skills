---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-ecdsa-sign-sig-verify
title: 使用ECDSA密钥对签名验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签介绍及算法规格 > 使用ECDSA密钥对签名验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:16baaacd0bb7e671e33e294d857cf4f88b15c99d114f01a0c08c6f3b52b94c05
---

对应的算法规格请查看[签名验签算法规格：ECDSA](crypto-sign-sig-verify-overview.md#ecdsa)。

**签名**

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)、[AsyKeyGenerator.generateKeyPair](../harmonyos-references/js-apis-cryptoframework.md#generatekeypair-1)，生成非对称密钥算法为ECC、密钥长度为256位的密钥对（KeyPair）。

   如何生成ECC非对称密钥，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：ECC](crypto-key-generation-conversion.md#ecc)和[随机生成非对称密钥对](crypto-generate-asym-key-pair-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createSign](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)，指定字符串参数'ECC256|SHA256'，创建非对称密钥类型为ECC256、摘要算法为SHA256的Sign实例，用于完成签名操作。
3. 调用[Sign.init](../harmonyos-references/js-apis-cryptoframework.md#init-3)，使用私钥（PriKey）初始化Sign实例。
4. 调用[Sign.update](../harmonyos-references/js-apis-cryptoframework.md#update-3)，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
5. 调用[Sign.sign](../harmonyos-references/js-apis-cryptoframework.md#sign-1)，生成数据签名。

**验签**

1. 调用[cryptoFramework.createVerify](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateverify)，指定字符串参数'ECC256|SHA256'，创建非对称密钥类型为ECC256、摘要算法为SHA256的Verify实例，用于完成验签操作。
2. 调用[Verify.init](../harmonyos-references/js-apis-cryptoframework.md#init-5)，使用公钥（PubKey）初始化Verify实例。
3. 调用[Verify.update](../harmonyos-references/js-apis-cryptoframework.md#update-5)，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
4. 调用[Verify.verify](../harmonyos-references/js-apis-cryptoframework.md#verify-1)，对数据进行验签。

* 异步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  // 完整的明文被拆分为input1和input2
  let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };

  async function signMessagePromise(priKey: cryptoFramework.PriKey) {
    let signAlg = 'ECC256|SHA256';
    let signer = cryptoFramework.createSign(signAlg);
    await signer.init(priKey);
    await signer.update(input1); // 如果明文较短，可以直接调用sign接口一次性传入
    let signData = await signer.sign(input2);
    return signData;
  }

  async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifyAlg = 'ECC256|SHA256';
    let verifier = cryptoFramework.createVerify(verifyAlg);
    await verifier.init(pubKey);
    await verifier.update(input1); // 如果明文较短，可以直接调用verify接口一次性传入
    let res = await verifier.verify(input2, signMessageBlob);
    console.info('verify result: ' + res);
    return res;
  }

  async function main() {
    let keyGenAlg = 'ECC256';
    let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
    let keyPair = await generator.generateKeyPair();
    let signData = await signMessagePromise(keyPair.priKey);
    let verifyResult = await verifyMessagePromise(signData, keyPair.pubKey);
    if (verifyResult === true) {
      console.info('verify result: success.');
    } else {
      console.error('verify result: failed.');
    }
  }
  ```
* 同步方法示例：

  ```typescript
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  // 完整的明文被拆分为input1和input2
  let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };

  function signMessageSync(priKey: cryptoFramework.PriKey) {
    let signAlg = 'ECC256|SHA256';
    let signer = cryptoFramework.createSign(signAlg);
    signer.initSync(priKey);
    signer.updateSync(input1); // 如果明文较短，可以直接调用sign接口一次性传入
    let signData = signer.signSync(input2);
    return signData;
  }

  function verifyMessageSync(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifyAlg = 'ECC256|SHA256';
    let verifier = cryptoFramework.createVerify(verifyAlg);
    verifier.initSync(pubKey);
    verifier.updateSync(input1); // 如果明文较短，可以直接调用verify接口一次性传入
    let res = verifier.verifySync(input2, signMessageBlob);
    console.info('verify result: ' + res);
    return res;
  }

  function main() {
    let keyGenAlg = 'ECC256';
    let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
    let keyPair = generator.generateKeyPairSync();
    let signData = signMessageSync(keyPair.priKey);
    let verifyResult = verifyMessageSync(signData, keyPair.pubKey);
    if (verifyResult === true) {
      console.info('verify result: success.');
    } else {
      console.error('verify result: failed.');
    }
  }
  ```
