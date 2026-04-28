---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-app-identity-info
title: 端侧应用配置
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 端侧应用配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d03c223bf5ce2aa03742d997b6269d53077b6838d6c25cab749d1f14ce9cb63
---

可下载并参考[示例代码-客户端](https://gitcode.com/HarmonyOS_Samples/payment-kit-sample-code-clientdemo-arkts)，以此来快速的完成商户端侧应用开发环境的构建。

通过下载示例代码或商户自行创建端侧应用后，需完成以下配置：

1. 配置bundleName
2. 配置应用属性

## 配置bundleName

在HarmonyOS应用/元服务“AppScope/app.json5”下的**bundleName**配置需要与开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[创建应用](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)时的包名保持一致。

配置内容示例如下：

```
1. {
2. "app": {
3. "bundleName": "com.huawei.******.******.demo",
4. }
5. }
```

## 配置应用属性

在HarmonyOS应用/元服务“entry/src/main/module.json5”文件中**module**的**metadata**节点下增加**client\_id**和**app\_id**属性配置。

配置内容示例如下：

```
1. {
2. "module": {
3. "metadata": [
4. {
5. "name": "app_id",
6. "value": "..."
7. },
8. {
9. "name": "client_id",
10. "value": "..."
11. },
12. ]
13. }
14. }
```

* 其中**app\_id**的value值为应用的APP ID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“APP ID”的值），详见下图的**标号1**处。
* 其中**client\_id**的value值为应用的OAuth 2.0客户端ID（在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站点击“开发与服务”，在项目列表中找到项目，在“项目设置 > 常规”页面的“应用”区域获取“OAuth 2.0客户端ID（凭据）：Client ID”的值），详见下图的**标号2**处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/V6w-XmRZRuqUrgcc2xd_HQ/zh-cn_image_0000002552799434.png?HW-CC-KV=V1&HW-CC-Date=20260427T235005Z&HW-CC-Expire=86400&HW-CC-Sign=1C51435A0EEE371676C34AD875EE0528EAF5D1CB6DA590E1469CF8489EF7F282)
