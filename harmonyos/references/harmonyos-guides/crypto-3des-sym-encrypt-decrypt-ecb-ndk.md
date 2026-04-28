---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-3des-sym-encrypt-decrypt-ecb-ndk
title: 使用3DES对称密钥加解密(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 加解密 > 加解密开发指导 > 使用3DES对称密钥加解密(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:319da64524ec72030477c0180d7107563d1fa92db79dccc982694b6eae01ac04
---

对应的算法规格请查看[对称密钥加解密算法规格：3DES](crypto-sym-encrypt-decrypt-spec.md#section3des)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

**创建对象**

调用[OH\_CryptoSymKeyGenerator\_Create](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_create)、[OH\_CryptoSymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_generate)，生成密钥算法为3DES、密钥长度为192位的对称密钥（OH\_CryptoSymKey）。

如何生成3DES对称密钥，开发者可参考下文示例，并结合[对称密钥生成和转换规格：3DES](crypto-sym-key-generation-conversion-spec.md#section3des)和[指定二进制数据转换对称密钥](crypto-convert-binary-data-to-sym-key-ndk.md)理解，参考文档与当前示例可能存在入参差异，请注意区分。

**加密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成加密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为加密（CRYPTO\_ENCRYPT\_MODE），指定加密密钥（OH\_CryptoSymKey），初始化加密Cipher实例。

   ECB模式无加密参数，params直接传入null。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（明文）。

   * 当数据量较小时，可以在init完成后直接调用final。
   * 当数据量较大时，可以多次调用update，即分段加密。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取加密后的数据。

   * 如果使用update接口传入数据，此处data传入null。如果使用final接口传入数据，此处data传入明文数据。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**解密**

1. 调用[OH\_CryptoSymCipher\_Create](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_create)，指定字符串参数'3DES192|ECB|PKCS7'，创建对称密钥类型为3DES192、分组模式为ECB、填充模式为PKCS7的Cipher实例，用于完成解密操作。
2. 调用[OH\_CryptoSymCipher\_Init](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_init)，设置模式为解密（CRYPTO\_DECRYPT\_MODE），指定解密密钥（OH\_CryptoSymKey），初始化解密Cipher实例。ECB模式无加密参数，传入null。
3. 调用[OH\_CryptoSymCipher\_Update](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_update)，更新数据（密文）。

   * 当数据量较小时，可以在init完成后直接调用final。
   * 当数据量较大时，可以多次调用update，即分段解密。
   * 用户可以根据数据量大小自行决定操作方式。例如，当数据量超过20时，使用 update。
4. 调用[OH\_CryptoSymCipher\_Final](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_final)，获取解密数据。

   * 如果使用update接口传入数据，此处data传入null。如果使用final接口传入数据，此处data传入密文数据。
   * final输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

**销毁对象**

调用[OH\_CryptoSymKeyGenerator\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkeygenerator_destroy)、[OH\_CryptoSymCipher\_Destroy](../harmonyos-references/capi-crypto-sym-cipher-h.md#oh_cryptosymcipher_destroy)、[OH\_CryptoSymKey\_Destroy](../harmonyos-references/capi-crypto-sym-key-h.md#oh_cryptosymkey_destroy)、[OH\_Crypto\_FreeDataBlob](../harmonyos-references/capi-crypto-common-h.md#oh_crypto_freedatablob)释放申请的内存，销毁对象。

## 开发示例

当前示例以ECB分组模式为例，不需要设置加解密参数。

如果使用CBC、CTR、OFB、CFB分组模式，需设置加解密参数IV。请参考[设置加解密参数IV](crypto-3des-sym-encrypt-decrypt-ecb-ndk.md#设置加解密参数iv)，无论加密还是解密，在生成和初始化Cipher实例时均需修改相关参数。

```
1. #include "CryptoArchitectureKit/crypto_common.h"
2. #include "CryptoArchitectureKit/crypto_sym_cipher.h"
3. #include <cstring>
4. #include "file.h"

6. OH_Crypto_ErrCode doTest3DesEcb()
7. {
8. OH_CryptoSymKeyGenerator *genCtx = nullptr;
9. OH_CryptoSymCipher *encCtx = nullptr;
10. OH_CryptoSymCipher *decCtx = nullptr;
11. OH_CryptoSymKey *keyCtx = nullptr;
12. OH_CryptoSymCipherParams *params = nullptr;
13. char *plainText = const_cast<char *>("this is test!");
14. Crypto_DataBlob input = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
15. Crypto_DataBlob outUpdate = {.data = nullptr, .len = 0};
16. Crypto_DataBlob decUpdate = {.data = nullptr, .len = 0};
17. OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("3DES192", &genCtx); // 随机生成对称密钥
18. if (ret != CRYPTO_SUCCESS) {
19. goto end;
20. }
21. ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
22. if (ret != CRYPTO_SUCCESS) {
23. goto end;
24. }
25. ret = OH_CryptoSymCipherParams_Create(&params); // 创建参数
26. if (ret != CRYPTO_SUCCESS) {
27. goto end;
28. }
29. ret = OH_CryptoSymCipher_Create("3DES192|ECB|PKCS7", &encCtx); // 加密操作
30. if (ret != CRYPTO_SUCCESS) {
31. goto end;
32. }
33. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
34. if (ret != CRYPTO_SUCCESS) {
35. goto end;
36. }
37. ret = OH_CryptoSymCipher_Final(encCtx, &input, &outUpdate);
38. if (ret != CRYPTO_SUCCESS) {
39. goto end;
40. }
41. ret = OH_CryptoSymCipher_Create("3DES192|ECB|PKCS7", &decCtx); // 解密操作
42. if (ret != CRYPTO_SUCCESS) {
43. goto end;
44. }
45. ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params);
46. if (ret != CRYPTO_SUCCESS) {
47. goto end;
48. }
49. ret = OH_CryptoSymCipher_Final(decCtx, &outUpdate, &decUpdate);
50. if (ret != CRYPTO_SUCCESS) {
51. goto end;
52. }
53. end:
54. OH_CryptoSymCipherParams_Destroy(params);
55. OH_CryptoSymCipher_Destroy(encCtx);
56. OH_CryptoSymCipher_Destroy(decCtx);
57. OH_CryptoSymKeyGenerator_Destroy(genCtx);
58. OH_CryptoSymKey_Destroy(keyCtx);
59. OH_Crypto_FreeDataBlob(&outUpdate);
60. OH_Crypto_FreeDataBlob(&decUpdate);
61. return ret;
62. }
```

[3des\_ecb\_encryption\_decryption.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/EncryptionDecryption/EncryptionDecryptionGuidance3DES/entry/src/main/cpp/types/project/3des_ecb_encryption_decryption.cpp#L16-L79)

### 设置加解密参数IV

下述示例为CBC分组模式，需要设置加解密参数IV。

如果分组模式为CBC、CTR、OFB或CFB，需参考如下设置IV。ECB模式无需设置加解密参数。

```
1. OH_CryptoSymCipherParams *params = nullptr;
2. uint8_t iv[8] = {1, 2, 4, 12, 3, 4, 2, 3}; // 示例代码iv值，开发者可使用安全随机数生成。
3. Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};

5. ret = OH_CryptoSymCipherParams_Create(&params);
6. if (ret != CRYPTO_SUCCESS) {
7. goto end;
8. }
9. // 设置参数。
10. ret = OH_CryptoSymCipherParams_SetParam(params, CRYPTO_IV_DATABLOB, &ivBlob); // CBC模式只需要设置iv。
11. if (ret != CRYPTO_SUCCESS) {
12. goto end;
13. }

15. // 加密。
16. ret = OH_CryptoSymCipher_Create("3DES192|CBC|PKCS7", &encCtx);
17. if (ret != CRYPTO_SUCCESS) {
18. goto end;
19. }
20. ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
21. if (ret != CRYPTO_SUCCESS) {
22. goto end;
23. }
24. // 本段代码只展示CBC、CTR、OFB、CFB分段模式的不同，其他流程请参考开发示例。
```
