---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-verification
title: 实名信息验证/授权场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 用户身份验证服务 > 实名信息验证/授权场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ebb9950506fe2b15dc77c700d865729074013ce9d1b0478563573082be93cf54
---

## 场景介绍

从5.1.1(19)版本开始，新增支持实名信息验证/授权场景。

例如应用/元服务登录、注册或账户认证等操作，开发者需要验证或获取用户实名信息时可接入实名信息验证/授权能力。

支持商户模型：不涉及

实名信息验证授权页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/DAJGSdDTSPKGHWM4fx10TQ/zh-cn_image_0000002706675180.png)

## 接入流程

华为支付实名信息验证授权接入流程如下：

| 步骤 | 说明 |
| --- | --- |
| 开发准备 | 请先完成开发准备后再进行下面的开发接入。  - [端侧应用配置](payment-config-app-identity-info.md)  - [用户信息验证授权接入准备](payment-real-name-preparations.md) |
| 接入实名信息验证/授权 | 根据实名信息验证/授权场景[开发步骤](payment-real-name-verification.md#开发步骤)完成接入。 |

## 业务流程

开发者通过接入Payment Kit实名信息验证授权能力，可以简便快捷地实现用户实名信息验证或获取用户授权后的实名信息（可二选一）。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/_mSoG9CySxii6xp7FkRWRg/zh-cn_image_0000002736434269.png)

### 实名信息验证

1. 开发者客户端收集用户实名信息请求开发者服务端发起实名信息预验证。
2. 开发者服务端请求Payment Kit服务端[实名信息预验证](../harmonyos-references/payment-api-common-verification-preverify.md)接口获取预验证ID（preVerifyId）。
3. Payment Kit服务端返回预验证ID给开发者服务端。
4. 开发者服务端返回预验证信息给开发者客户端。
5. 开发者客户端使用预验证ID调用[startRealNameVerification](../harmonyos-references/payment-realnameservice.md#startrealnameverification)接口拉起实名信息验证页面。
6. Payment Kit客户端展示验证信息。
7. 用户同意授权实名信息校验，Payment Kit客户端请求Payment Kit服务端处理校验。
8. Payment Kit服务端完成校验处理并返回校验结果给Payment Kit客户端展示给用户。
9. Payment Kit客户端同步返回**实名信息验证ID**给开发者客户端。
10. 开发者客户端使用实名信息校验ID请求开发者服务端查询实名信息校验结果。
11. 开发者服务端请求Payment Kit服务端[实名信息验证结果查询](../harmonyos-references/payment-api-common-verification-result.md)接口查询验证结果。
12. Payment Kit服务端返回实名信息验证结果给开发者服务端。
13. 开发者服务端将实名信息验证结果返回给开发者客户端，开发者客户端根据验证结果进行下一步业务处理。

### 实名信息授权

1. 开发者客户端如需要获取用户实名信息，可调用[startRealNameAuth](../harmonyos-references/payment-realnameservice.md#startrealnameauth)接口拉起实名信息授权页面。
2. Payment Kit客户端给用户展示实名信息授权页面。
3. 用户同意获取实名信息授权，Payment Kit客户端请求Payment Kit服务端校验授权处理
4. Payment Kit服务端完成校验处理并返回授权校验结果给Payment Kit客户端展示给用户。
5. Payment Kit客户端同步返回**实名信息授权ID**给开发者客户端。
6. 开发者客户端使用实名信息授权ID请求开发者服务端查询实名信息。
7. 开发者服务端请求Payment Kit服务端[实名信息授权结果查询](../harmonyos-references/payment-api-common-auth-result.md)接口查询用户实名信息授权结果及用户信息。
8. Payment Kit服务端会使用[开发者上传的公钥证书](payment-real-name-preparations.md#上传开发者公钥及下载华为公钥)进行隐私信息加密后返回给开发者服务端。
9. 开发者服务端使用配对的私钥证书进行解密后获取到用户实名信息。
10. 开发者服务端将用户实名信息返回给开发者客户端，开发者客户端根据业务需要，进行下一步处理。

## 接口说明

拉起用户实名信息验证授权页面接口。具体API说明详见[接口文档](../harmonyos-references/payment-realnameservice.md#startrealnameverification)。

| 接口名 | 描述 |
| --- | --- |
| startRealNameVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>; | 拉起用户实名信息验证页面。 |
| startRealNameAuth(context: common.UIAbilityContext | common.UIExtensionContext): Promise<string>; | 拉起用户实名信息授权页面。 |

## 开发步骤

### 实名信息验证

1. **发起实名信息预验证（服务器开发）**

   为保证API接口请求的安全性和可靠性需要获取应用级凭证，构建[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)作为开放API接口请求头后再发起请求。[PayDevAuth](../harmonyos-references/payment-model.md#paydevauth)定义示例代码如下：

   ```java
   @Data
   public class PayDevAuth {
       // 应用ID
       private String clientId;
       // 应用级token
       private String accessToken;
       private String traceId;
       private Long time;
       // 开发者加密公钥ID。用于华为对接口响应敏感字段加密
       private String developerEncKeyId;
       // 华为加密公钥ID。用于开发者对接口请求敏感字段加密
       private String petalpayEncKeyId;
       // 开发者验签公钥ID。用于华为对开发者加签的请求报文验签
       private String developerSignKeyId;
       // 华为验签公钥ID。用于开发者对华为加签的响应报文验签
       private String petalpaySignKeyId;
       private String headerSign;
       private String bodySign;
   }
   ```

   构建请求头信息示例代码如下：

   ```java
   // 获取accessToken
   private String getaccessToken(String clientId, String clientSecret) {
       HashMap<String, String> params = new HashMap<>();
       params.put("grant_type", "client_credentials");
       params.put("client_id", clientId);
       params.put("client_secret", clientSecret);
       Map<String, String> headers = new HashMap<>();
       headers.put("Content-Type", "application/x-www-form-urlencoded");
       // restfulClient为http请求客户端对象，请自行实现相关对象及方法的处理逻辑。
       ResponseEntity<Map> atRspResponseEntity = restfulClient.postForEntity(
           "https://oauth-login.cloud.huawei.com/oauth2/v3/token", params, null, headers, Map.class);
        return (String) atRspResponseEntity.getBody().get("access_token");
   }

   // 构建PayDevAuth请求头
   private String buildPayMercAuth(HashMap<String, String> body) {
       // 对body进行排序拼接
       String bodyStr = SignStringUtil.signString(body);
       // 构建 PayDevAuth 请求头
       PayDevAuth payDevAuth = new PayDevAuth();
       payDevAuth.setTraceId("tid" + System.currentTimeMillis());
       payDevAuth.setTime(System.currentTimeMillis());
       // 获取accessToken
       payDevAuth.setAccessToken(getAccessToken("clientId", "clientSecret"));
       // 获取签名priKey
       String priKey = "";
       // 请求体签名
       String bodySign = Sm2Utils.sign(Objects.requireNonNull(priKey, "The signing private key can’t null"), bodyStr);
       payDevAuth.setBodySign(bodySign);
       // 请求头签名
       String headerStr = ToStringUtil.signString(payDevAuth);
       String headerSign = Sm2Utils.sign(priKey, headerStr);
       payDevAuth.setHeaderSign(headerSign);
       return JsonUtils.obj2Json(payDevAuth);
   }
   ```

   请求[实名信息预验证](../harmonyos-references/payment-api-common-verification-preverify.md)接口获取预验证ID后返回给端侧拉起实名信息验证页面。参考以下示例代码：

   **说明** 

   人脸核身实人验证场景中，credentialIdNo、realName入参需要使用[SM2加密](payment-real-name-preparations.md#sm2加密示例代码参考)。

   ```java
   public String getPreVerifyId(String clientId, String clientSecret, String credentialIdNo, String realName, String openId)
       throws NoSuchAlgorithmException {
       HashMap<String, String> body = new HashMap<>();
       body.put("credentialType", "01");
       // 人脸核身实人验证场景
       body.put("credentialIdNo", getHashStr(credentialIdNo));
       body.put("realName", getHashStr(realName));
       body.put("openId", openId);
       HashMap<String, String> header = new HashMap<>();
       header.put("Content-Type", "application/json;charset=UTF-8");
       header.put("payDevAuth", buildPayMercAuth(body));
       // restfulClient为http请求客户端对象，请自行实现postForEntity请求方法。
       ResponseEntity<Map> responseEntity = restfulClient.postForEntity(
           "https://petalpay-developer.cloud.huawei.com.cn/api/v1/realname/verification/preverify", null, body, header, Map.class);
       return (String) responseEntity.getBody().get("preVerifyId");
   }

   public String getHashStr(String input) throws NoSuchAlgorithmException {
       byte[] encodedhash = MessageDigest.getInstance("SHA-512")
           .digest(input.getBytes(java.nio.charset.StandardCharsets.UTF_8));
       StringBuilder hexString = new StringBuilder();
       for (byte b : encodedhash) {
           String hex = Integer.toHexString(0xff & b);
           if (hex.length() == 1) {
               hexString.append('0');
           }
           hexString.append(hex);
       }
       return hexString.toString();
   }
   ```
2. **拉起实名信息验证（端侧开发）**

   开发者客户端使用后端服务返回的预验证ID作为参数调用[startRealNameVerification](../harmonyos-references/payment-realnameservice.md#startrealnameverification)接口拉起用户实名信息验证页面。当接口通过.then()方法返回时，则表示当前接口请求成功，通过.catch()方法返回表示接口请求失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/errorcode-payment.md)。示例代码如下：

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { realNameService } from '@kit.PaymentKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     requestStartVerifyRealNameInfoPromise() {
       // 请使用开发者真实的预验证ID（preVerifyId）
       let preVerifyId = '';
       realNameService.startRealNameVerification(this.context, preVerifyId)
         .then((verifyResultId: string) => {
           // 实名信息验证成功
           console.info(`succeeded in verifying, verifyResultId: ${verifyResultId}`);
         })
         .catch((error: BusinessError) => {
           // 实名信息验证失败
           console.error(`failed to verify, error.code: ${error.code}, error.message: ${error.message}`);
         });
     }

     build() {
       Column() {
         Button('requestStartVerifyRealNameInfoPromise')
           .type(ButtonType.Capsule)
           .width('50%')
           .margin(20)
           .onClick(() => {
             this.requestStartVerifyRealNameInfoPromise();
           })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
3. **查询实名信息验证结果（服务器开发）**

   请求[实名信息验证结果查询](../harmonyos-references/payment-api-common-verification-result.md)接口获取实名信息验证结果返回给客户端。

### 实名信息授权

1. **拉起实名信息授权（端侧开发）**

   开发者客户端调用[startRealNameAuth](../harmonyos-references/payment-realnameservice.md#startrealnameauth)接口拉起用户实名信息授权页面。当接口通过.then()方法返回时，则表示当前接口请求成功，通过.catch()方法返回表示接口请求失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/errorcode-payment.md)。示例代码如下：

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { realNameService } from '@kit.PaymentKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     requestStartRealNameAuthPromise() {
       realNameService.startRealNameAuth(this.context)
         .then((realNameAuthId: string) => {
           // 授权成功
           console.info(`succeeded in authorizing, realNameAuthId: ${realNameAuthId}`);
         })
         .catch((error: BusinessError) => {
           // 授权失败
           console.error(`failed to authorise, error.code: ${error.code}, error.message: ${error.message}`);
         });
     }

     build() {
       Column() {
         Button('requestStartRealNameAuthPromise')
           .type(ButtonType.Capsule)
           .width('50%')
           .margin(20)
           .onClick(() => {
             this.requestStartRealNameAuthPromise();
           })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
2. **查询实名信息授权结果（服务器开发）**

   请求[实名信息授权结果查询](../harmonyos-references/payment-api-common-verification-result.md)接口获取实名信息并使用publicKeyId配对的SM2私钥证书进行实名信息解密，根据业务需要返回给客户端。
