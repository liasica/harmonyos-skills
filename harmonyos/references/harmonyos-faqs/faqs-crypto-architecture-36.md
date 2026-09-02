---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-36
title: RSA如何使用现有的公私钥进行分段加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > RSA如何使用现有的公私钥进行分段加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a9259f3d3c8798b9b703e7f99e0a229f88821dce453e018832feb4ff22e79d2
---

## 问题现象

提供一个使用固定公私钥（字符串）进行RSA加解密的范例Demo。

## 背景知识

[使用RSA非对称密钥分段加解密](../harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment.md)，加密长度需要在固定长度进行，在实际应用中，数据量可能无法达到固定的长度要求，此时可以通过不同的填充模式进行数据填充。

## 解决方案

使用固定公私钥（字符串）进行RSA加解密整个过程Demo如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct Crypto {
  build() {
    Column() {
      Text('点击开始')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          rsaEncryptLongMessage();
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}

// 分段加密消息
function rsaEncryptBySegment(pubKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, pubKey, null);
  let plainTextSplitLen = 117; // 不高于加密位数/8-11 117
  let cipherText = new Uint8Array();
  for (let i = 0; i < plainText.data.length; i += plainTextSplitLen) {
    let updateMessage = plainText.data.subarray(i, i + plainTextSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 将原文按64字符进行拆分，循环调用doFinal进行加密，使用1024bit密钥时，每次加密生成128字节长度的密文
    let updateOutput = cipher.doFinalSync(updateMessageBlob);
    let mergeText = new Uint8Array(cipherText.length + updateOutput.data.length);
    mergeText.set(cipherText);
    mergeText.set(updateOutput.data, cipherText.length);
    cipherText = mergeText;
  }
  let cipherBlob: cryptoFramework.DataBlob = { data: cipherText };
  return cipherBlob;
}

// 分段解密消息
function rsaDecryptBySegment(priKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('RSA1024|PKCS1');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, priKey, null);
  let cipherTextSplitLen = 128; // RSA密钥每次加密生成的密文字节长度计算方式：密钥位数/8
  let decryptText = new Uint8Array();
  for (let i = 0; i < cipherText.data.length; i += cipherTextSplitLen) {
    let updateMessage = cipherText.data.subarray(i, i + cipherTextSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 将密文按128字节进行拆分解密，得到原文后进行拼接
    // 将原文按117字符进行拆分，循环调用doFinal进行加密，使用1024bit密钥时，每次加密生成128字节长度的密文
    let updateOutput = decoder.doFinalSync(updateMessageBlob);
    let mergeText = new Uint8Array(decryptText.length + updateOutput.data.length);
    mergeText.set(decryptText);
    mergeText.set(updateOutput.data, decryptText.length);
    decryptText = mergeText;
  }
  let decryptBlob: cryptoFramework.DataBlob = { data: decryptText };
  return decryptBlob;
}

function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_2');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKey success');
  return keyPair;
}

function rsaEncryptLongMessage() {
  let message = 'This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!';
  let base64 = new util.Base64Helper();

  let pkData =
    'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjSASCSzDPoXFq/6V5kXhhdH+gLaalmhZ+FNJZCx8Rr94po93Y85Icwwo2jQvnx8tRX0mof0Sk1GqgqSUHniXOJewu6KHDt8wZTnY8ncB3HJmPUa8Pct01MOmRZI3a31Rh6P8mZPI1iwZD/lxGkkyVo2MQDp/M4AwIy7n+QkGkfQIDAQAB';
  let skData =
    'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKNIBIJLMM+hcWr/pXmReGF0f6AtpqWaFn4U0lkLHxGv3imj3djzkhzDCjaNC+fHy1FfSah/RKTUaqCpJQeeJc4l7C7oocO3zBlOdjydwHccmY9Rrw9y3TUw6ZFkjdrfVGHo/yZk8jWLBkP+XEaSTJWjYxAOn8zgDAjLuf5CQaR9AgMBAAECgYABLlIqBxUxSz+gwHyX5n9yZP9PT0U3SWgEPW5QCo6M+DKpJnBCU3CpGJgIUPjXElDcI85Kk7ERaB/lTZPg/DnVwuaDoWO3utNkA9J5y1xIrJ+m32Op1WPQjYNTq8CDyVO0wqOsgXVMsbJaEezlNZed2gQ5CQQKLiIDuMznzla+gQJBANZHZMh+WX7RMBdeIHmWLRhg/nc9KVWYjSkD/d4S6HTBKASLdEDmSLT4NpVbEXtlpmaqV9wEaEY+QBjdkfMHaI0CQQDDEq4X2VvjCqjUiKeSTNXywxl48LLHC3A5pkl9vRYlt+ec7SLydseShP834DCBZIjRvqHs5UdXzvFOEQYaAIexAkBPc3FfFdpBN3dJctE/w/s8itpPhBILduEAUEaVTRV8FRKtfLfCSKC02UQD5Rx6UJp+frLNFaVERlil36H6JskRAkEAkVE4GZIVTmQhcvo+AtF0S/0k26BLPdX6iyeh9aZHel+ujYtmDkOH1lF3InPDDpELD1y4mZYPeI0z21j5N6OPcQJAdxnnEtw05TaX2DxbVhxPvEcwgpU/CpsrIC1eNe17Th68jAX4xVxTxSAUftECw8rBQ5C9vxGPbuPyvfk6MKkZ8A==';

  let pubKeyBlob = base64.decodeSync(pkData);
  let priKeyBlob = base64.decodeSync(skData);

  let keyPair = genKeyPairByData(pubKeyBlob, priKeyBlob);

  let plainText: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptText = rsaEncryptBySegment(keyPair.pubKey, plainText);

  let decryptText = rsaDecryptBySegment(keyPair.priKey, encryptText);
  console.info('decrypt plainText: ', buffer.from(decryptText.data).toString('utf-8'));
}
```

## 常见FAQ

Q：RSA加解密数据量较大时需要进行分段加解密，原因是什么？

A：非对称密钥的分段加密是指当明文大于单次加密支持的数据长度时（具体长度请查[非对称密钥加解密算法规格](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md)），需要将待加密数据分为合适长度的数据段，并对每个数据段执行加密操作，即创建Cipher，然后调用Cipher.init和Cipher.doFinal接口。

Q：RSA加解密数据量较大时需要进行分段加解密，这个数据量是多大？

A：严格意义上说，分段加解密是数据的拆分加解密，此时单次传入的数据量长度与密钥规格的长度相关。填充模式不同，输入的数据的规则不同，请根据[RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)算法规格确认单次传入的数据量长度。

Q：RSA加解密数据量较大时如果不使用分段签名，会有什么问题？

A：RSA加密和解密的速度相对较慢，尤其是在处理大量数据时，如果不进行分段处理，整个过程可能变得非常耗时，甚至在某些设备上可能因为处理时间过长而引起应用崩溃或挂载。RSA加密的数据大小是有限制的，通常不超过密钥长度（如1024位或2048位），尝试对超过这个限制的数据进行加密可能会导致内存溢出错误。

Q：为什么数据量较大时，需要分段进行签名验签？

A：当数据量较大时，需要分段进行签名验签的主要原因是提高效率和安全性。

* 对于大型文件或数据集，一次性读取和处理可能需要较大的内存空间，并且签名或验签操作可能需要更长的时间。通过分段处理，可以分散这些资源需求，使操作更加流畅和快速。
* 分段处理也可以提高安全性。如果一次性处理大量数据，任何在处理过程中发生的错误都可能导致整个数据集的安全性受损。分段处理可以减少每次处理的数据量，从而降低单一错误的影响。

Q：RSA分段加解密中偶现闪退失败do final fail，分段代码如下：

```ts
for (let i = 0; i < Math.ceil(encryptText.length / 64); i++) {
  console.info(encryptText.substring(0 + i * 64, 64 + i * 64))
  let plainTextBlob: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from(encryptText.substring(0 + i * 64, 64 + i * 64), 'utf-8').buffer) }
  let encryptBlob = cipher.doFinalSync(plainTextBlob);
  plainText = plainText + base64Helper.encodeToStringSync(encryptBlob.data);
}
```

A：分段方式错误，导致加密报错，使用subarray代替substring即可。
