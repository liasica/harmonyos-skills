---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-cmac-native
title: CMAC(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > CMAC > CMAC(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea8752e2a72d59192abcc2c3596aea1d56a1bcd2b7b770401aecd7e6cfd9707e
---

CMAC是基于对称密钥分组加密算法的消息认证码（Cipher-based Message Authentication Code），目前支持3DES加密算法的消息认证方法。

说明

仅支持在智能穿戴设备（Wearable）使用。

## 开发步骤

**生成密钥**

1. 获取生成密钥算法参数配置。
2. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，支持的规格是128比特长度的密钥。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md#支持的算法)的规格介绍，导入已有的密钥。

**执行CMAC**

1. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)获取算法参数配置。
2. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)和[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)计算MAC值。

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "huks/native_huks_type.h"
4. #include "napi/native_api.h"
5. #include <string.h>

7. static const uint32_t CMAC_COMMON_SIZE = 8;
8. static const uint32_t IV_SIZE = 8;
9. static uint8_t IV[IV_SIZE] = { 0 };

11. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params, uint32_t paramCount)
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

30. static struct OH_Huks_Param g_genParams[] = {
31. {
32. .tag = OH_HUKS_TAG_ALGORITHM,
33. .uint32Param = OH_HUKS_ALG_3DES
34. }, {
35. .tag = OH_HUKS_TAG_KEY_SIZE,
36. .uint32Param = OH_HUKS_3DES_KEY_SIZE_128
37. }, {
38. .tag = OH_HUKS_TAG_PURPOSE,
39. .uint32Param = OH_HUKS_KEY_PURPOSE_MAC
40. }
41. };

43. static struct OH_Huks_Param g_cmacParams[] = {
44. {
45. .tag = OH_HUKS_TAG_ALGORITHM,
46. .uint32Param = OH_HUKS_ALG_CMAC
47. }, {
48. .tag = OH_HUKS_TAG_KEY_SIZE,
49. .uint32Param = OH_HUKS_3DES_KEY_SIZE_128
50. }, {
51. .tag = OH_HUKS_TAG_PURPOSE,
52. .uint32Param = OH_HUKS_KEY_PURPOSE_MAC
53. }, {
54. .tag = OH_HUKS_TAG_BLOCK_MODE,
55. .uint32Param = OH_HUKS_MODE_CBC
56. }, {
57. .tag = OH_HUKS_TAG_PADDING,
58. .uint32Param = OH_HUKS_PADDING_ISO_IEC_9797_1
59. }, {
60. .tag = OH_HUKS_TAG_IV,
61. .blob = {
62. .size = IV_SIZE,
63. .data = (uint8_t *)IV
64. }
65. }
66. };

68. OH_Huks_Result HksCmacTest(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *cmacParamSet,
69. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
70. {
71. uint8_t handleE[sizeof(uint64_t)] = {0};
72. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleE};
73. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, cmacParamSet, &handle, nullptr);
74. if (ret.errorCode != OH_HUKS_SUCCESS) {
75. return ret;
76. }
77. ret = OH_Huks_FinishSession(&handle, cmacParamSet, inData, outData);
78. return ret;
79. }

81. static napi_value CmacKey(napi_env env, napi_callback_info info)
82. {
83. char tmpKeyAlias[] = "test_cmac";
84. struct OH_Huks_Blob keyAlias = { (uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias };
85. struct OH_Huks_ParamSet *genParamSet = nullptr;
86. struct OH_Huks_ParamSet *cmacParamSet = nullptr;
87. OH_Huks_Result ohResult;
88. do {
89. /*       * 1.1 获取生成密钥算法参数配置       */
90. ohResult = InitParamSet(&genParamSet, g_genParams, sizeof(g_genParams) / sizeof(OH_Huks_Param));
91. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
92. break;
93. }
94. /*               * 1.2 调用OH_Huks_GenerateKeyItem        */
95. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
96. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
97. break;
98. }
99. /*        * 2.1. 获取CMAC算法参数配置        */
100. char tmpInData[] = "CMAC_INDATA";
101. struct OH_Huks_Blob inData = { (uint32_t)strlen(tmpInData), (uint8_t *)tmpInData };
102. uint8_t mac[CMAC_COMMON_SIZE] = { 0 };
103. struct OH_Huks_Blob macData= {CMAC_COMMON_SIZE, mac};
104. ohResult = InitParamSet(&cmacParamSet, g_cmacParams, sizeof(g_cmacParams) / sizeof(OH_Huks_Param));
105. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
106. break;
107. }
108. /*        * 2.2 调用initSession和finishSession计算MAC        */
109. ohResult = HksCmacTest(&keyAlias, cmacParamSet, &inData, &macData);
110. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
111. break;
112. }
113. } while (0);
114. OH_Huks_FreeParamSet(&genParamSet);
115. OH_Huks_FreeParamSet(&cmacParamSet);

117. napi_value ret;
118. napi_create_int32(env, ohResult.errorCode, &ret);
119. return ret;
120. }
```
