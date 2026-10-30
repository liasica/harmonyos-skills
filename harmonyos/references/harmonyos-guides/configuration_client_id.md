---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id
title: 配置Client ID
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 接入准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f7e25c35f0c05be0573fcf39f7b08bf7c079d2b73a620968e677d092cd04e827
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/PJ6FvGTWRdGH6BPEf2gyIg/zh-cn_image_0000002806108991.png)
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
