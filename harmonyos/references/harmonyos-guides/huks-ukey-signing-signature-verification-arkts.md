---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-ukey-signing-signature-verification-arkts
title: 签名/验签(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > 签名/验签 > 签名/验签(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7b400d47e9ada4dbaf9e56cc0a8aff063fb24a0248e474dd57244269690df318
---

当前指导提供以下示例，供开发者参考完成签名、验签开发：

* [密钥算法为RSA、摘要算法为SHA256、填充模式为PSS](huks-ukey-signing-signature-verification-arkts.md#rsasha256pss)

具体的场景介绍及支持的算法规格，请参考[签名/验签介绍及算法规格](huks-ukey-signing-signature-verification-overview.md)。

## 开发步骤

**签名**

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，[打开资源](huks-open-close-resource-ndk.md#打开资源)后完成PIN码认证。
2. 指定待签名的明文数据。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入明文数据，properties传入算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，获取签名signature。

**验签**

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)作为resourceId，并作为密钥别名，然后[打开资源](huks-open-close-resource-ndk.md#打开资源)。
2. 获取待验证的签名。
3. 获取属性参数[HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)，包括两个字段properties和inData。inData传入签名signature，properties传入算法参数配置。
4. 调用[initSession](../harmonyos-references/js-apis-huks.md#huksinitsession9)初始化密钥会话，并获取会话的句柄handle。
5. 调用[updateSession](../harmonyos-references/js-apis-huks.md#huksupdatesession9)更新密钥会话。
6. 调用[finishSession](../harmonyos-references/js-apis-huks.md#huksfinishsession9)结束密钥会话，验证签名。

## 开发案例

### RSA/SHA256/PSS

```
1. /*
2. * 密钥算法为RSA，摘要算法为SHA256，填充模式为PSS
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let handle: number;
8. let plaintext = '123456';
9. let signature: Uint8Array;

11. function StringToUint8Array(str: string) {
12. let arr: number[] = [];
13. for (let i = 0, j = str.length; i < j; ++i) {
14. arr.push(str.charCodeAt(i));
15. }
16. return new Uint8Array(arr);
17. }

19. function Uint8ArrayToString(fileData: Uint8Array) {
20. let dataString = '';
21. for (let i = 0; i < fileData.length; i++) {
22. dataString += String.fromCharCode(fileData[i]);
23. }
24. return dataString;
25. }

27. function GetRsaSignProperties() {
28. let properties: Array<huks.HuksParam> = [{
29. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
30. value: huks.HuksKeyAlg.HUKS_ALG_RSA
31. }, {
32. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
33. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
34. }, {
35. tag: huks.HuksTag.HUKS_TAG_PADDING,
36. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
37. }, {
38. tag: huks.HuksTag.HUKS_TAG_DIGEST,
39. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
40. }, {
41. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
42. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN
43. }, {
44. tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
45. value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
46. }];
47. return properties;
48. }

50. function GetRsaVerifyProperties() {
51. let properties: Array<huks.HuksParam> = [{
52. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
53. value: huks.HuksKeyAlg.HUKS_ALG_RSA
54. }, {
55. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
56. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
57. }, {
58. tag: huks.HuksTag.HUKS_TAG_PADDING,
59. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
60. }, {
61. tag: huks.HuksTag.HUKS_TAG_DIGEST,
62. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
63. }, {
64. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
65. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
66. }, {
67. tag: huks.HuksTag.HUKS_TAG_KEY_CLASS,
68. value: huks.HuksKeyClassType.HUKS_KEY_CLASS_EXTENSION
69. }];
70. return properties;
71. }

73. async function initSession(keyAlias: string, huksOptions: huks.HuksOptions) {
74. console.info(`promise: enter initSession`);
75. try {
76. await huks.initSession(keyAlias, huksOptions)
77. .then((data) => {
78. handle = data.handle;
79. console.info(`promise: initSession success`);
80. }).catch((error: BusinessError) => {
81. console.error(`promise: initSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
82. })
83. } catch (error) {
84. console.error(`promise: initSession input arg invalid`);
85. }
86. }

88. async function updateSession(handle: number, huksOptions: huks.HuksOptions) {
89. console.info(`promise: enter updateSession`);
90. try {
91. await huks.updateSession(handle, huksOptions)
92. .then((data) => {
93. let outData = data.outData as Uint8Array;
94. console.info(`promise: updateSession success, data = ${Uint8ArrayToString(outData)}`);
95. }).catch((error: BusinessError) => {
96. console.error(`promise: updateSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
97. })
98. } catch (error) {
99. console.error(`promise: updateSession input arg invalid`);
100. }
101. }

103. async function finishSession(handle: number, huksOptions: huks.HuksOptions) {
104. console.info(`promise: enter finishSession`);
105. try {
106. await huks.finishSession(handle, huksOptions)
107. .then((data) => {
108. signature = data.outData as Uint8Array;
109. console.info(`promise: finishSession success, data = ${Uint8ArrayToString(signature)}`);
110. }).catch((error: BusinessError) => {
111. console.error(`promise: finishSession failed, errCode : ${error.code}, errMsg : ${error.message}`);
112. })
113. } catch (error) {
114. console.error(`promise: finishSession input arg invalid`);
115. }
116. }

118. async function Sign(keyAlias: string, plaintext: string) {
119. console.info(`enter Sign`);
120. let signProperties = GetRsaSignProperties();
121. let options: huks.HuksOptions = {
122. properties: signProperties,
123. }
124. await initSession(keyAlias, options);

126. if (handle !== undefined) {
127. options.inData = StringToUint8Array(plaintext);
128. await finishSession(handle, options);
129. }
130. }

132. async function Verify(keyAlias: string, plaintext: string, signature: Uint8Array) {
133. console.info(`enter Verify`);
134. let verifyProperties = GetRsaVerifyProperties();
135. let options: huks.HuksOptions = {
136. properties: verifyProperties,
137. }

139. await initSession(keyAlias, options);

141. if (handle !== undefined) {
142. options.inData = StringToUint8Array(plaintext);
143. await updateSession(handle, options);
144. options.inData = signature;
145. await finishSession(handle, options);
146. }
147. }

149. async function testSignVerify() {
150. // 假设keyAlias是已获取的resourceId
151. let keyAlias = JSON.stringify({
152. providerName: "testProviderName",
153. bundleName: "com.example.cryptoapplication",
154. abilityName: "CryptoExtension",
155. index: {
156. key: "testKey"
157. } as ESObject
158. });
159. await Sign(keyAlias, plaintext);
160. await Verify(keyAlias, plaintext, signature);
161. }
```
