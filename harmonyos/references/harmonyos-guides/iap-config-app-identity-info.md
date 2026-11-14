---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-app-identity-info
title: 配置应用身份信息
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 配置应用身份信息
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:18d8e4a4c5f77b955ac36d47dee343f623d4204ba07cee6c754d9da5b3cb31e9
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

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)，点击“应用管理”，选择目标应用，在“基础信息”页“OAuth 2.0客户端ID（凭据）”栏获取目标应用的**Client ID**。

   **说明** 

   * 下图中的APP ID可用于服务器API接口请求。
   * 如果开发者应用的compatibleSdkVersion>=14，则接入IAP Kit不要求开发者[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹)以及配置应用身份信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/s-lC5AI6T7mVxxwoG13C8g/zh-cn_image_0000002817507485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004821Z&HW-CC-Expire=31536000000&HW-CC-Sign=FEBA768141688837893504710217701986A0AB968C1C6ECA5F25516512DAA0B9)
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
