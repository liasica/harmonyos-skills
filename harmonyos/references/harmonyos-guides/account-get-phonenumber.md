---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-phonenumber
title: 获取手机号
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取手机号
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2c95516752ce969c049b4516d933bc610359e79a48b1b040eafddf4658215419
---

## 场景介绍

当应用需要获取用户手机号时，可使用Account Kit提供的手机号授权能力，向用户发起手机号授权申请，经用户同意授权后，获取到手机号并为用户提供相应服务。以下对Account Kit提供的手机号授权能力进行介绍，获取手机号功能还可使用场景化控件[快速验证手机号Button](scenario-fusion-button-getphonenumber.md)进行实现。

**说明** 

1. 对用户选择的华为账号绑定的手机号或者新增的手机号进行验证，**不保证是实时的验证**，**仅首次需要用户授权**。
2. 在应用账号已登录并绑定用户华为账号UnionID的情况下，应用可以在获取手机号等用户信息时根据实际业务场景判断是否需要提前校验当前应用账号绑定的UnionID与系统账号当前的UnionID是否一致。

**图1** 手机端获取手机号（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/0_DxpU68SMugIH0XeJ9p5w/zh-cn_image_0000002736433917.png "点击放大")

**图2** Wearable设备获取手机号（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/2i4mdGtdSdqjcO_BA8TIeA/zh-cn_image_0000002706834766.png "点击放大")

## 约束与限制

1. 应用满足《[常见类型移动互联网应用程序必要个人信息范围规定](http://www.cac.gov.cn/2021-03/22/c_1617990997054277.htm)》（对第三方网站的内容，华为不承担任何责任）中使用手机号的必要业务场景。
2. 儿童账号无法通过该能力获取到手机号。
3. 获取手机号能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。
4. 获取手机号能力目前仅支持游戏类应用申请使用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/2T3SkjyyQyuAgL38xXmJpw/zh-cn_image_0000002736313873.png)

流程说明：

1. 应用通过传对应scope和permission调用授权API，如果已授权则直接返回临时登录凭证Authorization Code；如果未授权则拉起授权页，在用户确认授权后，返回Authorization Code。
2. 将Authorization Code传给应用服务端，使用Client ID、Client Secret、Authorization Code从华为服务器中获取Access Token，再使用Access Token请求获取用户信息。
3. 从用户信息中获取到手机号、UnionID、OpenID。

## 接口说明

获取手机号关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-authentication.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)(): [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest) | 获取授权接口，通过[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)传入返回手机号的scope：phone及返回Authorization Code的permission：serviceauthcode，即可获取到Authorization Code。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建授权请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行授权操作。 |

**注意** 

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

1. 在进行代码开发前，请先确认您已完成[开发准备](account-config-permissions.md)工作。

   * 若未配置签名和指纹，将报错[1001500001 应用指纹证书校验失败](account-faq-1.md)。
   * 若未完成“获取您的手机号”权限申请，将报错[1001502014 应用未申请scopes或permissions权限](account-faq-2.md)。
2. 设备需要登录华为账号，若未登录则拉起登录页面。

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
   // 获取手机号需要传如下scope，传参数之前需要先申请对应scope权限，否则会返回1001502014错误码
   authRequest.scopes = ['phone'];
   // 获取authorizationCode需传如下permission
   authRequest.permissions = ['serviceauthcode'];
   // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   authRequest.forceAuthorization = true;
   // 建议使用generateRandomUUID生成state，可用于一致性比对，防止跨站攻击
   authRequest.state = util.generateRandomUUID();
   ```
3. 调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)方法执行授权请求，并处理授权结果，从授权结果中解析出Authorization Code，之后将Authorization Code传给应用服务端处理。

   ```typescript
   // 执行请求
   try {
     // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
     const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
     controller.executeRequest(authRequest).then((data) => {
       const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
       const state = authorizationWithHuaweiIDResponse.state;
       // state为空时，归一化处理为空字符串
       const normalizedRequestState = authRequest.state || '';
       const normalizedState = state || '';
       if (normalizedRequestState !== normalizedState) {
         hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
         return;
       }
       hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
       const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
       const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
       // 开发者处理authorizationCode
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
     // 在应用获取手机号场景下，涉及UI交互时，建议按照如下错误码指导提示用户
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
       // 获取用户信息失败，请尝试使用其他方式登录
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

### 服务端开发

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-phone.md#接口原型)获取用户信息，从用户信息中获取用户手机号、UnionID、OpenID。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](../harmonyos-references/account-api-obtain-refresh-token.md#接口原型)向华为账号服务器请求获取新的Access Token。

   **说明** 

   1. 当Access Token失效时，若您不使用Refresh Token向账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，业务可重新登录授权获取Authorization Code，向账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](../harmonyos-references/account-api-obtain-refresh-token.md#错误码)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
