---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-common
title: 公共说明
breadcrumb: API参考 > 应用服务 > Account Kit（华为账号服务） > REST API > 公共说明
category: harmonyos-references
scraped_at: 2026-04-28T08:16:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42e26f216c1445f6ff52796db015f10209cde6810816ce986529f501a0798258
---

## TLS协议及加密套件

| TLS版本 | 加密套件 **（IANA名称）** |
| --- | --- |
| TLS1.2 | TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384  TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256  TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384  TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256 |

## 示例代码环境配置

REST API接口提供的示例代码，运行时需要进行如下配置：

* 配置maven依赖

  ```
  1. <dependencies>
  2. <dependency>
  3. <groupId>com.alibaba.fastjson2</groupId>
  4. <artifactId>fastjson2</artifactId>
  5. <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
  6. </dependency>
  7. <dependency>
  8. <groupId>org.apache.httpcomponents</groupId>
  9. <artifactId>httpclient</artifactId>
  10. <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
  11. </dependency>
  12. <dependency>
  13. <groupId>org.projectlombok</groupId>
  14. <artifactId>lombok</artifactId>
  15. <version>1.18.26</version> <!--此处替换为您项目需要的版本-->
  16. </dependency>
  17. <dependency>
  18. <groupId>ch.qos.logback</groupId>
  19. <artifactId>logback-classic</artifactId>
  20. <version>1.2.11</version> <!--此处替换为您项目需要的版本-->
  21. </dependency>
  22. </dependencies>
  ```
* 引入CallUtils工具类（请将此工具类与API的示例代码放于同一路径下，如不在同一路径，请手动到API的示例代码添加import）

  ```
  1. import com.alibaba.fastjson2.JSON;
  2. import com.alibaba.fastjson2.JSONObject;
  3. import lombok.extern.slf4j.Slf4j;
  4. import org.apache.http.Header;
  5. import org.apache.http.HttpEntity;
  6. import org.apache.http.HttpStatus;
  7. import org.apache.http.client.config.RequestConfig;
  8. import org.apache.http.client.methods.CloseableHttpResponse;
  9. import org.apache.http.client.methods.HttpUriRequest;
  10. import org.apache.http.config.Registry;
  11. import org.apache.http.config.RegistryBuilder;
  12. import org.apache.http.conn.socket.ConnectionSocketFactory;
  13. import org.apache.http.conn.socket.PlainConnectionSocketFactory;
  14. import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
  15. import org.apache.http.entity.ContentType;
  16. import org.apache.http.entity.StringEntity;
  17. import org.apache.http.impl.client.CloseableHttpClient;
  18. import org.apache.http.impl.client.HttpClients;
  19. import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
  20. import org.apache.http.util.EntityUtils;
  21. import javax.net.ssl.SSLContext;
  22. import javax.net.ssl.TrustManagerFactory;
  23. import java.io.IOException;
  24. import java.security.KeyManagementException;
  25. import java.security.KeyStore;
  26. import java.security.KeyStoreException;
  27. import java.security.NoSuchAlgorithmException;
  28. import java.util.Map;
  29. import java.util.Objects;
  30. import java.util.function.BiFunction;

  32. /**
  33. * HTTP调用工具类
  34. */
  35. @Slf4j
  36. public class CallUtils {
  37. public static String remoteCall(HttpUriRequest request) throws IOException {
  38. return remoteCall(request, CallUtils::nspErrorHandler);
  39. }

  41. public static String remoteCallOAuth(HttpUriRequest request) throws IOException {
  42. return remoteCall(request, CallUtils::oauthErrorHandler);
  43. }

  45. public static String remoteCallAccountApi(HttpUriRequest request) throws IOException {
  46. return remoteCall(request, CallUtils::accountApiErrorHandler);
  47. }

  49. public static <E extends Exception> String remoteCall(HttpUriRequest request,
  50. BiFunction<CloseableHttpResponse, String, E> errorHandler) throws IOException, E {
  51. try (CloseableHttpResponse response = getClient().execute(request)) {
  52. HttpEntity responseEntity = response.getEntity();
  53. String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
  54. EntityUtils.consume(responseEntity);
  55. if (errorHandler != null) {
  56. E error = errorHandler.apply(response, ret);
  57. if (null != error) {
  58. throw error;
  59. }
  60. }
  61. return ret;
  62. }
  63. }

  65. public static JSONObject toJsonObject(String json) {
  66. return (JSONObject) JSON.parse(json);
  67. }

  69. public static StringEntity wrapJsonEntity(Object obj) {
  70. return new StringEntity(CallUtils.toJsonString(obj), ContentType.create("application/json", "UTF-8"));
  71. }

  73. public static String toJsonString(Object obj) {
  74. return JSON.toJSONString(obj);
  75. }

  77. public static IOException nspErrorHandler(CloseableHttpResponse response, String rawBody) {
  78. int statusCode = response.getStatusLine().getStatusCode();
  79. if (statusCode != 200) {
  80. return new IOException("call failed! status:" + statusCode + ", response data: " + rawBody);
  81. }
  82. Header nspStatus = response.getFirstHeader("NSP_STATUS");
  83. if (Objects.nonNull(nspStatus)) {
  84. return new IOException("call failed! nsp_status:" + nspStatus.getValue() + ", response data: " + rawBody);
  85. }
  86. return null;
  87. }

  89. public static IOException oauthErrorHandler(CloseableHttpResponse response, String rawBody) {
  90. int statusCode = response.getStatusLine().getStatusCode();
  91. // http状态码为200，请求成功
  92. if (statusCode == HttpStatus.SC_OK) {
  93. return null;
  94. }
  95. // http状态码非200，解析响应的body，业务视情况进行处理
  96. Map<String, Object> errorResponseBody = CallUtils.toJsonObject(rawBody);
  97. // 业务响应主错误码
  98. Object error = errorResponseBody.get("error");
  99. // 业务响应子错误码
  100. Object subError = errorResponseBody.get("sub_error");
  101. // 业务可根据返回的主+子错误码进行自己的业务处理；例：错误码不为空，抛出异常
  102. if (Objects.nonNull(error) && Objects.nonNull(subError)) {
  103. return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
  104. }
  105. return null;
  106. }

  108. public static IOException accountApiErrorHandler(CloseableHttpResponse response, String rawBody) {
  109. int statusCode = response.getStatusLine().getStatusCode();
  110. // http状态码不是200，请求失败
  111. if (statusCode != 200) {
  112. return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
  113. }
  114. // http状态码为200，解析响应的body，判断业务错误码
  115. JSONObject errorResponseBody = CallUtils.toJsonObject(rawBody);
  116. // 业务响应码
  117. Integer resultCode = errorResponseBody.getInteger("resultCode");
  118. // resultCode为0表示成功，非0表示失败
  119. if (Objects.nonNull(resultCode) && resultCode != 0) {
  120. return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
  121. }
  122. return null;
  123. }

  125. private static CloseableHttpClient getClient() {
  126. PoolingHttpClientConnectionManager connectionManager = buildConnectionManager(
  127. new String[] {"TLSv1.2"}, new String[] {
  128. "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
  129. "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
  130. });
  131. connectionManager.setMaxTotal(400);
  132. connectionManager.setDefaultMaxPerRoute(400);
  133. RequestConfig config = RequestConfig.custom()
  134. .setConnectionRequestTimeout(100)
  135. .setRedirectsEnabled(false)
  136. .build();
  137. return HttpClients.custom()
  138. .useSystemProperties()
  139. .setConnectionManager(connectionManager)
  140. .setDefaultRequestConfig(config)
  141. .build();
  142. }

  144. private static PoolingHttpClientConnectionManager buildConnectionManager(String[] supportedProtocols,
  145. String[] supportedCipherSuites) {
  146. PoolingHttpClientConnectionManager connectionManager = null;
  147. try {
  148. SSLContext sc = SSLContext.getInstance("TLSv1.2");
  149. TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
  150. tmf.init((KeyStore) null);
  151. sc.init(null, tmf.getTrustManagers(), null);
  152. SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sc, supportedProtocols,
  153. supportedCipherSuites, SSLConnectionSocketFactory.getDefaultHostnameVerifier());
  154. Registry<ConnectionSocketFactory> registry = RegistryBuilder.<ConnectionSocketFactory>create()
  155. .register("http", new PlainConnectionSocketFactory())
  156. .register("https", sslsf)
  157. .build();
  158. connectionManager = new PoolingHttpClientConnectionManager(registry);
  159. } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
  160. log.error("build connect manager failed", e);
  161. }
  162. return connectionManager;
  163. }
  164. }
  ```
