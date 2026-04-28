---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-on-demand-acquisition
title: 华为账号其他方式登录获取用户风险等级
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取风险等级 > 华为账号其他方式登录获取用户风险等级
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:daec464a4abec1b2c659feddb96a3f341ab02946a0abd1a2c52fe462eb7f8e1f
---

## 场景介绍

应用已使用华为账号关联登录场景下，开展商户补贴、优惠券发放等商业营销活动时获取华为账号风险等级，有效识别“薅羊毛”风险，保护营销资源合理使用，降低业务安全问题给营销方带来的损失，为相关活动保驾护航。以下对Account Kit提供的获取用户风险等级能力进行介绍，如果需要同时获取风险等级和手机号还可参考场景化控件[获取手机号和风险等级Button](scenario-fusion-button-get-risklevel.md)进行实现。

## 约束与限制

1. 获取用户风险等级scope仅支持与openid、phone、profile组合使用，接口支持的全量scopes见[scope列表](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)。
2. 获取风险等级能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/_tZsX9CyTXK6coP1t2GP3g/zh-cn_image_0000002552958758.png?HW-CC-KV=V1&HW-CC-Date=20260427T234801Z&HW-CC-Expire=86400&HW-CC-Sign=944C586CEE637F1F5FAB26CEBF639096CDFE77C83B4730A78DDCCEABB74EF3C7)

流程说明：

1. 应用通过传对应scope和permission调用授权API，如果已授权则直接返回临时登录凭证Authorization Code，如果未授权：

   1. scopes传入riskLevel，则授权API直接返回Authorization Code。
   2. scopes传入riskLevel、profile/phone，则拉起授权页，用户点击允许后授权API返回Authorization Code。
2. 将Authorization Code传给应用服务端，使用Client ID、Client Secret、Authorization Code从华为账号服务器中获取Access Token，再使用Access Token请求获取用户的风险等级。

## 接口说明

获取用户风险等级关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-authentication.md)。

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)(): [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest) | 获取授权接口，通过[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)传入风险等级的scope：riskLevel及Authorization Code的permission：serviceauthcode，即可在授权结果中获取到Authorization Code。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建授权请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行授权操作。可从[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)的子类[AuthorizationWithHuaweiIDResponse](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidresponse)中解析[AuthorizationWithHuaweiIDCredential](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidcredential)，其中包含authorizedScopes，可确认风险等级是否授权成功。具体解析方法请参考[客户端开发](account-get-risklevel-on-demand-acquisition.md#客户端开发)的示例代码。 |

## 开发前提

1. 在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。
2. 应用在使用获取风险等级能力之前，需要完成对应的scope权限申请。

   scope权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](account-faq-2.md)。当前可通过发送邮件至[accountkit@huawei.com](mailto:accountkit@huawei.com)进行申请。

   请提供如下信息进行申请，我们会在1-2个工作日内回复申请结果，请您留意邮箱消息。

   **邮件主题**：【获取风险等级】权限申请

   **邮件正文**：（请在正文中描述下具体希望申请的权限）

   **企业名称**：\*\*\*

   **应用名称**：\*\*\*

   **应用包名**：com.\*\*\*.\*\*\*

   **APP ID**：1\*\*\*\*12

   **Client ID**：1\*\*\*\*14

   **背景介绍：** （请提供应用简单介绍，便于快速了解）

   **使用场景**：（请提供相关使用场景的文字描述、交互流程图或参考交互视频等，可提供类似应用的使用场景进行说明）

   **使用该权限的必要性：** （请提供应用需要该权限和信息的必要性）

## 客户端开发

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
   3. // 获取风险等级需要传如下scope
   4. authRequest.scopes = ['riskLevel'];
   5. // 获取authorizationCode需传如下permission
   6. authRequest.permissions = ['serviceauthcode'];
   7. // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   8. authRequest.forceAuthorization = true;
   9. // 用于防跨站点请求伪造
   10. authRequest.state = util.generateRandomUUID();
   ```
3. 调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)方法执行授权请求，并处理授权结果，从授权结果中解析出authorizedScopes和Authorization Code。

   ```
   1. // 执行授权请求
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
   13. let riskLevelAuthorized: boolean = false;
   14. const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
   15. const authorizedScopes = authorizationWithHuaweiIDCredential?.authorizedScopes;
   16. // 判断授权成功scopes中是否包含riskLevel
   17. if (authorizedScopes?.includes("riskLevel")) {
   18. riskLevelAuthorized = true;
   19. }
   20. const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
   21. // 开发者处理riskLevelAuthorized, authorizationCode
   22. }).catch((err: BusinessError) => {
   23. dealAllError(err);
   24. });
   25. } catch (error) {
   26. dealAllError(error);
   27. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError): void {
   3. hilog.error(0x0000, 'testTag', `Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}`);
   4. // 在应用获取用户风险等级场景下，涉及UI交互时，建议按照如下错误码指导提示用户
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
   16. // 获取用户信息失败，请稍后重试
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

## 服务端开发

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[获取用户风险等级接口](../harmonyos-references/account-api-getuserrisklevel.md#接口原型)获取用户的风险等级。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](../harmonyos-references/account-api-getuserrisklevel.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](../harmonyos-references/account-api-obtain-refresh-token.md#接口原型)向华为账号服务器请求获取新的Access Token。

   说明

   1. 当Access Token失效时，若应用不使用Refresh Token向华为账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，应用可重新登录授权获取Authorization Code，向华为账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](../harmonyos-references/account-api-obtain-refresh-token.md#错误码)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
3. 应用服务端基于风险等级判别用户风险程度，决定是否需要对用户进行额外验证或拦截用户行为。
