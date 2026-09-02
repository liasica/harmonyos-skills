---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-kit-new-00002
title: 如何实现SM2签名与验签数据预处理
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何实现SM2签名与验签数据预处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:2a232ac2c34cf02206bd9feb37b86a13ecc449fb171793620fdaa0a2aaeec11a
---

## 问题现象

在HarmonyOS应用开发中，当需要对SM2签名数据进行预处理时，开发者需要按照国密算法标准计算预处理摘要。在Java等平台中，开发者需要手动获取SM2公钥的Z值，将其与SM3摘要拼接后参与运算。开发者需要了解HarmonyOS系统是否支持自动完成国密SM2签名预处理，以及如何在应用侧利用系统加解密能力实现SM2签名与验签流程。

## 背景知识

HarmonyOS提供了CryptoArchitectureKit（加密架构套件），支持SM2非对称加密和SM3摘要算法。在进行SM2签名与验签时，可以通过cryptoFramework模块创建签名和验签实例，并指定摘要算法为SM3。

国密SM2签名标准中，签名前需要对明文进行预处理：先根据签名者公钥计算Z值（由曲线参数、公钥坐标等按固定格式拼接而成），再将Z值与明文一起送入SM3摘要算法计算，最终得到预处理摘要e，最后对e执行SM2签名运算。在Java等平台中，这一Z值计算和拼接步骤需要开发者手动实现（如通过BouncyCastle等库获取sm3Z并手动拼接）。在HarmonyOS中，当指定签名算法为SM2\_256|SM3时，系统底层会自动完成国密标准的Z值计算和拼接预处理，开发者无需手动获取Z值或拼接SM3，只需将明文数据传入update或sign接口即可。

更多加解密开发指导可参考[SM2签名和验签](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#sm2)。

## 解决方案

使用CryptoArchitectureKit提供的cryptoFramework接口实现SM2签名与验签。密钥类型设置为SM2，摘要算法设置为SM3，系统会自动完成国密标准的Z值计算和拼接预处理。开发者只需通过update方法分段传入明文数据，最后调用sign或verify完成签名或验签操作，无需像Java那样手动获取Z值并拼接SM3。

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

// 完整的明文被拆分为input1和input2
let input1: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
let input2: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };

async function signMessagePromise(priKey: cryptoFramework.PriKey) {
  let signAlg = 'SM2_256|SM3';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  await signer.update(input1); // 如果明文较短，可以直接调用sign接口一次性传入
  let signData = await signer.sign(input2);
  return signData;
}

async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'SM2_256|SM3';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  await verifier.update(input1); // 如果明文较短，可以直接调用verify接口一次性传入
  let res = await verifier.verify(input2, signMessageBlob);
  console.info(`verify result = ${res}`);
  return res;
}

async function main() {
  try {
    let keyGenAlg = 'SM2_256';
    let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
    let keyPair = await generator.generateKeyPair();
    let signData = await signMessagePromise(keyPair.priKey);
    let verifyResult = await verifyMessagePromise(signData, keyPair.pubKey);
    if (verifyResult === true) {
      console.info('verify result: success.');
    } else {
      console.error('verify result: failed.');
    }
  } catch (err) {
    console.error(`Crypto operation failed: ${err}`);
  }
}
```
