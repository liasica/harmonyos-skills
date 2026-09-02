---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-51
title: 如何生成DH密钥
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何生成DH密钥
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:560accbfa8b57a53d52dd6c5e8a90b45840ea11b9a02cd662cfb444acd2ec525
---

## 问题现象

如何生成DH密钥，需要有实现生成DH密钥的具体流程和代码示例。

## 背景知识

* DH算法介绍：[DH](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#dh)（Diffie–Hellman key exchange），是一种密钥协商算法，只涉及公钥的交换，它可以提供前向安全性，即使在通信渠道被监听的情况下，也不会暴露双方的私钥。当前支持使用字符串参数和密钥参数两种方式生成DH密钥，且支持根据素数长度和私钥长度生成公共密钥参数。

* DH算法规格介绍：
  + 场景一：[使用字符串参数生成](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#使用字符串参数生成-6)。
  + 场景二：[使用密钥参数生成](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#使用密钥参数生成-6)。
* DH算法相关接口介绍。

  | 名称 | 接口 |
  | --- | --- |
  | 指定DH算法公共参数。 | [DHCommonParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#dhcommonparamsspec11) |
  | 指定DH算法私钥参数。 | [DHPriKeySpec](../harmonyos-references/js-apis-cryptoframework.md#dhprikeyspec11) |
  | 指定DH算法公钥参数。 | [DHPubKeySpec](../harmonyos-references/js-apis-cryptoframework.md#dhpubkeyspec11) |
  | 指定DH算法全量参数。 | [DHKeyPairSpec](../harmonyos-references/js-apis-cryptoframework.md#dhkeypairspec11) |
  | 通过指定密钥参数，创建非对称密钥生成器。 | [createAsyKeyGeneratorBySpec](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygeneratorbyspec10) |
  | 通过指定算法名称的字符串，创建非对称密钥生成器。 | [createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator) |

## 解决方案

* 场景一：调用createAsyKeyGenerator接口通过DH字符串参数生成DH密钥对.

  ```ts
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  // 使用字符串参数生成DH密钥对
  export function getDHKeyFromStringParams() {
    try {
      // 1、生成密钥对
      let spec = cryptoFramework.createAsyKeyGenerator('DH_modp2048');
      let pubKey = spec.generateKeyPairSync().pubKey.getEncoded().data;
      let priKey = spec.generateKeyPairSync().priKey.getEncoded().data;
      console.info(`getDHKeyFromStringparams success, DH public key = ${pubKey.toString()}`);
      console.info(`getDHKeyFromStringparams success, DH priKey key = ${priKey.toString()}`);
    } catch (error) {
      console.error(`failed`);
    }
  }
  ```
* 场景二：使用密钥参数生成DH密钥。
  1. 调用DHCommonParamsSpec接口通过p、g、l参数生成密钥公共参数DHCommonParamsSpec。
  2. 调用DHKeyPairSpec接口通过私钥参数、公钥参数和公共参数生成DH密钥参数DHKeyPairSpec。
  3. 调用createAsyKeyGeneratorBySpec接口通过DH密钥参数生成DH密钥对。

     ```ts
     // 使用密钥参数生成DH密钥对
     export function getDHKeyFromParams() {
       try {
         // 1、生成公共参数
         let dHCommonParamsSpec: cryptoFramework.DHCommonParamsSpec = {
           // 参数仅用于示例，按照实际填写
           p: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
           g: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34'),
           l: 192,
           algName: 'DH',
           specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
         };
         // 2、生成密钥对参数
         let dHKeyPairSpec: cryptoFramework.DHKeyPairSpec = {
           // 参数仅用于示例，按照实际填写
           sk: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
           pk: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
           params: dHCommonParamsSpec,
           algName: 'DH',
           specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC
         };
         // 3、生成密钥对
         let spec = cryptoFramework.createAsyKeyGeneratorBySpec(dHKeyPairSpec);
         let pubKey = spec.generateKeyPairSync().pubKey.getEncoded().data;
         let priKey = spec.generateKeyPairSync().priKey.getEncoded().data;
         console.info(`getDHKeyFromparams success, DH public key = ${pubKey.toString()}`);
         console.info(`getDHKeyFromparams success, DH priKey key = ${priKey.toString()}`);
       } catch (error) {
         console.error(`getDHKeyFromparams failed`);
       }
     }
     ```

  完整示例参考如下：

  ```ts
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  // 使用字符串参数生成DH密钥对
  export function getDHKeyFromStringParams() {
    try {
      // 1、生成密钥对
      let spec = cryptoFramework.createAsyKeyGenerator('DH_modp2048');
      let pubKey = spec.generateKeyPairSync().pubKey.getEncoded().data;
      let priKey = spec.generateKeyPairSync().priKey.getEncoded().data;
      console.info(`getDHKeyFromStringparams success, DH public key = ${pubKey.toString()}`);
      console.info(`getDHKeyFromStringparams success, DH priKey key = ${priKey.toString()}`);
    } catch (error) {
      console.error(`failed`);
    }
  }

  // 使用密钥参数生成DH密钥对
  export function getDHKeyFromParams() {
    try {
      // 1、生成公共参数
      let dHCommonParamsSpec: cryptoFramework.DHCommonParamsSpec = {
        // 参数仅用于示例，按照实际填写
        p: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
        g: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34'),
        l: 192,
        algName: 'DH',
        specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC
      };
      // 2、生成密钥对参数
      let dHKeyPairSpec: cryptoFramework.DHKeyPairSpec = {
        // 参数仅用于示例，按照实际填写
        sk: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
        pk: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
        params: dHCommonParamsSpec,
        algName: 'DH',
        specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC
      };
      // 3、生成密钥对
      let spec = cryptoFramework.createAsyKeyGeneratorBySpec(dHKeyPairSpec);
      let pubKey = spec.generateKeyPairSync().pubKey.getEncoded().data;
      let priKey = spec.generateKeyPairSync().priKey.getEncoded().data;
      console.info(`getDHKeyFromparams success, DH public key = ${pubKey.toString()}`);
      console.info(`getDHKeyFromparams success, DH priKey key = ${priKey.toString()}`);
    } catch (error) {
      console.error(`getDHKeyFromparams failed`);
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
            getDHKeyFromStringParams();
            getDHKeyFromParams();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 常见FAQ

Q： 使用密钥参数生成DH密钥对参数l有限制吗？

A： 私钥长度l为可选参数，默认为0，l值的设置范围需大于2\*(96+(素数P位数-1)/1024\*16)。

Q： 使用密钥参数生成DH密钥对参数p有限制吗？

A： 素数p的比特长度必须大于等于512，小于等于10000。

## 总结

DH算法生成密钥可以通过使用字符串参数和使用密钥参数两种方式生成。
