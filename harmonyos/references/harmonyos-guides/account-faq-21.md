---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-21
title: 60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:18c9ecd9fa0b33ddb5b57ca256e494107a153dd367145d47198fabe82b5e7e39
---

**问题现象**

调用服务器接口/oauth2/v6/quickLogin/getPhoneNumber时出现错误60180007，无法获取华为账号的一键登录手机号。

**可能原因**

1. 在进行华为账号一键登录功能开发时，登录按钮的[LoginWithHuaweiIDButtonParams.loginType](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)属性未设置为LoginType.QUICK\_LOGIN。
2. 客户端传给服务器的Authorization Code，是通过华为账号一键登录预取号阶段获取到的Authorization Code。
3. 客户端传给服务器的Authorization Code，不是华为账号一键登录场景获取到的。

**解决措施**

1. 在获取到的匿名手机号和隐私协议在一键登录页面展示时，登录按钮的[LoginWithHuaweiIDButtonParams.loginType](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)属性需设置为LoginType.QUICK\_LOGIN，完整示例代码请参考一键登录[客户端开发](account-phone-unionid-login.md#客户端开发)的步骤**3.展示一键登录页面并获取Authorization Code**。

   ```typescript
   import { loginComponentManager } from '@kit.AccountKit';

   let params: loginComponentManager.LoginWithHuaweiIDButtonParams = {
     // LoginWithHuaweiIDButton支持的样式
     style: loginComponentManager.Style.BUTTON_RED,
     // 设置登录类型为一键登录
     loginType: loginComponentManager.LoginType.QUICK_LOGIN
   };
   // 将params作为LoginWithHuaweiIDButton组件属性
   ```
2. 一键登录预取号阶段获取到的Authorization Code不具备用户一键登录数据的授权，因此调用服务器接口报错。请参考一键登录[客户端开发](account-phone-unionid-login.md#客户端开发)的步骤**3.展示一键登录页面并获取Authorization Code**及示例代码，获取正确的Authorization Code。
3. Authorization Code是获取用户信息的临时凭证，不同场景下的Authorization Code获取到的用户数据也不同，因此在接入华为账号一键登录时，请务必按照[华为账号一键登录（获取手机号和UnionID/OpenID）](account-phone-unionid-login.md)指南流程进行开发。
