---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec-ndk
title: 指定密钥参数生成非对称密钥对(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定密钥参数生成非对称密钥对(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df271c1a3d109903dedcbc448101561b32b47731e1da4af08fc0fa9f527fe548
---

以RSA、ECC、SM2为例，根据指定的密钥参数，生成非对称密钥对（KeyPair），并获取密钥参数属性。

该对象可用于后续的加解密等操作。获取的密钥参数属性可用于存储或传输。

## 指定密钥参数生成RSA密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：RSA](crypto-asym-key-generation-conversion-spec.md#rsa)。

1. 调用[OH\_CryptoAsymKeySpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_create)，指定算法名为"RSA"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC，创建参数对象（keySpec）。
2. 指定uint8\_t类型的RSA密钥对数据（pk、sk、n），分别封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。
3. 调用[OH\_CryptoAsymKeySpec\_SetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_RSA\_E\_DATABLOB（pk）、CRYPTO\_RSA\_D\_DATABLOB（sk）、CRYPTO\_RSA\_N\_DATABLOB（n）, 依次传入封装后的[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)，设置参数对象（keySpec）。

   注意

   pk、sk、n均要以大端模式输入，且必须为正数。
4. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
5. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成RSA密钥对（keyPair）。
6. 分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_getparam)，获取RSA算法中私钥和公钥的各种密钥参数。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <string>
3. #define SPLIT_SIZE 2

5. static OH_Crypto_ErrCode GetRsaKeyParams(OH_CryptoKeyPair *keyCtx, Crypto_DataBlob *pubKeyData, Crypto_DataBlob *dataN)
6. {
7. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyCtx);
8. if (pubKey == nullptr) {
9. return CRYPTO_OPERTION_ERROR;
10. }
11. OH_Crypto_ErrCode ret = OH_CryptoPubKey_GetParam(pubKey, CRYPTO_RSA_E_DATABLOB, pubKeyData);
12. if (ret != CRYPTO_SUCCESS) {
13. return ret;
14. }
15. return OH_CryptoPubKey_GetParam(pubKey, CRYPTO_RSA_N_DATABLOB, dataN);
16. }

18. static void FreeRsaKeyParams(Crypto_DataBlob *pubKeyData, Crypto_DataBlob *dataN)
19. {
20. OH_Crypto_FreeDataBlob(pubKeyData);
21. OH_Crypto_FreeDataBlob(dataN);
22. }

24. size_t RsaConvertHex(uint8_t* dest, size_t count, const char* src)
25. {
26. size_t i;
27. int value;

29. for (i = 0; i < count && sscanf(src + i * SPLIT_SIZE, "%2x", &value) == 1; i++) {
30. dest[i] = value;
31. }
32. return i;
33. }

35. struct RsaParams {
36. Crypto_DataBlob nData;
37. Crypto_DataBlob eData;
38. uint8_t n[1024];
39. uint8_t e[20];
40. };

42. static void PrepareRsaParams(RsaParams *params)
43. {
44. std::string nStr = "9260d0750ae117eee55c3f3deaba74917521a262ee76007cdf8a56755ad73a1598a1408410a01434c3f"
45. "5bc54a88b57fa19fc4328daea0750a4c44e88cff3b2382621b80f670464433e4336e6d003e8cd65bff211da144b88291c2259a"
46. "00a72b711c116ef7686e8fee34e4d933c868187bdc26f7be071493c86f7a5941c3510806ad67b0f94d88f5cf5c02a092821d86"
47. "26e8932b65c5bd8c92049c210932b7afa7ac59c0e886ae5c1edb00d8ce2c57633db26bd6639bff73cee82be9275c402b4cf2a4"
48. "388da8cf8c64eefe1c5a0f5ab8057c39fa5c0589c3e253f0960332300f94bea44877b588e1edbde97cf2360727a09b775262d"
49. "7ee552b3319b9266f05a25";
50. std::string eStr = "010001";

52. size_t nLen = RsaConvertHex(params->n, nStr.size() / SPLIT_SIZE, nStr.c_str());
53. size_t eLen = RsaConvertHex(params->e, eStr.size() / SPLIT_SIZE, eStr.c_str());

55. params->nData = {.data = params->n, .len = nLen};
56. params->eData = {.data = params->e, .len = eLen};
57. }

59. static OH_Crypto_ErrCode CreateRsaKeySpec(RsaParams *params, OH_CryptoAsymKeySpec **keySpec)
60. {
61. OH_Crypto_ErrCode ret = OH_CryptoAsymKeySpec_Create("RSA", CRYPTO_ASYM_KEY_PUBLIC_KEY_SPEC, keySpec);
62. if (ret != CRYPTO_SUCCESS) {
63. return ret;
64. }

66. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_RSA_E_DATABLOB, &params->eData);
67. if (ret != CRYPTO_SUCCESS) {
68. OH_CryptoAsymKeySpec_Destroy(*keySpec);
69. return ret;
70. }

72. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_RSA_N_DATABLOB, &params->nData);
73. if (ret != CRYPTO_SUCCESS) {
74. OH_CryptoAsymKeySpec_Destroy(*keySpec);
75. return ret;
76. }

78. return CRYPTO_SUCCESS;
79. }

81. static OH_Crypto_ErrCode GenerateRsaKeyPair(OH_CryptoAsymKeySpec *keySpec,
82. OH_CryptoAsymKeyGeneratorWithSpec **generatorSpec, OH_CryptoKeyPair **keyPair)
83. {
84. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGeneratorWithSpec_Create(keySpec, generatorSpec);
85. if (ret != CRYPTO_SUCCESS) {
86. return ret;
87. }

89. ret = OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(*generatorSpec, keyPair);
90. if (ret != CRYPTO_SUCCESS) {
91. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(*generatorSpec);
92. return ret;
93. }

95. return CRYPTO_SUCCESS;
96. }

98. static OH_Crypto_ErrCode ValidateRsaKeyPair(OH_CryptoKeyPair *keyPair)
99. {
100. Crypto_DataBlob dataE = {.data = nullptr, .len = 0};
101. Crypto_DataBlob dataN = {.data = nullptr, .len = 0};
102. OH_Crypto_ErrCode ret = GetRsaKeyParams(keyPair, &dataE, &dataN);
103. if (ret != CRYPTO_SUCCESS) {
104. FreeRsaKeyParams(&dataE, &dataN);
105. return ret;
106. }
107. FreeRsaKeyParams(&dataE, &dataN);
108. return CRYPTO_SUCCESS;
109. }

111. OH_Crypto_ErrCode doTestRsaGenKeyPairBySpec()
112. {
113. RsaParams params = {};
114. PrepareRsaParams(&params);

116. OH_CryptoAsymKeySpec *keySpec = nullptr;
117. OH_Crypto_ErrCode ret = CreateRsaKeySpec(&params, &keySpec);
118. if (ret != CRYPTO_SUCCESS) {
119. return ret;
120. }

122. OH_CryptoAsymKeyGeneratorWithSpec *generatorSpec = nullptr;
123. OH_CryptoKeyPair *keyPair = nullptr;
124. ret = GenerateRsaKeyPair(keySpec, &generatorSpec, &keyPair);
125. if (ret != CRYPTO_SUCCESS) {
126. OH_CryptoAsymKeySpec_Destroy(keySpec);
127. return ret;
128. }

130. ret = ValidateRsaKeyPair(keyPair);

132. OH_CryptoKeyPair_Destroy(keyPair);
133. OH_CryptoAsymKeySpec_Destroy(keySpec);
134. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(generatorSpec);
135. return ret;
136. }
```

[rsa.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/cpp/types/project/rsa.cpp#L16-L155)

## 指定密钥参数生成ECC密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：ECC](crypto-asym-key-generation-conversion-spec.md#ecc)。

1. 调用[OH\_CryptoAsymKeySpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_create)，指定算法名为"ECC"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_COMMON\_PARAMS\_SPEC，创建参数对象（keySpec）。
2. 指定uint8\_t类型的ECC公私钥包含的公共参数（p、a、b、gx、gy、n、h），分别封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。
3. 调用[OH\_CryptoAsymKeySpec\_SetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_ECC\_FP\_P\_DATABLOB（p）、CRYPTO\_ECC\_A\_DATABLOB（a）、CRYPTO\_ECC\_B\_DATABLOB（b）、CRYPTO\_ECC\_G\_X\_DATABLOB（gx）、CRYPTO\_ECC\_G\_Y\_DATABLOB（gy）、CRYPTO\_ECC\_N\_DATABLOB（n）、CRYPTO\_ECC\_H\_INT（h）, 依次传入封装后的[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)，设置到参数对象（keySpec）。

   注意

   p、a、b、gx、gy、n、h均要以大端模式输入，且必须为正数。
4. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
5. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成ECC密钥对（keyPair）。
6. 分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_getparam)，获取ECC算法中私钥和公钥的各种密钥参数。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <string>

4. #define SPLIT_SIZE 2

6. static OH_Crypto_ErrCode GetEccKeyParams(OH_CryptoKeyPair *keyCtx, Crypto_DataBlob *pubKeyXData,
7. Crypto_DataBlob *pubKeyYData, Crypto_DataBlob *privKeyData)
8. {
9. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyCtx);
10. if (pubKey == nullptr) {
11. return CRYPTO_OPERTION_ERROR;
12. }
13. OH_Crypto_ErrCode ret = OH_CryptoPubKey_GetParam(pubKey, CRYPTO_ECC_PK_X_DATABLOB, pubKeyXData);
14. if (ret != CRYPTO_SUCCESS) {
15. return ret;
16. }
17. ret = OH_CryptoPubKey_GetParam(pubKey, CRYPTO_ECC_PK_Y_DATABLOB, pubKeyYData);
18. if (ret != CRYPTO_SUCCESS) {
19. return ret;
20. }

22. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyCtx);
23. if (privKey == nullptr) {
24. return CRYPTO_OPERTION_ERROR;
25. }
26. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_SK_DATABLOB, privKeyData);
27. return ret;
28. }

30. static void FreeEccKeyParams(Crypto_DataBlob *pubKeyXData, Crypto_DataBlob *pubKeyYData, Crypto_DataBlob *privKeyData)
31. {
32. OH_Crypto_FreeDataBlob(pubKeyXData);
33. OH_Crypto_FreeDataBlob(pubKeyYData);
34. OH_Crypto_FreeDataBlob(privKeyData);
35. }

37. struct EccCommonParams {
38. Crypto_DataBlob pData;
39. Crypto_DataBlob aData;
40. Crypto_DataBlob bData;
41. Crypto_DataBlob gxData;
42. Crypto_DataBlob gyData;
43. Crypto_DataBlob nData;
44. Crypto_DataBlob hData;
45. };

47. static OH_Crypto_ErrCode GetEccCommonParams(OH_CryptoKeyPair *keyCtx, EccCommonParams *params)
48. {
49. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyCtx);
50. if (privKey == nullptr) {
51. return CRYPTO_OPERTION_ERROR;
52. }
53. OH_Crypto_ErrCode ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_FP_P_DATABLOB, &params->pData);
54. if (ret != CRYPTO_SUCCESS) {
55. return ret;
56. }
57. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_A_DATABLOB, &params->aData);
58. if (ret != CRYPTO_SUCCESS) {
59. return ret;
60. }
61. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_B_DATABLOB, &params->bData);
62. if (ret != CRYPTO_SUCCESS) {
63. return ret;
64. }
65. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_G_X_DATABLOB, &params->gxData);
66. if (ret != CRYPTO_SUCCESS) {
67. return ret;
68. }
69. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_G_Y_DATABLOB, &params->gyData);
70. if (ret != CRYPTO_SUCCESS) {
71. return ret;
72. }
73. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_N_DATABLOB, &params->nData);
74. if (ret != CRYPTO_SUCCESS) {
75. return ret;
76. }
77. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_H_INT, &params->hData);
78. if (ret != CRYPTO_SUCCESS) {
79. return ret;
80. }
81. return ret;
82. }

84. static void FreeEccCommonParams(EccCommonParams *params)
85. {
86. OH_Crypto_FreeDataBlob(&params->pData);
87. OH_Crypto_FreeDataBlob(&params->aData);
88. OH_Crypto_FreeDataBlob(&params->bData);
89. OH_Crypto_FreeDataBlob(&params->gxData);
90. OH_Crypto_FreeDataBlob(&params->gyData);
91. OH_Crypto_FreeDataBlob(&params->nData);
92. OH_Crypto_FreeDataBlob(&params->hData);
93. }

95. size_t ConvertHex(uint8_t* dest, size_t count, const char* src)
96. {
97. size_t i;
98. int value;

100. for (i = 0; i < count && sscanf(src + i * SPLIT_SIZE, "%2x", &value) == 1; i++) {
101. dest[i] = value;
102. }
103. return i;
104. }

106. struct EccParams {
107. Crypto_DataBlob pData;
108. Crypto_DataBlob aData;
109. Crypto_DataBlob bData;
110. Crypto_DataBlob gxData;
111. Crypto_DataBlob gyData;
112. Crypto_DataBlob nData;
113. Crypto_DataBlob hData;
114. uint8_t p[256];
115. uint8_t gx[256];
116. uint8_t gy[256];
117. uint8_t a[256];
118. uint8_t b[256];
119. uint8_t n[256];
120. uint8_t h[4];
121. };

123. static void PrepareEccParams(EccParams *params)
124. {
125. std::string pStr = "ffffffffffffffffffffffffffffffff000000000000000000000001";
126. std::string gxStr = "b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21";
127. std::string gyStr = "bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34";
128. std::string aStr = "fffffffffffffffffffffffffffffffefffffffffffffffffffffffe";
129. std::string bStr = "b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4";
130. std::string nStr = "ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d";
131. uint8_t h[] = {0x00, 0x00, 0x00, 0x01}; // 大端序

133. size_t pLen = ConvertHex(params->p, pStr.size() / SPLIT_SIZE, pStr.c_str());
134. size_t gxLen = ConvertHex(params->gx, gxStr.size() / SPLIT_SIZE, gxStr.c_str());
135. size_t gyLen = ConvertHex(params->gy, gyStr.size() / SPLIT_SIZE, gyStr.c_str());
136. size_t aLen = ConvertHex(params->a, aStr.size() / SPLIT_SIZE, aStr.c_str());
137. size_t bLen = ConvertHex(params->b, bStr.size() / SPLIT_SIZE, bStr.c_str());
138. size_t nLen = ConvertHex(params->n, nStr.size() / SPLIT_SIZE, nStr.c_str());

140. params->pData = {.data = params->p, .len = pLen};
141. params->aData = {.data = params->a, .len = aLen};
142. params->bData = {.data = params->b, .len = bLen};
143. params->gxData = {.data = params->gx, .len = gxLen};
144. params->gyData = {.data = params->gy, .len = gyLen};
145. params->nData = {.data = params->n, .len = nLen};
146. params->hData = {.data = h, .len = sizeof(h)};
147. }

149. static OH_Crypto_ErrCode CreateEccKeySpec(EccParams *params, OH_CryptoAsymKeySpec **keySpec)
150. {
151. OH_Crypto_ErrCode ret = OH_CryptoAsymKeySpec_Create("ECC", CRYPTO_ASYM_KEY_COMMON_PARAMS_SPEC, keySpec);
152. if (ret != CRYPTO_SUCCESS) {
153. return ret;
154. }

156. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_FP_P_DATABLOB, &params->pData);
157. if (ret != CRYPTO_SUCCESS) {
158. OH_CryptoAsymKeySpec_Destroy(*keySpec);
159. return ret;
160. }

162. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_A_DATABLOB, &params->aData);
163. if (ret != CRYPTO_SUCCESS) {
164. OH_CryptoAsymKeySpec_Destroy(*keySpec);
165. return ret;
166. }

168. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_B_DATABLOB, &params->bData);
169. if (ret != CRYPTO_SUCCESS) {
170. OH_CryptoAsymKeySpec_Destroy(*keySpec);
171. return ret;
172. }

174. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_G_X_DATABLOB, &params->gxData);
175. if (ret != CRYPTO_SUCCESS) {
176. OH_CryptoAsymKeySpec_Destroy(*keySpec);
177. return ret;
178. }

180. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_G_Y_DATABLOB, &params->gyData);
181. if (ret != CRYPTO_SUCCESS) {
182. OH_CryptoAsymKeySpec_Destroy(*keySpec);
183. return ret;
184. }

186. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_N_DATABLOB, &params->nData);
187. if (ret != CRYPTO_SUCCESS) {
188. OH_CryptoAsymKeySpec_Destroy(*keySpec);
189. return ret;
190. }

192. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_H_INT, &params->hData);
193. if (ret != CRYPTO_SUCCESS) {
194. OH_CryptoAsymKeySpec_Destroy(*keySpec);
195. return ret;
196. }

198. return CRYPTO_SUCCESS;
199. }

201. static OH_Crypto_ErrCode GenerateEccKeyPair(OH_CryptoAsymKeySpec *keySpec,
202. OH_CryptoAsymKeyGeneratorWithSpec **generatorSpec, OH_CryptoKeyPair **keyPair)
203. {
204. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGeneratorWithSpec_Create(keySpec, generatorSpec);
205. if (ret != CRYPTO_SUCCESS) {
206. return ret;
207. }

209. ret = OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(*generatorSpec, keyPair);
210. if (ret != CRYPTO_SUCCESS) {
211. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(*generatorSpec);
212. return ret;
213. }

215. return CRYPTO_SUCCESS;
216. }

218. static OH_Crypto_ErrCode ValidateEccKeyPair(OH_CryptoKeyPair *keyPair)
219. {
220. Crypto_DataBlob dataPkX = {.data = nullptr, .len = 0};
221. Crypto_DataBlob dataPkY = {.data = nullptr, .len = 0};
222. Crypto_DataBlob dataSk = {.data = nullptr, .len = 0};
223. OH_Crypto_ErrCode ret = GetEccKeyParams(keyPair, &dataPkX, &dataPkY, &dataSk);
224. if (ret != CRYPTO_SUCCESS) {
225. FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
226. return ret;
227. }
228. FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);

230. EccCommonParams commonParams = {};
231. ret = GetEccCommonParams(keyPair, &commonParams);
232. if (ret != CRYPTO_SUCCESS) {
233. FreeEccCommonParams(&commonParams);
234. return ret;
235. }
236. FreeEccCommonParams(&commonParams);

238. return CRYPTO_SUCCESS;
239. }

241. OH_Crypto_ErrCode doTestEccGenKeyPairBySpec()
242. {
243. EccParams params = {};
244. PrepareEccParams(&params);

246. OH_CryptoAsymKeySpec *keySpec = nullptr;
247. OH_Crypto_ErrCode ret = CreateEccKeySpec(&params, &keySpec);
248. if (ret != CRYPTO_SUCCESS) {
249. return ret;
250. }

252. OH_CryptoAsymKeyGeneratorWithSpec *generatorSpec = nullptr;
253. OH_CryptoKeyPair *keyPair = nullptr;
254. ret = GenerateEccKeyPair(keySpec, &generatorSpec, &keyPair);
255. if (ret != CRYPTO_SUCCESS) {
256. OH_CryptoAsymKeySpec_Destroy(keySpec);
257. return ret;
258. }

260. ret = ValidateEccKeyPair(keyPair);

262. OH_CryptoKeyPair_Destroy(keyPair);
263. OH_CryptoAsymKeySpec_Destroy(keySpec);
264. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(generatorSpec);
265. return ret;
266. }
```

[ecc.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/cpp/types/project/ecc.cpp#L16-L285)

## 根据椭圆曲线名生成SM2密钥对

对应的算法规格请查看[非对称密钥生成和转换规格：SM2](crypto-asym-key-generation-conversion-spec.md#sm2)。

1. 调用[OH\_CryptoAsymKeySpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_create)，指定算法名为"SM2"， 密钥参数类型为CRYPTO\_ASYM\_KEY\_KEY\_PAIR\_SPEC，创建密钥参数对象（keySpec）。
2. 调用[OH\_CryptoAsymKeySpec\_GenEcCommonParamsSpec](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_geneccommonparamsspec)，指定曲线为"NID\_sm2"， 生成SM2公共参数对象（sm2CommonSpec）。
3. 调用[OH\_CryptoAsymKeySpec\_SetCommonParamsSpec](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setcommonparamsspec)，将生成SM2公共参数对象（sm2CommonSpec）设置到密钥参数对象（keySpec）。
4. 指定uint8\_t类型的SM2密钥对数据（pkx、pky、sk），分别封装成[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)。
5. 调用[OH\_CryptoAsymKeySpec\_SetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeyspec_setparam)，指定参数类型分别为CRYPTO\_ECC\_PK\_X\_DATABLOB（pkx）、CRYPTO\_ECC\_PK\_Y\_DATABLOB（pky）、CRYPTO\_ECC\_SK\_DATABLOB（sk）, 依次传入封装后的[Crypto\_DataBlob](../harmonyos-references/capi-cryptocommonapi-crypto-datablob.md)，设置到参数对象（keySpec）。

   注意

   pkx、pky、sk均要以大端模式输入，且必须为正数。
6. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_Create](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_create)，将参数对象（keySpec）传入，创建非对称密钥生成器（generatorSpec）。
7. 调用[OH\_CryptoAsymKeyGeneratorWithSpec\_GenKeyPair](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoasymkeygeneratorwithspec_genkeypair)，生成SM2密钥对（keyPair）。
8. 分别传入密钥对中的私钥和公钥，调用[OH\_CryptoPrivKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptoprivkey_getparam)和[OH\_CryptoPubKey\_GetParam](../harmonyos-references/capi-crypto-asym-key-h.md#oh_cryptopubkey_getparam)，获取SM2算法中私钥和公钥的各种密钥参数。

```
1. #include "CryptoArchitectureKit/crypto_architecture_kit.h"
2. #include <string>
3. #define SPLIT_SIZE 2

5. static OH_Crypto_ErrCode GetEccKeyParams(OH_CryptoKeyPair *keyCtx, Crypto_DataBlob *pubKeyXData,
6. Crypto_DataBlob *pubKeyYData, Crypto_DataBlob *privKeyData)
7. {
8. OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyCtx);
9. if (pubKey == nullptr) {
10. return CRYPTO_OPERTION_ERROR;
11. }
12. OH_Crypto_ErrCode ret = OH_CryptoPubKey_GetParam(pubKey, CRYPTO_ECC_PK_X_DATABLOB, pubKeyXData);
13. if (ret != CRYPTO_SUCCESS) {
14. return ret;
15. }
16. ret = OH_CryptoPubKey_GetParam(pubKey, CRYPTO_ECC_PK_Y_DATABLOB, pubKeyYData);
17. if (ret != CRYPTO_SUCCESS) {
18. return ret;
19. }

21. OH_CryptoPrivKey *privKey = OH_CryptoKeyPair_GetPrivKey(keyCtx);
22. if (privKey == nullptr) {
23. return CRYPTO_OPERTION_ERROR;
24. }
25. ret = OH_CryptoPrivKey_GetParam(privKey, CRYPTO_ECC_SK_DATABLOB, privKeyData);
26. return ret;
27. }

29. static void FreeEccKeyParams(Crypto_DataBlob *pubKeyXData, Crypto_DataBlob *pubKeyYData, Crypto_DataBlob *privKeyData)
30. {
31. OH_Crypto_FreeDataBlob(pubKeyXData);
32. OH_Crypto_FreeDataBlob(pubKeyYData);
33. OH_Crypto_FreeDataBlob(privKeyData);
34. }

36. size_t Sm2ConvertHex(uint8_t* dest, size_t count, const char* src)
37. {
38. size_t i;
39. int value;

41. for (i = 0; i < count && sscanf(src + i * SPLIT_SIZE, "%2x", &value) == 1; i++) {
42. dest[i] = value;
43. }
44. return i;
45. }

47. struct Sm2Params {
48. Crypto_DataBlob pkXData;
49. Crypto_DataBlob pkYData;
50. Crypto_DataBlob skData;
51. uint8_t pkX[256];
52. uint8_t pkY[256];
53. uint8_t sk[256];
54. };

56. static void PrepareSm2Params(Sm2Params *params)
57. {
58. std::string pkXStr = "67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4";
59. std::string pkYStr = "D48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071";
60. std::string skStr = "6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074";

62. size_t pkXLen = Sm2ConvertHex(params->pkX, pkXStr.size() / SPLIT_SIZE, pkXStr.c_str());
63. size_t pkYLen = Sm2ConvertHex(params->pkY, pkYStr.size() / SPLIT_SIZE, pkYStr.c_str());
64. size_t skLen = Sm2ConvertHex(params->sk, skStr.size() / SPLIT_SIZE, skStr.c_str());

66. params->pkXData = {.data = params->pkX, .len = pkXLen};
67. params->pkYData = {.data = params->pkY, .len = pkYLen};
68. params->skData = {.data = params->sk, .len = skLen};
69. }

71. static OH_Crypto_ErrCode CreateSm2KeySpec(Sm2Params *params, OH_CryptoAsymKeySpec **keySpec,
72. OH_CryptoAsymKeySpec **sm2CommonSpec)
73. {
74. OH_Crypto_ErrCode ret = OH_CryptoAsymKeySpec_Create("SM2", CRYPTO_ASYM_KEY_KEY_PAIR_SPEC, keySpec);
75. if (ret != CRYPTO_SUCCESS) {
76. return ret;
77. }

79. ret = OH_CryptoAsymKeySpec_GenEcCommonParamsSpec("NID_sm2", sm2CommonSpec);
80. if (ret != CRYPTO_SUCCESS) {
81. OH_CryptoAsymKeySpec_Destroy(*keySpec);
82. return ret;
83. }

85. ret = OH_CryptoAsymKeySpec_SetCommonParamsSpec(*keySpec, *sm2CommonSpec);
86. if (ret != CRYPTO_SUCCESS) {
87. OH_CryptoAsymKeySpec_Destroy(*sm2CommonSpec);
88. OH_CryptoAsymKeySpec_Destroy(*keySpec);
89. return ret;
90. }

92. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_PK_X_DATABLOB, &params->pkXData);
93. if (ret != CRYPTO_SUCCESS) {
94. OH_CryptoAsymKeySpec_Destroy(*sm2CommonSpec);
95. OH_CryptoAsymKeySpec_Destroy(*keySpec);
96. return ret;
97. }

99. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_PK_Y_DATABLOB, &params->pkYData);
100. if (ret != CRYPTO_SUCCESS) {
101. OH_CryptoAsymKeySpec_Destroy(*sm2CommonSpec);
102. OH_CryptoAsymKeySpec_Destroy(*keySpec);
103. return ret;
104. }

106. ret = OH_CryptoAsymKeySpec_SetParam(*keySpec, CRYPTO_ECC_SK_DATABLOB, &params->skData);
107. if (ret != CRYPTO_SUCCESS) {
108. OH_CryptoAsymKeySpec_Destroy(*sm2CommonSpec);
109. OH_CryptoAsymKeySpec_Destroy(*keySpec);
110. return ret;
111. }

113. return CRYPTO_SUCCESS;
114. }

116. static OH_Crypto_ErrCode GenerateSm2KeyPair(OH_CryptoAsymKeySpec *keySpec,
117. OH_CryptoAsymKeyGeneratorWithSpec **generatorSpec, OH_CryptoKeyPair **keyPair)
118. {
119. OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGeneratorWithSpec_Create(keySpec, generatorSpec);
120. if (ret != CRYPTO_SUCCESS) {
121. return ret;
122. }

124. ret = OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(*generatorSpec, keyPair);
125. if (ret != CRYPTO_SUCCESS) {
126. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(*generatorSpec);
127. return ret;
128. }

130. return CRYPTO_SUCCESS;
131. }

133. static OH_Crypto_ErrCode ValidateSm2KeyPair(OH_CryptoKeyPair *keyPair)
134. {
135. Crypto_DataBlob dataPkX = {.data = nullptr, .len = 0};
136. Crypto_DataBlob dataPkY = {.data = nullptr, .len = 0};
137. Crypto_DataBlob dataSk = {.data = nullptr, .len = 0};
138. OH_Crypto_ErrCode ret = GetEccKeyParams(keyPair, &dataPkX, &dataPkY, &dataSk);
139. if (ret != CRYPTO_SUCCESS) {
140. FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
141. return ret;
142. }
143. FreeEccKeyParams(&dataPkX, &dataPkY, &dataSk);
144. return CRYPTO_SUCCESS;
145. }

147. OH_Crypto_ErrCode doTestSm2GenKeyPairBySpec()
148. {
149. Sm2Params params = {};
150. PrepareSm2Params(&params);

152. OH_CryptoAsymKeySpec *keySpec = nullptr;
153. OH_CryptoAsymKeySpec *sm2CommonSpec = nullptr;
154. OH_Crypto_ErrCode ret = CreateSm2KeySpec(&params, &keySpec, &sm2CommonSpec);
155. if (ret != CRYPTO_SUCCESS) {
156. return ret;
157. }

159. OH_CryptoAsymKeyGeneratorWithSpec *generatorSpec = nullptr;
160. OH_CryptoKeyPair *keyPair = nullptr;
161. ret = GenerateSm2KeyPair(keySpec, &generatorSpec, &keyPair);
162. if (ret != CRYPTO_SUCCESS) {
163. OH_CryptoAsymKeySpec_Destroy(sm2CommonSpec);
164. OH_CryptoAsymKeySpec_Destroy(keySpec);
165. return ret;
166. }

168. ret = ValidateSm2KeyPair(keyPair);

170. OH_CryptoKeyPair_Destroy(keyPair);
171. OH_CryptoAsymKeyGeneratorWithSpec_Destroy(generatorSpec);
172. OH_CryptoAsymKeySpec_Destroy(sm2CommonSpec);
173. OH_CryptoAsymKeySpec_Destroy(keySpec);
174. return ret;
175. }
```

[sm2.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/SpecifiedParametersGenerateAsymmetricKeyPair/entry/src/main/cpp/types/project/sm2.cpp#L16-L194)
