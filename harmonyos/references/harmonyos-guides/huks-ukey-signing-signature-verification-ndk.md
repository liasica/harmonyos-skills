---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-signing-signature-verification-ndk
title: 签名/验签(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 签名/验签 > 签名/验签(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:11c7765c4141dcd71bfa9761ee2fead6696ca140df7e6b7934d7e4e860849cd8
---

以密钥算法为RSA、摘要算法为SHA384、填充模式为PSS的密钥为例，完成签名、验签：

* [密钥算法为RSA、摘要算法为SHA384、填充模式为PSS](huks-ukey-signing-signature-verification-ndk.md#rsasha384pss)

具体的场景介绍及支持的算法规格，请参考[签名/验签介绍及算法规格](huks-ukey-signing-signature-verification-overview.md)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so libhuks_external_crypto.z.so)
```

## 开发步骤

**签名**

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，[打开资源](huks-open-close-resource-ndk.md#打开资源)后完成PIN码认证。
2. 指定待签名的明文数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置，并指定KeyClass参数，tag为[OH\_HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，值为[OH\_HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyclasstype)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取签名signature。

**验签**

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，然后[打开资源](huks-open-close-resource-ndk.md#打开资源)。
2. 获取待验证的签名。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置，并指定KeyClass参数，tag为[OH\_HUKS\_TAG\_KEY\_CLASS](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，值为[OH\_HUKS\_KEY\_CLASS\_EXTENSION](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_keyclasstype)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_UpdateSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_updatesession)更新密钥会话。
6. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，验证签名。

## 开发案例

### RSA/SHA384/PSS

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>

6. OH_Huks_Result InitParamSet(
7. struct OH_Huks_ParamSet **paramSet,
8. const struct OH_Huks_Param *params,
9. uint32_t paramCount)
10. {
11. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
12. if (ret.errorCode != OH_HUKS_SUCCESS) {
13. return ret;
14. }
15. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
16. if (ret.errorCode != OH_HUKS_SUCCESS) {
17. OH_Huks_FreeParamSet(paramSet);
18. return ret;
19. }
20. ret = OH_Huks_BuildParamSet(paramSet);
21. if (ret.errorCode != OH_HUKS_SUCCESS) {
22. OH_Huks_FreeParamSet(paramSet);
23. return ret;
24. }
25. return ret;
26. }

28. static struct OH_Huks_Param g_signParamsTest[] = {
29. {
30. .tag = OH_HUKS_TAG_ALGORITHM,
31. .uint32Param = OH_HUKS_ALG_RSA
32. }, {
33. .tag = OH_HUKS_TAG_PURPOSE,
34. .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN
35. }, {
36. .tag = OH_HUKS_TAG_KEY_SIZE,
37. .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048
38. }, {
39. .tag = OH_HUKS_TAG_PADDING,
40. .uint32Param = OH_HUKS_PADDING_PSS
41. }, {
42. .tag = OH_HUKS_TAG_DIGEST,
43. .uint32Param = OH_HUKS_DIGEST_SHA384
44. }, {
45. .tag = OH_HUKS_TAG_KEY_CLASS,
46. .uint32Param = OH_HUKS_KEY_CLASS_EXTENSION
47. }
48. };

50. static struct OH_Huks_Param g_verifyParamsTest[] = {
51. {
52. .tag = OH_HUKS_TAG_ALGORITHM,
53. .uint32Param = OH_HUKS_ALG_RSA
54. }, {
55. .tag = OH_HUKS_TAG_PURPOSE,
56. .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY
57. }, {
58. .tag = OH_HUKS_TAG_KEY_SIZE,
59. .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048
60. }, {
61. .tag = OH_HUKS_TAG_PADDING,
62. .uint32Param = OH_HUKS_PADDING_PSS
63. }, {
64. .tag = OH_HUKS_TAG_DIGEST,
65. .uint32Param = OH_HUKS_DIGEST_SHA384
66. }, {
67. .tag = OH_HUKS_TAG_KEY_CLASS,
68. .uint32Param = OH_HUKS_KEY_CLASS_EXTENSION
69. }
70. };

72. static const uint32_t RSA_COMMON_SIZE = 1024;
73. static const char *DATA_TO_SIGN = "Hks_RSA_Sign_Verify_Test_0000000000000000000000000000000000000000000000000000000"
74. "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
75. "0000000000000000000000000000000000000000000000000000000000000000000000000_string";
76. static const char *KEY_ALIAS = "{\"providerName\":\"testProviderName\",\"abilityName\":\"CryptoExtension\","
77. "\"bundleName\":\"com.example.cryptoapplication\",\"index\":{\"key\":\"testKey\"}}";

79. static napi_value SignVerifyKey(napi_env env, napi_callback_info info)
80. {
81. // 假设keyAlias是获取的resourceId
82. struct OH_Huks_Blob keyAlias = {
83. (uint32_t)strlen(KEY_ALIAS),
84. (uint8_t *)KEY_ALIAS
85. };
86. struct OH_Huks_Blob inData = {
87. (uint32_t)strlen(DATA_TO_SIGN),
88. (uint8_t *)DATA_TO_SIGN
89. };
90. struct OH_Huks_ParamSet *signParamSet = nullptr;
91. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
92. OH_Huks_Result ohResult;
93. do {
94. ohResult = InitParamSet(&signParamSet, g_signParamsTest, sizeof(g_signParamsTest) / sizeof(OH_Huks_Param));
95. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
96. break;
97. }
98. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsTest,
99. sizeof(g_verifyParamsTest) / sizeof(OH_Huks_Param));
100. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
101. break;
102. }
103. /* 1. Sign */
104. // Init
105. uint8_t handleS[sizeof(uint64_t)] = {0};
106. struct OH_Huks_Blob handleSign = { (uint32_t)sizeof(uint64_t), handleS };
107. ohResult = OH_Huks_InitSession(&keyAlias, signParamSet, &handleSign, nullptr);
108. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
109. break;
110. }
111. // Finish
112. uint8_t outDataS[RSA_COMMON_SIZE] = {0};
113. struct OH_Huks_Blob outDataSign = { RSA_COMMON_SIZE, outDataS };
114. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet,  &inData, &outDataSign);
115. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
116. break;
117. }

119. /* 2. Verify */
120. // Init
121. uint8_t handleV[sizeof(uint64_t)] = {0};
122. struct OH_Huks_Blob handleVerify = { (uint32_t)sizeof(uint64_t), handleV };
123. ohResult = OH_Huks_InitSession(&keyAlias, verifyParamSet, &handleVerify, nullptr);
124. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
125. break;
126. }
127. // Update loop
128. uint8_t temp[] = "out";
129. struct OH_Huks_Blob verifyOut = { (uint32_t)sizeof(temp), temp };
130. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, &inData, &verifyOut);
131. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
132. break;
133. }
134. // Finish
135. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, &outDataSign, &verifyOut);
136. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
137. break;
138. }
139. } while (0);
140. OH_Huks_FreeParamSet(&signParamSet);
141. OH_Huks_FreeParamSet(&verifyParamSet);

143. napi_value ret;
144. napi_create_int32(env, ohResult.errorCode, &ret);
145. return ret;
146. }
```
