---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-34
title: 使用OpenSSL创建的Ed25519签名验签报错
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 使用OpenSSL创建的Ed25519签名验签报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:e3c171dc8f8414aef9ae2723de331de0d25d64c0a9b664cbf679c365a8cd6edf
---

## 问题现象

使用OpenSSL创建的Ed25519密钥，然后使用HarmonyOS的方法生成密钥信息报错。

OpenSSL创建Ed25519密钥代码：

```shell
openssl genpkey -algorithm ED25519 -out ed25519-private.pem && openssl pkey -pubout -in ed25519-private.pem > ed25519-public.pem
```

OpenSSL创建的Ed25519密钥：

```ts
let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S'
let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA='
```

Ed25519密钥转换代码：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

// 转换密钥对
function genKeyPairByData() {
  let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S'
  let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA='

  try {
    let pubKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(pubKey, 'utf-8').buffer) };
    let priKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(priKey, 'utf-8').buffer) };
    let ed25519Generator = cryptoFramework.createAsyKeyGenerator('Ed25519');
    let keyPair = ed25519Generator.convertKeySync(pubKeyBlob, priKeyBlob);
    console.info('convertKey success');
    return keyPair;
  } catch (error) {
    console.error(`ECDSA ${error}, error code: ${error.code}`);
    return null;
  }
}
```

报错信息：

```txt
ECDSA Error: convert key fail., error code: 17630001
```

## 背景知识

* [Ed25519](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#ed25519)是基于EdDSA算法的数字签名算法，密钥长度为256位，采用Edwards曲线实现。该算法不支持加解密，主要用于数字签名和验证。
* 同步获取指定数据生成非对称密钥：[AsyKeyGenerator.convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12-1)。

## 问题定位

1. 根据[错误码17630001](../harmonyos-references/errorcode-crypto-framework.md#section17630001-密码操作错误)查询相关错误信息。
2. 由于方法并未使用第三方算法库，所以根据错误码信息可以得知是输入参数错误。
3. 根据OpenSSL创建的Ed25519密钥结果可以看出提供的公私钥数据为Base64格式。
4. 检查代码，可以发现在将公私钥数据转换为方法需要的Uint8Array类型数据时，使用的是new Uint8Array(buffer.from(pubKey, 'utf-8').buffer)，而此方法是将utf-8类型字符串转换为Uint8Array类型。
5. 可以确认Base64格式类型数据转换为Uint8Array类型数据方法使用错误。

## 分析结论

在将Base64格式类型的Ed25519公私钥数据转换成Uint8Array类型的Ed25519公私钥数据时，使用了错误的数据类型转换方法，没有成功转换为正确的Uint8Array类型的Ed25519公私钥数据，从而导致非对称密钥转换API时报错。

## 修改建议

使用正确的数据类型转换方法，将Base64格式类型的Ed25519公私钥数据转换成Uint8Array类型，然后使用AsyKeyGenerator.convertKeySync方法将Ed25519公私钥数据转换为Ed25519密钥对keyPair，即可进行签名验签。示例代码参考：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct KeyPair {
  genKeyPairByData() {
    let priKey = 'MC4CAQAwBQYDK2VwBCIEIPFypge0/4Q4Nj+g3rdkq1waRD/wmRetRJ4eUBT0D86S';
    let pubKey = 'MCowBQYDK2VwAyEADb/Cqqww74MVIcezIun9Mh1lbnx3cw9Qy9vYztWx2NA=';

    try {
      let pubKeyBlob: cryptoFramework.DataBlob = { data: this.base64ToUint8Array(pubKey) };
      let priKeyBlob: cryptoFramework.DataBlob = { data: this.base64ToUint8Array(priKey) };
      let ed25519Generator = cryptoFramework.createAsyKeyGenerator('Ed25519');
      let keyPair = ed25519Generator.convertKeySync(pubKeyBlob, priKeyBlob);
      console.info('convertKey success');
      return keyPair;
    } catch (error) {
      return null;
    }
  }

  // Base64转Uint8Array
  base64ToUint8Array(str: string): Uint8Array {
    let base64Helper = new util.Base64Helper();
    return base64Helper.decodeSync(str);
  }

  // 签名
  signMessagePromise(message: string, priKey: cryptoFramework.PriKey) {
    let signer = cryptoFramework.createSign('Ed25519');
    let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    signer.initSync(priKey);
    let signData = signer.signSync(input);
    return signData;
  }

  // 验签
  verifyMessagePromise(message: string, signMessageBlob: cryptoFramework.DataBlob, pubKey: cryptoFramework.PubKey) {
    let verifier = cryptoFramework.createVerify('Ed25519');
    let input: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
    verifier.initSync(pubKey);
    let res = verifier.verifySync(input, signMessageBlob);
    console.info(`verify result is ${res}`);
    return res;
  }

  build() {
    Column() {
      Button('点击签名验签')
        .fontSize(20)
        .padding(10)
        .onClick(() => {
          let message = 'this is a test data';
          let keypair = this.genKeyPairByData();
          if (keypair) {
            let signData = this.signMessagePromise(message, keypair.priKey);
            this.verifyMessagePromise(message, signData, keypair.pubKey);
          } else {
            console.info('convertKey failed');
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：如何根据服务端传入的公钥进行签名验签？

A：服务端仅传入公钥数据时，可通过[generatePubKeySync](../harmonyos-references/js-apis-cryptoframework.md#generatepubkeysync12)方法生成密钥对，签名验签方法与本文示例相同。

## 总结

不同的API方法需要使用不同的数据类型。在进行数据类型转换时，应根据原始数据类型和目标数据类型正确使用数据类型转换方法。
