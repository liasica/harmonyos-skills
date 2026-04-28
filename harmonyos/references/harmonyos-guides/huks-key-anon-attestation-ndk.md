---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-anon-attestation-ndk
title: 匿名密钥证明(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥证明 > 匿名密钥证明(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e98f727e5d80e3ccf7199e5978b0011b64059bbde2f8f372edb8a24f34d7a74
---

在使用本功能时，需确保网络通畅。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化参数集：通过[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)、[OH\_Huks\_AddParams](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_addparams)、[OH\_Huks\_BuildParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_buildparamset)构造参数集paramSet，参数集中必须包含[OH\_Huks\_KeyAlg](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyalg)，[OH\_Huks\_KeySize](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keysize)，[OH\_Huks\_KeyPurpose](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keypurpose)属性。
3. 将密钥别名与参数集作为参数传入[OH\_Huks\_AnonAttestKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_anonattestkeyitem)方法中，即可证明密钥。

## 开发案例

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

26. static uint32_t g_size = 4096;
27. static uint32_t CERT_COUNT = 4;
28. void FreeCertChain(struct OH_Huks_CertChain *certChain, const uint32_t pos)
29. {
30. if (certChain == nullptr || certChain->certs == nullptr) {
31. return;
32. }
33. for (uint32_t j = 0; j < pos; j++) {
34. if (certChain->certs[j].data != nullptr) {
35. free(certChain->certs[j].data);
36. certChain->certs[j].data = nullptr;
37. }
38. }
39. if (certChain->certs != nullptr) {
40. free(certChain->certs);
41. certChain->certs = nullptr;
42. }
43. }

45. int32_t ConstructDataToCertChain(struct OH_Huks_CertChain *certChain)
46. {
47. if (certChain == nullptr) {
48. return OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT;
49. }
50. certChain->certsCount = CERT_COUNT;

52. certChain->certs = (struct OH_Huks_Blob *)malloc(sizeof(struct OH_Huks_Blob) * (certChain->certsCount));
53. if (certChain->certs == nullptr) {
54. return OH_HUKS_ERR_CODE_INTERNAL_ERROR;
55. }
56. for (uint32_t i = 0; i < certChain->certsCount; i++) {
57. certChain->certs[i].size = g_size;
58. certChain->certs[i].data = (uint8_t *)malloc(certChain->certs[i].size);
59. if (certChain->certs[i].data == nullptr) {
60. FreeCertChain(certChain, i);
61. return OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT;
62. }
63. }
64. return 0;
65. }

67. static struct OH_Huks_Param g_genAnonAttestParams[] = {
68. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
69. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
70. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
71. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
72. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
73. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
74. };

76. #define CHALLENGE_DATA "hi_challenge_data"
77. static struct OH_Huks_Blob g_challenge = {sizeof(CHALLENGE_DATA), (uint8_t *)CHALLENGE_DATA};
78. static napi_value AnonAttestKey(napi_env env, napi_callback_info info)
79. {
80. /* 1.确定密钥别名 */
81. struct OH_Huks_Blob genAlias = {(uint32_t)strlen("test_anon_attest"), (uint8_t *)"test_anon_attest"};
82. static struct OH_Huks_Param g_anonAttestParams[] = {
83. {.tag = OH_HUKS_TAG_ATTESTATION_CHALLENGE, .blob = g_challenge},
84. {.tag = OH_HUKS_TAG_ATTESTATION_ID_ALIAS, .blob = genAlias},
85. };
86. struct OH_Huks_ParamSet *genParamSet = nullptr;
87. struct OH_Huks_ParamSet *anonAttestParamSet = nullptr;
88. OH_Huks_Result ohResult;
89. OH_Huks_Blob certs = {0};
90. OH_Huks_CertChain certChain = {&certs, 0};
91. do {
92. /* 2.初始化密钥参数集 */
93. ohResult =
94. InitParamSet(&genParamSet, g_genAnonAttestParams, sizeof(g_genAnonAttestParams) / sizeof(OH_Huks_Param));
95. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
96. break;
97. }
98. ohResult =
99. InitParamSet(&anonAttestParamSet, g_anonAttestParams, sizeof(g_anonAttestParams) / sizeof(OH_Huks_Param));
100. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
101. break;
102. }
103. ohResult = OH_Huks_GenerateKeyItem(&genAlias, genParamSet, nullptr);
104. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
105. break;
106. }

108. (void)ConstructDataToCertChain(&certChain);
109. /* 3.证明密钥 */
110. ohResult = OH_Huks_AnonAttestKeyItem(&genAlias, anonAttestParamSet, &certChain);
111. } while (0);
112. FreeCertChain(&certChain, CERT_COUNT);
113. OH_Huks_FreeParamSet(&genParamSet);
114. OH_Huks_FreeParamSet(&anonAttestParamSet);
115. (void)OH_Huks_DeleteKeyItem(&genAlias, NULL);

117. napi_value ret;
118. napi_create_int32(env, ohResult.errorCode, &ret);
119. return ret;
120. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/AnonymousKeyProof/entry/src/main/cpp/napi_init.cpp#L15-L136)
