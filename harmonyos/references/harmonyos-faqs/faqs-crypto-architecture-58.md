---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-58
title: ECC密钥如何转化为非压缩十六进制字符串
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > ECC密钥如何转化为非压缩十六进制字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4255c94cf840e1d316ee2da5eec97027b98c984e4f9323d4a27561b22b28f65d
---

## 问题现象

其他端生成的ECC的公钥字符串长度为65字节（130位16进制字符串），ArkTS中使用generateKeyPairSync生成的KeyPair里面的公钥二进制数据长度远多于65字节，如何通过KeyPair获取非压缩16进制的公私钥字符串？

## 背景知识

[使用ECC压缩/非压缩点格式转换(ArkTS)](../harmonyos-guides/crypto-convert-compressed-or-uncompressed-ecc-point.md)：支持将压缩/非压缩的点数据转换为Point对象，用于密钥对象生成；也支持将Point对象转换为压缩/非压缩的点数据。

服务端使用的是非压缩16进制私钥和公钥，需要提取参数转化成非压缩私钥公钥与服务端交互。

* ECC公钥长度一般为65字节，其中前导04是固定的，代表非压缩格式。
* 32个字节的私钥在某些情况下被省略了前导的零，需要手动在前面补上0才能构成完整的私钥。

## 解决方案

通过密钥获取密钥参数X和Y合成非压缩公钥，获取SK参数转化成私钥。SM2也是基于椭圆曲线的公钥密码算法，公钥结构与ECC相同，是ECC算法的一种具体实现，demo以SM2算法为例。

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// Uint8Array to hexadecimal
function uint8ArrayToHexStr(data: Uint8Array): string {
  let hexString = '';
  let i: number;
  for (i = 0; i < data.length; i++) {
    let char = ('00' + data[i].toString(16)).slice(-2);
    hexString += char;
  }
  return hexString;
}

function padding(data: string): string {
  while (data.length < 64) {
    data = '0' + data;
  }
  return data;
}

function gen() {
  let keypairGenerator = cryptoFramework.createAsyKeyGenerator('SM2_256');
  let keyPair = keypairGenerator.generateKeyPairSync();
  let oldPk = uint8ArrayToHexStr(keyPair.pubKey.getEncoded().data);
  let oldSk = uint8ArrayToHexStr(keyPair.priKey.getEncoded().data);
  console.info(`SM2 oldPk.len = ${oldPk.length}`);
  console.info(`SM2 oldSk.len = ${oldSk.length}`);

  let x = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  let y = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
  let pk = '04' + padding(x.toString(16)) + padding(y.toString(16));
  console.info(`pk.len=${pk.length},pk:${pk}`);

  let priKey = keyPair.priKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_SK_BN);
  let sk = padding(priKey.toString(16));
  console.info(`sk.len=${sk.length},sk:${sk}`);
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text('Hello World')
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          gen();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
