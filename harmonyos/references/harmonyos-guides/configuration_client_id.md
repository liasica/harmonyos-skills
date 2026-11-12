---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id
title: 配置Client ID
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 接入准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8bb9497b8f03162409fb848e16e7197515a283dfbc4391ac901e9ed5262e6224
---

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/home/101653523124949886)平台，进入“开发者管理 > ID、证书和Profile > APP ID > 项目管理”，获取客户端ID中的“Client ID"信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/jd3dFgXpSbic-7Y3O1sxvg/zh-cn_image_0000002786519720.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=35CFB92D20AB216FD82B3F5476B719589E66364273F665C6497A4ADFEC98CD7D)
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
