---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login
title: 华为账号一键登录（获取手机号和UnionID/OpenID）
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 华为账号一键登录（获取手机号和UnionID/OpenID）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:49+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3c7a6b2dc9d4d0b3db0e15ab481375ff834f78620df8999386bebf630d828497
---

## 概述

华为账号一键登录是基于[OAuth 2.0协议标准](https://oauth.net/2/)和[OpenID Connect协议标准](https://openid.net/connect/)构建的OAuth 2.0授权登录系统，应用可以通过华为账号一键登录能力快捷地获取华为账号用户的身份标识和手机号，快速建立应用内的用户体系。

**优势：**

* 利用系统账号的安全性和便利性，用户无需输入账号名和密码，无需复杂的安全验证，简化登录步骤，提高用户转化率。
* 提供系统验证过的手机号，关联应用已有用户。
* 实现Phone、Tablet、PC/2in1、TV设备一致的登录体验。

## 场景介绍

若应用需同时获取手机号和UnionID完成用户登录，Account Kit提供了同时获取手机号和UnionID的华为账号一键登录按钮。应用可以将华为账号一键登录按钮嵌入自有的登录页，使用登录按钮获取手机号和UnionID，实现用户登录。设备登录华为账号（该账号已绑定手机号）后，一键登录获取手机号可不依赖设备插SIM卡。

说明

1. 儿童账号一键登录场景：

   用户使用儿童账号进行登录，点击一键登录会触发Account Kit默认提供的家长验密流程（Account Kit提供的验证页，暂不可自定义），家长验密完成后可获取用户的身份标识和手机号。并且TV设备暂不支持儿童账号。
2. 手机号验证机制说明：

   Account Kit调用系统能力获取华为账号登录设备上的SIM卡手机号码，与华为账号绑定的手机号进行校验（有网络即可，无需使用SIM卡移动数据）。用户点击一键登录按钮后，结合华为账号使用过程中账号所绑定的手机号短信验证记录，90天内有验证通过的记录，则返回该华为账号绑定的手机号；若90天内没有验证通过的记录，则触发Account Kit默认提供的短信验证流程（Account Kit提供的验证页，暂不可自定义），确保返回的手机号经过验证。

## 约束与限制

1. 应用满足《[常见类型移动互联网应用程序必要个人信息范围规定](http://www.cac.gov.cn/2021-03/22/c_1617990997054277.htm)》中使用手机号的必要业务场景。
2. 使用华为账号一键登录功能用户必须同意[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)，当用户点击[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)，系统浅色模式下应用需跳转到如下链接<https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN>，系统深色模式下跳转到<https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN&bgmode=black>。
3. 应用在用户同意后获取到手机号，需要根据自身业务场景判断使用的方式，必要时增加其他安全验证手段，比如对二次放号的判断。
4. 华为账号一键登录服务当前仅限中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）用户可用。
5. 应用服务端获取华为账号绑定号码时，该服务器必须部署在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
6. 华为账号一键登录支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。
7. 仅支持企业开发者使用一键登录，个人开发者请使用[华为账号登录](account-unionid-login-button.md)或[静默登录](account-silent-login.md)实现登录。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/GYlpl0YdQLWeMkTRfmxIEQ/zh-cn_image_0000002589245051.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=4C3E4D3913F9E447C5F4D1FC3347F0BFA49AF758F92C5B7F565B3D742AF2A970)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/zGOv-6rOTnySDgcO6Vvm0A/zh-cn_image_0000002558765246.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=280F7B2031B7DCB21C84AA3762CC0C9F7176BCF56E76F98F24E36140DB5B40A8)

## 登录页面UX设计规范

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/-BqrJ52ES-6RrpNtaYOt6A/zh-cn_image_0000002558605590.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=9CAD8ABCE4ED4B43510E93CAA89CE7274F9149D3D30BD4E9D4ECF870E30AC748)

一键登录按钮的用户体验和UX设计需符合[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)规范，用户体验设计图2中的华为标志按钮可参考[华为账号登录视觉规范](../design-guides/id-0000001880001344.md#section61791745172816)中的样式三。不符合规范的UX设计可能会对应用上架和用户体验带来影响。一键登录按钮的样式设计具体可以参考[华为账号登录按钮类型](../harmonyos-references/account-api-component-manager.md#style)。

## 用户场景设计

用户使用华为账号一键登录能力，注册/登录应用时，可能存在多种场景，应用可参照以下流程，根据自身业务场景进行设计。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/FMv4J6m2Q720uziKX93IOw/zh-cn_image_0000002589325117.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=08E985A7FE40F1191699D23624C7D4C8670690C9DC3322A4765E5F6B2FA66912)

说明

**将UnionID/OpenID和手机号同时与应用账号建立关联，可以为用户带来更多便利的功能。如：实现[静默登录](account-silent-login.md)、[获取华为账号用户信息](account-get-user-info-overview.md)、[获取华为账号风险等级](account-get-risklevel-byquicklogin.md)等。实现免用户操作登录，获得安全快捷的应用登录体验。**

## 业务流程

### 用户首次登录应用

若应用未接入过华为账号登录，不存在使用华为账号登录过的应用账号，请参照以下流程接入华为账号一键登录。

**图1** 华为账号一键登录（用户首次登录应用）流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/bRFMuarjSIy0O4-H6jeqFA/zh-cn_image_0000002589245053.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=00C83113070E01D4A91D37A253FE7A6601430AFBDA748A6D3D77ED3C8B57D26C)

流程说明：

1. 预取号阶段（序号1-4）：

   1. 用户打开应用后，应用scope传quickLoginAnonymousPhone调用[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)授权请求获取匿名手机号。如果获取到匿名手机号为空，应用需要展示其他登录方式。

      说明

      获取匿名手机号需要进行超时处理，应用可根据实际场景设置超时时间，推荐设置5秒保证用户体验。
   2. 若华为账号未登录，调用[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)授权请求会返回[1001502001 用户未登录华为账号](../harmonyos-references/account-api-error-code.md#section1001502001-用户未登录华为账号)错误码，此时应用需要展示其他登录方式进行应用登录。
2. 展示一键登录页面阶段（序号5）：

   1. 获取到的匿名手机号需要展示在页面上并设置好隐私协议，设置登录按钮类型为LoginType.QUICK\_LOGIN，展示包含[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton)组件的一键登录页面。应用可结合实际登录风控场景，通过组件参数传入风险等级标识[获取华为账号风险等级](account-get-risklevel-byquicklogin.md)，通过华为账号一键登录获取用户风险等级，对恶意账号进行风控，提升应用的安全等级。
3. 点击一键登录关联用户账号阶段（序号6-16）：

   1. 用户同意协议后，点击华为账号一键登录按钮，应用可以通过[HuaweiIDCredential](../harmonyos-references/account-api-component-manager.md#huaweiidcredential)获取到Authorization Code等数据。
   2. 将获取的Authorization Code数据传给应用服务端，应用服务端通过Authorization Code调用[/oauth2/v6/quickLogin/getPhoneNumber接口](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md#接口原型)获取用户完整手机号和UnionID、OpenID。
   3. 应用通过关联用户手机号和UnionID、OpenID完成用户登录。

### 用户非首次登录应用（可选）

应用接入过华为账号登录，存在使用华为账号登录过的用户账号，即根据UnionID/OpenID判断用户已关联过应用系统数据库，则需要参照以下流程开发。

**图2** 华为账号一键登录（用户非首次登录应用）流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/zo06eReHRdyc7Kyqd_PwyQ/zh-cn_image_0000002558765248.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=CB9AD184314B62FBD3E75B3D5C3E7AE134B276E243C8FB04659B221A94B1B742)

流程说明：

1. 应用调用[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)授权请求获取[AuthorizationWithHuaweiIDResponse](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidresponse)响应结果中的Authorization Code。
2. 应用服务端通过Authorization Code调用[/oauth2/v6/quickLogin/getPhoneNumber接口](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md#接口原型)获取用户相关信息。通过Authorization Code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。
3. 应用对用户身份标识UnionID/OpenID、业务登录凭证SessionId信息进行认证后，通过UnionID/OpenID判断用户是否已关联应用系统数据库，如已关联，结合风控、安全因素及自身业务场景判断，可展示已关联的账号，由用户选择是否使用华为账号登录应用，或免用户操作，静默登录应用。

## 接口说明

华为账号一键登录按钮关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [createAuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest)(): [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest) | 获取授权接口，通过[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)传入一键登录的scope：quickLoginAnonymousPhone，即可在授权结果中获取到用户的匿名手机号和Authorization Code。 |
| [constructor](../harmonyos-references/account-api-authentication.md#constructor)(context?: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)) | 创建授权请求Controller。 |
| [executeRequest](../harmonyos-references/account-api-authentication.md#executerequest-1)(request: [AuthenticationRequest](../harmonyos-references/account-api-authentication.md#authenticationrequest)): Promise<[AuthenticationResponse](../harmonyos-references/account-api-authentication.md#authenticationresponse)> | 通过Promise方式执行授权操作。 |
| [LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton) | 华为账号Button登录组件。  该组件仅纯文本样式支持华为账号一键登录功能。开发者可以通过调整按钮的大小、圆角等参数以适配HarmonyOS应用登录界面。如果仍然不能满足开发者的诉求，可以使用[Style](../harmonyos-references/account-api-component-manager.md#style)的BUTTON\_CUSTOM值定义按钮的文字颜色和背景色。 |
| [onClickLoginWithHuaweiIDButton](../harmonyos-references/account-api-component-manager.md#onclickloginwithhuaweiidbutton-1)(callback: AsyncCallback<[HuaweiIDCredential](../harmonyos-references/account-api-component-manager.md#huaweiidcredential)>): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 注册华为账号一键登录按钮的结果回调。 |
| [setAgreementStatus](../harmonyos-references/account-api-component-manager.md#setagreementstatus-1)(agreementStatus: [AgreementStatus](../harmonyos-references/account-api-component-manager.md#agreementstatus)): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 设置协议状态方法。用户未同意协议前设置协议状态为NOT\_ACCEPTED，用户同意协议后设置协议状态为ACCEPTED，才可以完成华为账号登录。 |
| [onClickEvent](../harmonyos-references/account-api-component-manager.md#onclickevent-1)(callback: AsyncCallback<[ClickEvent](../harmonyos-references/account-api-component-manager.md#clickevent)>): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 注册华为账号一键登录按钮的点击事件回调。 |
| [continueLogin](../harmonyos-references/account-api-component-manager.md#continuelogin)(callback: AsyncCallback<void>): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 用户点击协议弹框的同意并登录按钮结果回调。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

1. 在进行代码开发前，请先确认已完成[开发准备](account-config-permissions.md)工作。

   若未配置签名和指纹，将报错[1001500001 应用指纹证书校验失败](account-faq-1.md)。

   若未申请“华为账号一键登录”权限，将报错[1001502014 应用未申请scopes或permissions权限](account-faq-2.md)。
2. 若应用开启了[代码混淆](source-obfuscation-guide.md)，应用工程代码中获取到的quickLoginAnonymousPhone（匿名手机号）属性需要配置混淆白名单防止编译release包时被混淆，否则无法获取到匿名手机号。在调用获取匿名手机号方法工程模块的混淆文件obfuscation-rules.txt中添加：

   ```
   1. # 开发者开启属性混淆需要配置quickLoginAnonymousPhone属性白名单防止其被混淆
   2. -enable-property-obfuscation
   3. -keep-property-name
   4. quickLoginAnonymousPhone
   ```

## 客户端开发

开发者可参考下述内容自行开发，也可使用Account Kit为常见的三方开发框架（Flutter、H5、React-Native、uni-app）提供的SampleCode示例工程，用于接入华为账号一键登录能力，具体可参考[三方开发框架接入华为账号一键登录](account-faq-18.md)进行开发。

### 用户首次登录应用

1. 导入模块。

   导入Account Kit的[authentication](../harmonyos-references/account-api-authentication.md)模块及相关公共模块。

   ```
   1. import { authentication } from '@kit.AccountKit';
   2. import { util } from '@kit.ArkTS';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取匿名手机号。

   调用[authentication](../harmonyos-references/account-api-authentication.md)模块的[AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)请求获取华为账号用户的匿名手机号。匿名手机号用于登录页面展示。

   注意

   该场景下forceAuthorization参数需设置为false。

   根据获取的响应结果判断，可能存在以下场景：

   1）返回ArkTS错误码，开发者可参考下表针对不同错误码进行处理：

   **表1** 获取匿名手机号错误码处理

   | 错误码 | 错误描述 | 处理建议 |
   | --- | --- | --- |
   | 1001502001 | 用户未登录华为账号 | 应用展示其他登录方式 |
   | 1001502005 | 网络异常 | 提示用户检查当前网络状态后重试 |
   | 1001502009 | 内部错误 | 应用展示其他登录方式 |
   | 1001502014 | 应用未申请scopes或permissions权限 | 请参考[1001502014 应用未申请scopes或permissions权限的可能原因和解决方法](account-faq-2.md)解决该报错 |
   | 1001500001 | 应用指纹证书校验失败 | 请参考[1001500001 应用指纹证书校验失败的可能原因和解决办法](account-faq-1.md)解决该报错 |
   | 1001500002 | 重复请求 | 重复请求，应用无需处理 |
   | 1001500003 | 不支持该scopes或permissions | 1、华为账号用户注册地可能为中国境外、香港特别行政区、澳门特别行政区或中国台湾，应用展示其他登录方式  2、仅在5.1.1(19)支持TV设备，其他版本应用可以通过[华为账号登录](account-unionid-login-button.md)进行登录 |
   | 12300001 | 系统服务异常 | 应用展示其他登录方式 |

   2）获取到的匿名手机号为空，说明华为账号没有绑定手机号、权限未申请或未生效，上述异常场景应用需要展示其他登录方式。

   3）若开发者开启了[代码混淆](source-obfuscation-guide.md)，需将quickLoginAnonymousPhone（匿名手机号）属性加入混淆白名单，防止其被混淆。

   ```
   1. getQuickLoginAnonymousPhone() {
   2. // 创建授权请求，并设置参数
   3. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   4. // 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限，否则会返回1001502014错误码
   5. authRequest.scopes = ['quickLoginAnonymousPhone'];
   6. // 用于防跨站点请求伪造
   7. authRequest.state = util.generateRandomUUID();
   8. // 一键登录场景该参数必须设置为false
   9. authRequest.forceAuthorization = false;
   10. const controller = new authentication.AuthenticationController();
   11. try {
   12. controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
   13. // 获取到匿名手机号
   14. const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
   15. if (anonymousPhone) {
   16. hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
   17. const quickLoginAnonymousPhone: string = anonymousPhone;
   18. return;
   19. }
   20. hilog.info(0x0000, 'testTag', 'Succeeded in authentication. AnonymousPhone is empty.');
   21. // 未获取到匿名手机号，应用需要跳转到其他方式登录页面
   22. }).catch((error: BusinessError) => {
   23. this.dealAllError(error);
   24. })
   25. } catch (error) {
   26. this.dealAllError(error);
   27. }
   28. }

   30. // 错误处理
   31. dealAllError(error: BusinessError): void {
   32. hilog.error(0x0000, 'testTag',
   33. `Failed to get quickLoginAnonymousPhone, errorCode is ${error.code}, errorMessage is ${error.message}`);
   34. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
   35. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   36. // 华为账号未登录，应用需要展示其他登录方式
   37. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   38. // 网络异常，请检查当前网络状态并重试或展示其他登录方式
   39. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
   40. // 登录失败，应用需要展示其他登录方式
   41. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
   42. // 系统服务异常，应用需要展示其他登录方式
   43. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
   44. // 重复请求，应用无需处理
   45. } else {
   46. // 应用登录失败，应用需要展示其他登录方式
   47. }
   48. }

   50. export enum ErrorCode {
   51. // 账号未登录
   52. ERROR_CODE_LOGIN_OUT = 1001502001,
   53. // 网络错误
   54. ERROR_CODE_NETWORK_ERROR = 1001502005,
   55. // 内部错误
   56. ERROR_CODE_INTERNAL_ERROR = 1001502009,
   57. // 系统服务异常
   58. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   59. // 重复请求
   60. ERROR_CODE_REQUEST_REFUSE = 1001500002
   61. }
   ```
3. 展示一键登录页面并获取Authorization Code

   将获取到的匿名手机号设置给下面QuickLoginButtonComponent组件示例代码中的**quickLoginAnonymousPhone**变量，调用[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件，实现应用自己的登录页面，并展示华为账号一键登录按钮和华为账号用户认证协议（Account Kit提供跳转链接，应用需实现协议跳转，参见[约束与限制](account-phone-unionid-login.md#约束与限制)第2点），用户同意协议并点击一键登录按钮后，可获取到Authorization Code，将该值传给应用服务端用于获取用户信息（完整手机号、UnionID、OpenID）。通过code凭证获取用户信息可以有效避免因数据遍历、身份伪造、重放攻击导致的安全风险。

   ```
   1. import { loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { connection } from '@kit.NetworkKit';

   6. @Component
   7. struct QuickLoginComponent {
   8. // 第二步获取的匿名手机号传到此处
   9. @State quickLoginAnonymousPhone: string = '';

   11. build() {
   12. if (this.quickLoginAnonymousPhone) {
   13. QuickLoginButtonComponent({
   14. quickLoginAnonymousPhone: this.quickLoginAnonymousPhone
   15. })
   16. } else {
   17. // 授权获取匿名手机号为空时，请应用自行实现其他方式登录页面
   18. }
   19. }
   20. }

   22. @Component
   23. struct QuickLoginButtonComponent {
   24. logTag: string = 'QuickLoginButtonComponent';
   25. domainId: number = 0x0000;
   26. @State quickLoginAnonymousPhone: string = '';
   27. // 是否勾选协议
   28. @State isSelected: boolean = false;
   29. // 华为账号用户认证协议链接，此处仅为示例，实际开发过程中，出于可维护性、安全性等方面考虑，域名不建议硬编码在本地
   30. private static USER_AUTHENTICATION_PROTOCOL: string =
   31. 'https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
   32. private static USER_SERVICE_TAG = '用户服务协议';
   33. private static PRIVACY_TAG = '隐私协议';
   34. private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';
   35. // 定义LoginWithHuaweiIDButton展示的隐私文本，展示应用的用户服务协议、隐私协议和华为账号用户认证协议
   36. privacyText: loginComponentManager.PrivacyText[] = [{
   37. text: '已阅读并同意',
   38. type: loginComponentManager.TextType.PLAIN_TEXT
   39. }, {
   40. text: '《用户服务协议》',
   41. tag: QuickLoginButtonComponent.USER_SERVICE_TAG,
   42. type: loginComponentManager.TextType.RICH_TEXT
   43. }, {
   44. text: '《隐私协议》',
   45. tag: QuickLoginButtonComponent.PRIVACY_TAG,
   46. type: loginComponentManager.TextType.RICH_TEXT
   47. }, {
   48. text: '和',
   49. type: loginComponentManager.TextType.PLAIN_TEXT
   50. }, {
   51. text: '《华为账号用户认证协议》',
   52. tag: QuickLoginButtonComponent.USER_AUTHENTICATION_TAG,
   53. type: loginComponentManager.TextType.RICH_TEXT
   54. }, {
   55. text: '。',
   56. type: loginComponentManager.TextType.PLAIN_TEXT
   57. }];
   58. // 构造LoginWithHuaweiIDButton组件的控制器
   59. controller: loginComponentManager.LoginWithHuaweiIDButtonController =
   60. new loginComponentManager.LoginWithHuaweiIDButtonController()
   61. /**
   62. * 当应用使用自定义的登录页时，如果用户未同意协议，需要设置协议状态为NOT_ACCEPTED，当用户同意协议后再设置
   63. * 协议状态为ACCEPTED，才可以使用华为账号一键登录功能
   64. */
   65. .setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED)
   66. .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
   67. response: loginComponentManager.HuaweiIDCredential) => {
   68. this.handleLoginWithHuaweiIDButton(error, response);
   69. })
   70. .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
   71. if (error) {
   72. hilog.error(this.domainId, this.logTag,
   73. `onClickEvent error. errCode is ${error.code}, errMessage is ${error.message}`);
   74. return;
   75. }
   76. hilog.info(this.domainId, this.logTag, `onClickEvent clickEvent: ${clickEvent}`);
   77. // 设置按钮为不可点击态，待业务逻辑处理完成后，再设置为可点击态
   78. this.controller.setEnabled(false);
   79. });
   80. agreementDialog: CustomDialogController = new CustomDialogController({
   81. builder: AgreementDialog({
   82. privacyText: this.privacyText,
   83. cancel: () => {
   84. this.agreementDialog.close();
   85. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
   86. },
   87. confirm: () => {
   88. this.agreementDialog.close();
   89. this.isSelected = true;
   90. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
   91. // 调用此方法，同意协议与登录一并完成，无需再次点击登录按钮
   92. this.controller.continueLogin((error: BusinessError) => {
   93. if (error) {
   94. hilog.error(this.domainId, this.logTag,
   95. `Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}`);
   96. } else {
   97. hilog.info(this.domainId, this.logTag,
   98. 'Succeeded in clicking agreementDialog continueLogin.');
   99. }
   100. });
   101. },
   102. clickHyperlinkText: () => {
   103. this.agreementDialog.close();
   104. this.jumpToPrivacyWebView();
   105. }
   106. }),
   107. autoCancel: false,
   108. alignment: DialogAlignment.Center
   109. });

   111. // Toast提示
   112. showToast(resource: string) {
   113. try {
   114. this.getUIContext().getPromptAction().showToast({
   115. message: resource,
   116. duration: 2000
   117. });
   118. } catch (error) {
   119. const message = (error as BusinessError).message;
   120. const code = (error as BusinessError).code;
   121. hilog.error(this.domainId, this.logTag, `showToast args  errCode is ${code}, errMessage is ${message}`);
   122. }
   123. }

   125. // 跳转华为账号用户认证协议页，该页面需在工程main_pages.json文件配置
   126. jumpToPrivacyWebView() {
   127. try {
   128. // 需在module.json5中配置“ohos.permission.GET_NETWORK_INFO”权限
   129. const checkNetConn = connection.hasDefaultNetSync();
   130. if (!checkNetConn) {
   131. this.showToast('服务或网络异常，请稍后重试');
   132. return;
   133. }
   134. } catch (error) {
   135. const message = error.message as string;
   136. const code = error.code as string;
   137. hilog.error(0x0000, 'testTag', `Failed to hasDefaultNetSync, errCode is ${code}, errMessage is ${message}`);
   138. }
   139. this.getUIContext().getRouter().pushUrl({
   140. // 需在module.json5配置“ohos.permission.INTERNET”网络权限
   141. url: 'pages/WebPage',
   142. params: {
   143. isFromDialog: true,
   144. url: QuickLoginButtonComponent.USER_AUTHENTICATION_PROTOCOL
   145. }
   146. }, (err) => {
   147. if (err) {
   148. hilog.error(this.domainId, this.logTag,
   149. `Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}`);
   150. }
   151. });
   152. }

   154. handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
   155. response: loginComponentManager.HuaweiIDCredential) {
   156. if (error) {
   157. hilog.error(this.domainId, this.logTag,
   158. `Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}`);
   159. if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   160. this.getUIContext().showAlertDialog(
   161. {
   162. message: '网络未连接，请检查网络设置。',
   163. offset: { dx: 0, dy: -12 },
   164. alignment: DialogAlignment.Bottom,
   165. autoCancel: false,
   166. confirm: {
   167. value: '知道了',
   168. action: () => {
   169. // 用户点击“知道了”按钮，可于此处补充业务逻辑
   170. }
   171. }
   172. }
   173. );
   174. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
   175. // 未同意协议，弹出协议弹框，推荐使用该回调方式
   176. this.agreementDialog.open();
   177. } else if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   178. // 华为账号未登录提示
   179. this.showToast('华为账号未登录，请重试');
   180. } else if (error.code === ErrorCode.ERROR_CODE_NOT_SUPPORTED) {
   181. // 不支持该scopes或permissions提示
   182. this.showToast('该scopes或permissions不支持');
   183. } else if (error.code === ErrorCode.ERROR_CODE_PARAMETER_ERROR) {
   184. // 参数错误提示
   185. this.showToast('参数错误');
   186. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
   187. // 用户取消，无需特别处理
   188. } else {
   189. // 其他提示系统或服务异常
   190. this.showToast('服务或网络异常，请稍后重试');
   191. }
   192. this.controller.setEnabled(true);
   193. return;
   194. }
   195. try {
   196. if (this.isSelected) {
   197. if (response) {
   198. hilog.info(this.domainId, this.logTag, 'Succeeded in clicking LoginWithHuaweiIDButton.');
   199. // 开发者根据实际业务情况使用以下信息
   200. const authCode = response.authorizationCode;
   201. }
   202. } else {
   203. this.agreementDialog.open();
   204. }
   205. } catch (err) {
   206. hilog.error(this.domainId, this.logTag,
   207. `Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}`);
   208. this.getUIContext().showAlertDialog(
   209. {
   210. message: '服务或网络异常，请稍后重试',
   211. offset: { dx: 0, dy: -12 },
   212. alignment: DialogAlignment.Bottom,
   213. autoCancel: false,
   214. confirm: {
   215. value: '知道了',
   216. action: () => {
   217. // 用户点击“知道了”按钮，可于此处补充业务逻辑
   218. }
   219. }
   220. }
   221. );
   222. } finally {
   223. this.controller.setEnabled(true);
   224. }
   225. }

   227. build() {
   228. Scroll() {
   229. Column() {
   230. Column() {
   231. Column() {
   232. // 此处为示例资源，开发者可使用应用图标进行替换，以保证正常编译运行
   233. Image($r('app.media.app_icon'))
   234. .width(48)
   235. .height(48)
   236. .draggable(false)
   237. .copyOption(CopyOptions.None)
   238. .onComplete(() => {
   239. hilog.info(this.domainId, this.logTag, 'appIcon loading success.');
   240. })
   241. .onError(() => {
   242. hilog.error(this.domainId, this.logTag, 'appIcon loading fail.');
   243. })

   245. Text($r('app.string.app_name'))
   246. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   247. .fontWeight(FontWeight.Medium)
   248. .fontWeight(FontWeight.Bold)
   249. .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
   250. .minFontSize($r('sys.float.ohos_id_text_size_body1'))
   251. .maxLines(1)
   252. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   253. .constraintSize({ maxWidth: '100%' })
   254. .margin({
   255. top: 12
   256. })

   258. Text('应用描述')
   259. .fontSize($r('sys.float.ohos_id_text_size_body2'))
   260. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
   261. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
   262. .fontWeight(FontWeight.Regular)
   263. .constraintSize({ maxWidth: '100%' })
   264. .margin({
   265. top: 8
   266. })
   267. }.margin({
   268. top: 100
   269. })

   271. Column() {
   272. Text(this.quickLoginAnonymousPhone)
   273. .fontSize(36)
   274. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   275. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   276. .fontWeight(FontWeight.Bold)
   277. .lineHeight(48)
   278. .textAlign(TextAlign.Center)
   279. .maxLines(1)
   280. .constraintSize({ maxWidth: '100%', minHeight: 48 })

   282. Text('华为账号绑定号码')
   283. .fontSize($r('sys.float.ohos_id_text_size_body2'))
   284. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
   285. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
   286. .fontWeight(FontWeight.Regular)
   287. .lineHeight(19)
   288. .textAlign(TextAlign.Center)
   289. .maxLines(1)
   290. .constraintSize({ maxWidth: '100%' })
   291. .margin({
   292. top: 8
   293. })
   294. }.margin({
   295. top: 64
   296. })

   298. Column() {
   299. LoginWithHuaweiIDButton({
   300. params: {
   301. // LoginWithHuaweiIDButton支持的样式
   302. style: loginComponentManager.Style.BUTTON_RED,
   303. // 账号登录按钮在登录过程中展示加载态
   304. extraStyle: {
   305. buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
   306. show: true
   307. })
   308. },
   309. // LoginWithHuaweiIDButton的边框圆角半径
   310. borderRadius: 24,
   311. // LoginWithHuaweiIDButton支持的登录类型
   312. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
   313. // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
   314. supportDarkMode: true
   315. },
   316. controller: this.controller
   317. })
   318. }
   319. .height(40)
   320. .margin({
   321. top: 56
   322. })

   324. Column() {
   325. Button({
   326. type: ButtonType.Capsule,
   327. stateEffect: true
   328. }) {
   329. Text('其他方式登录')
   330. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
   331. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   332. .fontWeight(FontWeight.Medium)
   333. .fontSize($r('sys.float.ohos_id_text_size_button1'))
   334. .focusable(true)
   335. .focusOnTouch(true)
   336. .textOverflow({ overflow: TextOverflow.Ellipsis })
   337. .maxLines(1)
   338. .padding({ left: 8, right: 8 })
   339. }
   340. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
   341. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   342. .fontWeight(FontWeight.Medium)
   343. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   344. .focusable(true)
   345. .focusOnTouch(true)
   346. .constraintSize({ minHeight: 40 })
   347. .width('100%')
   348. .onClick(() => {
   349. hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
   350. })
   351. }.margin({ top: 16 })
   352. }.width('100%')

   354. Row() {
   355. Row() {
   356. Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
   357. .width(24)
   358. .height(24)
   359. .focusable(true)
   360. .focusOnTouch(true)
   361. .margin({ top: 0 })
   362. .select(this.isSelected)
   363. .onChange((value: boolean) => {
   364. if (value) {
   365. this.isSelected = true;
   366. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
   367. } else {
   368. this.isSelected = false;
   369. this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT_ACCEPTED);
   370. }
   371. hilog.info(this.domainId, this.logTag, `agreementChecked: ${value}`);
   372. })
   373. }

   375. Row() {
   376. Text() {
   377. ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
   378. if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
   379. Span(item?.text)
   380. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
   381. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
   382. .fontWeight(FontWeight.Regular)
   383. .fontSize($r('sys.float.ohos_id_text_size_body3'))
   384. } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
   385. Span(item?.text)
   386. .fontColor($r('sys.color.ohos_id_color_text_primary_activated'))
   387. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   388. .fontWeight(FontWeight.Medium)
   389. .fontSize($r('sys.float.ohos_id_text_size_body3'))
   390. .onClick(() => {
   391. // 应用需要根据item.tag实现协议页面的跳转逻辑
   392. hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
   393. // 华为账号用户认证协议
   394. if (item.tag === QuickLoginButtonComponent.USER_AUTHENTICATION_TAG) {
   395. this.jumpToPrivacyWebView();
   396. }
   397. })
   398. }
   399. }, (item: loginComponentManager.PrivacyText) => item.text.toString())
   400. }
   401. .width('100%')
   402. }
   403. .margin({ left: 12 })
   404. .layoutWeight(1)
   405. .constraintSize({ minHeight: 24 })
   406. }
   407. .alignItems(VerticalAlign.Top)
   408. .margin({
   409. top: 16,
   410. bottom: 16
   411. })
   412. }
   413. .justifyContent(FlexAlign.SpaceBetween)
   414. .constraintSize({ minHeight: '100%' })
   415. .margin({
   416. left: 16,
   417. right: 16
   418. })
   419. }
   420. .width('100%')
   421. .height('100%')
   422. }
   423. }

   425. @CustomDialog
   426. export struct AgreementDialog {
   427. logTag: string = 'AgreementDialog';
   428. domainId: number = 0x0000;
   429. dialogController?: CustomDialogController;
   430. cancel: () => void = () => {
   431. // 用户点击“取消”按钮，可于此处补充业务逻辑
   432. };
   433. confirm: () => void = () => {
   434. // 用户点击“同意并登录”按钮，可于此处补充业务逻辑
   435. };
   436. clickHyperlinkText: () => void = () => {
   437. // 用户点击超链接文本，可于此处补充业务逻辑
   438. };
   439. privacyText: loginComponentManager.PrivacyText[] = [];
   440. private static USER_AUTHENTICATION_TAG = '华为账号用户认证协议';

   442. build() {
   443. Column() {
   444. Row() {
   445. Text('用户协议与隐私条款')
   446. .id('loginPanel_agreement_dialog_privacy_title')
   447. .maxFontSize($r('sys.float.ohos_id_text_size_headline8'))
   448. .minFontSize($r('sys.float.ohos_id_text_size_body1'))
   449. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   450. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   451. .fontWeight(FontWeight.Bold)
   452. .textAlign(TextAlign.Center)
   453. .textOverflow({ overflow: TextOverflow.Ellipsis })
   454. .maxLines(2)
   455. }
   456. .alignItems(VerticalAlign.Center)
   457. .constraintSize({ minHeight: 56, maxWidth: 400 })
   458. .margin({
   459. left: $r('sys.float.ohos_id_max_padding_start'),
   460. right: $r('sys.float.ohos_id_max_padding_start')
   461. })

   463. Row() {
   464. Text() {
   465. ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
   466. if (item?.type === loginComponentManager.TextType.PLAIN_TEXT && item?.text) {
   467. Span(item?.text)
   468. .fontSize($r('sys.float.ohos_id_text_size_body1'))
   469. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   470. .fontFamily($r('sys.string.ohos_id_text_font_family_regular'))
   471. .fontWeight(FontWeight.Regular)
   472. } else if (item?.type === loginComponentManager.TextType.RICH_TEXT && item?.text) {
   473. Span(item?.text)
   474. .fontSize($r('sys.float.ohos_id_text_size_body1'))
   475. .fontColor('#CE0E2D')
   476. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   477. .fontWeight(FontWeight.Medium)
   478. .onClick(() => {
   479. // 应用需要根据item.tag实现协议页面的跳转逻辑
   480. hilog.info(this.domainId, this.logTag, `click privacy text tag: ${item.tag}`);
   481. // 华为账号用户认证协议
   482. if (item.tag === AgreementDialog.USER_AUTHENTICATION_TAG) {
   483. hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
   484. this.clickHyperlinkText();
   485. }
   486. })
   487. }
   488. }, (item: loginComponentManager.PrivacyText) => item.text.toString())
   489. }
   490. .width('100%')
   491. .textOverflow({ overflow: TextOverflow.Ellipsis })
   492. .maxLines(10)
   493. .textAlign(TextAlign.Start)
   494. .focusable(true)
   495. .focusOnTouch(true)
   496. .padding({ left: 24, right: 24 })
   497. }.width('100%')

   499. Flex({
   500. direction: FlexDirection.Row
   501. }) {
   502. Button('取消',
   503. { type: ButtonType.Capsule, stateEffect: true })
   504. .id('loginPanel_agreement_cancel_btn')
   505. .fontColor($r('sys.color.ohos_id_color_text_primary'))
   506. .fontSize($r('sys.float.ohos_id_text_size_button1'))
   507. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   508. .backgroundColor(Color.Transparent)
   509. .fontWeight(FontWeight.Medium)
   510. .focusable(true)
   511. .focusOnTouch(true)
   512. .constraintSize({ minHeight: 40, maxWidth: 400 })
   513. .width('50%')
   514. .onClick(() => {
   515. hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
   516. this.cancel();
   517. })

   519. Button('同意并登录',
   520. { type: ButtonType.Capsule, stateEffect: true })
   521. .id('loginPanel_agreement_dialog_huawei_id_login_btn')
   522. .fontColor(Color.White)
   523. .backgroundColor('#CE0E2D')
   524. .fontSize($r('sys.float.ohos_id_text_size_button1'))
   525. .fontFamily($r('sys.string.ohos_id_text_font_family_medium'))
   526. .fontWeight(FontWeight.Medium)
   527. .focusable(true)
   528. .focusOnTouch(true)
   529. .constraintSize({ minHeight: 40, maxWidth: 400 })
   530. .width('50%')
   531. .onClick(() => {
   532. hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
   533. this.confirm();
   534. })
   535. }
   536. .margin({
   537. top: 8,
   538. left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
   539. right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
   540. bottom: 16
   541. })
   542. }.backgroundColor($r('sys.color.ohos_id_color_dialog_default_bg'))
   543. .padding({
   544. left: 16,
   545. right: 16
   546. })
   547. }
   548. }

   550. export enum ErrorCode {
   551. // 账号未登录
   552. ERROR_CODE_LOGIN_OUT = 1001502001,
   553. // 该账号不支持一键登录，如海外账号
   554. ERROR_CODE_NOT_SUPPORTED = 1001500003,
   555. // 网络错误
   556. ERROR_CODE_NETWORK_ERROR = 1001502005,
   557. // 内部错误
   558. ERROR_CODE_INTERNAL_ERROR = 1001502009,
   559. // 用户取消授权
   560. ERROR_CODE_USER_CANCEL = 1001502012,
   561. // 系统服务异常
   562. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   563. // 用户未同意用户协议
   564. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001,
   565. // 参数错误
   566. ERROR_CODE_PARAMETER_ERROR = 401,
   567. // 重复请求
   568. ERROR_CODE_REQUEST_REFUSE = 1001500002
   569. }
   ```

   以下是华为账号用户认证协议展示页示例代码：

   ```
   1. import { webview } from '@kit.ArkWeb';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 华为账号用户认证协议展示页
   6. @Entry
   7. @Component
   8. struct WebPage {
   9. @State webUrl?: string = '';
   10. @State progress: number = 0;
   11. logTag: string = 'WebPage';
   12. domainId: number = 0x0000;
   13. controller: webview.WebviewController = new webview.WebviewController();

   15. build() {
   16. Column() {
   17. Column() {
   18. Button({ type: ButtonType.Normal }) {
   19. Image($r('sys.media.ohos_ic_compnent_titlebar_back'))
   20. .backgroundColor(Color.Transparent)
   21. .borderRadius(20)
   22. .width(24)
   23. .height(24)
   24. .draggable(false)
   25. .autoResize(false)
   26. .focusable(true)
   27. .fillColor($r('sys.color.ohos_id_color_titlebar_icon'))
   28. .matchTextDirection(true)
   29. }
   30. .alignSelf(ItemAlign.Start)
   31. .backgroundColor($r('sys.color.ohos_id_color_button_normal'))
   32. .borderRadius(20)
   33. .width(40)
   34. .height(40)
   35. .onClick(() => {
   36. this.getUIContext().getRouter().back();
   37. })
   38. }
   39. .height(56)
   40. .width('100%')
   41. .justifyContent(FlexAlign.Center)
   42. .margin({
   43. top: 36,
   44. left: 16
   45. })

   47. Progress({ value: this.progress, type: ProgressType.Linear })
   48. .width('100%')
   49. .visibility(this.progress <= 99 ? Visibility.Visible : Visibility.None)

   51. Web({ src: this.webUrl ?? '', controller: this.controller })
   52. .backgroundColor(Color.Transparent)
   53. .margin({ bottom: 60 })
   54. .onProgressChange((event) => {
   55. hilog.info(this.domainId, this.logTag,
   56. 'onProgressChange: ', (event ? event.newProgress : -1));
   57. this.progress = event ? event.newProgress : 0;
   58. })
   59. .darkMode(WebDarkMode.Auto)
   60. .forceDarkAccess(true)
   61. .onLoadIntercept((event) => {
   62. hilog.info(this.domainId, this.logTag, 'onLoadIntercept');
   63. return false;
   64. })
   65. .onErrorReceive((event) => {
   66. if (event) {
   67. hilog.error(this.domainId, this.logTag, `onErrorReceive,errorInfo: ${event?.error?.getErrorInfo()}`);
   68. }
   69. })
   70. }
   71. .alignItems(HorizontalAlign.Start)
   72. .padding({ left: 12, right: 12, bottom: 60 })
   73. .width('100%')
   74. .height('100%')
   75. }

   77. aboutToAppear(): void {
   78. hilog.info(0x0000, 'testTag', 'aboutToAppear');
   79. const params = this.getUIContext().getRouter().getParams() as Record<string, string>;
   80. this.webUrl = params.url ?? '';
   81. hilog.info(0x0000, 'testTag', `webUrl: ${this.webUrl}`);
   82. }

   84. aboutToDisappear(): void {
   85. hilog.info(0x0000, 'testTag', 'aboutToDisappear');
   86. if (this.webUrl) {
   87. try {
   88. this.controller.stop();
   89. } catch (error) {
   90. hilog.error(0x0000, 'testTag',
   91. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
   92. }
   93. }
   94. }
   95. }
   ```

### 用户非首次登录应用（可选）

用户非首次登录应用流程请参考[首次登录应用开发流程](account-phone-unionid-login.md#用户首次登录应用-1)中的导入模块及获取匿名手机号，获取[AuthorizationWithHuaweiIDResponse](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidresponse)响应结果中的Authorization Code。可能存在的异常场景及处理方法，可参考表1 获取匿名手机号错误码处理。

正确获取到Authorization Code，开发者可将Authorization Code传给应用服务端用于获取用户身份标识（UnionID、OpenID），即可查询该用户是否已关联。

1）如已关联，结合风控、安全因素及自身业务场景判断，可展示已关联的账号，由用户选择是否使用华为账号登录应用，或免用户操作，静默登录应用，客户端开发结束。

2）如未关联，则参考[首次登录应用开发流程](account-phone-unionid-login.md#用户首次登录应用-1)中的展示一键登录页面并获取Authorization Code继续开发。

### 借助DevEco Studio辅助开发（可选）

1. 打开需要提供一键登录功能的页面，在页面的build()中创建一个容器（如Column）。
2. 在DevEco Studio菜单栏点击View > Tool Windows > Kit Assistant，或使用快捷键Alt + K，进入Kit Assistant页面。
3. 在左侧目录中点击选中AccountKit > QuickLoginButton，并拖拽至新创建的容器中。即可在当前位置插入相应的代码片段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/F33Kza61QROHotOmO4r1OQ/zh-cn_image_0000002558605592.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=54C9FB46BDF5FFCCD062283F4A46663BBEB756641F6ADB8148BE942440C5A0BD)

   若代码片段插入失败，可查询[快速插入场景化代码片段](ide-kit-assistant.md)的说明排查原因。
4. 在自动生成的代码段的getQuickLoginAnonymousPhone函数中，执行executeRequest函数可获取响应结果。

   根据获取的响应结果判断，可能存在以下场景：

   * 已正确获取到用户匿名手机号及Authorization Code，开发者可将Authorization Code传给应用服务端用于获取用户身份标识（UnionID、OpenID），即可查询该用户是否已关联。

     1）如已关联，结合风控、安全因素及自身业务场景判断，可展示已关联的账号，由用户选择是否使用华为账号登录应用，或免用户操作，静默登录应用，客户端开发结束。

     2）如未关联，再判断是否存在下面的异常场景，如无，则参考下面步骤5继续开发。
   * 存在如下异常场景：

     1）返回[1001502001 用户未登录华为账号](../harmonyos-references/account-api-error-code.md#section1001502001-用户未登录华为账号)错误码，说明华为账号未登录。

     2）返回[1001500003 不支持该scopes或permissions](../harmonyos-references/account-api-error-code.md#section1001500003-不支持该scopes或permissions)错误码，说明华为账号用户注册地为中国境外、香港特别行政区、澳门特别行政区或中国台湾。

     3）获取到的匿名手机号为空，说明华为账号没有绑定手机号、权限未申请或未生效。

     上述异常场景应用需要展示其他登录方式。
5. 根据上述代码实现应用的登录页面，并展示华为账号一键登录按钮和华为账号用户认证协议（Account Kit提供跳转链接，应用需实现协议跳转，参见[约束与限制](account-phone-unionid-login.md#约束与限制)第2点），用户同意协议并点击一键登录按钮后，可获取到Authorization Code，将该值传给应用服务端用于获取用户信息（完整手机号、UnionID、OpenID）。

## 服务端开发

1. 应用服务端使用Client ID、Client Secret、Authorization Code调用[/oauth2/v6/quickLogin/getPhoneNumber接口](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md#接口原型)获取完整手机号和华为账号用户标识UnionID。
2. 应用通过获取到的完整手机号或UnionID查询该用户是否已关联应用系统数据库。如已关联，则绑定获取的UnionID与手机号到已有用户上（如已绑定，则可忽略），完成用户登录；如未关联，则创建新用户并绑定手机号与UnionID到该用户上。

## 客户端与服务端交互开发

### 应用客户端到应用服务端的开发

业务流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/pRFCiYrISwiW8UmFRdaHcQ/zh-cn_image_0000002589325119.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=BBC559D2E2CD62013C072EBB0E587163536D356D6D9639B76F4B82AA1D98EE40)

* 准备：

1. 请先完成应用客户端一键登录的相关开发，相关开发指导参考[客户端开发](account-phone-unionid-login.md#客户端开发)；
2. 参考[使用fetch发送网络请求](remote-communication-netsend-arkts.md#如何使用fetch发起网络请求)完成客户端到服务端的接口请求，开发步骤如下；

   1. 在应用客户端调用应用服务端提供的接口，将Authorization Code传输给应用的服务端；

      注意

      应用客户端与应用服务端的交互安全需要应用自行保证。

      ```
      1. import { rcp } from '@kit.RemoteCommunicationKit';
      2. import { hilog } from '@kit.PerformanceAnalysisKit';
      3. import { util } from '@kit.ArkTS';
      4. import { BusinessError } from '@kit.BasicServicesKit';

      6. // 客户端请求接口示例代码
      7. export function rcpRequest(authCode: string) {
      8. // 定义请求头
      9. const headers: rcp.RequestHeaders = {
      10. 'accept': 'application/json'
      11. };
      12. // 定义要传递的参数
      13. const postMessage: Record<string, string> = {
      14. 'authorizationCode': authCode
      15. };
      16. const securityConfig: rcp.SecurityConfiguration = {
      17. tlsOptions: {
      18. tlsVersion: 'TlsV1.3'
      19. }
      20. };
      21. // 假设"http://localhost:8080"为应用服务端地址
      22. const baseUrl = 'http://localhost:8080/login';
      23. // 定义请求对象
      24. const req = new rcp.Request(baseUrl, 'POST', headers, postMessage);
      25. try {
      26. // 创建通信会话对象
      27. const session = rcp.createSession({ requestConfiguration: { security: securityConfig } });
      28. // 发起请求
      29. session.fetch(req).then((response) => {
      30. hilog.info(0x0000, 'getRcpResult', 'Succeeded in getting result from server.');
      31. if (response.body) {
      32. const decoder = util.TextDecoder.create('utf-8');
      33. const result = JSON.parse(decoder.decodeToString(new Uint8Array(response.body))) as Record<string, Object>;
      34. // 此为代码示例，具体实现请以业务服务端实际返回数据结构为准
      35. const phoneNumber: string = JSON.stringify(result['phone'] ?? '');
      36. if (phoneNumber) {
      37. // 应用处理相关逻辑
      38. }
      39. } else {
      40. hilog.error(0x0000, 'getRcpResult', 'Failed to get response body.');
      41. }
      42. }).catch((err: BusinessError) => {
      43. hilog.error(0x0000, 'getRcpResult', `err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
      44. });
      45. } catch (err) {
      46. hilog.error(0x0000, 'getRcpResult', `err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
      47. }
      48. }
      ```
   2. 应用服务端提供接口用于接收应用客户端获取到的Authorization Code；

      java示例代码：

      ```
      1. import com.huawei.account.common.Response;
      2. import com.huawei.account.entity.PhoneNumberResp;
      3. import com.huawei.account.entity.LoginReq;
      4. import com.huawei.account.service.impl.LoginService;
      5. import lombok.RequiredArgsConstructor;
      6. import org.springframework.web.bind.annotation.RestController;
      7. import org.springframework.web.bind.annotation.PostMapping;
      8. import org.springframework.web.bind.annotation.RequestBody;

      10. @RestController
      11. @RequiredArgsConstructor
      12. public class QuickLoginController {
      13. private final LoginService loginService;

      15. @PostMapping("/login")
      16. public Response login(@RequestBody LoginReq requestBody) {
      17. PhoneNumberResp accountInfo = loginService.loginWithHuawei(requestBody.getAuthorizationCode());
      18. return new Response(200, "login success!", accountInfo);
      19. }
      20. }
      ```

      python示例代码：

      ```
      1. from flask import Flask, request, jsonify

      3. from service.loginService import login_with_huawei

      5. app = Flask(__name__)

      7. @app.route('/login', methods=['POST'])
      8. def login():
      9. # 验证请求参数
      10. request_data = request.get_json()
      11. if not request_data or 'authorizationCode' not in request_data:
      12. return jsonify({
      13. 'code': 400,
      14. 'message': 'invalid authorizationCode',
      15. 'data': None
      16. })
      17. authorization_code = request_data['authorizationCode']

      19. # 调用服务层
      20. user_info = login_with_huawei(authorization_code)
      21. if not user_info:
      22. return jsonify({
      23. 'code': 401,
      24. 'message': 'Failed to authenticate with Huawei',
      25. 'data': None
      26. })

      28. # 成功响应
      29. return jsonify({
      30. 'code': 200,
      31. 'message': 'Login successful',
      32. 'data': user_info
      33. })

      36. if __name__ == '__main__':
      37. app.run(debug=True, port=8080)
      ```

      go示例代码：

      ```
      1. package main

      3. import (
      4. loginService "./service"
      5. "encoding/json"
      6. "errors"
      7. "fmt"
      8. _ "fmt"
      9. "io/ioutil"
      10. "log"
      11. "net/http"
      12. _ "strconv"
      13. )

      15. type LoginRequest struct {
      16. AuthorizationCode string `json:"authorizationCode"`
      17. }

      19. type Response struct {
      20. UserInfo UserInfo `json:"data"`
      21. Code     int      `json:"code"`
      22. Message  string   `json:"message"`
      23. }

      25. type UserInfo struct {
      26. OpenID            string `json:"openId"`
      27. UnionID           string `json:"unionId"`
      28. LoginMobileNumber string `json:"phoneNumber"`
      29. LoginMobileValid  int    `json:"phoneNumberValid"`
      30. PurePhoneNumber   string `json:"purePhoneNumber"`
      31. PhoneCountryCode  string `json:"phoneCountryCode"`
      32. }

      34. type PhoneNumberErrRsp struct {
      35. ResultCode int    `json:"resultCode"`
      36. ResultDesc string `json:"resultDesc"`
      37. }

      39. func loginHandler(w http.ResponseWriter, r *http.Request) {
      40. // 设置通用JSON响应头
      41. w.Header().Set("Content-Type", "application/json")
      42. // 1. 请求体解析
      43. var loginRequest LoginRequest
      44. if err := parseLoginRequest(r, &loginRequest); err != nil {
      45. sendErrorResponse(w, http.StatusBadRequest, "Invalid request format")
      46. return
      47. }
      48. // 2. 服务调用
      49. resp, err := loginService.LoginWithHuawei(loginRequest.AuthorizationCode)
      50. if err != nil {
      51. log.Printf("Login service error: %v", err)
      52. sendErrorResponse(w, http.StatusInternalServerError, "Authentication failed")
      53. return
      54. }
      55. defer resp.Body.Close()
      56. // 3. 响应处理
      57. userInfo, err := processUserInfoResponse(resp)
      58. if err != nil {
      59. log.Printf("User info processing error: %v", err)
      60. sendErrorResponse(w, http.StatusInternalServerError, "Failed to process user data")
      61. return
      62. }
      63. // 4. 成功响应
      64. sendSuccessResponse(w, userInfo)
      65. }

      67. func parseLoginRequest(r *http.Request, dest *LoginRequest) error {
      68. body, err := ioutil.ReadAll(r.Body)
      69. if err != nil {
      70. return fmt.Errorf("failed to read request body: %v", err)
      71. }
      72. defer r.Body.Close()
      73. if err := json.Unmarshal(body, dest); err != nil {
      74. return fmt.Errorf("invalid JSON format: %v", err)
      75. }
      76. if dest.AuthorizationCode == "" {
      77. return errors.New("missing authorization code")
      78. }
      79. return nil
      80. }

      82. func processUserInfoResponse(resp *http.Response) (*UserInfo, error) {
      83. if resp.StatusCode != http.StatusOK {
      84. return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
      85. }
      86. respBody, err := ioutil.ReadAll(resp.Body)
      87. var phoneNumberErrRsp PhoneNumberErrRsp
      88. err = json.Unmarshal(respBody, &phoneNumberErrRsp)
      89. if err != nil {
      90. return nil, fmt.Errorf("failed to unmarshal response body: %v", err)
      91. }
      92. if phoneNumberErrRsp.ResultCode != 0 {
      93. return nil, fmt.Errorf("api error %d: %s", phoneNumberErrRsp.ResultCode, phoneNumberErrRsp.ResultDesc)
      94. }
      95. var userInfo UserInfo
      96. err = json.Unmarshal(respBody, &userInfo)
      97. if err != nil {
      98. return nil, fmt.Errorf("failed to unmarshal response body: %v", err)
      99. }

      101. /*
      102. 根据业务设计流程，在数据库中查询用户信息，比如：
      103. 1、使用UnionID查询用户，匹配到了则返回用户信息；
      104. 2、未匹配到则使用手机号查询用户，查到了则将华为账号UnionID关联到该用户，返回用户信息；
      105. 3、UnionID和手机号均没有匹配到，则进入注册流程
      106. */

      108. return &userInfo, nil
      109. }

      111. func sendErrorResponse(w http.ResponseWriter, statusCode int, message string) {
      112. w.WriteHeader(statusCode)
      113. response := Response{
      114. Code:    statusCode,
      115. Message: message,
      116. }
      117. if err := json.NewEncoder(w).Encode(response); err != nil {
      118. log.Printf("Failed to encode error response: %v", err)
      119. }
      120. }

      122. func sendSuccessResponse(w http.ResponseWriter, userInfo *UserInfo) {
      123. response := Response{
      124. Code:     http.StatusOK,
      125. Message:  "Login successful",
      126. UserInfo: *userInfo,
      127. }
      128. if err := json.NewEncoder(w).Encode(response); err != nil {
      129. log.Printf("Failed to encode success response: %v", err)
      130. w.WriteHeader(http.StatusInternalServerError)
      131. }
      132. }

      134. func main() {
      135. http.HandleFunc("/login", loginHandler)
      136. log.Println("Server starting on :8080...")
      137. if err := http.ListenAndServe(":8080", nil); err != nil {
      138. log.Fatalf("Server failed: %v", err)
      139. }
      140. }
      ```

      php示例代码：

      ```
      1. <?php

      3. require __DIR__ . '/../service/LoginService.php';

      5. // 初始化路由
      6. $router = new Router();
      7. $router->addRoute('POST', '/login', function($request) {
      8. // 获取POST数据
      9. $requestBody = json_decode(file_get_contents('php://input'), true);
      10. if (isset($requestBody['authorizationCode'])) {
      11. // 调用服务层进行登录验证
      12. $userInfo = LoginService::loginWithHuawei($requestBody['authorizationCode']);
      13. if (!isset($userInfo)) {
      14. echo json_encode([
      15. 'code' => 500,
      16. 'message' => 'login failed!'
      17. ]);
      18. return;
      19. }

      21. // 返回响应
      22. echo json_encode([
      23. 'data' => $userInfo,
      24. 'code' => 200,
      25. 'message' => 'login success!'
      26. ]);
      27. } else {
      28. echo json_encode(['code' => 400, 'message' => 'Missing authorization code']);
      29. }
      30. });

      32. // 处理请求
      33. $router->dispatch($_SERVER['REQUEST_METHOD'], parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
      34. class Router {
      35. private $routes = [];

      37. public function addRoute($method, $path, $handler) {
      38. $this->routes[strtoupper($method)][$path] = $handler;
      39. }

      41. public function dispatch($method, $uri) {
      42. header('Content-Type: application/json');
      43. $method = strtoupper($method);
      44. // 精确匹配路由
      45. if (isset($this->routes[$method][$uri])) {
      46. $handler = $this->routes[$method][$uri];
      47. $handler($_REQUEST);
      48. return;
      49. }

      51. // 未找到路由
      52. echo json_encode([
      53. 'message' => 'Not Found',
      54. 'code' => 404
      55. ]);
      56. }
      57. }
      ```
   3. 应用服务端获取到Authorization Code之后，对接华为账号服务器，参考[服务端开发](account-phone-unionid-login.md#服务端开发)，调用[/oauth2/v6/quickLogin/getPhoneNumber接口](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md#接口原型)获取完整手机号、UnionID、OpenID；
   4. 根据获取的UnionID、OpenID、完整手机号，判断登录用户是否为新用户、是否已关联等等（根据实际业务开发）；
   5. 保存或更新用户信息到应用服务端，完成处理后，返回登录用户的信息至应用客户端；

      java示例代码：

      ```
      1. import com.alibaba.fastjson2.JSONObject;
      2. import com.huawei.account.config.AGCProperties;
      3. import com.huawei.account.config.Constants;
      4. import com.huawei.account.entity.PhoneNumberReq;
      5. import com.huawei.account.entity.PhoneNumberResp;
      6. import com.huawei.account.util.HttpUtil;
      7. import lombok.RequiredArgsConstructor;
      8. import lombok.extern.slf4j.Slf4j;
      9. import org.springframework.stereotype.Service;

      11. @Slf4j
      12. @Service
      13. @RequiredArgsConstructor
      14. public class LoginService {
      15. private final HttpUtil httpService;

      17. private final AGCProperties agcProperties;

      19. public PhoneNumberResp loginWithHuawei(String authorizationCode) {
      20. PhoneNumberReq phoneNumberReq = new PhoneNumberReq();
      21. phoneNumberReq.setClientId(agcProperties.getClientId()); // 读取配置项中Client ID
      22. phoneNumberReq.setClientSecret(agcProperties.getClientSecret()); // 读取配置项中Client Secret
      23. phoneNumberReq.setCode(authorizationCode);
      24. PhoneNumberResp phoneNumberResp = httpService.callHttpPost(Constants.QUICK_LOGIN_PHONE_NUMBER_URL, phoneNumberReq, PhoneNumberResp.class).getBody();
      25. log.info("/oauth2/v6/quickLogin/getPhoneNumber response body is: {}", JSONObject.toJSONString(phoneNumberResp));

      27. // 数据库相关：
      28. // 使用UnionID查询用户，匹配到了则返回用户信息；
      29. // 未匹配到则使用手机号查询用户，查到了则关联华为账号UnionID，返回用户信息；
      30. // UnionID和手机号均没有匹配到，则进入注册流程

      32. return phoneNumberResp;
      33. }
      34. }
      ```

      python示例代码：

      ```
      1. import requests
      2. import json
      3. import os

      5. parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
      6. target_file = os.path.join(parent_dir, "config", "agc.json")
      7. with open(target_file) as f:
      8. agc_config = json.load(f)

      10. def login_with_huawei(authorization_code):
      11. # 配置信息
      12. client_id = agc_config["clientId"] # 读取配置项中Client ID
      13. client_secret = agc_config["clientSecret"] # 读取配置项中Client Secret
      14. phone_number_url = "https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber"

      16. # 构建请求体
      17. token_request_body = {
      18. "clientId": client_id,
      19. "clientSecret": client_secret,
      20. "code": authorization_code
      21. }

      23. # 发送请求获取一键登录用户手机号等信息
      24. user_info_response = {}
      25. try:
      26. user_info_response = requests.post(phone_number_url, headers={'Content-Type': 'application/json'}, json=token_request_body)
      27. user_info_response.raise_for_status()  # 如果请求失败，抛出HTTPError异常
      28. user_info = json.loads(user_info_response.content.decode('utf-8'))
      29. except requests.RequestException as e:
      30. user_info = json.loads(user_info_response.content.decode('utf-8'))
      31. print(f"Error retrieving /oauth2/v6/quickLogin/getPhoneNumber: {e}")
      32. print(f"Error retrieving /oauth2/v6/quickLogin/getPhoneNumber: {user_info}")
      33. return None
      34. if "resultCode" in user_info:
      35. assert user_info["resultCode"] == 0

      37. # 根据业务设计流程，在数据库中查询用户信息，比如：
      38. # 1、使用UnionID查询用户，匹配到了则返回用户信息；
      39. # 2、未匹配到则使用手机号查询用户，查到了则将华为账号UnionID关联到该用户，返回用户信息；
      40. # 3、UnionID和手机号均没有匹配到，则进入注册流程

      42. return user_info
      ```

      go示例代码：

      ```
      1. package service

      3. import (
      4. "bytes"
      5. "encoding/json"
      6. "fmt"
      7. "io/ioutil"
      8. "net"
      9. "net/http"
      10. "path/filepath"
      11. "sync"
      12. "time"
      13. )

      15. type Response struct {
      16. Data    interface{} `json:"data"`
      17. Code    int         `json:"code"`
      18. Message string      `json:"message"`
      19. }

      21. type PhoneNumberReq struct {
      22. ClientId     string `json:"clientId"`
      23. ClientSecret string `json:"clientSecret"`
      24. Code         string `json:"code"`
      25. }

      27. var httpClient = &http.Client{
      28. Transport: &http.Transport{
      29. DialContext: (&net.Dialer{
      30. Timeout: 5 * time.Second,
      31. }).DialContext,
      32. TLSHandshakeTimeout:   5 * time.Second,
      33. ResponseHeaderTimeout: 10 * time.Second,
      34. },
      35. Timeout: 30 * time.Second,
      36. }

      38. var (
      39. config     *Config
      40. configOnce sync.Once
      41. configErr  error
      42. )

      44. type Config struct {
      45. ClientID     string `json:"clientId"`
      46. ClientSecret string `json:"clientSecret"`
      47. }

      49. func LoadConfig() (*Config, error) {
      50. configOnce.Do(func() {
      51. data, err := ioutil.ReadFile(filepath.Join("src", "config", "agc.json"))
      52. if err != nil {
      53. configErr = err
      54. return
      55. }
      56. var cfg Config
      57. if err := json.Unmarshal(data, &cfg); err != nil {
      58. configErr = err
      59. return
      60. }
      61. config = &cfg
      62. })
      63. return config, configErr
      64. }

      66. func LoginWithHuawei(authorizationCode string) (*http.Response, error) {
      67. config, err := LoadConfig()
      68. if err != nil {
      69. return nil, err
      70. }
      71. // 1. 构造请求体
      72. reqBody := PhoneNumberReq{
      73. ClientId:     config.ClientID,
      74. ClientSecret: config.ClientSecret,
      75. Code:         authorizationCode,
      76. }
      77. // 2. 序列化为JSON
      78. jsonData, err := json.Marshal(reqBody)
      79. resp, err := httpClient.Post("https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber", "application/json", bytes.NewBuffer(jsonData))
      80. if err != nil {
      81. fmt.Errorf("failed to make POST request: %v, %v", config.ClientID, config.ClientSecret)
      82. return nil, fmt.Errorf("failed to make POST request: %v", err)
      83. }
      84. return resp, nil
      85. }
      ```

      php示例代码：

      ```
      1. <?php

      3. class LoginService {
      4. public static function loginWithHuawei($authorizationCode) {
      5. $agcConfig = require __DIR__ . '/../config/agc.php';
      6. $requestBody = [
      7. 'clientId' => $agcConfig['clientId'],
      8. 'clientSecret' => $agcConfig['clientSecret'],
      9. 'code' => $authorizationCode
      10. ];

      12. $ch = curl_init();
      13. curl_setopt_array($ch,
      14. [
      15. CURLOPT_RETURNTRANSFER => true,
      16. CURLOPT_POST => true,
      17. CURLOPT_HTTPHEADER => [
      18. 'Content-Type: application/json',
      19. 'Accept: application/json'
      20. ],
      21. CURLOPT_SSL_VERIFYPEER => false,
      22. CURLOPT_SSL_VERIFYHOST => false,
      23. CURLOPT_URL => 'https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber',
      24. CURLOPT_POSTFIELDS => json_encode($requestBody)
      25. ]);

      27. $response = curl_exec($ch);
      28. if ($response === false) {
      29. error_log('cURL Error: ' . curl_error($ch));
      30. curl_close($ch);
      31. return null;
      32. }

      34. $userInfo = json_decode($response, true);
      35. curl_close($ch);
      36. if (!isset($data['resultCode']) && $userInfo['resultCode'] != 0) {
      37. error_log('cURL Error: ' . curl_error($ch));
      38. curl_close($ch);
      39. }

      41. /**
      42. * 根据业务设计流程，在数据库中查询用户信息，比如：
      43. * 1、使用UnionID查询用户，匹配到了则返回用户信息；
      44. * 2、未匹配到则使用手机号查询用户，查到了则将华为账号UnionID关联到该用户，返回用户信息；
      45. * 3、UnionID和手机号均没有匹配到，则进入注册流程
      46. */

      48. return $userInfo;
      49. }
      50. }
      ```

### 客户端与服务端联调

前提：根据应用登录方案设计及实现，完成客户端和服务端开发，开发指导参见[客户端开发](account-phone-unionid-login.md#客户端开发)、[服务端开发](account-phone-unionid-login.md#服务端开发)和[应用客户端到应用服务端的开发](account-phone-unionid-login.md#应用客户端到应用服务端的开发)。

1. 在客户端获取到Authorization Code之后，传送给服务端接口；在服务端使用Authorization Code获取华为账号绑定的手机号、UnionID、OpenID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/jnOPjp-JTZqceO95VlIj1A/zh-cn_image_0000002589245055.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=A1DF0469F848AC1C5D4378338DB985CF83A7F7FDAE5FE86988695C43EFB60C03)
2. 根据应用登录方案使用华为账号绑定的手机号、UnionID、OpenID登录成功后，应用服务端返回用户信息给应用客户端，应用客户端可根据需要进行本地持久化存储，例如：登录状态、用户账号名、手机号、用户身份标识等。
3. 在应用客户端首页或个人信息页等位置，对当前登录用户信息进行展示，举例如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/BhtEGNBOTwC0whn9lMvL_A/zh-cn_image_0000002558765250.png?HW-CC-KV=V1&HW-CC-Date=20260429T053622Z&HW-CC-Expire=86400&HW-CC-Sign=A86B0EB56376DE4A9A75631198BAA4431B12C283054FFD509768435098439A8A "点击放大")

## 开发后验证

### 集成华为账号一键登录能力应用用户体验质量建议

应用完成开发后，可参照以下标准检查集成华为账号一键登录后的用户体验是否符合预期：

| 标准编号 | 标准项名称 | 类型 | 标准详细描述 |
| --- | --- | --- | --- |
| 1 | 满足华为账号提供登录设计规范 | 规则 | 需满足[华为账号开放登录](../design-guides/id-0000001880001344.md)中 **[【华为账号一键登录】按钮](../design-guides/id-0000001880001344.md#section41792374210)** 规范，保障HarmonyOS应用拥有简单易用、高效一致、快速安全的登录体验； |
| 2 | 用户交互体验原则 | 建议 | （1）登录页面的用户协议与隐私协议、华为账号用户认证协议可展示、可点击；  （2）当用户点击协议后，回退页面，须回到点击前的页面；  （3）只有用户勾选并同意所有协议后，才可继续进行登录操作，若用户未勾选协议时直接点击华为账号登录按钮，须有明确的同意协议提醒；  （4）点击登录按钮须直接完成登录流程，可出现头像、昵称授权页，但取消场景须不影响登录流程；若出现处理异常，须及时终止页面，不应出现应用卡死无法操作； |
| 3 | 登录页面内容用户体验原则 | 建议 | （1）若未提供其他登录方式，不应显示“其他登录方式”的入口；  （2）若使用华为账号一键登录，页面匿名手机号须展示从华为账号侧获取的匿名手机号，不应展示其他来源的手机号；  （3）用户协议中，必须包含[《华为账号用户认证协议》](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN)，且协议必须可点击、可加载，加载后支持回退页面，且回到点击前的页面； |
| 4 | 异常处理用户体验原则 | 建议 | 登录页面需进行异常处理保证：  （1）若登录异常（如网络异常、海外账号不支持等情况），勿将错误码等原始信息直接透传给用户；  （2）若登录时触发了华为侧的短信验证码校验，则在校验成功之后，应用不应再展示额外的验证码验证页面； |
| 5 | 应用生命周期变化的华为账号用户体验原则 | 建议 | 应用更新后，其登录状态须与更新前一致； |
