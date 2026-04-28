---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-config-app
title: 配置应用
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 启用数字商品服务 > 配置应用
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d23dd60b35bf7c81cb4ea1dc6e9ea3f669f6141e4fd4f3992a0dd8456b56959
---

接入数字商品服务前，需要先完成应用的bundleName配置和应用身份信息配置。

## bundleName配置

工程“AppScope/app.json5”下的**bundleName**需要与开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[创建应用](application-dev-overview.md#section13566816173114)时的包名保持一致。

配置内容示例如下：

```
1. {
2. "app": {
3. // bundleName需要与开发者在AppGallery Connect中创建应用时的包名保持一致
4. "bundleName": "com.huawei.***.***.demo",
5. // ...
6. }
7. }
```

## 配置应用身份信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标项目，通过“项目设置 > 常规 > 应用”获取目标应用的**Client ID**。

   说明

   * 下图中的APPID可用于服务器API接口请求。
   * 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](application-dev-overview.md#section1726913517284)以及配置应用身份信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/A-4Ru9rFRjGeNQovQOh4rg/zh-cn_image_0000002583438815.png?HW-CC-KV=V1&HW-CC-Date=20260427T234813Z&HW-CC-Expire=86400&HW-CC-Sign=0DF950E9985817CDC9137D5EC6A4F42A255B92D72D6B34B19DE4805B0713AC8A)
2. 在工程“entry/src/main/module.json5”的**module**节点增加如下**client\_id**属性配置，用于数字商品服务接口的应用身份鉴权。

   ```
   1. "module":{
   2. "type": "***",
   3. "name": "***",
   4. "description": "***",
   5. "mainElement": "***",
   6. "deviceTypes": [***],
   7. // ...
   8. "metadata": [
   9. {
   10. "name": "client_id",
   11. "value": "***"
   12. },
   13. // ...
   14. ]
   15. }
   ```
