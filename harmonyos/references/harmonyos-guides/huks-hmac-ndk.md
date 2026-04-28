---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-ndk
title: HMAC(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > HMAC > HMAC(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef01838522baa78a3c27e307e18f97ab4987d4607238a708f5daffb8f05d8352
---

HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code）。具体的场景介绍及支持的算法规格，请参考[HMAC介绍及算法规格](huks-hmac-overview.md)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，HMAC支持的规格请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行HMAC**

1. 获取密钥别名。
2. 获取待运算的数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取哈希后的数据。

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

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

26. static struct OH_Huks_Param g_genHmacParams[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_HMAC},
27. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_MAC},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
29. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA384}};

31. static const uint32_t HMAC_COMMON_SIZE = 1024;
32. OH_Huks_Result HksHmacTest(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *hmacParamSet,
33. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *hashText)
34. {
35. uint8_t handleE[sizeof(uint64_t)] = {0};
36. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleE};
37. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, hmacParamSet, &handle, nullptr);
38. if (ret.errorCode != OH_HUKS_SUCCESS) {
39. return ret;
40. }
41. ret = OH_Huks_FinishSession(&handle, hmacParamSet, inData, hashText);
42. return ret;
43. }

45. static napi_value HmacKey(napi_env env, napi_callback_info info)
46. {
47. char tmpKeyAlias[] = "test_hmac";
48. struct OH_Huks_Blob keyAlias = {(uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias};
49. struct OH_Huks_ParamSet *hmacParamSet = nullptr;
50. OH_Huks_Result ohResult;

52. do {
53. ohResult = InitParamSet(&hmacParamSet, g_genHmacParams, sizeof(g_genHmacParams) / sizeof(OH_Huks_Param));
54. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
55. break;
56. }

58. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, hmacParamSet, nullptr);
59. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
60. break;
61. }

63. char tmpInData[] = "HMAC_MAC_INDATA_1";
64. struct OH_Huks_Blob inData = {(uint32_t)strlen(tmpInData), (uint8_t *)tmpInData};
65. uint8_t cipher[HMAC_COMMON_SIZE] = {0};
66. struct OH_Huks_Blob hashText = {HMAC_COMMON_SIZE, cipher};

68. ohResult = HksHmacTest(&keyAlias, hmacParamSet, &inData, &hashText);
69. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
70. break;
71. }
72. } while (0);

74. OH_Huks_FreeParamSet(&hmacParamSet);
75. napi_value ret;
76. napi_create_int32(env, ohResult.errorCode, &ret);
77. return ret;
78. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/HMAC/entry/src/main/cpp/napi_init.cpp#L16-L95)
