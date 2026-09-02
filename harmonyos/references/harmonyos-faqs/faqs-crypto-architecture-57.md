---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-57
title: 如何指定密钥与偏移量实现DES加解密算法
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何指定密钥与偏移量实现DES加解密算法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:143653462e6179064a5335d6b94c4bda669e9d4bad12dc157a60782b1e88f706
---

## 问题现象

ArkTS语言可以实现DES加解密算法，如果想要实现指定编码格式下的密钥与偏移量，需要怎么去实现？

## 背景知识

* DES加解密算法：DES是一种分组加密算法，它将明文分成64位的块，然后对每个块进行加密操作。
* [DES](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#des)：算法库当前提供了DES加解密常用的4种加密模式：ECB、CBC、OFB和CFB。

## 解决方案

1. 定义编码函数方法。

   ```ts
   // GB2312转Uint8Array函数
   function gB2312Encode(gb2312Str: string): Uint8Array {
     let gbEncoder = new util.TextEncoder('gb2312');
     return gbEncoder.encodeInto(gb2312Str);
   }

   // Uint8Array转GB2312函数
   function gB2312Decode(gb2312Str: Uint8Array): string {
     let textDecoderOptions: util.TextDecoderOptions = {
       fatal: false,
       ignoreBOM: true
     };
     let gbDecoder = util.TextDecoder.create('gb2312', textDecoderOptions);
     return gbDecoder.decodeToString(gb2312Str);
   }
   ```
2. 定义一个生成iv值参数函数方法。

   ```ts
   // 生成偏移量
   function genIvParamsSpec(ivData: Uint8Array) {
     let ivParamsSpec: cryptoFramework.IvParamsSpec = {
       algName: 'IvParamsSpec', // CBC|CTR|OFB|CFB模式
       iv: { data: ivData }
     };
     return ivParamsSpec;
   }
   ```
3. 定义一个DES算法密钥生成函数方法。

   ```ts
   // 生成密钥
   function genSymKeyByData(symKeyData: Uint8Array) {
     let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
     let symGenerator = cryptoFramework.createSymKeyGenerator('DES64');
     let symKey = symGenerator.convertKeySync(symKeyBlob);
     console.info('convertKeySync success');
     return symKey;
   }
   ```
4. 定义一个DES加密消息函数方法。

   ```ts
   // 加密消息。
   function encryptMessage(symKey: cryptoFramework.SymKey, param: cryptoFramework.ParamsSpec,
     plainText: cryptoFramework.DataBlob) {
     let cipher = cryptoFramework.createCipher('DES64|CBC|PKCS5');
     cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, param);
     let encryptData = cipher.doFinalSync(plainText);
     return encryptData;
   }
   ```
5. 定义一个DES解密消息函数方法。

   ```ts
   // 解密消息。
   function decryptMessage(symKey: cryptoFramework.SymKey, param: cryptoFramework.ParamsSpec,
     cipherText: cryptoFramework.DataBlob) {
     let decoder = cryptoFramework.createCipher('DES64|CBC|PKCS5');
     decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, param);
     let decryptData = decoder.doFinalSync(cipherText);
     return decryptData;
   }
   ```

完整示例参考如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

// 生成密钥
function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symGenerator = cryptoFramework.createSymKeyGenerator('DES64');
  let symKey = symGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

// 生成偏移量
function genIvParamsSpec(ivData: Uint8Array) {
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec', // CBC|CTR|OFB|CFB模式
    iv: { data: ivData }
  };
  return ivParamsSpec;
}

// 加密消息。
function encryptMessage(symKey: cryptoFramework.SymKey, param: cryptoFramework.ParamsSpec,
  plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('DES64|CBC|PKCS5');
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, param);
  let encryptData = cipher.doFinalSync(plainText);
  return encryptData;
}

// 解密消息。
function decryptMessage(symKey: cryptoFramework.SymKey, param: cryptoFramework.ParamsSpec,
  cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('DES64|CBC|PKCS5');
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, param);
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

// GB2312转Uint8Array函数
function gB2312Encode(gb2312Str: string): Uint8Array {
  let gbEncoder = new util.TextEncoder('gb2312');
  return gbEncoder.encodeInto(gb2312Str);
}

// Uint8Array转GB2312函数
function gB2312Decode(gb2312Str: Uint8Array): string {
  let textDecoderOptions: util.TextDecoderOptions = {
    fatal: false,
    ignoreBOM: true
  };
  let gbDecoder = util.TextDecoder.create('gb2312', textDecoderOptions);
  return gbDecoder.decodeToString(gb2312Str);
}

function byteToHexString(byteArray: Uint8Array) {
  let hexString = '';
  for (let i = 0; i < byteArray.length; i++) {
    let byte = byteArray[i];
    // 将字节转换为十六进制字符串
    let hexByte = byte.toString(16);
    // 如果不足两位，则前面补零
    if (hexByte.length === 1) {
      hexByte = '0' + hexByte;
    }
    hexString += hexByte;
  }
  return hexString; // 通常十六进制字符串以大写形式表示
}

export function main() {
  try {
    let key = 'aaaabbbb';
    let iv = 'aaaabbbb';
    let message = '中文';

    let keyData = gB2312Encode(key);
    let ivData = gB2312Encode(iv);
    let symKey = genSymKeyByData(keyData);
    let ivParam = genIvParamsSpec(ivData);

    let plainText: cryptoFramework.DataBlob = { data: gB2312Encode(message) };

    let encryptText = encryptMessage(symKey, ivParam, plainText);
    console.info(`encrypt ok: ${byteToHexString(encryptText.data)}`);

    let decryptText = decryptMessage(symKey, ivParam, encryptText);
    if (plainText.data.toString() === decryptText.data.toString()) {
      console.info('decrypt plainText: ' + gB2312Decode(decryptText.data));
    } else {
      console.error('decrypt failed');
    }
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`DES. Code is ${err?.code}, message is ${err?.message}`);
  }
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('DES加解密')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          main();
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：DES算法从哪一个API版本开始支持？

A：DES算法从API20版本开始支持，想要实现DES算法进行加解密需要使用高于或等于API20版本的IDE开发工具。
