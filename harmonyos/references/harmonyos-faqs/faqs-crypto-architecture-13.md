---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-13
title: 如何实现RSA的公钥PK加密一段文字
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何实现RSA的公钥PK加密一段文字
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:47647f88d9716e4218cb34c78a6ed7626be5e4b429041e8104f8d2a079ec3fee
---

算法库目前提供了RSA加解密常用的三种模式：NoPadding、PKCS1 和 PKCS1\_OAEP。不同 RSA 密钥规格和不同填充方式支持加密的数据长度不同，详情见参考链接。

参考代码如下：

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { buffer, util } from '@kit.ArkTS';

4. // Convert string to byte stream
5. function stringToUint8Array(str: string) {
6. return new Uint8Array(buffer.from(str, 'utf-8').buffer);
7. }

9. // Convert byte stream into an understandable string
10. function uint8ArrayToString(array: Uint8Array) {
11. // Convert UTF-8 encoding to Unicode encoding
12. let out: string = '';
13. let index: number = 0;
14. let len: number = array.length;
15. while (index < len) {
16. let character = array[index++];
17. switch (character >> 4) {
18. case 0:
19. case 1:
20. case 2:
21. case 3:
22. case 4:
23. case 5:
24. case 6:
25. case 7:
26. out += String.fromCharCode(character);
27. break;
28. case 12:
29. case 13:
30. out += String.fromCharCode(((character & 0x1F) << 6) | (array[index++] & 0x3F));
31. break;
32. case 14:
33. out += String.fromCharCode(((character & 0x0F) << 12) | ((array[index++] & 0x3F) << 6) |
34. ((array[index++] & 0x3F) << 0));
35. break;
36. default:
37. break;
38. }
39. }
40. return out;
41. }

43. export class KeyPair {
44. publicKey: string = '';
45. privateKey: string = '';
46. }

48. export class RSA {
49. private ASY_KEY_NAME_RSA_3072: string = 'RSA1024';
50. private ALG_NAME_RSA_3072: string = 'RSA|PKCS1';
51. static priKey: Uint8Array = new Uint8Array(); // For temporary storage
52. static pubKey: Uint8Array = new Uint8Array(); // For temporary storage
53. private base: util.Base64Helper = new util.Base64Helper();

55. public async generateRsaKeyPair(): Promise<KeyPair> {
56. let keyPair: KeyPair = new KeyPair();
57. try {
58. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
59. const tempKeyPair = await asyKeyGenerator.generateKeyPair();
60. keyPair = {
61. publicKey: this.base.encodeToStringSync(tempKeyPair.pubKey.getEncoded().data),
62. privateKey: this.base.encodeToStringSync(tempKeyPair.priKey.getEncoded().data)
63. }
64. } catch (err) {
65. console.error(err);
66. }
67. return keyPair;
68. }

70. public async add(str: string, publicKey: string): Promise<string> {
71. let result = '';
72. try {
73. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
74. // Create a Cipher (decryption) object
75. let cipher = cryptoFramework.createCipher(this.ALG_NAME_RSA_3072);
76. // Introduce external public key encryption
77. let keyGenPromise: cryptoFramework.KeyPair =
78. await asyKeyGenerator.convertKey({ data: this.base.decodeSync(publicKey) }, null);
79. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyGenPromise.pubKey, null);
80. let put: cryptoFramework.DataBlob = { data: stringToUint8Array(str) };
81. const finalRes = await cipher.doFinal(put);
82. result = this.base.encodeToStringSync(finalRes.data);
83. console.info(result);
84. } catch (err) {
85. console.log(err.message);
86. }
87. return result;
88. }

90. public async rsaDecrypt(message: string | Uint8Array, privateKey: string): Promise<string> {
91. let result = '';
92. try {
93. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator(this.ASY_KEY_NAME_RSA_3072);
94. const keyPair = await asyKeyGenerator.convertKey(null, { data: this.base.decodeSync(privateKey) });
95. let cipher = cryptoFramework.createCipher(this.ALG_NAME_RSA_3072); // Create a Cipher (decryption) object
96. await cipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, keyPair.priKey, null);
97. let bytes: Uint8Array | string = message;
98. if (typeof message === 'string') {
99. bytes = this.base.decodeSync(message);
100. } else {
101. bytes = message;
102. }
103. const finalRes = await cipher.doFinal({ data: bytes });
104. result = uint8ArrayToString(finalRes.data);
105. console.info(result);
106. } catch (err) {
107. console.error(err.code);
108. }
109. return result;
110. }
111. }

113. @Entry
114. @Component
115. struct EncryptedText {
116. @State word: string = '加解密文字';
117. private EncryptionAndDecryption = new RSA();

119. async aboutToAppear(): Promise<void> {
120. let key = await this.EncryptionAndDecryption.generateRsaKeyPair();
121. let result = await this.EncryptionAndDecryption.add(this.word, key.publicKey);
122. this.EncryptionAndDecryption.rsaDecrypt(result, key.privateKey);
123. }

125. build() {
126. }
127. }
```

[RsaDecrypt.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/RsaDecrypt.ets#L21-L147)

**参考链接：**

[RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)
