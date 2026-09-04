---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-app-identity-info
title: 配置应用身份信息
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 配置应用身份信息
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:10+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:20527d651892f17e0a48432f4f5075dd0e8069957b4b87de09fc0e2b0850d5f3
---

## bundleName配置

在工程“AppScope/app.json5”下的**bundleName**需要与开发者在应用开发准备中[创建应用](application-dev-overview.md#创建应用)时的包名保持一致。

配置内容示例如下：

```json
{
  "app": {
    "bundleName": "com.huawei.***.***.demo",
  }
}
```

## 配置应用身份信息

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标项目，通过“项目设置 > 常规 > 应用”获取目标应用的**Client ID**。

   **说明** 

   * 下图中的APP ID可用于服务器API接口请求。
   * 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹) 以及配置应用身份信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/WxHHoSrjSqC_X5wMFwjRVg/zh-cn_image_0000002742124091.png)
2. 在工程“entry/src/main/module.json5”的**module**节点增加如下**client\_id**属性配置，用于IAP Kit接口的应用身份鉴权。

   ```json
   {
     "module":{
       "type": "***",
       "name": "***",
       "description": "***",
       "mainElement": "***",
       "deviceTypes": [***],
       "metadata": [
         {
           "name": "client_id",
           "value": "***"
         }
       ]
     }
   }
   ```
