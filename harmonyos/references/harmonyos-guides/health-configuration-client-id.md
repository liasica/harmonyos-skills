---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-10-11T07:22:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:10f9f416d7b9a2d6b4604f75b742ae3d7f55ef57a33631ccc7b218a79513fb3a
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/0xIJCKGtTsGfWOh-AZ0iKg/zh-cn_image_0000002755024736.png)
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
