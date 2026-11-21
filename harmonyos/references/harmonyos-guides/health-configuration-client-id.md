---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:db758acfbdfa04f6e542490d8797e8d97684ad10d19fbda7277879e99e90d6c8
---

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/home/101653523124949886)平台，进入“开发者管理 > ID、证书和Profile > APP ID > 项目管理”，获取客户端ID中的“Client ID"信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/vYcI0l-1QTK460dG5-c9Fw/zh-cn_image_0000002792878024.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCB7809A0155F067AC0FEA9C245D6D50477A22C5ABFC87B3E625A35E9EA812E6)
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
