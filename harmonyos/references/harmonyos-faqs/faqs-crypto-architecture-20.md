---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-20
title: 如何对公钥和私钥进行加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何对公钥和私钥进行加解密
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c787a2cece55b6c54a4eff62f6b42b9dbb1ff82534381a01a098ea7a6318ee1b
---

使用 `@kit.CryptoArchitectureKit` 提供的密码学能力，可实现非对称加密中“公钥加密、私钥解密”的典型场景。

首先，通过 `[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)` 对预先定义的“公钥”和“私钥”字符串进行解码，得到原始字节数据，并将其转换为十六进制字符串，为后续密钥生成做准备。

接着，通过两个核心函数 `convertStrToPubKey` 和 `convertStrToPriKey` 将这些十六进制字符串还原成SM2算法所需的公钥和私钥对象。

参考代码如下：

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { util } from '@kit.ArkTS';

4. let base = new util.Base64Helper();
5. let pubKeyStr = uint8ArrayToHexStr(base.decodeSync('公钥'));
6. let priKeyStr = uint8ArrayToHexStr(base.decodeSync('私钥'));

8. async function encryptionAndDecryption() {
9. // Generate public and private keys based on the key parameters
10. let pk = await convertStrToPubKey(pubKeyStr);
11. let sk = await convertStrToPriKey(priKeyStr);

13. // Encryption
14. let encryptText = await encryptMessagePromise(pk, '加密信息');
15. // Decryption
16. let res = await decryptMessagePromise(sk, encryptText);
17. }

19. // Generate SM2 public key based on key parameters
20. async function convertStrToPubKey(keyStr: string): Promise<cryptoFramework.PubKey> {
21. let pubKeyStr = keyStr.startsWith("04") ? keyStr.slice(2) : keyStr;
22. let pkPart1 = pubKeyStr.slice(0, pubKeyStr.length / 2);
23. let pkPart2 = pubKeyStr.slice(pubKeyStr.length / 2);
24. let pk: cryptoFramework.Point = {
25. x: BigInt("0x" + pkPart1),
26. y: BigInt("0x" + pkPart2),
27. }
28. let pubKeySpec: cryptoFramework.ECCPubKeySpec = {
29. params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
30. pk: pk,
31. algName: "SM2",
32. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC
33. }
34. let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(pubKeySpec);
35. return await keypairGenerator.generatePubKey();
36. }

38. // Generate SM2 private key based on key parameters
39. async function convertStrToPriKey(keyStr: string): Promise<cryptoFramework.PriKey> {
40. let sk = BigInt("0x" + keyStr);
41. let priKeySpec: cryptoFramework.ECCPriKeySpec = {
42. params: cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2'),
43. sk: sk,
44. algName: "SM2",
45. specType: cryptoFramework.AsyKeySpecType.PRIVATE_KEY_SPEC
46. }
47. let keypairGenerator = cryptoFramework.createAsyKeyGeneratorBySpec(priKeySpec);
48. return await keypairGenerator.generatePriKey();
49. }

51. // Decryption message
52. async function decryptMessagePromise(privateKey: cryptoFramework.PriKey, cipherText: cryptoFramework.DataBlob) {
53. let decoder = cryptoFramework.createCipher('SM2_256|SM3');
54. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, privateKey, null);
55. let decryptData = await decoder.doFinal(cipherText);
56. return decryptData;
57. }

59. // Encrypted message
60. async function encryptMessagePromise(publicKey: cryptoFramework.PubKey, plainText: string) {
61. let cipher = cryptoFramework.createCipher('SM2_256|SM3');
62. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, publicKey, null);
63. let encryptData = await cipher.doFinal({ data: stringToUint8Array(plainText) });
64. return encryptData;
65. }

67. function uint8ArrayToHexStr(data: Uint8Array): string {
68. let hexString = '';
69. let i: number;
70. for (i = 0; i < data.length; i++) {
71. let char = ('00' + data[i].toString(16)).slice(-2);
72. hexString += char;
73. }
74. return hexString;
75. }

77. function stringToUint8Array(str: string) {
78. let arr = new Uint8Array(str.length);
79. for (let i = 0, j = str.length; i < j; ++i) {
80. arr[i] = str.charCodeAt(i);
81. }
82. return arr;
83. }
```

[EncryptionAndDecryption.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/EncryptionAndDecryption.ets#L21-L103)
