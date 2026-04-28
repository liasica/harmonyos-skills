---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-envelop-key-ndk
title: 数字信封密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 数字信封密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6381a8181bb85e085562adbb109a63ca4adbc2cdedf5de54384f191691534ec8
---

从API 23开始支持[数字信封](huks-key-import-overview.md#数字信封导入)特性。

以数字信封导入RSA密钥和AES密钥为例。具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)，其中**数字信封导入密钥不支持DSA算法**。

使用数字信封导入密钥需要使用[OH\_HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，该标签值为[OH\_HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_algsuite)。

数字信封导入密钥时，如果是导入非对称密钥的密钥对，需要添加[OH\_HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)标签，并将公钥以X.509 DER格式封装填入该标签，且针对非对称密钥仅支持以密钥对形式导入。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 业务方设备（设备A）生成SM4密钥，cipherSm4。
2. 设备A使用生成的SM4密钥，以ECB/NoPadding模式对导入密钥importKey进行加密，得到加密后的密钥enImportKey=Encrypt(cipherSm4, importKey)。
3. 密钥导入方（设备B）导出SM2公钥，设备A接收该密钥。
4. 设备A使用收到的SM2公钥加密生成的SM4密钥，enSm4=Encrypt(Sm2, cipherSm4)。
5. 设备A将数字信封数据发送给设备B。
6. 设备B使用导入WrappedKey导入数字信封密钥。若导入密钥是对称密钥，此步骤只需对裸密钥进行加密。若导入非对称密钥的密钥对，则将公钥以DER格式封装，并放入[OH\_HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)中。

### RSA导入示例

```
1. #include <string.h>
2. #include "napi/native_api.h"
3. #include "huks/native_huks_api.h"
4. #include "huks/native_huks_param.h"
5. #include "huks/native_huks_type.h"

7. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
8. uint32_t paramCount) {
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

26. void ConcatBlob(OH_Huks_Blob *data1, OH_Huks_Blob *data2, OH_Huks_Blob *outData) {
27. if (outData == NULL || data1 == NULL || data2 == NULL) {
28. return;
29. }

31. uint32_t offset = 0;
32. memcpy(outData->data, &data1->size, sizeof(uint32_t));
33. offset += sizeof(uint32_t);

35. memcpy(outData->data + offset, data1->data, data1->size);
36. offset += data1->size;

38. memcpy(outData->data + offset, &data2->size, sizeof(uint32_t));
39. offset += sizeof(uint32_t);

41. memcpy(outData->data + offset, data2->data, data2->size);
42. outData->size = data1->size + data2->size + 2 * sizeof(uint32_t);

44. return;
45. }

47. // 用于生成Sm2密钥，模拟导入端已有的Sm2密钥
48. static struct OH_Huks_Param gEnvelopIniSm2[] = {
49. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT | OH_HUKS_KEY_PURPOSE_ENCRYPT},
50. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
51. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
52. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3},
53. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
54. };

56. // 用于模拟业务方得到的导入端Sm2公钥
57. static struct OH_Huks_Param gEnvelopEnSm2[] = {
58. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
59. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
60. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
61. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3},
62. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
63. };

65. // Sm4密钥明文
66. uint8_t sm4UintData[] = {
67. 0xb9, 0xef, 0x35, 0x49, 0xb7, 0x00, 0x91, 0x58, 0x0c, 0x6f, 0x43, 0x28, 0xf8, 0x95, 0x1c, 0x02,
68. };

70. OH_Huks_Blob gSm4Data = {sizeof(sm4UintData) / sizeof(sm4UintData[0]), sm4UintData};
71. uint8_t sm2KeyAliasUint8[] = "testKey";
72. OH_Huks_Blob gSm2KeyAlias = {.size = sizeof(sm2KeyAliasUint8), .data = sm2KeyAliasUint8};

74. static napi_value EnvelopImportKey(napi_env env, napi_callback_info info) {
75. struct OH_Huks_ParamSet *sm2GenerateKeyParamSet = NULL;
76. struct OH_Huks_Result ohResult;
77. struct OH_Huks_ParamSet *sm2KeyData = NULL;
78. napi_value ret;

80. // 生成一个sm2密钥模拟设备B导出的sm2密钥
81. ohResult = InitParamSet(&sm2GenerateKeyParamSet, gEnvelopIniSm2, sizeof(gEnvelopIniSm2) / sizeof(OH_Huks_Param));
82. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
83. napi_create_int32(env, ohResult.errorCode, &ret);
84. return ret;
85. }

87. ohResult = OH_Huks_GenerateKeyItem(&gSm2KeyAlias, sm2GenerateKeyParamSet, sm2KeyData);
88. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
89. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
90. napi_create_int32(env, ohResult.errorCode, &ret);
91. return ret;
92. }

94. uint8_t handleE[sizeof(uint64_t)] = {0};
95. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};

97. // 使用sm2密钥加密
98. struct OH_Huks_ParamSet *sm2EnKeyParamSet = NULL;
99. ohResult = InitParamSet(&sm2EnKeyParamSet, gEnvelopEnSm2, sizeof(gEnvelopEnSm2) / sizeof(OH_Huks_Param));
100. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
101. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
102. napi_create_int32(env, ohResult.errorCode, &ret);
103. return ret;
104. }

106. ohResult = OH_Huks_InitSession(&gSm2KeyAlias, sm2EnKeyParamSet, &handleEncrypt, nullptr);
107. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
108. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
109. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
110. napi_create_int32(env, ohResult.errorCode, &ret);
111. return ret;
112. }

114. static const uint32_t SM4_SIZE = 128;
115. uint8_t cipher[SM4_SIZE] = {0};
116. struct OH_Huks_Blob cipherSm4Data = {SM4_SIZE, cipher};
117. ohResult = OH_Huks_FinishSession(&handleEncrypt, sm2EnKeyParamSet, &gSm4Data, &cipherSm4Data);
118. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
119. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
120. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
121. napi_create_int32(env, ohResult.errorCode, &ret);
122. return ret;
123. }

125. uint8_t rsaUintPubKey[] = {
126. 0x30, 0x82, 0x01, 0x22, 0x30, 0x0d, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x01, 0x01, 0x05,
127. 0x00, 0x03, 0x82, 0x01, 0x0f, 0x00, 0x30, 0x82, 0x01, 0x0a, 0x02, 0x82, 0x01, 0x01, 0x00, 0xa2, 0xd2, 0x3c,
128. 0xe9, 0x87, 0x8b, 0x48, 0x34, 0xdd, 0x41, 0xe0, 0x65, 0x39, 0xcc, 0xea, 0x25, 0x25, 0xa6, 0x9e, 0x9f, 0x20,
129. 0xc6, 0x13, 0x9f, 0xb2, 0xa7, 0xf3, 0x77, 0x69, 0xfd, 0xa9, 0xbd, 0xe8, 0x2c, 0xf3, 0x87, 0x3a, 0xc0, 0x2a,
130. 0x01, 0x1f, 0x8d, 0x0f, 0x59, 0x28, 0x34, 0xfb, 0xe3, 0x8d, 0x9b, 0xa1, 0xe0, 0xe4, 0x60, 0x7d, 0x20, 0x19,
131. 0x49, 0x6f, 0x13, 0x5e, 0xae, 0x3e, 0x4d, 0x6c, 0x31, 0x6c, 0x0b, 0x90, 0xf8, 0xd2, 0xf3, 0x45, 0x4f, 0x3b,
132. 0x9f, 0x8e, 0x3b, 0x77, 0x20, 0x9e, 0x54, 0xec, 0x7b, 0x54, 0x15, 0xf0, 0x09, 0x8f, 0x5a, 0xf9, 0x87, 0x9a,
133. 0x27, 0x23, 0x99, 0x64, 0x4d, 0x8c, 0x80, 0x5c, 0x2e, 0xee, 0xc3, 0x57, 0x6e, 0x3d, 0x91, 0xfb, 0x77, 0x67,
134. 0x3b, 0x8a, 0xed, 0x01, 0xb5, 0x91, 0x33, 0xa1, 0xaa, 0xb2, 0x0d, 0x49, 0x25, 0x7c, 0x4d, 0x42, 0xde, 0xfb,
135. 0xcd, 0xd6, 0x48, 0xb8, 0xce, 0xe7, 0x22, 0x71, 0x43, 0x54, 0x2c, 0x6b, 0xbb, 0xbf, 0x63, 0xdc, 0xea, 0x6f,
136. 0x77, 0x81, 0xe9, 0x07, 0xe0, 0x18, 0xb3, 0x1e, 0x78, 0x4b, 0xbc, 0x17, 0x77, 0x62, 0x25, 0xd9, 0xe7, 0x23,
137. 0x6c, 0x80, 0xad, 0xdc, 0x51, 0x18, 0x1b, 0x33, 0x56, 0x59, 0x15, 0x43, 0xcf, 0x51, 0xd9, 0xbc, 0x6d, 0xf7,
138. 0x68, 0xd1, 0xe8, 0xbf, 0x41, 0x36, 0xd1, 0x30, 0x92, 0x7b, 0x48, 0xd1, 0x00, 0xe2, 0x9d, 0x8e, 0x94, 0xee,
139. 0x20, 0x2a, 0x18, 0xb1, 0x04, 0xba, 0xe7, 0x19, 0xdc, 0x69, 0x36, 0xf7, 0x34, 0x4b, 0x16, 0x10, 0x10, 0x2a,
140. 0x46, 0x1c, 0x4e, 0x6e, 0x62, 0xe1, 0x25, 0x79, 0xd5, 0x5c, 0xf3, 0x9a, 0xeb, 0x1f, 0x3d, 0x82, 0xa3, 0xaa,
141. 0x79, 0xde, 0x23, 0xa1, 0x2b, 0x50, 0x6d, 0x68, 0x3e, 0x77, 0x33, 0xe0, 0xc9, 0x18, 0xbc, 0x65, 0x58, 0x63,
142. 0x7b, 0x02, 0x03, 0x01, 0x00, 0x01,
143. };

145. OH_Huks_Param rsaParams[] = {
146. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_RSA},
147. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_RSA_KEY_SIZE_2048},
148. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
149. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
150. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
151. {.tag = OH_HUKS_TAG_UNWRAP_ALGORITHM_SUITE, .uint32Param = OH_HUKS_UNWRAP_SUITE_SM2_SM4_ECB_NOPADDING},
152. {.tag = OH_HUKS_TAG_IMPORT_KEY_TYPE, .uint32Param = OH_HUKS_KEY_TYPE_KEY_PAIR},
153. {.tag = OH_HUKS_TAG_ASYMMETRIC_PUBLIC_KEY_DATA, .blob = {sizeof(rsaUintPubKey), rsaUintPubKey}},
154. };

156. struct OH_Huks_ParamSet *rsaParamSet = NULL;
157. ohResult = InitParamSet(&rsaParamSet, rsaParams, sizeof(rsaParams) / sizeof(OH_Huks_Param));
158. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
159. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
160. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
161. napi_create_int32(env, ohResult.errorCode, &ret);
162. return ret;
163. }

165. // 已使用sm4加密，密钥为sm4UintData
166. uint8_t rsaPrivate[] = {
167. 0x4a, 0xce, 0x89, 0xa6, 0xda, 0x85, 0x6d, 0x56, 0xb3, 0xab, 0xc9, 0x70, 0x5e, 0x3f, 0xb6, 0x0e, 0x07, 0xdf,
168. 0xdf, 0x9c, 0xb3, 0x05, 0xd4, 0x8d, 0xc0, 0xac, 0x9b, 0x13, 0x3d, 0x1b, 0xdb, 0xa0, 0x46, 0x1a, 0xc8, 0x82,
169. 0x80, 0xe0, 0x2a, 0x28, 0x34, 0xa6, 0x4a, 0x97, 0x91, 0x58, 0xc8, 0x8c, 0x0f, 0xa2, 0xeb, 0xe1, 0xf8, 0x37,
170. 0x54, 0x99, 0x7e, 0xa1, 0xce, 0x1e, 0xf3, 0x8b, 0x8c, 0x8d, 0xec, 0x58, 0xb7, 0x32, 0x29, 0x36, 0x34, 0x46,
171. 0x92, 0x67, 0x09, 0xb3, 0xb4, 0xb3, 0x74, 0x3a, 0x77, 0x99, 0xd7, 0x4b, 0x1f, 0xf6, 0xa6, 0xb0, 0x99, 0x3d,
172. 0x3e, 0x92, 0xba, 0xcf, 0x83, 0xd0, 0x1e, 0x18, 0x68, 0x1a, 0xb5, 0xfe, 0x18, 0x6d, 0x9d, 0xc2, 0x39, 0x48,
173. 0x2e, 0x52, 0xfc, 0x33, 0x16, 0xb0, 0x58, 0xd5, 0xdf, 0x84, 0xbe, 0xfe, 0xe1, 0xfa, 0xa9, 0x65, 0x34, 0xb8,
174. 0x97, 0xa3, 0x9a, 0x45, 0x8a, 0x40, 0x4b, 0x09, 0xdf, 0x1c, 0x48, 0x57, 0x3f, 0xb2, 0x1f, 0xf3, 0x21, 0x7d,
175. 0xa8, 0xa5, 0xed, 0xe1, 0x61, 0x2f, 0xe0, 0xda, 0xae, 0x15, 0x22, 0x18, 0xf6, 0x84, 0x7d, 0x39, 0xae, 0x35,
176. 0x49, 0xec, 0xd8, 0x66, 0xff, 0x65, 0x7d, 0xd9, 0x74, 0x19, 0xad, 0x26, 0x64, 0xc0, 0x2d, 0x93, 0xf5, 0x83,
177. 0x7d, 0x8d, 0x98, 0x35, 0x2e, 0x67, 0xf9, 0xc0, 0xb1, 0xd7, 0x2b, 0xb5, 0x49, 0x98, 0x3a, 0x31, 0xa0, 0x66,
178. 0x71, 0x6e, 0x09, 0x70, 0xef, 0x56, 0x14, 0x9e, 0xb8, 0xd2, 0x17, 0x99, 0x44, 0x69, 0xcd, 0x3d, 0xcb, 0x3c,
179. 0xfe, 0xbe, 0x72, 0xc0, 0x43, 0x29, 0x86, 0x70, 0x9d, 0xa3, 0xc0, 0x68, 0xf6, 0x7e, 0x48, 0x2c, 0x4e, 0x48,
180. 0xe0, 0xf6, 0xa9, 0xcb, 0x28, 0x63, 0xe8, 0x33, 0xfc, 0xb4, 0x1a, 0x06, 0xf4, 0x13, 0x20, 0xfd, 0x90, 0x90,
181. 0x1c, 0x25, 0xd7, 0xf8,
182. };
183. OH_Huks_Blob rsaEnPrivateData = {sizeof(rsaPrivate), rsaPrivate};

185. uint8_t importKey[1000] = {0};
186. OH_Huks_Blob importKeyBlob = {0, importKey};
187. ConcatBlob(&cipherSm4Data, &rsaEnPrivateData, &importKeyBlob);

189. uint8_t importAlias[] = "importRsa";
190. OH_Huks_Blob rsaKeyAlias = {(uint32_t)sizeof(importAlias), importAlias};
191. ohResult = OH_Huks_ImportWrappedKeyItem(&rsaKeyAlias, &gSm2KeyAlias, rsaParamSet, &importKeyBlob);

193. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
194. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
195. OH_Huks_FreeParamSet(&rsaParamSet);

197. napi_create_int32(env, ohResult.errorCode, &ret);
198. return ret;
199. }
```

### AES导入示例

```
1. #include <string.h>
2. #include "napi/native_api.h"
3. #include "huks/native_huks_api.h"
4. #include "huks/native_huks_param.h"
5. #include "huks/native_huks_type.h"

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

27. void ConcatBlob(OH_Huks_Blob *data1, OH_Huks_Blob *data2, OH_Huks_Blob *outData)
28. {
29. if (outData == NULL || data1 == NULL || data2 == NULL) {
30. return;
31. }

33. uint32_t offset = 0;
34. memcpy(outData->data, &data1->size, sizeof(uint32_t));
35. offset += sizeof(uint32_t);

37. memcpy(outData->data + offset, data1->data, data1->size);
38. offset += data1->size;

40. memcpy(outData->data + offset, &data2->size, sizeof(uint32_t));
41. offset += sizeof(uint32_t);

43. memcpy(outData->data + offset, data2->data, data2->size);
44. outData->size = data1->size + data2->size + 2 * sizeof(uint32_t);

46. return;
47. }

49. // 用于生成Sm2密钥，模拟导入端已有的Sm2密钥
50. static struct OH_Huks_Param gEnvelopIniSm2[] = {
51. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT | OH_HUKS_KEY_PURPOSE_ENCRYPT},
52. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
53. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
54. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3},
55. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
56. };

58. // 用于模拟业务方得到的导入端Sm2公钥
59. static struct OH_Huks_Param gEnvelopEnSm2[] = {
60. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
61. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_SM2},
62. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_SM2_KEY_SIZE_256},
63. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SM3},
64. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
65. };

67. // Sm4密钥明文
68. uint8_t sm4UintData[] = {
69. 0xb9, 0xef, 0x35, 0x49, 0xb7, 0x00, 0x91, 0x58, 0x0c, 0x6f, 0x43, 0x28, 0xf8, 0x95, 0x1c, 0x02,
70. };

72. OH_Huks_Blob gSm4Data = {sizeof(sm4UintData) / sizeof(sm4UintData[0]), sm4UintData};
73. uint8_t sm2KeyAliasUint8[] = "testKey";
74. OH_Huks_Blob gSm2KeyAlias = {.size = sizeof(sm2KeyAliasUint8), .data = sm2KeyAliasUint8};

76. static napi_value EnvelopImportKeyTest(napi_env env, napi_callback_info info)
77. {
78. struct OH_Huks_ParamSet *sm2GenerateKeyParamSet = NULL;
79. struct OH_Huks_Result ohResult;
80. struct OH_Huks_ParamSet *sm2KeyData = NULL;
81. struct OH_Huks_ParamSet *aesParamSet = NULL;
82. struct OH_Huks_ParamSet *sm2EnKeyParamSet = NULL;
83. napi_value ret;

85. uint8_t aesAlias[] = "testAes";
86. OH_Huks_Blob aesAliasBlob = {(uint32_t)sizeof(aesAlias), aesAlias};

88. ohResult = InitParamSet(&sm2GenerateKeyParamSet, gEnvelopIniSm2, sizeof(gEnvelopIniSm2) / sizeof(OH_Huks_Param));
89. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
90. napi_create_int32(env, ohResult.errorCode, &ret);
91. return ret;
92. }
93. ohResult = OH_Huks_GenerateKeyItem(&gSm2KeyAlias, sm2GenerateKeyParamSet, sm2KeyData);
94. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
95. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
96. napi_create_int32(env, ohResult.errorCode, &ret);
97. return ret;
98. }
99. uint8_t handleE[sizeof(uint64_t)] = {0};
100. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
101. ohResult = InitParamSet(&sm2EnKeyParamSet, gEnvelopEnSm2, sizeof(gEnvelopEnSm2) / sizeof(OH_Huks_Param));
102. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
103. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
104. napi_create_int32(env, ohResult.errorCode, &ret);
105. return ret;
106. }

108. ohResult = OH_Huks_InitSession(&gSm2KeyAlias, sm2EnKeyParamSet, &handleEncrypt, nullptr);
109. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
110. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
111. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
112. napi_create_int32(env, ohResult.errorCode, &ret);
113. return ret;
114. }
115. static const uint32_t SM4_SIZE = 128;
116. uint8_t cipher[SM4_SIZE] = {0};
117. struct OH_Huks_Blob cipherSm4Data = {SM4_SIZE, cipher};
118. ohResult = OH_Huks_FinishSession(&handleEncrypt, sm2EnKeyParamSet, &gSm4Data, &cipherSm4Data);
119. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
120. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
121. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
122. napi_create_int32(env, ohResult.errorCode, &ret);
123. return ret;
124. }

126. OH_Huks_Param importAesParams[] = {
127. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
128. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
129. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_CBC},
130. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_PKCS7},
131. {.tag = OH_HUKS_TAG_UNWRAP_ALGORITHM_SUITE, .uint32Param = OH_HUKS_UNWRAP_SUITE_SM2_SM4_ECB_NOPADDING},
132. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_128}};

134. ohResult = InitParamSet(&aesParamSet, importAesParams, sizeof(importAesParams) / sizeof(OH_Huks_Param));
135. // 已使用sm4加密，密钥为sm4UintData
136. uint8_t importAesData[] = {
137. 0xa5, 0xa4, 0xef, 0x4b, 0x87, 0x69, 0xf1, 0xd0, 0x7c, 0xd0, 0x55, 0x9a, 0xe0, 0xb8, 0x8c, 0x36,
138. };
139. OH_Huks_Blob aesBlob = {sizeof(importAesData), importAesData};

141. uint8_t importKey[1000] = {0};
142. OH_Huks_Blob importKeyBlob = {0, importKey};
143. ConcatBlob(&cipherSm4Data, &aesBlob, &importKeyBlob);

145. ohResult = OH_Huks_ImportWrappedKeyItem(&aesAliasBlob, &gSm2KeyAlias, aesParamSet, &importKeyBlob);

147. OH_Huks_FreeParamSet(&sm2EnKeyParamSet);
148. OH_Huks_FreeParamSet(&sm2GenerateKeyParamSet);
149. OH_Huks_FreeParamSet(&aesParamSet);

151. return ret;
152. }
```
