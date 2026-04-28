---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-general-query-ndk
title: 通用查询(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 通用操作 > 通用查询(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bf2fd447d9445470a791b132ba41243b68bdc1c5ba9d95cbdee7e8abb13a2911
---

从API 22开始，huksExternalCrypto提供通用查询功能接口。从Ukey获取通用属性信息，完成属性查询操作。具体的场景介绍请参考[获取属性介绍及规格](huks-ukey-general-query-overview.md)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

## 开发步骤

**获取属性**

1. 构造resourceId和propertyId，先调用[OH\_Huks\_OpenResource](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_openresource)打开资源。
2. 初始化参数集：通过[OH\_Huks\_InitExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_initexternalcryptoparamset)、[OH\_Huks\_AddExternalCryptoParams](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_addexternalcryptoparams)、[OH\_Huks\_BuildExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_buildexternalcryptoparamset)构造参数集paramSet。
3. 调用[OH\_Huks\_GetProperty](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getproperty)获取属性信息。
4. 调用[OH\_Huks\_GetExternalCryptoParam](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_getexternalcryptoparam)从输出参数集中提取结果。
5. 调用[OH\_Huks\_FreeExternalCryptoParamSet](../harmonyos-references/capi-native-huks-external-crypto-api-h.md#oh_huks_freeexternalcryptoparamset)释放参数集资源。

## 开发案例

```
1. #include "huks/native_huks_external_crypto_api.h"
2. #include "huks/native_huks_external_crypto_type.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. OH_Huks_Result InitExternalCryptoParamSet(
7. OH_Huks_ExternalCryptoParamSet **paramSet,
8. const OH_Huks_ExternalCryptoParam *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitExternalCryptoParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddExternalCryptoParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeExternalCryptoParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildExternalCryptoParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeExternalCryptoParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }

28. static napi_value GetProperty(napi_env env, napi_callback_info info)
29. {
30. /* 1.假设已经打开了resourceId */
31. const char *resourceIdStr = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\","
32. "\"bundleName\":\"com.example.cryptoapplication\",\"index\":{\"key\":\"testKey\"}}";
33. const char *propertyIdStr = "SKF_GetDevInfo"; // 定义在GMT 0016-2023标准中的属性函数名称

35. struct OH_Huks_Blob resourceId = {
36. (uint32_t)strlen(resourceIdStr),
37. (uint8_t *)resourceIdStr
38. };
39. struct OH_Huks_Blob propertyId = {
40. (uint32_t)strlen(propertyIdStr),
41. (uint8_t *)propertyIdStr
42. };

44. /* 2.构造输入参数 */
45. OH_Huks_ExternalCryptoParam params[] = {};
46. OH_Huks_ExternalCryptoParamSet *paramSetIn = nullptr;
47. OH_Huks_ExternalCryptoParamSet *paramSetOut = nullptr;
48. OH_Huks_Result ohResult;

50. do {
51. /* 3.初始化并构建输入参数集 */
52. ohResult = InitExternalCryptoParamSet(&paramSetIn, params,
53. sizeof(params) / sizeof(OH_Huks_ExternalCryptoParam));
54. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
55. break;
56. }

58. /* 4.调用OH_Huks_GetProperty获取属性 */
59. ohResult = OH_Huks_GetProperty(&resourceId, &propertyId, paramSetIn, &paramSetOut);
60. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
61. break;
62. }

64. /* 5.从输出参数集中提取结果
65. * 输出参数集由函数内部分配，查询到的属性数据放在 OH_HUKS_EXT_CRYPTO_TAG_EXTRA_DATA TAG 中。
66. * 下面展示如何遍历返回的 params 并安全提取返回的属性字符串（示例）。
67. */
68. if (paramSetOut != nullptr && paramSetOut->paramsCnt > 0) {
69. for (uint32_t i = 0; i < paramSetOut->paramsCnt; i++) {
70. OH_Huks_ExternalCryptoParam *param = &paramSetOut->params[i];
71. /* 返回数据约定：GetProperty 的结果放在 OH_HUKS_EXT_CRYPTO_TAG_EXTRA_DATA TAG 中（示例使用 JSON 文本） */
72. if (param->tag == OH_HUKS_EXT_CRYPTO_TAG_EXTRA_DATA) {
73. /* 注意：param->blob.data 可能不是以 '\0' 结尾，需拷贝并手动添加终止符 */
74. char *outStr = (char *)malloc(param->blob.size + 1);
75. if (outStr != NULL) {
76. memcpy(outStr, param->blob.data, param->blob.size);
77. outStr[param->blob.size] = '\0';
78. // 解析 outStr（例如使用 JSON 解析库），示例：
79. // parse_json(outStr);
80. free(outStr);
81. }
82. }
83. }
84. }
85. } while (0);

87. /* 6.释放资源 */
88. OH_Huks_FreeExternalCryptoParamSet(&paramSetIn);
89. OH_Huks_FreeExternalCryptoParamSet(&paramSetOut);

91. napi_value ret;
92. napi_create_int32(env, ohResult.errorCode, &ret);
93. return ret;
94. }
```
