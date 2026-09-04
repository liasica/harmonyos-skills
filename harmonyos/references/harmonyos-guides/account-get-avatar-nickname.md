---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-avatar-nickname
title: 获取头像昵称
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取头像昵称
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:36e417217cec9f037db831b4d8afca791b2bee4d67eef29f96f060d0c5d4dba3
---

## 场景介绍

当应用需要获取用户头像昵称信息，可使用Account Kit提供的头像昵称授权能力，用户允许应用获取头像昵称后，可快速完成个人信息填写。以下对Account Kit提供的头像昵称授权能力进行介绍。此外，开发者也可通过场景化控件中的[选择头像Button](scenario-fusion-button-chooseavatar.md)获取用户头像。

**图1** 手机端获取头像昵称（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/DB0CPUYESKGQBEtJu7dA3g/zh-cn_image_0000002712245010.png "点击放大")

**图2** Wearable设备获取头像昵称（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/QkmaenHkQlOf_wn10W1Byw/zh-cn_image_0000002742003959.png "点击放大")

## 约束与限制

获取头像昵称能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/OVyMLdGmTXSOJ9x58x_uwg/zh-cn_image_0000002712404970.png)

流程说明：

1. 应用传对应scope调用授权API请求获取用户头像昵称。
2. 如用户已给应用授权，则开发者能直接获取用户头像昵称。
3. 如用户未授权，则授权请求会拉起授权页面，在用户确认授权后，开发者能获取到用户头像昵称。
4. 获取到头像url信息，开发者可以通过该url下载并使用用户头像。

## 接口说明

获取头像昵称关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-authentication.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)(): [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest) | 获取授权请求对象接口，通过在[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)对象中传入头像昵称的scope：profile及Authorization Code的permission：serviceauthcode，即可在授权结果中获取到用户头像昵称和Authorization Code。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建授权请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行授权操作。  头像昵称，可从[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)的子类[AuthorizationWithHuaweiIDResponse](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidresponse)中解析，具体解析方法请参考[客户端开发](account-get-avatar-nickname.md#客户端开发)的示例代码。 |

**注意** 

1.上述接口需在页面或自定义组件生命周期内调用。

2.未设置昵称默认返回华为账号绑定的匿名手机号/邮箱。

3.当用户更新头像后，原用户头像链接会立即失效。为确保头像正常显示，建议先将头像下载保存后再使用，避免因用户头像链接失效而影响业务流程。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

**注意** 

若未正确配置公钥指纹，将报错[1001500001 应用指纹证书校验失败](account-faq-1.md)。

## 开发步骤

### 客户端开发

1. 导入[authentication](../harmonyos-references/account-api-authentication.md)模块及相关公共模块。

   ```typescript
   import { authentication } from '@kit.AccountKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { util } from '@kit.ArkTS';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建授权请求并设置参数。

   ```typescript
   // 创建授权请求，并设置参数
   const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   // 获取头像昵称需要传如下scope
   authRequest.scopes = ['profile'];
   // 若开发者需要进行服务端开发以获取头像昵称，则需传如下permission获取authorizationCode
   authRequest.permissions = ['serviceauthcode'];
   // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   authRequest.forceAuthorization = true;
   // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
   authRequest.state = util.generateRandomUUID();
   ```
3. 调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)方法执行授权请求，并处理授权结果，从授权结果中解析出头像昵称和Authorization Code。

   ```typescript
   // 执行授权请求
   try {
     // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
     const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
     controller.executeRequest(authRequest).then((data) => {
       const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
       const state = authorizationWithHuaweiIDResponse?.state;
       // state为空时，归一化处理为空字符串
       const normalizedRequestState = authRequest.state || '';
       const normalizedState = state || '';
       if (normalizedRequestState !== normalizedState) {
         hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
       const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
       const avatarUri = authorizationWithHuaweiIDCredential?.avatarUri;
       const nickName = authorizationWithHuaweiIDCredential?.nickName;
       // 开发者处理avatarUri, nickName
       const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
       // 涉及服务端开发以获取头像昵称场景，开发者处理authorizationCode
       // ...
     }).catch((err: BusinessError) => {
       // ...
       dealAllError(err);
     });
   } catch (error) {
     dealAllError(error);
   }
   ```

   ```typescript
   // 错误处理
   function dealAllError(error: BusinessError): void {
     hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
     // 在应用获取头像昵称场景下，涉及UI交互时，建议按照如下错误码指导提示用户
     if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
       // 用户未登录华为账号，请登录华为账号并重试
     } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
       // 网络错误，请检查当前网络状态并重试
     } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
       // 用户取消授权
     } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
       // 系统服务异常，请稍后重试
     } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
       // 重复请求，应用无需处理
     } else {
       // 获取用户信息失败，请稍后重试
     }
   }

   export enum ErrorCode {
     // 账号未登录
     ERROR_CODE_LOGIN_OUT = 1001502001,
     // 网络错误
     ERROR_CODE_NETWORK_ERROR = 1001502005,
     // 用户取消授权
     ERROR_CODE_USER_CANCEL = 1001502012,
     // 系统服务异常
     ERROR_CODE_SYSTEM_SERVICE = 12300001,
     // 重复请求
     ERROR_CODE_REQUEST_REFUSE = 1001500002
   }
   ```

### 服务端开发（可选）

开发者根据业务需要选择是否进行服务端开发，客户端返回的头像昵称数据同步存在延迟，如果对头像昵称时效性要求较高，建议通过服务端获取。

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#接口原型)获取用户信息，从用户信息中获取用户头像昵称。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](../harmonyos-references/account-api-obtain-refresh-token.md#接口原型)向华为账号服务器请求获取新的Access Token。

   **说明** 

   1. 当Access Token失效时，若您不使用Refresh Token向账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，业务可重新登录授权获取Authorization Code，向账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](../harmonyos-references/account-api-obtain-refresh-token.md#错误码)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
