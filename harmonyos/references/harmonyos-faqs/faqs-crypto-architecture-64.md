---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-64
title: DES加密密文与其他端结果不一致问题如何解决
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > DES加密密文与其他端结果不一致问题如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:093029039acb83d6d3d180a07ad52812a0f90b9d1edc79f1575809dc1f299914
---

## 问题现象

使用ArkTS语言进行加解密操作与服务端加密结果不一致导致功能失败，如何修改ArkTS代码才能实现同样的加密结果？

DES目前支持分组模式为ECB/CBC/OFB/CFB，以下使用ECB/CBC分组模式使用错误来举例说明。

需要加密数据为1234，密钥为：MOBCB123，加密参数为：DES ECB PKCS7Padding；服务端加密结果为：dcc420f814a661c7；客户端加密结果为：OhGfo20IMls=。

## 背景知识

* [DES](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#des)：DES算法的加密过程由16轮相同的加密函数组成，每轮都使用不同的子密钥。子密钥是通过对原始密钥进行一系列的置换和移位操作生成的。在每一轮中，明文块被分为左右两部分，然后通过一系列的置换、替换和异或操作进行加密。
* [ParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#paramsspec)：加解密参数，适用于需要iv等参数的对称加解密模式。iv（Initialization Vector，初始化向量）是用于对称加密模式（如CBC/OFB/CFB）中引入随机性或唯一性的字节序列，保证相同明文在相同密钥下产生不同密文。
* ECB：无iv等参数的分组模式。

## 问题定位

1. 确认加解密流程：

   针对服务端与客户端加密结果不一致的问题，首先需要了解服务端使用什么语言与三方库，对特定的语言与三方库进行分析，确认加解密流程差异，如果使用了三方库或自定义加密流程则需要在ArkTS语言中复刻该流程。

   此处对于加解密流程不同不做详细说明，不同的三方库与服务端可能会根据自己的需求独特设计加密流程。例如：在生成密文后做逆序处理。

   以上例子中：服务端使用了java语言进行DES加密，并没有使用三方库进行加密，排除三方库对密文的特殊处理。
2. 确认编码格式：

   加解密过程中有三处编码格式需要进行检查服务端与客户端是否一致：密钥、原文、密文。

   以上例子中：针对加密结果进行分析，服务端加密结果为数字以及a-f字母构成，而客户端加密结果则含有=等特殊符号；根据编码规则分析，服务端对密文进行了16进制编码，而客户端则进行了base64编码。更改客户端编码为16进制编码后得出结果为：3a119fa36d08325b，与服务端结果依旧不同。
3. 确认加解密参数：

   DES加解密算法的参数分为：分组模式、密钥长度、填充模式。

   以上例子中：服务端使用的加密分组模式为CBC，与客户端使用的ECB模式不同导致加密结果不同。CBC分组模式需要添加偏移量进行加密，客户端添加偏移量MOBCB456后再次进行加密，结果为dcc420f814a661c7，与服务端结果一致。

## 分析结论

针对对称加解密，密钥参数、编码格式、加解密流程都一致才能保证加密结果一致。

以上例子中：客户端与服务端密文编码格式不同，且加密参数不同导致密文不一致。

## 修改建议

修改客户端编码模式与分组模式：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

// 加密消息。
function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('DES64|CBC|PKCS7');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, genIvParamsSpec());
  let encryptData = cipher.doFinalSync(plainText);
  return encryptData;
}

// 解密消息。
function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('DES64|CBC|PKCS7');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, genIvParamsSpec());
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symGenerator = cryptoFramework.createSymKeyGenerator('DES64');
  let symKey = symGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

// 生成偏移量
function genIvParamsSpec() {
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec',
    iv: { data: new Uint8Array(buffer.from('MOBCB456', 'utf-8').buffer) }
  };
  return ivParamsSpec;
}

function main() {
  let key = 'MOBCB123';
  let keyData = new Uint8Array(buffer.from(key, 'utf-8').buffer);
  let symKey = genSymKeyByData(keyData);
  let message = '1234';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptText = encryptMessage(symKey, plainText);
  console.info('encryptText: ', buffer.from(encryptText.data).toString('hex'));
  let decryptText = decryptMessage(symKey, encryptText);
  if (plainText.data.toString() === decryptText.data.toString()) {
    console.info('decrypt ok');
    console.info('decrypt plainText: ', buffer.from(decryptText.data).toString('utf-8'));
  } else {
    console.error('decrypt failed');
  }
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('DES加密')
        .onClick(() => {
          main();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
