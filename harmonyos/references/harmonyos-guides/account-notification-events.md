---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-notification-events
title: Account Kit通知事件
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit通知事件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ecc4e6c99884bb79956868a62c6470531d181b951a7d06165b19da45a074268a
---

## 概述

华为账号提供了多种通知事件机制，方便应用感知账号状态变化、系统未成年人模式变化和用户信息变更。事件类型包含：

| 事件类型 | 事件分类 | 描述 |
| --- | --- | --- |
| 华为账号登录/登出事件 | 客户端事件 | 应用在前台时通过订阅系统公共事件，实时感知系统华为账号的登录/登出状态。 |
| 系统未成年人模式开启/关闭事件 | 客户端事件 | 应用在前台时通过订阅系统公共事件，实时感知系统未成年人模式的开启/关闭状态。 |
| 用户信息变更事件 | 服务端事件 | 华为账号服务器向应用服务端发送通知，告知用户及其账户信息的重要变更，如用户取消授权、注销账号、手机号变更等。 |

## 华为账号登录/登出事件

### 场景介绍

应用在前台时可以订阅Account Kit提供的华为账号登录/登出广播事件，来感知华为账号的登录状态，实现用户登录/登出应用的逻辑。应用也可通过[getHuaweiIDState](../harmonyos-references/account-api-authentication.md#gethuaweiidstate)实时查询华为账号登录状态。

### 事件说明

以下是华为账号登录/登出发送的广播事件。

| 事件名称 | 描述 |
| --- | --- |
| [COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN](../harmonyos-references/commoneventmanager-definitions.md#common_event_distributed_account_login) | 表示分布式账号登录成功的动作。华为账号登录成功也会发送此广播事件。 |
| [COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT](../harmonyos-references/commoneventmanager-definitions.md#common_event_distributed_account_logout) | 表示分布式账号登出成功的动作。华为账号登出成功也会发送此广播事件。 |

### 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

### 开发步骤

1. 导入[commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 创建订阅者，并处理订阅结果。

   ```typescript
   // 订阅者信息
   const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
     events: [commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN,
       commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT]
   };

   // 定义订阅者，如开发者使用await改写createSubscriber方法，需要把此变量定义到全局(struct外层)
   let subscriber: commonEventManager.CommonEventSubscriber | null = null;
   // 创建订阅者
   commonEventManager.createSubscriber(subscribeInfo)
     .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
       subscriber = commonEventSubscriber;
       // 订阅公共事件
       commonEventManager.subscribe(subscriber,
         (error: BusinessError, data: commonEventManager.CommonEventData) => {
           if (error) {
             hilog.error(0x0000, 'testTag',
               `Failed to subscribe, code is ${error.code}, message is ${error.message}`);
           } else {
             hilog.info(0x0000, 'testTag', 'Succeeded in subscribing.');
             if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN) {
               // 订阅到华为账号登录事件
             }
             if (data.event === commonEventManager.Support.COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT) {
               // 订阅到华为账号登出事件
             }
           }
         });
     })
     .catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', `Failed to createSubscriber. Code: ${err.code}, message: ${err.message}`);
     });
   ```

## 系统未成年人模式开启/关闭事件

### 场景介绍

应用在前台时可以订阅Account Kit提供的系统未成年人模式公共事件，来感知系统未成年人模式的开启/关闭状态，以提供适龄内容。

### 事件说明

以下是系统未成年人模式开启/关闭发送的广播事件。

| 事件名称 | 值 | 描述 |
| --- | --- | --- |
| [COMMON\_EVENT\_MINORSMODE\_ON](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_on12) | usual.event.MINORSMODE\_ON | 表示系统未成年人模式开启事件。 |
| [COMMON\_EVENT\_MINORSMODE\_OFF](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_off12) | usual.event.MINORSMODE\_OFF | 表示系统未成年人模式关闭事件。 |

**说明** 

主动开启系统未成年人模式（PC/2in1设备暂不支持从控制中心开启系统未成年人模式），当前设备会发送系统未成年人模式开启事件。

### 开发前提

请先参考“开发准备”的[配置签名和指纹](account-sign-fingerprints.md)章节，通过自动签名方式完成签名信息的配置。请注意，该接口无需配置公钥指纹、Client ID，也无需申请账号权限。

### 开发步骤

1. 导入[commonEventManager](../harmonyos-references/js-apis-commoneventmanager.md)模块及相关公共模块。

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 创建订阅者，订阅系统未成年人模式开启或关闭事件。推荐在应用Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中调用。

   ```typescript
   // 订阅者信息
   const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
     events: [commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON,
       commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF]
   };

   // 定义订阅者，如开发者使用await改写createSubscriber方法，需要把此变量定义到全局(struct外层)
   let subscriber: commonEventManager.CommonEventSubscriber | null = null;
   // 创建订阅者
   commonEventManager.createSubscriber(subscribeInfo)
     .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
       // 这里获取到commonEventSubscriber对象需要暂存，用于后续事件回调。不可直接使用，否则会出现事件回调不生效的情况
       subscriber = commonEventSubscriber;
       // 订阅公共事件
       commonEventManager.subscribe(subscriber,
         (error: BusinessError, data: commonEventManager.CommonEventData) => {
           if (error) {
             dealCommonEventAllError(error);
             return;
           }
           if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON) {
             // 订阅到开启事件，可以调用获取年龄段的接口，根据年龄段刷新内容展示，同时如开发者有缓存年龄段或系统未成年人模式开启状态，则需要刷新缓存
             return;
           }
           if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF) {
             // 订阅到关闭事件，关闭当前应用的未成年人模式，刷新应用内容展示，取消年龄限制，如开发者有缓存系统未成年人模式开启状态，则需要刷新缓存
           }
         });
     })
     .catch((error: BusinessError) => {
       dealCommonEventAllError(error);
     });
   ```

   ```typescript
   function dealCommonEventAllError(error: BusinessError): void {
     hilog.error(0x0000, 'testTag', `Failed to subscribe. Code: ${error.code}, message: ${error.message}`);
   }
   ```

## 用户信息变更事件

### 场景介绍

通过订阅用户信息变更，您可以接收有关用户及其账户的重要更新。当用户及其账户信息发生变更时，华为账号服务器会发送通知到应用服务端，应用服务端可以根据通知消息进行自身业务处理。

### 事件说明

| 消息名称 | 事件类型 | 事件描述 |
| --- | --- | --- |
| tokens-revoked | https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked | 用户取消应用的授权 |
| account-purged | https://schemas.openid.net/secevent/risc/event-type/account-purged | 用户注销华为账号 |
| phone-modified | https://schemas.openid.net/secevent/oauth/event-type/phone-modified | 用户授权手机号变更 |

### 订阅用户信息变更

订阅步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/QUACA7stRXOmd_ZnE-sAMw/zh-cn_image_0000002706834774.png)
2. 在项目列表选择项目。
3. 进入“项目设置 > 开放能力管理”页面，点击“RISC”对应的“管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/CvmiL9fiSHib3TsCfoyHQw/zh-cn_image_0000002736313881.png)
4. 点击“启用”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/PufjgBUWQEa6v6hSC6lv4g/zh-cn_image_0000002706674840.png)
5. 点击“订阅通知”按钮，在弹窗中配置“回调地址”及“订阅范围”，然后点击“提交”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/lF9w0tWISLCJVlahA0M38w/zh-cn_image_0000002736433927.png)

   **说明** 

   回调地址：在开启订阅通知后，若华为用户信息发生变更，会发送通知消息到该地址。

   订阅范围：订阅的用户信息变更事件，详见[事件说明](account-notification-events.md#事件说明-2)。

### 处理通知消息

华为账号服务器向开发者应用服务端投递消息。开发者应用服务端接收到消息后需要先对消息头中的令牌进行验签，确保消息的完整有效性后解析并获取用户信息变更事件详情。具体步骤如下：

1. **验证消息头中的令牌签名。**

   您可通过任何JWT库（例如：[jwt.io](https://jwt.io/introduction/)）对其进行解析与验证。

   无论使用哪种库，您均需完成如下操作：

   1. 调用接口https://risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration，获取发行者标识（issuer）与签名密钥证书URI（jwks\_uri）。
   2. 通过依赖的JWT库，对消息头中的令牌进行解析，获取签名的KeyId。
   3. 通过签名的KeyId，从签名密钥证书URI中获取到JWT签名的公钥。
   4. 校验JWT签名中的aud与[订阅用户信息变更](account-notification-events.md#订阅用户信息变更)中提供的Client ID一致。
   5. 校验JWT签名中的issuer与发行者标识（issuer）一致。

   具体验签逻辑，请参考如下示例代码：

   Maven依赖配置

   ```xml
   <dependencies>
      <dependency>
         <groupId>com.github.ben-manes.caffeine</groupId>
         <artifactId>caffeine</artifactId>
         <version>2.9.3</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>   
         <groupId>com.auth0</groupId> 
         <artifactId>jwks-rsa</artifactId>
         <version>0.21.2</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>io.jsonwebtoken</groupId>
         <artifactId>jjwt-impl</artifactId>
         <version>0.11.5</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>io.jsonwebtoken</groupId>
         <artifactId>jjwt-jackson</artifactId>
         <version>0.11.5</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>com.alibaba.fastjson2</groupId>
         <artifactId>fastjson2</artifactId>
         <version>2.0.51</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>org.apache.httpcomponents</groupId>
         <artifactId>httpclient</artifactId>
         <version>4.5.6</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>org.projectlombok</groupId>
         <artifactId>lombok</artifactId>
         <version>1.18.26</version> <!--此处替换为您项目需要的版本-->
      </dependency>
      <dependency>
         <groupId>ch.qos.logback</groupId>
         <artifactId>logback-classic</artifactId>
         <version>1.2.11</version> <!--此处替换为您项目需要的版本-->
      </dependency>
   </dependencies>
   ```

   Java验签代码示例

   ```java
   import com.alibaba.fastjson2.JSON;
   import com.alibaba.fastjson2.JSONObject;
   import com.auth0.jwk.JwkProvider;
   import com.auth0.jwk.UrlJwkProvider;
   import com.github.benmanes.caffeine.cache.CacheLoader;
   import com.github.benmanes.caffeine.cache.Caffeine;
   import com.github.benmanes.caffeine.cache.LoadingCache;
   import io.jsonwebtoken.Claims;
   import io.jsonwebtoken.IncorrectClaimException;
   import io.jsonwebtoken.JwsHeader;
   import io.jsonwebtoken.Jwt;
   import io.jsonwebtoken.JwtParser;
   import io.jsonwebtoken.Jwts;
   import io.jsonwebtoken.SigningKeyResolver;
   import io.jsonwebtoken.security.SignatureException;
   import lombok.Data;
   import lombok.extern.slf4j.Slf4j;
   import org.apache.http.HttpEntity;
   import org.apache.http.HttpStatus;
   import org.apache.http.client.config.RequestConfig;
   import org.apache.http.client.methods.CloseableHttpResponse;
   import org.apache.http.client.methods.HttpGet;
   import org.apache.http.config.Registry;
   import org.apache.http.config.RegistryBuilder;
   import org.apache.http.conn.socket.ConnectionSocketFactory;
   import org.apache.http.conn.socket.PlainConnectionSocketFactory;
   import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
   import org.apache.http.impl.client.CloseableHttpClient;
   import org.apache.http.impl.client.HttpClients;
   import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
   import org.apache.http.util.EntityUtils;
   import org.checkerframework.checker.nullness.qual.NonNull;
   import org.checkerframework.checker.nullness.qual.Nullable;
   import javax.net.ssl.SSLContext;
   import javax.net.ssl.TrustManagerFactory;
   import java.io.IOException;
   import java.net.URL;
   import java.security.Key;
   import java.security.KeyManagementException;
   import java.security.KeyStore;
   import java.security.KeyStoreException;
   import java.security.NoSuchAlgorithmException;
   import java.security.PublicKey;
   import java.util.Objects;
   import java.util.concurrent.TimeUnit;

   /**
    * 订阅和处理用户信息变更
    */
   @Slf4j
   public class RiscDemo {
       /**
        * 公开配置信息地址
        */
       private static final String PUBLIC_CONFIGURATION_URL = "https://risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration";

       /**
        * 公开信息缓存
        */
       private final LoadingCache<String, PublicConfiguration> publicConfigurationCache = Caffeine.newBuilder()
               .expireAfterWrite(1, TimeUnit.DAYS)
               .build(key -> {
                   HttpGet request = new HttpGet(PUBLIC_CONFIGURATION_URL);
                   try (CloseableHttpResponse response = getClient().execute(request)) {
                       HttpEntity responseEntity = response.getEntity();
                       String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
                       EntityUtils.consume(responseEntity);
                       int statusCode = response.getStatusLine().getStatusCode();
                       // http状态码不是200，抛出异常
                       if (statusCode != HttpStatus.SC_OK) {
                           throw new IOException("call failed! http status code: " + statusCode + ", response data: " + ret);
                       }
                       JSONObject configJson = (JSONObject) JSON.parse(ret);
                       if (configJson == null) {
                           throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
                       }
                       String issuer = configJson.getString("issuer");
                       String jwksUri = configJson.getString("jwks_uri");
                       if (Objects.isNull(issuer) || Objects.isNull(jwksUri)) {
                           throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
                       }
                       PublicConfiguration publicConfiguration = new PublicConfiguration();
                       publicConfiguration.setIssuer(issuer);
                       publicConfiguration.setJwksUri(jwksUri);
                       return publicConfiguration;
                   }
               });

       /**
        * 公钥信息缓存
        */
       private final LoadingCache<String, PublicKey> publicKeyCache = Caffeine.newBuilder()
               .expireAfterWrite(1, TimeUnit.DAYS)
               .build(new CacheLoader<String, PublicKey>() {
                   @Override
                   public @Nullable PublicKey load(@NonNull String key) throws Exception {
                       PublicConfiguration publicConfiguration = getPublicConfiguration();
                       JwkProvider huaweiCerts = new UrlJwkProvider(new URL(publicConfiguration.getJwksUri()), null, null);
                       return huaweiCerts.get(key).getPublicKey();
                   }
               });

       /**
        * 调试方法入口
        * @param args main方法入参
        */
       public static void main(String[] args) {
           // 消息请求头中Authorization: Bearer <token>中的<token>
           String token = "<token>";
           // Client ID
           String clientId = "<Client ID>";
           Jwt<?, ?> jwt = new RiscDemo().validateSecurityEventToken(token, clientId);
           if (Objects.isNull(jwt)) {
               // 验签失败
               log.error("verify sign failed");
           } else {
               // 验签成功
               log.info("verify sign success");
           }
       }

       /**
        * 对Authorization头域中的token进行验签
        *
        * @param token    消息请求头中Authorization: Bearer <token>中的<token>
        * @param clientId clientId
        * @return 返回为null，则表示验签失败，否则表示验证成功
        */
       public Jwt<?, ?> validateSecurityEventToken(String token, String clientId) {
           try {
               // 公开配置信息中的issuer值
               String issuer = getPublicConfiguration().getIssuer();
               SigningKeyResolver signingKeyResolver = new SigningKeyResolver() {
                   private PublicKey getPublicKey(JwsHeader<?> jwsHeader) {
                       try {
                           return publicKeyCache.get(jwsHeader.getKeyId());
                       } catch (Exception e) {
                           throw new RuntimeException(e);
                       }
                   }
                   @Override
                   public Key resolveSigningKey(JwsHeader jwsHeader, Claims claims) {
                       return getPublicKey(jwsHeader);
                   }
                   @Override
                   public Key resolveSigningKey(JwsHeader jwsHeader, String s) {
                       return getPublicKey(jwsHeader);
                   }
               };
               // 验证并解析消息内容
               JwtParser parser = Jwts.parserBuilder()
                       .requireIssuer(issuer)
                       .requireAudience(clientId)
                       .setAllowedClockSkewSeconds(60)
                       .setSigningKeyResolver(signingKeyResolver)
                       .build();
               return parser.parse(token);
           } catch (IncorrectClaimException e) {
               // 消息的claim无效，针对异常进行处理（如：日志记录）
               log.error("claim invalid", e);
           } catch (SignatureException e) {
               // 验签失败，针对异常进行处理（如：日志记录）
               log.error("verify signature failed", e);
           } catch (Exception e) {
               // 其他异常，业务自行处理
               log.error("valid event token failed", e);
           }
           return null;
       }

       private PublicConfiguration getPublicConfiguration() {
           PublicConfiguration publicConfiguration = this.publicConfigurationCache.get("DEFAULT");
           if (publicConfiguration == null) {
               throw new IllegalArgumentException("public configuration get failed!");
           }
           return publicConfiguration;
       }

       private static CloseableHttpClient getClient() {
           PoolingHttpClientConnectionManager connectionManager = buildConnectionManager(
                   new String[] {"TLSv1.2"}, new String[] {
                           "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                           "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
                   });
           connectionManager.setMaxTotal(400);
           connectionManager.setDefaultMaxPerRoute(400);
           RequestConfig config = RequestConfig.custom()
                   .setConnectionRequestTimeout(100)
                   .setRedirectsEnabled(false)
                   .build();
           return HttpClients.custom()
                   .useSystemProperties()
                   .setConnectionManager(connectionManager)
                   .setDefaultRequestConfig(config)
                   .build();
       }

       private static PoolingHttpClientConnectionManager buildConnectionManager(String[] supportedProtocols,
                                                                                String[] supportedCipherSuites) {
           PoolingHttpClientConnectionManager connectionManager = null;
           try {
               SSLContext sc = SSLContext.getInstance("TLSv1.2");
               TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
               tmf.init((KeyStore) null);
               sc.init(null, tmf.getTrustManagers(), null);
               SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sc, supportedProtocols,
                       supportedCipherSuites, SSLConnectionSocketFactory.getDefaultHostnameVerifier());
               Registry<ConnectionSocketFactory> registry = RegistryBuilder.<ConnectionSocketFactory>create()
                       .register("http", new PlainConnectionSocketFactory())
                       .register("https", sslsf)
                       .build();
               connectionManager = new PoolingHttpClientConnectionManager(registry);
           } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
               log.error("build connect manager failed", e);
           }
           return connectionManager;
       }

       @Data
       static class PublicConfiguration {
           private String issuer;
           private String jwksUri;
       }
   }
   ```
2. **处理消息体。**

   * **JSON对象格式消息体**

     消息示例：用户注销华为账号

     ```json
     {
       "iss": "id.cloud.huawei.com",
       "aud": "<Client ID>",
       "iat": 1727619834,
       "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
       "events": {
         "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
           "subject": {
             "extra": "<触发事件用户的OpenID>",
             "iss": "id.cloud.huawei.com",
             "sub": "<触发事件用户的UnionID>",
             "subject_type": "iss_sub"
           }
         }
       }
     }
     ```

     消息示例：用户取消应用的授权

     ```json
     {
       "iss": "id.cloud.huawei.com",
       "aud": "<Client ID>",
       "iat": 1750403661,
       "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
       "events": {
         "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
           "subject": {
             "extra": "<触发事件用户的OpenID>",
             "iss": "id.cloud.huawei.com",
             "sub": "<触发事件用户的UnionID>",
             "subject_type": "iss_sub"
           },
           "scopes": [
             "phone",
             "userConsent",
             "openid",
             "email"
           ]
         }
       }
     }
     ```

     消息示例：用户授权手机号变更

     ```json
     {
       "iss": "id.cloud.huawei.com",
       "aud": "<Client ID>",
       "iat": 1750385669,
       "jti": "c27c197ba5c94081aa32b8dbc52389f3",
       "events": {
         "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
           "subject": {
             "extra": "<触发事件用户的OpenID>",
             "iss": "id.cloud.huawei.com",
             "sub": "<触发事件用户的UnionID>",
             "subject_type": "iss_sub"
           }
         }
       }
     }
     ```
   * **JSON数组格式消息体**

     消息示例：用户注销华为账号

     ```json
     [
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750385669,
         "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
         "events": {
           "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             }
           }
         }
       },
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750385669,
         "jti": "6672ed7d5c5e4c3c92f343ecac40f325",
         "events": {
           "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             }
           }
         }
       }
     ]
     ```

     消息示例：用户取消应用的授权

     ```json
     [
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750403661,
         "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
         "events": {
           "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             },
             "scopes": [
               "phone",
               "userConsent",
               "openid",
               "email"
             ]
           }
         }
       },
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750403661,
         "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb57",
         "events": {
           "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             },
             "scopes": [
               "phone",
               "userConsent",
               "openid",
               "email"
             ]
           }
         }
       }
     ]
     ```

     消息示例：用户授权手机号变更

     ```json
     [
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750385669,
         "jti": "c27c197ba5c94081aa32b8dbc52389f3",
         "events": {
           "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             }
           }
         }
       },
       {
         "iss": "id.cloud.huawei.com",
         "aud": "<Client ID>",
         "iat": 1750385669,
         "jti": "c27c197ba5c94081aa32b8dbc52389f4",
         "events": {
           "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
             "subject": {
               "extra": "<触发事件用户的OpenID>",
               "iss": "id.cloud.huawei.com",
               "sub": "<触发事件用户的UnionID>",
               "subject_type": "iss_sub"
             }
           }
         }
       }
     ]
     ```

   其中，各字段含义如下：

   | 参数 | 描述 |
   | --- | --- |
   | aud | Client ID（与[订阅用户信息变更](account-notification-events.md#订阅用户信息变更)中提供的Client ID一致）。 |
   | iss | 消息投递者标识，固定值“id.cloud.huawei.com”。 |
   | iat | 生成该事件的UTC时间戳（秒级）。 |
   | jti | 唯一随机字符串，用于标识此消息体，开发者可根据此字段来识别重投消息体。 |
   | events | 用户信息变更事件与事件消息体，格式为json。key是用户信息变更事件类型，value为其对应事件消息信息。 |
   | subject | 用户信息变更事件对应的消息体，格式为json，包含字段说明如下：  - sub：触发事件用户的UnionID（用户在同一个开发者下的所有应用中，此值唯一）。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。  - subject\_type：固定为“iss\_sub”。  - extra：触发事件用户的OpenID（用户在同一个应用中，此值唯一）。具体格式要求请参考[OpenID和UnionID的格式说明](account-faq-9.md)。  - iss：标识消息投递者，固定为“id.cloud.huawei.com”。 |
   | scopes | 取消授权的scope列表，格式为json数组。在事件类型为【https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked】时才存在此字段。 |
