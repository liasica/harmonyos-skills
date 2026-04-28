---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-encryption-decryption-arkts
title: 加解密(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 加密/解密 > 加解密(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:329af2ac483813b3865c7fee82a0cbe9159d7b5da54ae00bfabb0396c3be3b85
---

以AES128、RSA2048、SM2和DES64为例，完成加解密。具体的场景介绍及支持的算法规格，请参考[加解密支持的算法](huks-encryption-decryption-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**加密**

1. 获取密钥别名。
2. 获取待加密的数据。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置加密算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法加密，选取的分组模式为CBC、填充模式为PKCS7时，参数IV必选，请见开发案例：[AES/CBC/PKCS7](huks-encryption-decryption-arkts.md#aescbcpkcs7)。
   * 使用AES算法加密，选取的分组模式为GCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-arkts.md#aesgcmnopadding)。
   * 使用AES算法加密，选取的分组模式为CCM时，参数NONCE可选，AAD可选，请见开发案例：[AES/CCM/NoPadding](huks-encryption-decryption-arkts.md#aesccmnopadding)。
   * 使用RSA算法加密，需要选择相对应的分组模式、填充模式以及摘要算法DIGEST，请见开发案例：[RSA/ECB/PKCS1\_V1\_5](huks-encryption-decryption-arkts.md#rsaecbpkcs1_v1_5)和[RSA/ECB/OAEP/SHA256](huks-encryption-decryption-arkts.md#rsaecboaepsha256)。
   * 使用SM2算法加密，摘要算法DIGEST需要指定为SM3，请见开发案例：[SM2](huks-encryption-decryption-arkts.md#sm2)。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取加密后的密文。

**解密**

1. 获取密钥别名。
2. 获取待解密的密文。
3. 使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置解密算法参数配置。

   文档中提供多个示例，当使用不同算法时，请注意配置对应参数。

   * 使用AES算法解密，用例中选取的分组模式为GCM时，必须要填参数NONCE和参数AEAD，AAD可选，请见开发案例：[AES/GCM/NoPadding](huks-encryption-decryption-arkts.md#aesgcmnopadding)。
   * 其余示例参数与加密要求一致。

   详细规格请参考[加密/解密介绍及算法规格](huks-encryption-decryption-overview.md)。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取解密后的数据。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

### AES/CBC/PKCS7

```
1. /*
2. * 以下以AES/CBC/PKCS7的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
6. import { BusinessError } from '@kit.BasicServicesKit';

8. let aesKeyAlias = 'test_aesKeyAlias';
9. let handle: number;
10. let plainText = '123456';
11. let IV = cryptoFramework.createRandom().generateRandomSync(12).data;
12. let cipherData: Uint8Array;

14. function stringToUint8Array(str: string) {
15. let arr: number[] = [];
16. for (let i = 0, j = str.length; i < j; ++i) {
17. arr.push(str.charCodeAt(i));
18. }
19. return new Uint8Array(arr);
20. }

22. function uint8ArrayToString(fileData: Uint8Array) {
23. let dataString = '';
24. for (let i = 0; i < fileData.length; i++) {
25. dataString += String.fromCharCode(fileData[i]);
26. }
27. return dataString;
28. }

30. function getAesGenerateProperties() {
31. let properties: huks.HuksParam[] = [{
32. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
33. value: huks.HuksKeyAlg.HUKS_ALG_AES
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
36. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
37. }, {
38. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
39. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
40. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
41. }];
42. return properties;
43. }

45. function getAesEncryptProperties() {
46. let properties: huks.HuksParam[] = [{
47. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
48. value: huks.HuksKeyAlg.HUKS_ALG_AES
49. }, {
50. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
51. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
54. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_PADDING,
57. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
60. value: huks.HuksCipherMode.HUKS_MODE_CBC
61. }, {
62. tag: huks.HuksTag.HUKS_TAG_IV,
63. value: IV
64. }];
65. return properties;
66. }

68. function getAesDecryptProperties() {
69. let properties: huks.HuksParam[] = [{
70. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
71. value: huks.HuksKeyAlg.HUKS_ALG_AES
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
74. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
77. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
78. }, {
79. tag: huks.HuksTag.HUKS_TAG_PADDING,
80. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS7
81. }, {
82. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
83. value: huks.HuksCipherMode.HUKS_MODE_CBC
84. }, {
85. tag: huks.HuksTag.HUKS_TAG_IV,
86. value: IV
87. }];
88. return properties;
89. }

91. async function generateAesKey() {
92. /*
93. * 模拟生成密钥场景
94. */
95. /*
96. * 1. 获取生成密钥算法参数配置
97. */
98. let genProperties = getAesGenerateProperties();
99. let options: huks.HuksOptions = {
100. properties: genProperties
101. }
102. /*
103. * 2. 调用generateKeyItem
104. */
105. await huks.generateKeyItem(aesKeyAlias, options)
106. .then(() => {
107. console.info(`promise: generate AES Key success`);
108. }).catch((error: BusinessError) => {
109. console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
110. })
111. }

113. async function encryptData() {
114. /*
115. * 模拟加密场景
116. */
117. /*
118. * 1. 获取加密算法参数配置
119. */
120. let encryptProperties = getAesEncryptProperties();
121. let options: huks.HuksOptions = {
122. properties: encryptProperties,
123. inData: stringToUint8Array(plainText)
124. }
125. /*
126. * 2. 调用initSession获取handle
127. */
128. await huks.initSession(aesKeyAlias, options)
129. .then((data) => {
130. handle = data.handle;
131. }).catch((error: BusinessError) => {
132. console.error(`promise: init EncryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
133. })
134. /*
135. * 3. 调用finishSession获取加密后的密文
136. */
137. await huks.finishSession(handle, options)
138. .then((data) => {
139. console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
140. cipherData = data.outData as Uint8Array;
141. }).catch((error: BusinessError) => {
142. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
143. })
144. }

146. async function decryptData() {
147. /*
148. * 模拟解密场景
149. * 1. 获取密钥别名
150. */
151. /*
152. * 1. 获取解密算法参数配置
153. */
154. let decryptOptions = getAesDecryptProperties()
155. let options: huks.HuksOptions = {
156. properties: decryptOptions,
157. inData: cipherData
158. }
159. /*
160. * 2. 调用initSession获取handle
161. */
162. await huks.initSession(aesKeyAlias, options)
163. .then((data) => {
164. handle = data.handle;
165. }).catch((error: BusinessError) => {
166. console.error(`promise: init DecryptData failed, errCode : ${error.code}, errMsg : ${error.message}`);
167. })
168. /*
169. * 3. 调用finishSession获取解密后的数据
170. */
171. await huks.finishSession(handle, options)
172. .then((data) => {
173. console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
174. }).catch((error: BusinessError) => {
175. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
176. })
177. }

179. async function deleteKey() {
180. /*
181. * 模拟删除密钥场景
182. */
183. let emptyOptions: huks.HuksOptions = {
184. properties: []
185. }
186. /*
187. * 1. 调用deleteKeyItem删除密钥
188. */
189. await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
190. .then(() => {
191. console.info(`promise: delete data success`);
192. }).catch((error: BusinessError) => {
193. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
194. })
195. }
```

[AESCBCPKCS7.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/ets/pages/AESCBCPKCS7.ets#L15-L211)

### AES/GCM/NoPadding

```
1. /*
2. * 以下以AES/GCM/NoPadding的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
6. import { BusinessError } from '@kit.BasicServicesKit';

8. let aesKeyAlias = 'test_aesKeyAlias';
9. let handle: number;
10. let plainText = '123456';
11. let cipherData: Uint8Array;
12. let AAD = '1234567890123456';
13. let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;

15. function stringToUint8Array(str: string) {
16. let arr: number[] = [];
17. for (let i = 0, j = str.length; i < j; ++i) {
18. arr.push(str.charCodeAt(i));
19. }
20. return new Uint8Array(arr);
21. }

23. function uint8ArrayToString(fileData: Uint8Array) {
24. let dataString = '';
25. for (let i = 0; i < fileData.length; i++) {
26. dataString += String.fromCharCode(fileData[i]);
27. }
28. return dataString;
29. }

31. function getAesGenerateProperties() {
32. let properties: huks.HuksParam[] = [{
33. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
34. value: huks.HuksKeyAlg.HUKS_ALG_AES
35. }, {
36. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
37. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
40. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
41. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
42. }];
43. return properties;
44. }

46. function getAesGcmEncryptProperties() {
47. let properties: huks.HuksParam[] = [{
48. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
49. value: huks.HuksKeyAlg.HUKS_ALG_AES
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
52. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
55. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
56. }, {
57. tag: huks.HuksTag.HUKS_TAG_PADDING,
58. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
59. }, {
60. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
61. value: huks.HuksCipherMode.HUKS_MODE_GCM
62. }, {
63. tag: huks.HuksTag.HUKS_TAG_NONCE,
64. value: NONCE
65. }, {
66. tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
67. value: stringToUint8Array(AAD)
68. }];
69. return properties;
70. }

72. function getAesGcmDecryptProperties(cipherData: Uint8Array) {
73. let properties: huks.HuksParam[] = [{
74. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
75. value: huks.HuksKeyAlg.HUKS_ALG_AES
76. }, {
77. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
78. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
79. }, {
80. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
81. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
82. }, {
83. tag: huks.HuksTag.HUKS_TAG_PADDING,
84. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
85. }, {
86. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
87. value: huks.HuksCipherMode.HUKS_MODE_GCM
88. }, {
89. tag: huks.HuksTag.HUKS_TAG_NONCE,
90. value: NONCE
91. }, {
92. tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
93. value: stringToUint8Array(AAD)
94. }, {
95. tag: huks.HuksTag.HUKS_TAG_AE_TAG,
96. value: cipherData.slice(cipherData.length - 16)
97. }];
98. return properties;
99. }

101. async function generateAesKey() {
102. /*
103. * 模拟生成密钥场景
104. */
105. /*
106. * 1. 获取生成密钥算法参数配置
107. */
108. let genProperties = getAesGenerateProperties();
109. let options: huks.HuksOptions = {
110. properties: genProperties
111. }
112. /*
113. * 2. 调用generateKeyItem
114. */
115. await huks.generateKeyItem(aesKeyAlias, options)
116. .then(() => {
117. console.info(`promise: generate AES Key success`);
118. }).catch((error: BusinessError) => {
119. console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
120. })
121. }

123. async function encryptData() {
124. /*
125. * 模拟加密场景
126. */
127. /*
128. * 1. 获取加密算法参数配置
129. */
130. let encryptProperties = getAesGcmEncryptProperties();
131. let options: huks.HuksOptions = {
132. properties: encryptProperties,
133. inData: stringToUint8Array(plainText)
134. }
135. /*
136. * 2. 调用initSession获取handle
137. */
138. await huks.initSession(aesKeyAlias, options)
139. .then((data) => {
140. handle = data.handle;
141. }).catch((error: BusinessError) => {
142. console.error(`promise: init EncryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
143. })
144. /*
145. * 3. 调用finishSession获取加密后的密文
146. */
147. await huks.finishSession(handle, options)
148. .then((data) => {
149. console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
150. cipherData = data.outData as Uint8Array;
151. }).catch((error: BusinessError) => {
152. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
153. })
154. }

156. async function decryptData() {
157. /*
158. * 模拟解密场景
159. */
160. /*
161. * 1. 获取解密算法参数配置
162. */
163. let decryptOptions = getAesGcmDecryptProperties(cipherData)
164. let options: huks.HuksOptions = {
165. properties: decryptOptions,
166. inData: cipherData.slice(0, cipherData.length - 16)
167. }
168. /*
169. * 2. 调用initSession获取handle
170. */
171. await huks.initSession(aesKeyAlias, options)
172. .then((data) => {
173. handle = data.handle;
174. }).catch((error: BusinessError) => {
175. console.error(`promise: init DecryptDataGcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
176. })
177. /*
178. * 3. 调用finishSession获取解密后的数据
179. */
180. await huks.finishSession(handle, options)
181. .then((data) => {
182. console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
183. }).catch((error: BusinessError) => {
184. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
185. })
186. }

188. async function deleteKey() {
189. /*
190. * 模拟删除密钥场景
191. */
192. let emptyOptions: huks.HuksOptions = {
193. properties: []
194. }
195. /*
196. * 1. 调用deleteKeyItem删除密钥
197. */
198. await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
199. .then(() => {
200. console.info(`promise: delete data success`);
201. }).catch((error: BusinessError) => {
202. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
203. })
204. }
```

[AESGCMNoPadding.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/ets/pages/AESGCMNoPadding.ets#L15-L221)

### AES/CCM/NoPadding

```
1. /*
2. * 以下以AES/CCM/NoPadding的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
6. import { BusinessError } from "@kit.BasicServicesKit";

8. let aesKeyAlias = 'test_aesCcmKeyAlias';
9. let handle: number;
10. let plainText = '123456';
11. let cipherData: Uint8Array;
12. let AAD = '1234567890123456';
13. let NONCE = cryptoFramework.createRandom().generateRandomSync(12).data;
14. let aeadTagLen = 14;

16. function StringToUint8Array(str: string) {
17. let arr: number[] = new Array();
18. for (let i = 0, j = str.length; i < j; ++i) {
19. arr.push(str.charCodeAt(i));
20. }
21. return new Uint8Array(arr);
22. }

24. function Uint8ArrayToString(fileData: Uint8Array) {
25. let dataString = '';
26. for (let i = 0; i < fileData.length; i++) {
27. dataString += String.fromCharCode(fileData[i]);
28. }
29. return dataString;
30. }

32. function GetAesGenerateProperties() {
33. let properties: Array<huks.HuksParam> = [{
34. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
35. value: huks.HuksKeyAlg.HUKS_ALG_AES
36. }, {
37. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
38. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
39. }, {
40. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
41. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
42. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
43. }];
44. return properties;
45. }

47. function GetAesCcmEncryptProperties() {
48. let properties: Array<huks.HuksParam> = [{
49. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
50. value: huks.HuksKeyAlg.HUKS_ALG_AES
51. }, {
52. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
53. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
54. }, {
55. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
56. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
57. }, {
58. tag: huks.HuksTag.HUKS_TAG_PADDING,
59. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
60. }, {
61. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
62. value: huks.HuksCipherMode.HUKS_MODE_CCM
63. }, {
64. tag: huks.HuksTag.HUKS_TAG_NONCE,
65. value: NONCE
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
68. value: StringToUint8Array(AAD)
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_AE_TAG_LEN,
71. value: aeadTagLen
72. }];
73. return properties;
74. }

76. function GetAesCcmDecryptProperties(cipherData: Uint8Array) {
77. let properties: Array<huks.HuksParam> = [{
78. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
79. value: huks.HuksKeyAlg.HUKS_ALG_AES
80. }, {
81. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
82. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_128
83. }, {
84. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
85. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
86. }, {
87. tag: huks.HuksTag.HUKS_TAG_PADDING,
88. value: huks.HuksKeyPadding.HUKS_PADDING_NONE
89. }, {
90. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
91. value: huks.HuksCipherMode.HUKS_MODE_CCM
92. }, {
93. tag: huks.HuksTag.HUKS_TAG_NONCE,
94. value: NONCE
95. }, {
96. tag: huks.HuksTag.HUKS_TAG_ASSOCIATED_DATA,
97. value: StringToUint8Array(AAD)
98. }, {
99. tag: huks.HuksTag.HUKS_TAG_AE_TAG,
100. value: cipherData.slice(cipherData.length - aeadTagLen)
101. }, {
102. tag: huks.HuksTag.HUKS_TAG_AE_TAG_LEN,
103. value: aeadTagLen
104. }];
105. return properties;
106. }

108. async function GenerateAesKey() {
109. /*
110. * 模拟生成密钥场景
111. * 1. 确定密钥别名
112. */
113. /*
114. * 2. 获取生成密钥算法参数配置
115. */
116. let genProperties = GetAesGenerateProperties();
117. let options: huks.HuksOptions = {
118. properties: genProperties
119. }
120. /*
121. * 3. 调用generateKeyItem
122. */
123. await huks.generateKeyItem(aesKeyAlias, options)
124. .then(() => {
125. console.info(`promise: generate AES Key success`);
126. }).catch((error: BusinessError) => {
127. console.error(`promise: generate AES Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
128. })
129. }

131. async function EncryptData() {
132. /*
133. * 模拟加密场景
134. * 1. 获取密钥别名
135. */
136. /*
137. * 2. 获取待加密的数据
138. */
139. /*
140. * 3. 获取加密算法参数配置
141. */
142. let encryptProperties = GetAesCcmEncryptProperties();
143. let options: huks.HuksOptions = {
144. properties: encryptProperties,
145. inData: StringToUint8Array(plainText)
146. }
147. /*
148. * 4. 调用initSession获取handle
149. */
150. await huks.initSession(aesKeyAlias, options)
151. .then((data) => {
152. handle = data.handle;
153. }).catch((error: BusinessError) => {
154. console.error(`promise: init EncryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
155. })
156. /*
157. * 5. 调用finishSession获取加密后的密文
158. */
159. await huks.finishSession(handle, options)
160. .then((data) => {
161. console.info(`promise: encrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
162. cipherData = data.outData as Uint8Array;
163. }).catch((error: BusinessError) => {
164. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
165. })
166. }

168. async function DecryptData() {
169. /*
170. * 模拟解密场景
171. * 1. 获取密钥别名
172. */
173. /*
174. * 2. 获取待解密的密文
175. */
176. /*
177. * 3. 获取解密算法参数配置
178. */
179. let decryptOptions = GetAesCcmDecryptProperties(cipherData)
180. let options: huks.HuksOptions = {
181. properties: decryptOptions,
182. inData: cipherData.slice(0, cipherData.length - aeadTagLen)
183. }
184. /*
185. * 4. 调用initSession获取handle
186. */
187. await huks.initSession(aesKeyAlias, options)
188. .then((data) => {
189. handle = data.handle;
190. }).catch((error: BusinessError) => {
191. console.error(`promise: init DecryptDataCcm failed, errCode : ${error.code}, errMsg : ${error.message}`);
192. })
193. /*
194. * 5. 调用finishSession获取解密后的数据
195. */
196. await huks.finishSession(handle, options)
197. .then((data) => {
198. console.info(`promise: decrypt data success, data is ` + Uint8ArrayToString(data.outData as Uint8Array));
199. }).catch((error: BusinessError) => {
200. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
201. })
202. }

204. async function DeleteKey() {
205. /*
206. * 模拟删除密钥场景
207. * 1. 获取密钥别名
208. */
209. let emptyOptions: huks.HuksOptions = {
210. properties: []
211. }
212. /*
213. * 2. 调用deleteKeyItem删除密钥
214. */
215. await huks.deleteKeyItem(aesKeyAlias, emptyOptions)
216. .then(() => {
217. console.info(`promise: delete data success`);
218. }).catch((error: BusinessError) => {
219. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
220. })
221. }

223. async function TestEncryptDecrypt() {
224. await GenerateAesKey();
225. await EncryptData();
226. await DecryptData();
227. await DeleteKey();
228. }
```

### RSA/ECB/PKCS1\_V1\_5

```
1. /*
2. * 以下以RSA/ECB/PKCS1_V1_5模式的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let rsaKeyAlias = 'test_rsaKeyAlias';
8. let handle: number;
9. let plainText = '123456';
10. let cipherData: Uint8Array;

12. function stringToUint8Array(str: string) {
13. let arr: number[] = [];
14. for (let i = 0, j = str.length; i < j; ++i) {
15. arr.push(str.charCodeAt(i));
16. }
17. return new Uint8Array(arr);
18. }

20. function uint8ArrayToString(fileData: Uint8Array) {
21. let dataString = '';
22. for (let i = 0; i < fileData.length; i++) {
23. dataString += String.fromCharCode(fileData[i]);
24. }
25. return dataString;
26. }

28. function getRsaGenerateProperties() {
29. let properties: huks.HuksParam[] = [{
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_RSA
32. }, {
33. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
34. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
35. }, {
36. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
38. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
39. }];
40. return properties;
41. }

43. function getRsaEncryptProperties() {
44. let properties: huks.HuksParam[] = [{
45. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
46. value: huks.HuksKeyAlg.HUKS_ALG_RSA
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
49. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
52. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_PADDING,
55. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
56. }, {
57. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
58. value: huks.HuksCipherMode.HUKS_MODE_ECB
59. }, {
60. tag: huks.HuksTag.HUKS_TAG_DIGEST,
61. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
62. }];
63. return properties;
64. }

66. function getRsaDecryptProperties() {
67. let properties: huks.HuksParam[] = [{
68. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
69. value: huks.HuksKeyAlg.HUKS_ALG_RSA
70. }, {
71. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
72. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
73. }, {
74. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
75. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
76. }, {
77. tag: huks.HuksTag.HUKS_TAG_PADDING,
78. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
79. }, {
80. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
81. value: huks.HuksCipherMode.HUKS_MODE_ECB
82. }, {
83. tag: huks.HuksTag.HUKS_TAG_DIGEST,
84. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
85. }];
86. return properties;
87. }

89. async function generateRsaKey() {
90. /*
91. * 模拟生成密钥场景
92. */
93. /*
94. * 1. 获取生成密钥算法参数配置
95. */
96. let genProperties = getRsaGenerateProperties();
97. let options: huks.HuksOptions = {
98. properties: genProperties
99. }
100. /*
101. * 2. 调用generateKeyItem
102. */
103. await huks.generateKeyItem(rsaKeyAlias, options)
104. .then(() => {
105. console.info(`promise: generate RSA Key success`);
106. }).catch((error: BusinessError) => {
107. console.error(`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
108. })
109. }

111. async function encryptData() {
112. /*
113. * 模拟加密场景
114. */
115. /*
116. * 1. 获取加密算法参数配置
117. */
118. let encryptProperties = getRsaEncryptProperties();
119. let options: huks.HuksOptions = {
120. properties: encryptProperties,
121. inData: stringToUint8Array(plainText)
122. }
123. /*
124. * 2. 调用initSession获取handle
125. */
126. await huks.initSession(rsaKeyAlias, options)
127. .then((data) => {
128. handle = data.handle;
129. }).catch((error: BusinessError) => {
130. console.error(`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
131. })
132. /*
133. * 3. 调用finishSession获取加密后的密文
134. */
135. await huks.finishSession(handle, options)
136. .then((data) => {
137. console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
138. cipherData = data.outData as Uint8Array;
139. }).catch((error: BusinessError) => {
140. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
141. })
142. }

144. async function decryptData() {
145. /*
146. * 模拟解密场景
147. */
148. /*
149. * 1. 获取解密算法参数配置
150. */
151. let decryptOptions = getRsaDecryptProperties()
152. let options: huks.HuksOptions = {
153. properties: decryptOptions,
154. inData: cipherData
155. }
156. /*
157. * 2. 调用initSession获取handle
158. */
159. await huks.initSession(rsaKeyAlias, options)
160. .then((data) => {
161. handle = data.handle;
162. }).catch((error: BusinessError) => {
163. console.error(`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
164. })
165. /*
166. * 3. 调用finishSession获取解密后的数据
167. */
168. await huks.finishSession(handle, options)
169. .then((data) => {
170. console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
171. }).catch((error: BusinessError) => {
172. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
173. })
174. }

176. async function deleteKey() {
177. /*
178. * 模拟删除密钥场景
179. */
180. let emptyOptions: huks.HuksOptions = {
181. properties: []
182. }
183. /*
184. * 1. 调用deleteKeyItem删除密钥
185. */
186. await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
187. .then(() => {
188. console.info(`promise: delete data success`);
189. }).catch((error: BusinessError) => {
190. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
191. })
192. }
```

[RSAECBPKCS1\_V1\_5.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/ets/pages/RSAECBPKCS1_V1_5.ets#L15-L210)

### RSA/ECB/OAEP/SHA256

```
1. /*
2. * 以下以RSA/ECB/OAEP/SHA256模式的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let rsaKeyAlias = 'test_rsaKeyAlias';
8. let handle: number;
9. let plainText = '123456';
10. let cipherData: Uint8Array;

12. function stringToUint8Array(str: string) {
13. let arr: number[] = [];
14. for (let i = 0, j = str.length; i < j; ++i) {
15. arr.push(str.charCodeAt(i));
16. }
17. return new Uint8Array(arr);
18. }

20. function uint8ArrayToString(fileData: Uint8Array) {
21. let dataString = '';
22. for (let i = 0; i < fileData.length; i++) {
23. dataString += String.fromCharCode(fileData[i]);
24. }
25. return dataString;
26. }

28. function getRsaGenerateProperties() {
29. let properties: huks.HuksParam[] = [{
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_RSA
32. }, {
33. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
34. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
35. }, {
36. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
38. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
39. }];
40. return properties;
41. }

43. function getRsaEncryptProperties() {
44. let properties: huks.HuksParam[] = [{
45. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
46. value: huks.HuksKeyAlg.HUKS_ALG_RSA
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
49. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
52. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_PADDING,
55. value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
56. }, {
57. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
58. value: huks.HuksCipherMode.HUKS_MODE_ECB
59. }, {
60. tag: huks.HuksTag.HUKS_TAG_DIGEST,
61. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
62. }];
63. return properties;
64. }

66. function getRsaDecryptProperties() {
67. let properties: huks.HuksParam[] = [{
68. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
69. value: huks.HuksKeyAlg.HUKS_ALG_RSA
70. }, {
71. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
72. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
73. }, {
74. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
75. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
76. }, {
77. tag: huks.HuksTag.HUKS_TAG_PADDING,
78. value: huks.HuksKeyPadding.HUKS_PADDING_OAEP
79. }, {
80. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
81. value: huks.HuksCipherMode.HUKS_MODE_ECB
82. }, {
83. tag: huks.HuksTag.HUKS_TAG_DIGEST,
84. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
85. }];
86. return properties;
87. }

89. async function generateRsaKey() {
90. /*
91. * 模拟生成密钥场景
92. */
93. /*
94. * 1. 获取生成密钥算法参数配置
95. */
96. let genProperties = getRsaGenerateProperties();
97. let options: huks.HuksOptions = {
98. properties: genProperties
99. }
100. /*
101. * 2. 调用generateKeyItem
102. */
103. await huks.generateKeyItem(rsaKeyAlias, options)
104. .then(() => {
105. console.info(`promise: generate RSA Key success`);
106. }).catch((error: BusinessError) => {
107. console.error(`promise: generate RSA Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
108. })
109. }

111. async function encryptData() {
112. /*
113. * 模拟加密场景
114. */
115. /*
116. * 1. 获取加密算法参数配置
117. */
118. let encryptProperties = getRsaEncryptProperties();
119. let options: huks.HuksOptions = {
120. properties: encryptProperties,
121. inData: stringToUint8Array(plainText)
122. }
123. /*
124. * 2. 调用initSession获取handle
125. */
126. await huks.initSession(rsaKeyAlias, options)
127. .then((data) => {
128. handle = data.handle;
129. }).catch((error: BusinessError) => {
130. console.error(`promise: init EncryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
131. })
132. /*
133. * 3. 调用finishSession获取加密后的密文
134. */
135. await huks.finishSession(handle, options)
136. .then((data) => {
137. console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
138. cipherData = data.outData as Uint8Array;
139. }).catch((error: BusinessError) => {
140. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
141. })
142. }

144. async function decryptData() {
145. /*
146. * 模拟解密场景
147. */
148. /*
149. * 1. 获取解密算法参数配置
150. */
151. let decryptOptions = getRsaDecryptProperties()
152. let options: huks.HuksOptions = {
153. properties: decryptOptions,
154. inData: cipherData
155. }
156. /*
157. * 2. 调用initSession获取handle
158. */
159. await huks.initSession(rsaKeyAlias, options)
160. .then((data) => {
161. handle = data.handle;
162. }).catch((error: BusinessError) => {
163. console.error(`promise: init DecryptDataRsa failed, errCode : ${error.code}, errMsg : ${error.message}`);
164. })
165. /*
166. * 3. 调用finishSession获取解密后的数据
167. */
168. await huks.finishSession(handle, options)
169. .then((data) => {
170. console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
171. }).catch((error: BusinessError) => {
172. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
173. })
174. }

176. async function deleteKey() {
177. /*
178. * 模拟删除密钥场景
179. */
180. let emptyOptions: huks.HuksOptions = {
181. properties: []
182. }
183. /*
184. * 1. 调用deleteKeyItem删除密钥
185. */
186. await huks.deleteKeyItem(rsaKeyAlias, emptyOptions)
187. .then((data) => {
188. console.info(`promise: delete data success`);
189. }).catch((error: BusinessError) => {
190. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
191. })
192. }
```

[RSAECBOAEPSHA256.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/ets/pages/RSAECBOAEPSHA256.ets#L15-L210)

### SM2

```
1. /*
2. * 以下以SM2模式的Promise操作使用为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let sm2KeyAlias = 'test_sm2KeyAlias';
8. let handle: number;
9. let plainText = '123456';
10. let cipherData: Uint8Array;

12. function stringToUint8Array(str: string) {
13. let arr: number[] = [];
14. for (let i = 0, j = str.length; i < j; ++i) {
15. arr.push(str.charCodeAt(i));
16. }
17. return new Uint8Array(arr);
18. }

20. function uint8ArrayToString(fileData: Uint8Array) {
21. let dataString = '';
22. for (let i = 0; i < fileData.length; i++) {
23. dataString += String.fromCharCode(fileData[i]);
24. }
25. return dataString;
26. }

28. function getSm2GenerateProperties() {
29. let properties: huks.HuksParam[] = [{
30. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
31. value: huks.HuksKeyAlg.HUKS_ALG_SM2
32. }, {
33. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
34. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
35. }, {
36. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT |
38. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
39. }];
40. return properties;
41. }

43. function getSm2EncryptProperties() {
44. let properties: huks.HuksParam[] = [{
45. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
46. value: huks.HuksKeyAlg.HUKS_ALG_SM2
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
49. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
52. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_ENCRYPT
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_DIGEST,
55. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
56. }];
57. return properties;
58. }

60. function getSm2DecryptProperties() {
61. let properties: huks.HuksParam[] = [{
62. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
63. value: huks.HuksKeyAlg.HUKS_ALG_SM2
64. }, {
65. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
66. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
67. }, {
68. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
69. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_DECRYPT
70. }, {
71. tag: huks.HuksTag.HUKS_TAG_DIGEST,
72. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
73. }];
74. return properties;
75. }

77. async function generateSm2Key() {
78. /*
79. * 模拟生成密钥场景
80. */
81. /*
82. * 1. 获取生成密钥算法参数配置
83. */
84. let genProperties = getSm2GenerateProperties();
85. let options: huks.HuksOptions = {
86. properties: genProperties
87. }
88. /*
89. * 2. 调用generateKeyItem
90. */
91. await huks.generateKeyItem(sm2KeyAlias, options)
92. .then(() => {
93. console.info(`promise: generate SM2 Key success`);
94. }).catch((error: BusinessError) => {
95. console.error(`promise: generate SM2 Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
96. })
97. }

99. async function encryptDataSm2() {
100. /*
101. * 模拟加密场景
102. */
103. /*
104. * 1. 获取加密算法参数配置
105. */
106. let encryptProperties = getSm2EncryptProperties();
107. let options: huks.HuksOptions = {
108. properties: encryptProperties,
109. inData: stringToUint8Array(plainText)
110. }
111. /*
112. * 2. 调用initSession获取handle
113. */
114. await huks.initSession(sm2KeyAlias, options)
115. .then((data) => {
116. handle = data.handle;
117. }).catch((error: BusinessError) => {
118. console.error(`promise: init EncryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}`);
119. })
120. /*
121. * 3. 调用finishSession获取加密后的密文
122. */
123. await huks.finishSession(handle, options)
124. .then((data) => {
125. console.info(`promise: encrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
126. cipherData = data.outData as Uint8Array;
127. }).catch((error: BusinessError) => {
128. console.error(`promise: encrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
129. })
130. }

132. async function decryptDataSm2() {
133. /*
134. * 模拟解密场景
135. */
136. /*
137. * 1. 获取解密算法参数配置
138. */
139. let decryptOptions = getSm2DecryptProperties()
140. let options: huks.HuksOptions = {
141. properties: decryptOptions,
142. inData: cipherData
143. }
144. /*
145. * 2. 调用initSession获取handle
146. */
147. await huks.initSession(sm2KeyAlias, options)
148. .then((data) => {
149. handle = data.handle;
150. }).catch((error: BusinessError) => {
151. console.error(`promise: init DecryptDataSm2 failed, errCode : ${error.code}, errMsg : ${error.message}`);
152. })
153. /*
154. * 3. 调用finishSession获取解密后的数据
155. */
156. await huks.finishSession(handle, options)
157. .then((data) => {
158. console.info(`promise: decrypt data success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
159. }).catch((error: BusinessError) => {
160. console.error(`promise: decrypt data failed, errCode : ${error.code}, errMsg : ${error.message}`);
161. })
162. }

164. async function deleteKey() {
165. /*
166. * 模拟删除密钥场景
167. */
168. let emptyOptions: huks.HuksOptions = {
169. properties: []
170. }
171. /*
172. * 1. 调用deleteKeyItem删除密钥
173. */
174. await huks.deleteKeyItem(sm2KeyAlias, emptyOptions)
175. .then(() => {
176. console.info(`promise: delete data success`);
177. }).catch((error: BusinessError) => {
178. console.error(`promise: delete data failed, errCode : ${error.code}, errMsg : ${error.message}`);
179. })
180. }
```

[SM2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/EncryptionDecryption/entry/src/main/ets/pages/SM2.ets#L15-L198)
