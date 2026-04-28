---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-3
title: 如何使用服务端下发的RSA公钥（字符串）对明文数据进行加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用服务端下发的RSA公钥（字符串）对明文数据进行加密
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e501ebdd6f39fbdf91f391e48c131e48a5e637079c5e48855ac5140363ee1622
---

将服务器下发的RSA公钥字符串赋值给`pubKeyStr`，即可实现。具体代码参考如下：

```
1. import { buffer, util } from '@kit.ArkTS';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. /**
4. * Encrypt using RSA asymmetric key (PKCS1 mode)
5. * @param message Clear text data to be encrypted
6. * @returns Encrypted string, encoded in base64 format
7. */
8. export async function encryptRSA(message: string) {
9. // Server issues RSA public key string (base64 encoding)
10. let pubKeyStr = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFQArGDm5BXM4jHHuZGIb/kUoqrSjXkjqPLgrDmqBFxNyYsyxvyFRO10nStQwdRkQkh5lZ5sqC1G/z6lyDPpEySTBo9S5GLZ2Tj4yinNjcMXmOwiHfyQAQo9LwdlyTedwRchg0fYewWBVTVhGcWPowT1aA+GnQhYwNmaS/iKQsNQIDAQAB";
11. // Initialize Base64 tool instance
12. let base64Helper = new util.Base64Helper();
13. // Convert the public key to Uint8Array and package it as a DataBlob type
14. let pubKeyBlob: cryptoFramework.DataBlob = { data: base64Helper.decodeSync(pubKeyStr) };
15. // Create RSA key generator
16. let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
17. // Convert the public key wrapper data pubKeyBlob into a key pair type KeyPair
18. let keyPair = await rsaGenerator.convertKey(pubKeyBlob, null);
19. // Create a Cipher object
20. let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
21. // Initialize encryption mode and specify the key keyPair. pubKey
22. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyPair.pubKey, null);
23. // Packaging requires encrypted plaintext
24. let plainTextBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
25. // Pass in plaintext and retrieve encrypted data
26. let encryptBlob = await cipher.doFinal(plainTextBlob);
27. // Return encrypted string
28. return base64Helper.encodeToStringSync(encryptBlob.data);
29. }
```

[EncryptRSA.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/EncryptRSA.ets#L21-L49)

**参考链接**

[使用RSA非对称密钥（PKCS1模式）加解密](../harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1.md)
