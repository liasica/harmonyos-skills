---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-3
title: 如何使用服务端下发的RSA公钥（字符串）对明文数据进行加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用服务端下发的RSA公钥（字符串）对明文数据进行加密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:27bb45d393d2479bf520191f1b1d49df0b4a265ef6d85d2d6b872f91324169af
---

将服务器下发的RSA公钥字符串赋值给`pubKeyStr`，即可实现。具体代码参考如下：

```typescript
import { buffer, util } from '@kit.ArkTS';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
/**
 * Encrypt using RSA asymmetric key (PKCS1 mode)
 * @param message Clear text data to be encrypted
 * @returns Encrypted string, encoded in base64 format
 */
export async function encryptRSA(message: string) {
  // Server issues RSA public key string (base64 encoding)
  let pubKeyStr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFQArGDm5BXM4jHHuZGIb/kUoqrSjXkjqPLgrDmqBFxNyYsyxvyFRO10nStQwdRkQkh5lZ5sqC1G/z6lyDPpEySTBo9S5GLZ2Tj4yinNjcMXmOwiHfyQAQo9LwdlyTedwRchg0fYewWBVTVhGcWPowT1aA+GnQhYwNmaS/iKQsNQIDAQAB";
  // Initialize Base64 tool instance
  let base64Helper = new util.Base64Helper();
  // Convert the public key to Uint8Array and package it as a DataBlob type
  let pubKeyBlob: cryptoFramework.DataBlob = { data: base64Helper.decodeSync(pubKeyStr) };
  // Create RSA key generator
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  // Convert the public key wrapper data pubKeyBlob into a key pair type KeyPair
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, null);
  // Create a Cipher object
  let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
  // Initialize encryption mode and specify the key keyPair. pubKey
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
  // Packaging requires encrypted plaintext
  let plainTextBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  // Pass in plaintext and retrieve encrypted data
  let encryptBlob = await cipher.doFinal(plainTextBlob);
  // Return encrypted string
  return base64Helper.encodeToStringSync(encryptBlob.data);
}
```

**参考链接**

[使用RSA非对称密钥（PKCS1模式）加解密](../harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1.md)
