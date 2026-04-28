---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-process-userinfo-change
title: 订阅和处理用户信息变更
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 订阅和处理用户信息变更
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:06+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:281b21d857f00ac9544411b9f8d8bbe0220de12e36c8f298b9530ed41f3d665a
---

## 概述

通过订阅用户信息变更，您可以接收有关用户及其账户的重要更新。当用户及其账户信息发生变更时，华为账号服务器会发送通知到应用服务端，应用服务端可以根据通知消息进行自身业务处理。

## 用户信息变更事件介绍

| 消息名称 | 事件类型 | 事件描述 |
| --- | --- | --- |
| tokens-revoked | https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked | 用户取消应用的授权 |
| account-purged | https://schemas.openid.net/secevent/risc/event-type/account-purged | 用户注销华为账号 |
| phone-modified | https://schemas.openid.net/secevent/oauth/event-type/phone-modified | 用户授权手机号变更 |

## 订阅用户信息变更

订阅步骤如下：

1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/)，选择“管理中心 > API服务 > API库”。
2. 选择项目，然后在API名称搜索框检索关键字“RISC”，找到RISC点击进入详情。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/3WCl7qbJTaWvyrqcr1ukdA/zh-cn_image_0000002583438807.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=090699C04F70641EB07FE5B5182E61D0777C09B70BA9CA61C0F6FD9AB985951F)
3. 点击启用按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/O6i05fRNRsGRlBUMNa-DTQ/zh-cn_image_0000002552958762.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=A836FBB9F94938A64EAD8B8794581BBC4CC0F1E022AEED23447944B8C15B1E63)
4. 点击订阅通知按钮，在弹窗中配置回调地址及订阅范围。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/1eAEQuJQRxW7i7xcsQ7EIw/zh-cn_image_0000002583478763.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=8BF5D43A5F08BD41048F9B1F6F018279ECDCDF72DC7964F989193EEABBD6DB49)

   说明

   回调地址：在开启订阅通知后，若华为用户信息发生变更，会发送通知消息到该地址。

   订阅范围：订阅的用户信息变更事件，详见[用户信息变更事件介绍](subscribe-process-userinfo-change.md#用户信息变更事件介绍)。

## 处理通知消息

华为账号服务器向开发者应用服务端投递消息。开发者应用服务端接收到消息后需要先对消息头中的令牌进行验签，确保消息的完整有效性后解析并获取用户信息变更事件详情。具体步骤如下：

1. **验证消息头中的令牌签名。**

   您可通过任何JWT库（例如：[jwt.io](https://jwt.io/introduction/)）对其进行解析与验证。

   无论使用哪种库，您均需完成如下操作：

   1. 调用接口（https://risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration），获取发行者标识（issuer）与签名密钥证书URI（jwks\_uri）。
   2. 通过依赖的JWT库，对消息头中的令牌进行解析，获取签名的KeyId。
   3. 通过签名的KeyId，从签名密钥证书URI中获取到JWT签名的公钥。
   4. 校验JWT签名中的aud与[订阅用户信息变更](subscribe-process-userinfo-change.md#订阅用户信息变更)中提供的Client ID一致。
   5. 校验JWT签名中的issuer与发行者标识（issuer）一致。

   具体验签逻辑，请参考如下示例代码：

   Maven依赖配置

   ```
   1. <dependencies>
   2. <dependency>
   3. <groupId>com.github.ben-manes.caffeine</groupId>
   4. <artifactId>caffeine</artifactId>
   5. <version>2.9.3</version> <!--此处替换为您项目需要的版本-->
   6. </dependency>
   7. <dependency>
   8. <groupId>com.auth0</groupId>
   9. <artifactId>jwks-rsa</artifactId>
   10. <version>0.21.2</version> <!--此处替换为您项目需要的版本-->
   11. </dependency>
   12. <dependency>
   13. <groupId>io.jsonwebtoken</groupId>
   14. <artifactId>jjwt-impl</artifactId>
   15. <version>0.11.5</version> <!--此处替换为您项目需要的版本-->
   16. </dependency>
   17. <dependency>
   18. <groupId>io.jsonwebtoken</groupId>
   19. <artifactId>jjwt-jackson</artifactId>
   20. <version>0.11.5</version> <!--此处替换为您项目需要的版本-->
   21. </dependency>
   22. <dependency>
   23. <groupId>com.alibaba.fastjson2</groupId>
   24. <artifactId>fastjson2</artifactId>
   25. <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
   26. </dependency>
   27. <dependency>
   28. <groupId>org.apache.httpcomponents</groupId>
   29. <artifactId>httpclient</artifactId>
   30. <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
   31. </dependency>
   32. <dependency>
   33. <groupId>org.projectlombok</groupId>
   34. <artifactId>lombok</artifactId>
   35. <version>1.18.26</version> <!--此处替换为您项目需要的版本-->
   36. </dependency>
   37. <dependency>
   38. <groupId>ch.qos.logback</groupId>
   39. <artifactId>logback-classic</artifactId>
   40. <version>1.2.11</version> <!--此处替换为您项目需要的版本-->
   41. </dependency>
   42. </dependencies>
   ```

   Java验签代码示例

   ```
   1. import com.alibaba.fastjson2.JSON;
   2. import com.alibaba.fastjson2.JSONObject;
   3. import com.auth0.jwk.JwkProvider;
   4. import com.auth0.jwk.UrlJwkProvider;
   5. import com.github.benmanes.caffeine.cache.CacheLoader;
   6. import com.github.benmanes.caffeine.cache.Caffeine;
   7. import com.github.benmanes.caffeine.cache.LoadingCache;
   8. import io.jsonwebtoken.Claims;
   9. import io.jsonwebtoken.IncorrectClaimException;
   10. import io.jsonwebtoken.JwsHeader;
   11. import io.jsonwebtoken.Jwt;
   12. import io.jsonwebtoken.JwtParser;
   13. import io.jsonwebtoken.Jwts;
   14. import io.jsonwebtoken.SigningKeyResolver;
   15. import io.jsonwebtoken.security.SignatureException;
   16. import lombok.Data;
   17. import lombok.extern.slf4j.Slf4j;
   18. import org.apache.http.HttpEntity;
   19. import org.apache.http.HttpStatus;
   20. import org.apache.http.client.config.RequestConfig;
   21. import org.apache.http.client.methods.CloseableHttpResponse;
   22. import org.apache.http.client.methods.HttpGet;
   23. import org.apache.http.config.Registry;
   24. import org.apache.http.config.RegistryBuilder;
   25. import org.apache.http.conn.socket.ConnectionSocketFactory;
   26. import org.apache.http.conn.socket.PlainConnectionSocketFactory;
   27. import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
   28. import org.apache.http.impl.client.CloseableHttpClient;
   29. import org.apache.http.impl.client.HttpClients;
   30. import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
   31. import org.apache.http.util.EntityUtils;
   32. import org.checkerframework.checker.nullness.qual.NonNull;
   33. import org.checkerframework.checker.nullness.qual.Nullable;
   34. import javax.net.ssl.SSLContext;
   35. import javax.net.ssl.TrustManagerFactory;
   36. import java.io.IOException;
   37. import java.net.URL;
   38. import java.security.Key;
   39. import java.security.KeyManagementException;
   40. import java.security.KeyStore;
   41. import java.security.KeyStoreException;
   42. import java.security.NoSuchAlgorithmException;
   43. import java.security.PublicKey;
   44. import java.util.Objects;
   45. import java.util.concurrent.TimeUnit;

   47. /**
   48. * 订阅和处理用户信息变更
   49. */
   50. @Slf4j
   51. public class RiscDemo {
   52. /**
   53. * 公开配置信息地址
   54. */
   55. private static final String PUBLIC_CONFIGURATION_URL = "https://risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration";

   57. /**
   58. * 公开信息缓存
   59. */
   60. private final LoadingCache<String, PublicConfiguration> publicConfigurationCache = Caffeine.newBuilder()
   61. .expireAfterWrite(1, TimeUnit.DAYS)
   62. .build(key -> {
   63. HttpGet request = new HttpGet(PUBLIC_CONFIGURATION_URL);
   64. try (CloseableHttpResponse response = getClient().execute(request)) {
   65. HttpEntity responseEntity = response.getEntity();
   66. String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
   67. EntityUtils.consume(responseEntity);
   68. int statusCode = response.getStatusLine().getStatusCode();
   69. // http状态码不是200，抛出异常
   70. if (statusCode != HttpStatus.SC_OK) {
   71. throw new IOException("call failed! http status code: " + statusCode + ", response data: " + ret);
   72. }
   73. JSONObject configJson = (JSONObject) JSON.parse(ret);
   74. if (configJson == null) {
   75. throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
   76. }
   77. String issuer = configJson.getString("issuer");
   78. String jwksUri = configJson.getString("jwks_uri");
   79. if (Objects.isNull(issuer) || Objects.isNull(jwksUri)) {
   80. throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
   81. }
   82. PublicConfiguration publicConfiguration = new PublicConfiguration();
   83. publicConfiguration.setIssuer(issuer);
   84. publicConfiguration.setJwksUri(jwksUri);
   85. return publicConfiguration;
   86. }
   87. });

   89. /**
   90. * 公钥信息缓存
   91. */
   92. private final LoadingCache<String, PublicKey> publicKeyCache = Caffeine.newBuilder()
   93. .expireAfterWrite(1, TimeUnit.DAYS)
   94. .build(new CacheLoader<String, PublicKey>() {
   95. @Override
   96. public @Nullable PublicKey load(@NonNull String key) throws Exception {
   97. PublicConfiguration publicConfiguration = getPublicConfiguration();
   98. JwkProvider huaweiCerts = new UrlJwkProvider(new URL(publicConfiguration.getJwksUri()), null, null);
   99. return huaweiCerts.get(key).getPublicKey();
   100. }
   101. });

   103. /**
   104. * 调试方法入口
   105. * @param args main方法入参
   106. */
   107. public static void main(String[] args) {
   108. // 消息请求头中Authorization: Bearer <token>中的<token>
   109. String token = "<token>";
   110. // Client ID
   111. String clientId = "<Client ID>";
   112. Jwt<?, ?> jwt = new RiscDemo().validateSecurityEventToken(token, clientId);
   113. if (Objects.isNull(jwt)) {
   114. // 验签失败
   115. log.error("verify sign failed");
   116. } else {
   117. // 验签成功
   118. log.info("verify sign success");
   119. }
   120. }

   122. /**
   123. * 对Authorization头域中的token进行验签
   124. *
   125. * @param token    消息请求头中Authorization: Bearer <token>中的<token>
   126. * @param clientId clientId
   127. * @return 返回为null，则表示验签失败，否则表示验证成功
   128. */
   129. public Jwt<?, ?> validateSecurityEventToken(String token, String clientId) {
   130. try {
   131. // 公开配置信息中的issuer值
   132. String issuer = getPublicConfiguration().getIssuer();
   133. SigningKeyResolver signingKeyResolver = new SigningKeyResolver() {
   134. private PublicKey getPublicKey(JwsHeader<?> jwsHeader) {
   135. try {
   136. return publicKeyCache.get(jwsHeader.getKeyId());
   137. } catch (Exception e) {
   138. throw new RuntimeException(e);
   139. }
   140. }
   141. @Override
   142. public Key resolveSigningKey(JwsHeader jwsHeader, Claims claims) {
   143. return getPublicKey(jwsHeader);
   144. }
   145. @Override
   146. public Key resolveSigningKey(JwsHeader jwsHeader, String s) {
   147. return getPublicKey(jwsHeader);
   148. }
   149. };
   150. // 验证并解析消息内容
   151. JwtParser parser = Jwts.parserBuilder()
   152. .requireIssuer(issuer)
   153. .requireAudience(clientId)
   154. .setAllowedClockSkewSeconds(60)
   155. .setSigningKeyResolver(signingKeyResolver)
   156. .build();
   157. return parser.parse(token);
   158. } catch (IncorrectClaimException e) {
   159. // 消息的claim无效，针对异常进行处理（如：日志记录）
   160. log.error("claim invalid", e);
   161. } catch (SignatureException e) {
   162. // 验签失败，针对异常进行处理（如：日志记录）
   163. log.error("verify signature failed", e);
   164. } catch (Exception e) {
   165. // 其他异常，业务自行处理
   166. log.error("valid event token failed", e);
   167. }
   168. return null;
   169. }

   171. private PublicConfiguration getPublicConfiguration() {
   172. PublicConfiguration publicConfiguration = this.publicConfigurationCache.get("DEFAULT");
   173. if (publicConfiguration == null) {
   174. throw new IllegalArgumentException("public configuration get failed!");
   175. }
   176. return publicConfiguration;
   177. }

   179. private static CloseableHttpClient getClient() {
   180. PoolingHttpClientConnectionManager connectionManager = buildConnectionManager(
   181. new String[] {"TLSv1.2"}, new String[] {
   182. "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
   183. "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
   184. });
   185. connectionManager.setMaxTotal(400);
   186. connectionManager.setDefaultMaxPerRoute(400);
   187. RequestConfig config = RequestConfig.custom()
   188. .setConnectionRequestTimeout(100)
   189. .setRedirectsEnabled(false)
   190. .build();
   191. return HttpClients.custom()
   192. .useSystemProperties()
   193. .setConnectionManager(connectionManager)
   194. .setDefaultRequestConfig(config)
   195. .build();
   196. }

   198. private static PoolingHttpClientConnectionManager buildConnectionManager(String[] supportedProtocols,
   199. String[] supportedCipherSuites) {
   200. PoolingHttpClientConnectionManager connectionManager = null;
   201. try {
   202. SSLContext sc = SSLContext.getInstance("TLSv1.2");
   203. TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
   204. tmf.init((KeyStore) null);
   205. sc.init(null, tmf.getTrustManagers(), null);
   206. SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sc, supportedProtocols,
   207. supportedCipherSuites, SSLConnectionSocketFactory.getDefaultHostnameVerifier());
   208. Registry<ConnectionSocketFactory> registry = RegistryBuilder.<ConnectionSocketFactory>create()
   209. .register("http", new PlainConnectionSocketFactory())
   210. .register("https", sslsf)
   211. .build();
   212. connectionManager = new PoolingHttpClientConnectionManager(registry);
   213. } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
   214. log.error("build connect manager failed", e);
   215. }
   216. return connectionManager;
   217. }

   219. @Data
   220. static class PublicConfiguration {
   221. private String issuer;
   222. private String jwksUri;
   223. }
   224. }
   ```
2. **处理消息体。**

   * **JSON对象格式消息体**

     消息示例：用户注销华为账号

     ```
     1. {
     2. "iss": "id.cloud.huawei.com",
     3. "aud": "<Client ID>",
     4. "iat": 1727619834,
     5. "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
     6. "events": {
     7. "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
     8. "subject": {
     9. "extra": "<触发事件用户的OpenID>",
     10. "iss": "id.cloud.huawei.com",
     11. "sub": "<触发事件用户的UnionID>",
     12. "subject_type": "iss_sub"
     13. }
     14. }
     15. }
     16. }
     ```

     消息示例：用户取消应用的授权

     ```
     1. {
     2. "iss": "id.cloud.huawei.com",
     3. "aud": "<Client ID>",
     4. "iat": 1750403661,
     5. "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
     6. "events": {
     7. "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
     8. "subject": {
     9. "extra": "<触发事件用户的OpenID>",
     10. "iss": "id.cloud.huawei.com",
     11. "sub": "<触发事件用户的UnionID>",
     12. "subject_type": "iss_sub"
     13. },
     14. "scopes": [
     15. "phone",
     16. "userConsent",
     17. "openid",
     18. "email"
     19. ]
     20. }
     21. }
     22. }
     ```

     消息示例：用户授权手机号变更

     ```
     1. {
     2. "iss": "id.cloud.huawei.com",
     3. "aud": "<Client ID>",
     4. "iat": 1750385669,
     5. "jti": "c27c197ba5c94081aa32b8dbc52389f3",
     6. "events": {
     7. "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
     8. "subject": {
     9. "extra": "<触发事件用户的OpenID>",
     10. "iss": "id.cloud.huawei.com",
     11. "sub": "<触发事件用户的UnionID>",
     12. "subject_type": "iss_sub"
     13. }
     14. }
     15. }
     16. }
     ```
   * **JSON数组格式消息体**

     消息示例：用户注销华为账号

     ```
     1. [
     2. {
     3. "iss": "id.cloud.huawei.com",
     4. "aud": "<Client ID>",
     5. "iat": 1750385669,
     6. "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
     7. "events": {
     8. "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
     9. "subject": {
     10. "extra": "<触发事件用户的OpenID>",
     11. "iss": "id.cloud.huawei.com",
     12. "sub": "<触发事件用户的UnionID>",
     13. "subject_type": "iss_sub"
     14. }
     15. }
     16. }
     17. },
     18. {
     19. "iss": "id.cloud.huawei.com",
     20. "aud": "<Client ID>",
     21. "iat": 1750385669,
     22. "jti": "6672ed7d5c5e4c3c92f343ecac40f325",
     23. "events": {
     24. "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
     25. "subject": {
     26. "extra": "<触发事件用户的OpenID>",
     27. "iss": "id.cloud.huawei.com",
     28. "sub": "<触发事件用户的UnionID>",
     29. "subject_type": "iss_sub"
     30. }
     31. }
     32. }
     33. }
     34. ]
     ```

     消息示例：用户取消应用的授权

     ```
     1. [
     2. {
     3. "iss": "id.cloud.huawei.com",
     4. "aud": "<Client ID>",
     5. "iat": 1750403661,
     6. "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
     7. "events": {
     8. "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
     9. "subject": {
     10. "extra": "<触发事件用户的OpenID>",
     11. "iss": "id.cloud.huawei.com",
     12. "sub": "<触发事件用户的UnionID>",
     13. "subject_type": "iss_sub"
     14. },
     15. "scopes": [
     16. "phone",
     17. "userConsent",
     18. "openid",
     19. "email"
     20. ]
     21. }
     22. }
     23. },
     24. {
     25. "iss": "id.cloud.huawei.com",
     26. "aud": "<Client ID>",
     27. "iat": 1750403661,
     28. "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb57",
     29. "events": {
     30. "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
     31. "subject": {
     32. "extra": "<触发事件用户的OpenID>",
     33. "iss": "id.cloud.huawei.com",
     34. "sub": "<触发事件用户的UnionID>",
     35. "subject_type": "iss_sub"
     36. },
     37. "scopes": [
     38. "phone",
     39. "userConsent",
     40. "openid",
     41. "email"
     42. ]
     43. }
     44. }
     45. }
     46. ]
     ```

     消息示例：用户授权手机号变更

     ```
     1. [
     2. {
     3. "iss": "id.cloud.huawei.com",
     4. "aud": "<Client ID>",
     5. "iat": 1750385669,
     6. "jti": "c27c197ba5c94081aa32b8dbc52389f3",
     7. "events": {
     8. "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
     9. "subject": {
     10. "extra": "<触发事件用户的OpenID>",
     11. "iss": "id.cloud.huawei.com",
     12. "sub": "<触发事件用户的UnionID>",
     13. "subject_type": "iss_sub"
     14. }
     15. }
     16. }
     17. },
     18. {
     19. "iss": "id.cloud.huawei.com",
     20. "aud": "<Client ID>",
     21. "iat": 1750385669,
     22. "jti": "c27c197ba5c94081aa32b8dbc52389f4",
     23. "events": {
     24. "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
     25. "subject": {
     26. "extra": "<触发事件用户的OpenID>",
     27. "iss": "id.cloud.huawei.com",
     28. "sub": "<触发事件用户的UnionID>",
     29. "subject_type": "iss_sub"
     30. }
     31. }
     32. }
     33. }
     34. ]
     ```

   其中，各字段含义如下：

   | 参数 | 描述 |
   | --- | --- |
   | aud | Client ID（与[订阅用户信息变更](subscribe-process-userinfo-change.md#订阅用户信息变更)中提供的Client ID一致）。 |
   | iss | 消息投递者标识，固定值“id.cloud.huawei.com”。 |
   | iat | 生成该事件的UTC时间戳（秒级）。 |
   | jti | 唯一随机字符串，用于标识此消息体，开发者可根据此字段来识别重投消息体。 |
   | events | 用户信息变更事件与事件消息体，格式为json。key是用户信息变更事件类型，value为其对应事件消息信息。 |
   | subject | 用户信息变更事件对应的消息体，格式为json，包含字段说明如下：  - sub：触发事件用户的UnionID（用户在同一个开发者下的所有应用中，此值唯一）。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。  - subject\_type：固定为“iss\_sub”。  - extra：触发事件用户的OpenID（用户在同一个应用中，此值唯一）。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。  - iss：标识消息投递者，固定为“id.cloud.huawei.com”。 |
   | scopes | 取消授权的scope列表，格式为json数组。在事件类型为【https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked】时才存在此字段。 |
