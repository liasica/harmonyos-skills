---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-envelop-key-arkts
title: 数字信封导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 数字信封导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a310c681a7a2a98de7af080571c9181a578aa093c3f1ef947395960a55e2d18
---

从API 23开始支持[数字信封](huks-key-import-overview.md#数字信封导入)特性。

以数字信封导入RSA密钥和AES密钥为例。具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)，其中**数字信封导入密钥不支持DSA算法**。

使用数字信封导入密钥需要使用[HUKS\_TAG\_UNWRAP\_ALGORITHM\_SUITE](../harmonyos-references/js-apis-huks.md#hukstag)标签，该标签值为[HUKS\_UNWRAP\_SUITE\_SM2\_SM4\_ECB\_NOPADDING](../harmonyos-references/js-apis-huks.md#huksunwrapsuite9)。

数字信封导入密钥时，如果是导入非对称密钥的密钥对，需要添加[HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA](../harmonyos-references/js-apis-huks.md#hukstag)标签，并将公钥以X.509 DER格式封装填入该标签，且针对非对称密钥仅支持以密钥对形式导入。

## 开发步骤

1. 业务方设备（设备A）生成SM4密钥，cipherSm4。
2. 设备A使用生成的SM4密钥加密将导入密钥importKey，加密使用ECB/NoPadding模式，enImportKey=Encrypt(cipherSm4, importKey)。
3. 密钥导入方（设备B）导出SM2公钥，设备A接收该密钥。
4. 设备A使用收到的SM2公钥加密生成的SM4密钥，enSm4=Encrypt(Sm2, cipherSm4)。
5. 设备A将数字信封数据发送给设备B。
6. 设备B使用导入WrappedKey导入数字信封密钥。若导入密钥是对称密钥，此步骤只需对裸密钥进行加密。若导入非对称密钥的密钥对，则将公钥以DER格式封装，并放入[HUKS\_TAG\_ASYMMETRIC\_PUBLIC\_KEY\_DATA](../harmonyos-references/js-apis-huks.md#hukstag)中。

### RSA

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { huks } from "@kit.UniversalKeystoreKit";

4. function intToUint8Array(value: number): Uint8Array
5. {
6. const buffer = new ArrayBuffer(4);
7. const view = new DataView(buffer);
8. view.setUint32(0, value, true);
9. return new Uint8Array(buffer);
10. }

12. function concatUint8Arrays(arrays: Uint8Array[]): Uint8Array
13. {
14. const totalLength = arrays.reduce((sum, arr) => sum + arr.length, 0);
15. const result = new Uint8Array(totalLength);
16. let offset = 0;
17. for (const arr of arrays) {
18. result.set(arr, offset);
19. offset += arr.length;
20. }
21. return result;
22. }

24. let wrappingParamSetSm2: Array<huks.HuksParam> = [
25. {
26. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
27. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
28. },
29. {
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_SM2
32. },
33. {
34. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
35. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
36. },
37. {
38. tag: huks.HuksTag.HUKS_TAG_DIGEST,
39. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
40. },
41. {
42. tag: huks.HuksTag.HUKS_TAG_PADDING,
43. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
44. }
45. ];
46. let option: huks.HuksOptions = { properties: wrappingParamSetSm2 };

48. let sm4PlainData = new Uint8Array([
49. 0xb9, 0xef, 0x35, 0x49, 0xb7, 0x00, 0x91, 0x58, 0x0c, 0x6f, 0x43, 0x28, 0xf8, 0x95, 0x1c, 0x02,
50. ]);

52. let enParamSm2: Array<huks.HuksParam> = [
53. {
54. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
55. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
56. },
57. {
58. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
59. value: huks.HuksKeyAlg.HUKS_ALG_SM2
60. },
61. {
62. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
63. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
64. },
65. {
66. tag: huks.HuksTag.HUKS_TAG_DIGEST,
67. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
68. },
69. {
70. tag: huks.HuksTag.HUKS_TAG_PADDING,
71. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
72. }
73. ];

75. let enOption: huks.HuksOptions = {
76. properties: enParamSm2,
77. inData: sm4PlainData
78. };

80. let cipherData: Uint8Array;
81. let handle: number;

83. async function EnvelopRsaTest()
84. {
85. let wrappingKeyAlias = "WrappedKey";
86. await huks.generateKeyItem(wrappingKeyAlias, option)

88. // 使用生成的Sm2密钥加密Sm4密钥
89. await huks.initSession(wrappingKeyAlias, enOption)
90. .then((data) => {
91. handle = data.handle;
92. }).catch((error: BusinessError) => {
93. console.error('decrypt init fail, errorCode: ${error.code}')
94. })
95. await huks.finishSession(handle, enOption)
96. .then((data) => {
97. console.info('encrypt success')
98. cipherData = data.outData as Uint8Array
99. }).catch((error: BusinessError) => {
100. console.error(`encrypt finish fail, errorCode: ${error.code}`)
101. })

103. let enDataRsa: Uint8Array = new Uint8Array([
104. 0x4a, 0xce, 0x89, 0xa6, 0xda, 0x85, 0x6d, 0x56, 0xb3, 0xab, 0xc9, 0x70, 0x5e, 0x3f, 0xb6, 0x0e,
105. 0x07, 0xdf, 0xdf, 0x9c, 0xb3, 0x05, 0xd4, 0x8d, 0xc0, 0xac, 0x9b, 0x13, 0x3d, 0x1b, 0xdb, 0xa0,
106. 0x46, 0x1a, 0xc8, 0x82, 0x80, 0xe0, 0x2a, 0x28, 0x34, 0xa6, 0x4a, 0x97, 0x91, 0x58, 0xc8, 0x8c,
107. 0x0f, 0xa2, 0xeb, 0xe1, 0xf8, 0x37, 0x54, 0x99, 0x7e, 0xa1, 0xce, 0x1e, 0xf3, 0x8b, 0x8c, 0x8d,
108. 0xec, 0x58, 0xb7, 0x32, 0x29, 0x36, 0x34, 0x46, 0x92, 0x67, 0x09, 0xb3, 0xb4, 0xb3, 0x74, 0x3a,
109. 0x77, 0x99, 0xd7, 0x4b, 0x1f, 0xf6, 0xa6, 0xb0, 0x99, 0x3d, 0x3e, 0x92, 0xba, 0xcf, 0x83, 0xd0,
110. 0x1e, 0x18, 0x68, 0x1a, 0xb5, 0xfe, 0x18, 0x6d, 0x9d, 0xc2, 0x39, 0x48, 0x2e, 0x52, 0xfc, 0x33,
111. 0x16, 0xb0, 0x58, 0xd5, 0xdf, 0x84, 0xbe, 0xfe, 0xe1, 0xfa, 0xa9, 0x65, 0x34, 0xb8, 0x97, 0xa3,
112. 0x9a, 0x45, 0x8a, 0x40, 0x4b, 0x09, 0xdf, 0x1c, 0x48, 0x57, 0x3f, 0xb2, 0x1f, 0xf3, 0x21, 0x7d,
113. 0xa8, 0xa5, 0xed, 0xe1, 0x61, 0x2f, 0xe0, 0xda, 0xae, 0x15, 0x22, 0x18, 0xf6, 0x84, 0x7d, 0x39,
114. 0xae, 0x35, 0x49, 0xec, 0xd8, 0x66, 0xff, 0x65, 0x7d, 0xd9, 0x74, 0x19, 0xad, 0x26, 0x64, 0xc0,
115. 0x2d, 0x93, 0xf5, 0x83, 0x7d, 0x8d, 0x98, 0x35, 0x2e, 0x67, 0xf9, 0xc0, 0xb1, 0xd7, 0x2b, 0xb5,
116. 0x49, 0x98, 0x3a, 0x31, 0xa0, 0x66, 0x71, 0x6e, 0x09, 0x70, 0xef, 0x56, 0x14, 0x9e, 0xb8, 0xd2,
117. 0x17, 0x99, 0x44, 0x69, 0xcd, 0x3d, 0xcb, 0x3c, 0xfe, 0xbe, 0x72, 0xc0, 0x43, 0x29, 0x86, 0x70,
118. 0x9d, 0xa3, 0xc0, 0x68, 0xf6, 0x7e, 0x48, 0x2c, 0x4e, 0x48, 0xe0, 0xf6, 0xa9, 0xcb, 0x28, 0x63,
119. 0xe8, 0x33, 0xfc, 0xb4, 0x1a, 0x06, 0xf4, 0x13, 0x20, 0xfd, 0x90, 0x90, 0x1c, 0x25, 0xd7, 0xf8,
120. ]);

122. let publicKey: Uint8Array = new Uint8Array([
123. 0x30, 0x82, 0x01, 0x22, 0x30, 0x0d, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86, 0xf7, 0x0d, 0x01, 0x01,
124. 0x01, 0x05, 0x00, 0x03, 0x82, 0x01, 0x0f, 0x00, 0x30, 0x82, 0x01, 0x0a, 0x02, 0x82, 0x01, 0x01,
125. 0x00, 0xa2, 0xd2, 0x3c, 0xe9, 0x87, 0x8b, 0x48, 0x34, 0xdd, 0x41, 0xe0, 0x65, 0x39, 0xcc, 0xea,
126. 0x25, 0x25, 0xa6, 0x9e, 0x9f, 0x20, 0xc6, 0x13, 0x9f, 0xb2, 0xa7, 0xf3, 0x77, 0x69, 0xfd, 0xa9,
127. 0xbd, 0xe8, 0x2c, 0xf3, 0x87, 0x3a, 0xc0, 0x2a, 0x01, 0x1f, 0x8d, 0x0f, 0x59, 0x28, 0x34, 0xfb,
128. 0xe3, 0x8d, 0x9b, 0xa1, 0xe0, 0xe4, 0x60, 0x7d, 0x20, 0x19, 0x49, 0x6f, 0x13, 0x5e, 0xae, 0x3e,
129. 0x4d, 0x6c, 0x31, 0x6c, 0x0b, 0x90, 0xf8, 0xd2, 0xf3, 0x45, 0x4f, 0x3b, 0x9f, 0x8e, 0x3b, 0x77,
130. 0x20, 0x9e, 0x54, 0xec, 0x7b, 0x54, 0x15, 0xf0, 0x09, 0x8f, 0x5a, 0xf9, 0x87, 0x9a, 0x27, 0x23,
131. 0x99, 0x64, 0x4d, 0x8c, 0x80, 0x5c, 0x2e, 0xee, 0xc3, 0x57, 0x6e, 0x3d, 0x91, 0xfb, 0x77, 0x67,
132. 0x3b, 0x8a, 0xed, 0x01, 0xb5, 0x91, 0x33, 0xa1, 0xaa, 0xb2, 0x0d, 0x49, 0x25, 0x7c, 0x4d, 0x42,
133. 0xde, 0xfb, 0xcd, 0xd6, 0x48, 0xb8, 0xce, 0xe7, 0x22, 0x71, 0x43, 0x54, 0x2c, 0x6b, 0xbb, 0xbf,
134. 0x63, 0xdc, 0xea, 0x6f, 0x77, 0x81, 0xe9, 0x07, 0xe0, 0x18, 0xb3, 0x1e, 0x78, 0x4b, 0xbc, 0x17,
135. 0x77, 0x62, 0x25, 0xd9, 0xe7, 0x23, 0x6c, 0x80, 0xad, 0xdc, 0x51, 0x18, 0x1b, 0x33, 0x56, 0x59,
136. 0x15, 0x43, 0xcf, 0x51, 0xd9, 0xbc, 0x6d, 0xf7, 0x68, 0xd1, 0xe8, 0xbf, 0x41, 0x36, 0xd1, 0x30,
137. 0x92, 0x7b, 0x48, 0xd1, 0x00, 0xe2, 0x9d, 0x8e, 0x94, 0xee, 0x20, 0x2a, 0x18, 0xb1, 0x04, 0xba,
138. 0xe7, 0x19, 0xdc, 0x69, 0x36, 0xf7, 0x34, 0x4b, 0x16, 0x10, 0x10, 0x2a, 0x46, 0x1c, 0x4e, 0x6e,
139. 0x62, 0xe1, 0x25, 0x79, 0xd5, 0x5c, 0xf3, 0x9a, 0xeb, 0x1f, 0x3d, 0x82, 0xa3, 0xaa, 0x79, 0xde,
140. 0x23, 0xa1, 0x2b, 0x50, 0x6d, 0x68, 0x3e, 0x77, 0x33, 0xe0, 0xc9, 0x18, 0xbc, 0x65, 0x58, 0x63,
141. 0x7b, 0x02, 0x03, 0x01, 0x00, 0x01,
142. ]);

144. let paramRsa: Array<huks.HuksParam> = [
145. {
146. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
147. value: huks.HuksKeyAlg.HUKS_ALG_RSA
148. },
149. {
150. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
151. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
152. },
153. {
154. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
155. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
156. },
157. {
158. tag: huks.HuksTag.HUKS_TAG_PADDING,
159. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
160. },
161. {
162. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
163. value: huks.HuksCipherMode.HUKS_MODE_ECB
164. },
165. {
166. tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
167. value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_SM2_SM4_ECB_NOPADDING
168. },
169. {
170. tag: huks.HuksTag.HUKS_TAG_IMPORT_KEY_TYPE,
171. value: huks.HuksImportKeyType.HUKS_KEY_TYPE_KEY_PAIR
172. },
173. {
174. tag: huks.HuksTag.HUKS_TAG_ASYMMETRIC_PUBLIC_KEY_DATA,
175. value: publicKey
176. }];
177. let impRsaOption: huks.HuksOptions = {
178. properties: paramRsa
179. };

181. let wrapDataLen = intToUint8Array(enDataRsa.length);
182. let ciLen = intToUint8Array(cipherData.length);
183. impRsaOption.inData = concatUint8Arrays([ciLen, cipherData, wrapDataLen, enDataRsa]);

185. await huks.importWrappedKeyItem("importRsa", wrappingKeyAlias, impRsaOption)
186. .then((data) => {
187. console.info('import success')
188. }).catch((error: BusinessError) => {
189. console.error(`import fail, errorCode: ${error.code}`)
190. });
191. }
```

### AES

```
1. import { BusinessError } from "@kit.BasicServicesKit";
2. import { huks } from "@kit.UniversalKeystoreKit";

4. function intToUint8Array(value: number): Uint8Array
5. {
6. const buffer = new ArrayBuffer(4);
7. const view = new DataView(buffer);
8. view.setUint32(0, value, true);
9. return new Uint8Array(buffer);
10. }

12. function concatUint8Arrays(arrays: Uint8Array[]): Uint8Array
13. {
14. const totalLength = arrays.reduce((sum, arr) => sum + arr.length, 0);
15. const result = new Uint8Array(totalLength);
16. let offset = 0;
17. for (const arr of arrays) {
18. result.set(arr, offset);
19. offset += arr.length;
20. }
21. return result;
22. }

24. let wrappingParamSetSm2: Array<huks.HuksParam> = [
25. {
26. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
27. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
28. },
29. {
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_SM2
32. },
33. {
34. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
35. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
36. },
37. {
38. tag: huks.HuksTag.HUKS_TAG_DIGEST,
39. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
40. },
41. {
42. tag: huks.HuksTag.HUKS_TAG_PADDING,
43. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
44. }
45. ];
46. let option: huks.HuksOptions = { properties: wrappingParamSetSm2 };

48. let sm4PlainData = new Uint8Array([
49. 0xb9, 0xef, 0x35, 0x49, 0xb7, 0x00, 0x91, 0x58, 0x0c, 0x6f, 0x43, 0x28, 0xf8, 0x95, 0x1c, 0x02,
50. ]);

52. let enParamSm2: Array<huks.HuksParam> = [
53. {
54. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
55. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
56. },
57. {
58. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
59. value: huks.HuksKeyAlg.HUKS_ALG_SM2
60. },
61. {
62. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
63. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
64. },
65. {
66. tag: huks.HuksTag.HUKS_TAG_DIGEST,
67. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
68. },
69. {
70. tag: huks.HuksTag.HUKS_TAG_PADDING,
71. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
72. }
73. ];

75. let enOption: huks.HuksOptions = {
76. properties: enParamSm2,
77. inData: sm4PlainData
78. };

80. let cipherData: Uint8Array;
81. let handle: number;

83. async function EnvelopAesTest()
84. {
85. let wrappingKeyAlias = "WrappedKey";
86. await huks.generateKeyItem(wrappingKeyAlias, option)

88. // 使用生成的Sm2密钥加密Sm4密钥
89. await huks.initSession(wrappingKeyAlias, enOption)
90. .then((data) => {
91. handle = data.handle;
92. }).catch((error: BusinessError) => {
93. console.error('decrypt init fail')
94. });
95. await huks.finishSession(handle, enOption)
96. .then((data) => {
97. cipherData = data.outData as Uint8Array
98. }).catch((error: BusinessError) => {
99. console.error(`encrypt finish fail,errorCode: ${error.code}`)
100. });

102. let paramSetAes: Array<huks.HuksParam> = [
103. {
104. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
105. value: huks.HuksKeyAlg.HUKS_ALG_AES
106. },
107. {
108. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
109. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
110. },
111. {
112. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
113. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
114. },
115. {
116. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
117. value: huks.HuksCipherMode.HUKS_MODE_CBC
118. },
119. {
120. tag: huks.HuksTag.HUKS_TAG_PADDING,
121. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
122. },
123. {
124. tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
125. value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_SM2_SM4_ECB_NOPADDING
126. }];

128. let enDataAes = new Uint8Array([
129. 0xa5, 0xa4, 0xef, 0x4b, 0x87, 0x69, 0xf1, 0xd0, 0x7c, 0xd0, 0x55, 0x9a, 0xe0, 0xb8, 0x8c, 0x36,
130. ]);

132. let impAesOption: huks.HuksOptions = { properties: paramSetAes }

134. let wrapDataLen = intToUint8Array(enDataAes.length);
135. let ciLen = intToUint8Array(cipherData.length);
136. impAesOption.inData = concatUint8Arrays([ciLen, cipherData, wrapDataLen, enDataAes]);

138. await huks.importWrappedKeyItem("importAes", wrappingKeyAlias, impAesOption)
139. .then((data) => {
140. console.info('import success')
141. }).catch((error: BusinessError) => {
142. console.error(`import fail, errorCode: ${error.code}`)
143. });
144. }
```
