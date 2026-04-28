---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm4-sym-encrypt-decrypt-gcm-by-segment
title: 使用SM4对称密钥（GCM模式）分段加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用SM4对称密钥（GCM模式）分段加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bfd594b38407281b55716c8fe1e95987d1e6948a7087d539751552ad8a5386dd
---

对应的算法规格请查看[对称密钥加解密算法规格：SM4](crypto-sym-encrypt-decrypt-spec.md#sm4)。

**加密**

1. 调用[cryptoFramework.createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)、[SymKeyGenerator.generateSymKey](../harmonyos-references/js-apis-cryptoframework.md#generatesymkey-1)，生成密钥算法为SM4、密钥长度为128位的对称密钥（SymKey）。

   如何生成SM4对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：SM4](crypto-sym-key-generation-conversion-spec.md#sm4)和[随机生成对称密钥](crypto-generate-sym-key-randomly.md)理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成加密操作。
3. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为加密（cryptoFramework.CryptoMode.ENCRYPT\_MODE），指定加密密钥（SymKey）和GCM模式对应的加密参数（GcmParamsSpec），初始化加密Cipher实例。
4. 将一次传入数据量设置为20字节，多次调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（明文）。

   * 当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。
   * 建议开发者对每次update的结果都判断是否为null，并在结果不为null时取出其中的数据进行拼接，形成完整的密文。因为在不同的模式下，update的结果可能会受到不同影响。

     1）比如ECB和CBC模式，始终以分组作为基本单位来加密，并输出本次update产生的加密分组结果。即当本次update操作凑满一个分组就输出密文，没有凑满则此次update输出null，将未加密的数据与下次输入的数据拼接凑分组再输出。等到最后doFinal的时候，将未加密的数据，根据指定的填充模式进行填充，再输出剩余加密结果。解密过程中的update同理。

     2）对于流加密模式（比如CTR和OFB模式），通常密文长度和明文长度相等。
5. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取加密后的数据。

   * 由于已使用update传入数据，此处data传入null。
   * doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。
6. 读取[GcmParamsSpec](../harmonyos-references/js-apis-cryptoframework.md#gcmparamsspec).authTag作为解密的认证信息。

   在GCM模式下，需要从加密后的数据中取出末尾16字节，作为解密时初始化的认证信息。示例中authTag恰好为16字节。

**解密**

1. 调用[cryptoFramework.createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)，指定字符串参数'SM4\_128|GCM|PKCS7'，创建对称密钥类型为SM4\_128、分组模式为GCM、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[Cipher.init](../harmonyos-references/js-apis-cryptoframework.md#init-1)，设置模式为解密（cryptoFramework.CryptoMode.DECRYPT\_MODE），指定解密密钥（SymKey）和GCM模式对应的解密参数（GcmParamsSpec），初始化解密Cipher实例。
3. 将一次传入数据量设置为20字节，多次调用[Cipher.update](../harmonyos-references/js-apis-cryptoframework.md#update-1)，更新数据（密文）。
4. 调用[Cipher.doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal-1)，获取解密后的数据。

* 异步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genGcmParamsSpec() {
  11. let ivBlob = generateRandom(12);
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. }; // The GCM authTag is obtained by doFinal() in encryption and passed in params of init() in decryption.
  20. let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
  21. iv: ivBlob,
  22. aad: aadBlob,
  23. authTag: tagBlob,
  24. algName: 'GcmParamsSpec'
  25. };
  26. return gcmParamsSpec;
  27. }

  29. let gcmParams = genGcmParamsSpec();

  31. // 分段加密消息
  32. async function encryptMessageUpdateBySegment(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  33. let cipher = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  34. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  35. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  36. let cipherText = new Uint8Array();
  37. for (let i = 0; i < plainText.data.length; i += updateLength) {
  38. let updateMessage = plainText.data.subarray(i, i + updateLength);
  39. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  40. // 分段update
  41. let updateOutput = await cipher.update(updateMessageBlob);
  42. // 把update的结果拼接起来，得到密文（有些情况下还需拼接doFinal的结果，这取决于分组模式
  43. // 和填充模式，本例中GCM模式的doFinal结果只包含authTag而不含密文，所以不需要拼接）
  44. let mergeText = new Uint8Array(cipherText.length + updateOutput.data.length);
  45. mergeText.set(cipherText);
  46. mergeText.set(updateOutput.data, cipherText.length);
  47. cipherText = mergeText;
  48. }
  49. gcmParams.authTag = await cipher.doFinal(null);
  50. let cipherBlob: cryptoFramework.DataBlob = { data: cipherText };
  51. return cipherBlob;
  52. }

  54. // 分段解密消息
  55. async function decryptMessagePromise(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  56. let decoder = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  57. await decoder.init(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
  58. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  59. let decryptText = new Uint8Array();
  60. for (let i = 0; i < cipherText.data.length; i += updateLength) {
  61. let updateMessage = cipherText.data.subarray(i, i + updateLength);
  62. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  63. // 分段update
  64. let updateOutput = await decoder.update(updateMessageBlob);
  65. // 把update的结果拼接起来，得到明文
  66. let mergeText = new Uint8Array(decryptText.length + updateOutput.data.length);
  67. mergeText.set(decryptText);
  68. mergeText.set(updateOutput.data, decryptText.length);
  69. decryptText = mergeText;
  70. }
  71. let decryptData = await decoder.doFinal(null);
  72. if (decryptData == null) {
  73. console.info('GCM decrypt result: success, decryptData is null.');
  74. }
  75. let decryptBlob: cryptoFramework.DataBlob = { data: decryptText };
  76. return decryptBlob;
  77. }

  79. async function genSymKeyByData(symKeyData: Uint8Array) {
  80. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  81. let sm4Generator = cryptoFramework.createSymKeyGenerator('SM4_128');
  82. let symKey = await sm4Generator.convertKey(symKeyBlob);
  83. console.info('convertKey result: success.');
  84. return symKey;
  85. }

  87. async function sm4() {
  88. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  89. let symKey = await genSymKeyByData(keyData);
  90. let message = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee'; // 假设信息总共43字节，根据utf-8解码后，也是43字节
  91. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  92. let encryptText = await encryptMessageUpdateBySegment(symKey, plainText);
  93. let decryptText = await decryptMessagePromise(symKey, encryptText);
  94. if (plainText.data.toString() === decryptText.data.toString()) {
  95. console.info('decrypt ok.');
  96. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  97. } else {
  98. console.error('decrypt failed.');
  99. }
  100. }
  ```

  [sm4\_gcm\_seg\_encryption\_decryption\_asynchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4ArkTs/entry/src/main/ets/pages/sm4_gcm_seg_encryption_decryption/sm4_gcm_seg_encryption_decryption_asynchronous.ets#L16-L117)
* 同步方法示例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function generateRandom(len: number) {
  5. let rand = cryptoFramework.createRandom();
  6. let generateRandSync = rand.generateRandomSync(len);
  7. return generateRandSync;
  8. }

  10. function genGcmParamsSpec() {
  11. let ivBlob = generateRandom(12); // 12 bytes
  12. let arr = [1, 2, 3, 4, 5, 6, 7, 8]; // 8 bytes
  13. let dataAad = new Uint8Array(arr);
  14. let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  15. arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]; // 16 bytes
  16. let dataTag = new Uint8Array(arr);
  17. let tagBlob: cryptoFramework.DataBlob = {
  18. data: dataTag
  19. }; // The GCM authTag is obtained by doFinal() in encryption and passed in params of init() in decryption.
  20. let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
  21. iv: ivBlob,
  22. aad: aadBlob,
  23. authTag: tagBlob,
  24. algName: 'GcmParamsSpec'
  25. };
  26. return gcmParamsSpec;
  27. }

  29. let gcmParams = genGcmParamsSpec();

  31. // 分段加密消息
  32. function encryptMessageUpdateBySegment(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
  33. let cipher = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  34. cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  35. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  36. let cipherText = new Uint8Array();
  37. for (let i = 0; i < plainText.data.length; i += updateLength) {
  38. let updateMessage = plainText.data.subarray(i, i + updateLength);
  39. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  40. // 分段update
  41. let updateOutput = cipher.updateSync(updateMessageBlob);
  42. // 把update的结果拼接起来，得到密文（有些情况下还需拼接doFinal的结果，这取决于分组模式
  43. // 和填充模式，本例中GCM模式的doFinal结果只包含authTag而不含密文，所以不需要拼接）
  44. let mergeText = new Uint8Array(cipherText.length + updateOutput.data.length);
  45. mergeText.set(cipherText);
  46. mergeText.set(updateOutput.data, cipherText.length);
  47. cipherText = mergeText;
  48. }
  49. gcmParams.authTag = cipher.doFinalSync(null);
  50. let cipherBlob: cryptoFramework.DataBlob = { data: cipherText };
  51. return cipherBlob;
  52. }

  54. // 分段解密消息
  55. function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
  56. let decoder = cryptoFramework.createCipher('SM4_128|GCM|PKCS7');
  57. decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, gcmParams);
  58. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求
  59. let decryptText = new Uint8Array();
  60. for (let i = 0; i < cipherText.data.length; i += updateLength) {
  61. let updateMessage = cipherText.data.subarray(i, i + updateLength);
  62. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  63. // 分段update
  64. let updateOutput = decoder.updateSync(updateMessageBlob);
  65. // 把update的结果拼接起来，得到明文
  66. let mergeText = new Uint8Array(decryptText.length + updateOutput.data.length);
  67. mergeText.set(decryptText);
  68. mergeText.set(updateOutput.data, decryptText.length);
  69. decryptText = mergeText;
  70. }
  71. let decryptData = decoder.doFinalSync(null);
  72. if (decryptData == null) {
  73. console.info('GCM decrypt result: success, decryptData is null.');
  74. }
  75. let decryptBlob: cryptoFramework.DataBlob = { data: decryptText };
  76. return decryptBlob;
  77. }

  79. function genSymKeyByData(symKeyData: Uint8Array) {
  80. let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  81. let sm4Generator = cryptoFramework.createSymKeyGenerator('SM4_128');
  82. let symKey = sm4Generator.convertKeySync(symKeyBlob);
  83. console.info('convertKeySync result: success.');
  84. return symKey;
  85. }

  87. function main() {
  88. let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  89. let symKey = genSymKeyByData(keyData);
  90. let message = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee'; // 假设信息总共43字节，根据utf-8解码后，也是43字节
  91. let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  92. let encryptText = encryptMessageUpdateBySegment(symKey, plainText);
  93. let decryptText = decryptMessage(symKey, encryptText);
  94. if (plainText.data.toString() === decryptText.data.toString()) {
  95. console.info('decrypt ok.');
  96. console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
  97. } else {
  98. console.error('decrypt failed.');
  99. }
  100. }
  ```

  [sm4\_gcm\_seg\_encryption\_decryption\_synchronous.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidanceSM4ArkTs/entry/src/main/ets/pages/sm4_gcm_seg_encryption_decryption/sm4_gcm_seg_encryption_decryption_synchronous.ets#L16-L117)
