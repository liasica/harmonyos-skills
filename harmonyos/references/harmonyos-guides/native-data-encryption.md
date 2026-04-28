---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-data-encryption
title: 数据库加密 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 数据库加密 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd8dc5e576d7cb93656278375529d96187e45d1dcc30143e4813078d03a3ac0c
---

## 场景介绍

为了增强数据库的安全性，数据库提供了安全的加密功能，以有效保护存储的内容。

通过数据库加密，实现了数据库数据存储的保密性和完整性要求，使得数据库以密文方式存储并在密态方式下工作，确保了数据安全。

加密后的数据库只能通过接口进行访问，无法通过其它方式打开数据库文件。数据库的加密属性在创建数据库时确认，无法变更；关系型数据库从API version 22开始，支持通过[OH\_Rdb\_RekeyEx](../harmonyos-references/capi-relational-store-h.md#oh_rdb_rekeyex)接口调整其加密属性。

当前仅支持使用关系型数据库（C/C++）进行数据库加密。

## 开发步骤

关系型数据库通过调用OH\_Rdb\_SetEncrypted方法来设置是否加密。isEncrypted参数为true时表示加密，为false时表示不加密，默认不加密。

当isEncrypted为true时，可调用OH\_Rdb\_SetCryptoParam方法设置自定义的加密/解密密钥和算法等参数。

1. CMakeLists.txt中添加以下lib。

   ```
   1. libnative_rdb_ndk.z.so
   ```
2. 导入头文件。

   ```
   1. #include <cstring>
   2. #include "database/rdb/relational_store.h"
   3. #include "hilog/log.h"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L18-L20)
3. 针对是否配置自定义加密/解密参数，有如下两种场景：

   * 场景1：不配置自定义加密/解密参数，此时会使用默认的配置进行数据库的加密/解密。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
     4. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     5. OH_Rdb_SetStoreName(config, "RdbTest.db");
     6. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     7. // 设置为使用加密方式创建或打开数据库
     8. OH_Rdb_SetEncrypted(config, true);
     9. int errCode = 0;
     10. // 获取OH_Rdb_Store实例
     11. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     12. OH_Rdb_CloseStore(store);
     13. store = nullptr;
     14. OH_Rdb_DestroyConfig(config);
     15. config = nullptr;
     ```

     [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L25-L41)
   * 场景2：使用OH\_Rdb\_SetCryptoParam接口配置加密参数，此时会使用开发者自定义的密钥和算法参数进行数据库的加密/解密。

     如果开发者不关心加密算法及参数，使用默认加密配置即可，无需创建和配置自定义加密参数。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
     4. OH_Rdb_SetStoreName(config, "RdbTestConfigEncryptParam.db");
     5. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     6. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     7. // 设置为使用加密方式创建或打开数据库
     8. OH_Rdb_SetEncrypted(config, true);
     9. // 创建自定义加密参数对象
     10. OH_Rdb_CryptoParam *cryptoParam = OH_Rdb_CreateCryptoParam();

     12. // 示例中使用硬编码密钥仅用于演示目的， 实际应用中应使用安全的密钥管理服务
     13. uint8_t key[6] = {0x31, 0x32, 0x33, 0x34, 0x35, 0x36};
     14. // 使用指定的密钥打开加密数据库。不指定则由数据库负责生成并保存密钥，并使用生成的密钥。
     15. const int32_t length = 6;
     16. OH_Crypto_SetEncryptionKey(cryptoParam, key, length);
     17. // 秘钥信息使用完之后要清空
     18. for (size_t i = 0; i < sizeof(key); i++) {
     19. key[i] = 0;
     20. }
     21. // 设置KDF算法迭代次数。迭代次数必须大于零。不指定或等于零则使用默认值10000和默认加密算法。
     22. const int64_t iteration = 64000;
     23. OH_Crypto_SetIteration(cryptoParam, iteration);
     24. // 设置加密算法，如不设置默认为AES_256_GCM
     25. OH_Crypto_SetEncryptionAlgo(cryptoParam, Rdb_EncryptionAlgo::RDB_AES_256_CBC);
     26. // 设置HMAC算法，如不设置默认为SHA256
     27. OH_Crypto_SetHmacAlgo(cryptoParam, RDB_HMAC_SHA512);
     28. // 设置KDF算法，如不设置默认为SHA256
     29. OH_Crypto_SetKdfAlgo(cryptoParam, RDB_KDF_SHA512);
     30. // 设置打开加密数据库时使用的页大小，须为1024到65536之间的整数且为2的幂，如不设置默认为1024
     31. const int64_t pageSize = 4096;
     32. OH_Crypto_SetCryptoPageSize(cryptoParam, pageSize);
     33. // 设置自定义加密参数
     34. OH_Rdb_SetCryptoParam(config, cryptoParam);

     36. int errCode = 0;
     37. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     38. // 销毁自定义加密参数对象
     39. OH_Rdb_DestroyCryptoParam(cryptoParam);
     40. cryptoParam = nullptr;
     41. OH_Rdb_CloseStore(store);
     42. store = nullptr;
     43. OH_Rdb_DestroyConfig(config);
     44. config = nullptr;
     ```

     [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L52-L97)
4. 从API version 22开始，支持更换数据库密钥和加密参数，如果开发者需要更换已创建的加密数据库的密钥或者加密参数，可以使用OH\_Rdb\_RekeyEx进行更换。

   针对更换数据库密钥和加密参数，有如下场景：

   说明

   加密参数变更需谨慎，在完成OH\_Rdb\_RekeyEx操作后，必须使用新的参数来打开数据库，否则可能会导致开库失败。如果rekey过程因设备断电等原因中断，操作可能成功也可能失败。因此，建议业务方做好兜底保障（使用OH\_Rdb\_RekeyEx前后的参数进行冗余重试），确保不会错误地判断数据库的状态，从而避免出现数据库无法打开的问题。

   * 场景1：原数据库为默认参数加密数据库，更换密钥和加密参数。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, true);
     9. int errCode = 0;
     10. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     11. if (store == NULL) {
     12. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     13. OH_Rdb_DestroyConfig(config);
     14. config = NULL;
     15. return;
     16. }
     17. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     18. if (crypto == NULL) {
     19. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     20. OH_Rdb_DestroyConfig(config);
     21. OH_Rdb_CloseStore(store);
     22. config = NULL;
     23. store = NULL;
     24. return;
     25. }
     26. OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     27. OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     28. OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     29. OH_Crypto_SetCryptoPageSize(crypto, 2048);
     30. errCode = OH_Rdb_RekeyEx(store, crypto);

     32. if (errCode != 0) {
     33. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     34. }
     35. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     36. OH_Rdb_DestroyConfig(config);
     37. OH_Rdb_CloseStore(store);
     38. OH_Rdb_DestroyCryptoParam(crypto);
     39. config = NULL;
     40. store = NULL;
     41. crypto = NULL;
     ```
   * 场景2：原数据库为自定义参数加密数据库，更换自定义密钥和加密参数。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, true);
     9. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     10. if (crypto == NULL) {
     11. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     12. OH_Rdb_DestroyConfig(config);
     13. config = NULL;
     14. return;
     15. }
     16. uint8_t encryptionKey[] = "12345678";
     17. OH_Crypto_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
     18. memset(encryptionKey, 0, sizeof(encryptionKey));
     19. OH_Rdb_SetCryptoParam(config, crypto);

     21. int errCode = 0;
     22. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     23. if (store == NULL) {
     24. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     25. OH_Rdb_DestroyConfig(config);
     26. config = NULL;
     27. return;
     28. }
     29. OH_Rdb_CryptoParam *newCryptoParam = OH_Rdb_CreateCryptoParam();
     30. if (newCryptoParam == NULL) {
     31. OH_LOG_ERROR(LOG_APP, "Create newCryptoParam failed.");
     32. OH_Rdb_DestroyConfig(config);
     33. OH_Rdb_CloseStore(store);
     34. OH_Rdb_DestroyCryptoParam(crypto);
     35. config = NULL;
     36. store = NULL;
     37. crypto = NULL;
     38. return;
     39. }
     40. // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     41. uint8_t key[] = "87654321";
     42. OH_Crypto_SetEncryptionKey(newCryptoParam, key, sizeof(key));
     43. memset(key, 0, sizeof(key));
     44. OH_Crypto_SetEncryptionAlgo(newCryptoParam, RDB_AES_256_CBC);
     45. OH_Crypto_SetHmacAlgo(newCryptoParam, RDB_HMAC_SHA512);
     46. OH_Crypto_SetKdfAlgo(newCryptoParam, RDB_KDF_SHA512);
     47. OH_Crypto_SetCryptoPageSize(newCryptoParam, 4096);
     48. errCode = OH_Rdb_RekeyEx(store, newCryptoParam);

     50. if (errCode != 0) {
     51. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     52. }
     53. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     54. OH_Rdb_DestroyConfig(config);
     55. OH_Rdb_CloseStore(store);
     56. OH_Rdb_DestroyCryptoParam(crypto);
     57. OH_Rdb_DestroyCryptoParam(newCryptoParam);
     58. config = NULL;
     59. store = NULL;
     60. crypto = NULL;
     61. newCryptoParam = NULL;
     ```
   * 场景3：原数据库为默认参数加密库，更换自定义密钥和加密参数。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, true);
     9. int errCode = 0;
     10. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     11. if (store == NULL) {
     12. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     13. OH_Rdb_DestroyConfig(config);
     14. config = NULL;
     15. return;
     16. }
     17. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     18. if (crypto == NULL) {
     19. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     20. OH_Rdb_CloseStore(store);
     21. OH_Rdb_DestroyConfig(config);
     22. config = NULL;
     23. store = NULL;
     24. return;
     25. }
     26. // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     27. uint8_t key[] = "12345678";
     28. errCode = OH_Crypto_SetEncryptionKey(crypto, key, sizeof(key));
     29. memset(key, 0, sizeof(key));
     30. OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     31. OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     32. OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     33. OH_Crypto_SetCryptoPageSize(crypto, 2048);
     34. errCode = OH_Rdb_RekeyEx(store, crypto);

     36. if (errCode != 0) {
     37. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     38. }
     39. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     40. OH_Rdb_DestroyConfig(config);
     41. OH_Rdb_CloseStore(store);
     42. OH_Rdb_DestroyCryptoParam(crypto);
     43. config = NULL;
     44. store = NULL;
     45. crypto = NULL;
     ```
   * 场景4：原数据库为自定义参数加密数据库，更换数据库生成密钥和自定义加密参数。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, true);
     9. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     10. if (crypto == NULL) {
     11. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     12. OH_Rdb_DestroyConfig(config);
     13. config = NULL;
     14. return;
     15. }
     16. // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     17. uint8_t encryptionKey[] = "12345678";
     18. OH_Crypto_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
     19. memset(encryptionKey, 0, sizeof(encryptionKey));
     20. OH_Rdb_SetCryptoParam(config, crypto);

     22. int errCode = 0;
     23. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     24. if (store == NULL) {
     25. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     26. OH_Rdb_DestroyConfig(config);
     27. config = NULL;
     28. return;
     29. }
     30. OH_Rdb_CryptoParam *newCryptoParam = OH_Rdb_CreateCryptoParam();
     31. if (newCryptoParam == NULL) {
     32. OH_LOG_ERROR(LOG_APP, "Create newCryptoParam failed.");
     33. OH_Rdb_DestroyConfig(config);
     34. OH_Rdb_CloseStore(store);
     35. OH_Rdb_DestroyCryptoParam(crypto);
     36. config = NULL;
     37. store = NULL;
     38. crypto = NULL;
     39. return;
     40. }
     41. OH_Crypto_SetEncryptionAlgo(newCryptoParam, RDB_AES_256_CBC);
     42. OH_Crypto_SetHmacAlgo(newCryptoParam, RDB_HMAC_SHA512);
     43. OH_Crypto_SetKdfAlgo(newCryptoParam, RDB_KDF_SHA512);
     44. OH_Crypto_SetCryptoPageSize(newCryptoParam, 4096);
     45. errCode = OH_Rdb_RekeyEx(store, newCryptoParam);

     47. if (errCode != 0) {
     48. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     49. }
     50. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     51. OH_Rdb_DestroyConfig(config);
     52. OH_Rdb_CloseStore(store);
     53. OH_Rdb_DestroyCryptoParam(crypto);
     54. OH_Rdb_DestroyCryptoParam(newCryptoParam);
     55. config = NULL;
     56. store = NULL;
     57. crypto = NULL;
     58. newCryptoParam = NULL;
     ```
   * 场景5：原数据库为加密数据库，更换为非加密数据库。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, true);

     10. int errCode = 0;
     11. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     12. if (store == NULL) {
     13. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     14. OH_Rdb_DestroyConfig(config);
     15. config = NULL;
     16. return;
     17. }
     18. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     19. if (crypto == NULL) {
     20. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     21. OH_Rdb_DestroyConfig(config);
     22. OH_Rdb_CloseStore(store);
     23. config = NULL;
     24. store = NULL;
     25. return;
     26. }
     27. OH_Crypto_SetEncryptionAlgo(crypto, RDB_PLAIN_TEXT);
     28. errCode = OH_Rdb_RekeyEx(store, crypto);

     30. if (errCode != 0) {
     31. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     32. }
     33. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     34. OH_Rdb_DestroyConfig(config);
     35. OH_Rdb_CloseStore(store);
     36. OH_Rdb_DestroyCryptoParam(crypto);
     37. config = NULL;
     38. store = NULL;
     39. crypto = NULL;
     ```
   * 场景6：原数据库为非加密数据库，更换为加密数据库。

     ```
     1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     4. OH_Rdb_SetStoreName(config, "RdbTest.db");
     5. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     6. OH_Rdb_SetModuleName(config, "entry");
     7. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     8. OH_Rdb_SetEncrypted(config, false);

     10. int errCode = 0;
     11. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     12. if (store == NULL) {
     13. OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
     14. OH_Rdb_DestroyConfig(config);
     15. config = NULL;
     16. return;
     17. }
     18. OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     19. if (crypto == NULL) {
     20. OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
     21. OH_Rdb_DestroyConfig(config);
     22. OH_Rdb_CloseStore(store);
     23. config = NULL;
     24. store = NULL;
     25. return;
     26. }
     27. OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     28. OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     29. OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     30. OH_Crypto_SetCryptoPageSize(crypto, 2048);
     31. errCode = OH_Rdb_RekeyEx(store, crypto);

     33. if (errCode != 0) {
     34. OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     35. }
     36. // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     37. OH_Rdb_DestroyConfig(config);
     38. OH_Rdb_CloseStore(store);
     39. OH_Rdb_DestroyCryptoParam(crypto);
     40. config = NULL;
     41. store = NULL;
     42. crypto = NULL;
     ```
