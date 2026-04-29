---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-group-key-arkts
title: 群组密钥(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 其他操作 > 群组密钥 > 群组密钥(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d7d2af8fb2ef16b63e8a508bfc2484d5f8ee7e0b15fb82c262eccab04ba06615
---

从API 23开始，HUKS支持群组密钥功能。群组密钥支持的HUKS密钥操作及详细介绍参考[群组密钥介绍](huks-group-key-overview.md)，本文档以[AES/CBC/PKCS7加解密](huks-group-key-arkts.md#aescbcpkcs7加解密)、[X25519非对称密钥协商](huks-group-key-arkts.md#x25519非对称密钥协商)、[PBKDF2派生密钥](huks-group-key-arkts.md#pbkdf2派生密钥)为例展示群组密钥使用方法。

**配置文件**

使用群组密钥之前，需要在app.json5文件中配置群组信息，配置方法参考[配置文件示例](app-configuration-file.md#配置文件示例)中assetAccessGroups字段的配置方式。

## AES/CBC/PKCS7加解密

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，推荐使用[HUKS\_TAG\_KEY\_OVERRIDE](../harmonyos-references/js-apis-huks.md#hukstag)，避免密钥被覆盖。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 指定密钥别名。
2. 指定待加密的数据。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置加密算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取加密后的密文。

**解密**

1. 指定密钥别名。
2. 指定待解密的密文。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置解密算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取解密后的数据。

**删除密钥**

1. 指定密钥别名。
2. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置密钥删除算法参数配置。需要添加群组密钥标签[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)。
3. 调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

### 开发示例

```
1. /*
2. * 以下以AES/CBC/PKCS7的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
6. import { BusinessError } from "@kit.BasicServicesKit";

8. let aesKeyAlias = 'groupKeyTestAesKeyAlias';
9. let handle: number;
10. let plainText = '123456';
11. let IV = cryptoFramework.createRandom().generateRandomSync(12).data;
12. let cipherData: Uint8Array;
13. /*
14. * 需要在app.json5中配置assetAccessGroups字段新增群组信息
15. */
16. let group = 'ohos.test.groupKey';

18. function StringToUint8Array(str: string) {
19. let arr: number[] = new Array();
20. for (let i = 0, j = str.length; i < j; ++i) {
21. arr.push(str.charCodeAt(i));
22. }
23. return new Uint8Array(arr);
24. }

26. function Uint8ArrayToString(fileData: Uint8Array) {
27. let dataString = '';
28. for (let i = 0; i < fileData.length; i++) {
29. dataString += String.fromCharCode(fileData[i]);
30. }
31. return dataString;
32. }

34. function GetAesGenerateProperties() {
35. let properties: Array<huks.HuksParam> = [{
36. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
37. value: huks.HuksKeyAlg.HUKS_ALG_AES
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
40. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
43. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
44. }, {
45. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
46. value: StringToUint8Array(group)
47. }];
48. return properties;
49. }

51. function GetAesEncryptProperties() {
52. let properties: Array<huks.HuksParam> = [{
53. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
54. value: huks.HuksKeyAlg.HUKS_ALG_AES
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
57. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
60. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
61. }, {
62. tag: huks.HuksTag.HUKS_TAG_PADDING,
63. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
64. }, {
65. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
66. value: huks.HuksCipherMode.HUKS_MODE_CBC
67. }, {
68. tag: huks.HuksTag.HUKS_TAG_IV,
69. value: IV
70. }, {
71. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
72. value: StringToUint8Array(group)
73. }];
74. return properties;
75. }

77. function GetAesDecryptProperties() {
78. let properties: Array<huks.HuksParam> = [{
79. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
80. value: huks.HuksKeyAlg.HUKS_ALG_AES
81. }, {
82. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
83. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
84. }, {
85. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
86. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
87. }, {
88. tag: huks.HuksTag.HUKS_TAG_PADDING,
89. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
90. }, {
91. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
92. value: huks.HuksCipherMode.HUKS_MODE_CBC
93. }, {
94. tag: huks.HuksTag.HUKS_TAG_IV,
95. value: IV
96. }, {
97. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
98. value: StringToUint8Array(group)
99. }];
100. return properties;
101. }

103. async function GenerateAesKey() {
104. /*
105. * 模拟生成密钥场景
106. * 1. 确定密钥别名
107. */
108. /*
109. * 2. 获取生成密钥算法参数配置
110. */
111. let genProperties = GetAesGenerateProperties();
112. let options: huks.HuksOptions = {
113. properties: genProperties
114. }
115. /*
116. * 3. 调用generateKeyItem
117. */
118. await huks.generateKeyItem(aesKeyAlias, options)
119. .then(() => {
120. console.info(`promise: generate AES Key success`);
121. }).catch((error: BusinessError) => {
122. console.error(`promise: generate AES Key failed, errCode: ${error.code}, errMsg: ${error.message}`);
123. })
124. }

126. async function EncryptData() {
127. /*
128. * 模拟加密场景
129. * 1. 获取密钥别名
130. */
131. /*
132. * 2. 获取待加密的数据
133. */
134. /*
135. * 3. 获取加密算法参数配置
136. */
137. let encryptProperties = GetAesEncryptProperties();
138. let options: huks.HuksOptions = {
139. properties: encryptProperties,
140. inData: StringToUint8Array(plainText)
141. }
142. /*
143. * 4. 调用initSession获取handle
144. */
145. await huks.initSession(aesKeyAlias, options)
146. .then((data) => {
147. handle = data.handle;
148. }).catch((error: BusinessError) => {
149. console.error(`promise: init EncryptData failed, errCode: ${error.code}, errMsg: ${error.message}`);
150. })
151. /*
152. * 5. 调用finishSession获取加密后的密文
153. */
154. await huks.finishSession(handle, options)
155. .then((data) => {
156. console.info(`promise: encrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
157. cipherData = data.outData as Uint8Array;
158. }).catch((error: BusinessError) => {
159. console.error(`promise: encrypt data failed, errCode: ${error.code}, errMsg: ${error.message}`);
160. })
161. }

163. async function DecryptData() {
164. /*
165. * 模拟解密场景
166. * 1. 获取密钥别名
167. */
168. /*
169. * 2. 获取待解密的密文
170. */
171. /*
172. * 3. 获取解密算法参数配置
173. */
174. let decryptOptions = GetAesDecryptProperties()
175. let options: huks.HuksOptions = {
176. properties: decryptOptions,
177. inData: cipherData
178. }
179. /*
180. * 4. 调用initSession获取handle
181. */
182. await huks.initSession(aesKeyAlias, options)
183. .then((data) => {
184. handle = data.handle;
185. }).catch((error: BusinessError) => {
186. console.error(`promise: init DecryptData failed, errCode: ${error.code}, errMsg: ${error.message}`);
187. })
188. /*
189. * 5. 调用finishSession获取解密后的数据
190. */
191. await huks.finishSession(handle, options)
192. .then((data) => {
193. console.info(`promise: decrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
194. }).catch((error: BusinessError) => {
195. console.error(`promise: decrypt data failed, errCode: ${error.code}, errMsg: ${error.message}`);
196. })
197. }

199. async function DeleteKey() {
200. /*
201. * 模拟删除密钥场景
202. * 1. 获取密钥别名
203. */
204. let deleteProperties: Array<huks.HuksParam> = [
205. {
206. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
207. value: StringToUint8Array(group)
208. }
209. ]
210. let deleteOptions: huks.HuksOptions = {
211. properties: deleteProperties
212. }
213. /*
214. * 2. 调用deleteKeyItem删除密钥
215. */
216. await huks.deleteKeyItem(aesKeyAlias, deleteOptions)
217. .then(() => {
218. console.info(`promise: delete data success`);
219. }).catch((error: BusinessError) => {
220. console.error(`promise: delete data failed, errCode: ${error.code}, errMsg: ${error.message}`);
221. })
222. }

224. async function TestGroupKeyEncryptDecrypt() {
225. await GenerateAesKey();
226. await EncryptData();
227. await DecryptData();
228. await DeleteKey();
229. }
```

## X25519非对称密钥协商

### 开发步骤

**生成密钥**

设备A、设备B各自生成一个非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)或[密钥导入](huks-key-import-overview.md)。

密钥生成时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于生成群组密钥。

**导出密钥**

设备A、B导出非对称密钥对的公钥材料，具体请参考[密钥导出](huks-export-key-arkts.md)。

导出密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于导出群组密钥。

**密钥协商**

设备A、B分别基于本端私钥和对端设备的公钥，协商出共享密钥。

密钥协商时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于协商群组密钥。

**删除密钥**

当密钥废弃不用时，设备A、B均需要删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

删除密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于删除群组密钥。

### 开发示例

```
1. /*
2. * 以下以X25519密钥的Promise操作使用为例
3. * 通过群组密钥协商群组密钥
4. */
5. import { huks } from '@kit.UniversalKeystoreKit';
6. import { BusinessError } from "@kit.BasicServicesKit";

8. function StringToUint8Array(str: string) {
9. let arr: number[] = new Array();
10. for (let i = 0, j = str.length; i < j; ++i) {
11. arr.push(str.charCodeAt(i));
12. }
13. return new Uint8Array(arr);
14. }

16. function Uint8ArrayToString(fileData: Uint8Array) {
17. let dataString = '';
18. for (let i = 0; i < fileData.length; i++) {
19. dataString += String.fromCharCode(fileData[i]);
20. }
21. return dataString;
22. }

24. /*
25. * 确定密钥别名和封装密钥属性参数集
26. */
27. let srcKeyAliasFirst = "AgreeX25519KeyFirstAlias";
28. let srcKeyAliasSecond = "AgreeX25519KeySecondAlias";
29. let agreeX25519InData = 'AgreeX25519TestIndata';
30. let finishOutData: Uint8Array;
31. let handle: number;
32. let exportKey: Uint8Array;
33. let exportKeyFirst: Uint8Array;
34. let exportKeySecond: Uint8Array;
35. /*
36. * 需要在app.json5中配置assetAccessGroups字段新增群组信息
37. */
38. let group = 'ohos.test.groupKey';
39. /* 集成生成密钥参数集 */
40. let properties: Array<huks.HuksParam> = [{
41. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
42. value: huks.HuksKeyAlg.HUKS_ALG_X25519,
43. }, {
44. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
45. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_AGREE,
46. }, {
47. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
48. value: huks.HuksKeySize.HUKS_CURVE25519_KEY_SIZE_256,
49. }, {
50. tag: huks.HuksTag.HUKS_TAG_DIGEST,
51. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_PADDING,
54. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
57. value: huks.HuksCipherMode.HUKS_MODE_CBC,
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
60. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
61. }, {
62. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
63. value: StringToUint8Array(group)
64. }
65. ];
66. let HuksOptions: huks.HuksOptions = {
67. properties: properties,
68. inData: new Uint8Array(new Array())
69. }
70. const finishProperties: Array<huks.HuksParam> = [{
71. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
72. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
73. }, {
74. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
75. value: true
76. }, {
77. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
78. value: huks.HuksKeyAlg.HUKS_ALG_AES,
79. }, {
80. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
81. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
82. }, {
83. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
84. value:
85. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
86. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
87. }, {
88. tag: huks.HuksTag.HUKS_TAG_DIGEST,
89. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
90. }, {
91. tag: huks.HuksTag.HUKS_TAG_PADDING,
92. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
93. }, {
94. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
95. value: huks.HuksCipherMode.HUKS_MODE_ECB,
96. }, {
97. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
98. value: StringToUint8Array(group)
99. }
100. ];
101. /* 集成第一个协商参数集 */
102. let finishOptionsFirst: huks.HuksOptions = {
103. properties: [
104. ...finishProperties, {
105. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
106. value: StringToUint8Array(srcKeyAliasFirst + 'final'),
107. }],
108. inData: StringToUint8Array(agreeX25519InData)
109. }
110. /* 集成第二个协商参数集 */
111. let finishOptionsSecond: huks.HuksOptions = {
112. properties: [
113. ...finishProperties, {
114. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
115. value: StringToUint8Array(srcKeyAliasSecond + 'final'),
116. }],
117. inData: StringToUint8Array(agreeX25519InData)
118. }

120. /* 生成密钥 */
121. async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
122. console.info("promise: enter generateKeyItem");
123. try {
124. await huks.generateKeyItem(keyAlias, huksOptions)
125. .then(() => {
126. console.info(`promise: generateKeyItem success`);
127. }).catch((error: BusinessError) => {
128. console.error(`promise: generateKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
129. })
130. } catch (error) {
131. console.error(`promise: generateKeyItem input arg invalid`);
132. }
133. }

135. /* 初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选） */
136. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
137. console.info("promise: enter initSession");
138. try {
139. await huks.initSession(keyAlias, huksOptions)
140. .then((data) => {
141. handle = data.handle;
142. console.info(`promise: initSession success`);
143. }).catch((error: BusinessError) => {
144. console.error(`promise: initSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
145. })
146. } catch (error) {
147. console.error(`promise: initSession input arg invalid`);
148. }
149. }

151. /* 分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据 */
152. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
153. console.info("promise: enter updateSession");
154. try {
155. await huks.updateSession(handle, huksOptions)
156. .then((data) => {
157. console.info(`promise: updateSession success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
158. }).catch((error: BusinessError) => {
159. console.error(`promise: updateSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
160. })
161. } catch (error) {
162. console.error(`promise: updateSession input arg invalid`);
163. }
164. }

166. /* 结束密钥会话并进行相应的密钥操作，输出处理数据 */
167. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
168. console.info("promise: enter finishSession");
169. try {
170. await huks.finishSession(handle, huksOptions)
171. .then((data) => {
172. finishOutData = data.outData as Uint8Array;
173. console.info(`promise: finishSession success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
174. }).catch((error: BusinessError) => {
175. console.error(`promise: finishSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
176. })
177. } catch (error) {
178. console.error(`promise: finishSession input arg invalid`);
179. }
180. }

182. /* 导出密钥 */
183. async function exportKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
184. console.info("promise: enter exportKeyItem");
185. try {
186. await huks.exportKeyItem(keyAlias, huksOptions)
187. .then((data) => {
188. exportKey = data.outData as Uint8Array;
189. console.info(`promise: exportKey success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
190. }).catch((error: BusinessError) => {
191. console.error(`promise: exportKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
192. })
193. } catch (error) {
194. console.error(`promise: exportKeyItem input arg invalid`);
195. }
196. }

198. /* 删除密钥操作 */
199. async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
200. console.info("promise: enter deleteKeyItem");
201. try {
202. await huks.deleteKeyItem(keyAlias, huksOptions)
203. .then(() => {
204. console.info(`promise: deleteKeyItem success`);
205. }).catch((error: BusinessError) => {
206. console.error(`promise: deleteKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
207. })
208. } catch (error) {
209. console.error(`promise: deleteKeyItem input arg invalid`);
210. }
211. }

213. async function testAgree() {
214. /* 1.确定密钥别名并集成要参数集。A设备：srcKeyAliasFirst；B设备：srcKeyAliasSecond */
215. /* 2.设备A生成密钥 */
216. await generateKeyItem(srcKeyAliasFirst, HuksOptions);
217. /* 3.设备B生成密钥 */
218. await generateKeyItem(srcKeyAliasSecond, HuksOptions);
219. /* 4.设备A、B导出非对称密钥的公钥 */
220. await exportKeyItem(srcKeyAliasFirst, HuksOptions);
221. exportKeyFirst = exportKey;
222. await exportKeyItem(srcKeyAliasSecond, HuksOptions);
223. exportKeySecond = exportKey;
224. /* 5.对第一个密钥进行协商（三段式） */
225. await initSession(srcKeyAliasFirst, HuksOptions);
226. HuksOptions.inData = exportKeySecond;
227. await updateSession(handle, HuksOptions);
228. await finishSession(handle, finishOptionsFirst);
229. /* 6.对第二个密钥进行协商（三段式） */
230. await initSession(srcKeyAliasSecond, HuksOptions);
231. HuksOptions.inData = exportKeyFirst;
232. await updateSession(handle, HuksOptions);
233. await finishSession(handle, finishOptionsSecond);
234. /* 7.设备A、B删除密钥 */
235. await deleteKeyItem(srcKeyAliasFirst, HuksOptions);
236. await deleteKeyItem(srcKeyAliasSecond, HuksOptions);
237. }
```

## PBKDF2派生密钥

### 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 密钥生成时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于生成群组密钥。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions，添加参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于派生群组密钥。
2. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
3. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
4. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

删除密钥时，指定参数[HUKS\_TAG\_KEY\_ACCESS\_GROUP](../harmonyos-references/js-apis-huks.md#hukstag)，用于删除群组密钥。

### 开发示例

```
1. /*
2. * 以下以PBKDF2密钥的Promise操作使用为例
3. * 使用群组密钥派生群组密钥
4. */
5. import { huks } from '@kit.UniversalKeystoreKit';
6. import { BusinessError } from "@kit.BasicServicesKit";

8. function StringToUint8Array(str: string) {
9. let arr: number[] = new Array();
10. for (let i = 0, j = str.length; i < j; ++i) {
11. arr.push(str.charCodeAt(i));
12. }
13. return new Uint8Array(arr);
14. }

16. function Uint8ArrayToString(fileData: Uint8Array) {
17. let dataString = '';
18. for (let i = 0; i < fileData.length; i++) {
19. dataString += String.fromCharCode(fileData[i]);
20. }
21. return dataString;
22. }

24. /*
25. * 确定密钥别名和封装密钥属性参数集
26. */
27. let srcKeyAlias = "pbkdf2Key";
28. let salt = "mySalt";
29. let iterationCount = 10000;
30. let derivedKeySize = 32;
31. let handle: number;
32. let finishOutData: Uint8Array;
33. /*
34. * 需要在app.json5中配置assetAccessGroups字段新增群组信息
35. */
36. let group = 'ohos.test.groupKey';

38. /* 集成生成密钥参数集 */
39. let properties: Array<huks.HuksParam> = [{
40. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
41. value: huks.HuksKeyAlg.HUKS_ALG_AES,
42. }, {
43. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
44. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
45. }, {
46. tag: huks.HuksTag.HUKS_TAG_DIGEST,
47. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
48. }, {
49. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
50. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
51. }, {
52. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
53. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
54. }, {
55. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
56. value: StringToUint8Array(group)
57. }
58. ];

60. let huksOptions: huks.HuksOptions = {
61. properties: properties,
62. inData: new Uint8Array(new Array())
63. }

65. /* 集成init时密钥参数集 */
66. let initProperties: Array<huks.HuksParam> = [{
67. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
68. value: huks.HuksKeyAlg.HUKS_ALG_PBKDF2,
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
71. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_DIGEST,
74. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
77. value: derivedKeySize,
78. }, {
79. tag: huks.HuksTag.HUKS_TAG_ITERATION,
80. value: iterationCount,
81. }, {
82. tag: huks.HuksTag.HUKS_TAG_SALT,
83. value: StringToUint8Array(salt),
84. }, {
85. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
86. value: StringToUint8Array(group)
87. }
88. ];

90. let initOptions: huks.HuksOptions = {
91. properties: initProperties,
92. inData: new Uint8Array(new Array())
93. }

95. /* 集成finish时密钥参数集 */
96. let finishProperties: Array<huks.HuksParam> = [{
97. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
98. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
99. }, {
100. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
101. value: true,
102. }, {
103. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
104. value: huks.HuksKeyAlg.HUKS_ALG_AES,
105. }, {
106. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
107. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
108. }, {
109. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
110. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
111. }, {
112. tag: huks.HuksTag.HUKS_TAG_DIGEST,
113. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
114. }, {
115. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
116. value: StringToUint8Array(srcKeyAlias),
117. }, {
118. tag: huks.HuksTag.HUKS_TAG_PADDING,
119. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
120. }, {
121. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
122. value: huks.HuksCipherMode.HUKS_MODE_ECB,
123. }, {
124. tag: huks.HuksTag.HUKS_TAG_KEY_ACCESS_GROUP,
125. value: StringToUint8Array(group)
126. }
127. ];

129. let finishOptions: huks.HuksOptions = {
130. properties: finishProperties,
131. inData: new Uint8Array(new Array())
132. }

134. async function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
135. console.info(`promise: enter generateKeyItem`);
136. try {
137. await huks.generateKeyItem(keyAlias, huksOptions)
138. .then(() => {
139. console.info(`promise: generateKeyItem success`);
140. }).catch((error: BusinessError) => {
141. console.error(`promise: generateKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
142. })
143. } catch (error) {
144. console.error(`promise: generateKeyItem input arg invalid`);
145. }
146. }

148. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
149. console.info(`promise: enter initSession`);
150. try {
151. await huks.initSession(keyAlias, huksOptions)
152. .then((data) => {
153. handle = data.handle;
154. console.info(`promise: initSession success`);
155. }).catch((error: BusinessError) => {
156. console.error(`promise: initSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
157. })
158. } catch (error) {
159. console.error(`promise: initSession input arg invalid`);
160. }
161. }

163. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
164. console.info(`promise: enter updateSession`);
165. try {
166. await huks.updateSession(handle, huksOptions)
167. .then((data) => {
168. let outData = data.outData as Uint8Array;
169. console.info(`promise: updateSession success, data = ${Uint8ArrayToString(outData)}`);
170. }).catch((error: BusinessError) => {
171. console.error(`promise: updateSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
172. })
173. } catch (error) {
174. console.error(`promise: updateSession input arg invalid`);
175. }
176. }

178. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
179. console.info(`promise: enter finishSession`);
180. try {
181. await huks.finishSession(handle, huksOptions)
182. .then((data) => {
183. let outData = data.outData as Uint8Array;
184. console.info(`promise: finishSession success, data = ${Uint8ArrayToString(outData)}`);
185. }).catch((error: BusinessError) => {
186. console.error(`promise: finishSession failed, errCode: ${error.code}, errMsg: ${error.message}`);
187. })
188. } catch (error) {
189. console.error(`promise: finishSession input arg invalid`);
190. }
191. }

193. async function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
194. console.info(`promise: enter deleteKeyItem`);
195. try {
196. await huks.deleteKeyItem(keyAlias, huksOptions)
197. .then(() => {
198. console.info(`promise: deleteKeyItem success`);
199. }).catch((error: BusinessError) => {
200. console.error(`promise: deleteKeyItem failed, errCode: ${error.code}, errMsg: ${error.message}`);
201. })
202. } catch (error) {
203. console.error(`promise: deleteKeyItem input arg invalid`);
204. }
205. }
206. async function testDerive() {
207. /* 生成密钥 */
208. await generateKeyItem(srcKeyAlias, huksOptions);
209. /* 进行派生操作 */
210. await initSession(srcKeyAlias, initOptions);
211. await updateSession(handle, initOptions);
212. await finishSession(handle, finishOptions);
213. await deleteKeyItem(srcKeyAlias, huksOptions);
214. }
```
