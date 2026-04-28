---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-signing-signature-verification-arkts
title: 签名/验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 签名/验签 > 签名/验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2522f615042b44985e00598e98048b9e86e66867104533b1c338dc39b86506d2
---

当前指导提供以下示例，供开发者参考完成签名、验签开发：

* 密钥算法为ECC256、摘要算法为SHA256，请见开发案例：[ECC256/SHA256](huks-signing-signature-verification-arkts.md#ecc256sha256)
* 密钥算法为SM2、摘要算法为SM3，请见开发案例：[SM2/SM3](huks-signing-signature-verification-arkts.md#sm2sm3)
* 密钥算法为SM2、摘要算法为NoDigest，请见开发案例：[SM2/NoDigest](huks-signing-signature-verification-arkts.md#sm2nodigest)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PSS，请见开发案例：[RSA/SHA256/PSS](huks-signing-signature-verification-arkts.md#rsasha256pss)
* 密钥算法为RSA、摘要算法为SHA256、填充模式为PKCS1\_V1\_5，请见开发案例：[RSA/SHA256/PKCS1\_V1\_5](huks-signing-signature-verification-arkts.md#rsasha256pkcs1_v1_5)
* 密钥算法为RSA、摘要算法为SHA384、填充模式为PSS，请见开发案例：[RSA2048/SHA384/PSS](huks-signing-signature-verification-arkts.md#rsa2048sha384pss)
* [密钥算法为ECC、摘要算法为SHA256、用户认证类型包含TUI PIN、携带认证信息的签名类型](huks-signing-signature-verification-arkts.md#eccsha256携带认证信息的签名类型)

具体的场景介绍及支持的算法规格，请参考[签名/验签支持的算法](huks-signing-signature-verification-overview.md#支持的算法)。

## 开发步骤

**生成密钥**

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化密钥属性集。
3. 调用[generateKeyItem](../harmonyos-references/js-apis-huks.md#huksgeneratekeyitem9)生成密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。

除此之外，开发者也可以参考[密钥导入](huks-key-import-overview.md)，导入已有的密钥。

**签名**

1. 获取密钥别名。
2. 指定待签名的明文数据。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入明文数据，properties使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取签名signature。

**验签**

1. 获取密钥别名。
2. 获取待验证的签名signature。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入签名signature，properties使用[HuksParam](../harmonyos-references/js-apis-huks.md#huksparam)设置算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
6. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，验证签名。

**删除密钥**

当密钥废弃不用时，需要调用[deleteKeyItem](../harmonyos-references/js-apis-huks.md#huksdeletekeyitem9)删除密钥，具体请参考[密钥删除](huks-delete-key-arkts.md)。

## 开发案例

### ECC256/SHA256

```
1. /*
2. * 密钥算法为ECC256、摘要算法为SHA256
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_eccKeyAlias';
7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function stringToUint8Array(str: String) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getEccGenerateProperties() {
28. let properties: huks.HuksParam[] = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_ECC
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
36. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
37. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_DIGEST,
40. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
41. }];
42. return properties;
43. }

45. function getEccSignProperties() {
46. let properties: huks.HuksParam[] = [{
47. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
48. value: huks.HuksKeyAlg.HUKS_ALG_ECC
49. }, {
50. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
51. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
54. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_DIGEST,
57. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
58. }];
59. return properties;
60. }

62. function getEccVerifyProperties() {
63. let properties: huks.HuksParam[] = [{
64. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
65. value: huks.HuksKeyAlg.HUKS_ALG_ECC
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
68. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
71. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_DIGEST,
74. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
75. }];
76. return properties;
77. }

79. async function generateEccKey(keyAlias: string) {
80. let genProperties = getEccGenerateProperties();
81. let options: huks.HuksOptions = {
82. properties: genProperties
83. }
84. await huks.generateKeyItem(keyAlias, options)
85. .then((data) => {
86. console.info(`promise: generate ECC Key success, data = ${JSON.stringify(data)}`);
87. }).catch((err: Error) => {
88. console.error(`promise: generate ECC Key failed, error: ` + JSON.stringify(err));
89. throw (err as Error);
90. })
91. }

93. async function sign(keyAlias: string, plaintext: string) {
94. let signProperties = getEccSignProperties();
95. let options: huks.HuksOptions = {
96. properties: signProperties,
97. inData: stringToUint8Array(plaintext)
98. }
99. await huks.initSession(keyAlias, options)
100. .then((data) => {
101. handle = data.handle;
102. }).catch((err: Error) => {
103. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
104. throw (err as Error);
105. })
106. await huks.finishSession(handle, options)
107. .then((data) => {
108. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
109. signature = data.outData as Uint8Array;
110. }).catch((err: Error) => {
111. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
112. throw (err as Error);
113. })
114. }

116. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
117. let verifyProperties = getEccVerifyProperties()
118. let options: huks.HuksOptions = {
119. properties: verifyProperties,
120. inData: stringToUint8Array(plaintext)
121. }
122. await huks.initSession(keyAlias, options)
123. .then((data) => {
124. handle = data.handle;
125. }).catch((err: Error) => {
126. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
127. throw (err as Error);
128. })
129. await huks.updateSession(handle, options)
130. .then((data) => {
131. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
132. }).catch((err: Error) => {
133. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
134. throw (err as Error);
135. })
136. options.inData = signature;
137. await huks.finishSession(handle, options)
138. .then((data) => {
139. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
140. }).catch((err: Error) => {
141. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
142. throw (err as Error);
143. })
144. }

146. async function deleteEccKey(keyAlias: string) {
147. let emptyOptions: huks.HuksOptions = {
148. properties: []
149. }
150. await huks.deleteKeyItem(keyAlias, emptyOptions)
151. .then((data) => {
152. console.info(`promise: delete data success`);
153. }).catch((err: Error) => {
154. console.error(`promise: delete data failed`);
155. throw (err as Error);
156. })
157. }

159. async function testSignVerify() {
160. await generateEccKey(keyAlias);
161. await sign(keyAlias, plaintext);
162. await verify(keyAlias, plaintext, signature);
163. await deleteEccKey(keyAlias);
164. }
```

[ECC256SHA256.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/ECC256SHA256.ets#L16-L181)

### SM2/SM3

```
1. /*
2. * 密钥算法为SM2、摘要算法为SM3
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_sm2KeyAlias';
7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function stringToUint8Array(str: String) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getSm2GenerateProperties() {
28. let properties: huks.HuksParam[] = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_SM2
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
36. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
37. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_DIGEST,
40. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
41. }];
42. return properties;
43. }

45. function getSm2SignProperties() {
46. let properties: huks.HuksParam[] = [{
47. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
48. value: huks.HuksKeyAlg.HUKS_ALG_SM2
49. }, {
50. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
51. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
54. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_DIGEST,
57. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
58. }];
59. return properties;
60. }

62. function getSm2VerifyProperties() {
63. let properties: huks.HuksParam[] = [{
64. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
65. value: huks.HuksKeyAlg.HUKS_ALG_SM2
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
68. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
71. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_DIGEST,
74. value: huks.HuksKeyDigest.HUKS_DIGEST_SM3
75. }];
76. return properties;
77. }

79. async function generateSm2Key(keyAlias: string) {
80. let genProperties = getSm2GenerateProperties();
81. let options: huks.HuksOptions = {
82. properties: genProperties
83. }
84. await huks.generateKeyItem(keyAlias, options)
85. .then((data) => {
86. console.info(`promise: generate Sm2 Key success, data = ${JSON.stringify(data)}`);
87. }).catch((err: Error) => {
88. console.error(`promise: generate Sm2 Key failed, error: ` + JSON.stringify(err));
89. throw (err as Error);
90. })
91. }

93. async function sign(keyAlias: string, plaintext: string) {
94. let signProperties = getSm2SignProperties();
95. let options: huks.HuksOptions = {
96. properties: signProperties,
97. inData: stringToUint8Array(plaintext)
98. }
99. await huks.initSession(keyAlias, options)
100. .then((data) => {
101. handle = data.handle;
102. }).catch((err: Error) => {
103. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
104. throw (err as Error);
105. })
106. await huks.finishSession(handle, options)
107. .then((data) => {
108. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
109. signature = data.outData as Uint8Array;
110. }).catch((err: Error) => {
111. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
112. throw (err as Error);
113. })
114. }

116. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
117. let verifyProperties = getSm2VerifyProperties()
118. let options: huks.HuksOptions = {
119. properties: verifyProperties,
120. inData: stringToUint8Array(plaintext)
121. }
122. await huks.initSession(keyAlias, options)
123. .then((data) => {
124. handle = data.handle;
125. }).catch((err: Error) => {
126. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
127. throw (err as Error);
128. })
129. await huks.updateSession(handle, options)
130. .then((data) => {
131. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
132. }).catch((err: Error) => {
133. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
134. throw (err as Error);
135. })
136. options.inData = signature;
137. await huks.finishSession(handle, options)
138. .then((data) => {
139. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
140. }).catch((err: Error) => {
141. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
142. throw (err as Error);
143. })
144. }

146. async function deleteSm2Key(keyAlias: string) {
147. let emptyOptions: huks.HuksOptions = {
148. properties: []
149. }
150. await huks.deleteKeyItem(keyAlias, emptyOptions)
151. .then((data) => {
152. console.info(`promise: delete data success`);
153. }).catch((err: Error) => {
154. console.error(`promise: delete data failed`);
155. throw (err as Error);
156. })
157. }

159. export async function testSignVerify() {
160. await generateSm2Key(keyAlias);
161. await sign(keyAlias, plaintext);
162. await verify(keyAlias, plaintext, signature);
163. await deleteSm2Key(keyAlias);
164. }
```

[SM2SM3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/SM2SM3.ets#L16-L181)

### SM2/NoDigest

```
1. /*
2. * 密钥算法为SM2、摘要算法为NoDigest，由业务自己做SM3摘要
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let keyAlias = 'test_sm2KeyAlias';
8. let handle: number;
9. let hash = '12345678901234567890123456789012';
10. let signature: Uint8Array;

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
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
38. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
39. }, {
40. tag: huks.HuksTag.HUKS_TAG_DIGEST,
41. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
42. }];
43. return properties;
44. }

46. function getSm2SignProperties() {
47. let properties: huks.HuksParam[] = [{
48. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
49. value: huks.HuksKeyAlg.HUKS_ALG_SM2
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
52. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
55. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
56. }, {
57. tag: huks.HuksTag.HUKS_TAG_DIGEST,
58. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
59. }];
60. return properties;
61. }

63. function getSm2VerifyProperties() {
64. let properties: huks.HuksParam[] = [{
65. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
66. value: huks.HuksKeyAlg.HUKS_ALG_SM2
67. }, {
68. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
69. value: huks.HuksKeySize.HUKS_SM2_KEY_SIZE_256
70. }, {
71. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
72. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
73. }, {
74. tag: huks.HuksTag.HUKS_TAG_DIGEST,
75. value: huks.HuksKeyDigest.HUKS_DIGEST_NONE
76. }];
77. return properties;
78. }

80. async function generateSm2Key(keyAlias: string) {
81. console.info(`enter generateSm2Key`);
82. let genProperties = getSm2GenerateProperties();
83. let options: huks.HuksOptions = {
84. properties: genProperties
85. };
86. await huks.generateKeyItem(keyAlias, options)
87. .then(() => {
88. console.info(`promise: generateSm2Key success`);
89. }).catch((error: BusinessError) => {
90. console.error(`promise: generateSm2Key failed, errCode : ${error.code}, errMsg : ${error.message}`);
91. throw (error as Error);
92. })
93. }

95. async function sign(keyAlias: string, plaintext: string) {
96. let signProperties = getSm2SignProperties();
97. let options: huks.HuksOptions = {
98. properties: signProperties,
99. inData: stringToUint8Array(plaintext)
100. };
101. await huks.initSession(keyAlias, options)
102. .then((data) => {
103. handle = data.handle;
104. }).catch((error: BusinessError) => {
105. console.error(`promise: init sign failed, error: ` + JSON.stringify(error));
106. throw (error as Error);
107. })
108. await huks.finishSession(handle, options)
109. .then((data) => {
110. signature = data.outData as Uint8Array;
111. console.info(`promise: sign success, data is ` + uint8ArrayToString(signature));
112. }).catch((error: BusinessError) => {
113. console.error(`promise: sign failed, error: ` + JSON.stringify(error));
114. throw (error as Error);
115. })
116. }

118. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
119. let verifyProperties = getSm2VerifyProperties();
120. let options: huks.HuksOptions = {
121. properties: verifyProperties,
122. inData: stringToUint8Array(plaintext)
123. };
124. await huks.initSession(keyAlias, options)
125. .then((data) => {
126. handle = data.handle;
127. }).catch((error: BusinessError) => {
128. console.error(`promise: init verify failed, error: ` + JSON.stringify(error));
129. throw (error as Error);
130. })
131. await huks.updateSession(handle, options)
132. .then((data) => {
133. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
134. }).catch((error: BusinessError) => {
135. console.error(`promise: update verify failed, error: ` + JSON.stringify(error));
136. throw (error as Error);
137. })
138. options.inData = signature;
139. await huks.finishSession(handle, options)
140. .then((data) => {
141. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
142. }).catch((error: BusinessError) => {
143. console.error(`promise: verify failed, error: ` + JSON.stringify(error));
144. throw (error as Error);
145. })
146. }

148. async function deleteSm2Key(keyAlias: string) {
149. console.info(`enter deleteSm2Key`);
150. let emptyOptions: huks.HuksOptions = {
151. properties: []
152. };
153. await huks.deleteKeyItem(keyAlias, emptyOptions)
154. .then((data) => {
155. console.info(`promise: delete data success`);
156. }).catch((error: Error) => {
157. console.error(`promise: delete data failed`);
158. throw (error as Error);
159. })
160. }

162. async function testSignVerify() {
163. await generateSm2Key(keyAlias);
164. await sign(keyAlias, hash);
165. await verify(keyAlias, hash, signature);
166. await deleteSm2Key(keyAlias);
167. }
```

[SM2NoDigest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/SM2NoDigest.ets#L16-L184)

### RSA/SHA256/PSS

```
1. /*
2. * 密钥算法为RSA，摘要算法为SHA256，填充模式为PSS
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_rsaKeyAlias';
7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function stringToUint8Array(str: string) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getRsaGenerateProperties() {
28. let properties: huks.HuksParam[] = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_RSA
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
36. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
37. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_PADDING,
40. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_DIGEST,
43. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
44. }];
45. return properties;
46. }

48. function getRsaSignProperties() {
49. let properties: huks.HuksParam[] = [{
50. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
51. value: huks.HuksKeyAlg.HUKS_ALG_RSA
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_PADDING,
54. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_DIGEST,
57. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
60. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
61. }];
62. return properties;
63. }

65. function getRsaVerifyProperties() {
66. let properties: huks.HuksParam[] = [{
67. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
68. value: huks.HuksKeyAlg.HUKS_ALG_RSA
69. }, {
70. tag: huks.HuksTag.HUKS_TAG_PADDING,
71. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_DIGEST,
74. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
77. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
78. }];
79. return properties;
80. }

82. async function generateRsaKey(keyAlias: string) {
83. let genProperties = getRsaGenerateProperties();
84. let options: huks.HuksOptions = {
85. properties: genProperties
86. };
87. await huks.generateKeyItem(keyAlias, options)
88. .then((data) => {
89. console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
90. }).catch((err: Error) => {
91. console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
92. throw (err as Error);
93. });
94. }

96. async function sign(keyAlias: string, plaintext: string) {
97. let signProperties = getRsaSignProperties();
98. let options: huks.HuksOptions = {
99. properties: signProperties,
100. inData: stringToUint8Array(plaintext)
101. }
102. await huks.initSession(keyAlias, options)
103. .then((data) => {
104. handle = data.handle;
105. }).catch((err: Error) => {
106. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
107. return;
108. });

110. if (handle !== undefined) {
111. await huks.finishSession(handle, options)
112. .then((data) => {
113. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
114. signature = data.outData as Uint8Array;
115. }).catch((err: Error) => {
116. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
117. throw (err as Error);
118. });
119. }
120. }

122. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
123. let verifyProperties = getRsaVerifyProperties();
124. let options: huks.HuksOptions = {
125. properties: verifyProperties,
126. inData: stringToUint8Array(plaintext)
127. }
128. await huks.initSession(keyAlias, options)
129. .then((data) => {
130. handle = data.handle;
131. }).catch((err: Error) => {
132. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
133. return;
134. });

136. if (handle !== undefined) {
137. await huks.updateSession(handle, options)
138. .then((data) => {
139. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
140. }).catch((err: Error) => {
141. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
142. throw (err as Error);
143. });

145. options.inData = signature;
146. await huks.finishSession(handle, options)
147. .then((data) => {
148. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
149. }).catch((err: Error) => {
150. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
151. throw (err as Error);
152. });
153. }
154. }

156. async function deleteRsaKey(keyAlias: string) {
157. let emptyOptions: huks.HuksOptions = {
158. properties: []
159. }
160. await huks.deleteKeyItem(keyAlias, emptyOptions)
161. .then((data) => {
162. console.info(`promise: delete data success`);
163. }).catch((err: Error) => {
164. console.error(`promise: delete data failed`);
165. throw (err as Error);
166. });
167. }

169. export async function testSignVerify() {
170. await generateRsaKey(keyAlias);
171. await sign(keyAlias, plaintext);
172. await verify(keyAlias, plaintext, signature);
173. await deleteRsaKey(keyAlias);
174. }
```

[RSASHA256PSS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/RSASHA256PSS.ets#L16-L191)

### RSA/SHA256/PKCS1\_V1\_5

```
1. /*
2. * 密钥算法为RSA，摘要算法为SHA256，填充模式为PKCS1_V1_5
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_rsaKeyAlias';
7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function stringToUint8Array(str: String) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getRsaGenerateProperties() {
28. let properties: huks.HuksParam[] = [
29. { tag: huks.HuksTag.HUKS_TAG_ALGORITHM, value: huks.HuksKeyAlg.HUKS_ALG_RSA },
30. { tag: huks.HuksTag.HUKS_TAG_KEY_SIZE, value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048 },
31. {
32. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
33. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
34. },
35. { tag: huks.HuksTag.HUKS_TAG_PADDING, value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5 },
36. { tag: huks.HuksTag.HUKS_TAG_DIGEST, value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256 }
37. ];
38. return properties;
39. }

41. function getRsaSignProperties() {
42. let properties: huks.HuksParam[] = [{
43. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
44. value: huks.HuksKeyAlg.HUKS_ALG_RSA
45. }, {
46. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
47. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
48. }, {
49. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
50. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
51. }, {
52. tag: huks.HuksTag.HUKS_TAG_PADDING,
53. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
54. }, {
55. tag: huks.HuksTag.HUKS_TAG_DIGEST,
56. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
57. }];
58. return properties;
59. }

61. function getRsaVerifyProperties() {
62. let properties: huks.HuksParam[] = [{
63. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
64. value: huks.HuksKeyAlg.HUKS_ALG_RSA
65. }, {
66. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
67. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
68. }, {
69. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
70. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
71. }, {
72. tag: huks.HuksTag.HUKS_TAG_PADDING,
73. value: huks.HuksKeyPadding.HUKS_PADDING_PKCS1_V1_5
74. }, {
75. tag: huks.HuksTag.HUKS_TAG_DIGEST,
76. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
77. }];
78. return properties;
79. }

81. async function generateRsaKey(keyAlias: string) {
82. let genProperties = getRsaGenerateProperties();
83. let options: huks.HuksOptions = {
84. properties: genProperties
85. }
86. await huks.generateKeyItem(keyAlias, options)
87. .then((data) => {
88. console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
89. }).catch((err: Error) => {
90. console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
91. throw (err as Error);
92. })
93. }

95. async function sign(keyAlias: string, plaintext: string) {
96. let signProperties = getRsaSignProperties();
97. let options: huks.HuksOptions = {
98. properties: signProperties,
99. inData: stringToUint8Array(plaintext)
100. }
101. await huks.initSession(keyAlias, options)
102. .then((data) => {
103. handle = data.handle;
104. }).catch((err: Error) => {
105. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
106. throw (err as Error);
107. })
108. await huks.finishSession(handle, options)
109. .then((data) => {
110. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
111. signature = data.outData as Uint8Array;
112. }).catch((err: Error) => {
113. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
114. throw (err as Error);
115. })
116. }

118. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
119. let verifyProperties = getRsaVerifyProperties()
120. let options: huks.HuksOptions = {
121. properties: verifyProperties,
122. inData: stringToUint8Array(plaintext)
123. }
124. await huks.initSession(keyAlias, options)
125. .then((data) => {
126. handle = data.handle;
127. }).catch((err: Error) => {
128. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
129. throw (err as Error);
130. })
131. await huks.updateSession(handle, options)
132. .then((data) => {
133. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
134. }).catch((err: Error) => {
135. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
136. throw (err as Error);
137. })
138. options.inData = signature;
139. await huks.finishSession(handle, options)
140. .then((data) => {
141. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
142. }).catch((err: Error) => {
143. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
144. throw (err as Error);
145. })
146. }

148. async function deleteRsaKey(keyAlias: string) {
149. let emptyOptions: huks.HuksOptions = {
150. properties: []
151. }
152. await huks.deleteKeyItem(keyAlias, emptyOptions)
153. .then((data) => {
154. console.info(`promise: delete data success`);
155. }).catch((err: Error) => {
156. console.error(`promise: delete data failed`);
157. throw (err as Error);
158. })
159. }

161. export async function testSignVerify() {
162. await generateRsaKey(keyAlias);
163. await sign(keyAlias, plaintext);
164. await verify(keyAlias, plaintext, signature);
165. await deleteRsaKey(keyAlias);
166. }
```

[RSASHA256PKCS1\_V1\_5.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/RSASHA256PKCS1_V1_5.ets#L16-L183)

### RSA2048/SHA384/PSS

```
1. /*
2. * 密钥算法为RSA2048、摘要算法为SHA384、填充模式为PSS
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. let keyAlias = 'test_rsaSha384PssKeyAlias';
7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function stringToUint8Array(str: String) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function getRsaGenerateProperties() {
28. let properties: huks.HuksParam[] = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_RSA
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
36. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
37. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_PADDING,
40. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_DIGEST,
43. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
44. }];
45. return properties;
46. }

48. function getRsaSignProperties() {
49. let properties: huks.HuksParam[] = [{
50. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
51. value: huks.HuksKeyAlg.HUKS_ALG_RSA
52. }, {
53. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
54. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
55. }, {
56. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
57. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
58. }, {
59. tag: huks.HuksTag.HUKS_TAG_PADDING,
60. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
61. }, {
62. tag: huks.HuksTag.HUKS_TAG_DIGEST,
63. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
64. }];
65. return properties;
66. }

68. function getRsaVerifyProperties() {
69. let properties: huks.HuksParam[] = [{
70. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
71. value: huks.HuksKeyAlg.HUKS_ALG_RSA
72. }, {
73. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
74. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
75. }, {
76. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
77. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
78. }, {
79. tag: huks.HuksTag.HUKS_TAG_PADDING,
80. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
81. }, {
82. tag: huks.HuksTag.HUKS_TAG_DIGEST,
83. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA384
84. }];
85. return properties;
86. }

88. async function generateRsaKey(keyAlias: string) {
89. let genProperties = getRsaGenerateProperties();
90. let options: huks.HuksOptions = {
91. properties: genProperties
92. }
93. await huks.generateKeyItem(keyAlias, options)
94. .then((data) => {
95. console.info(`promise: generate RSA Key success, data = ${JSON.stringify(data)}`);
96. }).catch((err: Error) => {
97. console.error(`promise: generate RSA Key failed, error: ` + JSON.stringify(err));
98. throw (err as Error);
99. })
100. }

102. async function sign(keyAlias: string, plaintext: string) {
103. let signProperties = getRsaSignProperties();
104. let options: huks.HuksOptions = {
105. properties: signProperties,
106. inData: stringToUint8Array(plaintext)
107. };
108. await huks.initSession(keyAlias, options)
109. .then((data) => {
110. handle = data.handle;
111. }).catch((err: Error) => {
112. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
113. throw (err as Error);
114. })
115. await huks.finishSession(handle, options)
116. .then((data) => {
117. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
118. signature = data.outData as Uint8Array;
119. }).catch((err: Error) => {
120. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
121. throw (err as Error);
122. })
123. }

125. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
126. let verifyProperties = getRsaVerifyProperties()
127. let options: huks.HuksOptions = {
128. properties: verifyProperties,
129. inData: stringToUint8Array(plaintext)
130. };
131. await huks.initSession(keyAlias, options)
132. .then((data) => {
133. handle = data.handle;
134. }).catch((err: Error) => {
135. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
136. throw (err as Error);
137. })
138. await huks.updateSession(handle, options)
139. .then((data) => {
140. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
141. }).catch((err: Error) => {
142. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
143. throw (err as Error);
144. })
145. options.inData = signature;
146. await huks.finishSession(handle, options)
147. .then((data) => {
148. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
149. }).catch((err: Error) => {
150. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
151. throw (err as Error);
152. })
153. }

155. async function deleteRsaKey(keyAlias: string) {
156. let emptyOptions: huks.HuksOptions = {
157. properties: []
158. };
159. await huks.deleteKeyItem(keyAlias, emptyOptions)
160. .then((data) => {
161. console.info(`promise: delete data success`);
162. }).catch((err: Error) => {
163. console.error(`promise: delete data failed`);
164. throw (err as Error);
165. })
166. }

168. async function testSignVerify() {
169. await generateRsaKey(keyAlias);
170. await sign(keyAlias, plaintext);
171. await verify(keyAlias, plaintext, signature);
172. await deleteRsaKey(keyAlias);
173. }
```

[RSA2048SHA384PSS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/KeyUsage/SigningVerification/entry/src/main/ets/pages/RSA2048SHA384PSS.ets#L16-L190)

### ECC/SHA256/携带认证信息的签名类型

前提条件：此功能的示例代码依赖数字盾服务的设置数字盾密码和验证数字盾密码，请参考[数字盾服务](devicesecurity-trustedauth-service.md)的数字盾密码管理和交易信息密码认证。

```
1. /*
2. * 密钥算法为ECC，摘要算法为SHA256，用户认证类型包含TUI PIN，携带认证信息的签名类型
3. * 在签名参数中加上HUKS_TAG_KEY_SECURE_SIGN_TYPE，值为HUKS_SECURE_SIGN_WITH_AUTHINFO即可使用携带认证信息的签名类型
4. * 在验签时，把携带认证信息的签名的前41位数据拆出来，剩下的是签名，然后把携带的认证信息拼在原数据的前面。
5. * 设置数字盾密码和验证数字盾密码请参考数字盾服务
6. */
7. import { huks } from '@kit.UniversalKeystoreKit';

9. let keyAlias = 'test_eccKeyAlias';
10. let handle: number;
11. let challenge: Uint8Array;
12. let plaintext = '123456';
13. let signature: Uint8Array;

15. function stringToUint8Array(str: String) {
16. let arr: number[] = new Array();
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

31. function GetEccGenerateProperties() {
32. let properties: Array<huks.HuksParam> = [{
33. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
34. value: huks.HuksKeyAlg.HUKS_ALG_ECC
35. }, {
36. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
37. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN | huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
38. }, {
39. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
40. value: huks.HuksKeySize.HUKS_ECC_KEY_SIZE_256,
41. }, {
42. tag: huks.HuksTag.HUKS_TAG_DIGEST,
43. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
44. }, {
45. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_PURPOSE,
46. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
47. }, {
48. tag: huks.HuksTag.HUKS_TAG_USER_AUTH_TYPE,
49. value: huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_TUI_PIN | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FINGERPRINT | huks.HuksUserAuthType.HUKS_USER_AUTH_TYPE_FACE
50. }, {
51. tag: huks.HuksTag.HUKS_TAG_KEY_AUTH_ACCESS_TYPE,
52. value: huks.HuksAuthAccessType.HUKS_AUTH_ACCESS_ALWAYS_VALID
53. }, {
54. tag: huks.HuksTag.HUKS_TAG_CHALLENGE_TYPE,
55. value: huks.HuksChallengeType.HUKS_CHALLENGE_TYPE_NORMAL
56. }];

58. return properties;
59. }

61. function GetEccSignProperties() {
62. let properties: Array<huks.HuksParam> = [{
63. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
64. value: huks.HuksKeyAlg.HUKS_ALG_ECC
65. }, {
66. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
67. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
68. }, {
69. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
70. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
71. }, {
72. tag: huks.HuksTag.HUKS_TAG_DIGEST,
73. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
74. }, {
75. tag: huks.HuksTag.HUKS_TAG_KEY_SECURE_SIGN_TYPE,
76. value: huks.HuksSecureSignType.HUKS_SECURE_SIGN_WITH_AUTHINFO
77. }];
78. return properties;
79. }

81. function GetEccVerifyProperties() {
82. let properties: Array<huks.HuksParam> = [{
83. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
84. value: huks.HuksKeyAlg.HUKS_ALG_ECC
85. }, {
86. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
87. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
88. }, {
89. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
90. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
91. }, {
92. tag: huks.HuksTag.HUKS_TAG_DIGEST,
93. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
94. }];
95. return properties;
96. }

98. async function GenerateEccKey(keyAlias: string) {
99. let genProperties = GetEccGenerateProperties();
100. let options: huks.HuksOptions = {
101. properties: genProperties
102. }
103. await huks.generateKeyItem(keyAlias, options)
104. .then((data) => {
105. console.info(`promise: generate ECC Key success, data = ${JSON.stringify(data)}`);
106. }).catch((err: Error) => {
107. console.error(`promise: generate ECC Key failed, error: ` + JSON.stringify(err));
108. })
109. }

111. async function sign(keyAlias: string, plaintext: string) {
112. let signProperties = GetEccSignProperties();
113. let options: huks.HuksOptions = {
114. properties: signProperties,
115. inData: stringToUint8Array(plaintext)
116. }
117. await huks.initSession(keyAlias, options)
118. .then((data) => {
119. handle = data.handle;
120. challenge = data.challenge as Uint8Array;
121. }).catch((err: Error) => {
122. console.error(`promise: init sign failed, error: ` + JSON.stringify(err));
123. })

125. let TuiAuthToken :trustedAuthentication.AuthToken;
126. // 验证TUI PIN并获取Authtoken请参考数字盾服务

128. await huks.finishSession(handle, options, TuiAuthToken.authToken)
129. .then((data) => {
130. console.info(`promise: sign success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
131. signature = data.outData as Uint8Array;
132. }).catch((err: Error) => {
133. console.error(`promise: sign failed, error: ` + JSON.stringify(err));
134. })
135. }

137. async function verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
138. let verifyProperties = GetEccVerifyProperties();
139. // 在验签时，把携带认证信息的签名的前41位数据拆出来，剩下的是签名，然后把携带的认证信息拼在原数据的前面。
140. let appendInfo = signature.subarray(0, 41);
141. let newSignature = signature.subarray(41);
142. let newIndata = new Uint8Array(appendInfo.length + indataArray.length);
143. newIndata.set(appendInfo, 0);
144. newIndata.set(stringToUint8Array(plaintext), appendInfo.length);
145. let options: huks.HuksOptions = {
146. properties: verifyProperties,
147. inData: newIndata
148. }
149. await huks.initSession(keyAlias, options)
150. .then((data) => {
151. handle = data.handle;
152. }).catch((err: Error) => {
153. console.error(`promise: init verify failed, error: ` + JSON.stringify(err));
154. })
155. await huks.updateSession(handle, options)
156. .then((data) => {
157. console.info(`promise: update verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
158. }).catch((err: Error) => {
159. console.error(`promise: update verify failed, error: ` + JSON.stringify(err));
160. })
161. options.inData = newSignature;
162. await huks.finishSession(handle, options)
163. .then((data) => {
164. console.info(`promise: verify success, data is ` + uint8ArrayToString(data.outData as Uint8Array));
165. }).catch((err: Error) => {
166. console.error(`promise: verify failed, error: ` + JSON.stringify(err));
167. })
168. }

170. async function DeleteEccKey(keyAlias: string) {
171. let emptyOptions: huks.HuksOptions = {
172. properties: []
173. }
174. await huks.deleteKeyItem(keyAlias, emptyOptions)
175. .then((data) => {
176. console.info(`promise: delete data success`);
177. }).catch((err: Error) => {
178. console.error(`promise: delete data failed`);
179. })
180. }

182. async function testSignVerify() {
183. await GenerateEccKey(keyAlias);
184. await sign(keyAlias, plaintext);
185. await verify(keyAlias, plaintext, signature);
186. await DeleteEccKey(keyAlias);
187. }
```
