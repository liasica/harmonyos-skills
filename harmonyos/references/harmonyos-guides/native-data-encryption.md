---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-data-encryption
title: 数据库加密 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 数据库加密 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2cf717396fdf08678c5bf8599561ee12e90fd56b2dff29dc7b7e8d0b17b206e
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

   ```txt
   libnative_rdb_ndk.z.so
   ```
2. 导入头文件。

   ```
   #include <cstring>
   #include "database/rdb/relational_store.h"
   #include "hilog/log.h"
   ```
3. 针对是否配置自定义加密/解密参数，有如下两种场景：

   * 场景1：不配置自定义加密/解密参数，此时会使用默认的配置进行数据库的加密/解密。

     ```
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     // 设置为使用加密方式创建或打开数据库
     OH_Rdb_SetEncrypted(config, true);
     int errCode = 0;
     // 获取OH_Rdb_Store实例
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     OH_Rdb_CloseStore(store);
     store = nullptr;
     OH_Rdb_DestroyConfig(config);
     config = nullptr;
     ```
   * 场景2：使用OH\_Rdb\_SetCryptoParam接口配置加密参数，此时会使用开发者自定义的密钥和算法参数进行数据库的加密/解密。

     如果开发者不关心加密算法及参数，使用默认加密配置即可，无需创建和配置自定义加密参数。

     ```
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
     OH_Rdb_SetStoreName(config, "RdbTestConfigEncryptParam.db");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     // 设置为使用加密方式创建或打开数据库
     OH_Rdb_SetEncrypted(config, true);
     // 创建自定义加密参数对象
     OH_Rdb_CryptoParam *cryptoParam = OH_Rdb_CreateCryptoParam();
         
     // 示例中使用硬编码密钥仅用于演示目的， 实际应用中应使用安全的密钥管理服务
     uint8_t key[6] = {0x31, 0x32, 0x33, 0x34, 0x35, 0x36};
     // 使用指定的密钥打开加密数据库。不指定则由数据库负责生成并保存密钥，并使用生成的密钥。
     const int32_t length = 6;
     OH_Crypto_SetEncryptionKey(cryptoParam, key, length);
     // 密钥信息使用完之后要清空
     for (size_t i = 0; i < sizeof(key); i++) {
         key[i] = 0;
     }
     // 设置KDF算法迭代次数。迭代次数必须大于零。不指定或等于零则使用默认值10000和默认加密算法。
     const int64_t iteration = 64000;
     OH_Crypto_SetIteration(cryptoParam, iteration);
     // 设置加密算法，如不设置默认为AES_256_GCM
     OH_Crypto_SetEncryptionAlgo(cryptoParam, Rdb_EncryptionAlgo::RDB_AES_256_CBC);
     // 设置HMAC算法，如不设置默认为SHA256
     OH_Crypto_SetHmacAlgo(cryptoParam, RDB_HMAC_SHA512);
     // 设置KDF算法，如不设置默认为SHA256
     OH_Crypto_SetKdfAlgo(cryptoParam, RDB_KDF_SHA512);
     // 设置打开加密数据库时使用的页大小，须为1024到65536之间的整数且为2的幂，如不设置默认为1024
     const int64_t pageSize = 4096;
     OH_Crypto_SetCryptoPageSize(cryptoParam, pageSize);
     // 设置自定义加密参数
     OH_Rdb_SetCryptoParam(config, cryptoParam);
         
     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     // 销毁自定义加密参数对象
     OH_Rdb_DestroyCryptoParam(cryptoParam);
     cryptoParam = nullptr;
     OH_Rdb_CloseStore(store);
     store = nullptr;
     OH_Rdb_DestroyConfig(config);
     config = nullptr;
     ```
4. 从API version 22开始，支持更换数据库密钥和加密参数，如果开发者需要更换已创建的加密数据库的密钥或者加密参数，可以使用OH\_Rdb\_RekeyEx进行更换。

   针对更换数据库密钥和加密参数，有如下场景：

   **说明** 

   加密参数变更需谨慎，在完成OH\_Rdb\_RekeyEx操作后，必须使用新的参数来打开数据库，否则可能会导致开库失败。如果rekey过程因设备断电等原因中断，操作可能成功也可能失败。因此，建议业务方做好兜底保障（使用OH\_Rdb\_RekeyEx前后的参数进行冗余重试），确保不会错误地判断数据库的状态，从而避免出现数据库无法打开的问题。

   * 场景1：原数据库为默认参数加密数据库，更换密钥和加密参数。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, true);
     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_DestroyConfig(config);
         OH_Rdb_CloseStore(store);
         config = NULL;
         store = NULL;
         return;
     }
     OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     OH_Crypto_SetCryptoPageSize(crypto, 2048);
     errCode = OH_Rdb_RekeyEx(store, crypto);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     config = NULL;
     store = NULL;
     crypto = NULL;
     ```
   * 场景2：原数据库为自定义参数加密数据库，更换自定义密钥和加密参数。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, true);
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     uint8_t encryptionKey[] = "12345678";
     OH_Crypto_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
     memset(encryptionKey, 0, sizeof(encryptionKey));
     OH_Rdb_SetCryptoParam(config, crypto);

     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *newCryptoParam = OH_Rdb_CreateCryptoParam();
     if (newCryptoParam == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create newCryptoParam failed.");
         OH_Rdb_DestroyConfig(config);
         OH_Rdb_CloseStore(store);
         OH_Rdb_DestroyCryptoParam(crypto);
         config = NULL;
         store = NULL;
         crypto = NULL;
         return;
     }
     // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     uint8_t key[] = "87654321";
     OH_Crypto_SetEncryptionKey(newCryptoParam, key, sizeof(key));
     memset(key, 0, sizeof(key));
     OH_Crypto_SetEncryptionAlgo(newCryptoParam, RDB_AES_256_CBC);
     OH_Crypto_SetHmacAlgo(newCryptoParam, RDB_HMAC_SHA512);
     OH_Crypto_SetKdfAlgo(newCryptoParam, RDB_KDF_SHA512);
     OH_Crypto_SetCryptoPageSize(newCryptoParam, 4096);
     errCode = OH_Rdb_RekeyEx(store, newCryptoParam);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     OH_Rdb_DestroyCryptoParam(newCryptoParam);
     config = NULL;
     store = NULL;
     crypto = NULL;
     newCryptoParam = NULL;
     ```
   * 场景3：原数据库为默认参数加密库，更换自定义密钥和加密参数。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, true);
     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_CloseStore(store);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         store = NULL;
         return;
     }
     // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     uint8_t key[] = "12345678";
     errCode = OH_Crypto_SetEncryptionKey(crypto, key, sizeof(key));
     memset(key, 0, sizeof(key));
     OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     OH_Crypto_SetCryptoPageSize(crypto, 2048);
     errCode = OH_Rdb_RekeyEx(store, crypto);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     config = NULL;
     store = NULL;
     crypto = NULL;
     ```
   * 场景4：原数据库为自定义参数加密数据库，更换数据库生成密钥和自定义加密参数。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, true);
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     // 注意：示例中使用硬编码密钥仅用于演示目的，实际应用中应使用安全的密钥管理服务，使用后应该及时清零
     uint8_t encryptionKey[] = "12345678";
     OH_Crypto_SetEncryptionKey(crypto, encryptionKey, sizeof(encryptionKey));
     memset(encryptionKey, 0, sizeof(encryptionKey));
     OH_Rdb_SetCryptoParam(config, crypto);

     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *newCryptoParam = OH_Rdb_CreateCryptoParam();
     if (newCryptoParam == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create newCryptoParam failed.");
         OH_Rdb_DestroyConfig(config);
         OH_Rdb_CloseStore(store);
         OH_Rdb_DestroyCryptoParam(crypto);
         config = NULL;
         store = NULL;
         crypto = NULL;
         return;
     }
     OH_Crypto_SetEncryptionAlgo(newCryptoParam, RDB_AES_256_CBC);
     OH_Crypto_SetHmacAlgo(newCryptoParam, RDB_HMAC_SHA512);
     OH_Crypto_SetKdfAlgo(newCryptoParam, RDB_KDF_SHA512);
     OH_Crypto_SetCryptoPageSize(newCryptoParam, 4096);
     errCode = OH_Rdb_RekeyEx(store, newCryptoParam);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     OH_Rdb_DestroyCryptoParam(newCryptoParam);
     config = NULL;
     store = NULL;
     crypto = NULL;
     newCryptoParam = NULL;
     ```
   * 场景5：原数据库为加密数据库，更换为非加密数据库。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, true);

     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_DestroyConfig(config);
         OH_Rdb_CloseStore(store);
         config = NULL;
         store = NULL;
         return;
     }
     OH_Crypto_SetEncryptionAlgo(crypto, RDB_PLAIN_TEXT);
     errCode = OH_Rdb_RekeyEx(store, crypto);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     config = NULL;
     store = NULL;
     crypto = NULL;
     ```
   * 场景6：原数据库为非加密数据库，更换为加密数据库。

     ```c
     OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
     OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
     OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
     OH_Rdb_SetStoreName(config, "RdbTest.db");
     OH_Rdb_SetBundleName(config, "com.example.nativedemo");
     OH_Rdb_SetModuleName(config, "entry");
     OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
     OH_Rdb_SetEncrypted(config, false);

     int errCode = 0;
     OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
     if (store == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
         OH_Rdb_DestroyConfig(config);
         config = NULL;
         return;
     }
     OH_Rdb_CryptoParam *crypto = OH_Rdb_CreateCryptoParam();
     if (crypto == NULL) {
         OH_LOG_ERROR(LOG_APP, "Create crypto failed.");
         OH_Rdb_DestroyConfig(config);
         OH_Rdb_CloseStore(store);
         config = NULL;
         store = NULL;
         return;
     }
     OH_Crypto_SetEncryptionAlgo(crypto, RDB_AES_256_CBC);
     OH_Crypto_SetHmacAlgo(crypto, RDB_HMAC_SHA512);
     OH_Crypto_SetKdfAlgo(crypto, RDB_KDF_SHA512);
     OH_Crypto_SetCryptoPageSize(crypto, 2048);
     errCode = OH_Rdb_RekeyEx(store, crypto);

     if (errCode != 0) {
         OH_LOG_ERROR(LOG_APP, "RekeyEx failed, errCode: %{public}d", errCode);
     }
     // 在完成OH_Rdb_RekeyEx操作后，如果后续需要重新开库时必须使用新的参数来打开数据库
     OH_Rdb_DestroyConfig(config);
     OH_Rdb_CloseStore(store);
     OH_Rdb_DestroyCryptoParam(crypto);
     config = NULL;
     store = NULL;
     crypto = NULL;
     ```
