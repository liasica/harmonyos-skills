---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2e482f338b7ad917afb08881b40269833dfeae2c5dd884d085a67a6fbf498433
---

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/home/101653523124949886)平台，进入“开发者管理 > ID、证书和Profile > APP ID > 项目管理”，获取客户端ID中的“Client ID"信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/NkERQdGGRIakVkLjvYh3gQ/zh-cn_image_0000002820406323.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CC3CF0D870464494D9EFD5550577834C67E9CA81FB11FB816D1A79BE6C14426)
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
