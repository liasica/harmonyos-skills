---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-ndk
title: 查询密钥别名集(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 查询密钥别名集 > 查询密钥别名集(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:126bfceea72ab4a2b765769128ec14d5a01916f0577fcb6098d3589366cd2fa9
---

HUKS提供了接口供应用查询密钥别名集。

说明

轻量级智能穿戴不支持查询密钥别名集功能。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 初始化密钥属性集。用于查询指定密钥别名集TAG，TAG仅支持[OH\_HUKS\_TAG\_AUTH\_STORAGE\_LEVEL](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
2. 调用接口[OH\_Huks\_ListAliases](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_listaliases)，查询密钥别名集。

```
1. /* 以下查询密钥别名集为例 */
2. #include "huks/native_huks_api.h"
3. #include "huks/native_huks_param.h"
4. #include "napi/native_api.h"
5. #include <string.h>

7. OH_Huks_Result InitParamSet(
8. struct OH_Huks_ParamSet **paramSet,
9. const struct OH_Huks_Param *params,
10. uint32_t paramCount)
11. {
12. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
13. if (ret.errorCode != OH_HUKS_SUCCESS) {
14. return ret;
15. }
16. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
17. if (ret.errorCode != OH_HUKS_SUCCESS) {
18. OH_Huks_FreeParamSet(paramSet);
19. return ret;
20. }
21. ret = OH_Huks_BuildParamSet(paramSet);
22. if (ret.errorCode != OH_HUKS_SUCCESS) {
23. OH_Huks_FreeParamSet(paramSet);
24. return ret;
25. }
26. return ret;
27. }

29. struct OH_Huks_Param g_testQueryParam[] = {
30. {
31. .tag = OH_HUKS_TAG_AUTH_STORAGE_LEVEL,
32. .uint32Param = OH_HUKS_AUTH_STORAGE_LEVEL_DE
33. },
34. };

36. static napi_value ListAliases(napi_env env, napi_callback_info info)
37. {
38. struct OH_Huks_ParamSet *testQueryParamSet = nullptr;
39. struct OH_Huks_KeyAliasSet *outData = nullptr;
40. struct OH_Huks_Result ohResult;
41. do {
42. /* 1.初始化密钥属性集 */
43. ohResult = InitParamSet(&testQueryParamSet, g_testQueryParam,
44. sizeof(g_testQueryParam) / sizeof(OH_Huks_Param));
45. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
46. break;
47. }
48. /* 2.查询密钥别名集 */
49. ohResult = OH_Huks_ListAliases(testQueryParamSet, &outData);
50. } while (0);

52. OH_Huks_FreeParamSet(&testQueryParamSet);
53. OH_Huks_FreeKeyAliasSet(outData);
54. napi_value ret;
55. napi_create_int32(env, ohResult.errorCode, &ret);
56. return ret;
57. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/OtherOperations/QueryKeyAliasSet/entry/src/main/cpp/napi_init.cpp#L16-L74)
