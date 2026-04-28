---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-phonenumber
title: 快速验证
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取手机号 > 快速验证
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d86a2e57b62c4fe525d87fd67d327d86da9c054b72003a63bb173e0a603912d4
---

## 场景介绍

当应用对获取的手机号时效性要求不高时，可使用Account Kit提供的手机号授权与快速验证能力，向用户发起手机号授权申请，经用户同意授权后，获取到手机号并为用户提供相应服务。以下对Account Kit提供的手机号授权与快速验证能力进行介绍，快速验证手机号功能还可使用场景化控件[快速验证手机号Button](scenario-fusion-button-getphonenumber.md)进行实现。

说明

对用户选择的华为账号绑定的手机号或者新增的手机号进行验证，**不保证是实时的验证**，**仅首次需要用户授权**。

**图1** 手机端快速验证手机号（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/_qQCTVbQRF2ko-_UWoa5dA/zh-cn_image_0000002552958754.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=931C4AFE7DA71403B99E4CE510F236E071F908CC60DEFED220399A723614DFAE "点击放大")

**图2** Wearable设备快速验证手机号（请以实际效果为准）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/7WmnkZoyQM2ITrczyF4Zkw/zh-cn_image_0000002583478755.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=90E1BEB091186000F23180C38E70F21B1C00E18EE490433DDCDAEA80F694B007 "点击放大")

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/L6VLOsFYTYii_TSyoHCuuw/zh-cn_image_0000002552799106.png?HW-CC-KV=V1&HW-CC-Date=20260427T234759Z&HW-CC-Expire=86400&HW-CC-Sign=88DDC7AB7B933307097B5A17DE0F7DBFC36000376F1878927CC77B52DF76C5C6)

流程说明：

1. 应用通过传对应scope和permission调用授权API，如果已授权则直接返回临时登录凭证Authorization Code；如果未授权则拉起授权页，在用户确认授权后，返回Authorization Code。
2. 将Authorization Code传给应用服务端，使用Client ID、Client Secret、Authorization Code从华为服务器中获取Access Token，再使用Access Token请求获取用户信息。
3. 从用户信息中获取到手机号、UnionID、OpenID。

## 接口说明

获取快速验证手机号关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-authentication.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)(): [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest) | 获取授权接口，通过[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)传入返回手机号的scope：phone及返回Authorization Code的permission：serviceauthcode，即可获取到Authorization Code。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建授权请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行授权操作。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

1、在进行代码开发前，请先确认您已完成[开发准备](account-config-permissions.md)工作。

* 若未配置签名和指纹，将报错[1001500001 应用指纹证书校验失败](account-faq-1.md)。
* 若未完成“获取您的手机号”权限申请，将报错[1001502014 应用未申请scopes或permissions权限](account-faq-2.md)。

2、设备需要登录华为账号，若未登录则拉起登录页面。

## 开发步骤

### 客户端开发

1. 导入[authentication](../harmonyos-references/account-api-authentication.md)模块及相关公共模块。

   ```
   1. import { authentication } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { util } from '@kit.ArkTS';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建授权请求并设置参数。

   ```
   1. // 创建授权请求，并设置参数
   2. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   3. // 获取手机号需要传如下scope，传参数之前需要先申请对应scope权限，否则会返回1001502014错误码
   4. authRequest.scopes = ['phone'];
   5. // 获取authorizationCode需传如下permission
   6. authRequest.permissions = ['serviceauthcode'];
   7. // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   8. authRequest.forceAuthorization = true;
   9. // 用于防跨站点请求伪造
   10. authRequest.state = util.generateRandomUUID();
   ```
3. 调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)方法执行授权请求，并处理授权结果，从授权结果中解析出Authorization Code，之后将Authorization Code传给应用服务端处理。

   ```
   1. // 执行请求
   2. try {
   3. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   4. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
   5. controller.executeRequest(authRequest).then((data) => {
   6. const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
   7. const state = authorizationWithHuaweiIDResponse.state;
   8. if (state && authRequest.state !== state) {
   9. hilog.error(0x0000, 'testTag', `Failed to authorize. The state is different, response state: ${state}`);
   10. return;
   11. }
   12. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
   13. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
   14. const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
   15. // 开发者处理authorizationCode
   16. }).catch((err: BusinessError) => {
   17. dealAllError(err);
   18. });
   19. } catch (error) {
   20. dealAllError(error);
   21. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError): void {
   3. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
   4. // 在应用快速验证手机号场景下，涉及UI交互时，建议按照如下错误码指导提示用户
   5. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   6. // 用户未登录华为账号，请登录华为账号并重试
   7. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   8. // 网络异常，请检查当前网络状态并重试
   9. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
   10. // 用户取消授权
   11. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
   12. // 系统服务异常，请稍后重试
   13. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
   14. // 重复请求，应用无需处理
   15. } else {
   16. // 获取用户信息失败，请尝试使用其他方式登录
   17. }
   18. }

   20. export enum ErrorCode {
   21. // 账号未登录
   22. ERROR_CODE_LOGIN_OUT = 1001502001,
   23. // 网络错误
   24. ERROR_CODE_NETWORK_ERROR = 1001502005,
   25. // 用户取消授权
   26. ERROR_CODE_USER_CANCEL = 1001502012,
   27. // 系统服务异常
   28. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   29. // 重复请求
   30. ERROR_CODE_REQUEST_REFUSE = 1001500002
   31. }
   ```

### 服务端开发

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[获取用户信息接口](../harmonyos-references/account-api-get-user-info-get-phone.md#接口原型)获取用户信息，从用户信息中获取用户手机号、UnionID、OpenID。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](../harmonyos-references/account-api-get-user-info-get-nickname-and-avatar.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](../harmonyos-references/account-api-obtain-refresh-token.md#接口原型)向华为账号服务器请求获取新的Access Token。

   说明

   1. 当Access Token失效时，若您不使用Refresh Token向账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，业务可重新登录授权获取Authorization Code，向账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](../harmonyos-references/account-api-obtain-refresh-token.md#错误码)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
