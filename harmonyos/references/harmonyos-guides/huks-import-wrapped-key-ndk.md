---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-wrapped-key-ndk
title: 安全导入密钥(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 安全导入密钥(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f4d386bde5948a588882f51011d16e4ce21320f6b2137a8f6a0ce227729f262
---

以安全导入ECDH密钥对为例，涉及业务侧加密密钥的[密钥生成](huks-key-generation-overview.md)、[协商](huks-key-agreement-overview.md)等操作不在本示例中体现。

具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)。

## 在CMake脚本中链接相关动态库

```
1. target_link_libraries(entry PUBLIC libhuks_ndk.z.so)
```

## 开发步骤

1. 设备A（导入设备）将待导入密钥转换成[HUKS密钥材料格式](huks-concepts.md#密钥材料格式)To\_Import\_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤）。
2. 设备B（被导入设备）生成一个安全导入用途的非对称密钥对Wrapping\_Key（公钥Wrapping\_Pk，私钥Wrapping\_Sk），导出Wrapping\_Key的公钥材料Wrapping\_Pk发送给设备A。
3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller\_Key（公钥Caller\_Pk，私钥Caller\_Sk），导出Caller\_Key的公钥材料Caller\_Pk并保存。
4. 设备A生成一个对称密钥Caller\_Kek，该密钥用于加密To\_Import\_Key生成To\_Import\_Key\_Enc。
5. 设备A基于Caller\_Key的私钥Caller\_Sk和设备B Wrapping\_Key的公钥Wrapping\_Pk，协商出Shared\_Key，使用Shared\_Key加密Caller\_Kek，生成Caller\_Kek\_Enc。
6. 设备A封装Caller\_Pk、Caller\_Kek\_Enc、To\_Import\_Key\_Enc等安全导入的密钥材料并发送给设备B，安全导入密钥材料格式见[安全导入密钥材料格式](huks-key-import-overview.md#安全导入密钥材料格式)。
7. 设备B导入封装的加密密钥材料。
8. 设备A、B删除用于安全导入的密钥。

## 开发案例

构造安全导入密钥的参数集

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <algorithm>

6. #define MAX_MALLOC_SIZE 0x800000

8. OH_Huks_Result InitParamSet(struct OH_Huks_ParamSet **paramSet, const struct OH_Huks_Param *params,
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
27. struct HksImportWrappedKeyTestParams {
28. // server key, for real.
29. struct OH_Huks_Blob *wrappingKeyAlias;
30. struct OH_Huks_ParamSet *genWrappingKeyParamSet;
31. uint32_t publicKeySize;
32. struct OH_Huks_Blob *callerKeyAlias;
33. struct OH_Huks_ParamSet *genCallerKeyParamSet;
34. struct OH_Huks_Blob *callerKekAlias;
35. struct OH_Huks_Blob *callerKek;
36. struct OH_Huks_ParamSet *importCallerKekParamSet;
37. struct OH_Huks_Blob *callerAgreeKeyAlias;
38. struct OH_Huks_ParamSet *agreeParamSet;
39. struct OH_Huks_ParamSet *importWrappedKeyParamSet;
40. struct OH_Huks_Blob *importedKeyAlias;
41. struct OH_Huks_Blob *importedPlainKey;
42. uint32_t keyMaterialLen;
43. };
44. static const uint32_t IV_SIZE = 16;
45. static uint8_t IV[IV_SIZE] = "bababababababab"; // 此处仅为测试数据，实际使用时该值每次应该不同。
46. static const uint32_t WRAPPED_KEY_IV_SIZE = 16;
47. static uint8_t WRAPPED_KEY_IV[IV_SIZE] = "bababababababab"; // 此处仅为测试数据，实际使用时该值每次应该不同。
48. static const uint32_t AAD_SIZE = 16;
49. static uint8_t AAD[AAD_SIZE] = "abababababababa"; // 此处仅为测试数据，实际使用时该值每次应该不同。
50. static const uint32_t NONCE_SIZE = 12;
51. static uint8_t NONCE[NONCE_SIZE] = "hahahahahah"; // 此处仅为测试数据，实际使用时该值每次应该不同。
52. static const uint32_t AEAD_TAG_SIZE = 16;
53. static const uint32_t X25519_256_SIZE = 256;
54. static struct OH_Huks_Blob g_wrappingKeyAliasAes256 = {.size = (uint32_t)strlen("test_wrappingKey_x25519_aes256"),
55. .data = (uint8_t *)"test_wrappingKey_x25519_aes256"};
56. static struct OH_Huks_Blob g_callerKeyAliasAes256 = {.size = (uint32_t)strlen("test_caller_key_x25519_aes256"),
57. .data = (uint8_t *)"test_caller_key_x25519_aes256"};
58. static struct OH_Huks_Blob g_callerKekAliasAes256 = {.size = (uint32_t)strlen("test_caller_kek_x25519_aes256"),
59. .data = (uint8_t *)"test_caller_kek_x25519_aes256"};
60. static struct OH_Huks_Blob g_callerAes256Kek = {.size = (uint32_t)strlen("This is kek to encrypt plain key"),
61. .data = (uint8_t *)"This is kek to encrypt plain key"};
62. static struct OH_Huks_Blob g_callerAgreeKeyAliasAes256 = {.size =
63. (uint32_t)strlen("test_caller_agree_key_x25519_aes256"),
64. .data = (uint8_t *)"test_caller_agree_key_x25519_aes256"};
65. static struct OH_Huks_Blob g_importedKeyAliasAes256 = {.size = (uint32_t)strlen("test_import_key_x25519_aes256"),
66. .data = (uint8_t *)"test_import_key_x25519_aes256"};
67. static struct OH_Huks_Blob g_importedAes256PlainKey = {.size = (uint32_t)strlen("This is plain key to be imported"),
68. .data = (uint8_t *)"This is plain key to be imported"};
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/cpp/napi_init.cpp#L16-L86)

```
1. static struct OH_Huks_Param g_importWrappedAes256Params[] = {
2. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
3. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT | OH_HUKS_KEY_PURPOSE_DECRYPT},
4. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
5. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
6. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
7. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
8. {.tag = OH_HUKS_TAG_UNWRAP_ALGORITHM_SUITE, .uint32Param = OH_HUKS_UNWRAP_SUITE_X25519_AES_256_GCM_NOPADDING},
9. {.tag = OH_HUKS_TAG_ASSOCIATED_DATA,
10. .blob = {.size = AAD_SIZE, .data = (uint8_t *)AAD}}, // 此处仅为测试数据，实际使用时该值应与调用者信息相关。
11. {.tag = OH_HUKS_TAG_NONCE,
12. .blob = {.size = NONCE_SIZE, .data = (uint8_t *)NONCE}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
13. static const uint32_t g_x25519PubKeySize = 32;
14. static struct OH_Huks_Param g_genWrappingKeyParams[] = {
15. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
16. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_UNWRAP},
17. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256}};
18. static struct OH_Huks_Param g_genCallerX25519Params[] = {
19. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
20. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
21. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256}};
22. static struct OH_Huks_Param g_importParamsCallerKek[] = {
23. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
24. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
25. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
26. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
27. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
28. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
29. {.tag = OH_HUKS_TAG_IV,
30. .blob = {.size = WRAPPED_KEY_IV_SIZE,
31. .data = (uint8_t *)WRAPPED_KEY_IV}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
32. static struct OH_Huks_Param g_callerAgreeParams[] = {
33. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_X25519},
34. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_AGREE},
35. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_CURVE25519_KEY_SIZE_256}};
36. static struct OH_Huks_Param g_aesKekEncryptParams[] = {
37. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
38. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
39. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
40. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
41. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
42. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
43. {.tag = OH_HUKS_TAG_ASSOCIATED_DATA,
44. .blob = {.size = AAD_SIZE, .data = (uint8_t *)AAD}}, // 此处仅为测试数据，实际使用时该值应与调用者信息相关。
45. {.tag = OH_HUKS_TAG_NONCE,
46. .blob = {.size = NONCE_SIZE, .data = (uint8_t *)NONCE}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
47. static struct OH_Huks_Param g_importAgreeKeyParams[] = {
48. {.tag = OH_HUKS_TAG_ALGORITHM, .uint32Param = OH_HUKS_ALG_AES},
49. {.tag = OH_HUKS_TAG_PURPOSE, .uint32Param = OH_HUKS_KEY_PURPOSE_ENCRYPT},
50. {.tag = OH_HUKS_TAG_KEY_SIZE, .uint32Param = OH_HUKS_AES_KEY_SIZE_256},
51. {.tag = OH_HUKS_TAG_PADDING, .uint32Param = OH_HUKS_PADDING_NONE},
52. {.tag = OH_HUKS_TAG_BLOCK_MODE, .uint32Param = OH_HUKS_MODE_GCM},
53. {.tag = OH_HUKS_TAG_DIGEST, .uint32Param = OH_HUKS_DIGEST_NONE},
54. {.tag = OH_HUKS_TAG_IV,
55. .blob = {.size = IV_SIZE, .data = (uint8_t *)IV}}}; // 此处仅为测试数据，实际使用时该值每次应该不同。
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/cpp/napi_init.cpp#L88-L144)

安全导入密钥的核心函数实现

```
1. OH_Huks_Result HuksAgreeKey(const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *keyAlias,
2. const struct OH_Huks_Blob *peerPublicKey, struct OH_Huks_Blob *agreedKey)
3. {
4. uint8_t temp[10] = {0};
5. struct OH_Huks_Blob inData = {sizeof(temp), temp};
6. uint8_t handleU[sizeof(uint64_t)] = {0};
7. struct OH_Huks_Blob handle = {sizeof(uint64_t), handleU};
8. OH_Huks_Result ret = OH_Huks_InitSession(keyAlias, paramSet, &handle, nullptr);
9. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
10. return ret;
11. }
12. uint8_t outDataU[1024] = {0};
13. struct OH_Huks_Blob outDataUpdate = {1024, outDataU};
14. ret = OH_Huks_UpdateSession(&handle, paramSet, peerPublicKey, &outDataUpdate);
15. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
16. return ret;
17. }
18. ret = OH_Huks_FinishSession(&handle, paramSet, &inData, agreedKey);
19. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
20. return ret;
21. }
22. return ret;
23. }

25. OH_Huks_Result MallocAndCheckBlobData(struct OH_Huks_Blob *blob, const uint32_t blobSize)
26. {
27. struct OH_Huks_Result ret;
28. ret.errorCode = OH_HUKS_SUCCESS;
29. if (blobSize == 0 || blobSize > MAX_MALLOC_SIZE) {
30. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
31. }
32. blob->data = (uint8_t *)malloc(blobSize);
33. if (blob->data == NULL) {
34. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
35. }
36. return ret;
37. }

39. static const uint32_t TIMES = 4;
40. static const uint32_t MAX_UPDATE_SIZE = 64;
41. static const uint32_t MAX_OUTDATA_SIZE = MAX_UPDATE_SIZE * TIMES;
42. #define HUKS_FREE_BLOB(blob)                                                                                           \
43. do {                                                                                                               \
44. if ((blob).data != nullptr) {                                                                                  \
45. free((blob).data);                                                                                         \
46. (blob).data = nullptr;                                                                                     \
47. }                                                                                                              \
48. (blob).size = 0;                                                                                               \
49. } while (0)
50. #define OH_HUKS_KEY_BYTES(keySize) (((keySize) + 7) / 8)
51. static OH_Huks_Result HksEncryptLoopUpdate(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet,
52. const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
53. {
54. struct OH_Huks_Result ret;
55. ret.errorCode = OH_HUKS_SUCCESS;
56. struct OH_Huks_Blob inDataSeg = *inData;
57. uint8_t *lastPtr = inData->data + inData->size - 1;
58. struct OH_Huks_Blob outDataSeg = {MAX_OUTDATA_SIZE, NULL};
59. uint8_t *cur = outData->data;
60. outData->size = 0;
61. inDataSeg.size = MAX_UPDATE_SIZE;
62. bool isFinished = false;
63. while (inDataSeg.data <= lastPtr) {
64. if (inDataSeg.data + MAX_UPDATE_SIZE <= lastPtr) {
65. outDataSeg.size = MAX_OUTDATA_SIZE;
66. } else {
67. isFinished = true;
68. inDataSeg.size = lastPtr - inDataSeg.data + 1;
69. break;
70. }
71. if (MallocAndCheckBlobData(&outDataSeg, outDataSeg.size).errorCode != (int32_t)OH_HUKS_SUCCESS) {
72. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
73. return ret;
74. }
75. ret = OH_Huks_UpdateSession(handle, paramSet, &inDataSeg, &outDataSeg);
76. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
77. free(outDataSeg.data);
78. return ret;
79. }
80. std::copy(outDataSeg.data, outDataSeg.data + outDataSeg.size, cur);
81. cur += outDataSeg.size;
82. outData->size += outDataSeg.size;
83. free(outDataSeg.data);
84. if ((isFinished == false) && (inDataSeg.data + MAX_UPDATE_SIZE > lastPtr)) {
85. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
86. return ret;
87. }
88. inDataSeg.data += MAX_UPDATE_SIZE;
89. }
90. struct OH_Huks_Blob outDataFinish = {inDataSeg.size * TIMES, NULL};
91. if (MallocAndCheckBlobData(&outDataFinish, outDataFinish.size).errorCode != (int32_t)OH_HUKS_SUCCESS) {
92. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
93. return ret;
94. }
95. ret = OH_Huks_FinishSession(handle, paramSet, &inDataSeg, &outDataFinish);
96. if (ret.errorCode != OH_HUKS_SUCCESS) {
97. free(outDataFinish.data);
98. return ret;
99. }
100. std::copy(outDataFinish.data, outDataFinish.data + outDataFinish.size, cur);
101. outData->size += outDataFinish.size;
102. free(outDataFinish.data);
103. return ret;
104. }
105. OH_Huks_Result HuksEncrypt(const struct OH_Huks_Blob *key, const struct OH_Huks_ParamSet *paramSet,
106. const struct OH_Huks_Blob *plainText, struct OH_Huks_Blob *cipherText)
107. {
108. uint8_t handle[sizeof(uint64_t)] = {0};
109. struct OH_Huks_Blob handleBlob = {sizeof(uint64_t), handle};
110. OH_Huks_Result ret = OH_Huks_InitSession(key, paramSet, &handleBlob, nullptr);
111. if (ret.errorCode != OH_HUKS_SUCCESS) {
112. return ret;
113. }
114. ret = HksEncryptLoopUpdate(&handleBlob, paramSet, plainText, cipherText);
115. return ret;
116. }
117. static OH_Huks_Result BuildWrappedKeyData(struct OH_Huks_Blob **blobArray, uint32_t size,
118. struct OH_Huks_Blob *outData)
119. {
120. uint32_t totalLength = size * sizeof(uint32_t);
121. struct OH_Huks_Result ret;
122. ret.errorCode = OH_HUKS_SUCCESS;
123. /* 计算大小 */
124. for (uint32_t i = 0; i < size; ++i) {
125. totalLength += blobArray[i]->size;
126. }
127. struct OH_Huks_Blob outBlob = {0, nullptr};
128. outBlob.size = totalLength;
129. ret = MallocAndCheckBlobData(&outBlob, outBlob.size);
130. if (ret.errorCode != OH_HUKS_SUCCESS) {
131. return ret;
132. }
133. uint32_t offset = 0;
134. /* 拷贝数据 */
135. for (uint32_t i = 0; i < size; ++i) {
136. if (totalLength - offset >= sizeof(blobArray[i]->size)) {
137. std::copy(reinterpret_cast<uint8_t *>(&blobArray[i]->size),
138. reinterpret_cast<uint8_t *>(&blobArray[i]->size) + sizeof(blobArray[i]->size),
139. outBlob.data + offset);
140. } else {
141. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
142. return ret;
143. }
144. offset += sizeof(blobArray[i]->size);
145. if (totalLength - offset >= blobArray[i]->size) {
146. std::copy(blobArray[i]->data, blobArray[i]->data + blobArray[i]->size, outBlob.data + offset);
147. } else {
148. ret.errorCode = OH_HUKS_ERR_CODE_INTERNAL_ERROR;
149. return ret;
150. }
151. offset += blobArray[i]->size;
152. }
153. outData->size = outBlob.size;
154. outData->data = outBlob.data;
155. return ret;
156. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/cpp/napi_init.cpp#L146-L303)

```
1. static OH_Huks_Result CheckParamsValid(const struct HksImportWrappedKeyTestParams *params)
2. {
3. struct OH_Huks_Result ret;
4. ret.errorCode = OH_HUKS_SUCCESS;
5. if (params == nullptr) {
6. ret.errorCode = OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT;
7. return ret;
8. }
9. if (params->wrappingKeyAlias == nullptr || params->genWrappingKeyParamSet == nullptr ||
10. params->callerKeyAlias == nullptr || params->genCallerKeyParamSet == nullptr ||
11. params->callerKekAlias == nullptr || params->callerKek == nullptr ||
12. params->importCallerKekParamSet == nullptr || params->callerAgreeKeyAlias == nullptr ||
13. params->agreeParamSet == nullptr || params->importWrappedKeyParamSet == nullptr ||
14. params->importedKeyAlias == nullptr || params->importedPlainKey == nullptr) {
15. ret.errorCode = OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT;
16. return ret;
17. }
18. return ret;
19. }

21. static OH_Huks_Result GenerateAndExportHuksPublicKey(const struct HksImportWrappedKeyTestParams *params,
22. struct OH_Huks_Blob *huksPublicKey)
23. {
24. OH_Huks_Result ret = OH_Huks_GenerateKeyItem(params->wrappingKeyAlias, params->genWrappingKeyParamSet, nullptr);
25. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
26. return ret;
27. }
28. huksPublicKey->size = params->publicKeySize;
29. ret = MallocAndCheckBlobData(huksPublicKey, huksPublicKey->size);
30. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
31. return ret;
32. }
33. ret = OH_Huks_ExportPublicKeyItem(params->wrappingKeyAlias, nullptr, huksPublicKey);
34. return ret;
35. }
36. static OH_Huks_Result GenerateAndExportCallerPublicKey(const struct HksImportWrappedKeyTestParams *params,
37. struct OH_Huks_Blob *callerSelfPublicKey)
38. {
39. OH_Huks_Result ret = OH_Huks_GenerateKeyItem(params->callerKeyAlias, params->genCallerKeyParamSet, nullptr);
40. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
41. return ret;
42. }
43. callerSelfPublicKey->size = params->publicKeySize;
44. ret = MallocAndCheckBlobData(callerSelfPublicKey, callerSelfPublicKey->size);
45. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
46. return ret;
47. }
48. ret = OH_Huks_ExportPublicKeyItem(params->callerKeyAlias, params->genWrappingKeyParamSet, callerSelfPublicKey);
49. return ret;
50. }

52. static OH_Huks_Result ImportKekAndAgreeSharedSecret(const struct HksImportWrappedKeyTestParams *params,
53. const struct OH_Huks_Blob *huksPublicKey,
54. struct OH_Huks_Blob *outSharedKey)
55. {
56. OH_Huks_Result ret =
57. OH_Huks_ImportKeyItem(params->callerKekAlias, params->importCallerKekParamSet, params->callerKek);
58. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
59. return ret;
60. }
61. ret = MallocAndCheckBlobData(outSharedKey, outSharedKey->size);
62. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
63. return ret;
64. }
65. ret = HuksAgreeKey(params->agreeParamSet, params->callerKeyAlias, huksPublicKey, outSharedKey);
66. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
67. return ret;
68. }
69. struct OH_Huks_ParamSet *importAgreeKeyParams = nullptr;
70. ret = InitParamSet(&importAgreeKeyParams, g_importAgreeKeyParams,
71. sizeof(g_importAgreeKeyParams) / sizeof(OH_Huks_Param));
72. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
73. return ret;
74. }
75. ret = OH_Huks_ImportKeyItem(params->callerAgreeKeyAlias, importAgreeKeyParams, outSharedKey);
76. OH_Huks_FreeParamSet(&importAgreeKeyParams);
77. return ret;
78. }
79. static OH_Huks_Result EncryptImportedPlainKeyAndKek(const struct HksImportWrappedKeyTestParams *params,
80. struct OH_Huks_Blob *plainCipherText,
81. struct OH_Huks_Blob *kekCipherText)
82. {
83. struct OH_Huks_ParamSet *encryptParamSet = nullptr;
84. OH_Huks_Result ret =
85. InitParamSet(&encryptParamSet, g_aesKekEncryptParams, sizeof(g_aesKekEncryptParams) / sizeof(OH_Huks_Param));
86. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
87. return ret;
88. }
89. ret = HuksEncrypt(params->callerKekAlias, encryptParamSet, params->importedPlainKey, plainCipherText);
90. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
91. return ret;
92. }
93. ret = HuksEncrypt(params->callerAgreeKeyAlias, encryptParamSet, params->callerKek, kekCipherText);
94. OH_Huks_FreeParamSet(&encryptParamSet);
95. return ret;
96. }
97. static OH_Huks_Result ImportWrappedKey(const struct HksImportWrappedKeyTestParams *params,
98. struct OH_Huks_Blob *plainCipher, struct OH_Huks_Blob *kekCipherText,
99. struct OH_Huks_Blob *peerPublicKey, struct OH_Huks_Blob *wrappedKeyData)
100. {
101. struct OH_Huks_Blob commonAad = {.size = AAD_SIZE, .data = reinterpret_cast<uint8_t *>(AAD)};
102. struct OH_Huks_Blob commonNonce = {.size = NONCE_SIZE, .data = reinterpret_cast<uint8_t *>(NONCE)};
103. struct OH_Huks_Blob keyMaterialLen = {.size = sizeof(uint32_t), .data = (uint8_t *)&params->keyMaterialLen};
104. /* 从密文中拷贝AEAD的tag并缩小其大小 */
105. const uint32_t tagSize = AEAD_TAG_SIZE;
106. uint8_t kekTagBuf[tagSize] = {0};
107. struct OH_Huks_Blob kekTag = {.size = tagSize, .data = kekTagBuf};
108. std::copy(plainCipher->data + (plainCipher->size - tagSize),
109. plainCipher->data + (plainCipher->size - tagSize) + tagSize, kekTag.data);
110. plainCipher->size -= tagSize;
111. /* 从密钥加密密钥的密文中拷贝AEAD的tag并缩小其大小 */
112. uint8_t agreeKeyTagBuf[tagSize] = {0};
113. struct OH_Huks_Blob agreeKeyTag = {.size = tagSize, .data = agreeKeyTagBuf};
114. std::copy(kekCipherText->data + (kekCipherText->size - tagSize),
115. kekCipherText->data + (kekCipherText->size - tagSize) + tagSize, agreeKeyTagBuf);
116. kekCipherText->size -= tagSize;
117. struct OH_Huks_Blob *blobArray[] = {peerPublicKey, &commonAad,   &commonNonce, &agreeKeyTag,    kekCipherText,
118. &commonAad,    &commonNonce, &kekTag,      &keyMaterialLen, plainCipher};
119. OH_Huks_Result ret = BuildWrappedKeyData(blobArray, OH_HUKS_IMPORT_WRAPPED_KEY_TOTAL_BLOBS, wrappedKeyData);
120. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
121. return ret;
122. }
123. struct OH_Huks_Param *purpose = nullptr;
124. ret = OH_Huks_GetParam(params->importWrappedKeyParamSet, OH_HUKS_TAG_PURPOSE, &purpose);
125. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
126. return ret;
127. }
128. ret = OH_Huks_ImportWrappedKeyItem(params->importedKeyAlias, params->wrappingKeyAlias,
129. params->importWrappedKeyParamSet, wrappedKeyData);
130. return ret;
131. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/cpp/napi_init.cpp#L305-L437)

安全导入密钥的完整流程实现

```
1. OH_Huks_Result HksImportWrappedKeyTestCommonCase(const struct HksImportWrappedKeyTestParams *params)
2. {
3. OH_Huks_Result ret = CheckParamsValid(params);
4. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
5. return ret;
6. }
7. struct OH_Huks_Blob huksPublicKey = {0, nullptr};
8. struct OH_Huks_Blob callerSelfPublicKey = {0, nullptr};
9. struct OH_Huks_Blob outSharedKey = {.size = OH_HUKS_KEY_BYTES(OH_HUKS_AES_KEY_SIZE_256), .data = nullptr};
10. struct OH_Huks_Blob wrappedKeyData = {0, nullptr};
11. uint8_t plainKeyCipherBuffer[OH_HUKS_MAX_KEY_SIZE] = {0};
12. struct OH_Huks_Blob plainCipherText = {OH_HUKS_MAX_KEY_SIZE, plainKeyCipherBuffer};
13. uint8_t kekCipherTextBuffer[OH_HUKS_MAX_KEY_SIZE] = {0};
14. struct OH_Huks_Blob kekCipherText = {OH_HUKS_MAX_KEY_SIZE, kekCipherTextBuffer};
15. /* 模拟安全导入密钥场景，设备A为远端设备（导入设备），设备B为本端设备（被导入设备） */
16. do {
17. /**
18. * 1. 设备A将待导入密钥转换成HUKS密钥材料格式To_Import_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤），
19. *   本示例使用g_importedAes256PlainKey（对称密钥）作为模拟
20. */
21. /**
22. * 2. 设备B生成一个加密导入用途的、用于协商的非对称密钥对Wrapping_Key（公钥Wrapping_Pk，私钥Wrapping_Sk），
23. * 导出Wrapping_Key公钥Wrapping_Pk存放在变量huksPublicKey中
24. */
25. ret = GenerateAndExportHuksPublicKey(params, &huksPublicKey);
26. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
27. break;
28. }
29. /**
30. * 3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller_Key（公钥Caller_Pk，私钥Caller_Sk），
31. * 导出Caller_Key公钥Caller_Pk存放在变量callerSelfPublicKey中
32. */
33. ret = GenerateAndExportCallerPublicKey(params, &callerSelfPublicKey);
34. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
35. break;
36. }
37. /**
38. * 4. 设备A生成一个对称密钥Caller_Kek，该密钥后续将用于加密To_Import_Key
39. * 设备A基于Caller_Key的私钥Caller_Sk和设备B Wrapping_Key的公钥Wrapping_Pk，协商出Shared_Key
40. */
41. ret = ImportKekAndAgreeSharedSecret(params, &huksPublicKey, &outSharedKey);
42. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
43. break;
44. }
45. /**
46. * 5. 设备A使用Caller_Kek加密To_Import_Key，生成To_Import_Key_Enc
47. * 设备A使用Shared_Key加密Caller_Kek，生成Caller_Kek_Enc
48. */
49. ret = EncryptImportedPlainKeyAndKek(params, &plainCipherText, &kekCipherText);
50. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
51. break;
52. }
53. /**
54. * 6. 设备A封装Caller_Pk、To_Import_Key_Enc、Caller_Kek_Enc等安全导入的材料并发送给设备B。
55. * 本示例作为变量存放在callerSelfPublicKey，plainCipherText，kekCipherText
56. * 7. 设备B导入封装的加密密钥材料
57. */
58. ret = ImportWrappedKey(params, &plainCipherText, &kekCipherText, &callerSelfPublicKey, &wrappedKeyData);
59. } while (0);
60. /* 8. 设备A、B删除用于安全导入的密钥 */
61. HUKS_FREE_BLOB(huksPublicKey);
62. HUKS_FREE_BLOB(callerSelfPublicKey);
63. HUKS_FREE_BLOB(outSharedKey);
64. HUKS_FREE_BLOB(wrappedKeyData);
65. return ret;
66. }

68. void HksClearKeysForWrappedKeyTest(const struct HksImportWrappedKeyTestParams *params)
69. {
70. OH_Huks_Result ret = CheckParamsValid(params);
71. if (ret.errorCode != (int32_t)OH_HUKS_SUCCESS) {
72. return;
73. }
74. (void)OH_Huks_DeleteKeyItem(params->wrappingKeyAlias, nullptr);
75. (void)OH_Huks_DeleteKeyItem(params->callerKeyAlias, nullptr);
76. (void)OH_Huks_DeleteKeyItem(params->callerKekAlias, nullptr);
77. (void)OH_Huks_DeleteKeyItem(params->callerAgreeKeyAlias, nullptr);
78. (void)OH_Huks_DeleteKeyItem(params->importedKeyAlias, nullptr);
79. }

81. static OH_Huks_Result InitCommonTestParamsAndDoImport(struct HksImportWrappedKeyTestParams *importWrappedKeyTestParams,
82. const struct OH_Huks_Param *importedKeyParamSetArray,
83. uint32_t arraySize)
84. {
85. struct OH_Huks_ParamSet *genX25519KeyParamSet = nullptr;
86. struct OH_Huks_ParamSet *genCallerKeyParamSet = nullptr;
87. struct OH_Huks_ParamSet *callerImportParamsKek = nullptr;
88. struct OH_Huks_ParamSet *agreeParamSet = nullptr;
89. struct OH_Huks_ParamSet *importPlainKeyParams = nullptr;
90. OH_Huks_Result ret;
91. do {
92. ret = InitParamSet(&genX25519KeyParamSet, g_genWrappingKeyParams,
93. sizeof(g_genWrappingKeyParams) / sizeof(OH_Huks_Param));
94. if (ret.errorCode != OH_HUKS_SUCCESS) {
95. break;
96. }
97. importWrappedKeyTestParams->genWrappingKeyParamSet = genX25519KeyParamSet;
98. importWrappedKeyTestParams->publicKeySize = g_x25519PubKeySize;
99. ret = InitParamSet(&genCallerKeyParamSet, g_genCallerX25519Params,
100. sizeof(g_genCallerX25519Params) / sizeof(OH_Huks_Param));
101. if (ret.errorCode != OH_HUKS_SUCCESS) {
102. break;
103. }
104. importWrappedKeyTestParams->genCallerKeyParamSet = genCallerKeyParamSet;
105. ret = InitParamSet(&callerImportParamsKek, g_importParamsCallerKek,
106. sizeof(g_importParamsCallerKek) / sizeof(OH_Huks_Param));
107. if (ret.errorCode != OH_HUKS_SUCCESS) {
108. break;
109. }
110. importWrappedKeyTestParams->importCallerKekParamSet = callerImportParamsKek;
111. ret = InitParamSet(&agreeParamSet, g_callerAgreeParams, sizeof(g_callerAgreeParams) / sizeof(OH_Huks_Param));
112. if (ret.errorCode != OH_HUKS_SUCCESS) {
113. break;
114. }
115. importWrappedKeyTestParams->agreeParamSet = agreeParamSet;
116. ret = InitParamSet(&importPlainKeyParams, importedKeyParamSetArray, arraySize);
117. if (ret.errorCode != OH_HUKS_SUCCESS) {
118. break;
119. }
120. importWrappedKeyTestParams->importWrappedKeyParamSet = importPlainKeyParams;
121. ret = HksImportWrappedKeyTestCommonCase(importWrappedKeyTestParams);
122. } while (0);
123. OH_Huks_FreeParamSet(&genX25519KeyParamSet);
124. OH_Huks_FreeParamSet(&genCallerKeyParamSet);
125. OH_Huks_FreeParamSet(&callerImportParamsKek);
126. OH_Huks_FreeParamSet(&agreeParamSet);
127. OH_Huks_FreeParamSet(&importPlainKeyParams);
128. return ret;
129. }
130. static napi_value NAPI_Global_importWrappedKey(napi_env env, napi_callback_info info)
131. {
132. struct HksImportWrappedKeyTestParams importWrappedKeyTestParams001 = {0};
133. importWrappedKeyTestParams001.wrappingKeyAlias = &g_wrappingKeyAliasAes256;
134. importWrappedKeyTestParams001.keyMaterialLen = g_importedAes256PlainKey.size;
135. importWrappedKeyTestParams001.callerKeyAlias = &g_callerKeyAliasAes256;
136. importWrappedKeyTestParams001.callerKekAlias = &g_callerKekAliasAes256;
137. importWrappedKeyTestParams001.callerKek = &g_callerAes256Kek;
138. importWrappedKeyTestParams001.callerAgreeKeyAlias = &g_callerAgreeKeyAliasAes256;
139. importWrappedKeyTestParams001.importedKeyAlias = &g_importedKeyAliasAes256;
140. importWrappedKeyTestParams001.importedPlainKey = &g_importedAes256PlainKey;
141. OH_Huks_Result ohResult =
142. InitCommonTestParamsAndDoImport(&importWrappedKeyTestParams001, g_importWrappedAes256Params,
143. sizeof(g_importWrappedAes256Params) / sizeof(struct OH_Huks_Param));
144. HksClearKeysForWrappedKeyTest(&importWrappedKeyTestParams001);
145. napi_value ret;
146. napi_create_int32(env, ohResult.errorCode, &ret);
147. return ret;
148. }

150. static napi_value IsKeyExist(napi_env env, napi_callback_info info)
151. {
152. /* 1.指定密钥别名 */
153. struct OH_Huks_Blob keyAlias = {
154. (uint32_t)strlen("test_key"),
155. (uint8_t *)"test_key"
156. };

158. /* 2.调用OH_Huks_IsKeyItemExist判断密钥是否存在 */
159. struct OH_Huks_Result ohResult = OH_Huks_IsKeyItemExist(&keyAlias, NULL);
160. napi_value ret;
161. napi_create_int32(env, ohResult.errorCode, &ret);
162. return ret;
163. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/cpp/napi_init.cpp#L439-L601)

## 调测验证

调用[OH\_Huks\_IsKeyItemExist](../harmonyos-references/capi-native-huks-api-h.md#oh_huks_iskeyitemexist)验证密钥是否存在，如密钥存在即表示密钥导入成功。

```
1. #include "huks/native_huks_api.h"
2. #include "huks/native_huks_param.h"
3. #include "napi/native_api.h"
4. #include <string.h>
5. static napi_value IsKeyExist(napi_env env, napi_callback_info info)
6. {
7. /* 1.指定密钥别名 */
8. struct OH_Huks_Blob keyAlias = {
9. (uint32_t)strlen("test_key"),
10. (uint8_t *)"test_key"
11. };

13. /* 2.调用OH_Huks_IsKeyItemExist判断密钥是否存在 */
14. struct OH_Huks_Result ohResult = OH_Huks_IsKeyItemExist(&keyAlias, NULL);
15. if (ohResult.errorCode != OH_HUKS_SUCCESS) {
16. // 失败。
17. } else {
18. // 成功。
19. }
20. napi_value ret;
21. napi_create_int32(env, ohResult.errorCode, &ret);
22. return ret;
23. }
```
