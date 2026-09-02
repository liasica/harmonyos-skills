---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-56
title: 使用24位的16进制字符串生成SM4算法密钥报错是什么原因
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 使用24位的16进制字符串生成SM4算法密钥报错是什么原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c02a40371710341ecd2abfe4f5d2246a17f839b6d7cb74d9bfbeafd5b2a0c1be
---

## 问题现象

在生成SM4算法密钥时，使用24位的16进制字符串进行转换生成报错，是什么原因？

```screen
async function sm4Key() {
  const symAlgName = 'SM4_128';
  const sKey: string = "3e8f1b2c9d5a7a6f0e4b2d8c";
  const symKeyData = buffer.from(sKey, 'hex');
  let symKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(symKeyData.buffer) };
  try {
    let aesGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
    let symKey = await aesGenerator.convertKey(symKeyBlob);
    console.info(`sm4密钥生成成功`);
  } catch (e) {
    console.error(`sm4密钥生成失败: e = ${e.code} ${e.message}`);
  }
}
```

## 背景知识

[SM4](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#sm4)：分组密码算法，分组长度为128位。

## 问题定位

1. 16进制字符为4bit。
2. 24位的16进制字符串为96bit。
3. SM4\_128算法规格对应的密钥长度为128bit，需要使用32位16进制字符串。

## 分析结论

由于SM4算法规格只有SM4\_128一种，需要使用32位16进制字符串作为密钥，而使用24位的16进制字符串导致密钥参数长度不够报错。

## 修改建议

将生成SM4\_128算法规格密钥的16进制字符串替换为32位字符长度。

```screen
import { buffer } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function sm4Key() {
  const symAlgName = 'SM4_128';
  const sKey: string = '3e8f1b2c9d5a7a6f0e4b2d8c7a1e4af5';
  const symKeyData = buffer.from(sKey, 'hex');
  let symKeyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(symKeyData.buffer) };
  try {
    let aesGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
    await aesGenerator.convertKey(symKeyBlob);
    console.info(`sm4密钥生成成功`);
  } catch (e) {
    console.error(`sm4密钥生成失败: e = ${e.code} ${e.message}`);
  }
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
          sm4Key();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

使用指定字符串或二进制数据进行生成密钥时，数据长度需要符合对应算法规格密钥长度标准。
