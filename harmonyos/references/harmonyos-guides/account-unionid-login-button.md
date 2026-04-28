---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-unionid-login-button
title: 使用“华为账号登录”按钮登录
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 登录 > 华为账号登录（获取UnionID/OpenID） > 使用“华为账号登录”按钮登录
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed782f84f34bccda127fe67563e279681545ceded03fae6ae0a3a5efdb0214aa
---

## 场景介绍

应用可以使用Account Kit提供的华为账号登录按钮及服务端交互获取华为账号用户身份标识UnionID、OpenID，通过UnionID、OpenID完成用户登录；或者与应用账号完成绑定，绑定后用于登录或者验证。

华为账号登录按钮包含文本、标志和文本、标志三种样式，以满足应用对界面风格一致性和灵活性的要求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/mCgUFe9LTtavCSUaJEJ2yg/zh-cn_image_0000002583478751.png?HW-CC-KV=V1&HW-CC-Date=20260427T234757Z&HW-CC-Expire=86400&HW-CC-Sign=CF71C73B0DEF1288062CB9CAC3FFDDE058E43CAB964683DD484227371C85CFB7)

## 约束与限制

华为账号按钮登录能力支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/LObQVpTQSdeWkTLB09tKFA/zh-cn_image_0000002552799102.png?HW-CC-KV=V1&HW-CC-Date=20260427T234757Z&HW-CC-Expire=86400&HW-CC-Sign=0BAEDB59C4AF04C331CA07F8DFD2B4EB6E64759C65638FDC18FDD408E929D717)

账号登录按钮的用户体验和UX设计需符合[【华为账号登录】按钮](../design-guides/id-0000001880001344.md#section2624430102713)规范，不符合规范的UX设计可能会对应用上架和用户体验带来影响。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/ZD2emAq3TQSxd9WcIT4buQ/zh-cn_image_0000002583438797.png?HW-CC-KV=V1&HW-CC-Date=20260427T234757Z&HW-CC-Expire=86400&HW-CC-Sign=8F7AE84A0C5D55D36B4A79DC8FF0487B6EE1A7CE72087506C01F69038716EA09)

流程说明：

1. 调用登录按钮展示登录页阶段（序号1-3）：

   1. 用户打开应用进行登录，应用设置[LoginType](../harmonyos-references/account-api-component-manager.md#logintype)类型为LoginType.ID后拉起应用自己的登录页并展示“华为账号登录”按钮，用户点击按钮，请求华为账号授权信息。
2. 用户点击登录阶段（序号4-6）：

   1. 如华为账号未登录，将拉起华为账号登录页，用户登录后，将返回Authorization Code等数据给应用。
   2. 如华为账号已登录，将直接返回Authorization Code等数据给应用。
3. 用户关联应用账号阶段（序号7-16）：

   1. 应用服务端通过Authorization Code获取到Access Token，再使用Access Token调用[解析凭证接口](../harmonyos-references/account-api-get-token-info.md#接口原型)获取用户相关信息。通过Authorization Code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。
   2. 应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录等功能。
   3. 应用对用户身份标识UnionID/OpenID、业务登录凭证SessionId信息进行认证后，通过UnionID/OpenID判断用户是否已关联应用系统数据库，如已关联，则完成用户登录；如未关联，则创建新用户，绑定UnionID/OpenID。

## 接口说明

华为账号登录按钮关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton) | 华为账号Button登录组件。  当前该组件支持Icon类型按钮、纯文本按钮、Icon和文本混合按钮，如果仍然不能满足开发者的诉求，可以使用[Style](../harmonyos-references/account-api-component-manager.md#style)的BUTTON\_CUSTOM值定义按钮的文字颜色和背景色。 |
| [onClickLoginWithHuaweiIDButton](../harmonyos-references/account-api-component-manager.md#onclickloginwithhuaweiidbutton-1)(callback: AsyncCallback<[HuaweiIDCredential](../harmonyos-references/account-api-component-manager.md#huaweiidcredential)>): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 注册华为账号登录按钮的登录事件结果回调。使用callback异步回调。 |
| [setAgreementStatus](../harmonyos-references/account-api-component-manager.md#setagreementstatus-1)(agreementStatus: [AgreementStatus](../harmonyos-references/account-api-component-manager.md#agreementstatus)): [LoginWithHuaweiIDButtonController](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttoncontroller) | 设置协议状态方法。如果需要用户同意协议才能完成华为账号登录，请先设置协议状态为NOT\_ACCEPTED，当用户同意协议后设置协议状态为ACCEPTED，才可以完成华为账号登录。 |

注意

上述接口需在页面或自定义组件生命周期内调用。

## 开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成[配置签名和指纹](account-sign-fingerprints.md)、[配置Client ID](account-client-id.md)。此场景无需申请账号权限。

## 客户端开发

1. 导入[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)模块及相关公共模块。

   ```
   1. import { LoginWithHuaweiIDButton, loginComponentManager } from '@kit.AccountKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton)组件，展示华为账号登录按钮，用户点击华为账号登录按钮后，应用获取到Authorization Code、ID Token，将数据传给应用服务端，可参考[客户端与服务端交互开发](account-phone-unionid-login.md#客户端与服务端交互开发)的开发步骤a和b，完成服务端开发。通过Authorization Code凭证获取用户信息可以有效避免黑客通过数据遍历、身份伪造、重放攻击等手段导致的安全风险。应用可以通过公开的网址获取到华为账号服务器发布的公钥，对签名和ID Token中的必要信息进行验证，以证明其没有被篡改过。解析ID Token可参考[ID Token解析与验证](account-faq-12.md#解析与验证)。

   ```
   1. @Entry
   2. @Component
   3. struct PreviewLoginButtonPage {
   4. // 构造LoginWithHuaweiIDButton组件的控制器
   5. controller: loginComponentManager.LoginWithHuaweiIDButtonController =
   6. new loginComponentManager.LoginWithHuaweiIDButtonController()
   7. .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
   8. if (error) {
   9. this.dealAllError(error);
   10. return;
   11. }

   13. if (response) {
   14. hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
   15. const authCode = response.authorizationCode;
   16. // 开发者处理authCode
   17. }
   18. });

   20. // 错误处理
   21. dealAllError(error: BusinessError): void {
   22. hilog.error(0x0000, 'testTag',
   23. `Failed to login, errorCode is ${error.code}, errorMessage is ${error.message}`);
   24. // 在应用登录涉及UI交互场景下，建议按照如下错误码指导提示用户
   25. if (error.code === ErrorCode.ERROR_CODE_LOGIN_OUT) {
   26. // 用户未登录华为账号，请登录华为账号并重试或者尝试使用其他方式登录
   27. } else if (error.code === ErrorCode.ERROR_CODE_NETWORK_ERROR) {
   28. // 网络异常，请检查当前网络状态并重试或者尝试使用其他方式登录
   29. } else if (error.code === ErrorCode.ERROR_CODE_INTERNAL_ERROR) {
   30. // 登录失败，请尝试使用其他方式登录
   31. } else if (error.code === ErrorCode.ERROR_CODE_USER_CANCEL) {
   32. // 用户取消授权
   33. } else if (error.code === ErrorCode.ERROR_CODE_SYSTEM_SERVICE) {
   34. // 系统服务异常，请稍后重试或者尝试使用其他方式登录
   35. } else if (error.code === ErrorCode.ERROR_CODE_REQUEST_REFUSE) {
   36. // 重复请求，应用无需处理
   37. } else if (error.code === ErrorCode.ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED) {
   38. // 用户未同意协议
   39. } else {
   40. // 应用登录失败，请尝试使用其他方式登录
   41. }
   42. }

   44. build() {
   45. Column() {
   46. Column() {
   47. Column() {
   48. LoginWithHuaweiIDButton({
   49. params: {
   50. // LoginWithHuaweiIDButton支持的样式
   51. style: loginComponentManager.Style.BUTTON_RED,
   52. // 账号登录按钮在登录过程中展示加载态
   53. extraStyle: {
   54. buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
   55. show: true
   56. })
   57. },
   58. // LoginWithHuaweiIDButton的边框圆角半径
   59. borderRadius: 24,
   60. // LoginWithHuaweiIDButton支持的登录类型
   61. loginType: loginComponentManager.LoginType.ID,
   62. // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
   63. supportDarkMode: true
   64. },
   65. controller: this.controller
   66. })
   67. }
   68. .height(40)
   69. }.width('100%')
   70. }
   71. .justifyContent(FlexAlign.Center)
   72. .constraintSize({ minHeight: '100%' })
   73. .margin({
   74. left: 16,
   75. right: 16
   76. })
   77. }
   78. }

   80. export enum ErrorCode {
   81. // 账号未登录
   82. ERROR_CODE_LOGIN_OUT = 1001502001,
   83. // 网络错误
   84. ERROR_CODE_NETWORK_ERROR = 1001502005,
   85. // 内部错误
   86. ERROR_CODE_INTERNAL_ERROR = 1001502009,
   87. // 用户取消授权
   88. ERROR_CODE_USER_CANCEL = 1001502012,
   89. // 系统服务异常
   90. ERROR_CODE_SYSTEM_SERVICE = 12300001,
   91. // 重复请求
   92. ERROR_CODE_REQUEST_REFUSE = 1001500002,
   93. // 用户未同意用户协议
   94. ERROR_CODE_AGREEMENT_STATUS_NOT_ACCEPTED = 1005300001
   95. }
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
