---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-unionid-login-api
title: 使用自定义按钮登录
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 华为账号登录（获取UnionID/OpenID） > 使用自定义按钮登录
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e49218f779b851abc63731ecf6ca72e0f6c9c90e81dd401e773135853bb4c030
---

## 场景介绍

应用应遵照[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)使用规则在登录页面嵌入自定义华为账号登录按钮，使用自定义按钮触发调用华为账号登录API获取Authorization Code，通过服务端交互获取用户的UnionID、OpenID完成用户登录；或者与应用账号完成绑定，绑定后用于登录或者验证。

## 约束与限制

自定义按钮登录能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/-hTa7uAYT9-iTwAuMCe5pg/zh-cn_image_0000002583438797.png?HW-CC-KV=V1&HW-CC-Date=20260427T234757Z&HW-CC-Expire=86400&HW-CC-Sign=B85BAF5E0BB37AC428D366F02B85216B9DBD44BED937E72337324348F7AB5941)

流程说明：

1. 展示自定义按钮调用登录API阶段（序号1-4）：

   1. 用户打开应用进行登录，点击自定义登录按钮，应用传forceLogin等参数后调用华为账号登录API，请求华为账号授权信息。
   2. 如华为账号未登录，将拉起华为账号登录页，用户登录后，将返回Authorization Code等数据给应用。
   3. 如华为账号已登录，将直接返回Authorization Code等数据给应用。
2. 用户关联应用账号阶段（序号5-16）：

   1. 应用服务端通过Authorization Code获取到Access Token，再使用Access Token调用[解析凭证接口](../harmonyos-references/account-api-get-token-info.md#接口原型)获取用户相关信息。通过Authorization Code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。
   2. 应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录等功能。
   3. 应用对用户身份标识UnionID/OpenID、业务登录凭证SessionId信息进行认证后，通过UnionID/OpenID判断用户是否已关联应用系统数据库，如已关联，则完成用户登录；如未关联，则创建新用户，绑定UnionID/OpenID。

## 接口说明

使用API获取UnionID登录关键接口如下表所示，具体API说明详见[API参考](../harmonyos-references/account-api-authentication.md)。

| 接口名 | 描述 |
| --- | --- |
| [createLoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createloginwithhuaweiidrequest)(): [LoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#loginwithhuaweiidrequest) | 创建账号登录请求。[LoginWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#loginwithhuaweiidrequest)中的forceLogin参数用来控制当用户未登录华为账号时，是否强制拉起华为账号登录界面。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建登录请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行登录操作。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

## 客户端开发

1. 根据[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)规范开发自定义登录图标按钮，参考如下步骤在点击事件中完成华为账号登录API调用。
2. 导入[authentication](../harmonyos-references/account-api-authentication.md)模块及相关公共模块。

   ```
   1. import { authentication } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { util } from '@kit.ArkTS';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
3. 创建登录请求并设置参数。

   ```
   1. // 创建登录请求，并设置参数
   2. const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
   3. // 用户是否需要登录授权，该值为true且用户未登录或未授权时，会拉起用户登录或授权页面
   4. loginRequest.forceLogin = true;
   5. // 用于防跨站点请求伪造
   6. loginRequest.state = util.generateRandomUUID();
   ```
4. 调用[AuthenticationController](../harmonyos-references/account-api-authentication.md#authenticationcontroller)对象的[executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)方法执行登录请求，并处理登录结果，获取到Authorization Code及ID Token。之后将Authorization Code传给应用服务端处理，可参考[客户端与服务端交互开发](account-phone-unionid-login.md#客户端与服务端交互开发)的开发步骤a和b。通过code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。应用可以通过公开的网址获取到华为账号服务器发布的公钥，对签名和ID Token中的必要信息进行验证，以证明其没有被篡改过。解析ID Token可参考[ID Token解析与验证](account-faq-12.md#解析与验证)。

   ```
   1. // 执行登录请求
   2. try {
   3. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   4. const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
   5. controller.executeRequest(loginRequest).then((response: authentication.LoginWithHuaweiIDResponse) => {
   6. const loginWithHuaweiIDResponse = response as authentication.LoginWithHuaweiIDResponse;
   7. const state = loginWithHuaweiIDResponse.state;
   8. if (state && loginRequest.state !== state) {
   9. hilog.error(0x0000, 'testTag', `Failed to login. The state is different, response state: ${state}`);
   10. return;
   11. }
   12. hilog.info(0x0000, 'testTag', 'Succeeded in logging in.');
   13. const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
   14. const code = loginWithHuaweiIDCredential?.authorizationCode;
   15. // 开发者处理code
   16. }).catch((error: BusinessError) => {
   17. dealAllError(error);
   18. })
   19. } catch (error) {
   20. dealAllError(error);
   21. }
   ```

   ```
   1. // 错误处理
   2. function dealAllError(error: BusinessError): void {
   3. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
   4. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
   5. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   6. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
   7. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   8. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
   9. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
   10. // 登录失败，请尝试使用其他方式登录
   11. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
   12. // 用户取消授权
   13. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
   14. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
   15. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
   16. // 重复请求，应用无需处理
   17. } else {
   18. // 应用登录失败，请尝试使用其他方式登录
   19. }
   20. }

   22. export enum ErrorCode {
   23. // 账号未登录
   24. ERROR_CODE_LOGIN_OUT = 1001502001,
   25. // 网络错误
   26. ERROR_CODE_NETWORK_ERROR = 1001502005,
   27. // 内部错误
   28. ERROR_CODE_INTERNAL_ERROR = 1001502009,
   29. // 用户取消授权
   30. ERROR_CODE_USER_CANCEL = 1001502012,
   31. // 系统服务异常
   32. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   33. // 重复请求
   34. ERROR_CODE_REQUEST_REFUSE = 1001500002
   35. }
   ```

## 服务端开发

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[获取用户级凭证接口](../harmonyos-references/account-api-obtain-user-token.md#接口原型)向华为账号服务器请求获取Access Token、Refresh Token。
2. 使用Access Token调用[解析凭证接口](../harmonyos-references/account-api-get-token-info.md#接口原型)获取用户的UnionID。

   **Access Token过期处理**

   由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过[REST API错误码](../harmonyos-references/account-api-get-token-info.md#错误码)判断），可以使用Refresh Token（有效期180天）通过[刷新用户级凭证接口](../harmonyos-references/account-api-obtain-refresh-token.md#接口原型)向华为账号服务器请求获取新的Access Token。

   说明

   1. 当Access Token失效时，若应用不使用Refresh Token向华为账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。
   2. 当Access Token非正常失效（如修改密码、退出账号、删除设备）时，应用可重新登录授权获取Authorization Code，向华为账号服务器请求获取新的Access Token。

   **Refresh Token过期处理**

   由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过[REST API错误码](../harmonyos-references/account-api-obtain-refresh-token.md#错误码)判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。
3. 应用在自己的用户体系通过查询获取的UnionID判断该用户是否已关联。如已关联，则完成用户登录；如未关联，则创建新用户，绑定UnionID，完成用户登录。
