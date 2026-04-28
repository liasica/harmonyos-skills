---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-ndk
title: 签名/验签(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 签名/验签 > 签名/验签(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0528029971cfe38de9d646bba919f085f55407a63ac98ee4e5c2e0b35a4eb7e0
---

当前指导提供以下示例，供开发者参考完成签名、验签开发：

* 密钥算法为ECC256、摘要算法为SHA256，请见开发案例：[ECC256/SHA256](huks-signing-signature-verification-ndk.md#ecc256sha256)
* 密钥算法为SM2、摘要算法为SM3，请见开发案例：[SM2/SM3](huks-signing-signature-verification-ndk.md#sm2sm3)
* 密钥算法为SM2、摘要算法为NoDigest，请见开发案例：[SM2/NoDigest](huks-signing-signature-verification-ndk.md#sm2nodigest)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PSS，请见开发案例：[RSA/SHA256/PSS](huks-signing-signature-verification-ndk.md#rsasha256pss)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PKCS1\_V1\_5，请见开发案例：[RSA/SHA256/PKCS1\_V1\_5](huks-signing-signature-verification-ndk.md#rsasha256pkcs1_v1_5)
* 密钥算法为RSA、摘要算法为SHA384、填充模式为PSS，请见开发案例：[RSA/SHA384/PSS](huks-signing-signature-verification-ndk.md#rsasha384pss)

具体的场景介绍及支持的算法规格，请参考[签名/验签支持的算法](huks-signing-signature-verification-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**签名**

1. 获取密钥别名。
2. 指定待签名的明文数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取签名signature。

**验签**

1. 获取密钥别名。
2. 获取待验证的签名signature。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_UpdateSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_updatesession)更新密钥会话。
6. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，验证签名。

**删除密钥**

当密钥废弃不用时，需要调用[OH\_Huks\_DeleteKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

## 开发案例

### ECC256/SHA256

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsTestECC[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
28. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
29. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
30. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
31. };

33. static struct OH_Huks_Param g_signParamsTestECC[] = {
34. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
35. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
37. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};

39. static struct OH_Huks_Param g_verifyParamsTestECC[] = {
40. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_ECC},
41. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
42. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_ECC_KEY_SIZE_256},
43. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}};

45. static const uint32_t ECC_COMMON_SIZE = 256;
46. static const char *DATA_TO_SIGN_ECC = "Hks_ECC_Sign_Verify_Test_0000000000000000000000000000000000000000000000000000000"
47. "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
48. "00000000000000000000000000000000000000000000000000"
49. "00000000000000000000000_string";

51. /* 1. 生成密钥 */
52. static OH_Huks_Result GenerateKeyECC(const struct OH_Huks_Blob *keyAlias,
53. const struct OH_Huks_ParamSet *genParamSet)
54. {
55. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
56. }

58. /* 2. 签名 */
59. static OH_Huks_Result SignDataECC(const struct OH_Huks_Blob *keyAlias,
60. const struct OH_Huks_ParamSet *signParamSet,
61. const struct OH_Huks_Blob *inData,
62. struct OH_Huks_Blob *outDataSign)
63. {
64. uint8_t handleS[sizeof(uint64_t)] = {0};
65. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

67. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
68. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
69. return ohResult;
70. }

72. ohResult = OH_Huks_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
73. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
74. return ohResult;
75. }

77. struct OH_Huks_Blob finishInData = {0, NULL};
78. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);

80. return ohResult;
81. }

83. /* 3. 验签 */
84. static OH_Huks_Result VerifySignatureECC(const struct OH_Huks_Blob *keyAlias,
85. const struct OH_Huks_ParamSet *verifyParamSet,
86. const struct OH_Huks_Blob *inData,
87. const struct OH_Huks_Blob *signature)
88. {
89. uint8_t handleV[sizeof(uint64_t)] = {0};
90. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

92. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
93. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
94. return ohResult;
95. }

97. uint8_t temp[] = "out";
98. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
99. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
100. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
101. return ohResult;
102. }

104. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

106. return ohResult;
107. }

109. napi_value SignVerifyKeyECC(napi_env env, napi_callback_info info)
110. {
111. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_ECC"), (uint8_t *)"test_signVerify_ECC"};
112. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_ECC), (uint8_t *)DATA_TO_SIGN_ECC};
113. struct OH_Huks_ParamSet *genParamSet = nullptr;
114. struct OH_Huks_ParamSet *signParamSet = nullptr;
115. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
116. OH_Huks_Result ohResult;

118. do {
119. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsTestECC,
120. sizeof(g_genSignVerifyParamsTestECC) / sizeof(OH_Huks_Param));
121. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
122. break;
123. }

125. ohResult = InitParamSet(&signParamSet, g_signParamsTestECC,
126. sizeof(g_signParamsTestECC) / sizeof(OH_Huks_Param));
127. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
128. break;
129. }

131. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsTestECC,
132. sizeof(g_verifyParamsTestECC) / sizeof(OH_Huks_Param));
133. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
134. break;
135. }

137. /* 1. 生成密钥 */
138. ohResult = GenerateKeyECC(&g_keyAlias, genParamSet);
139. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
140. break;
141. }

143. /* 2. 签名 */
144. uint8_t outDataS[ECC_COMMON_SIZE] = {0};
145. struct OH_Huks_Blob outDataSign = {ECC_COMMON_SIZE, outDataS};
146. ohResult = SignDataECC(&g_keyAlias, signParamSet, &inData, &outDataSign);
147. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
148. break;
149. }

151. /* 3. 验签 */
152. ohResult = VerifySignatureECC(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
153. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
154. break;
155. }
156. } while (0);

158. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
159. OH_Huks_FreeParamSet(&genParamSet);
160. OH_Huks_FreeParamSet(&signParamSet);
161. OH_Huks_FreeParamSet(&verifyParamSet);

163. napi_value ret;
164. napi_create_int32(env, ohResult.errorCode, &ret);
165. return ret;
166. }
```

[ecc\_sha256\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/ecc_sha256_sign_verify.cpp#L16-L183)

### SM2/SM3

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsSM2[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
29. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
30. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3},
31. };

33. static struct OH_Huks_Param g_signParamsSM2[] = {
34. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
35. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
36. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN},
37. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3}
38. };

40. static struct OH_Huks_Param g_verifyParamsSM2[] = {
41. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
42. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
43. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
44. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3}
45. };

47. static const uint32_t SM2_COMMON_SIZE = 256;
48. static const char *DATA_TO_SIGN_SM2 = "Hks_SM2_Sign_Verify_Test_0000000000000000000000000000000000000000000000000000000"
49. "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
50. "0000000000000000000000000000000000000000000000000"
51. "000000000000000000000000_string";

53. /* 1. 生成密钥 */
54. static OH_Huks_Result GenerateKeySM2(const struct OH_Huks_Blob *keyAlias,
55. const struct OH_Huks_ParamSet *genParamSet)
56. {
57. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
58. }

60. /* 2. 签名 */
61. static OH_Huks_Result SignDataSM2(const struct OH_Huks_Blob *keyAlias,
62. const struct OH_Huks_ParamSet *signParamSet,
63. const struct OH_Huks_Blob *inData,
64. struct OH_Huks_Blob *outDataSign)
65. {
66. uint8_t handleS[sizeof(uint64_t)] = {0};
67. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

69. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
70. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
71. return ohResult;
72. }

74. ohResult = OH_Huks_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
75. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
76. return ohResult;
77. }

79. struct OH_Huks_Blob finishInData = {0, NULL};
80. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);

82. return ohResult;
83. }

85. /* 3. 验签 */
86. static OH_Huks_Result VerifySignatureSM2(const struct OH_Huks_Blob *keyAlias,
87. const struct OH_Huks_ParamSet *verifyParamSet,
88. const struct OH_Huks_Blob *inData,
89. const struct OH_Huks_Blob *signature)
90. {
91. uint8_t handleV[sizeof(uint64_t)] = {0};
92. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

94. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
95. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
96. return ohResult;
97. }

99. uint8_t temp[] = "out";
100. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
101. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
102. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
103. return ohResult;
104. }

106. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

108. return ohResult;
109. }

111. napi_value SignVerifyKeySM2SM3(napi_env env, napi_callback_info info)
112. {
113. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_SM2_SM3"),
114. (uint8_t *)"test_signVerify_SM2_SM3"};
115. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_SM2), (uint8_t *)DATA_TO_SIGN_SM2};
116. struct OH_Huks_ParamSet *genParamSet = nullptr;
117. struct OH_Huks_ParamSet *signParamSet = nullptr;
118. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
119. OH_Huks_Result ohResult;

121. do {
122. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsSM2,
123. sizeof(g_genSignVerifyParamsSM2) / sizeof(OH_Huks_Param));
124. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
125. break;
126. }

128. ohResult = InitParamSet(&signParamSet, g_signParamsSM2,
129. sizeof(g_signParamsSM2) / sizeof(OH_Huks_Param));
130. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
131. break;
132. }

134. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsSM2,
135. sizeof(g_verifyParamsSM2) / sizeof(OH_Huks_Param));
136. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
137. break;
138. }

140. /* 1. 生成密钥 */
141. ohResult = GenerateKeySM2(&g_keyAlias, genParamSet);
142. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
143. break;
144. }

146. /* 2. 签名 */
147. uint8_t outDataS[SM2_COMMON_SIZE] = {0};
148. struct OH_Huks_Blob outDataSign = {SM2_COMMON_SIZE, outDataS};
149. ohResult = SignDataSM2(&g_keyAlias, signParamSet, &inData, &outDataSign);
150. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
151. break;
152. }

154. /* 3. 验签 */
155. ohResult = VerifySignatureSM2(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
156. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
157. break;
158. }
159. } while (0);

161. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
162. OH_Huks_FreeParamSet(&genParamSet);
163. OH_Huks_FreeParamSet(&signParamSet);
164. OH_Huks_FreeParamSet(&verifyParamSet);

166. napi_value ret;
167. napi_create_int32(env, ohResult.errorCode, &ret);
168. return ret;
169. }
```

[sm2\_sm3\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/sm2_sm3_sign_verify.cpp#L16-L186)

### SM2/NoDigest

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsSM2NoDigest[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
29. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
30. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
31. };

33. static struct OH_Huks_Param g_signParamsSM2NoDigest[] = {
34. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
35. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
36. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN},
37. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}
38. };

40. static struct OH_Huks_Param g_verifyParamsSM2NoDigest[] = {
41. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
42. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
43. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
44. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE}
45. };

47. static const uint32_t SM2_COMMON_SIZE = 256;
48. static const char *DATA_TO_SIGN_SM2_NODIGEST = "12345678901234567890123456789012";

50. /* 1. 生成密钥 */
51. static OH_Huks_Result GenerateKeySM2(const struct OH_Huks_Blob *keyAlias,
52. const struct OH_Huks_ParamSet *genParamSet)
53. {
54. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
55. }

57. /* 2. 签名 */
58. static OH_Huks_Result SignDataSM2NoDigest(const struct OH_Huks_Blob *keyAlias,
59. const struct OH_Huks_ParamSet *signParamSet,
60. const struct OH_Huks_Blob *inData,
61. struct OH_Huks_Blob *outDataSign)
62. {
63. uint8_t handleS[sizeof(uint64_t)] = {0};
64. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

66. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
67. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
68. return ohResult;
69. }

71. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, inData, outDataSign);

73. return ohResult;
74. }

76. /* 3. 验签  */
77. static OH_Huks_Result VerifySignatureSM2NoDigest(const struct OH_Huks_Blob *keyAlias,
78. const struct OH_Huks_ParamSet *verifyParamSet,
79. const struct OH_Huks_Blob *inData,
80. const struct OH_Huks_Blob *signature)
81. {
82. uint8_t handleV[sizeof(uint64_t)] = {0};
83. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

85. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
86. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
87. return ohResult;
88. }

90. uint8_t temp[] = "out";
91. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
92. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
93. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
94. return ohResult;
95. }

97. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

99. return ohResult;
100. }

102. napi_value SignVerifyKeySM2NoDigest(napi_env env, napi_callback_info info)
103. {
104. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_SM2_NoDigest"),
105. (uint8_t *)"test_signVerify_SM2_NoDigest"};
106. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_SM2_NODIGEST), (uint8_t *)DATA_TO_SIGN_SM2_NODIGEST};
107. struct OH_Huks_ParamSet *genParamSet = nullptr;
108. struct OH_Huks_ParamSet *signParamSet = nullptr;
109. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
110. OH_Huks_Result ohResult;

112. do {
113. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsSM2NoDigest,
114. sizeof(g_genSignVerifyParamsSM2NoDigest) / sizeof(OH_Huks_Param));
115. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
116. break;
117. }

119. ohResult = InitParamSet(&signParamSet, g_signParamsSM2NoDigest,
120. sizeof(g_signParamsSM2NoDigest) / sizeof(OH_Huks_Param));
121. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
122. break;
123. }

125. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsSM2NoDigest,
126. sizeof(g_verifyParamsSM2NoDigest) / sizeof(OH_Huks_Param));
127. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
128. break;
129. }

131. /* 1. 生成密钥 */
132. ohResult = GenerateKeySM2(&g_keyAlias, genParamSet);
133. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
134. break;
135. }

137. /* 2. 签名 */
138. uint8_t outDataS[SM2_COMMON_SIZE] = {0};
139. struct OH_Huks_Blob outDataSign = {SM2_COMMON_SIZE, outDataS};
140. ohResult = SignDataSM2NoDigest(&g_keyAlias, signParamSet, &inData, &outDataSign);
141. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
142. break;
143. }

145. /* 3. 验签 */
146. ohResult = VerifySignatureSM2NoDigest(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
147. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
148. break;
149. }
150. } while (0);

152. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
153. OH_Huks_FreeParamSet(&genParamSet);
154. OH_Huks_FreeParamSet(&signParamSet);
155. OH_Huks_FreeParamSet(&verifyParamSet);

157. napi_value ret;
158. napi_create_int32(env, ohResult.errorCode, &ret);
159. return ret;
160. }
```

[sm2\_nodigest\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/sm2_nodigest_sign_verify.cpp#L16-L177)

### RSA/SHA256/PSS

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsRsaPss[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
29. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
30. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
31. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
32. };

34. static struct OH_Huks_Param g_signParamsRsaPss[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
37. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
38. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
39. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN}
40. };

42. static struct OH_Huks_Param g_verifyParamsRsaPss[] = {
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
44. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
45. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
46. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
47. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY}
48. };

50. static const uint32_t RSA_COMMON_SIZE = 1024;
51. static const char *DATA_TO_SIGN_RSA_PSS = "Hks_RSA_PSS_Sign_Verify_Test_0000000000000000000000000000000000000000000"
52. "000000000000000000000000000000000000000000000000000000000000000000000000"
53. "000000000000000000000000000000000000000000000000000000000000000_string";

55. /* 1. 生成密钥 */
56. static OH_Huks_Result GenerateKey(const struct OH_Huks_Blob *keyAlias,
57. const struct OH_Huks_ParamSet *genParamSet)
58. {
59. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
60. }

62. /* 2. 签名 */
63. static OH_Huks_Result SignData(const struct OH_Huks_Blob *keyAlias,
64. const struct OH_Huks_ParamSet *signParamSet,
65. const struct OH_Huks_Blob *inData,
66. struct OH_Huks_Blob *outDataSign)
67. {
68. uint8_t handleS[sizeof(uint64_t)] = {0};
69. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

71. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
72. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
73. return ohResult;
74. }

76. ohResult = OH_Huks_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
77. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
78. return ohResult;
79. }

81. struct OH_Huks_Blob finishInData = {0, nullptr};
82. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);

84. return ohResult;
85. }

87. /* 3. 验签 */
88. static OH_Huks_Result VerifySignature(const struct OH_Huks_Blob *keyAlias,
89. const struct OH_Huks_ParamSet *verifyParamSet,
90. const struct OH_Huks_Blob *inData,
91. const struct OH_Huks_Blob *signature)
92. {
93. uint8_t handleV[sizeof(uint64_t)] = {0};
94. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

96. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
97. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
98. return ohResult;
99. }

101. uint8_t temp[] = "out";
102. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
103. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
104. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
105. return ohResult;
106. }

108. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

110. return ohResult;
111. }

113. napi_value SignVerifyKeyRsaSha256Pss(napi_env env, napi_callback_info info)
114. {
115. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_RSA_SHA256_PSS"),
116. (uint8_t *)"test_signVerify_RSA_SHA256_PSS"};
117. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_RSA_PSS), (uint8_t *)DATA_TO_SIGN_RSA_PSS};
118. struct OH_Huks_ParamSet *genParamSet = nullptr;
119. struct OH_Huks_ParamSet *signParamSet = nullptr;
120. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
121. OH_Huks_Result ohResult;

123. do {
124. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsRsaPss,
125. sizeof(g_genSignVerifyParamsRsaPss) / sizeof(OH_Huks_Param));
126. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
127. break;
128. }

130. ohResult = InitParamSet(&signParamSet, g_signParamsRsaPss, sizeof(g_signParamsRsaPss) / sizeof(OH_Huks_Param));
131. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
132. break;
133. }

135. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsRsaPss,
136. sizeof(g_verifyParamsRsaPss) / sizeof(OH_Huks_Param));
137. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
138. break;
139. }

141. ohResult = GenerateKey(&g_keyAlias, genParamSet);
142. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
143. break;
144. }

146. uint8_t outDataS[RSA_COMMON_SIZE] = {0};
147. struct OH_Huks_Blob outDataSign = {RSA_COMMON_SIZE, outDataS};
148. ohResult = SignData(&g_keyAlias, signParamSet, &inData, &outDataSign);
149. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
150. break;
151. }

153. ohResult = VerifySignature(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
154. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
155. break;
156. }
157. } while (0);

159. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
160. OH_Huks_FreeParamSet(&genParamSet);
161. OH_Huks_FreeParamSet(&signParamSet);
162. OH_Huks_FreeParamSet(&verifyParamSet);

164. napi_value ret;
165. napi_create_int32(env, ohResult.errorCode, &ret);
166. return ret;
167. }
```

[rsa\_sha256\_pss\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/rsa_sha256_pss_sign_verify.cpp#L16-L184)

### RSA/SHA256/PKCS1\_V1\_5

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsRsaPkcs1[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
29. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
30. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
31. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
32. };

34. static struct OH_Huks_Param g_signParamsRsaPkcs1[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
37. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN},
38. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
39. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}
40. };

42. static struct OH_Huks_Param g_verifyParamsRsaPkcs1[] = {
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
44. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
45. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY},
46. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS1_V1_5},
47. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256}
48. };

50. static const uint32_t RSA_COMMON_SIZE = 1024;
51. static const char *DATA_TO_SIGN_RSA_PKCS1 = "Hks_RSA_PKCS1_V1_5_Sign_Verify_Test_000000000000000000000000000000"
52. "000000000000000000000000000000000000000000000000000000000000000000"
53. "000000000000000000000000000000000000000000000000000000000000_string";

55. /* 1. 生成密钥 */
56. static OH_Huks_Result GenerateKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *genParamSet)
57. {
58. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
59. }

61. /* 2. 验签 */
62. static OH_Huks_Result SignData(const struct OH_Huks_Blob *keyAlias,
63. const struct OH_Huks_ParamSet *signParamSet,
64. const struct OH_Huks_Blob *inData,
65. struct OH_Huks_Blob *outDataSign)
66. {
67. uint8_t handleS[sizeof(uint64_t)] = {0};
68. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

70. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
71. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
72. return ohResult;
73. }

75. ohResult = OH_Huks_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
76. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
77. return ohResult;
78. }

80. struct OH_Huks_Blob finishInData = {0, nullptr};
81. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);

83. return ohResult;
84. }

86. /* 3. 验签 */
87. static OH_Huks_Result VerifySignature(const struct OH_Huks_Blob *keyAlias,
88. const struct OH_Huks_ParamSet *verifyParamSet,
89. const struct OH_Huks_Blob *inData,
90. const struct OH_Huks_Blob *signature)
91. {
92. uint8_t handleV[sizeof(uint64_t)] = {0};
93. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

95. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
96. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
97. return ohResult;
98. }

100. uint8_t temp[] = "out";
101. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
102. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
103. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
104. return ohResult;
105. }

107. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

109. return ohResult;
110. }

112. napi_value SignVerifyKeyRsaSha256Pkcs1V15(napi_env env, napi_callback_info info)
113. {
114. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_RSA_SHA256_PKCS1"),
115. (uint8_t *)"test_signVerify_RSA_SHA256_PKCS1"};
116. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_RSA_PKCS1), (uint8_t *)DATA_TO_SIGN_RSA_PKCS1};
117. struct OH_Huks_ParamSet *genParamSet = nullptr;
118. struct OH_Huks_ParamSet *signParamSet = nullptr;
119. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
120. OH_Huks_Result ohResult;

122. do {
123. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsRsaPkcs1,
124. sizeof(g_genSignVerifyParamsRsaPkcs1) / sizeof(OH_Huks_Param));
125. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
126. break;
127. }

129. ohResult = InitParamSet(&signParamSet, g_signParamsRsaPkcs1,
130. sizeof(g_signParamsRsaPkcs1) / sizeof(OH_Huks_Param));
131. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
132. break;
133. }

135. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsRsaPkcs1,
136. sizeof(g_verifyParamsRsaPkcs1) / sizeof(OH_Huks_Param));
137. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
138. break;
139. }

141. ohResult = GenerateKey(&g_keyAlias, genParamSet);
142. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
143. break;
144. }

146. uint8_t outDataS[RSA_COMMON_SIZE] = {0};
147. struct OH_Huks_Blob outDataSign = {RSA_COMMON_SIZE, outDataS};
148. ohResult = SignData(&g_keyAlias, signParamSet, &inData, &outDataSign);
149. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
150. break;
151. }

153. ohResult = VerifySignature(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
154. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
155. break;
156. }
157. } while (0);

159. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
160. OH_Huks_FreeParamSet(&genParamSet);
161. OH_Huks_FreeParamSet(&signParamSet);
162. OH_Huks_FreeParamSet(&verifyParamSet);

164. napi_value ret;
165. napi_create_int32(env, ohResult.errorCode, &ret);
166. return ret;
167. }
```

[rsa\_sha256\_pkcs1\_v1\_5\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/rsa_sha256_pkcs1_v1_5_sign_verify.cpp#L16-L184)

### RSA/SHA384/PSS

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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

26. static struct OH_Huks_Param g_genSignVerifyParamsRsaSha384Pss[] = {
27. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
28. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
29. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN | OH_HUKS_KEY_PURPOSE_VERIFY},
30. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
31. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA384},
32. };

34. static struct OH_Huks_Param g_signParamsRsaSha384Pss[] = {
35. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
37. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
38. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA384},
39. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_SIGN}
40. };

42. static struct OH_Huks_Param g_verifyParamsRsaSha384Pss[] = {
43. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
44. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
45. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PSS},
46. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA384},
47. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_VERIFY}
48. };

50. static const uint32_t RSA_COMMON_SIZE = 1024;
51. static const char *DATA_TO_SIGN_RSA_SHA384_PSS = "Hks_RSA_SHA384_PSS_Sign_Verify_Test_000000000000000000000000000"
52. "000000000000000000000000000000000000000000000000000000000000"
53. "000000000000000000000000000000000000000000000000000000_string";

55. /* 1. 生成密钥 */
56. static OH_Huks_Result GenerateKeyRSA(const struct OH_Huks_Blob *keyAlias,
57. const struct OH_Huks_ParamSet *genParamSet)
58. {
59. return OH_Huks_GenerateKeyItem(keyAlias, genParamSet, nullptr);
60. }

62. /* 2. 签名 */
63. static OH_Huks_Result SignDataRSA(const struct OH_Huks_Blob *keyAlias,
64. const struct OH_Huks_ParamSet *signParamSet,
65. const struct OH_Huks_Blob *inData,
66. struct OH_Huks_Blob *outDataSign)
67. {
68. uint8_t handleS[sizeof(uint64_t)] = {0};
69. struct OH_Huks_Blob handleSign = {(uint32_t)sizeof(uint64_t), handleS};

71. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, signParamSet, &handleSign, nullptr);
72. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
73. return ohResult;
74. }

76. ohResult = OH_Huks_UpdateSession(&handleSign, signParamSet, inData, outDataSign);
77. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
78. return ohResult;
79. }

81. struct OH_Huks_Blob finishInData = {0, NULL};
82. ohResult = OH_Huks_FinishSession(&handleSign, signParamSet, &finishInData, outDataSign);

84. return ohResult;
85. }

87. /* 3. 验签  */
88. static OH_Huks_Result VerifySignatureRSA(const struct OH_Huks_Blob *keyAlias,
89. const struct OH_Huks_ParamSet *verifyParamSet,
90. const struct OH_Huks_Blob *inData,
91. const struct OH_Huks_Blob *signature)
92. {
93. uint8_t handleV[sizeof(uint64_t)] = {0};
94. struct OH_Huks_Blob handleVerify = {(uint32_t)sizeof(uint64_t), handleV};

96. OH_Huks_Result ohResult = OH_Huks_InitSession(keyAlias, verifyParamSet, &handleVerify, nullptr);
97. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
98. return ohResult;
99. }

101. uint8_t temp[] = "out";
102. struct OH_Huks_Blob verifyOut = {(uint32_t)sizeof(temp), temp};
103. ohResult = OH_Huks_UpdateSession(&handleVerify, verifyParamSet, inData, &verifyOut);
104. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
105. return ohResult;
106. }

108. ohResult = OH_Huks_FinishSession(&handleVerify, verifyParamSet, signature, &verifyOut);

110. return ohResult;
111. }

113. napi_value SignVerifyKey(napi_env env, napi_callback_info info)
114. {
115. struct OH_Huks_Blob g_keyAlias = {(uint32_t)strlen("test_signVerify_RSA_SHA384_PSS"),
116. (uint8_t *)"test_signVerify_RSA_SHA384_PSS"};
117. struct OH_Huks_Blob inData = {(uint32_t)strlen(DATA_TO_SIGN_RSA_SHA384_PSS),
118. (uint8_t *)DATA_TO_SIGN_RSA_SHA384_PSS};
119. struct OH_Huks_ParamSet *genParamSet = nullptr;
120. struct OH_Huks_ParamSet *signParamSet = nullptr;
121. struct OH_Huks_ParamSet *verifyParamSet = nullptr;
122. OH_Huks_Result ohResult;

124. do {
125. ohResult = InitParamSet(&genParamSet, g_genSignVerifyParamsRsaSha384Pss,
126. sizeof(g_genSignVerifyParamsRsaSha384Pss) / sizeof(OH_Huks_Param));
127. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
128. break;
129. }

131. ohResult = InitParamSet(&signParamSet, g_signParamsRsaSha384Pss,
132. sizeof(g_signParamsRsaSha384Pss) / sizeof(OH_Huks_Param));
133. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
134. break;
135. }

137. ohResult = InitParamSet(&verifyParamSet, g_verifyParamsRsaSha384Pss,
138. sizeof(g_verifyParamsRsaSha384Pss) / sizeof(OH_Huks_Param));
139. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
140. break;
141. }

143. /* 1. 生成密钥 */
144. ohResult = GenerateKeyRSA(&g_keyAlias, genParamSet);
145. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
146. break;
147. }

149. /* 2. 签名 */
150. uint8_t outDataS[RSA_COMMON_SIZE] = {0};
151. struct OH_Huks_Blob outDataSign = {RSA_COMMON_SIZE, outDataS};
152. ohResult = SignDataRSA(&g_keyAlias, signParamSet, &inData, &outDataSign);
153. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
154. break;
155. }

157. /* 3. 验签 */
158. ohResult = VerifySignatureRSA(&g_keyAlias, verifyParamSet, &inData, &outDataSign);
159. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
160. break;
161. }
162. } while (0);

164. (void)OH_Huks_DeleteKeyItem(&g_keyAlias, genParamSet);
165. OH_Huks_FreeParamSet(&genParamSet);
166. OH_Huks_FreeParamSet(&signParamSet);
167. OH_Huks_FreeParamSet(&verifyParamSet);

169. napi_value ret;
170. napi_create_int32(env, ohResult.errorCode, &ret);
171. return ret;
172. }
```

[rsa\_sha384\_pss\_sign\_verify.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/cpp/rsa_sha384_pss_sign_verify.cpp#L16-L189)
