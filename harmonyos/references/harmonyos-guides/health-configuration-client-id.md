---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:73c949a114b40b7152366d9df85a27f81b1306441d42b7d5f50fa84a7b697b91
---

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/home/101653523124949886)平台，进入“开发者管理 > ID、证书和Profile > APP ID > 项目管理”，获取客户端ID中的“Client ID"信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/qcYdnepZTKCe1IozLv9tLQ/zh-cn_image_0000002788308042.png?HW-CC-KV=V1&HW-CC-Date=20261114T004635Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CEC5257BFFA856C82058274A99C34AB45AE2ADDA192E48FA86E7DA3652F759D)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

   ```json
   "module": {
     "name": "xxxx",
     "type": "entry",
     "description": "xxxx",
     "mainElement": "xxxx",
     "deviceTypes": [],
     "pages": "xxxx",
     "abilities": [],
     "metadata": [
       {
         "name": "client_id",
         "value": "xxxxxx"
       }
     ]
   }
   ```
