---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-ndk
title: 消息摘要计算SHA256(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息摘要计算 > 消息摘要计算开发指导 > 消息摘要计算SHA256(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e5355e9873fefbf17f757c454a5e8209fd33dde2ac14ef566cf7d9acd0221c45
---

对应的算法规格请查看[消息摘要计算算法规格](crypto-generate-message-digest-overview.md#支持的算法与规格)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libohcrypto.so)
```

## 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](crypto-generate-message-digest-ndk.md#摘要算法一次性传入)，也可以把数据人工分段，然后[分段update](crypto-generate-message-digest-ndk.md#分段摘要算法)。对于同一段数据而言，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### 摘要算法（一次性传入）

1. 调用[OH\_CryptoDigest\_Create](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_create)，指定摘要算法SHA256，生成摘要实例（OH\_CryptoDigest）。
2. 调用[OH\_CryptoDigest\_Update](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_update)，传入自定义消息，进行摘要更新计算。单次update长度没有限制。
3. 调用[OH\_CryptoDigest\_Final](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_final)，获取摘要计算结果。
4. 调用[OH\_CryptoDigest\_GetLength](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_getlength)，获取摘要计算长度，单位为字节。
5. 调用[OH\_DigestCrypto\_Destroy](../harmonyos-references/capi-crypto-digest-h.md#oh_digestcrypto_destroy)，销毁摘要实例（OH\_CryptoDigest）。

* 以下使用单次传入数据，获取摘要计算结果为例：

  ```
  1. #include "CryptoArchitectureKit/crypto_common.h"
  2. #include "CryptoArchitectureKit/crypto_digest.h"
  3. #include <cstring>

  5. OH_Crypto_ErrCode doTestSha256Md()
  6. {
  7. OH_Crypto_ErrCode ret;
  8. OH_CryptoDigest *ctx = nullptr;
  9. char *testData = const_cast<char *>("0123456789");
  10. Crypto_DataBlob in = {.data = (uint8_t *)(testData), .len = strlen(testData)};
  11. Crypto_DataBlob out = {.data = nullptr, .len = 0};
  12. int mdLen = 0;
  13. ret = OH_CryptoDigest_Create("SHA256", &ctx);
  14. if (ret != CRYPTO_SUCCESS) {
  15. return ret;
  16. }
  17. do {
  18. ret = OH_CryptoDigest_Update(ctx, &in);
  19. if (ret != CRYPTO_SUCCESS) {
  20. break;
  21. }
  22. ret = OH_CryptoDigest_Final(ctx, &out);
  23. if (ret != CRYPTO_SUCCESS) {
  24. break;
  25. }
  26. mdLen = OH_CryptoDigest_GetLength(ctx);
  27. } while (0);
  28. OH_Crypto_FreeDataBlob(&out);
  29. OH_DigestCrypto_Destroy(ctx);
  30. return ret;
  31. }
  ```

  [singleTime.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/cpp/types/project/sha256/singleTime.cpp#L16-L50)

### 分段摘要算法

1. 调用[OH\_CryptoDigest\_Create](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_create)，指定摘要算法SHA256，生成摘要实例（OH\_CryptoDigest）。
2. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[OH\_CryptoDigest\_Update](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_update)，进行摘要更新计算。
3. 调用[OH\_CryptoDigest\_Final](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_final)，获取摘要计算结果。
4. 调用[OH\_CryptoDigest\_GetLength](../harmonyos-references/capi-crypto-digest-h.md#oh_cryptodigest_getlength)，获取摘要计算长度，单位为字节。
5. 调用[OH\_DigestCrypto\_Destroy](../harmonyos-references/capi-crypto-digest-h.md#oh_digestcrypto_destroy)，销毁摘要实例（OH\_CryptoDigest）。

* 以下使用分段传入数据，获取摘要计算结果为例：

  ```
  1. #include <cstdlib>
  2. #include "CryptoArchitectureKit/crypto_common.h"
  3. #include "CryptoArchitectureKit/crypto_digest.h"
  4. #define OH_CRYPTO_DIGEST_DATA_MAX (1024 * 1024 * 100)

  6. static constexpr int INT_640 = 640;

  8. OH_Crypto_ErrCode doLoopSha256Md()
  9. {
  10. OH_Crypto_ErrCode ret;
  11. OH_CryptoDigest *ctx = nullptr;
  12. uint8_t *testData = (uint8_t *)malloc(OH_CRYPTO_DIGEST_DATA_MAX);
  13. if (testData == nullptr) {
  14. return CRYPTO_MEMORY_ERROR;
  15. }
  16. Crypto_DataBlob out = {.data = nullptr, .len = 0};
  17. int mdLen = 0;
  18. int isBlockSize = 20;
  19. int offset = 0;

  21. ret = OH_CryptoDigest_Create("SHA256", &ctx);
  22. if (ret != CRYPTO_SUCCESS) {
  23. return ret;
  24. }
  25. do {
  26. for (int i = 0; i < INT_640 / isBlockSize; i++) {
  27. Crypto_DataBlob in = {
  28. .data = reinterpret_cast<uint8_t *>(testData + offset),
  29. .len = static_cast<size_t>(isBlockSize)};
  30. ret = OH_CryptoDigest_Update(ctx, &in);
  31. if (ret != CRYPTO_SUCCESS) {
  32. break;
  33. }
  34. offset += isBlockSize;
  35. }
  36. ret = OH_CryptoDigest_Final(ctx, &out);
  37. if (ret != CRYPTO_SUCCESS) {
  38. break;
  39. }
  40. mdLen = OH_CryptoDigest_GetLength(ctx);
  41. } while (0);
  42. OH_Crypto_FreeDataBlob(&out);
  43. OH_DigestCrypto_Destroy(ctx);
  44. return ret;
  45. }
  ```

  [segmentation.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/cpp/types/project/sha256/segmentation.cpp#L16-L64)
