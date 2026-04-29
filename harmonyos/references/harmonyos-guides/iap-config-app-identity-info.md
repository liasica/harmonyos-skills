---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-app-identity-info
title: 配置应用身份信息
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 配置应用身份信息
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:37+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:19c3315987b2f0dd23d1516c63d11209135d0a1f56f7f4bc47bda1c1f9ead7d4
---

## bundleName配置

在工程“AppScope/app.json5”下的**bundleName**需要与开发者在应用开发准备中[创建应用](application-dev-overview.md#创建应用)时的包名保持一致。

配置内容示例如下：

```
1. {
2. "app": {
3. "bundleName": "com.huawei.***.***.demo",
4. }
5. }
```

## 配置应用身份信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标项目，通过“项目设置 > 常规 > 应用”获取目标应用的**Client ID**。

   说明

   * 下图中的APP ID可用于服务器API接口请求。
   * 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹) 以及配置应用身份信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/a4PlVcoQTvmgLfBZfrjRxQ/zh-cn_image_0000002589245229.png?HW-CC-KV=V1&HW-CC-Date=20260429T053835Z&HW-CC-Expire=86400&HW-CC-Sign=724BD343F32B23BCAA0EC00BF95FD84A1D30E553A66DA1AA86B84A7E77279F52)
2. 在工程“entry/src/main/module.json5”的**module**节点增加如下**client\_id**属性配置，用于IAP Kit接口的应用身份鉴权。

   ```
   1. {
   2. "module":{
   3. "type": "***",
   4. "name": "***",
   5. "description": "***",
   6. "mainElement": "***",
   7. "deviceTypes": [***],
   8. "metadata": [
   9. {
   10. "name": "client_id",
   11. "value": "***"
   12. }
   13. ]
   14. }
   15. }
   ```
