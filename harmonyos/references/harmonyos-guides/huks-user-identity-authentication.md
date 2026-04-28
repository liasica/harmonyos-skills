---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-user-identity-authentication
title: 用户身份认证访问控制开发指导
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 访问控制 > 用户身份认证访问控制开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7476bd0f0d9a758c8a70468709068e3a4bf0f0ca5ad44cbb086cfedbdbf3993f
---

场景介绍及相关概念说明请参考[用户身份认证访问控制简介](huks-identity-authentication-overview.md)。

## 开发步骤

### 生成密钥

指定指纹访问控制类型及相关属性。

生成或导入密钥时，在密钥属性集中需指定三个参数：用户认证类型[HuksUserAuthType](../harmonyos-references/js-apis-huks.md#huksuserauthtype9)、授权访问类型[HuksAuthAccessType](../harmonyos-references/js-apis-huks.md#huksauthaccesstype9)、挑战值类型[HuksChallengeType](../harmonyos-references/js-apis-huks.md#hukschallengetype9)。

## 开发案例

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { userAuth } from '@kit.UserAuthenticationKit';

4. const KEY_ALIAS = 'test_sm4_key_alias';
5. const IV = '1234567890123456';
6. const CIPHER_IN_DATA = 'Hks_SM4_Cipher_Test_101010101010101010110_string';
7. const AUTH_TYPE = userAuth.UserAuthType.PIN;
8. const AUTH_TRUST_LEVEL = userAuth.AuthTrustLevel.ATL1;

10. let sessionHandle: number;
11. let challenge: Uint8Array;
12. let authToken: Uint8Array;
13. let encryptedData: Uint8Array;

15. class ThrowObject {
16. public isThrow: boolean = false;
17. }

19. function stringToUint8Array(str: string): Uint8Array {
20. let arr: number[] = [];
21. for (let i = 0, j = str.length; i < j; ++i) {
22. arr.push(str.charCodeAt(i));
23. }
24. return new Uint8Array(arr);
25. }

27. /* 步骤1：密钥生成模块 */
28. const KEY_GENERATION_PROPERTIES: huks.HuksParam[] = [
29. {
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_SM4
32. },
33. {
34. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
35. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
36. },
37. {
38. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
39. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
40. },
41. {
42. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
43. value: huks.HuksCipherMode.HUKS_MODE_CBC,
44. },
45. {
46. tag: huks.HuksTag.HUKS_TAG_PADDING,
47. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
48. },
49. {
50. tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
51. value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_PIN
52. },
53. {
54. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
55. value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_INVALID_CLEAR_PASSWORD
56. },
57. {
58. tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
59. value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
60. }
61. ];

63. /* 生成密钥 */
64. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject): Promise<void> {
65. return new Promise<void>((resolve, reject) => {
66. try {
67. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
68. if (error) {
69. reject(error);
70. } else {
71. resolve(data);
72. }
73. });
74. } catch (error) {
75. throwObject.isThrow = true;
76. const err = error instanceof Error ? error : new Error(String(error));
77. throw err;
78. }
79. });
80. }

82. /* 生成SM4密钥 */
83. async function step1GenerateKey(): Promise<void> {
84. const generateOptions: huks.HuksOptions = {
85. properties: KEY_GENERATION_PROPERTIES,
86. inData: new Uint8Array([])
87. };

89. let throwObject: ThrowObject = { isThrow: true };
90. try {
91. await generateKeyItem(KEY_ALIAS, generateOptions, throwObject)
92. .then((data) => {
93. console.info('密钥生成成功');
94. })
95. .catch((error: Error) => {
96. if (throwObject.isThrow) {
97. const err = error instanceof Error ? error : new Error(String(error));
98. throw err;
99. } else {
100. console.error('密钥生成失败: ' + JSON.stringify(error));
101. }
102. });
103. } catch (error) {
104. console.error('密钥生成参数错误: ' + JSON.stringify(error));
105. const err = error instanceof Error ? error : new Error(String(error));
106. throw err;
107. }
108. }

110. /* 步骤2：初始化会话模块 - 初始化加密会话并获取挑战值 */
111. const INIT_SESSION_PROPERTIES: huks.HuksParam[] = [
112. {
113. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
114. value: huks.HuksKeyAlg.HUKS_ALG_SM4,
115. },
116. {
117. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
118. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT,
119. },
120. {
121. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
122. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
123. },
124. {
125. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
126. value: huks.HuksCipherMode.HUKS_MODE_CBC,
127. },
128. {
129. tag: huks.HuksTag.HUKS_TAG_PADDING,
130. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
131. },
132. {
133. tag: huks.HuksTag.HUKS_TAG_IV,
134. value: stringToUint8Array(IV),
135. }
136. ];

138. /* 初始化会话 */
139. function initSession(keyAlias: string, huksOptions: huks.HuksOptions,
140. throwObject: ThrowObject): Promise<huks.HuksSessionHandle> {
141. return new Promise<huks.HuksSessionHandle>((resolve, reject) => {
142. try {
143. huks.initSession(keyAlias, huksOptions, (error, data) => {
144. if (error) {
145. reject(error);
146. } else {
147. resolve(data);
148. }
149. });
150. } catch (error) {
151. throwObject.isThrow = true;
152. const err = error instanceof Error ? error : new Error(String(error));
153. throw err;
154. }
155. });
156. }

158. /* 初始化会话并获取挑战值 */
159. async function step2InitSession(): Promise<void> {
160. const initOptions: huks.HuksOptions = {
161. properties: INIT_SESSION_PROPERTIES,
162. inData: new Uint8Array([])
163. };

165. let throwObject: ThrowObject = { isThrow: true };
166. try {
167. await initSession(KEY_ALIAS, initOptions, throwObject)
168. .then((data) => {
169. sessionHandle = data.handle;
170. challenge = data.challenge as Uint8Array;
171. console.info('会话初始化成功，挑战值: ' + challenge.toString());
172. })
173. .catch((error: Error) => {
174. if (throwObject.isThrow) {
175. const err = error instanceof Error ? error : new Error(String(error));
176. throw err;
177. } else {
178. console.error('会话初始化失败: ' + JSON.stringify(error));
179. }
180. });
181. } catch (error) {
182. console.error('会话初始化参数错误: ' + JSON.stringify(error));
183. const err = error instanceof Error ? error : new Error(String(error));
184. throw err;
185. }
186. }
```

### 通过PIN码认证获取授权令牌

```
1. /* 步骤3：用户认证模块 - 通过PIN码认证获取授权令牌 */
2. /* 执行用户认证 */
3. function performUserAuthentication(huksChallenge: Uint8Array): void {
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
19. console.info('认证实例创建成功');
20. } catch (error) {
21. console.error('认证实例创建失败: ' + JSON.stringify(error));
22. const err = error instanceof Error ? error : new Error(String(error));
23. throw err;
24. }

26. /* 订阅认证结果 */
27. try {
28. auth.on('result', {
29. onResult(result) {
30. console.info('用户认证成功，获取到令牌');
31. authToken = result.token;
32. step4EncryptWithToken();
33. }
34. });
35. console.info('认证结果订阅成功');
36. } catch (error) {
37. console.error('认证结果订阅失败: ' + JSON.stringify(error));
38. const err = error instanceof Error ? error : new Error(String(error));
39. throw err;
40. }

42. /* 开始认证 */
43. try {
44. auth.start();
45. console.info('等待用户输入PIN码');
46. } catch (error) {
47. console.error('认证启动失败: ' + JSON.stringify(error));
48. const err = error instanceof Error ? error : new Error(String(error));
49. throw err;
50. }
51. }
```

[UserIdentityAuthentication.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/AccessControl/entry/src/main/ets/pages/UserIdentityAuthentication.ets#L205-L257)

### 使用认证令牌进行加密操作

```
1. /* 步骤4：加密操作模块 - 使用认证令牌进行加密操作 */
2. /* 加密参数配置 */
3. const ENCRYPT_PROPERTIES: huks.HuksParam[] = [
4. {
5. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
6. value: huks.HuksKeyAlg.HUKS_ALG_SM4,
7. },
8. {
9. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
10. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT,
11. },
12. {
13. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
14. value: huks.HuksKeySize.HUKS_SM4_KEY_SIZE_128,
15. },
16. {
17. tag: huks.HuksTag.HUKS_TAG_PADDING,
18. value: huks.HuksKeyPadding.HUKS_PADDING_NONE,
19. },
20. {
21. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
22. value: huks.HuksCipherMode.HUKS_MODE_CBC,
23. },
24. {
25. tag: huks.HuksTag.HUKS_TAG_IV,
26. value: stringToUint8Array(IV),
27. }
28. ];

30. /* 更新会话 */
31. function updateSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
32. throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
33. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
34. try {
35. huks.updateSession(handle, huksOptions, token, (error, data) => {
36. if (error) {
37. reject(error);
38. } else {
39. resolve(data);
40. }
41. });
42. } catch (error) {
43. throwObject.isThrow = true;
44. const err = error instanceof Error ? error : new Error(String(error));
45. throw err;
46. }
47. });
48. }

50. /* 完成会话 */
51. function finishSession(handle: number, huksOptions: huks.HuksOptions, token: Uint8Array,
52. throwObject: ThrowObject): Promise<huks.HuksReturnResult> {
53. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
54. try {
55. huks.finishSession(handle, huksOptions, token, (error, data) => {
56. if (error) {
57. reject(error);
58. } else {
59. resolve(data);
60. }
61. });
62. } catch (error) {
63. throwObject.isThrow = true;
64. const err = error instanceof Error ? error : new Error(String(error));
65. throw err;
66. }
67. });
68. }

70. /* 使用认证令牌进行加密 */
71. async function step4EncryptWithToken(): Promise<void> {
72. const encryptOptions: huks.HuksOptions = {
73. properties: ENCRYPT_PROPERTIES,
74. inData: stringToUint8Array(CIPHER_IN_DATA)
75. };

77. /* 更新会话，传入认证令牌 */
78. let throwObject: ThrowObject = { isThrow: true };
79. try {
80. await updateSession(sessionHandle, encryptOptions, authToken, throwObject)
81. .then((data) => {
82. console.info('会话更新成功');
83. })
84. .catch((error: Error) => {
85. if (throwObject.isThrow) {
86. const err = error instanceof Error ? error : new Error(String(error));
87. throw err;
88. } else {
89. console.error('会话更新失败: ' + JSON.stringify(error));
90. }
91. });
92. } catch (error) {
93. console.error('会话更新参数错误: ' + JSON.stringify(error));
94. const err = error instanceof Error ? error : new Error(String(error));
95. throw err;
96. }

98. /* 完成会话，传入认证令牌 */
99. throwObject = { isThrow: false };
100. try {
101. await finishSession(sessionHandle, encryptOptions, authToken, throwObject)
102. .then((data) => {
103. encryptedData = data.outData as Uint8Array;
104. console.info('加密完成');

106. /* 验证加密结果 */
107. const originalData = stringToUint8Array(CIPHER_IN_DATA);
108. if (encryptedData.toString() === originalData.toString()) {
109. console.error('加密验证失败：加密数据与原始数据相同');
110. } else {
111. console.info('加密验证成功：数据已正确加密');
112. }
113. })
114. .catch((error: Error) => {
115. if (throwObject.isThrow) {
116. const err = error instanceof Error ? error : new Error(String(error));
117. throw err;
118. } else {
119. console.error('会话完成失败: ' + JSON.stringify(error));
120. }
121. });
122. } catch (error) {
123. console.error('会话完成参数错误: ' + JSON.stringify(error));
124. const err = error instanceof Error ? error : new Error(String(error));
125. throw err;
126. }
127. }

129. /* 主流程入口 - 执行完整的密钥生成、认证和加密流程 */
130. async function main(): Promise<void> {
131. await step1GenerateKey();
132. await step2InitSession();
133. performUserAuthentication(challenge);
134. }
```

[UserIdentityAuthentication.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/AccessControl/entry/src/main/ets/pages/UserIdentityAuthentication.ets#L259-L394)
