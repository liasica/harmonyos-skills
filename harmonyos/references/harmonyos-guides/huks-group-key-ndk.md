---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-ndk
title: 群组密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2795be4164d33ccf015d550aa73df23c5a5f5fd2a55c066bf01ea1ca9fcee07
---

从API 23开始，HUKS支持群组密钥功能。群组密钥支持的HUKS密钥操作及详细介绍参考[群组密钥介绍](huks-group-key-overview.md)，本文档以[AES/CBC/PKCS7加解密](huks-group-key-ndk.md#aescbcpkcs7加解密)、[X25519非对称密钥协商](huks-group-key-ndk.md#x25519非对称密钥协商)、[PBKDF2派生密钥](huks-group-key-ndk.md#pbkdf2派生密钥)为例展示群组密钥使用方法。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

**配置文件**

使用群组密钥之前，需要在app.json5文件中配置群组信息，配置方法参考[配置文件示例](app-configuration-file.md#配置文件示例)中assetAccessGroups字段的配置方式。

## AES/CBC/PKCS7加解密

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)、[OH\_HUKS\_TAG\_KEY\_OVERRIDE](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，避免密钥被覆盖。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 指定密钥别名。
2. 指定待加密的数据。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取加密后的密文。

**解密**

1. 指定密钥别名。
2. 指定待解密的密文。
3. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
4. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，获取解密后的数据。

**删除密钥**

1. 指定密钥别名。
2. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
3. 调用[OH\_Huks\_DeleteKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

当密钥废弃不用时，需要调用OH\_Huks\_DeleteKeyItem删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

### 开发示例

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>
5. #include "CryptoArchitectureKit/crypto_architecture_kit.h"

7. static OH_Crypto_ErrCode genRandomNumber(uint32_t randomLength, uint8_t *out)
8. {
9. /* 创建随机数生成器 */
10. OH_CryptoRand *rand = nullptr;
11. OH_Crypto_ErrCode ret = OH_CryptoRand_Create(&rand);
12. if (ret != CRYPTO_SUCCESS) {
13. return ret;
14. }
15. Crypto_DataBlob blob = {out, randomLength};
16. /* 生成指定长度的随机数 */
17. ret = OH_CryptoRand_GenerateRandom(rand, randomLength, &blob);
18. if (ret != CRYPTO_SUCCESS) {
19. OH_CryptoRand_Destroy(rand);
20. return ret;
21. }
22. OH_CryptoRand_Destroy(rand);

24. return CRYPTO_SUCCESS;
25. }

27. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params, uint32_t paramCount)
28. {
29. OH_Huks_Result ret = OH_Huks_InitParamSet(paramSet);
30. if (ret.errorCode != OH_HUKS_SUCCESS) {
31. return ret;
32. }
33. ret = OH_Huks_AddParams(*paramSet, params, paramCount);
34. if (ret.errorCode != OH_HUKS_SUCCESS) {
35. OH_Huks_FreeParamSet(paramSet);
36. return ret;
37. }
38. ret = OH_Huks_BuildParamSet(paramSet);
39. if (ret.errorCode != OH_HUKS_SUCCESS) {
40. OH_Huks_FreeParamSet(paramSet);
41. return ret;
42. }
43. return ret;
44. }
45. uint32_t OH_HUKS_TAG_KEY_ACCESS_GROUP = 5 << 28 | 523;
46. static const uint32_t IV_SIZE = 16;
47. static uint8_t IV[IV_SIZE] = { 0 };
48. static OH_Crypto_ErrCode ret = genRandomNumber(IV_SIZE, IV);
49. /*
50. * 需要在app.json5中配置assetAccessGroups字段新增分组信息
51. */
52. static char group[] = "ohos.test.group";
53. static struct OH_Huks_Param g_genEncDecParams[] = {
54. {
55. .tag = OH_HUKS_TAG_ALGORITHM,
56. .uint32Param = OH_HUKS_ALG_AES
57. }, {
58. .tag = OH_HUKS_TAG_PURPOSE,
59. .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT
60. }, {
61. .tag = OH_HUKS_TAG_KEY_SIZE,
62. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
63. }, {
64. .tag = OH_HUKS_TAG_PADDING,
65. .uint32Param = OH_HUKS_PADDING_PKCS7
66. }, {
67. .tag = OH_HUKS_TAG_BLOCK_MODE,
68. .uint32Param = OH_HUKS_MODE_CBC
69. }, {
70. .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
71. .blob = {
72. .size = (uint32_t)strlen(group),
73. .data = (uint8_t *)group
74. }
75. }
76. };
77. static struct OH_Huks_Param g_encryptParams[] = {
78. {
79. .tag = OH_HUKS_TAG_ALGORITHM,
80. .uint32Param = OH_HUKS_ALG_AES
81. }, {
82. .tag = OH_HUKS_TAG_PURPOSE,
83. .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT
84. }, {
85. .tag = OH_HUKS_TAG_KEY_SIZE,
86. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
87. }, {
88. .tag = OH_HUKS_TAG_PADDING,
89. .uint32Param = OH_HUKS_PADDING_PKCS7
90. }, {
91. .tag = OH_HUKS_TAG_BLOCK_MODE,
92. .uint32Param = OH_HUKS_MODE_CBC
93. }, {
94. .tag = OH_HUKS_TAG_IV,
95. .blob = {
96. .size = IV_SIZE,
97. .data = (uint8_t *)IV
98. }
99. }, {
100. .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
101. .blob = {
102. .size = (uint32_t)strlen(group),
103. .data = (uint8_t *)group
104. }
105. }
106. };
107. static struct OH_Huks_Param g_decryptParams[] = {
108. {
109. .tag = OH_HUKS_TAG_ALGORITHM,
110. .uint32Param = OH_HUKS_ALG_AES
111. }, {
112. .tag = OH_HUKS_TAG_PURPOSE,
113. .uint32Param = OH_HUKS_KEY_PURPOSE_DECRYPT
114. }, {
115. .tag = OH_HUKS_TAG_KEY_SIZE,
116. .uint32Param = OH_HUKS_AES_KEY_SIZE_256
117. }, {
118. .tag = OH_HUKS_TAG_PADDING,
119. .uint32Param = OH_HUKS_PADDING_PKCS7
120. }, {
121. .tag = OH_HUKS_TAG_BLOCK_MODE,
122. .uint32Param = OH_HUKS_MODE_CBC
123. }, {
124. .tag = OH_HUKS_TAG_IV,
125. .blob = {
126. .size = IV_SIZE,
127. .data = (uint8_t *)IV
128. }
129. }, {
130. .tag = OH_HUKS_TAG_KEY_ACCESS_GROUP,
131. .blob = {
132. .size = (uint32_t)strlen(group),
133. .data = (uint8_t *)group
134. }
135. }
136. };
137. static const uint32_t AES_COMMON_SIZE = 1024;

139. OH_Huks_Result HksAesCipherTestEncrypt(
140. const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *encryptParamSet,
141. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *cipherText)
142. {
143. uint8_t handleE[sizeof(uint64_t)] = {0};
144. struct OH_Huks_Blob handleEncrypt = {sizeof(uint64_t), handleE};
145. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, encryptParamSet, &handleEncrypt, nullptr);
146. if (ret.errorCode != OH_HUKS_SUCCESS) {
147. return ret;
148. }
149. ret = OH_Huks_FinishSession(&handleEncrypt, encryptParamSet, inData, cipherText);
150. return ret;
151. }

153. OH_Huks_Result HksAesCipherTestDecrypt(const struct OH_Huks_Blob *keyAlias,
154. const struct OH_Huks_ParamSet *decryptParamSet, const struct OH_Huks_Blob *cipherText,
155. struct OH_Huks_Blob *plainText, const struct OH_Huks_Blob *inData)
156. {
157. uint8_t handleD[sizeof(uint64_t)] = {0};
158. struct OH_Huks_Blob handleDecrypt = {sizeof(uint64_t), handleD};
159. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, decryptParamSet, &handleDecrypt, nullptr);
160. if (ret.errorCode != OH_HUKS_SUCCESS) {
161. return ret;
162. }
163. ret = OH_Huks_FinishSession(&handleDecrypt, decryptParamSet, cipherText, plainText);
164. return ret;
165. }

167. static napi_value EncDecKey(napi_env env, napi_callback_info info)
168. {
169. char tmpKeyAlias[] = "test_enc_dec";
170. struct OH_Huks_Blob keyAlias = { (uint32_t)strlen(tmpKeyAlias), (uint8_t *)tmpKeyAlias };
171. struct OH_Huks_ParamSet *genParamSet = nullptr;
172. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
173. struct OH_Huks_ParamSet *decryptParamSet = nullptr;
174. OH_Huks_Result ohResult;
175. do {
176. /* 1. Generate Key */
177. /*
178. * 模拟生成密钥场景
179. * 1.1. 确定密钥别名
180. */
181. /*
182. * 1.2. 获取生成密钥算法参数配置
183. */
184. ohResult = InitParamSet(&genParamSet, g_genEncDecParams, sizeof(g_genEncDecParams) / sizeof(OH_Huks_Param));
185. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
186. break;
187. }
188. /*
189. * 1.3. 调用generateKeyItem
190. */
191. ohResult = OH_Huks_GenerateKeyItem(&keyAlias, genParamSet, nullptr);
192. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
193. break;
194. }
195. /* 2. Encrypt */
196. /*
197. * 模拟加密场景
198. * 2.1. 获取密钥别名
199. */
200. /*
201. * 2.2. 获取待加密的数据
202. */
203. /*
204. * 2.3. 获取加密算法参数配置
205. */
206. ohResult = InitParamSet(&encryptParamSet, g_encryptParams, sizeof(g_encryptParams) / sizeof(OH_Huks_Param));
207. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
208. break;
209. }
210. char tmpInData[] = "AES_ECB_INDATA_1";
211. struct OH_Huks_Blob inData = { (uint32_t)strlen(tmpInData), (uint8_t *)tmpInData };
212. uint8_t cipher[AES_COMMON_SIZE] = {0};
213. struct OH_Huks_Blob cipherText = {AES_COMMON_SIZE, cipher};
214. /*
215. * 2.4. 调用initSession获取handle
216. */
217. /*
218. * 2.5. 调用finishSession获取加密后的密文
219. */
220. ohResult = HksAesCipherTestEncrypt(&keyAlias, encryptParamSet, &inData, &cipherText);
221. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
222. break;
223. }
224. /* 3. Decrypt */
225. /*
226. * 模拟解密场景
227. * 3.1. 获取密钥别名
228. */
229. /*
230. * 3.2. 获取待解密的密文
231. */
232. /*
233. * 3.3. 获取解密算法参数配置
234. */
235. ohResult = InitParamSet(&decryptParamSet, g_decryptParams, sizeof(g_decryptParams) / sizeof(OH_Huks_Param));
236. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
237. break;
238. }
239. uint8_t plain[AES_COMMON_SIZE] = {0};
240. struct OH_Huks_Blob plainText = {AES_COMMON_SIZE, plain};
241. /*
242. * 3.4. 调用initSession获取handle
243. */
244. /*
245. * 3.5. 调用finishSession获取解密后的数据
246. */
247. ohResult = HksAesCipherTestDecrypt(&keyAlias, decryptParamSet, &cipherText, &plainText, &inData);
248. } while (0);
249. /* 4. Delete Key */
250. /*
251. * 模拟删除密钥场景
252. * 4.1. 获取密钥别名
253. */
254. /*
255. * 4.2. 调用deleteKeyItem删除密钥
256. */
257. (void)OH_Huks_DeleteKeyItem(&keyAlias, genParamSet);

259. OH_Huks_FreeParamSet(&genParamSet);
260. OH_Huks_FreeParamSet(&encryptParamSet);
261. OH_Huks_FreeParamSet(&decryptParamSet);

263. napi_value ret;
264. napi_create_int32(env, ohResult.errorCode, &ret);
265. return ret;
266. }
```

## X25519非对称密钥协商

### 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于生成群组密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-ndk.md)。

导出密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于导出群组密钥。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于协商群组密钥。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

删除密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于删除群组密钥。

### 开发示例

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <cstring>

6. static struct OH_Huks_Blob g_group = {(uint32_t)strlen("ohos.test.group"), (uint8_t *)"ohos.test.group"};
7. /* 初始化参数 */
8. static OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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
27. static struct OH_Huks_Blob g_keyAliasFinal1001 = {(uint32_t)strlen("HksECDHAgreeKeyAliasTest001_1_final"),
28. (uint8_t *)"HksECDHAgreeKeyAliasTest001_1_final"};
29. /* 集成密钥参数集 */
30. static struct OH_Huks_Param g_genAgreeParams[] = {
31. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
32. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
33. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
34. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
35. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
36. };
37. static struct OH_Huks_Param g_agreeParamsInit01[] = {
38. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
39. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
40. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
41. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
42. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
43. };
44. static struct OH_Huks_Param g_agreeParamsFinish01[] = {
45. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
46. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
47. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
48. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
49. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal1001},
50. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
51. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
52. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
53. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
54. };
55. static struct OH_Huks_Blob g_keyAliasFinal2001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2_final"),
56. (uint8_t *)"HksX25519AgreeKeyAliasTest001_2_final"};
57. static struct OH_Huks_Param g_agreeParamsInit02[] = {
58. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
59. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
60. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256},
61. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
62. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
63. };
64. static struct OH_Huks_Param g_agreeParamsFinish02[] = {
65. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
66. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
67. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
68. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
69. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_keyAliasFinal2001},
70. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
71. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
72. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
73. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
74. };
75. static const uint32_t X25519_COMMON_SIZE = 256;
76. static struct OH_Huks_Blob g_keyAlias01001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_1"),
77. (uint8_t *)"HksX25519AgreeKeyAliasTest001_1"};
78. static struct OH_Huks_Blob g_keyAlias02001 = {(uint32_t)strlen("HksX25519AgreeKeyAliasTest001_2"),
79. (uint8_t *)"HksX25519AgreeKeyAliasTest001_2"};

81. static OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
82. {
83. struct OH_Huks_Result ret;
84. ret.errorCode = OH_HUKS_SUCCESS;
85. if (blobSize == 0 || blobSize > X25519_COMMON_SIZE) {
86. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
87. return ret;
88. }
89. blob->data = (uint8_t *)malloc(blobSize);
90. if (blob->data == NULL) {
91. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
92. }
93. return ret;
94. }
95. /* 导出密钥 */
96. OH_Huks_Result HksX25519AgreeExport(const struct OH_Huks_Blob *keyAlias1, const struct OH_Huks_Blob *keyAlias2,
97. struct OH_Huks_Blob *publicKey1, struct OH_Huks_Blob *publicKey2,
98. const struct OH_Huks_ParamSet *genParamSet)
99. {
100. OH_Huks_Result ret = OH_Huks_ExportPublicKeyItem(keyAlias1, genParamSet, publicKey1);
101. if (ret.errorCode != OH_HUKS_SUCCESS) {
102. return ret;
103. }
104. ret = OH_Huks_ExportPublicKeyItem(keyAlias2, genParamSet, publicKey2);
105. if (ret.errorCode != OH_HUKS_SUCCESS) {
106. return ret;
107. }
108. return ret;
109. }
110. static const char *IN_DATA = "Hks_X25519_Agree_Test";
111. /* 协商密钥操作 */
112. OH_Huks_Result HksX25519AgreeFinish(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *publicKey,
113. const struct OH_Huks_ParamSet *initParamSet,
114. const struct OH_Huks_ParamSet *finishParamSet, struct OH_Huks_Blob *outData)
115. {
116. struct OH_Huks_Blob inData = {(uint32_t)strlen(IN_DATA), (uint8_t *)IN_DATA};
117. uint8_t handleU[sizeof(uint64_t)] = {0};
118. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
119. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, initParamSet, &handle, nullptr);
120. if (ret.errorCode != OH_HUKS_SUCCESS) {
121. return ret;
122. }
123. uint8_t outDataU[X25519_COMMON_SIZE] = {0};
124. struct OH_Huks_Blob outDataUpdate = {X25519_COMMON_SIZE, outDataU};
125. ret = OH_Huks_UpdateSession(&handle, initParamSet, publicKey, &outDataUpdate);
126. if (ret.errorCode != OH_HUKS_SUCCESS) {
127. return ret;
128. }
129. ret = OH_Huks_FinishSession(&handle, finishParamSet, &inData, outData);
130. if (ret.errorCode != OH_HUKS_SUCCESS) {
131. return ret;
132. }
133. return ret;
134. }

136. static OH_Huks_Result InitializeAgreeParamSets(struct OH_Huks_ParamSet **genParamSet,
137. struct OH_Huks_ParamSet **initParamSet01,
138. struct OH_Huks_ParamSet **finishParamSet01,
139. struct OH_Huks_ParamSet **initParamSet02,
140. struct OH_Huks_ParamSet **finishParamSet02)
141. {
142. OH_Huks_Result ohResult;

144. ohResult = InitParamSet(genParamSet, g_genAgreeParams,
145. sizeof(g_genAgreeParams) / sizeof(OH_Huks_Param));
146. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
147. return ohResult;
148. }
149. ohResult = InitParamSet(initParamSet01, g_agreeParamsInit01,
150. sizeof(g_agreeParamsInit01) / sizeof(OH_Huks_Param));
151. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
152. return ohResult;
153. }
154. ohResult = InitParamSet(finishParamSet01, g_agreeParamsFinish01,
155. sizeof(g_agreeParamsFinish01) / sizeof(OH_Huks_Param));
156. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
157. return ohResult;
158. }
159. ohResult = InitParamSet(initParamSet02, g_agreeParamsInit02,
160. sizeof(g_agreeParamsInit02) / sizeof(OH_Huks_Param));
161. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
162. return ohResult;
163. }
164. ohResult = InitParamSet(finishParamSet02, g_agreeParamsFinish02,
165. sizeof(g_agreeParamsFinish02) / sizeof(OH_Huks_Param));
166. return ohResult;
167. }

169. static OH_Huks_Result GenerateKeyPair(struct OH_Huks_ParamSet *genParamSet)
170. {
171. OH_Huks_Result ohResult;

173. /* 设备A生成密钥 */
174. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias01001, genParamSet, nullptr);
175. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
176. return ohResult;
177. }

179. /* 设备B生成密钥 */
180. ohResult = OH_Huks_GenerateKeyItem(&g_keyAlias02001, genParamSet, nullptr);
181. return ohResult;
182. }

184. static OH_Huks_Result KeyAgreement(struct OH_Huks_Blob *g_keyAlias,
185. struct OH_Huks_Blob *publicKey,
186. struct OH_Huks_Blob *outData,
187. struct OH_Huks_ParamSet *initParamSet,
188. struct OH_Huks_ParamSet *finishParamSet)
189. {
190. OH_Huks_Result ohResult;

192. ohResult = MallocAndCheckBlobData(outData, outData->size);
193. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
194. return ohResult;
195. }
196. /* 协商密钥 */
197. ohResult = HksX25519AgreeFinish(g_keyAlias, publicKey, initParamSet, finishParamSet, outData);
198. return ohResult;
199. }

201. static void CleanKey(struct OH_Huks_Blob *genKeyAlias,
202. struct OH_Huks_Blob *genKeyAliasFinal,
203. struct OH_Huks_ParamSet *genParamSet,
204. struct OH_Huks_ParamSet **initParamSet,
205. struct OH_Huks_ParamSet **finishParamSet)
206. {
207. OH_Huks_DeleteKeyItem(genKeyAlias, genParamSet);
208. OH_Huks_DeleteKeyItem(genKeyAliasFinal, genParamSet);
209. OH_Huks_FreeParamSet(initParamSet);
210. OH_Huks_FreeParamSet(finishParamSet);
211. }

213. /* 协商密钥整体流程 */
214. napi_value X25519AgreeKey(napi_env env, napi_callback_info info)
215. {
216. struct OH_Huks_ParamSet *genParamSet = nullptr;
217. struct OH_Huks_ParamSet *initParamSet01 = nullptr;
218. struct OH_Huks_ParamSet *finishParamSet01 = nullptr;
219. struct OH_Huks_ParamSet *initParamSet02 = nullptr;
220. struct OH_Huks_ParamSet *finishParamSet02 = nullptr;
221. struct OH_Huks_Blob publicKey01 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
222. struct OH_Huks_Blob publicKey02 = {.size = OH_HUKS_AES_KEY_SIZE_256, .data = nullptr};
223. struct OH_Huks_Blob outData01 = {.size = X25519_COMMON_SIZE, .data = nullptr};
224. struct OH_Huks_Blob outData02 = {.size = X25519_COMMON_SIZE, .data = nullptr};
225. OH_Huks_Result ohResult;
226. do {
227. /* 1.确定密钥别名集成密钥参数集 */
228. ohResult = InitializeAgreeParamSets(&genParamSet, &initParamSet01, &finishParamSet01,
229. &initParamSet02, &finishParamSet02);
230. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
231. break;
232. }
233. /* 2.设备A和设备B生成密钥 */
234. ohResult = GenerateKeyPair(genParamSet);
235. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
236. break;
237. }
238. ohResult = MallocAndCheckBlobData(&publicKey01, publicKey01.size);
239. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
240. break;
241. }
242. ohResult = MallocAndCheckBlobData(&publicKey02, publicKey02.size);
243. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
244. break;
245. }
246. /* 3.设备A、B导出公钥 */
247. ohResult = HksX25519AgreeExport(&g_keyAlias01001, &g_keyAlias02001, &publicKey01, &publicKey02, genParamSet);
248. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
249. break;
250. }
251. /* 4.设备A、B执行密钥协商 */
252. ohResult = KeyAgreement(&g_keyAlias01001, &publicKey02, &outData01, initParamSet01, finishParamSet01);
253. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
254. break;
255. }
256. ohResult = KeyAgreement(&g_keyAlias02001, &publicKey01, &outData02, initParamSet02, finishParamSet02);
257. } while (0);
258. free(publicKey01.data);
259. free(publicKey02.data);
260. free(outData01.data);
261. free(outData02.data);
262. /* 5.设备A、B删除密钥 */
263. CleanKey(&g_keyAlias01001, &g_keyAliasFinal1001, genParamSet, &initParamSet01, &finishParamSet01);
264. CleanKey(&g_keyAlias02001, &g_keyAliasFinal2001, genParamSet, &initParamSet02, &finishParamSet02);
265. OH_Huks_FreeParamSet(&genParamSet);

267. napi_value ret;
268. napi_create_int32(env, ohResult.errorCode, &ret);
269. return ret;
270. }
```

## PBKDF2派生密钥

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 密钥生成时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于生成群组密钥。
3. 调用[OH\_Huks\_GenerateKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_generatekeyitem)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions，添加参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于派生群组密钥。
2. 调用[OH\_Huks\_InitParamSet](../harmonyos-references/capi-native-huks-param-h.md#oh_huks_initparamset)指定算法参数配置。需要添加群组密钥标签[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)。
3. 调用[OH\_Huks\_InitSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_initsession)初始化密钥会话，并获取会话的句柄handle。
4. 调用[OH\_Huks\_UpdateSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_updatesession)更新密钥会话。
5. 调用[OH\_Huks\_FinishSession](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_finishsession)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用[OH\_Huks\_DeleteKeyItem](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_deletekeyitem)删除密钥，具体请参考[密钥删除](huks-delete-key-ndk.md)。

删除密钥时，指定参数[OH\_HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/capi-native-huks-type-h.md#oh_huks_tag)，用于删除群组密钥。

### 开发示例

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
25. static const uint32_t DERIVE_KEY_SIZE_32 = 32;
26. static const uint32_t DERIVE_KEY_SIZE_256 = 256;
27. static const uint32_t DERIVE_KEY_ITERATION = 10000;
28. static const uint32_t SALT_SIZE = 8;
29. static const char DERIVE_KEY_SALT[SALT_SIZE] = "mysalt1";
30. static struct OH_Huks_Blob g_deriveKeyAlias = {(uint32_t)strlen("test_derive"), (uint8_t *)"test_derive"};
31. static struct OH_Huks_Blob g_group = {(uint32_t)strlen("ohos.test.group"), (uint8_t *)"ohos.test.group"};
32. static struct OH_Huks_Param g_genDeriveParams[] = {
33. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
34. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
35. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
36. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
37. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
38. };
39. static struct OH_Huks_Param g_hkdfParams[] = {
40. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_PBKDF2},
41. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
42. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_SHA256},
43. {.tag = OH_HUKS_TAG_DERIVE_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_32},
44. {.tag = OH_HUKS_TAG_ITERATION, .uint32Param = DERIVE_KEY_ITERATION},
45. {.tag = OH_HUKS_TAG_SALT, .blob = {.size = SALT_SIZE, .data = (uint8_t *) DERIVE_KEY_SALT}},
46. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
47. };
48. static struct OH_Huks_Param g_hkdfFinishParams[] = {
49. {.tag = OH_HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG, .uint32Param = OH_HUKS_STORAGE_ONLY_USED_IN_HUKS},
50. {.tag = OH_HUKS_TAG_KEY_ALIAS, .blob = g_deriveKeyAlias},
51. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
52. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = DERIVE_KEY_SIZE_256},
53. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_DERIVE},
54. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
55. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
56. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_ECB},
57. {.tag = OH_HUKS_TAG_KEY_ACCESS_GROUP, .blob = g_group}
58. };
59. static const uint32_t COMMON_SIZE = 1024;
60. static const char *G_DERIVE_IN_DATA = "Hks_PBKDF2_Derive_Test_0_string";
61. static OH_Huks_Result PerformPbkdfDerivation(const struct OH_Huks_Blob *genAlias,
62. struct OH_Huks_ParamSet *hkdfParamSet,
63. struct OH_Huks_ParamSet *hkdfFinishParamSet,
64. const struct OH_Huks_Blob &inData)
65. {
66. OH_Huks_Result ohResult;
67. /* Init */
68. uint8_t handleD[sizeof(uint64_t)] = {0};
69. struct OH_Huks_Blob handleDerive = {sizeof(uint64_t), handleD};
70. ohResult = OH_Huks_InitSession(genAlias, hkdfParamSet, &handleDerive, nullptr);
71. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
72. return ohResult;
73. }
74. /* Update */
75. uint8_t tmpOut[COMMON_SIZE] = {0};
76. struct OH_Huks_Blob outData = {COMMON_SIZE, tmpOut};
77. ohResult = OH_Huks_UpdateSession(&handleDerive, hkdfParamSet, &inData, &outData);
78. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
79. return ohResult;
80. }
81. /* Finish */
82. uint8_t outDataD[COMMON_SIZE] = {0};
83. struct OH_Huks_Blob outDataDerive = {COMMON_SIZE, outDataD};
84. ohResult = OH_Huks_FinishSession(&handleDerive, hkdfFinishParamSet, &inData, &outDataDerive);
85. return ohResult;
86. }

88. napi_value PbkdfDeriveKey(napi_env env, napi_callback_info info)
89. {
90. struct OH_Huks_Blob genAlias = {(uint32_t)strlen("test_signVerify"), (uint8_t *)"test_signVerify"};
91. struct OH_Huks_Blob inData = {(uint32_t)strlen(G_DERIVE_IN_DATA), (uint8_t *)G_DERIVE_IN_DATA};
92. struct OH_Huks_ParamSet *genParamSet = nullptr;
93. struct OH_Huks_ParamSet *hkdfParamSet = nullptr;
94. struct OH_Huks_ParamSet *hkdfFinishParamSet = nullptr;
95. OH_Huks_Result ohResult;
96. do {
97. ohResult = InitParamSet(&genParamSet, g_genDeriveParams, sizeof(g_genDeriveParams) /
98. sizeof(OH_Huks_Param));
99. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
100. break;
101. }
102. ohResult = InitParamSet(&hkdfParamSet, g_hkdfParams, sizeof(g_hkdfParams) /
103. sizeof(OH_Huks_Param));
104. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
105. break;
106. }
107. ohResult =InitParamSet(&hkdfFinishParamSet, g_hkdfFinishParams, sizeof(g_hkdfFinishParams) /
108. sizeof(OH_Huks_Param));
109. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
110. break;
111. }
112. /* 1. 生成密钥 */
113. ohResult = OH_Huks_GenerateKeyItem(&genAlias, genParamSet, nullptr);
114. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
115. break;
116. }
117. /* 2. 派生密钥 */
118. ohResult = PerformPbkdfDerivation(&genAlias, hkdfParamSet, hkdfFinishParamSet, inData);
119. } while (0);
120. (void)OH_Huks_DeleteKeyItem(&genAlias, genParamSet);
121. (void)OH_Huks_DeleteKeyItem(&g_deriveKeyAlias, genParamSet);
122. OH_Huks_FreeParamSet(&genParamSet);
123. OH_Huks_FreeParamSet(&hkdfParamSet);
124. OH_Huks_FreeParamSet(&hkdfFinishParamSet);

126. napi_value ret;
127. napi_create_int32(env, ohResult.errorCode, &ret);
128. return ret;
129. }
```
