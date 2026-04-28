---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-arkts
title: 密钥派生(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥派生 > 密钥派生(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33a1f3580bb1dd49bf3ffa93db39185ba078f6f0cb79a75b50a247bac81c00c1
---

以PBKDF2和HKDF256密钥为例，完成密钥派生。具体的场景介绍及支持的算法规格，请参考[密钥派生支持的算法](huks-key-derivation-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集，可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识基于该密钥派生出的密钥是否由HUKS管理。

   * 当TAG设置为HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS时，表示基于该密钥派生出的密钥，由HUKS管理，可保证派生密钥全生命周期不出安全环境。
   * 当TAG设置为HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED时，表示基于该密钥派生出的密钥，返回给调用方管理，由业务自行保证密钥安全。
   * 若业务未设置TAG的具体值，表示基于该密钥派生出的密钥，即可由HUKS管理，也可返回给调用方管理，业务可在后续派生时再选择使用何种方式保护密钥。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**密钥派生**

1. 获取密钥别名，指定对应的属性参数HuksOptions。

   可指定参数HUKS\_TAG\_DERIVED\_AGREED\_KEY\_STORAGE\_FLAG（可选），用于标识派生得到的密钥是否由HUKS管理。

   | 生成 | 派生 | 规格 |
   | --- | --- | --- |
   | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
   | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
   | 未指定TAG具体值 | HUKS\_STORAGE\_ONLY\_USED\_IN\_HUKS | 密钥由HUKS管理 |
   | 未指定TAG具体值 | HUKS\_STORAGE\_KEY\_EXPORT\_ALLOWED | 密钥返回给调用方管理 |
   | 未指定TAG具体值 | 未指定TAG具体值 | 密钥返回给调用方管理 |

   注：派生时指定的TAG值，不可与生成时指定的TAG值冲突。表格中仅列举有效的指定方式。
2. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
3. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
4. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，完成派生。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

### HKDF

准备HKDF密钥派生材料

```
1. /*
2. * 以下以HKDF密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. /*
7. * 确定密钥别名和封装密钥属性参数集
8. */
9. let srcKeyAlias = 'hkdf_Key';
10. let deriveHkdfInData = 'deriveHkdfTestIndata';
11. let handle: number;
12. let finishOutData: Uint8Array;
13. let huksKeyDeriveKeySize = 32;
14. /* 集成生成密钥参数集 */
15. let properties: huks.HuksParam[] = [
16. {
17. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
18. value: huks.HuksKeyAlg.HUKS_ALG_AES,
19. }, {
20. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
21. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
22. }, {
23. tag: huks.HuksTag.HUKS_TAG_DIGEST,
24. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
25. }, {
26. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
27. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128,
28. }, {
29. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
30. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
31. }];

33. let huksOptions: huks.HuksOptions = {
34. properties: properties,
35. inData: new Uint8Array([])
36. }
37. /* 集成init时密钥参数集 */
38. let initProperties: huks.HuksParam[] = [{
39. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
40. value: huks.HuksKeyAlg.HUKS_ALG_HKDF,
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
43. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
44. }, {
45. tag: huks.HuksTag.HUKS_TAG_DIGEST,
46. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
49. value: huksKeyDeriveKeySize,
50. }];

52. let initOptions: huks.HuksOptions = {
53. properties: initProperties,
54. inData: new Uint8Array([])
55. }
56. /* 集成finish时密钥参数集 */
57. let finishProperties: huks.HuksParam[] = [{
58. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
59. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
60. }, {
61. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
62. value: true,
63. }, {
64. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
65. value: huks.HuksKeyAlg.HUKS_ALG_AES,
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
68. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
71. value:
72. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
73. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
74. }, {
75. tag: huks.HuksTag.HUKS_TAG_DIGEST,
76. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
77. }, {
78. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
79. value: stringToUint8Array(srcKeyAlias),
80. }, {
81. tag: huks.HuksTag.HUKS_TAG_PADDING,
82. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
83. }, {
84. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
85. value: huks.HuksCipherMode.HUKS_MODE_ECB,
86. }];
87. let finishOptions: huks.HuksOptions = {
88. properties: finishProperties,
89. inData: new Uint8Array([])
90. }

92. function stringToUint8Array(str: String) {
93. let arr: number[] = [];
94. for (let i = 0, j = str.length; i < j; ++i) {
95. arr.push(str.charCodeAt(i));
96. }
97. return new Uint8Array(arr);
98. }

100. class ThrowObject {
101. public isThrow = false;
102. }
```

[HKDF.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/ets/pages/HKDF.ets#L17-L120)

执行密钥派生

```
1. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
2. return new Promise<void>((resolve, reject) => {
3. try {
4. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
5. if (error) {
6. reject(error);
7. } else {
8. resolve(data);
9. }
10. });
11. } catch (error) {
12. throwObject.isThrow = true;
13. throw (error as Error);
14. }
15. });
16. }

18. async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
19. console.info(`enter promise generateKeyItem`);
20. let throwObject: ThrowObject = { isThrow: false };
21. try {
22. await generateKeyItem(keyAlias, huksOptions, throwObject)
23. .then((data) => {
24. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
25. })
26. .catch((error: Error) => {
27. if (throwObject.isThrow) {
28. throw (error as Error);
29. } else {
30. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
31. throw (error as Error);
32. }
33. });
34. } catch (error) {
35. console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
36. throw (error as Error);
37. }
38. }

40. function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
41. return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
42. try {
43. huks.initSession(keyAlias, huksOptions, (error, data) => {
44. if (error) {
45. reject(error);
46. } else {
47. resolve(data);
48. }
49. });
50. } catch (error) {
51. throwObject.isThrow = true;
52. throw (error as Error);
53. }
54. });
55. }

57. async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
58. console.info(`enter promise doInit`);
59. let throwObject: ThrowObject = { isThrow: false };
60. try {
61. await initSession(keyAlias, huksOptions, throwObject)
62. .then((data) => {
63. console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
64. handle = data.handle;
65. })
66. .catch((error: Error) => {
67. if (throwObject.isThrow) {
68. throw (error as Error);
69. } else {
70. console.error(`promise: doInit failed, ${JSON.stringify(error)}`);
71. throw (error as Error);
72. }
73. });
74. } catch (error) {
75. console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
76. throw (error as Error);
77. }
78. }

80. function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
81. return new Promise<huks.HuksOptions>((resolve, reject) => {
82. try {
83. huks.updateSession(handle, huksOptions, (error, data) => {
84. if (error) {
85. reject(error);
86. } else {
87. resolve(data);
88. }
89. });
90. } catch (error) {
91. throwObject.isThrow = true;
92. throw (error as Error);
93. }
94. });
95. }

97. async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
98. console.info(`enter promise doUpdate`);
99. let throwObject: ThrowObject = { isThrow: false };
100. try {
101. await updateSession(handle, huksOptions, throwObject)
102. .then((data) => {
103. console.info(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
104. })
105. .catch((error: Error) => {
106. if (throwObject.isThrow) {
107. throw (error as Error);
108. } else {
109. console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
110. throw (error as Error);
111. }
112. });
113. } catch (error) {
114. console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
115. throw (error as Error);
116. }
117. }

119. function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
120. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
121. try {
122. huks.finishSession(handle, huksOptions, (error, data) => {
123. if (error) {
124. reject(error);
125. } else {
126. resolve(data);
127. }
128. });
129. } catch (error) {
130. throwObject.isThrow = true;
131. throw (error as Error);
132. }
133. });
134. }

136. async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
137. console.info(`enter promise doFinish`);
138. let throwObject: ThrowObject = { isThrow: false };
139. try {
140. await finishSession(handle, huksOptions, throwObject)
141. .then((data) => {
142. finishOutData = data.outData as Uint8Array;
143. console.info(`promise: doFinish success, data = ${JSON.stringify(data)}`);
144. })
145. .catch((error: Error) => {
146. if (throwObject.isThrow) {
147. throw (error as Error);
148. } else {
149. console.error(`promise: doFinish failed, ${JSON.stringify(error)}`);
150. throw (error as Error);
151. }
152. });
153. } catch (error) {
154. console.error(`promise: doFinish input arg invalid, ${JSON.stringify(error)}`);
155. throw (error as Error);
156. }
157. }

159. function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
160. return new Promise<void>((resolve, reject) => {
161. try {
162. huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
163. if (error) {
164. reject(error);
165. } else {
166. resolve(data);
167. }
168. });
169. } catch (error) {
170. throwObject.isThrow = true;
171. throw (error as Error);
172. }
173. });
174. }

176. async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
177. console.info(`enter promise deleteKeyItem`);
178. let throwObject: ThrowObject = { isThrow: false };
179. try {
180. await deleteKeyItem(keyAlias, huksOptions, throwObject)
181. .then((data) => {
182. console.info(`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}`);
183. })
184. .catch((error: Error) => {
185. if (throwObject.isThrow) {
186. throw (error as Error);
187. } else {
188. console.error(`promise: deleteKeyItem failed, ${JSON.stringify(error)}`);
189. throw (error as Error);
190. }
191. });
192. } catch (error) {
193. console.error(`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}`);
194. throw (error as Error);
195. }
196. }

198. async function testDerive() {
199. /* 生成密钥 */
200. await publicGenKeyFunc(srcKeyAlias, huksOptions);
201. /* 进行派生操作 */
202. await publicInitFunc(srcKeyAlias, initOptions);
203. initOptions.inData = stringToUint8Array(deriveHkdfInData);
204. await publicUpdateFunc(handle, initOptions);
205. await publicFinishFunc(handle, finishOptions);
206. await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
207. }
```

[HKDF.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/ets/pages/HKDF.ets#L122-L330)

### PBKDF2

准备PBKDF2密钥派生材料

```
1. /*
2. * 以下以PBKDF2密钥的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. /*
7. * 确定密钥别名和封装密钥属性参数集
8. */
9. let srcKeyAlias = 'pbkdf2_Key';
10. let salt = 'mySalt';
11. let iterationCount = 10000;
12. let derivedKeySize = 32;
13. let handle: number;
14. let finishOutData: Uint8Array;

16. /* 集成生成密钥参数集 */
17. let properties: huks.HuksParam[] = [
18. {
19. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
20. value: huks.HuksKeyAlg.HUKS_ALG_AES,
21. }, {
22. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
23. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
24. }, {
25. tag: huks.HuksTag.HUKS_TAG_DIGEST,
26. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
27. }, {
28. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
29. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
30. }, {
31. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
32. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
33. }
34. ];

36. let huksOptions: huks.HuksOptions = {
37. properties: properties,
38. inData: new Uint8Array([])
39. }

41. /* 集成init时密钥参数集 */
42. let initProperties: huks.HuksParam[] = [
43. {
44. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
45. value: huks.HuksKeyAlg.HUKS_ALG_PBKDF2,
46. }, {
47. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
48. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DERIVE,
49. }, {
50. tag: huks.HuksTag.HUKS_TAG_DIGEST,
51. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256,
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_DERIVE_KEY_SIZE,
54. value: derivedKeySize,
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_ITERATION,
57. value: iterationCount,
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_SALT,
60. value: stringToUint8Array(salt),
61. }
62. ];

64. let initOptions: huks.HuksOptions = {
65. properties: initProperties,
66. inData: new Uint8Array([])
67. }

69. /* 集成finish时密钥参数集 */
70. let finishProperties: huks.HuksParam[] = [
71. {
72. tag: huks.HuksTag.HUKS_TAG_DERIVED_AGREED_KEY_STORAGE_FLAG,
73. value: huks.HuksKeyStorageType.HUKS_STORAGE_ONLY_USED_IN_HUKS,
74. }, {
75. tag: huks.HuksTag.HUKS_TAG_IS_KEY_ALIAS,
76. value: true,
77. }, {
78. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
79. value: huks.HuksKeyAlg.HUKS_ALG_AES,
80. }, {
81. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
82. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256,
83. }, {
84. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
85. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
86. }, {
87. tag: huks.HuksTag.HUKS_TAG_DIGEST,
88. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE,
89. }, {
90. tag: huks.HuksTag.HUKS_TAG_KEY_ALIAS,
91. value: stringToUint8Array(srcKeyAlias),
92. }, {
93. tag: huks.HuksTag.HUKS_TAG_PADDING,
94. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
95. }, {
96. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
97. value: huks.HuksCipherMode.HUKS_MODE_ECB,
98. }
99. ];

101. let finishOptions: huks.HuksOptions = {
102. properties: finishProperties,
103. inData: new Uint8Array([])
104. }

106. function stringToUint8Array(str: String) {
107. let arr: number[] = [];
108. for (let i = 0, j = str.length; i < j; ++i) {
109. arr.push(str.charCodeAt(i));
110. }
111. return new Uint8Array(arr);
112. }

114. class ThrowObject {
115. public isThrow = false;
116. }
```

[PBKDF2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/ets/pages/PBKDF2.ets#L15-L132)

执行密钥派生

```
1. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
2. return new Promise<void>((resolve, reject) => {
3. try {
4. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
5. if (error) {
6. reject(error);
7. } else {
8. resolve(data);
9. }
10. });
11. } catch (error) {
12. throwObject.isThrow = true;
13. throw (error as Error);
14. }
15. });
16. }

18. async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
19. console.info(`enter promise generateKeyItem`);
20. let throwObject: ThrowObject = { isThrow: false };
21. try {
22. await generateKeyItem(keyAlias, huksOptions, throwObject)
23. .then((data) => {
24. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
25. })
26. .catch((error: Error) => {
27. if (throwObject.isThrow) {
28. throw (error as Error);
29. } else {
30. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
31. throw (error as Error);
32. }
33. });
34. } catch (error) {
35. console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
36. throw (error as Error);
37. }
38. }

40. function initSession(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
41. return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
42. try {
43. huks.initSession(keyAlias, huksOptions, (error, data) => {
44. if (error) {
45. reject(error);
46. } else {
47. resolve(data);
48. }
49. });
50. } catch (error) {
51. throwObject.isThrow = true;
52. throw (error as Error);
53. }
54. });
55. }

57. async function publicInitFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
58. console.info(`enter promise doInit`);
59. let throwObject: ThrowObject = { isThrow: false };
60. try {
61. await initSession(keyAlias, huksOptions, throwObject)
62. .then((data) => {
63. console.info(`promise: doInit success, data = ${JSON.stringify(data)}`);
64. handle = data.handle;
65. })
66. .catch((error: Error) => {
67. if (throwObject.isThrow) {
68. throw (error as Error);
69. } else {
70. console.error(`promise: doInit failed, ${JSON.stringify(error)}`);
71. throw (error as Error);
72. }
73. });
74. } catch (error) {
75. console.error(`promise: doInit input arg invalid, ${JSON.stringify(error)}`);
76. throw (error as Error);
77. }
78. }

80. function updateSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
81. return new Promise<huks.HuksOptions>((resolve, reject) => {
82. try {
83. huks.updateSession(handle, huksOptions, (error, data) => {
84. if (error) {
85. reject(error);
86. } else {
87. resolve(data);
88. }
89. });
90. } catch (error) {
91. throwObject.isThrow = true;
92. throw (error as Error);
93. }
94. });
95. }

97. async function publicUpdateFunc(handle: number, huksOptions: huks.HuksOptions) {
98. console.info(`enter promise doUpdate`);
99. let throwObject: ThrowObject = { isThrow: false };
100. try {
101. await updateSession(handle, huksOptions, throwObject)
102. .then((data) => {
103. console.info(`promise: doUpdate success, data = ${JSON.stringify(data)}`);
104. })
105. .catch((error: Error) => {
106. if (throwObject.isThrow) {
107. throw (error as Error);
108. } else {
109. console.error(`promise: doUpdate failed, ${JSON.stringify(error)}`);
110. throw (error as Error);
111. }
112. });
113. } catch (error) {
114. console.error(`promise: doUpdate input arg invalid, ${JSON.stringify(error)}`);
115. throw (error as Error);
116. }
117. }

119. function finishSession(handle: number, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
120. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
121. try {
122. huks.finishSession(handle, huksOptions, (error, data) => {
123. if (error) {
124. reject(error);
125. } else {
126. resolve(data);
127. }
128. });
129. } catch (error) {
130. throwObject.isThrow = true;
131. throw (error as Error);
132. }
133. });
134. }

136. async function publicFinishFunc(handle: number, huksOptions: huks.HuksOptions) {
137. console.info(`enter promise doFinish`);
138. let throwObject: ThrowObject = { isThrow: false };
139. try {
140. await finishSession(handle, huksOptions, throwObject)
141. .then((data) => {
142. finishOutData = data.outData as Uint8Array;
143. console.info(`promise: doFinish success, data = ${JSON.stringify(data)}`);
144. })
145. .catch((error: Error) => {
146. if (throwObject.isThrow) {
147. throw (error as Error);
148. } else {
149. console.error(`promise: doFinish failed, ${JSON.stringify(error)}`);
150. throw (error as Error);
151. }
152. });
153. } catch (error) {
154. console.error(`promise: doFinish input arg invalid, ${JSON.stringify(error)}`);
155. throw (error as Error);
156. }
157. }

159. function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
160. return new Promise<void>((resolve, reject) => {
161. try {
162. huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
163. if (error) {
164. reject(error);
165. } else {
166. resolve(data);
167. }
168. });
169. } catch (error) {
170. throwObject.isThrow = true;
171. throw (error as Error);
172. }
173. });
174. }

176. async function publicDeleteKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
177. console.info(`enter promise deleteKeyItem`);
178. let throwObject: ThrowObject = { isThrow: false };
179. try {
180. await deleteKeyItem(keyAlias, huksOptions, throwObject)
181. .then((data) => {
182. console.info(`promise: deleteKeyItem key success, data = ${JSON.stringify(data)}`);
183. })
184. .catch((error: Error) => {
185. if (throwObject.isThrow) {
186. throw (error as Error);
187. } else {
188. console.error(`promise: deleteKeyItem failed, ${JSON.stringify(error)}`);
189. throw (error as Error);
190. }
191. });
192. } catch (error) {
193. console.error(`promise: deleteKeyItem input arg invalid, ${JSON.stringify(error)}`);
194. throw (error as Error);
195. }
196. }

198. async function testDerive() {
199. /* 生成密钥 */
200. await publicGenKeyFunc(srcKeyAlias, huksOptions);
201. /* 进行派生操作 */
202. await publicInitFunc(srcKeyAlias, initOptions);
203. await publicUpdateFunc(handle, initOptions);
204. await publicFinishFunc(handle, finishOptions);
205. await publicDeleteKeyFunc(srcKeyAlias, huksOptions);
206. }
```

[PBKDF2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/KeyDerivation/entry/src/main/ets/pages/PBKDF2.ets#L134-L341)
