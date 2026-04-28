---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-key-in-plaintext-ndk
title: 明文导入密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 明文导入密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea274f7665a2c019bc190e0f97dabb3643fad33a4cf020f36bc7cca3a623cc11
---

以明文导入ECC密钥为例。具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 封装密钥属性集和密钥材料。通过[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)、[OH\_Huks\_AddParams](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_addparams)、[OH\_Huks\_BuildParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_buildparamset)构造密钥属性集paramSet。

   * 密钥属性集中必须包含[OH\_Huks\_KeyAlg](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyalg)、[OH\_Huks\_KeySize](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keysize)、[OH\_Huks\_KeyPurpose](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keypurpose)属性。
   * 密钥材料须符合[HUKS密钥材料格式](huks-concepts.md#密钥材料格式)。
3. 调用[OH\_Huks\_ImportKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_importkeyitem)，传入密钥别名和密钥属性集，导入密钥。

### 导入AES256密钥

```
1. /* 以下以明文导入AES密钥为例 */
2. #include "huks/native_huks_api.h"
3. #include "huks/native_huks_param.h"
4. #include "napi/native_api.h"
5. #include <cstring>
6. #include "file.h"

8. #define OH_HUKS_AES_KEY_SIZE_32 32

10. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
11. uint32_t paramCount)
12. {
13. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. return ret;
16. }
17. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
18. if (ret.errorCode != OH_HUKS_SUCCESS) {
19. OH_Huks_FreeParamSet(paramSet);
20. return ret;
21. }
22. ret = OH_Huks_BuildParamSet(paramSet);
23. if (ret.errorCode != OH_HUKS_SUCCESS) {
24. OH_Huks_FreeParamSet(paramSet);
25. return ret;
26. }
27. return ret;
28. }
29. static struct OH_Huks_Param g_testImportKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
30. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
31. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
32. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

34. napi_value ImportAesKey(napi_env env, napi_callback_info info)
35. {
36. /* 公钥，用于后续导入密钥 */
37. uint8_t pubKey[OH_HUKS_AES_KEY_SIZE_32] = {0xfb, 0x8b, 0x9f, 0x12, 0xa0, 0x83, 0x19, 0xbe, 0x6a, 0x6f, 0x63,
38. 0x2a, 0x7c, 0x86, 0xba, 0xca, 0x64, 0x0b, 0x88, 0x96, 0xe2, 0xfa,
39. 0x77, 0xbc, 0x71, 0xe3, 0x0f, 0x0f, 0x9e, 0x3c, 0xe5, 0xf9};
40. struct OH_Huks_Blob publicKey = {OH_HUKS_AES_KEY_SIZE_32, pubKey};
41. struct OH_Huks_ParamSet *testImportKeyParamSet = nullptr;
42. struct OH_Huks_Result ohResult;
43. do {
44. ohResult = InitParamSet(&testImportKeyParamSet, g_testImportKeyParam,
45. sizeof(g_testImportKeyParam) / sizeof(OH_Huks_Param));
46. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
47. break;
48. }
49. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
50. break;
51. }
52. /* 导入密钥 */
53. char newKey[] = "test_aes_import";
54. struct OH_Huks_Blob newKeyAlias = {.size = (uint32_t)strlen(newKey), .data = (uint8_t *)newKey};
55. ohResult = OH_Huks_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
56. } while (0);

58. OH_Huks_FreeParamSet(&testImportKeyParamSet);

60. napi_value ret;
61. napi_create_int32(env, ohResult.errorCode, &ret);
62. return ret;
63. }
```

[napi\_aes256.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/cpp/types/projects/napi_aes256.cpp#L16-L80)

### 导入RSA2048密钥对

```
1. /* 以下以明文导入RSA2048密钥为例 */
2. #include "huks/native_huks_api.h"
3. #include "huks/native_huks_param.h"
4. #include "napi/native_api.h"
5. #include <cstring>
6. #include "file.h"

8. #define RSA_KEY_SIZE_1024 1024

10. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
11. uint32_t paramCount)
12. {
13. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. return ret;
16. }
17. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
18. if (ret.errorCode != OH_HUKS_SUCCESS) {
19. OH_Huks_FreeParamSet(paramSet);
20. return ret;
21. }
22. ret = OH_Huks_BuildParamSet(paramSet);
23. if (ret.errorCode != OH_HUKS_SUCCESS) {
24. OH_Huks_FreeParamSet(paramSet);
25. return ret;
26. }
27. return ret;
28. }
29. static struct OH_Huks_Param g_testImportKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
30. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
31. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
32. {.tag = OH_HUKS_TAG_IMPORT_KEY_TYPE, .uint32Param = OH_HUKS_KEY_TYPE_KEY_PAIR},
33. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

35. napi_value ImportRsaKey(napi_env env, napi_callback_info info)
36. {
37. /* 密钥材料，用于后续导入密钥 */
38. uint8_t pubKey[RSA_KEY_SIZE_1024] = {0x01, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x03,
39. 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xc5, 0x35, 0x62, 0x48, 0xc4, 0x92, 0x87, 0x73, 0x0d, 0x42, 0x96,
40. 0xfc, 0x7b, 0x11, 0x05, 0x06, 0x0f, 0x8d, 0x66, 0xc1, 0x0e, 0xad, 0x37, 0x44, 0x92, 0x95, 0x2f, 0x6a, 0x55,
41. 0xba, 0xec, 0x1d, 0x54, 0x62, 0x0a, 0x4b, 0xd3, 0xc7, 0x05, 0xe4, 0x07, 0x40, 0xd9, 0xb7, 0xc2, 0x12, 0xcb,
42. 0x9a, 0x90, 0xad, 0xe3, 0x24, 0xe8, 0x5e, 0xa6, 0xf8, 0xd0, 0x6e, 0xbc, 0xd1, 0x69, 0x7f, 0x6b, 0xe4, 0x2b,
43. 0x4e, 0x1a, 0x65, 0xbb, 0x73, 0x88, 0x6b, 0x7c, 0xaf, 0x7e, 0xd0, 0x47, 0x26, 0xeb, 0xa5, 0xbe, 0xd6, 0xe8,
44. 0xee, 0x9c, 0xa5, 0x66, 0xa5, 0xc9, 0xd3, 0x25, 0x13, 0xc4, 0x0e, 0x6c, 0xab, 0x50, 0xb6, 0x50, 0xc9, 0xce,
45. 0x8f, 0x0a, 0x0b, 0xc6, 0x28, 0x69, 0xe9, 0x83, 0x69, 0xde, 0x42, 0x56, 0x79, 0x7f, 0xde, 0x86, 0x24, 0xca,
46. 0xfc, 0xaa, 0xc0, 0xf3, 0xf3, 0x7f, 0x92, 0x8e, 0x8a, 0x12, 0x52, 0xfe, 0x50, 0xb1, 0x5e, 0x8c, 0x01, 0xce,
47. 0xfc, 0x7e, 0xf2, 0x4f, 0x5f, 0x03, 0xfe, 0xa7, 0xcd, 0xa1, 0xfc, 0x94, 0x52, 0x00, 0x8b, 0x9b, 0x7f, 0x09,
48. 0xab, 0xa8, 0xa4, 0xf5, 0xb4, 0xa5, 0xaa, 0xfc, 0x72, 0xeb, 0x17, 0x40, 0xa9, 0xee, 0xbe, 0x8f, 0xc2, 0xd1,
49. 0x80, 0xc2, 0x0d, 0x44, 0xa9, 0x59, 0x44, 0x59, 0x81, 0x3b, 0x5d, 0x4a, 0xde, 0xfb, 0xae, 0x24, 0xfc, 0xa3,
50. 0xd9, 0xbc, 0x57, 0x55, 0xc2, 0x26, 0xbc, 0x19, 0xa7, 0x9a, 0xc5, 0x59, 0xa3, 0xee, 0x5a, 0xef, 0x41, 0x80,
51. 0x7d, 0xf8, 0x5e, 0xc1, 0x1d, 0x32, 0x38, 0x41, 0x5b, 0xb6, 0x92, 0xb8, 0xb7, 0x03, 0x0d, 0x3e, 0x59, 0x0f,
52. 0x1c, 0xb3, 0xe1, 0x2a, 0x95, 0x1a, 0x3b, 0x50, 0x4f, 0xc4, 0x1d, 0xcf, 0x73, 0x7c, 0x14, 0xca, 0xe3, 0x0b,
53. 0xa7, 0xc7, 0x1a, 0x41, 0x4a, 0xee, 0xbe, 0x1f, 0x43, 0xdd, 0xf9, 0x01, 0x00, 0x01, 0x88, 0x4b, 0x82, 0xe7,
54. 0xe3, 0xe3, 0x99, 0x75, 0x6c, 0x9e, 0xaf, 0x17, 0x44, 0x3e, 0xd9, 0x07, 0xfd, 0x4b, 0xae, 0xce, 0x92, 0xc4,
55. 0x28, 0x44, 0x5e, 0x42, 0x79, 0x08, 0xb6, 0xc3, 0x7f, 0x58, 0x2d, 0xef, 0xac, 0x4a, 0x07, 0xcd, 0xaf, 0x46,
56. 0x8f, 0xb4, 0xc4, 0x43, 0xf9, 0xff, 0x5f, 0x74, 0x2d, 0xb5, 0xe0, 0x1c, 0xab, 0xf4, 0x6e, 0xd5, 0xdb, 0xc8,
57. 0x0c, 0xfb, 0x76, 0x3c, 0x38, 0x66, 0xf3, 0x7f, 0x01, 0x43, 0x7a, 0x30, 0x39, 0x02, 0x80, 0xa4, 0x11, 0xb3,
58. 0x04, 0xd9, 0xe3, 0x57, 0x23, 0xf4, 0x07, 0xfc, 0x91, 0x8a, 0xc6, 0xcc, 0xa2, 0x16, 0x29, 0xb3, 0xe5, 0x76,
59. 0x4a, 0xa8, 0x84, 0x19, 0xdc, 0xef, 0xfc, 0xb0, 0x63, 0x33, 0x0b, 0xfa, 0xf6, 0x68, 0x0b, 0x08, 0xea, 0x31,
60. 0x52, 0xee, 0x99, 0xef, 0x43, 0x2a, 0xbe, 0x97, 0xad, 0xb3, 0xb9, 0x66, 0x7a, 0xae, 0xe1, 0x8f, 0x57, 0x86,
61. 0xe5, 0xfe, 0x14, 0x3c, 0x81, 0xd0, 0x64, 0xf8, 0x86, 0x1a, 0x0b, 0x40, 0x58, 0xc9, 0x33, 0x49, 0xb8, 0x99,
62. 0xc6, 0x2e, 0x94, 0x70, 0xee, 0x09, 0x88, 0xe1, 0x5c, 0x4e, 0x6c, 0x22, 0x72, 0xa7, 0x2a, 0x21, 0xdd, 0xd7,
63. 0x1d, 0xfc, 0x63, 0x15, 0x0b, 0xde, 0x06, 0x9c, 0xf3, 0x28, 0xf3, 0xac, 0x4a, 0xa8, 0xb5, 0x50, 0xca, 0x9b,
64. 0xcc, 0x0a, 0x04, 0xfe, 0x3f, 0x98, 0x68, 0x81, 0xac, 0x24, 0x53, 0xea, 0x1f, 0x1c, 0x6e, 0x5e, 0xca, 0xe8,
65. 0x31, 0x0d, 0x08, 0x12, 0xf3, 0x26, 0xf8, 0x5e, 0xeb, 0x10, 0x27, 0xae, 0xaa, 0xc3, 0xad, 0x6c, 0xc1, 0x89,
66. 0xdb, 0x7d, 0x5a, 0x12, 0x55, 0xad, 0x11, 0x19, 0xa1, 0xa9, 0x8f, 0x0b, 0x6d, 0x78, 0x8d, 0x1c, 0xdf, 0xe5,
67. 0x63, 0x82, 0x0b, 0x7d, 0x23, 0x04, 0xb4, 0x75, 0x8c, 0xed, 0x77, 0xfc, 0x1a, 0x85, 0x29, 0x11, 0xe0, 0x61};
68. struct OH_Huks_Blob publicKey = {RSA_KEY_SIZE_1024, pubKey};
69. struct OH_Huks_ParamSet *testImportKeyParamSet = nullptr;
70. struct OH_Huks_Result ohResult;
71. do {
72. ohResult = InitParamSet(&testImportKeyParamSet, g_testImportKeyParam,
73. sizeof(g_testImportKeyParam) / sizeof(OH_Huks_Param));
74. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
75. break;
76. }
77. /* 导入密钥 */
78. char newKey[] = "test_rsa_import";
79. struct OH_Huks_Blob newKeyAlias = {.size = (uint32_t)strlen(newKey), .data = (uint8_t *)newKey};
80. ohResult = OH_Huks_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
81. } while (0);

83. OH_Huks_FreeParamSet(&testImportKeyParamSet);

85. napi_value ret;
86. napi_create_int32(env, ohResult.errorCode, &ret);
87. return ret;
88. }
```

[napi\_rsa2048.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/cpp/types/projects/napi_rsa2048.cpp#L16-L105)

### 导入X25519密钥公钥

```
1. /* 以下以明文导入X25519密钥为例 */
2. #include "huks/native_huks_api.h"
3. #include "huks/native_huks_param.h"
4. #include "napi/native_api.h"
5. #include <cstring>
6. #include "file.h"

8. #define X25519_KEY_SIZE_32 32

10. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
11. uint32_t paramCount)
12. {
13. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. return ret;
16. }
17. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
18. if (ret.errorCode != OH_HUKS_SUCCESS) {
19. OH_Huks_FreeParamSet(paramSet);
20. return ret;
21. }
22. ret = OH_Huks_BuildParamSet(paramSet);
23. if (ret.errorCode != OH_HUKS_SUCCESS) {
24. OH_Huks_FreeParamSet(paramSet);
25. return ret;
26. }
27. return ret;
28. }
29. static struct OH_Huks_Param g_testImportKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
30. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
31. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
32. {.tag = OH_HUKS_TAG_IMPORT_KEY_TYPE, .uint32Param = OH_HUKS_KEY_TYPE_PUBLIC_KEY},
33. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

35. napi_value ImportX25519Key(napi_env env, napi_callback_info info)
36. {
37. /* 公钥，用于后续导入密钥 */
38. uint8_t pubKey[X25519_KEY_SIZE_32] = {0x30, 0x2A, 0x30, 0x05, 0x06, 0x03, 0x2B, 0x65, 0x6E, 0x03, 0x21, 0x00,
39. 0xD2, 0x36, 0x9E, 0xCF, 0xF0, 0x61, 0x5B, 0x73, 0xCE, 0x4F, 0xF0, 0x40,
40. 0x2B, 0x89, 0x18, 0x3E, 0x06, 0x33, 0x60, 0xC6};
41. struct OH_Huks_Blob publicKey = {X25519_KEY_SIZE_32, pubKey};
42. struct OH_Huks_ParamSet *testImportKeyParamSet = nullptr;
43. struct OH_Huks_Result ohResult;
44. do {
45. ohResult = InitParamSet(&testImportKeyParamSet, g_testImportKeyParam,
46. sizeof(g_testImportKeyParam) / sizeof(OH_Huks_Param));
47. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
48. break;
49. }
50. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
51. break;
52. }
53. /* 导入密钥 */
54. char newKey[] = "test_X25519_import";
55. struct OH_Huks_Blob newKeyAlias = {.size = (uint32_t)strlen(newKey), .data = (uint8_t *)newKey};
56. ohResult = OH_Huks_ImportKeyItem(&newKeyAlias, testImportKeyParamSet, &publicKey);
57. } while (0);

59. OH_Huks_FreeParamSet(&testImportKeyParamSet);

61. napi_value ret;
62. napi_create_int32(env, ohResult.errorCode, &ret);
63. return ret;
64. }
```

[napi\_x25519.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportKeyPlainText/entry/src/main/cpp/types/projects/napi_x25519.cpp#L16-L81)
