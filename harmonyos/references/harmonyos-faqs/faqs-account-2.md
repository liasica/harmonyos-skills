---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-account-2
title: 使用华为账号一键登录成功后，用户名显示为长段随机字符
breadcrumb: FAQ > 应用服务开发 > 华为账号服务（Account Kit） > 使用华为账号一键登录成功后，用户名显示为长段随机字符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cc85960ddb5bb6b887d0866709170a52a1820a3e267fc32a52f6b2eb19f179de
---

## 问题现象

使用华为账号一键登录成功后，用户名（昵称）显示为长段随机字符，视觉观感较差。

## 背景知识

* [华为账号一键登录](../harmonyos-guides/account-phone-unionid-login.md)是基于OAuth 2.0协议标准和OpenID Connect协议标准构建的OAuth2.0授权登录系统，应用可以通过华为账号一键登录能力方便地获取华为账号用户的身份标识和手机号，快速构建应用内的用户体系。
* 当应用需要[获取华为账号用户信息](../harmonyos-guides/account-get-user-info.md)或者完善用户个人资料（头像昵称、收货地址、发票抬头）时，或需要获取用户风险等级判断用户风险时，可通过Account Kit提供的相关能力，引导用户填写并管理相关信息，完成授权流程。
* 如应用需要[完善用户头像昵称信息](../harmonyos-guides/account-get-avatar-nickname.md)，可使用Account Kit提供的头像昵称授权能力，用户允许应用获取头像昵称后，可快速完成个人信息填写。

## 问题定位

1. 确认应用是否进行获取用户头像和昵称的申请操作。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/AISNV-nqSuSTgjBxLFpsXg/zh-cn_image_0000002658793675.png "点击放大")
2. 排查是否进行获取用户头像和昵称的相关代码开发。
   * 排查是否导入authentication模块及相关公共模块。

     ```ts
     import { authentication } from '@kit.AccountKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { util } from '@kit.ArkTS';
     import { BusinessError } from '@kit.BasicServicesKit';
     ```
   * 排查是否创建授权请求并设置参数。

     ```ts
     const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
     ```
3. 排查是否直接使用OpenID或随机字符作为用户名。

   ```ts
   const userName = data.uid; // 这里返回的是UID或随机字符，而非华为手机号或昵称
   console.info(`当前用户名: ${userName}`); // 输出:随机字符或数字
   ```

## 分析结论

在开发华为账号一键登录功能时，未进行获取用户头像和昵称的相关代码开发，无法使用华为头像和昵称作为应用的用户头像和昵称，直接使用随机字符或数字作为用户名。

## 修改建议

参考获取用户头像和昵称[开发步骤](../harmonyos-guides/account-get-avatar-nickname.md#开发步骤)，避免直接使用OpenID或随机字符等作为用户名。
