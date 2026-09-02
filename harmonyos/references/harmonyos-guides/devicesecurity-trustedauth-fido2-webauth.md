---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-fido2-webauth
title: 网页场景接入数字盾（FIDO2）
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 网页场景接入数字盾（FIDO2）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62b1119f5bb352b497b617de59bea29f9a0856f3b6235be2042266d99c18c792
---

从API版本26.0.0开始，新增支持网页场景下的数字盾认证。

网页可以通过接入浏览器提供的WebAuthn接口，调用通行密钥（FIDO2）能力，结合网页自身配套实现的数字盾认证应用，可以支持网页完成数字盾认证，实现高安全性的网银登录、网银支付等场景。

## 场景介绍

用户在浏览器进行网银登录与支付时，常面临交易数据篡改、远程劫持等安全威胁。传统U盾虽能提供较高安全保障，但存在携带不便、需安装驱动程序等体验问题。为解决这一痛点，通行密钥（FIDO2）支持网页端数字盾认证，在确保网银支付安全性的同时优化了用户体验。

## 约束与限制

网页已满足通行密钥（FIDO2）能力的约束与限制条件，具体参见[约束与限制](onlineauthentication-passkey-intro.md#约束与限制)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/JpOvIvSbQVSgikMw_5kBZg/zh-cn_image_0000002736313407.jpg)

网页通过FIDO2实现数字盾认证时，需由调用方网页、浏览器、Online Authentication Kit（FIDO2）、配套的认证应用以及Device Security Kit共同协作完成。流程如下：

1. 调用方通过浏览器Webauthn接口发起通行密钥（FIDO2）认证请求，在并在请求中携带数字盾数据。
2. 浏览器将请求转发至FIDO2，FIDO2解析入参数据并检测到"scene"的值为"digitalShield"后进入数字盾分支流程。
3. FIDO2校验身份（[App Linking应用链接](applinking-introduction.md)域名、appId签名、rpId一致性）。
4. 校验通过后弹窗确认拉起数字盾应用并传递解析后的largeBlob数据。
5. 数字盾应用与Device Security Kit交互完成支付认证。
6. Device Security Kit将带有交易信息hash的authToken结果返回数字盾应用。
7. 数字盾应用将authToken和认证结果数据封装后返回FIDO2。
8. FIDO2对认证结果进行解析并完成authToken的校验。
9. 验证通过后FIDO2将认证结果返回浏览器。
10. 浏览器将结果转发回接口调用方。

## 开发准备

1. 使用通行密钥（FIDO2）注册与认证功能的开发准备及数字盾认证应用关联网页域名的配置方式，参见[通行密钥开发准备](onlineauthentication-passwordless-auth-preparation.md#通行密钥开发准备)。
2. 网页需配套实现数字盾扩展应用，才可完成完整网页数字盾认证能力，在应用内可自行定制数字盾TUI展示图标等。应用接入数字盾认证能力请参考[数字盾服务概述](devicesecurity-trustedauth-overview.md)。
3. 网页配套实现的数字盾认证应用需已上架应用市场，并在设备上安装；若应用未安装，将引导用户跳转至应用市场下载。

## 开发步骤

1. 注册通行密钥（FIDO2）。

   在使用网页数字盾认证能力前，网页需要为用户注册一个通行密钥（FIDO2）。网页可通过接入W3C WebAuthn标准接口，调用通行密钥（FIDO2）能力，为用户创建通行密钥（FIDO2）。

   ```javascript
   // 网页通过navigator.credentials.create注册通行密钥（FIDO2）
   const publicKeyCredentialCreationOptions = {
     publicKey: {
       challenge: new Uint8Array([...]),     // 服务器生成的challenge
       rp: { name: "Example xxx", id: "xxx.example.com" },     // 此处rp和user仅为示例代码，非真实数据
       user: {
         id: new Uint8Array([...]),
         name: "user@example.xxx.com",
         displayName: "Example User xxx"
       },
       pubKeyCredParams: [{ type: "public-key", alg: -7 }],
       authenticatorSelection: {
         authenticatorAttachment: "platform",
         userVerification: "required"
       }
     }
   };
   const credential = await navigator.credentials.create(publicKeyCredentialCreationOptions);
   ```
2. 发起FIDO2认证请求，在extensions中携带largeBlob。

   网页通过navigator.credentials.get接口发起认证时，在extensions的largeBlob.write字段中携带CBOR编码的数字盾数据。

   ```javascript
   // 构造数字盾largeBlob数据并CBOR编码，largeBlob大小不超过2kb
   const digShieldBlob = {
     scene: "digitalShield",                       // 固定为"digitalShield"，用于触发数字盾流程
     appIdentity: {
       packageName: "com.huawei.hms.digshield",    // 目标数字盾应用bundleName
       appId: "com.huawei.hms.digshield_Bxxxxxxxxx", // 目标应用签名信息，可在签名配置中查看
       rpId: "example.com"                          // 网站依赖方标识，须与认证请求rpId一致
     },
     authData: ""                                   // 附加认证数据，由业务自行定义，透传至数字盾应用
   };
   // 将digShieldBlob进行CBOR编码后转为二进制数据，赋值给largeBlob.write
   // 需使用第三方CBOR库完成编码
   const largeBlobWriteData = encodeCbor(digShieldBlob);

   // 通过navigator.credentials.get发起认证
   const publicKeyCredentialRequestOptions = {
     publicKey: {
       challenge: new Uint8Array([...]),     // 服务器生成的challenge
       rpId: "example.com",
       allowCredentials: [{
         type: "public-key",
         id: credential.rawId
       }],
       extensions: {
         largeBlob: {
           write: largeBlobWriteData
         }
       }
     }
   };
   const assertion = await navigator.credentials.get(publicKeyCredentialRequestOptions);
   ```

   **说明** 

   * 从网页跳转至数字盾认证应用时，系统会弹窗获取用户同意，以保证安全性。
   * 开发者需确保largeBlob.write.appIdentity字段传入的数据与数字盾应用的[App Linking应用链接](applinking-introduction.md)域名和appId签名一致，否则校验将不通过。
3. 处理认证结果。

   认证成功后，网页可从返回的PublicKeyCredential中获取认证结果，其中数字盾的扩展认证信息包含在clientExtensionResults的authData字段中：

   ```javascript
   // 从认证结果中获取数字盾扩展数据
   const clientExtensionResults = assertion.getClientExtensionResults();
   const digShieldAuthData = clientExtensionResults.authData;  // 数字盾认证结果数据

   // 将assertion响应（含id、response.signature、response.authenticatorData、
   // response.clientDataJSON等）发送至FIDO服务器进行验证
   ```

   **说明** 

   * 数字盾应用与FIDO2之间通过系统Ability拉起机制（startAbilityForResult）进行通信：FIDO2将largeBlob数据通过Want参数传递给数字盾应用，数字盾应用完成认证后通过AbilityResult返回认证结果。
   * 认证响应报文的组装格式请遵循W3C WebAuthn标准。
