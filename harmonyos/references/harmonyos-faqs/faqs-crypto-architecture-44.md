---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-44
title: 如何使用DSA算法实现签名验签的功能
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用DSA算法实现签名验签的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:976e53574e9c172110d7df2022d5634ec589aece1834f03e57eea205910ea980
---

## 问题现象

想要使用DSA算法实现[签名验签](../harmonyos-guides/crypto-sign-sig-verify-overview.md)的功能，具体代码是怎样实现的呢？

## 背景知识

* [DSA](../harmonyos-guides/crypto-sign-sig-verify-overview.md#dsa)：DSA（Digital Signature Algorithm，数字签名算法）的安全性基于整数有限域离散对数问题的困难性，具有较好的兼容性和适用性。
* [createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10)：指定密钥参数，获取非对称密钥生成器实例。
* 签名验签：当需要判断接收的数据是否被篡改、数据是否为指定对象发送的数据时，可以使用签名验签操作。

## 解决方案

1. 配置DSA1024公钥和私钥中包含的公共参数dsaCommonSpec。
2. 设置DSA1024密钥对中包含的全参数。
3. 调用createAsyKeyGeneratorBySpec方法生成DSA算法的非对称密钥生成器。
4. 通过密钥生成器生成DSA非对称密钥对。
5. 使用DSA私钥对数据进行签名。
6. 使用DSA公钥对签名数据进行验签。

流程图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/qP9gRDfkTW-4DnuYGoSonQ/zh-cn_image_0000002658968429.png "点击放大")

完整示例参考如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('This is Sign test plan', 'utf-8').buffer) };

// 配置DSA1024公钥和私钥中包含的公共参数
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  };
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  };
  return dsaKeyPairSpec;
}

async function signMessagePromise(priKey: cryptoFramework.PriKey) {
  let signAlg = 'DSA3702|SHA256';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  let signData = await signer.sign(input);
  return signData;
}

async function verifyMessagePromise(signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'DSA3702|SHA256';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  let res = await verifier.verify(input, signMessageBlob);
  hilog.info(0x0000, 'test', 'DSA verify result is ' + res);
  return res;
}

function main() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE();
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  // 异步获取非对称密钥生成器生成的密钥
  asyKeyGeneratorBySpec.generateKeyPair(async (err, keyPair) => {
    if (err) {
      hilog.error(0x0000, 'test', 'generateKeyPair: error.');
      return;
    }
    hilog.info(0x0000, 'test', 'generateKeyPair: success.');
    // 签名
    let signData = await signMessagePromise(keyPair.priKey);
    // 验签
    let verifyResult = await verifyMessagePromise(signData, keyPair.pubKey);
    if (verifyResult === true) {
      hilog.info(0x0000, 'test', 'verify success');
    } else {
      hilog.error(0x0000, 'test', 'verify failed');
    }
  });
}

@Entry
@Component
struct DSA {
  build() {
    Column() {
      Button('点击进行验证')
        .fontSize(30)
        .onClick(() => {
          main();
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
