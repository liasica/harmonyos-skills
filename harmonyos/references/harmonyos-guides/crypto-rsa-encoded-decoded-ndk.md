---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded-ndk
title: 使用RSA私钥进行编码解码(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 使用RSA私钥进行编码解码(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6a8b22a80a1ae171eebe0395b487068c394ee5bcb219b9a882f2bd7e7faa868c
---

**编码**

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)、[OH\_CryptoAsymKeyGenerator\_Generate](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_generate)，生成RSA密钥类型为RSA2048、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)和[随机生成非对称密钥对(C/C++)](crypto-generate-asym-key-pair-randomly-ndk.md)理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。
2. 调用[OH\_CryptoPrivKeyEncodingParams\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_create)创建参数对象（params），并通过[OH\_CryptoPrivKeyEncodingParams\_SetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkeyencodingparams_setparam)设置加密算法和密码。
3. 调用[OH\_CryptoPrivKey\_Encode](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkey_encode)，传入参数CRYPTO\_PEM/CRYPTO\_DER、PKCS1/PKCS8和参数对象（params）生成编码后的私钥字符串。

**解码**

1. 调用[OH\_CryptoAsymKeyGenerator\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_create)生成RSA非对称密钥生成器keyGen。

   如何生成RSA非对称密钥对，开发者可参考下文示例，并结合[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。
2. 调用[OH\_CryptoAsymKeyGenerator\_SetPassword](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_setpassword)，传入编码后的私钥字符串与编码口令。
3. 调用[OH\_CryptoAsymKeyGenerator\_Convert](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygenerator_convert)，传入参数CRYPTO\_PEM和编码后的私钥字符串，返回RSA密钥对。

* 编码示例：

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include "file.h"

4. static OH_Crypto_ErrCode SetParams(OH_CryptoPrivKeyEncodingParams *params)
5. {
6. Crypto_DataBlob password = {(uint8_t *)"1234567890", 10};
7. Crypto_DataBlob cipher = {(uint8_t *)"AES-128-CBC", 11};
8. OH_Crypto_ErrCode ret = OH_CryptoPrivKeyEncodingParams_SetParam(params,
9. CRYPTO_PRIVATE_KEY_ENCODING_PASSWORD_STR, &password);
10. if (ret != CRYPTO_SUCCESS) {
11. return ret;
12. }
13. ret = OH_CryptoPrivKeyEncodingParams_SetParam(params, CRYPTO_PRIVATE_KEY_ENCODING_SYMMETRIC_CIPHER_STR, &cipher);
14. if (ret != CRYPTO_SUCCESS) {
15. return ret;
16. }
17. return CRYPTO_SUCCESS;
18. }

20. OH_Crypto_ErrCode doTestPriKeyPkcs1Encoded()
21. {
22. OH_CryptoAsymKeyGenerator *keyGen = nullptr;
23. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA2048", &keyGen);
24. if (ret != CRYPTO_SUCCESS) {
25. return ret;
26. }
27. OH_CryptoKeyPair *keyPair = nullptr;
28. ret = OH_CryptoAsymKeyGenerator_Generate(keyGen, &keyPair);
29. if (ret != CRYPTO_SUCCESS) {
30. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
31. return ret;
32. }

34. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyPair);
35. if (privKey == nullptr) {
36. OH_CryptoKeyPair_Destroy(keyPair);
37. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
38. return CRYPTO_OPERTION_ERROR;
39. }
40. OH_CryptoPrivKeyEncodingParams *params = nullptr;
41. ret = OH_CryptoPrivKeyEncodingParams_Create(&params);
42. if (ret != CRYPTO_SUCCESS) {
43. OH_CryptoKeyPair_Destroy(keyPair);
44. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
45. return ret;
46. }
47. ret = SetParams(params);
48. if (ret != CRYPTO_SUCCESS) {
49. OH_CryptoPrivKeyEncodingParams_Destroy(params);
50. OH_CryptoKeyPair_Destroy(keyPair);
51. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
52. return ret;
53. }

55. Crypto_DataBlob pemData = {0};
56. ret = OH_CryptoPrivKey_Encode(privKey, CRYPTO_PEM, "PKCS1", params, &pemData);
57. if (ret != CRYPTO_SUCCESS) {
58. OH_CryptoPrivKeyEncodingParams_Destroy(params);
59. OH_CryptoKeyPair_Destroy(keyPair);
60. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
61. return ret;
62. }
63. OH_Crypto_FreeDataBlob(&pemData);
64. OH_CryptoPrivKeyEncodingParams_Destroy(params);
65. OH_CryptoKeyPair_Destroy(keyPair);
66. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
67. return ret;
68. }
```

* 解码示例：

  ```
  1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
  2. #include <string>
  3. #include "file.h"

  5. OH_Crypto_ErrCode doTestPriKeyPkcs1Decoded()
  6. {
  7. std::string priKeyPkcs1EncodingStr =
  8. "-----BEGIN RSA PRIVATE KEY-----\n"
  9. "Proc-Type: 4,ENCRYPTED\n"
  10. "DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n"
  11. "7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n"
  12. "t0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n"
  13. "vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n"
  14. "/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n"
  15. "W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n"
  16. "mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n"
  17. "T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n"
  18. "LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n"
  19. "Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n"
  20. "BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n"
  21. "k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n"
  22. "iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n"
  23. "OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n"
  24. "-----END RSA PRIVATE KEY-----\n";

  26. OH_CryptoAsymKeyGenerator *keyGen = nullptr;
  27. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA2048", &keyGen);
  28. if (ret != CRYPTO_SUCCESS) {
  29. return ret;
  30. }

  32. OH_CryptoKeyPair *dupKeyPair = nullptr;
  33. Crypto_DataBlob priKeyPkcs1EncodingData = {};
  34. priKeyPkcs1EncodingData.data = reinterpret_cast<uint8_t *>(const_cast<char *>(priKeyPkcs1EncodingStr.c_str()));
  35. priKeyPkcs1EncodingData.len = strlen(priKeyPkcs1EncodingStr.c_str());
  36. std::string password = "123456";
  37. ret = OH_CryptoAsymKeyGenerator_SetPassword(keyGen, reinterpret_cast<const unsigned char *>(password.c_str()),
  38. password.size());
  39. if (ret != CRYPTO_SUCCESS) {
  40. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
  41. return ret;
  42. }
  43. ret = OH_CryptoAsymKeyGenerator_Convert(keyGen, CRYPTO_PEM, nullptr, &priKeyPkcs1EncodingData, &dupKeyPair);
  44. if (ret != CRYPTO_SUCCESS) {
  45. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
  46. return ret;
  47. }
  48. OH_CryptoKeyPair_Destroy(dupKeyPair);
  49. OH_CryptoAsymKeyGenerator_Destroy(keyGen);
  50. return ret;
  51. }
  ```

  [prikey\_decoding.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/PrikeyOperation/entry/src/main/cpp/types/project/prikey_decoding.cpp#L16-L68)
