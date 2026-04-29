---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/configuration_client_id
title: 配置Client ID
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 接入准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c4d4c8ea55583f5adb6b7faf3a32dc6360bb49ba3c8414387ce47993dab993f
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/K0ML26deRT-6Nm7zMZSdOQ/zh-cn_image_0000002589244793.png?HW-CC-KV=V1&HW-CC-Date=20260429T053343Z&HW-CC-Expire=86400&HW-CC-Sign=8711A7F4BB87B5AC7D589C562D89B50952F84706F339433C3E0BF6E67E515A94)
2. 在工程中entry模块的module.json5文件中，新增metadata，配置name为client\_id，value为上一步获取的Client ID的值，如下所示：

   ```
   1. {
   2. "module": {
   3. "name": "xxxx",
   4. "type": "entry",
   5. "description": "xxxx",
   6. "mainElement": "xxxx",
   7. "deviceTypes": [],
   8. "pages": "xxxx",
   9. "abilities": [],
   10. "metadata": [
   11. // 配置如下信息
   12. {
   13. "name": "client_id",
   14. "value": "xxxxxx"
   15. }
   16. ]
   17. }
   18. }
   ```
