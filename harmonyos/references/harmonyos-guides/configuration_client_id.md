---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id
title: 配置Client ID
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 接入准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ca1e0cfb7fe9381ae046a6a4b5c25355db9acd207a5574e9a189c5a57ace82da
---

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/home/101653523124949886)平台，进入“开发者管理 > ID、证书和Profile > APP ID > 项目管理”，获取客户端ID中的“Client ID"信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5uUCeJa_RfScei5kxle9xg/zh-cn_image_0000002820405805.png?HW-CC-KV=V1&HW-CC-Date=20261119T014823Z&HW-CC-Expire=31536000000&HW-CC-Sign=93053A99D8C21A8B2EC1FEED87023AF19AFD2F67A33EB2DDE85EF4F65B1AA648)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

   ```json5
   {
     "module": {
       "name": "xxxx",
       "type": "entry",
       "description": "xxxx",
       "mainElement": "xxxx",
       "deviceTypes": [],
       "pages": "xxxx",
       "abilities": [],
       "metadata": [
         // 配置如下信息
         {
           "name": "client_id",
           "value": "xxxxxx"
         }
       ]
     }
   }
   ```
