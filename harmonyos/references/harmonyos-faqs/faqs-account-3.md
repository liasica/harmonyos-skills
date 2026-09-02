---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-3
title: 华为账号一键登录获取不到手机号怎么解决
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 华为账号一键登录获取不到手机号怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:76b3a567a46c590948affb02acaf1f144c4f3dbf98eb7d710b37ee574c8733ee
---

## 问题现象

* 调用AuthorizationWithHuaweiIDRequest获取到的响应数据没有quickLoginAnonymousPhone字段。
* 调用[获取用户信息](../harmonyos-references/account-api-get-user-info.md)接口返回的数据没有loginMobileNumber字段。

## 背景知识

* [Account Kit（华为账号服务）](../harmonyos-guides/account-kit-guide.md)：提供简单、快速、安全的登录功能，让用户快捷地使用华为账号登录应用。用户授权后，Account Kit可提供头像、昵称、手机号码等信息，帮助应用更了解用户。
  1. [华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)：华为账号一键登录是基于OAuth2.0协议标准和OpenID Connect协议标准构建的OAuth2.0授权登录系统，应用可以通过华为账号一键登录能力方便地获取华为账号用户的身份标识和手机号，快速建立应用内的用户体系。

     | 接口名 | 描述 |
     | --- | --- |
     | [createAuthorizationWithHuaweiIDRequest()](../harmonyos-references/account-api-authentication.md#createauthorizationwithhuaweiidrequest) | 获取授权接口，通过AuthorizationWithHuaweiIDRequest传入一键登录的scope：quickLoginAnonymousPhone，即可在授权结果中获取到用户UnionID、OpenID、匿名化手机号。 |
     | [LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md#loginwithhuaweiidbutton) | 华为账号Button登录组件。 |
     | [onClickLoginWithHuaweiIDButton](../harmonyos-references/account-api-component-manager.md#onclickloginwithhuaweiidbutton) | 注册华为账号一键登录按钮的结果回调。 |
  2. [获取华为账号用户信息](../harmonyos-guides/account-get-user-info.md)：
     + [获取手机号](../harmonyos-guides/account-get-phonenumber.md)：当应用需要获取用户手机号时，可调用Account Kit的手机号授权能力，引导用户完成手机号授权。
     + [快速验证](../harmonyos-guides/account-get-phonenumber.md)：对用户选择的华为账号绑定的手机号或者新增的手机号进行验证，不保证是实时验证，仅首次需要用户授权。
  3. [ArkTS错误码](../harmonyos-references/errorcode-account-kit.md)：介绍本模块特有错误码。
* [快速验证手机号Button](../harmonyos-guides/scenario-fusion-button-getphonenumber.md)：快速验证手机号Button功能用于帮助开发者向用户发起手机号申请，经用户同意后，应用可获取手机号，为用户提供相应服务（完整流程可参考[手机号快速验证](../harmonyos-guides/account-get-phonenumber.md)）。

## 问题定位

* 检查quickLoginMobilePhone（华为账号一键登录）的scope权限申请是否生效；
* 检查华为账号是否绑定手机号；
* 检查华为账号是否是中国境内的账号；
* 检查服务端获取华为账号绑定号码时，该服务器是否部署在中国境内；
* 检查HiLog日志，查看错误码是否为1001500003或1001502014，表示scopes或permissions设置有问题；
* 检查是否开启了[源码混淆](../harmonyos-guides/source-obfuscation-guide.md)。

## 分析结论

在华为账号一键登录场景下，获取匿名手机号为空或无法获取到明文手机号时，可能有以下原因：

* quickLoginMobilePhone[申请账号权限](../harmonyos-guides/account-config-permissions.md)没有生效；
* 华为账号未绑定手机号；
* 使用华为账号一键登录服务的账号不是中国境内账号；
* 应用服务端获取华为账号绑定号码时，该服务器没有部署在中国境内；
* scope或permissions参数设置有问题；
* 开发者开启了[ArkGuard混淆](../harmonyos-guides/source-obfuscation-guide.md)。

## 修改建议

在华为账号一键登录场景下，获取匿名手机号为空或无法获取到明文手机号时，建议通过以下步骤排查解决：

* [申请账号权限](../harmonyos-guides/account-config-permissions.md)待生效，权限申请后需要24小时后生效或将调试设备系统时间向后调整24小时后重试。
* 华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。
* 使用华为账号一键登录服务的账号必须是中国境内（不包含中国香港、中国澳门、中国台湾）华为账号。
* 应用服务端获取华为账号绑定号码时，该服务器必须部署在中国境内（不包含中国香港、中国澳门、中国台湾），参考华为账号一键登录[约束与限制](../harmonyos-guides/account-phone-unionid-login.md#约束与限制)。
* 确认权限申请成功后，确认scope参数是否符合预期，详情可参考一键登录[客户端开发](../harmonyos-guides/account-phone-unionid-login.md#客户端开发)。
* 开发者开启了[ArkGuard混淆](../harmonyos-guides/source-obfuscation-guide.md)，quickLoginAnonymousPhone（匿名手机号）属性需要配置混淆白名单防止被混淆，参考[配置混淆选项](../harmonyos-guides/source-obfuscation-guide.md#配置混淆选项)中使用-keep-property-name保留属性名称。

## 常见FAQ

Q：华为一键登录，服务端如何拿到完整手机号？

A：[服务端开发](../harmonyos-guides/account-phone-unionid-login.md#服务端开发)可以使用Access Token调用[获取用户信息](../harmonyos-references/account-api-get-user-info.md)接口获取用户信息，从用户信息中获取用户绑定的完整手机号。

Q：华为账号登录使用自定义按钮登录，不用LoginWithHuaweiIDButton获取的Authorization Code，服务器是否可以获取明文手机号？

A：不可以，必须用LoginWithHuaweiIDButton且申请了华为账号一键登录权限后获取到的Authorization Code才能取到明文手机号。

Q：部分华为账号进行华为账号一键登录时，登录页面显示空白。

A：如果用户的华为账号为邮箱账号，并且没有绑定手机账号，此时quickLoginAnonymousPhone调用AuthorizationWithHuaweiIDRequest授权请求获取匿名手机号，手机号为空。此时需要进行空值判断并引导用户使用其他登录方式，否则使用空手机号进行后续登录处理，会导致页面空白，登录失败。

Q：华为一键登录，本地运行到手机可以拿到匿名手机号，为什么发布测试拿不到匿名手机号？

A：如果是调试包，修改app.json5中的versionCode即可；如果是发布包，需修改系统时间到25小时以后。

Q：华为一键登录在开启代理后报错errCode:1001500001。

A：原因是开启代理后的域名未添加进域名校验白名单，可以在正常登录后，把公钥指纹缓存到本地再开启代理。

Q：开发者服务端请求华为账号服务端的[一键登录获取华为账号绑定号码和UnionID/OpenID](../harmonyos-references/account-api-get-user-info-quicklogin-by-code.md)报错，提示javax.net.ssl.sSLHandshakeException: Remote host closed connection during handshake，如何解决？

A：华为账号使用的证书是全球可信证书，出现此问题一般是开发者启用了代理导致的，如Nginx正向代理访问互联网系统，又在NG上面配置了转发访问规则，对华为账号https地址进行校验，这种情形就会出现该问题，建议开发者在Nginx代理时对华为账号证书处理下。

Q：一键登录获取华为账号绑定号码失败，报错“session timeout”，但偶尔会获取成功。

A：获取华为账号绑定号码请求时，Request Body需要传入access\_token，但access\_token存在特殊字符，导致请求失败，需要对Request Body传入的access\_token数据进行URLEncoder.encode。

Q：一键登录中在API17的设备上能正常实现华为一键登录功能，API18，19的云测试设备一直提示报错显示scope权限问题，从API18开始增加了什么权限的校验吗？

A：从API18开始，在[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件参数[LoginWithHuaweiIDButtonParams](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)中新增riskLevel字段。该字段需设置为true，具体可参考文档：[客户端开发](../harmonyos-guides/account-get-risklevel-byquicklogin.md#客户端开发)。

Q：调用[LoginWithHuaweiIDButton](../harmonyos-references/account-api-huawei-id-button.md)组件，在[LoginWithHuaweiIDButtonParams](../harmonyos-references/account-api-component-manager.md#loginwithhuaweiidbuttonparams)参数中设置风险等级字段标识riskLevel为true，即使用获取风险等级，需要什么前提条件吗？

A：应用在使用获取风险等级能力之前，需要完成对应的scope权限申请，scope权限申请审批未完成或未通过，将报错[1001502014 应用未申请scopes或permissions权限](../harmonyos-guides/account-faq-2.md)。若不使用的话可设置为false。

Q：华为账号登录，[使用自定义按钮登录](../harmonyos-guides/account-unionid-login-api.md)时会有用户授权弹窗吗？

A：自定义按钮登录不会有用户授权弹窗。

Q：华为账号一键登录授权，为什么使用调试证书在5.1的设备上无法获得授权，在6.0以上系统就正常授权？

A：6.0以上系统做了优化，针对于调试证书，可以不配置指纹证书。6.0以下版本还是需要配置指纹证书。
