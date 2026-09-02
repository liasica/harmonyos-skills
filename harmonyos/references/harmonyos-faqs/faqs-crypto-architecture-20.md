---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-20
title: 如何对公钥和私钥进行加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何对公钥和私钥进行加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:542ca8db78dd60e2ca3fccf7ac9b8dc76c99a83db25b62fb2e631e6d9bd54e89
---

使用 `@kit.CryptoArchitectureKit` 提供的密码学能力，可实现非对称加密中“公钥加密、私钥解密”的典型场景。

首先，通过 `[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)` 对预先定义的“公钥”和“私钥”字符串进行解码，得到原始字节数据，并将其转换为十六进制字符串，为后续密钥生成做准备。

接着，通过两个核心函数 `convertStrToPubKey` 和 `convertStrToPriKey` 将这些十六进制字符串还原成SM2算法所需的公钥和私钥对象。

参考代码如下：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';

let base = new util.Base64Helper();
let pubKeyStr = uint8ArrayToHexStr(base.decodeSync('公钥'));
let priKeyStr = uint8ArrayToHexStr(base.decodeSync('私钥'));

async function encryptionAndDecryption() {
  // Generate public and private keys based on the key parameters
  let pk = await convertStrToPubKey(pubKeyStr);
  let sk = await convertStrToPriKey(priKeyStr);

  // Encryption 
  let encryptText = await encryptMessagePromise(pk, '加密信息');
  // Decryption
  let res = await decryptMessagePromise(sk, encryptText);
}

// Generate SM2 public key based on key parameters
async function convertStrToPubKey(keyStr: string): Promise<cryptoFramework.PubKey> {
  let pubKeyStr = keyStr.startsWith("04") ? keyStr.slice(2) : keyStr;
  let pkPart1 = pubKeyStr.slice(0, pubKeyStr.length / 2);
  let pkPart2 = pubKeyStr.slice(pubKeyStr.length / 2);
  let pk: cryptoFramework.Point = {
    x: BigInt("0x" + pkPart1),
    y: BigInt("0x" + pkPart2),
  }
  let pubKeySpec: cryptoFramework.ECCPubKeySpec = {
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    pk: pk,
    algName: "SM2",
    specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
  }
  let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubKeySpec);
  return await keypairGenerator.generatePubKey();
}

// Generate SM2 private key based on key parameters 
async function convertStrToPriKey(keyStr: string): Promise<cryptoFramework.PriKey> {
  let sk = BigInt("0x" + keyStr);
  let priKeySpec: cryptoFramework.ECCPriKeySpec = {
    params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
    sk: sk,
    algName: "SM2",
    specType: cryptoFramework.AsyKeySpecType.PRIVATE_KEY_SPEC
  }
  let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(priKeySpec);
  return await keypairGenerator.generatePriKey();
}

// Decryption message
async function decryptMessagePromise(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
  let decoder = cryptoFramework.createCipher('SM2_256|SM3');
  await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
  let decryptData = await decoder.doFinal(cipherText);
  return decryptData;
}

// Encrypted message
async function encryptMessagePromise(publicKey: cryptoFramework.PubKey, plainText: string) {
  let cipher = cryptoFramework.createCipher('SM2_256|SM3');
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
  let encryptData = await cipher.doFinal({ data: stringToUint8Array(plainText) });
  return encryptData;
}

function uint8ArrayToHexStr(data: Uint8Array): string {
  let hexString = '';
  let i: number;
  for (i = 0; i < data.length; i++) {
    let char = ('00' + data[i].toString(16)).slice(-2);
    hexString += char;
  }
  return hexString;
}

function stringToUint8Array(str: string) {
  let arr = new Uint8Array(str.length);
  for (let i = 0, j = str.length; i < j; ++i) {
    arr[i] = str.charCodeAt(i);
  }
  return arr;
}
```
