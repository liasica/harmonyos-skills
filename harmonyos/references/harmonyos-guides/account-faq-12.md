---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-12
title: ID Token的使用场景与使用方法
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > ID Token的使用场景与使用方法
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c19bb658a3813250a0cef26a547518023714b822b2dae4bb12de53b0c519bc5a
---

ID Token是OIDC（[OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)）协议相对于OAuth 2.0协议扩展的一个用户身份凭证。

ID Token 是 JWT Token格式，意味着：

1. 用户的身份信息直接被编码进了ID Token，不需要额外请求其他的资源来获取用户信息。
2. ID Token 可以验证其是华为账号服务颁发的，携带华为账号签名信息，验证签名可证明其没有被篡改过。

## 使用场景

1. 应用无服务器，只有客户端，该场景下无法使用Authorization Code完成服务器侧的接口调用获取用户信息，需从ID Token中解析出用户信息；
2. 应用有服务器，希望在服务器侧解析ID Token对应字段，获取用户信息。

## 字段说明

ID Token是JWT Token格式数据，其中payload包含字段如下：

| 字段 | 参数类型 | 是否默认返回 | 描述 |
| --- | --- | --- | --- |
| iss | string | 是 | 固定值："https://accounts.huawei.com"。 |
| sub | string | 是 | 即用户的UnionID。同一个开发者下的所有应用，此参数均相同。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。 |
| aud | string | 是 | 接收ID Token的Client ID。 |
| exp | number | 是 | ID Token的过期时间戳（10位）。 |
| iat | number | 是 | ID Token的生成时间戳（10位）。 |
| at\_hash | string | 是 | Access Token的哈希值。 |
| azp | string | 是 | 生成ID Token的Client ID。 |
| openid | string | 是 | 用户OpenID。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。 |
| nonce | string | 否 | 防重放攻击随机值。详情请参考[LoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#loginwithhuaweiidrequest)或[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)的nonce字段说明。 |
| picture | string | 否 | 用户头像图片链接。该字段返回场景：[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |
| display\_name | string | 否 | 华为账号对应的昵称，没有昵称则取匿名化的邮箱或手机号。该字段返回场景：  [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |
| nickname | string | 否 | 华为账号对应的昵称。该字段返回场景：  [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)中的scopes包含profile。 |

## 解析与验证

### **服务端解析与验证**

使用场景：有服务器应用。

对于有应用服务端的应用，推荐在服务端进行ID Token解析与验证，具体参考以下Maven工程依赖配置及Java示例代码。

Maven工程依赖：

```
1. <dependencies>
2. <dependency>
3. <groupId>com.alibaba.fastjson2</groupId>
4. <artifactId>fastjson2</artifactId>
5. <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
6. </dependency>
7. <dependency>
8. <groupId>org.bouncycastle</groupId>
9. <artifactId>bcprov-jdk18on</artifactId>
10. <version>1.74</version> <!--此处替换为您项目需要的版本-->
11. </dependency>
12. <dependency>
13. <groupId>org.apache.httpcomponents</groupId>
14. <artifactId>httpclient</artifactId>
15. <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
16. </dependency>
17. <dependency>
18. <groupId>com.auth0</groupId>
19. <artifactId>jwks-rsa</artifactId>
20. <version>0.8.2</version> <!--此处替换为您项目需要的版本-->
21. </dependency>
22. <dependency>
23. <groupId>com.auth0</groupId>
24. <artifactId>java-jwt</artifactId>
25. <version>3.8.1</version> <!--此处替换为您项目需要的版本-->
26. </dependency>
27. </dependencies>
```

Java代码示例：

```
1. import com.alibaba.fastjson2.JSONArray;
2. import com.alibaba.fastjson2.JSONObject;
3. import com.auth0.jwk.InvalidPublicKeyException;
4. import com.auth0.jwk.Jwk;
5. import com.auth0.jwt.JWT;
6. import com.auth0.jwt.JWTVerifier;
7. import com.auth0.jwt.algorithms.Algorithm;
8. import com.auth0.jwt.exceptions.JWTDecodeException;
9. import com.auth0.jwt.exceptions.JWTVerificationException;
10. import com.auth0.jwt.exceptions.TokenExpiredException;
11. import com.auth0.jwt.interfaces.DecodedJWT;
12. import org.apache.commons.codec.binary.Base64;
13. import org.apache.http.HttpEntity;
14. import org.apache.http.client.config.RequestConfig;
15. import org.apache.http.client.methods.CloseableHttpResponse;
16. import org.apache.http.client.methods.HttpGet;
17. import org.apache.http.impl.client.CloseableHttpClient;
18. import org.apache.http.impl.client.HttpClients;
19. import org.apache.http.util.EntityUtils;
20. import org.bouncycastle.jce.provider.BouncyCastleProvider;
21. import java.nio.charset.StandardCharsets;
22. import java.security.GeneralSecurityException;
23. import java.security.Security;
24. import java.security.Signature;
25. import java.security.interfaces.RSAPublicKey;
26. import java.util.ArrayList;
27. import java.util.HashMap;
28. import java.util.List;
29. import java.util.Map;
30. public class IDTokenParser {
31. // 请替换为您的Client ID
32. private final static String CLIENT_ID = "123456";
33. private final static int MAX_PUBLIC_KEY_SIZE = 4;
34. // 缓存jwt公钥信息
35. private final Map<String, RSAPublicKey> keyId2PublicKey = new HashMap<>();
36. /**
37. * JWK JSON Web Key端点，开发者可以从该端点获取最近两天的JWK
38. * 公钥在24小时内更新。确保以下ID Token在24小时内生成
39. */
40. private static final String CERT_URL = "https://oauth-login.cloud.huawei.com/oauth2/v3/certs";
41. // ID Token的issuer
42. public static final String ID_TOKEN_ISSUE = "https://accounts.huawei.com";
43. public static final String ALG_RS256 = "RS256";
44. public final static String ALG_PS256 = "PS256";
45. public static void main(String[] args) throws Exception {
46. // 由上述CLIENT_ID对应值生成的ID Token
47. String idToken = "<ID Token>";
48. IDTokenParser idTokenParser = new IDTokenParser();
49. JSONObject idTokenInfo = idTokenParser.verifyAndParse(idToken);
50. // 解析获取ID Token中的数据，例：解析获取iss
51. String iss = idTokenInfo.getString("iss");
52. }
53. /**
54. * 验证并解析ID Token
55. * @param idToken idToken
56. * @return ID Token携带的信息
57. * @throws Exception 异常
58. */
59. public JSONObject verifyAndParse(String idToken) throws Exception {
60. try {
61. DecodedJWT decoder = JWT.decode(idToken);
62. if (!decoder.getIssuer().equals(ID_TOKEN_ISSUE)) {
63. // issuer校验不通过，抛出异常（异常类型可自行选择）
64. throw new RuntimeException("issuer no match");
65. }
66. if (decoder.getAudience().size() > 0) {
67. if (!decoder.getAudience().get(0).equals(CLIENT_ID)) {
68. // audience校验不通过，抛出异常（异常类型可自行选择）
69. throw new RuntimeException("audience no match");
70. }
71. }
72. // 获取ID Token签名使用的算法
73. String alg = decoder.getAlgorithm();
74. if (ALG_RS256.equals(alg)) {
75. Algorithm algorithm = Algorithm.RSA256(getRSAPublicKeyByKid(decoder.getKeyId()), null);
76. JWTVerifier verifier = JWT.require(algorithm).build();
77. JSONObject jsonObject = JSONObject.parseObject(new String(Base64.decodeBase64(decoder.getPayload())));
78. // 验证签名
79. verifier.verify(decoder);
80. jsonObject.put("alg", decoder.getAlgorithm());
81. jsonObject.put("typ", decoder.getType());
82. jsonObject.put("kid", decoder.getKeyId());
83. return jsonObject;
84. } else if (ALG_PS256.equals(alg)) {
85. PS256Algorithm algorithm = new PS256Algorithm(getRSAPublicKeyByKid(decoder.getKeyId()));
86. boolean verifyResult = algorithm.verify(decoder.getHeader(), decoder.getPayload(),
87. decoder.getSignature());
88. if (verifyResult) {
89. JSONObject jsonObject = JSONObject.parseObject(
90. new String(Base64.decodeBase64(decoder.getPayload())));
91. jsonObject.put("alg", decoder.getAlgorithm());
92. jsonObject.put("typ", decoder.getType());
93. jsonObject.put("kid", decoder.getKeyId());
94. return jsonObject;
95. }
96. }
97. return null;
98. } catch (JWTDecodeException e) {
99. // ID Token解析失败，此场景常见于ID Token格式不正确
100. throw new RuntimeException("ID Token decode failed");
101. } catch (TokenExpiredException e) {
102. // ID Token已过期
103. throw new RuntimeException("ID Token expired");
104. }
105. }
106. /**
107. * 通过kid获取公钥信息，请缓存公钥信息，示例中采用map方式进行缓存，开发者可选择其它合适的方式进行缓存
108. * @param keyId  keyId
109. * @return 公钥信息
110. * @throws InvalidPublicKeyException 异常
111. */
112. private RSAPublicKey getRSAPublicKeyByKid(String keyId) throws InvalidPublicKeyException {
113. if (keyId2PublicKey.get(keyId) != null) {
114. return keyId2PublicKey.get(keyId);
115. }
116. JSONArray keys = getJwks();
117. if (keys == null) {
118. return null;
119. }
120. if (keyId2PublicKey.size() > MAX_PUBLIC_KEY_SIZE) {
121. keyId2PublicKey.clear();
122. }
123. for (int i = 0; i < keys.size(); i++) {
124. String kid = keys.getJSONObject(i).getString("kid");
125. String alg = keys.getJSONObject(i).getString("alg");
126. if (ALG_RS256.equals(alg) || ALG_PS256.equals(alg)) {
127. keyId2PublicKey.put(kid, getRsaPublicKeyByJwk(keys.getJSONObject(i)));
128. }
129. }
130. return keyId2PublicKey.get(keyId);
131. }
132. /**
133. * 从https://oauth-login.cloud.huawei.com/oauth2/v3/certs获取jwt公钥信息jwk
134. * 因为jwk每天都会更新，所以需要缓存jwk
135. * @return JSONObject 公钥信息数组
136. */
137. private static JSONArray getJwks() {
138. CloseableHttpClient httpClient = HttpClients.createDefault();
139. HttpGet httpGet = new HttpGet(CERT_URL);
140. RequestConfig requestConfig = RequestConfig.custom()
141. .setConnectTimeout(5000)
142. .setConnectionRequestTimeout(5000)
143. .setSocketTimeout(5000)
144. .build();
145. httpGet.setConfig(requestConfig);
146. try {
147. CloseableHttpResponse response = httpClient.execute(httpGet);
148. HttpEntity entity = response.getEntity();
149. String result = EntityUtils.toString(entity);
150. return JSONObject.parseObject(result).getJSONArray("keys");
151. } catch (Exception e) {
152. return null;
153. } finally {
154. if (null != httpClient) {
155. try {
156. httpClient.close();
157. } catch (Exception e) {
158. e.printStackTrace();
159. }
160. }
161. }
162. }
163. /**
164. * 通过jwk获取公钥信息
165. * @return RSAPublicKey 公钥信息
166. */
167. private static RSAPublicKey getRsaPublicKeyByJwk(JSONObject jwkObject) throws InvalidPublicKeyException {
168. Map<String, Object> additionalAttributes = new HashMap<>();
169. additionalAttributes.put("n", jwkObject.getString("n"));
170. additionalAttributes.put("e", jwkObject.getString("e"));
171. List<String> operations = new ArrayList<>();
172. Jwk jwk = new Jwk(jwkObject.getString("kid"), jwkObject.getString("kty"), jwkObject.getString("alg"),
173. jwkObject.getString("use"), operations, null, null, null, additionalAttributes);
174. return (RSAPublicKey) jwk.getPublicKey();
175. }
176. static class PS256Algorithm {
177. private final RSAPublicKey publicKey;
178. public PS256Algorithm(RSAPublicKey publicKey) {
179. this.publicKey = publicKey;
180. }
181. public boolean verify(String header, String payload, String signature) throws JWTVerificationException {
182. byte[] contentBytes = (header + '.' + payload).getBytes(StandardCharsets.UTF_8);
183. byte[] signatureBytes = Base64.decodeBase64(signature);
184. try {
185. Security.addProvider(new BouncyCastleProvider());
186. Signature sign = Signature.getInstance("SHA256WithRSA/PSS");
187. sign.initVerify(publicKey);
188. sign.update(contentBytes);
189. return sign.verify(signatureBytes);
190. } catch (GeneralSecurityException e) {
191. throw new JWTVerificationException("JWT verify failed");
192. }
193. }
194. }
195. }
```

### **客户端解析与验证**

使用场景：无服务器应用。

对于无服务器应用，可在客户端获取ID Token后，进行本地解析与验证，解析后可获取用户数据，并验证签名，具体参考如下ArkTS代码示例，将获取的ID Token作为方法入参，并将代码中的CLIENT\_ID替换为应用真实的Client ID：

```
1. import { buffer } from '@kit.ArkTS';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
3. import { http } from '@kit.NetworkKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. decodeBase64(data: string): string {
7. return buffer.from(data, 'base64').toString('utf8');
8. }
9. // 解析ID Token并验证
10. decodeIdToken(idToken: string): void {
11. const parts = idToken.split('.');
12. if (parts.length !== 3) {
13. return;
14. }
15. const idTokenObj: Record<string, Object> = {};
16. // ID Token头部
17. idTokenObj['header'] = JSON.parse(this.decodeBase64(parts[0]));
18. // ID Token负载
19. idTokenObj['payload'] = JSON.parse(this.decodeBase64(parts[1]));
20. // ID Token签名
21. idTokenObj['signature'] = parts[2];
22. const header: Record<string, string> = idTokenObj['header'] as Record<string, string>;
23. // 从负载中解析出nonce等数据
24. const payLoad: Record<string, string> = idTokenObj['payload'] as Record<string, string>;
25. const nonce: string = payLoad['nonce'];
26. // 应用Client ID，使用前请替换
27. const CLIENT_ID: string = '<应用Client ID>';
28. const ID_TOKEN_ISSUE: string = 'https://accounts.huawei.com';
29. const iss: string = payLoad['iss'];
30. const aud: string = payLoad['aud'];
31. if(iss !== ID_TOKEN_ISSUE){
32. // 验证失败，开发者处理失败场景
33. hilog.error(0x0000, 'testTag', 'Failed to check iss');
34. return;
35. }
36. if(aud !== CLIENT_ID){
37. // 验证失败，开发者处理失败场景
38. hilog.error(0x0000, 'testTag', 'Failed to check aud');
39. return;
40. }
41. // 验证签名
42. this.checkSignature(idToken, header['kid'], header['alg']);
43. }

45. private stringToUint8Array(str: string): Uint8Array {
46. const arr: number[] = [];
47. for (let i = 0, j = str.length; i < j; ++i) {
48. arr.push(str.charCodeAt(i));
49. }
50. const tmpUint8Array: Uint8Array = new Uint8Array(arr);
51. return tmpUint8Array;
52. }
53. // 验签方法
54. private checkSignature(idToken: string, kid: string, alg: string) {
55. if (!idToken) {
56. return;
57. }
58. const parts = idToken.split('.');
59. if (parts.length !== 3) {
60. return;
61. }
62. const url = 'https://oauth-login.cloud.huawei.com/oauth2/v3/certs';
63. // 创建http请求，应用需在module.json5文件中先申请“ohos.permission.INTERNET”网络权限，请求才能发送成功
64. const httpRequest = http.createHttp();
65. httpRequest.request(url, (err, data) => {
66. if (err) {
67. hilog.error(0x0000, 'testTag', `Failed to httpRequest. Code: ${err.code}, message: ${err.message}`);
68. httpRequest.destroy();
69. return;
70. }
71. let nStr = '';
72. let eStr = '';
73. const keys: object[] = JSON.parse(data.result as string)["keys"];
74. for (let item of keys) {
75. if (kid === item['kid']) {
76. nStr = item['n'];
77. eStr = item['e'];
78. break;
79. }
80. }
81. const nBigInt = '0x' + buffer.from(nStr, "base64url").toString('hex');
82. const eBigInt = '0x' + buffer.from(eStr, "base64url").toString('hex');
83. const dsaCommonSpec: cryptoFramework.RSACommonParamsSpec = {
84. algName: "RSA",
85. specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
86. n: BigInt(nBigInt),
87. }
88. const rsaKeyPairSpec: cryptoFramework.RSAPubKeySpec = {
89. algName: "RSA",
90. specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC,
91. params: dsaCommonSpec,
92. pk: BigInt(eBigInt),
93. }
94. const asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(rsaKeyPairSpec);
95. asyKeyGeneratorBySpec.generatePubKey(async (error, publicKey) => {
96. if (error) {
97. return;
98. }
99. if (publicKey === null) {
100. return;
101. }
102. const idTokenSign = parts[2];
103. const idTokenSignArr: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(idTokenSign, "base64url").buffer) };
104. const idToken = parts[0] + '.' + parts[1];
105. const idTokenArr: cryptoFramework.DataBlob = { data: this.stringToUint8Array(idToken) };
106. const verifier = alg === 'PS256' ? cryptoFramework.createVerify("RSA2048|PSS|SHA256|MGF1_SHA256")
107. : cryptoFramework.createVerify("RSA2048|PKCS1|SHA256");
108. verifier.init(publicKey, (initErr, result) => {
109. verifier.verify(idTokenArr, idTokenSignArr, (verifyErr, data) => {
110. // 打印验签结果，结果为true则验签通过
111. hilog.info(0x0000, 'testTag', 'verify result is: %{public}s', data);
112. });
113. });
114. })
115. httpRequest.destroy();
116. });
117. }
```
