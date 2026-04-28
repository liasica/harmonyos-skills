---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-anon-attestation-arkts
title: 匿名密钥证明(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥证明 > 匿名密钥证明(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf3914f09a9915a0201e47a96d98a61fc3793fecec2e854b8b23d61c3337d9c1
---

在使用本功能时，需确保网络通畅。

## 开发步骤

1. 指定密钥别名，密钥别名命名规范参考[密钥生成介绍及算法规格](huks-key-generation-overview.md)。
2. 初始化参数集。

   [HuksOptions](../harmonyos-references/js-apis-huks.md#huksoptions)中的properties字段中的参数必须包含[HUKS\_TAG\_ATTESTATION\_CHALLENGE](../harmonyos-references/js-apis-huks.md#hukstag)属性,可选参数包含[HUKS\_TAG\_ATTESTATION\_ID\_VERSION\_INFO](../harmonyos-references/js-apis-huks.md#hukstag)，[HUKS\_TAG\_ATTESTATION\_ID\_ALIAS](../harmonyos-references/js-apis-huks.md#hukstag)属性。
3. 生成非对称密钥，具体请参考[密钥生成](huks-key-generation-overview.md)。
4. 将密钥别名与参数集作为参数传入[anonAttestKeyItem](../harmonyos-references/js-apis-huks.md#huksanonattestkeyitem11)方法中，即可证明密钥。

## 开发案例

```
1. /*
2. * 以下以anonAttestKey的Promise接口操作验证为例
3. */
4. import { huks } from '@kit.UniversalKeystoreKit';

6. /* 1.确定密钥别名 */
7. let keyAliasString = 'key anon attest';
8. let aliasString = keyAliasString;
9. let aliasUint8 = stringToUint8Array(keyAliasString);
10. let securityLevel = stringToUint8Array('sec_level');
11. let challenge = stringToUint8Array('challenge_data');
12. let versionInfo = stringToUint8Array('version_info');
13. let anonAttestCertChain: string[];

15. class ThrowObject {
16. public isThrow: boolean = false;
17. }

19. /* 封装生成时的密钥参数集 */
20. let genKeyProperties: huks.HuksParam[] = [
21. {
22. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
23. value: huks.HuksKeyAlg.HUKS_ALG_RSA
24. },
25. {
26. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
27. value: huks.HuksKeySize.HUKS_RSA_KEY_SIZE_2048
28. },
29. {
30. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
31. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
32. },
33. {
34. tag: huks.HuksTag.HUKS_TAG_DIGEST,
35. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
36. },
37. {
38. tag: huks.HuksTag.HUKS_TAG_PADDING,
39. value: huks.HuksKeyPadding.HUKS_PADDING_PSS
40. },
41. {
42. tag: huks.HuksTag.HUKS_TAG_KEY_GENERATE_TYPE,
43. value: huks.HuksKeyGenerateType.HUKS_KEY_GENERATE_TYPE_DEFAULT
44. },
45. {
46. tag: huks.HuksTag.HUKS_TAG_BLOCK_MODE,
47. value: huks.HuksCipherMode.HUKS_MODE_ECB
48. }
49. ]
50. let genOptions: huks.HuksOptions = {
51. properties: genKeyProperties
52. };

54. /* 2.封装证明密钥的参数集 */
55. let anonAttestKeyProperties: huks.HuksParam[] = [
56. {
57. tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_SEC_LEVEL_INFO,
58. value: securityLevel
59. },
60. {
61. tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
62. value: challenge
63. },
64. {
65. tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_VERSION_INFO,
66. value: versionInfo
67. },
68. {
69. tag: huks.HuksTag.HUKS_TAG_ATTESTATION_ID_ALIAS,
70. value: aliasUint8
71. }
72. ]
73. let huksOptions: huks.HuksOptions = {
74. properties: anonAttestKeyProperties
75. };

77. function stringToUint8Array(str: string) {
78. let arr: number[] = [];
79. for (let i = 0, j = str.length; i < j; ++i) {
80. arr.push(str.charCodeAt(i));
81. }
82. return new Uint8Array(arr);
83. }

85. function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
86. return new Promise<void>((resolve, reject) => {
87. try {
88. huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
89. if (error) {
90. reject(error);
91. } else {
92. resolve(data);
93. }
94. });
95. } catch (error) {
96. throwObject.isThrow = true;
97. throw (error as Error);
98. }
99. });
100. }

102. /* 3.生成密钥 */
103. async function publicGenKeyFunc(keyAlias: string, huksOptions: huks.HuksOptions) {
104. console.info(`enter promise generateKeyItem`);
105. let throwObject: ThrowObject = { isThrow: false };
106. try {
107. await generateKeyItem(keyAlias, huksOptions, throwObject)
108. .then((data) => {
109. console.info(`promise: generateKeyItem success, data = ${JSON.stringify(data)}`);
110. })
111. .catch((error: Error) => {
112. if (throwObject.isThrow) {
113. throw (error as Error);
114. } else {
115. console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
116. }
117. });
118. } catch (error) {
119. console.error(`promise: generateKeyItem input arg invalid, ${JSON.stringify(error)}`);
120. }
121. }

123. /* 4.证明密钥 */
124. function anonAttestKeyItem(keyAlias: string, huksOptions: huks.HuksOptions, throwObject: ThrowObject) {
125. return new Promise<huks.HuksReturnResult>((resolve, reject) => {
126. try {
127. huks.anonAttestKeyItem(keyAlias, huksOptions, (error, data) => {
128. if (error) {
129. reject(error);
130. } else {
131. resolve(data);
132. }
133. });
134. } catch (error) {
135. throwObject.isThrow = true;
136. throw (error as Error);
137. }
138. });
139. }

141. async function publicAnonAttestKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<string> {
142. console.info(`enter promise anonAttestKeyItem`);
143. let throwObject: ThrowObject = { isThrow: false };
144. try {
145. await anonAttestKeyItem(keyAlias, huksOptions, throwObject)
146. .then((data) => {
147. console.info(`promise: anonAttestKeyItem success, data = ${JSON.stringify(data)}`);
148. if (data !== null && data.certChains !== null) {
149. anonAttestCertChain = data.certChains as string[];
150. }
151. })
152. .catch((error: Error) => {
153. if (throwObject.isThrow) {
154. throw (error as Error);
155. } else {
156. console.error(`promise: anonAttestKeyItem failed, ${JSON.stringify(error)}`);
157. }
158. });
159. return 'Success';
160. } catch (error) {
161. console.error(`promise: anonAttestKeyItem input arg invalid, ${JSON.stringify(error)}`);
162. return 'Failed';
163. }
164. }

166. async function anonAttestKeyTest(): Promise<string> {
167. await publicGenKeyFunc(aliasString, genOptions);
168. let ret = await publicAnonAttestKey(aliasString, huksOptions);
169. console.info('anon attest certChain data: ' + anonAttestCertChain)
170. return ret;
171. }
```

[AnonymousKeyProof.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/UniversalKeystoreKit/AnonymousKeyProof/entry/src/main/ets/pages/AnonymousKeyProof.ets#L15-L187)
