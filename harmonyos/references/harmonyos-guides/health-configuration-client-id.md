---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b6476973a1ebd29612a83251a96000ca37a32ed224036c66a4eb887e9d03b7d
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/XpkYsXHpR1K5gELXewhIiw/zh-cn_image_0000002583478913.png?HW-CC-KV=V1&HW-CC-Date=20260427T234909Z&HW-CC-Expire=86400&HW-CC-Sign=F662CE68DED58FFB284BC93BF50D2C8B1FB15BE88D188DB05B1D4D35132DAF46)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

   ```
   1. "module": {
   2. "name": "xxxx",
   3. "type": "entry",
   4. "description": "xxxx",
   5. "mainElement": "xxxx",
   6. "deviceTypes": [],
   7. "pages": "xxxx",
   8. "abilities": [],
   9. "metadata": [ // 配置如下信息
   10. {
   11. "name": "client_id",
   12. "value": "xxxxxx"
   13. }
   14. ]
   15. }
   ```
