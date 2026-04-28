---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-3
title: 一键登录场景下无法获取到匿名手机号如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 一键登录场景下无法获取到匿名手机号如何解决
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:917525d8d421be5640b149a65e96955966a97412e4d31080160b4673ca075822
---

在华为账号一键登录场景下无法获取到匿名手机号时，建议通过以下步骤排查解决：

1. 开发者开启了[代码混淆](source-obfuscation-guide.md)，quickLoginAnonymousPhone（匿名手机号）属性需要配置混淆白名单防止release包被混淆。在调用获取匿名手机号方法工程模块的混淆文件obfuscation-rules.txt中添加：

   ```
   1. # 开发者开启属性混淆需要配置quickLoginAnonymousPhone属性白名单防止其被混淆
   2. -enable-property-obfuscation
   3. -keep-property-name
   4. quickLoginAnonymousPhone
   ```
2. Wearable、TV（非5.1.1版本）设备无法获取到手机号，会报[1001500003 不支持该scopes或permissions](../harmonyos-references/account-api-error-code.md#section1001500003-不支持该scopes或permissions)。
3. 华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。
4. 使用华为账号一键登录服务的账号必须是中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）华为账号。
5. 确认是否在AGC的[开发与服务](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/myProject)中申请华为账号一键登录权限。图示为未申请状态，未申请将报错[1001502014 应用未申请scopes或permissions权限](account-faq-2.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-XPMyZ4XSz-a2aYVZ00L8Q/zh-cn_image_0000002552958742.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=E2FC48C1819164A72E3E8666B11A558FDB256B923AD001E86F5AB0805CD34C4E)
6. 申请的华为账号一键登录权限待审批或待生效，**权限申请后需要24小时后生效或将调试设备的系统时间向后调整24小时后重试。**
7. 权限申请成功后，确认scope参数是否传入的是quickLoginAnonymousPhone，详情可参考一键登录[客户端开发](account-phone-unionid-login.md#客户端开发)。

   ```
   1. // 创建授权请求，并设置参数
   2. const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
   3. // 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限，否则会返回1001502014错误码
   4. authRequest.scopes = ['quickLoginAnonymousPhone'];
   ```
