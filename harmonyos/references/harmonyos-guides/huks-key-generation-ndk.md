---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-generation-ndk
title: 生成密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥生成 > 生成密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bae43452d31af6d03b97306faceb1e58cf99882602921801ffb57ad0d2b1bee
---

以ECC算法为例，生成随机密钥。具体的场景介绍及支持的算法规格，请参考[密钥生成支持的算法](huks-key-generation-overview.md#支持的算法)。

注意

密钥别名中禁止包含个人数据等敏感信息。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。通过[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)、[OH\_Huks\_AddParams](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_addparams)、[OH\_Huks\_BuildParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_buildparamset)构造密钥属性集paramSet。

   密钥属性集中必须包含[OH\_Huks\_KeyAlg](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyalg)、[OH\_Huks\_KeySize](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keysize)、[OH\_Huks\_KeyPurpose](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keypurpose)属性。注：一个密钥只能有一类PURPOSE，并且，生成密钥时指定的用途要与使用时的方式一致，否则会导致异常。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)，传入密钥别名和密钥属性集，生成密钥。

说明

如果业务再次使用相同别名调用HUKS生成密钥，HUKS将生成新密钥并直接覆盖历史的密钥文件。

```
1. /* 以下以生成ECC密钥为例 */
2. #include "huks/native_huks_api.h"
3. #include "huks/native_huks_param.h"
4. #include "napi/native_api.h"
5. #include <cstring>

7. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
8. uint32_t paramCount)
9. {
10. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
11. if (ret.errorCode != OH_HUKS_SUCCESS) {
12. return ret;
13. }
14. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
15. if (ret.errorCode != OH_HUKS_SUCCESS) {
16. OH_Huks_FreeParamSet(paramSet);
17. return ret;
18. }
19. ret = OH_Huks_BuildParamSet(paramSet);
20. if (ret.errorCode != OH_HUKS_SUCCESS) {
21. OH_Huks_FreeParamSet(paramSet);
22. return ret;
23. }
24. return ret;
25. }

27. struct OH_Huks_Param g_testGenerateKeyParam[] = {{.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
28. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
29. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
30. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}};

32. static napi_value GenerateKey(napi_env env, napi_callback_info info)
33. {
34. /* 1.确定密钥别名 */
35. const char *alias = "test_generate";
36. struct OH_Huks_Blob aliasBlob = {.size = (uint32_t)strlen(alias), .data = (uint8_t *)alias};
37. struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
38. struct OH_Huks_Result ohResult;
39. do {
40. /* 2.初始化密钥属性集 */
41. ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
42. sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
43. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
44. break;
45. }
46. /* 3.生成密钥 */
47. ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
48. } while (0);
49. OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
50. napi_value ret;
51. napi_create_int32(env, ohResult.errorCode, &ret);
52. return ret;
53. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/GenerateKey/entry/src/main/cpp/napi_init.cpp#L16-L70)
