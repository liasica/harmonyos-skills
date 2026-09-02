---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-config-app
title: 配置应用
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 启用数字商品服务 > 配置应用
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c549e50cae5184b5d327d800c6078d73722d6718615a1128f0175f184af761a0
---

接入数字商品服务前，需要先完成应用的bundleName配置和应用身份信息配置。

## bundleName配置

工程“AppScope/app.json5”下的**bundleName**需要与开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[创建应用](application-dev-overview.md#创建应用)时的包名保持一致。

配置内容示例如下：

```json5
{
  "app": {
    // bundleName需要与开发者在AppGallery Connect中创建应用时的包名保持一致
    "bundleName": "com.example.appgallery.kit.demo",
    // ...
  }
}
```

## 配置应用身份信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标项目，通过“项目设置 > 常规 > 应用”获取目标应用的**Client ID**。

   **说明** 

   * 下图中的APPID可用于服务器API接口请求。
   * 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹)以及配置应用身份信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/QrTeE7z4Rp6qhT0T_J-69A/zh-cn_image_0000002706834782.png)
2. 在工程“entry/src/main/module.json5”的**module**节点增加如下**client\_id**属性配置，用于数字商品服务接口的应用身份鉴权。

   ```json5
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone",
         "tablet",
         "2in1",
         "tv",
         "car"
       ],
       // ...
       "metadata": [
         // ...
         {
           "name": "client_id",
           "value": "***"
         }
       ]
     }
   }
   ```
