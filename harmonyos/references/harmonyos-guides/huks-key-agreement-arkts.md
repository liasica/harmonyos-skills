---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-agreement-arkts
title: 密钥协商(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥协商 > 密钥协商(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af135b2cc79883185a8d00ae71a126800ea7c6db3aff554b6c2dfdcff32feecd
---

以X25519，DH和ECDH三个协商密钥类型为例，在密钥由HUKS管理的情况下，完成密钥协商。具体的场景介绍及支持的算法规格，请参考[密钥协商支持的算法](huks-key-agreement-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，可指定参数[HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG](../harmonyos-references/js-apis-huks.md#hukstag)（可选），用于标识基于该密钥协商出的密钥是否由HUKS管理。

* 当TAG设置为[HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS](../harmonyos-references/js-apis-huks.md#hukskeystoragetype)时，表示基于该密钥协商出的密钥，由HUKS管理，可保证协商密钥全生命周期不出安全环境。
* 当TAG设置为[HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED](../harmonyos-references/js-apis-huks.md#hukskeystoragetype)时，表示基于该密钥协商出的密钥，返回给调用方管理，由业务自行保证密钥安全。
* 若业务未设置TAG的具体值，表示基于该密钥协商出的密钥，可由HUKS管理，也可返回给调用方管理，业务可在后续协商时再选择使用何种方式保护密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识协商得到的密钥是否由HUKS管理。

| 生成 | 协商 | 规格 |
| --- | --- | --- |
| HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
| 未指定TAG具体值 | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
| 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

注：协商时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

下面分别以X25519、DH和ECDH密钥为例，进行协商。

### X25519非对称密钥协商用例

准备X25519密钥协商材料：

```
1. /*
2. * 以下以X25519密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. function stringToUint8Array(str: string) {
8. let arr: number[] = [];
9. for (let i = 0, j = str.length; i < j; ++i) {
10. arr.push(str.charCodeAt(i));
11. }
12. return new Uint8Array(arr);
13. }

15. function uint8ArrayToString(fileData: Uint8Array) {
16. let dataString = '';
17. for (let i = 0; i < fileData.length; i++) {
18. dataString += String.fromCharCode(fileData[i]);
19. }
20. return dataString;
21. }

23. /*
24. * 确定密钥别名和封装密钥属性参数集
25. */
26. let srcKeyAliasFirst = 'AgreeX25519KeyFirstAlias';
27. let srcKeyAliasSecond = 'AgreeX25519KeySecondAlias';
28. let agreeX25519InData = 'AgreeX25519TestIndata';
29. let finishOutData: Uint8Array;
30. let handle: number;
31. let exportKey: Uint8Array;
32. let exportKeyFirst: Uint8Array;
33. let exportKeySecond: Uint8Array;
34. /* 集成生成密钥参数集 */
35. let properties: huks.HuksParam[] = [{
36. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
37. value: huks.HuksKeyAlg.HUKS_ALG_X25519,
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
40. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
43. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256,
44. }, {
45. tag: huks.HuksTag.HUKS_TAG_DIGEST,
46. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_PADDING,
49. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
52. value: huks.HuksCipherMode.HUKS_MODE_CBC,
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
55. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
56. }
57. ];
58. let huksOptions: huks.HuksOptions = {
59. properties: properties,
60. inData: new Uint8Array([])
61. }
62. /* 集成第一个协商参数集 */
63. const finishProperties: huks.HuksParam[] = [{
64. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
65. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
68. value: true
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
71. value: huks.HuksKeyAlg.HUKS_ALG_AES,
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
74. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
77. value:
78. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
79. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
80. }, {
81. tag: huks.HuksTag.HUKS_TAG_DIGEST,
82. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
83. }, {
84. tag: huks.HuksTag.HUKS_TAG_PADDING,
85. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
86. }, {
87. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
88. value: huks.HuksCipherMode.HUKS_MODE_ECB,
89. }
90. ];
91. let finishOptionsFirst: huks.HuksOptions = {
92. properties: [
93. ...finishProperties, {
94. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
95. value: stringToUint8Array(srcKeyAliasFirst + 'final'),
96. }],
97. inData: stringToUint8Array(agreeX25519InData)
98. }
99. /* 集成第二个协商参数集 */
100. let finishOptionsSecond: huks.HuksOptions = {
101. properties: [
102. ...finishProperties, {
103. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
104. value: stringToUint8Array(srcKeyAliasSecond + 'final'),
105. }],
106. inData: stringToUint8Array(agreeX25519InData)
107. }
```

[X25519.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/ets/pages/X25519.ets#L15-L124)

执行密钥协商：

```
1. /* 生成密钥 */
2. async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
3. console.info('promise: enter generateKeyItem');
4. try {
5. await huks.generateKeyItem(keyAlias, huksOptions)
6. .then(() => {
7. console.info(`promise: generateKeyItem success`);
8. }).catch((error: BusinessError) => {
9. console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
10. })
11. } catch (error) {
12. console.error(`promise: generateKeyItem input arg invalid`);
13. }
14. }

16. /* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
17. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
18. console.info('promise: enter initSession');
19. try {
20. await huks.initSession(keyAlias, huksOptions)
21. .then((data) => {
22. handle = data.handle;
23. console.info(`promise: initSession success`);
24. }).catch((error: BusinessError) => {
25. console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
26. })
27. } catch (error) {
28. console.error(`promise: initSession input arg invalid`);
29. }
30. }

32. /* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
33. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
34. console.info('promise: enter updateSession');
35. try {
36. await huks.updateSession(handle, huksOptions)
37. .then((data) => {
38. console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
39. }).catch((error: BusinessError) => {
40. console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
41. })
42. } catch (error) {
43. console.error(`promise: updateSession input arg invalid`);
44. }
45. }

47. /* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
48. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
49. console.info('promise: enter finishSession');
50. try {
51. await huks.finishSession(handle, huksOptions)
52. .then((data) => {
53. finishOutData = data.outData as Uint8Array;
54. console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
55. }).catch((error: BusinessError) => {
56. console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
57. })
58. } catch (error) {
59. console.error(`promise: finishSession input arg invalid`);
60. }
61. }

63. /* 导出密钥 */
64. async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
65. console.info('promise: enter exportKeyItem');
66. try {
67. await huks.exportKeyItem(keyAlias, huksOptions)
68. .then((data) => {
69. exportKey = data.outData as Uint8Array;
70. console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
71. }).catch((error: BusinessError) => {
72. console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
73. })
74. } catch (error) {
75. console.error(`promise: exportKeyItem input arg invalid`);
76. }
77. }

79. /* 删除密钥操作 */
80. async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
81. console.info('promise: enter deleteKeyItem');
82. try {
83. await huks.deleteKeyItem(keyAlias, huksOptions)
84. .then(() => {
85. console.info(`promise: deleteKeyItem success`);
86. }).catch((error: BusinessError) => {
87. console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
88. })
89. } catch (error) {
90. console.error(`promise: deleteKeyItem input arg invalid`);
91. }
92. }

94. async function testAgree() {
95. /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
96. /* 2.设备A生成密钥 */
97. await generateKeyItem(srcKeyAliasFirst, huksOptions);
98. /* 3.设备B生成密钥 */
99. await generateKeyItem(srcKeyAliasSecond, huksOptions);
100. /* 4.设备A、B导出非对称密钥的公钥 */
101. await exportKeyItem(srcKeyAliasFirst, huksOptions);
102. exportKeyFirst = exportKey;
103. await exportKeyItem(srcKeyAliasSecond, huksOptions);
104. exportKeySecond = exportKey;
105. /* 5.对第一个密钥进行协商（三段式） */
106. await initSession(srcKeyAliasFirst, huksOptions);
107. huksOptions.inData = exportKeySecond;
108. await updateSession(handle, huksOptions);
109. await finishSession(handle, finishOptionsFirst);
110. /* 6.对第二个密钥进行协商（三段式） */
111. await initSession(srcKeyAliasSecond, huksOptions);
112. huksOptions.inData = exportKeyFirst;
113. await updateSession(handle, huksOptions);
114. await finishSession(handle, finishOptionsSecond);
115. /* 7.设备A、B删除密钥 */
116. await deleteKeyItem(srcKeyAliasFirst, huksOptions);
117. await deleteKeyItem(srcKeyAliasSecond, huksOptions);
118. }
```

[X25519.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/ets/pages/X25519.ets#L126-L248)

### DH密钥协商用例

```
1. /*
2. * 下面以DH密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. function stringToUint8Array(str: string) {
8. let arr: number[] = [];
9. for (let i = 0, j = str.length; i < j; ++i) {
10. arr.push(str.charCodeAt(i));
11. }
12. return new Uint8Array(arr);
13. }

15. function uint8ArrayToBigInt(arr: Uint8Array): bigint {
16. let i = 0;
17. const byteMax: bigint = BigInt('0x100');
18. let result: bigint = BigInt('0');
19. while (i < arr.length) {
20. result = result * byteMax;
21. result = result + BigInt(arr[i]);
22. i += 1;
23. }
24. return result;
25. }

27. function uint8ArrayToString(fileData: Uint8Array) {
28. let dataString = '';
29. for (let i = 0; i < fileData.length; i++) {
30. dataString += String.fromCharCode(fileData[i]);
31. }
32. return dataString;
33. }

35. let handle: number;
36. let finishOutData: Uint8Array;
37. let exportKey: Uint8Array;
38. const dhAgree: huks.HuksParam[] = [{
39. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
40. value: huks.HuksKeyAlg.HUKS_ALG_DH,
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
43. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
44. }];
45. const dh2048Agree: huks.HuksParam[] = [
46. ...dhAgree, {
47. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
48. value: huks.HuksKeySize.HUKS_DH_KEY_SIZE_2048,
49. }];
50. const dhGenOptions: huks.HuksOptions = {
51. properties: dh2048Agree,
52. inData: new Uint8Array([])
53. };
54. const emptyOptions: huks.HuksOptions = {
55. properties: [],
56. inData: new Uint8Array([])
57. };

59. /* 生成密钥 */
60. async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
61. console.info('promise: enter generateKeyItem');
62. try {
63. await huks.generateKeyItem(keyAlias, huksOptions)
64. .then(() => {
65. console.info(`promise: generateKeyItem success`);
66. }).catch((error: BusinessError) => {
67. console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
68. })
69. } catch (error) {
70. console.error(`promise: generateKeyItem input arg invalid`);
71. }
72. }

74. /* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
75. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
76. console.info('promise: enter initSession');
77. try {
78. await huks.initSession(keyAlias, huksOptions)
79. .then((data) => {
80. handle = data.handle;
81. console.info(`promise: initSession success`);
82. }).catch((error: BusinessError) => {
83. console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
84. })
85. } catch (error) {
86. console.error(`promise: initSession input arg invalid`);
87. }
88. }

90. /* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
91. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
92. console.info('promise: enter updateSession');
93. try {
94. await huks.updateSession(handle, huksOptions)
95. .then((data) => {
96. console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
97. }).catch((error: BusinessError) => {
98. console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
99. })
100. } catch (error) {
101. console.error(`promise: updateSession input arg invalid`);
102. }
103. }

105. /* 查询密钥是否存在 */
106. async function isKeyItemExist(keyAlias: string, huksOptions: huks.HuksOptions) {
107. console.info('promise: enter isKeyItemExist');
108. try {
109. await huks.isKeyItemExist(keyAlias, huksOptions)
110. .then((data) => {
111. console.info(`isKeyItemExist success`);
112. }).catch((error: BusinessError) => {
113. console.error(`isKeyItemExist failed, errCode : ${error.code}, errMsg : ${error.message}`);
114. })
115. } catch (error) {
116. console.error(`isKeyItemExist input arg invalid`);
117. }
118. }

120. /* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
121. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
122. console.info('promise: enter finishSession');
123. try {
124. await huks.finishSession(handle, huksOptions)
125. .then((data) => {
126. finishOutData = data.outData as Uint8Array;
127. console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
128. }).catch((error: BusinessError) => {
129. console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
130. })
131. } catch (error) {
132. console.error(`promise: finishSession input arg invalid`);
133. }
134. }

136. /* 导出密钥 */
137. async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
138. console.info('promise: enter exportKeyItem');
139. try {
140. await huks.exportKeyItem(keyAlias, huksOptions)
141. .then((data) => {
142. exportKey = data.outData as Uint8Array;
143. console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
144. }).catch((error: BusinessError) => {
145. console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
146. })
147. } catch (error) {
148. console.error(`promise: exportKeyItem input arg invalid`);
149. }
150. }

152. /* 删除密钥操作 */
153. async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
154. console.info('promise: enter deleteKeyItem');
155. try {
156. await huks.deleteKeyItem(keyAlias, huksOptions)
157. .then(() => {
158. console.info(`promise: deleteKeyItem success`);
159. }).catch((error: BusinessError) => {
160. console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
161. })
162. } catch (error) {
163. console.error(`promise: deleteKeyItem input arg invalid`);
164. }
165. }

167. async function huksDhAgreeExportKey(keyAlias: string,
168. peerPubKey: Uint8Array) {
169. await initSession(keyAlias, dhGenOptions);
170. const dhAgreeUpdateBobPubKey: huks.HuksOptions = {
171. properties: [
172. ...dh2048Agree, {
173. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
174. value: huks.HuksKeyStorageType.HUKS_STORAGE_KEY_EXPORT_ALLOWED,
175. }],
176. inData: peerPubKey
177. };
178. await updateSession(handle, dhAgreeUpdateBobPubKey);
179. await finishSession(handle, emptyOptions);
180. }

182. async function huksDhAgreeInHuks(keyAlias: string, peerPubKey: Uint8Array,
183. aliasAgreedKey: string) {
184. const onlyUsedInHuks: huks.HuksParam[] = [{
185. tag: huks.HuksTag.HUKS_TAG_KEY_STORAGE_FLAG,
186. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
187. }, {
188. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
189. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
190. }];
191. const dhAgreeInit: huks.HuksOptions = {
192. properties: [
193. ...dhAgree,
194. { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256, },
195. ...onlyUsedInHuks],
196. inData: new Uint8Array([])
197. };
198. const dhAgreeFinishParams: huks.HuksParam[] = [
199. ...onlyUsedInHuks,
200. { tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS, value: true },
201. { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_AES },
202. { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256 },
203. {
204. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
205. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
206. }
207. ];

209. await initSession(keyAlias, dhAgreeInit);
210. const dhAgreeUpdatePubKey: huks.HuksOptions = {
211. properties: [...dhAgree, ...onlyUsedInHuks],
212. inData: peerPubKey
213. };
214. await updateSession(handle, dhAgreeUpdatePubKey);
215. const dhAgreeAliceFinish: huks.HuksOptions = {
216. properties: [...dhAgreeFinishParams, {
217. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS, value: stringToUint8Array(aliasAgreedKey)
218. }], inData: new Uint8Array([])
219. };
220. await finishSession(handle, dhAgreeAliceFinish);
221. }

223. async function huksDhAgreeInHuksTest(
224. aliasA: string, aliasB: string,
225. pubKeyA: Uint8Array, pubKeyB: Uint8Array,
226. aliasAgreedKeyFromA: string, aliasAgreedKeyFromB: string) {

228. await huksDhAgreeInHuks(aliasA, pubKeyB, aliasAgreedKeyFromA);
229. const aliceAgreedExist = await isKeyItemExist(aliasAgreedKeyFromA, emptyOptions);
230. console.info(`ok! aliceAgreedExist in huks is ${aliceAgreedExist}`);

232. await huksDhAgreeInHuks(aliasB, pubKeyA, aliasAgreedKeyFromB);
233. const bobAgreedExist = await isKeyItemExist(aliasAgreedKeyFromB, emptyOptions);
234. console.info(`ok! bobAgreedExist in huks is ${bobAgreedExist}`);

236. await deleteKeyItem(aliasAgreedKeyFromA, emptyOptions);
237. await deleteKeyItem(aliasAgreedKeyFromB, emptyOptions);
238. }

240. async function huksDhAgreeTest() {
241. const aliasAlice = 'alice';
242. const aliasBob = 'bob';

244. /* 调用generateKeyItem生成别名为alice与bob的两个密钥 */
245. await generateKeyItem(aliasAlice, dhGenOptions);
246. await generateKeyItem(aliasBob, dhGenOptions);

248. /* 导出非对称密钥alice与bob的公钥 */
249. await exportKeyItem(aliasAlice, emptyOptions);
250. const pubKeyAlice = exportKey;
251. await exportKeyItem(aliasBob, emptyOptions);
252. const pubKeyBob = exportKey;

254. /* 开始协商，协商生成的密钥返回给业务管理 */
255. await huksDhAgreeExportKey(aliasAlice, pubKeyBob);
256. await huksDhAgreeExportKey(aliasBob, pubKeyAlice);

258. /* 开始协商，协商生成的密钥由HUKS管理 */
259. await huksDhAgreeInHuksTest(aliasAlice, aliasBob, pubKeyAlice, pubKeyBob, 'agreedKeyFromAlice', 'agreedKeyFromBob');
260. /* 设备A、B删除密钥 */
261. await deleteKeyItem(aliasAlice, emptyOptions);
262. await deleteKeyItem(aliasBob, emptyOptions);
263. }
```

[DH.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/ets/pages/DH.ets#L15-L172)

### ECDH密钥协商用例

准备ECDH密钥协商材料：

```
1. /*
2. * 以下以ECDH密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. function stringToUint8Array(str: string) {
8. let arr: number[] = [];
9. for (let i = 0, j = str.length; i < j; ++i) {
10. arr.push(str.charCodeAt(i));
11. }
12. return new Uint8Array(arr);
13. }

15. function uint8ArrayToString(fileData: Uint8Array) {
16. let dataString = '';
17. for (let i = 0; i < fileData.length; i++) {
18. dataString += String.fromCharCode(fileData[i]);
19. }
20. return dataString;
21. }

23. /*
24. * 确定密钥别名和封装密钥属性参数集
25. */
26. let srcKeyAliasFirst = 'AgreeECDHKeyFirstAlias';
27. let srcKeyAliasSecond = 'AgreeECDHKeySecondAlias';
28. let agreeECDHInData = 'AgreeECDHTestIndata';
29. let finishOutData: Uint8Array;
30. let handle: number;
31. let exportKey: Uint8Array;
32. let exportKeyFirst: Uint8Array;
33. let exportKeySecond: Uint8Array;
34. /* 集成生成密钥参数集 */
35. let genProperties: huks.HuksParam[] = [{
36. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
37. value: huks.HuksKeyAlg.HUKS_ALG_ECC,
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
40. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
43. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
44. }, {
45. tag: huks.HuksTag.HUKS_TAG_DIGEST,
46. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_PADDING,
49. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
52. value: huks.HuksCipherMode.HUKS_MODE_CBC,
53. }
54. ]
55. let genHuksOptions: huks.HuksOptions = {
56. properties: genProperties,
57. inData: new Uint8Array([])
58. }

60. let properties: huks.HuksParam[] = [{
61. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
62. value: huks.HuksKeyAlg.HUKS_ALG_ECDH,
63. }, {
64. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
65. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
68. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_DIGEST,
71. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_PADDING,
74. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
77. value: huks.HuksCipherMode.HUKS_MODE_CBC,
78. }, {
79. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
80. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
81. }
82. ]
83. let huksOptions: huks.HuksOptions = {
84. properties: properties,
85. inData: new Uint8Array([])
86. }
87. /* 集成第一个协商参数集 */
88. const finishProperties: huks.HuksParam[] = [{
89. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
90. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
91. }, {
92. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
93. value: true
94. }, {
95. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
96. value: huks.HuksKeyAlg.HUKS_ALG_AES,
97. }, {
98. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
99. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
100. }, {
101. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
102. value:
103. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
104. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
105. }, {
106. tag: huks.HuksTag.HUKS_TAG_DIGEST,
107. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
108. }, {
109. tag: huks.HuksTag.HUKS_TAG_PADDING,
110. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
111. }, {
112. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
113. value: huks.HuksCipherMode.HUKS_MODE_CBC,
114. }
115. ];
116. let finishOptionsFirst: huks.HuksOptions = {
117. properties: [
118. ...finishProperties, {
119. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
120. value: stringToUint8Array(srcKeyAliasFirst + 'final'),
121. }],
122. inData: stringToUint8Array(agreeECDHInData)
123. }
124. /* 集成第二个协商参数集 */
125. let finishOptionsSecond: huks.HuksOptions = {
126. properties: [
127. ...finishProperties, {
128. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
129. value: stringToUint8Array(srcKeyAliasSecond + 'final'),
130. }],
131. inData: stringToUint8Array(agreeECDHInData)
132. }
```

[ECDH.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/ets/pages/ECDH.ets#L15-L124)

执行密钥协商：

```
1. /* 生成密钥 */
2. async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
3. console.info('promise: enter generateKeyItem');
4. try {
5. await huks.generateKeyItem(keyAlias, huksOptions)
6. .then(() => {
7. console.info(`promise: generateKeyItem success`);
8. }).catch((error: BusinessError) => {
9. console.error(`promise: generateKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
10. })
11. } catch (error) {
12. console.error(`promise: generateKeyItem input arg invalid`);
13. }
14. }

16. /* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
17. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
18. console.info('promise: enter initSession');
19. try {
20. await huks.initSession(keyAlias, huksOptions)
21. .then((data) => {
22. handle = data.handle;
23. console.info(`promise: initSession success`);
24. }).catch((error: BusinessError) => {
25. console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
26. })
27. } catch (error) {
28. console.error(`promise: initSession input arg invalid`);
29. }
30. }

32. /* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
33. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
34. console.info('promise: enter updateSession');
35. try {
36. await huks.updateSession(handle, huksOptions)
37. .then((data) => {
38. console.info(`promise: updateSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
39. }).catch((error: BusinessError) => {
40. console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
41. })
42. } catch (error) {
43. console.error(`promise: updateSession input arg invalid`);
44. }
45. }

47. /* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
48. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
49. console.info('promise: enter finishSession');
50. try {
51. await huks.finishSession(handle, huksOptions)
52. .then((data) => {
53. finishOutData = data.outData as Uint8Array;
54. console.info(`promise: finishSession success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
55. }).catch((error: BusinessError) => {
56. console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
57. })
58. } catch (error) {
59. console.error(`promise: finishSession input arg invalid`);
60. }
61. }

63. /* 导出密钥 */
64. async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
65. console.info('promise: enter exportKeyItem');
66. try {
67. await huks.exportKeyItem(keyAlias, huksOptions)
68. .then((data) => {
69. exportKey = data.outData as Uint8Array;
70. console.info(`promise: exportKey success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
71. }).catch((error: BusinessError) => {
72. console.error(`promise: exportKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
73. })
74. } catch (error) {
75. console.error(`promise: exportKeyItem input arg invalid`);
76. }
77. }

79. /* 删除密钥操作 */
80. async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
81. console.info('promise: enter deleteKeyItem');
82. try {
83. await huks.deleteKeyItem(keyAlias, huksOptions)
84. .then(() => {
85. console.info(`promise: deleteKeyItem success`);
86. }).catch((error: BusinessError) => {
87. console.error(`promise: deleteKeyItem failed, errCode : ${error.code}, errMsg : ${error.message}`);
88. })
89. } catch (error) {
90. console.error(`promise: deleteKeyItem input arg invalid`);
91. }
92. }

94. async function testAgree() {
95. /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
96. /* 2.设备A生成密钥 */
97. await generateKeyItem(srcKeyAliasFirst, genHuksOptions);
98. /* 3.设备B生成密钥 */
99. await generateKeyItem(srcKeyAliasSecond, genHuksOptions);
100. /* 4.设备A、B导出非对称密钥的公钥 */
101. await exportKeyItem(srcKeyAliasFirst, genHuksOptions);
102. exportKeyFirst = exportKey;
103. await exportKeyItem(srcKeyAliasSecond, genHuksOptions);
104. exportKeySecond = exportKey;
105. /* 5.对第一个密钥进行协商（三段式） */
106. await initSession(srcKeyAliasFirst, huksOptions);
107. huksOptions.inData = exportKeySecond;
108. await updateSession(handle, huksOptions);
109. await finishSession(handle, finishOptionsFirst);
110. /* 6.对第二个密钥进行协商（三段式） */
111. await initSession(srcKeyAliasSecond, huksOptions);
112. huksOptions.inData = exportKeyFirst;
113. await updateSession(handle, huksOptions);
114. await finishSession(handle, finishOptionsSecond);
115. /* 7.设备A、B删除密钥 */
116. await deleteKeyItem(srcKeyAliasFirst, huksOptions);
117. await deleteKeyItem(srcKeyAliasSecond, huksOptions);
118. }
```

[ECDH.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyExchange/entry/src/main/ets/pages/ECDH.ets#L126-L247)
