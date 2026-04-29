---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-byquicklogin
title: 通过华为账号一键登录获取用户风险等级
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 获取华为账号用户信息 > 获取风险等级 > 通过华为账号一键登录获取用户风险等级
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33e9cdbeaa2e63402d72f5a4f6e3e05bea837008a6c8ea898e3b859517120b15
---

## 场景介绍

应用登录风控场景，可以通过[华为账号一键登录](account-phone-unionid-login.md)获取用户风险等级，对恶意账号进行风控，提升应用的安全等级。

## 约束与限制

通过华为账号一键登录获取用户风险等级能力支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。

## 业务流程

**图1** 华为账号一键登录（用户首次登录应用）获取华为账号风险等级流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/gKE3GWZUTzCE_F5uGSVp0Q/zh-cn_image_0000002589245063.png?HW-CC-KV=V1&HW-CC-Date=20260429T053652Z&HW-CC-Expire=86400&HW-CC-Sign=1B9AFAAC20C359F126E402F549DC393C32D63B42AD9F681E96A0D48E892A87EA)

1. 参考[华为账号一键登录业务流程](account-phone-unionid-login.md#业务流程)，确保系统账号已登录，匿名手机号获取成功，且用户首次使用华为账号登录应用。（如用户非首次使用华为账号登录，可通过[华为账号其他方式登录获取用户风险等级](account-get-risklevel-on-demand-acquisition.md)来查询华为账号的风险等级）
2. 调用[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件，在[LoginWithHuaweiIDButtonParams](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)参数中设置风险等级字段标识riskLevel，拉起应用登录页。
3. 用户同意协议后，点击华为账号一键登录按钮，应用可以通过[HuaweiIDCredential](../harmonyos-references/account-api-component-manager.md#huaweiidcredential)获取到Authorization Code等数据。
4. 将获取的Authorization Code数据传给应用服务端，应用服务端通过调用[获取用户风险等级](../harmonyos-references/account-api-getuserrisklevel.md)接口查询当前登录用户的华为账号风险等级。
5. 应用基于用户风险等级判断继续登录流程或者返回对应风控措施。

## 接口说明

一键登录接口遵循[华为账号一键登录接口说明](account-phone-unionid-login.md#接口说明)，当应用需要获取用户风险等级时，在[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件参数[LoginWithHuaweiIDButtonParams](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)中传入riskLevel字段，通过一键登录返回Authorization Code查询用户的风险等级。

| 接口名 | 描述 |
| --- | --- |
| [LoginWithHuaweiIDButtonParams](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams) | [LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件参数，支持传入riskLevel字段（可选），标识一键登录后可查询用户风险等级。 |

## 开发前提

1. 在进行代码开发前，请确认已完成[一键登录开发前提](account-phone-unionid-login.md#开发前提)工作。
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

1. 一键登录前置流程（获取系统账号登录状态，获取系统账号匿名手机号）请参考[一键登录开发流程](account-phone-unionid-login.md#用户首次登录应用-1)中的导入模块及获取匿名手机号，确保系统账号已登录，匿名手机号获取成功，且用户首次通过华为账号登录该应用。
2. 参考[一键登录开发流程](account-phone-unionid-login.md#用户首次登录应用-1)中展示一键登录页面并获取Authorization Code的示例代码，在[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件参数params中设置riskLevel标识为true，其余示例代码保持不变，拉起应用登录页。

   ```
   1. LoginWithHuaweiIDButton({
   2. params: {
   3. // LoginWithHuaweiIDButton支持的样式
   4. style: loginComponentManager.Style.BUTTON_RED,
   5. // 账号登录按钮在登录过程中展示加载态
   6. extraStyle: {
   7. buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
   8. show: true
   9. })
   10. },
   11. // LoginWithHuaweiIDButton的边框圆角半径
   12. borderRadius: 24,
   13. // LoginWithHuaweiIDButton支持的登录类型
   14. loginType: loginComponentManager.LoginType.QUICK_LOGIN,
   15. // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
   16. supportDarkMode: true,
   17. // verifyPhoneNumber：如果华为账号用户在过去90天内未进行短信验证，是否拉起Account Kit提供的短信验证码页面
   18. verifyPhoneNumber: true,
   19. // riskLevel：标识应用期望在登录后获取华为账号的风险等级
   20. riskLevel: true,
   21. },
   22. controller: this.controller
   23. })
   ```
3. 用户同意协议并点击一键登录按钮后，可获取到Authorization Code，将该值传给应用服务端用于获取用户风险等级。

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
3. 应用基于风险等级判别用户风险程度，决定是否需要对用户进行额外验证或拦截用户行为。
