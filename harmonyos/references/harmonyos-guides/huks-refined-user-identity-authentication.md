---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-refined-user-identity-authentication
title: 细粒度用户身份认证访问控制开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 访问控制 > 细粒度用户身份认证访问控制开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bef2b95769143415940998c6481c3f1efd44ea9a3c037b4c21f82742a7ae3383
---

细粒度用户身份认证访问控制是基于已有用户身份认证访问控制的扩展，提供了基于生物特征和锁屏密码二次身份认证的细粒度访问控制能力，允许设置密钥在加密、解密、签名、验签、密钥协商、密钥派生的单个或多个场景时是否需要进行身份验证。

比如，业务需要使用HUKS密钥加密保存账号密码信息等数据，要求在加密的时候不进行指纹等身份认证，解密的时候需要进行指纹等身份认证，这时就需要依赖HUKS提供细粒度的二次身份认证访问控制机制。

使用该功能仅需在密钥生成阶段，通过额外指定用于细粒度用户身份认证访问控制的HuksTag：HUKS\_TAG\_KEY\_AUTH\_PURPOSE，来指定在某种算法用途的情况下需要使用用户身份认证访问控制能力。

说明

对于对称加解密场景，仅AES/CBC、AES/GCM、SM4/CBC模式支持细粒度访问控制。

## 开发步骤

### 密钥生成和数据加密

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { userAuth } from '@kit.UserAuthenticationKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const KEY_ALIAS = 'test_sm4_key_alias';
6. const CIPHER_IN_DATA = 'Hks_SM4_Cipher_Test_101010101010101010110_string'; // 明文数据
7. const IV = '1234567890123456'; // 初始化向量
8. const AUTH_TYPE = userAuth.UserAuthType.PIN; // 认证类型：PIN码
9. const AUTH_TRUST_LEVEL = userAuth.AuthTrustLevel.ATL1; // 认证信任级别

11. let sessionHandle = 0; // 会话句柄
12. let challenge: Uint8Array; // 挑战值
13. let authToken: Uint8Array; // 认证令牌
14. let encryptedData: Uint8Array; // 加密后的密文
15. let decryptedData: Uint8Array; // 解密后的明文

17. class ThrowObject {
18. public isThrow: boolean = false;
19. }

21. function stringToUint8Array(str: string): Uint8Array {
22. let arr: number[] = [];
23. for (let i = 0, j = str.length; i < j; ++i) {
24. arr.push(str.charCodeAt(i));
25. }
26. return new Uint8Array(arr);
27. }

29. /* 步骤1：密钥生成模块 */
30. const KEY_GENERATION_PROPERTIES: huks.HuksParam[] = [
31. {
32. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
33. value: huks.HuksKeyAlg.HUKS_ALG_SM4,
34. },
35. {
36. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
38. },
39. {
40. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
41. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
42. },
43. {
44. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
45. value: huks.HuksCipherMode.HUKS_MODE_CBC,
46. },
47. {
48. tag: huks.HuksTag.HUKS_TAG_PADDING,
49. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
50. },
51. {
52. tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
53. value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_PIN
54. },
55. {
56. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
57. value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD
58. },
59. {
60. tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
61. value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
62. },
63. {
64. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
65. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
66. }
67. ];

69. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject): Promise<void> {
70. return new Promise<void>((resolve, reject) => {
71. try {
72. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
73. if (error) {
74. reject(error);
75. } else {
76. resolve(data);
77. }
78. });
79. } catch (error) {
80. throwObject.isThrow = true;
81. const err = error instanceof Error ? error : new Error(String(error));
82. throw err;
83. }
84. });
85. }

87. /* 生成SM4密钥 */
88. async function step1GenerateKey(): Promise<void> {
89. const generateOptions: huks.HuksOptions = {
90. properties: KEY_GENERATION_PROPERTIES,
91. inData: new Uint8Array([])
92. };

94. let throwObject: ThrowObject = { isThrow: true };
95. try {
96. await generateKeyItem(KEY_ALIAS, generateOptions, throwObject)
97. .then((data) => {
98. console.info(`密钥生成成功: ${JSON.stringify(data)}`);
99. })
100. .catch((error: Error) => {
101. if (throwObject.isThrow) {
102. const err = error instanceof Error ? error : new Error(String(error));
103. throw err;
104. } else {
105. console.error(`密钥生成失败: ${JSON.stringify(error)}`);
106. }
107. });
108. } catch (error) {
109. console.error(`密钥生成参数无效: ${JSON.stringify(error)}`);
110. const err = error instanceof Error ? error : new Error(String(error));
111. throw err;
112. }
113. }

115. /* 步骤2：加密模块 */
116. const ENCRYPTION_PROPERTIES: huks.HuksParam[] = [
117. {
118. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
119. value: huks.HuksKeyAlg.HUKS_ALG_SM4,
120. },
121. {
122. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
123. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT,
124. },
125. {
126. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
127. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
128. },
129. {
130. tag: huks.HuksTag.HUKS_TAG_PADDING,
131. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
132. },
133. {
134. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
135. value: huks.HuksCipherMode.HUKS_MODE_CBC,
136. },
137. {
138. tag: huks.HuksTag.HUKS_TAG_IV,
139. value: stringToUint8Array(IV),
140. }
141. ];

143. function initEncryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
144. throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
145. return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
146. try {
147. huks.initSession(keyAlias, huksOptions, (error, data) => {
148. if (error) {
149. reject(error);
150. } else {
151. resolve(data);
152. }
153. });
154. } catch (error) {
155. throwObject.isThrow = true;
156. const err = error instanceof Error ? error : new Error(String(error));
157. throw err;
158. }
159. });
160. }

162. function finishEncryptSession(handle: number, huksOptions: huks.HuksOptions,
163. throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
164. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
165. try {
166. huks.finishSession(handle, huksOptions, (error, data) => {
167. if (error) {
168. reject(error);
169. } else {
170. resolve(data);
171. }
172. });
173. } catch (error) {
174. throwObject.isThrow = true;
175. const err = error instanceof Error ? error : new Error(String(error));
176. throw err;
177. }
178. });
179. }

181. /* 加密数据 */
182. async function step2EncryptData(): Promise<void> {
183. const encryptOptions: huks.HuksOptions = {
184. properties: ENCRYPTION_PROPERTIES,
185. inData: new Uint8Array([])
186. };

188. /* 初始化加密会话 */
189. let throwObject: ThrowObject = { isThrow: true };
190. try {
191. await initEncryptSession(KEY_ALIAS, encryptOptions, throwObject)
192. .then((data) => {
193. console.info(`加密会话初始化成功: ${JSON.stringify(data)}`);
194. sessionHandle = data.handle as number;
195. challenge = data.challenge as Uint8Array;
196. })
197. .catch((error: Error) => {
198. if (throwObject.isThrow) {
199. const err = error instanceof Error ? error : new Error(String(error));
200. throw err;
201. } else {
202. console.error(`加密会话初始化失败: ${JSON.stringify(error)}`);
203. }
204. });
205. } catch (error) {
206. console.error(`加密会话初始化参数无效: ${JSON.stringify(error)}`);
207. const err = error instanceof Error ? error : new Error(String(error));
208. throw err;
209. }

211. /* 执行加密操作 */
212. encryptOptions.inData = stringToUint8Array(CIPHER_IN_DATA);
213. throwObject = { isThrow: true };
214. try {
215. await finishEncryptSession(sessionHandle, encryptOptions, throwObject)
216. .then((data) => {
217. encryptedData = data.outData as Uint8Array;
218. console.info(`数据加密成功: ${JSON.stringify(data)}`);
219. })
220. .catch((error: Error) => {
221. if (throwObject.isThrow) {
222. const err = error instanceof Error ? error : new Error(String(error));
223. throw err;
224. } else {
225. console.error(`数据加密失败: ${JSON.stringify(error)}`);
226. }
227. });
228. } catch (error) {
229. console.error(`数据加密参数无效: ${JSON.stringify(error)}`);
230. const err = error instanceof Error ? error : new Error(String(error));
231. throw err;
232. }
233. }
```

[FineGrainedUserIdentityAuthentication.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/AccessControl/entry/src/main/ets/pages/FineGrainedUserIdentityAuthentication.ets#L16-L250)

### 用户认证

```
1. /* 步骤3：用户认证模块 */
2. function performUserAuthentication(huksChallenge: Uint8Array): void {
3. /* 配置认证参数 */
4. const authTypeList: userAuth.UserAuthType[] = [AUTH_TYPE];
5. const authParam: userAuth.AuthParam = {
6. challenge: huksChallenge,
7. authType: authTypeList,
8. authTrustLevel: AUTH_TRUST_LEVEL
9. };

11. const widgetParam: userAuth.WidgetParam = {
12. title: 'PIN',
13. };

15. /* 获取认证实例 */
16. let auth: userAuth.UserAuthInstance;
17. try {
18. auth = userAuth.getUserAuthInstance(authParam, widgetParam);
19. console.info('认证实例获取成功');
20. } catch (error) {
21. console.error('认证实例获取失败: ' + JSON.stringify(error));
22. const err = error instanceof Error ? error : new Error(String(error));
23. throw err;
24. }

26. /* 订阅认证结果 */
27. try {
28. auth.on('result', {
29. onResult(result) {
30. console.info('用户认证成功，获取到token: ' + JSON.stringify(result));
31. authToken = result.token;
32. step32CompleteDecryption();
33. }
34. });
35. console.info('认证结果订阅成功');
36. } catch (error) {
37. console.error('认证结果订阅失败: ' + JSON.stringify(error));
38. const err = error instanceof Error ? error : new Error(String(error));
39. throw err;
40. }

42. try {
43. auth.start();
44. console.info('认证流程已启动，等待用户输入PIN码...');
45. } catch (error) {
46. console.error('认证启动失败: ' + JSON.stringify(error));
47. const err = error instanceof Error ? error : new Error(String(error));
48. throw err;
49. }
50. }
```

[FineGrainedUserIdentityAuthentication.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/AccessControl/entry/src/main/ets/pages/FineGrainedUserIdentityAuthentication.ets#L252-L303)

### 数据解密和验证

```
1. /* 步骤4：解密模块 */
2. const DECRYPTION_PROPERTIES: huks.HuksParam[] = [
3. {
4. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
5. value: huks.HuksKeyAlg.HUKS_ALG_SM4,
6. },
7. {
8. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
9. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT,
10. },
11. {
12. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
13. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
14. },
15. {
16. tag: huks.HuksTag.HUKS_TAG_PADDING,
17. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
18. },
19. {
20. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
21. value: huks.HuksCipherMode.HUKS_MODE_CBC,
22. },
23. {
24. tag: huks.HuksTag.HUKS_TAG_IV,
25. value: stringToUint8Array(IV),
26. }
27. ];

29. function initDecryptSession(keyAlias: string, huksOptions: huks.HuksOptions,
30. throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
31. return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
32. try {
33. huks.initSession(keyAlias, huksOptions, (error, data) => {
34. if (error) {
35. reject(error);
36. } else {
37. resolve(data);
38. }
39. });
40. } catch (error) {
41. throwObject.isThrow = true;
42. const err = error instanceof Error ? error : new Error(String(error));
43. throw err;
44. }
45. });
46. }

48. function finishDecryptSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
49. throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
50. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
51. try {
52. huks.finishSession(handle, huksOptions, token, (error, data) => {
53. if (error) {
54. reject(error);
55. } else {
56. resolve(data);
57. }
58. });
59. } catch (error) {
60. throwObject.isThrow = true;
61. const err = error instanceof Error ? error : new Error(String(error));
62. throw err;
63. }
64. });
65. }

67. /* 初始化解密会话并触发用户认证 */
68. async function step31DecryptionAndAuth(): Promise<void> {

70. const decryptOptions: huks.HuksOptions = {
71. properties: DECRYPTION_PROPERTIES,
72. inData: new Uint8Array([])
73. };

75. /* 初始化解密会话，获取挑战值 */
76. let throwObject: ThrowObject = { isThrow: true };
77. try {
78. await initDecryptSession(KEY_ALIAS, decryptOptions, throwObject)
79. .then((data) => {
80. console.info(`解密会话初始化成功: ${JSON.stringify(data)}`);
81. sessionHandle = data.handle as number;
82. challenge = data.challenge as Uint8Array;
83. console.info('获取到挑战值: ' + challenge.toString());

85. /* 触发用户认证流程 */
86. performUserAuthentication(challenge);
87. })
88. .catch((error: Error) => {
89. if (throwObject.isThrow) {
90. const err = error instanceof Error ? error : new Error(String(error));
91. throw err;
92. } else {
93. console.error(`解密会话初始化失败: ${JSON.stringify(error)}`);
94. }
95. });
96. } catch (error) {
97. console.error(`解密会话初始化参数无效: ${JSON.stringify(error)}`);
98. const err = error instanceof Error ? error : new Error(String(error));
99. throw err;
100. }
101. }

103. /* 完成解密操作 */
104. async function step32CompleteDecryption(): Promise<void> {
105. const decryptOptions: huks.HuksOptions = {
106. properties: DECRYPTION_PROPERTIES,
107. inData: encryptedData // 使用之前加密的密文
108. };

110. let throwObject: ThrowObject = { isThrow: true };
111. try {
112. await finishDecryptSession(sessionHandle, decryptOptions, authToken, throwObject)
113. .then((data) => {
114. decryptedData = data.outData as Uint8Array;
115. console.info(`数据解密成功: ${JSON.stringify(data)}`);

117. /* 验证解密结果 */
118. const originalData = stringToUint8Array(CIPHER_IN_DATA);
119. if (decryptedData.toString() === originalData.toString()) {
120. console.info('解密验证成功！解密后的数据与原始明文一致');
121. } else {
122. console.error('解密验证失败！解密后的数据与原始明文不一致');
123. }
124. })
125. .catch((error: BusinessError) => {
126. if (throwObject.isThrow) {
127. const err = error instanceof Error ? error : new Error(String(error));
128. throw err;
129. } else {
130. console.error(`数据解密失败: ${JSON.stringify(error)}`);
131. }
132. });
133. } catch (error) {
134. console.error(`数据解密参数无效: ${JSON.stringify(error)}`);
135. const err = error instanceof Error ? error : new Error(String(error));
136. throw err;
137. }
138. }

140. /* 主函数：执行完整的SM4加密解密流程 */
141. async function main(): Promise<void> {
142. /* 步骤1：生成密钥 */
143. await step1GenerateKey();
144. /* 步骤2：加密数据 */
145. await step2EncryptData();
146. /* 步骤3：初始化解密并进行用户认证 */
147. await step31DecryptionAndAuth();
148. }
```

[FineGrainedUserIdentityAuthentication.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/AccessControl/entry/src/main/ets/pages/FineGrainedUserIdentityAuthentication.ets#L305-L454)
