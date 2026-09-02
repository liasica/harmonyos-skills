---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1206
title: 华为登录页面白屏，点击无响应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 华为登录页面白屏，点击无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d9681f0305b5f4ca6cd7a2a38d97e39982190e6cfae2d89e47c4d5929ab2dee1
---

## 问题现象

打开应用，应用图标加载后消失，跳转到华为一键登录页面白屏，点击滑动都无响应。

## 背景知识

* [华为账号一键登录（获取手机号和UnionID/OpenID）](../harmonyos-guides/account-phone-unionid-login.md)：华为账号一键登录是基于OAuth 2.0协议标准和OpenID Connect协议标准构建的OAuth2.0授权登录系统，应用可以通过华为账号一键登录能力快捷地获取华为账号用户的身份标识和手机号，快速建立应用内的用户体系。
* [AuthorizationWithHuaweiIDRequest](../harmonyos-references/account-api-authentication.md#authorizationwithhuaweiidrequest)请求获取到的匿名手机号可能为空，表明用户的华为账号没有绑定手机号、权限未申请或尚未生效，所以需要应用展示其他登录方式。

## 问题定位

1. 使用邮箱注册登录华为账号，不绑定手机号，打开应用，访问华为一键登录页面时出现白屏现象。而绑定手机号后再测试，功能正常。
2. 查看hilog日志，搜索关键字AuthorizationWithHuaweiID，发现应用获取华为账号用户的UnionID、OpenID、匿名手机号的请求被正常响应，返回的数据中存在UnionID和OpenID，但匿名手机号AnonymousPhone为空。

   ```txt
   06-20 14:09:46.781   57867-57867   C05320/应用包名/huaweiId_framewrok_base I WriteEndEvent:119# hiAppEvent WriteEndEvent: : {"api_name":"AuthorizationWithHuaweiID","app_id":"","begin_time":1750399786673,"end_time":1750399786781,"error_code":0,"result":0,"sdk_name":"AccountKit","trans_id":"transId_xxx"} 
   06-20 14:09:46.781   57867-57867   A03D00/应用包名/JSAPP I response.data {"authorizedScopes":["openid","quickLoginAnonymousPhone"],"extraInfo":{"localNumberConsistency":false},"openID":"xxx","unionID":"xxx"}
   06-20 14:09:46.781   57867-57867   A03D00/应用包名/JSAPP I unionID xxx
   06-20 14:09:46.781   57867-57867   A03D00/应用包名/JSAPP I openID xxx
   06-20 14:09:46.781   57867-57867   A00000/应用包名/testTag I Succeeded in authentication. AnonymousPhone is empty.
   ```
3. 排查应用华为一键登录页面的代码，当匿名手机号为空时，是否做了跳转到其他登录页面的处理。
4. 检查组件渲染逻辑是否和匿名手机号关联，从而导致了页面无内容加载，显示白屏。

## 分析结论

应用获取华为账号的匿名手机号时，未对为空的情况做处理，还将其作为判断条件，导致页面无内容加载，显示白屏。

## 修改建议

* 当获取到的匿名手机号为空，应用需要展示其他登录方式。
* 华为一键登录页面设计，可以参考Codelabs中的示例[Account Kit（华为账号一键登录）](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-AccountKit-QuickLogin)。
