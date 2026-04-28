---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-export-key-ndk
title: 密钥导出(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 密钥导出 > 密钥导出(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e23eff7ef8af4f02e95a422c8e7d93581dfd57c49dffc6f1f84c6f2bf489ef26
---

业务需要获取持久化存储的非对称密钥的公钥时使用，当前支持ECC/RSA/ED25519/X25519/SM2的公钥导出。

说明

轻量级智能穿戴仅支持RSA公钥导出。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 构造对应参数。

   * keyAlias：密钥别名，封装成[OH\_Huks\_Blob](../harmonyos-references/capi-hukstypeapi-oh-huks-blob.md)结构，密钥别名最大长度为128字节。
   * paramSetIn：预留参数，暂不需要处理，传空即可。
   * key：用于放置导出的公钥，为[OH\_Huks\_Blob](../harmonyos-references/capi-hukstypeapi-oh-huks-blob.md)类型对象，需要业务提前申请好内存，需申请足够容纳获取到的密钥属性集的内存大小。
2. 调用接口[OH\_Huks\_GetKeyItemParamSet](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_getkeyitemparamset)，传入上述参数。
3. 返回值为成功码/错误码，导出公钥以标准的X.509规范的DER格式封装在参数key中，具体请参考[公钥材料格式](huks-concepts.md#公钥材料格式)。

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>
5. /* 以下以生成ECC密钥为例 */
6. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
7. uint32_t paramCount)
8. {
9. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
10. if (ret.errorCode != OH_HUKS_SUCCESS) {
11. return ret;
12. }
13. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
14. if (ret.errorCode != OH_HUKS_SUCCESS) {
15. OH_Huks_FreeParamSet(paramSet);
16. return ret;
17. }
18. ret = OH_Huks_BuildParamSet(paramSet);
19. if (ret.errorCode != OH_HUKS_SUCCESS) {
20. OH_Huks_FreeParamSet(paramSet);
21. return ret;
22. }
23. return ret;
24. }

26. struct OH_Huks_Param g_testGenerateKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
27. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
29. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

31. static OH_Huks_Result GenerateKeyHelper(const char *alias)
32. {
33. struct OH_Huks_Blob aliasBlob = {.size = (uint32_t)strlen(alias), .data = (uint8_t *)alias};
34. struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
35. struct OH_Huks_Result ohResult;
36. do {
37. /* 1.初始化密钥属性集 */
38. ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
39. sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
40. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
41. break;
42. }
43. /* 2.生成密钥 */
44. ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
45. } while (0);
46. OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
47. return ohResult;
48. }

50. static napi_value ExportKey(napi_env env, napi_callback_info info)
51. {
52. /* 1. 参数构造：确定密钥别名 */
53. const char *alias = "test_key";
54. struct OH_Huks_Blob aliasBlob = { .size = (uint32_t)strlen(alias), .data = (uint8_t *)alias };
55. /* 生成密钥 */
56. OH_Huks_Result genResult = GenerateKeyHelper(alias);
57. if (genResult.errorCode != OH_HUKS_SUCCESS) {
58. napi_value ret;
59. napi_create_int32(env, genResult.errorCode, &ret);
60. return ret;
61. }
62. /* 构造参数：为待导出公钥申请内存 */
63. uint8_t *pubKey = (uint8_t *)malloc(512); // 请业务按实际密钥大小评估申请
64. if (pubKey == nullptr) {
65. return nullptr;
66. }
67. struct OH_Huks_Blob keyBlob = { 256, pubKey };
68. struct OH_Huks_Result ohResult;
69. do {
70. ohResult = OH_Huks_ExportPublicKeyItem(&aliasBlob, nullptr, &keyBlob);
71. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
72. break;
73. }
74. } while (0);
75. free(pubKey);
76. napi_value ret;
77. napi_create_int32(env, ohResult.errorCode, &ret);
78. return ret;
79. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/KeyExport/entry/src/main/cpp/napi_init.cpp#L16-L98)
