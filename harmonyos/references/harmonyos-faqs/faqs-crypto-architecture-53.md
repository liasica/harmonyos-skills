---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-53
title: 客户端公钥与服务端公钥不匹配问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 客户端公钥与服务端公钥不匹配问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e266de4585d76f010028b0a7c35984c415093c006c9fdc9b42f61698b87f5d9
---

## 问题现象

服务端java语言，API生成的ed25519和x25519公钥长度是32字节，而客户端的公钥getEncoded之后长度为44字节，两者不匹配，如何解决该问题？

问题代码如下：

```ts
// x25519密钥对
let keyGenX25519 = cryptoFramework.createAsyKeyGenerator('X25519');
let keyPairX25519 = keyGenX25519.generateKeyPairSync();
// Ed25519密钥对
let keyGenEd25519 = cryptoFramework.createAsyKeyGenerator('Ed25519');
let keyPairEd25519 = keyGenEd25519.generateKeyPairSync();
// ed25519对x25519的公钥进行签名
let publicKeyX25519: Uint8Array = keyPairX25519.pubKey.getEncoded().data
```

## 背景知识

[getEncoded()](../harmonyos-references/js-apis-cryptoframework.md#getencoded)方法返回编码后的公钥，类型是Uint8Array，其长度为44字节。

## 解决方案

使用[getAsyKeySpec](../harmonyos-references/js-apis-cryptoframework.md#getasykeyspec10)获取密钥参数，然后用[buffer.from](../harmonyos-references/js-apis-buffer.md#bufferfrom)根据密钥参数创建buffer对象，最后new Uint8Array()转换获取公钥。

代码如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Button('公钥长度')
        .onClick(() => {
          // x25519密钥对
          let keyGenX25519 = cryptoFramework.createAsyKeyGenerator('X25519');
          let keyPairX25519 = keyGenX25519.generateKeyPairSync();
          // Ed25519密钥对
          let keyGenEd25519 = cryptoFramework.createAsyKeyGenerator('Ed25519');
          let keyPairEd25519 = keyGenEd25519.generateKeyPairSync();
          // 转换32字节的公钥
          let dd = keyPairEd25519.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ED25519_PK_BN).toString(16); // 步骤一
          let cc = keyPairX25519.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.X25519_PK_BN).toString(16);
          let publicKeyEd25519: Uint8Array = new Uint8Array(buffer.from(dd, 'hex').buffer); // 步骤二
          let publicKeyX25519: Uint8Array = new Uint8Array(buffer.from(cc, 'hex').buffer);
          console.info('hm-->', publicKeyX25519.length, publicKeyEd25519.length);
        });
    }
    .height('80%')
  }
}
```

日志打印：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/USOh6HdpQIeccbvd6LoMgg/zh-cn_image_0000002628769116.png "点击放大")
