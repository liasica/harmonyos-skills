---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:08+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3afe6a2a861ac3b1c08da345b9af35729d7c7fd010cf8e9c255773c85d898719
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/yQLs2e7CQfi403m7yJdbow/zh-cn_image_0000002712405132.png)
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
