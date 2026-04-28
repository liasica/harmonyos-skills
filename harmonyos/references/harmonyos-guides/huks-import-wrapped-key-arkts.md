---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-import-wrapped-key-arkts
title: 安全导入密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 安全导入密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:deea3f02191e20fb0e235edee526515e6a868ba4ca8b74cae192209c73a31bb6
---

以安全导入ECDH密钥对为例，涉及业务侧加密密钥的[密钥生成](huks-key-generation-overview.md)、[协商](huks-key-agreement-overview.md)等操作不在本示例中体现。

具体的场景介绍及支持的算法规格，请参考[密钥导入支持的算法](huks-key-import-overview.md#支持的算法)。

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

构造用于ECDH密钥协商、AES-GCM加密和包装密钥导入的参数集

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. let IV = '0000000000000000';
4. let AAD = 'abababababababab';
5. let NONCE = 'hahahahahaha';
6. let TAG_SIZE = 16;
7. let FILED_LENGTH = 4;
8. let importedAes192PlainKey = 'The aes192 key to import';
9. let callerAes256Kek = 'The is kek to encrypt aes192 key';
10. let callerKeyAlias = 'test_caller_key_ecdh_aes192';
11. let callerKekAliasAes256 = 'test_caller_kek_ecdh_aes256';
12. let callerAgreeKeyAliasAes256 = 'test_caller_agree_key_ecdh_aes256';
13. let importedKeyAliasAes192 = 'test_import_key_ecdh_aes192';
14. let huksPubKey: Uint8Array;
15. let callerSelfPublicKey: Uint8Array;
16. let outSharedKey: Uint8Array;
17. let outPlainKeyEncData: Uint8Array;
18. let outKekEncData: Uint8Array;
19. let outKekEncTag: Uint8Array;
20. let outAgreeKeyEncTag: Uint8Array;
21. let mask = [0x000000FF, 0x0000FF00, 0x00FF0000, 0xFF000000];

23. function subUint8ArrayOf(arrayBuf: Uint8Array, start: number, end: number) {
24. let arr: number[] = [];
25. for (let i = start; i < end && i < arrayBuf.length; ++i) {
26. arr.push(arrayBuf[i]);
27. }
28. return new Uint8Array(arr);
29. }

31. function stringToUint8Array(str: string) {
32. let arr: number[] = [];
33. for (let i = 0, j = str.length; i < j; ++i) {
34. arr.push(str.charCodeAt(i));
35. }
36. return new Uint8Array(arr);
37. }

39. function assignLength(length: number, arrayBuf: Uint8Array, startIndex: number) {
40. let index = startIndex;
41. for (let i = 0; i < 4; i++) {
42. arrayBuf[index++] = (length & mask[i]) >> (i * 8);
43. }
44. return 4;
45. }

47. function assignData(data: Uint8Array, arrayBuf: Uint8Array, startIndex: number) {
48. let index = startIndex;
49. for (let i = 0; i < data.length; i++) {
50. arrayBuf[index++] = data[i];
51. }
52. return data.length;
53. }

55. let genWrappingKeyParams: huks.HuksOptions = {
56. properties: [
57. {
58. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
59. value: huks.HuksKeyAlg.HUKS_ALG_ECC
60. },
61. {
62. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
63. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_UNWRAP
64. },
65. {
66. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
67. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
68. },
69. {
70. tag: huks.HuksTag.HUKS_TAG_PADDING,
71. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
72. }
73. ]
74. }

76. let genCallerEcdhParams: huks.HuksOptions = {
77. properties: [
78. {
79. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
80. value: huks.HuksKeyAlg.HUKS_ALG_ECC
81. },
82. {
83. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
84. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
85. },
86. {
87. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
88. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
89. }
90. ]
91. }

93. let importParamsCallerKek: huks.HuksOptions = {
94. properties: [
95. {
96. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
97. value: huks.HuksKeyAlg.HUKS_ALG_AES
98. },
99. {
100. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
101. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
102. },
103. {
104. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
105. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
106. },
107. {
108. tag: huks.HuksTag.HUKS_TAG_PADDING,
109. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
110. },
111. {
112. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
113. value: huks.HuksCipherMode.HUKS_MODE_GCM
114. },
115. {
116. tag: huks.HuksTag.HUKS_TAG_DIGEST,
117. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
118. },
119. {
120. tag: huks.HuksTag.HUKS_TAG_IV,
121. value: stringToUint8Array(IV)
122. }
123. ],
124. inData: stringToUint8Array(callerAes256Kek)
125. }
```

[ImportEncryptedKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/ets/pages/ImportEncryptedKey.ets#L15-L142)

构造用于生成ECC解包装密钥、ECDH协商密钥和导入AES-GCM密钥加密密钥的参数集

```
1. let importParamsAgreeKey: huks.HuksOptions = {
2. properties: [
3. {
4. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
5. value: huks.HuksKeyAlg.HUKS_ALG_AES
6. },
7. {
8. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
9. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
10. },
11. {
12. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
13. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
14. },
15. {
16. tag: huks.HuksTag.HUKS_TAG_PADDING,
17. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
18. },
19. {
20. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
21. value: huks.HuksCipherMode.HUKS_MODE_GCM
22. },
23. {
24. tag: huks.HuksTag.HUKS_TAG_DIGEST,
25. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
26. },
27. {
28. tag: huks.HuksTag.HUKS_TAG_IV,
29. value: stringToUint8Array(IV)
30. }
31. ],
32. }

34. let callerAgreeParams: huks.HuksOptions = {
35. properties: [
36. {
37. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
38. value: huks.HuksKeyAlg.HUKS_ALG_ECDH
39. },
40. {
41. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
42. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE
43. },
44. {
45. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
46. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256
47. }
48. ]
49. }

51. let encryptKeyCommonParams: huks.HuksOptions = {
52. properties: [
53. {
54. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
55. value: huks.HuksKeyAlg.HUKS_ALG_AES
56. },
57. {
58. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
59. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
60. },
61. {
62. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
63. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
64. },
65. {
66. tag: huks.HuksTag.HUKS_TAG_PADDING,
67. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
68. },
69. {
70. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
71. value: huks.HuksCipherMode.HUKS_MODE_GCM
72. },
73. {
74. tag: huks.HuksTag.HUKS_TAG_NONCE,
75. value: stringToUint8Array(NONCE)
76. },
77. {
78. tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
79. value: stringToUint8Array(AAD)
80. }
81. ],
82. }

84. let importWrappedAes192Params: huks.HuksOptions = {
85. properties: [
86. {
87. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
88. value: huks.HuksKeyAlg.HUKS_ALG_AES
89. },
90. {
91. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
92. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
93. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
94. },
95. {
96. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
97. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_192
98. },
99. {
100. tag: huks.HuksTag.HUKS_TAG_PADDING,
101. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
102. },
103. {
104. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
105. value: huks.HuksCipherMode.HUKS_MODE_CBC
106. },
107. {
108. tag: huks.HuksTag.HUKS_TAG_DIGEST,
109. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
110. },
111. {
112. tag: huks.HuksTag.HUKS_TAG_UNWRAP_ALGORITHM_SUITE,
113. value: huks.HuksUnwrapSuite.HUKS_UNWRAP_SUITE_ECDH_AES_256_GCM_NOPADDING
114. },
115. {
116. tag: huks.HuksTag.HUKS_TAG_IV,
117. value: stringToUint8Array(IV)
118. }
119. ]
120. }
```

[ImportEncryptedKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/ets/pages/ImportEncryptedKey.ets#L144-L265)

生成密钥、导入密钥、删除密钥、导入包装密钥以及会话操作

```
1. async function publicGenerateItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
2. console.info(`enter promise generateKeyItem`);
3. try {
4. await huks.generateKeyItem(keyAlias, huksOptions)
5. .then(data => {
6. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
7. })
8. .catch((err: Error) => {
9. console.error(`promise: generateKeyItem failed, ${JSON.stringify(err)}`);
10. throw (err as Error);
11. })
12. } catch (err) {
13. console.error(`promise: generateKeyItem invalid, ${JSON.stringify(err)}`);
14. throw (err as Error);
15. }
16. }

18. async function publicImportKeyItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
19. console.info(`enter promise importKeyItem`);
20. try {
21. await huks.importKeyItem(keyAlias, huksOptions)
22. .then(data => {
23. console.info(`promise: importKeyItem success, data = ${JSON.stringify(data)}`);
24. }).catch((err: Error) => {
25. console.error(`promise: importKeyItem failed, ${JSON.stringify(err)}`);
26. throw (err as Error);
27. })
28. } catch (err) {
29. console.error(`promise: importKeyItem input arg invalid, ${JSON.stringify(err)}`);
30. throw (err as Error);
31. }
32. }

34. async function publicDeleteKeyItemFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
35. console.info(`enter promise deleteKeyItem`);
36. try {
37. await huks.deleteKeyItem(keyAlias, huksOptions)
38. .then(data => {
39. console.info(`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}`);
40. })
41. .catch((err: Error) => {
42. console.error(`promise: deleteKeyItem failed, ${JSON.stringify(err)}`);
43. throw (err as Error);
44. })
45. } catch (err) {
46. console.error(`promise: deleteKeyItem input arg invalid, ${JSON.stringify(err)}`);
47. throw (err as Error);
48. }
49. }

51. function importWrappedKeyItem(keyAlias: string, wrappingKeyAlias: string, huksOptions: huks.HuksOptions) {
52. return new Promise<void>((resolve, reject) => {
53. try {
54. huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions, (error, data) => {
55. if (error) {
56. reject(error);
57. } else {
58. resolve(data);
59. }
60. });
61. } catch (error) {
62. throw (error as Error);
63. }
64. });
65. }

67. async function publicImportWrappedKeyFunc(keyAlias: string, wrappingKeyAlias: string, huksOptions: huks.HuksOptions) {
68. console.info(`enter promise importWrappedKeyItem`);
69. for (let i = 0; i < huksOptions.inData!.length; i++) {
70. console.error(`${i}: ${huksOptions.inData![i]}`);
71. }
72. try {
73. await importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
74. .then((data) => {
75. console.info(`promise: importWrappedKeyItem success, data = ${JSON.stringify(data)}`);
76. })
77. .catch((error: Error) => {
78. console.error(`promise: importWrappedKeyItem failed, ${JSON.stringify(error)}`);
79. throw (error as Error);
80. });
81. } catch (error) {
82. console.error(`promise: importWrappedKeyItem input arg invalid, ${JSON.stringify(error)}`);
83. throw (error as Error);
84. }
85. }

87. async function publicImportWrappedKeyPromise(keyAlias: string, wrappingKeyAlias: string,
88. huksOptions: huks.HuksOptions) {
89. console.info(`enter promise importWrappedKeyItem`);
90. try {
91. await huks.importWrappedKeyItem(keyAlias, wrappingKeyAlias, huksOptions)
92. .then((data) => {
93. console.info(`promise: importWrappedKeyItem success, data = ${JSON.stringify(data)}`);
94. })
95. .catch((error: Error) => {
96. console.error(`promise: importWrappedKeyItem failed, ${JSON.stringify(error)}`);
97. throw (error as Error);
98. });
99. } catch (error) {
100. console.error(`promise: importWrappedKeyItem input arg invalid, ${JSON.stringify(error)}`);
101. throw (error as Error);
102. }
103. }

105. async function publicInitFunc(srcKeyAlias: string, huksOptions: huks.HuksOptions) {
106. let handle: number = 0;
107. console.info(`enter promise doInit`);
108. try {
109. await huks.initSession(srcKeyAlias, huksOptions)
110. .then((data) => {
111. console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
112. handle = data.handle;
113. })
114. .catch((error: Error) => {
115. console.error(`promise: doInit key failed, ${JSON.stringify(error)}`);
116. throw (error as Error);
117. });
118. } catch (error) {
119. console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
120. throw (error as Error);
121. }
122. return handle;
123. }

125. async function publicUpdateSessionFunction(handle: number, huksOptions: huks.HuksOptions) {
126. const maxUpdateSize = 64;
127. const inData = huksOptions.inData!;
128. const lastInDataPosition = inData.length - 1;
129. let inDataSegSize = maxUpdateSize;
130. let inDataSegPosition = 0;
131. let isFinished = false;
132. let outData: number[] = [];

134. while (inDataSegPosition <= lastInDataPosition) {
135. if (inDataSegPosition + maxUpdateSize > lastInDataPosition) {
136. isFinished = true;
137. inDataSegSize = lastInDataPosition - inDataSegPosition + 1;
138. console.info(`enter promise doUpdate`);
139. break;
140. }
141. huksOptions.inData = new Uint8Array(
142. Array.from(inData).slice(inDataSegPosition, inDataSegPosition + inDataSegSize)
143. );
144. console.info(`enter promise doUpdate`);
145. try {
146. await huks.updateSession(handle, huksOptions)
147. .then((data) => {
148. console.info(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
149. outData = outData.concat(Array.from(data.outData!));
150. })
151. .catch((error: Error) => {
152. console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
153. throw (error as Error);
154. });
155. } catch (error) {
156. console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
157. throw (error as Error);
158. }
159. if ((!isFinished) && (inDataSegPosition + maxUpdateSize > lastInDataPosition)) {
160. console.error(`update size invalid isFinished = ${isFinished}`);
161. console.error(`inDataSegPosition = ${inDataSegPosition}`);
162. console.error(`lastInDataPosition = ${lastInDataPosition}`);
163. return;
164. }
165. inDataSegPosition += maxUpdateSize;
166. }
167. return outData;
168. }

170. async function publicFinishSession(handle: number, huksOptions: huks.HuksOptions, inData: number[]) {
171. let outData: number[] = [];
172. console.info(`enter promise doFinish`);
173. try {
174. await huks.finishSession(handle, huksOptions)
175. .then((data) => {
176. console.info(`promise: doFinish success, data = ${JSON.stringify(data)}`);
177. outData = inData.concat(Array.from(data.outData!));
178. })
179. .catch((error: Error) => {
180. console.error(`promise: doFinish key failed, ${JSON.stringify(error)}`);
181. throw (error as Error);
182. });
183. } catch (error) {
184. console.error(`promise: doFinish input arg invalid, ${JSON.stringify(error)}`);
185. throw (error as Error);
186. }
187. return new Uint8Array(outData);
188. }
```

[ImportEncryptedKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/ets/pages/ImportEncryptedKey.ets#L267-L456)

密钥协商、加密、数据封装等核心功能函数实现

```
1. async function cipherFunction(keyAlias: string, huksOptions: huks.HuksOptions) {
2. let handle = await publicInitFunc(keyAlias, huksOptions);
3. let tmpData = await publicUpdateSessionFunction(handle, huksOptions);
4. let outData = await publicFinishSession(handle, huksOptions, tmpData!);
5. return outData;
6. }

8. async function agreeFunction(keyAlias: string, huksOptions: huks.HuksOptions, huksPublicKey: Uint8Array) {
9. let handle = await publicInitFunc(keyAlias, huksOptions);
10. let outSharedKey: Uint8Array = new Uint8Array;
11. huksOptions.inData = huksPublicKey;
12. console.info(`enter promise doUpdate`);
13. try {
14. await huks.updateSession(handle, huksOptions)
15. .then((data) => {
16. console.error(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
17. })
18. .catch((error: Error) => {
19. console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
20. throw (error as Error);
21. });
22. } catch (error) {
23. console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
24. throw (error as Error);
25. }
26. console.info(`enter promise doInit`);
27. try {
28. await huks.finishSession(handle, huksOptions)
29. .then((data) => {
30. console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
31. outSharedKey = data.outData as Uint8Array;
32. })
33. .catch((error: Error) => {
34. console.error(`promise: doInit key failed, ${JSON.stringify(error)}`);
35. throw (error as Error);
36. });
37. } catch (error) {
38. console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
39. throw (error as Error);
40. }
41. return outSharedKey;
42. }

44. async function importKekAndAgreeSharedSecret(callerKekAlias: string, importKekParams: huks.HuksOptions,
45. callerKeyAlias: string, huksPublicKey: Uint8Array, agreeParams: huks.HuksOptions) {
46. await publicImportKeyItemFunc(callerKekAlias, importKekParams);
47. outSharedKey = await agreeFunction(callerKeyAlias, agreeParams, huksPublicKey);
48. importParamsAgreeKey.inData = outSharedKey;
49. await publicImportKeyItemFunc(callerAgreeKeyAliasAes256, importParamsAgreeKey);
50. }

52. async function generateAndExportPublicKey(keyAlias: string, huksOptions: huks.HuksOptions, caller: Boolean) {
53. await publicGenerateItemFunc(keyAlias, huksOptions);
54. try {
55. await huks.exportKeyItem(keyAlias, huksOptions)
56. .then((data) => {
57. console.info(`promise: exportKeyItem success, data = ${JSON.stringify(data)}`);
58. if (caller) {
59. callerSelfPublicKey = data.outData as Uint8Array;
60. } else {
61. huksPubKey = data.outData as Uint8Array;
62. }
63. })
64. .catch((error: Error) => {
65. console.error(`promise: exportKeyItem failed, ${JSON.stringify(error)}`);
66. throw (error as Error);
67. });
68. } catch (error) {
69. console.error(`promise: generate pubKey failed, ${JSON.stringify(error)}`);
70. throw (error as Error);
71. }
72. }

74. async function encryptImportedPlainKeyAndKek(keyAlias: string) {
75. encryptKeyCommonParams.inData = stringToUint8Array(keyAlias)
76. let plainKeyEncData = await cipherFunction(callerKekAliasAes256, encryptKeyCommonParams);
77. outKekEncTag = subUint8ArrayOf(plainKeyEncData, plainKeyEncData.length - TAG_SIZE, plainKeyEncData.length)
78. outPlainKeyEncData = subUint8ArrayOf(plainKeyEncData, 0, plainKeyEncData.length - TAG_SIZE)
79. encryptKeyCommonParams.inData = stringToUint8Array(callerAes256Kek)
80. let kekEncData = await cipherFunction(callerAgreeKeyAliasAes256, encryptKeyCommonParams)
81. outAgreeKeyEncTag = subUint8ArrayOf(kekEncData, kekEncData.length - TAG_SIZE, kekEncData.length)
82. outKekEncData = subUint8ArrayOf(kekEncData, 0, kekEncData.length - TAG_SIZE)
83. }

85. async function buildWrappedDataAndImportWrappedKey(plainKey: string) {
86. let plainKeySizeBuff = new Uint8Array(4);
87. assignLength(plainKey.length, plainKeySizeBuff, 0);
88. let wrappedData = new Uint8Array(
89. FILED_LENGTH + huksPubKey.length +
90. FILED_LENGTH + AAD.length +
91. FILED_LENGTH + NONCE.length +
92. FILED_LENGTH + TAG_SIZE +
93. FILED_LENGTH + outKekEncData.length +
94. FILED_LENGTH + AAD.length +
95. FILED_LENGTH + NONCE.length +
96. FILED_LENGTH + TAG_SIZE +
97. FILED_LENGTH + plainKeySizeBuff.length +
98. FILED_LENGTH + outPlainKeyEncData.length
99. );
100. let index = 0;
101. let aadUint8Array = stringToUint8Array(AAD);
102. let nonceArray = stringToUint8Array(NONCE);
103. index += assignLength(callerSelfPublicKey.length, wrappedData, index); // 4
104. index += assignData(callerSelfPublicKey, wrappedData, index); // 91
105. index += assignLength(aadUint8Array.length, wrappedData, index); // 4
106. index += assignData(aadUint8Array, wrappedData, index); // 16
107. index += assignLength(nonceArray.length, wrappedData, index); // 4
108. index += assignData(nonceArray, wrappedData, index); // 12
109. index += assignLength(outAgreeKeyEncTag.length, wrappedData, index); // 4
110. index += assignData(outAgreeKeyEncTag, wrappedData, index); // 16
111. index += assignLength(outKekEncData.length, wrappedData, index); // 4
112. index += assignData(outKekEncData, wrappedData, index); // 32
113. index += assignLength(aadUint8Array.length, wrappedData, index); // 4
114. index += assignData(aadUint8Array, wrappedData, index); // 16
115. index += assignLength(nonceArray.length, wrappedData, index); // 4
116. index += assignData(nonceArray, wrappedData, index); // 12
117. index += assignLength(outKekEncTag.length, wrappedData, index); // 4
118. index += assignData(outKekEncTag, wrappedData, index); // 16
119. index += assignLength(plainKeySizeBuff.length, wrappedData, index); // 4
120. index += assignData(plainKeySizeBuff, wrappedData, index); // 4
121. index += assignLength(outPlainKeyEncData.length, wrappedData, index); // 4
122. index += assignData(outPlainKeyEncData, wrappedData, index); // 24
123. return wrappedData;
124. }
```

[ImportEncryptedKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/ets/pages/ImportEncryptedKey.ets#L458-L583)

安全导入密钥的完整流程实现

```
1. /* 模拟安全导入密钥场景，设备A为远端设备（导入设备），设备B为本端设备（被导入设备） */
2. async function ImportWrappedKey() {
3. /**
4. * 1. 设备A将待导入密钥转换成HUKS密钥材料格式To_Import_Key（仅针对非对称密钥，若待导入密钥是对称密钥则可省略此步骤），
5. *   本示例使用importedAes256PlainKey（对称密钥）作为模拟
6. */
7. /**
8. * 2. 设备B生成一个加密导入用途的、用于协商的非对称密钥对Wrapping_Key（公钥Wrapping_Pk，私钥Wrapping_Sk），
9. * 导出Wrapping_Key公钥Wrapping_Pk存放在变量huksPubKey中
10. */
11. const srcKeyAliasWrap = 'HUKS_Basic_Capability_Import_0200';
12. await generateAndExportPublicKey(srcKeyAliasWrap, genWrappingKeyParams, false);

14. /**
15. * 3. 设备A使用和设备B同样的算法，生成一个用于协商的非对称密钥对Caller_Key（公钥Caller_Pk，私钥Caller_Sk），
16. * 导出Caller_Key公钥Caller_Pk存放在变量callerSelfPublicKey中
17. */
18. await generateAndExportPublicKey(callerKeyAlias, genCallerEcdhParams, true);

20. /**
21. * 4. 设备A生成一个对称密钥Caller_Kek，该密钥后续将用于加密To_Import_Key
22. * 设备A基于Caller_Key的私钥Caller_Sk和设备B Wrapping_Key的公钥Wrapping_Pk，协商出Shared_Key
23. */
24. await importKekAndAgreeSharedSecret(callerKekAliasAes256, importParamsCallerKek, callerKeyAlias, huksPubKey,
25. callerAgreeParams);

27. /**
28. * 5. 设备A使用Caller_Kek加密To_Import_Key，生成To_Import_Key_Enc
29. * 设备A使用Shared_Key加密Caller_Kek，生成Caller_Kek_Enc
30. */
31. await encryptImportedPlainKeyAndKek(importedAes192PlainKey);

33. /**
34. * 6. 设备A封装Caller_Pk、To_Import_Key_Enc、Caller_Kek_Enc等安全导入的材料并发送给设备B。
35. * 本示例作为变量存放在callerSelfPublicKey，PlainKeyEncData，KekEncData
36. */
37. let wrappedData = await buildWrappedDataAndImportWrappedKey(importedAes192PlainKey);
38. importWrappedAes192Params.inData = wrappedData;

40. /* 7. 设备B导入封装的加密密钥材料 */
41. await publicImportWrappedKeyFunc(importedKeyAliasAes192, srcKeyAliasWrap, importWrappedAes192Params);

43. /* 8. 设备A、B删除用于安全导入的密钥 */
44. await publicDeleteKeyItemFunc(srcKeyAliasWrap, genWrappingKeyParams);
45. await publicDeleteKeyItemFunc(callerKeyAlias, genCallerEcdhParams);
46. await publicDeleteKeyItemFunc(importedKeyAliasAes192, importWrappedAes192Params);
47. await publicDeleteKeyItemFunc(callerKekAliasAes256, callerAgreeParams);
48. }

51. /*
52. * 确定密钥别名和封装密钥属性参数集
53. */
54. let keyAlias = 'test_import_key_ecdh_aes192';
55. let isKeyExist: Boolean;
56. let keyProperties: huks.HuksParam[] = [{
57. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
58. value: huks.HuksKeyAlg.HUKS_ALG_AES,
59. }];
60. let huksOptions: huks.HuksOptions = {
61. properties: keyProperties, // 非空填充
62. inData: new Uint8Array([]) // 非空填充
63. }

65. function Check() {
66. try {
67. huks.isKeyItemExist(keyAlias, huksOptions, (error, data) => {
68. if (error) {
69. console.error(`callback: isKeyItemExist failed, ${JSON.stringify(error)}`);
70. } else {
71. if (data !== null && data.valueOf() !== null) {
72. isKeyExist = data.valueOf();
73. console.info(`callback: isKeyItemExist success, isKeyExist = ${isKeyExist}`);
74. }
75. }
76. });
77. } catch (error) {
78. console.error(`callback: isKeyItemExist input arg invalid, ${JSON.stringify(error)}`);
79. throw (error as Error);
80. }
81. }
```

[ImportEncryptedKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/ImportEncryptedKey/entry/src/main/ets/pages/ImportEncryptedKey.ets#L585-L665)

## 调测验证

调用[huks.isKeyItemExist](../harmonyos-references/js-apis-huks.md#huksiskeyitemexist9)验证密钥是否存在，如密钥存在即表示密钥导入成功。

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from "@kit.BasicServicesKit";

4. /*
5. * 确定密钥别名和封装密钥属性参数集
6. */
7. let keyAlias = 'test_import_key_ecdh_aes192';
8. let isKeyExist: Boolean;
9. let keyProperties: Array<huks.HuksParam> = [{
10. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
11. value: huks.HuksKeyAlg.HUKS_ALG_AES,
12. }];
13. let huksOptions: huks.HuksOptions = {
14. properties: keyProperties, // 非空填充。
15. inData: new Uint8Array(new Array()) // 非空填充。
16. }

18. async function isKeyItemExist(keyAlias: string, options: huks.HuksOptions): Promise<boolean> {
19. console.info(`promise: enter isKeyItemExist`);
20. let ret: boolean = false;
21. try {
22. await huks.isKeyItemExist(keyAlias, options)
23. .then((data) => {
24. console.info(`promise: isKeyItemExist success, data = ${data}`);
25. ret = true;
26. }).catch((error: BusinessError) => {
27. console.error(`promise: isKeyItemExist failed, errCode : ${error.code}, errMsg : ${error.message}`);
28. })
29. } catch (error) {
30. console.error(`promise: isKeyItemExist input arg invalid`);
31. }
32. return ret;
33. }

35. async function importWrappedKeyExistTest() {
36. let retImp = await isKeyItemExist(keyAlias, huksOptions);
37. if (retImp == false) {
38. console.error("importWrappedKeyExistTest failed");
39. return;
40. }
41. console.error("importWrappedKeyExistTest success");
42. }
```
