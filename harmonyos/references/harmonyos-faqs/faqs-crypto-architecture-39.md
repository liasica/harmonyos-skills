---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-39
title: AES加解密CBC模式解密失败
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > AES加解密CBC模式解密失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a10dfd707b4fb42f7f50c1d4927016a824a023365efdd9ae03378ee020837267
---

## 问题现象

使用AES加解密算法CBC模式进行解密，密文解密后的明文前一部分出现乱码，后一部分成功解密。

## 背景知识

AES加解密为常见的对称加解密算法，AES加解密相关信息可以参考以下链接文档：

* [AES密钥规格](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)。
* [随机生成AES密钥](../harmonyos-guides/crypto-generate-sym-key-randomly.md#随机生成aes密钥)。
* [AES加解密算法规格](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#aes)。
* [AES对称密钥（CBC模式）加解密](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-cbc.md)。

## 问题定位

1. 检查文本编码格式是否是UTF-8格式，不是则修改为UTF-8格式。
2. 检查密文是否经过移位、替换等操作，是则进行对应反向操作。
3. 检查iv值生成方式。
4. 检查加密和解密时的iv值是否一致，不一致则修改为一致。

   ```ets
   // 生成随机iv
   function genRandomIv() {
     let rand = cryptoFramework.createRandom();
     let ivBlob = rand.generateRandomSync(16);
     let ivParamsSpec: cryptoFramework.IvParamsSpec = {
       algName: "IvParamsSpec",
       iv: ivBlob
     };
     return ivParamsSpec;
   }

   // 加密消息
   function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
     let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
     let iv = genRandomIv();
     // 加密初始化
     cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
     let cipherData = cipher.doFinalSync(plainText);
     return cipherData;
   }

   // 解密消息
   function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
     let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
     let iv = genRandomIv();
     // 解密初始化
     let decryptData: cryptoFramework.DataBlob = cipherText;
     decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
     try {
       decryptData = decoder.doFinalSync(cipherText);
     } catch (error) {
       console.error('doFinalSync fail');
     }
     return decryptData;
   }
   ```

## 分析结论

AES加解密算法CBC模式需要有偏移向量iv值，由于加密和解密时各自生成了iv值，使得使用的偏移向量iv值不一致，导致密文解密后的明文前一部分出现乱码，后一部分成功解密。

## 修改建议

将AES加密和解密的偏移向量iv值修改一致后问题解决，使用安全随机数生成方法生成一次iv，加密与解密共用此iv值。

```ets
// 加密消息
function encryptMessageNew(symKey: cryptoFramework.SymKey, iv: cryptoFramework.IvParamsSpec,
  plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  // 加密初始化
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  let cipherData = cipher.doFinalSync(plainText);
  return cipherData;
}

// 解密消息
function decryptMessageNew(symKey: cryptoFramework.SymKey, iv: cryptoFramework.IvParamsSpec,
  cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  // 解密初始化
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}
```

完整代码如下：

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer, util } from '@kit.ArkTS';

// 生成密钥
function genSymKeyByData(symKeyData: Uint8Array) {
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = symGenerator.convertKeySync(symKeyBlob);
  console.info('convertKeySync success');
  return symKey;
}

// 生成随机iv
function genRandomIv() {
  let rand = cryptoFramework.createRandom();
  let ivBlob = rand.generateRandomSync(16);
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: "IvParamsSpec",
    iv: ivBlob
  };
  return ivParamsSpec;
}

// 加密消息
function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  let iv = genRandomIv();
  // 加密初始化
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  let cipherData = cipher.doFinalSync(plainText);
  return cipherData;
}

// 解密消息
function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  let iv = genRandomIv();
  // 解密初始化
  let decryptData: cryptoFramework.DataBlob = cipherText;
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  try {
    decryptData = decoder.doFinalSync(cipherText);
  } catch (error) {
    console.error('doFinalSync fail');
  }
  return decryptData;
}

// 加密消息
function encryptMessageNew(symKey: cryptoFramework.SymKey, iv: cryptoFramework.IvParamsSpec,
  plainText: cryptoFramework.DataBlob) {
  let cipher = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  // 加密初始化
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
  let cipherData = cipher.doFinalSync(plainText);
  return cipherData;
}

// 解密消息
function decryptMessageNew(symKey: cryptoFramework.SymKey, iv: cryptoFramework.IvParamsSpec,
  cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('AES128|CBC|PKCS7');
  // 解密初始化
  decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
  let decryptData = decoder.doFinalSync(cipherText);
  return decryptData;
}

function question() {
  let message = 'This is a test';
  // 必须是16字节
  let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let symKey = genSymKeyByData(keyData);
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptText = encryptMessage(symKey, plainText);
  let decryptText = decryptMessage(symKey, encryptText);
  if (plainText.data.toString() === decryptText.data.toString()) {
    console.info('decrypt plainText:', decryptText.data.toString());
  } else {
    console.error('decrypt failed');
  }
}

function answer() {
  let iv = genRandomIv();
  let message = '中文';
  let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let symKey = genSymKeyByData(keyData);
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptText = encryptMessageNew(symKey, iv, plainText);
  let decryptText = decryptMessageNew(symKey, iv, encryptText);
  if (plainText.data.toString() === decryptText.data.toString()) {
    let decoder = util.TextDecoder.create('utf-8');
    let str = decoder.decodeToString(new Uint8Array(decryptText.data));
    console.info('decrypt plainText:', str);
  } else {
    console.error('decrypt failed');
  }
}

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Column() {
        Text('question')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            question();
          });
        Text('answer')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            answer();
          });
      };
    }
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：使用axios post请求到的数据直接乱码解密失败怎么办？

A：需要确认请求数据的编码格式是否前后端不一致。

Q：使用AES128|CBC|PKCS7进行解密，公钥是后端固定分配的，iv为密文base64.decode后的前16位，16位以后的内容为解密内容。解密后通过Uint8Array转string获得的字符串是乱码该如何解决？

A：后端提供的密钥长度为24字节，需要将算法标识由AES128调整为AES192，确保密钥长度与算法规格匹配，并将buffer.from方法的公钥字符串转成24位的Uint8Array。iv提取需确保前16字节与加密端完全一致，且Base64解码时需要指定MIME编码类型：base64.decode(ref, util.Type.MIME)。
