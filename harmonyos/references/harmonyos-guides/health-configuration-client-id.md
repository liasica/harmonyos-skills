---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-configuration-client-id
title: 配置Client ID
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 配置Client ID
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a9248d9901d47c6d3d1aef58cf17ab819a4cddacb2ada6c25feac0f0611d32e
---

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的Client ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/tmjWuX2JRkqTOYM8jdbFEw/zh-cn_image_0000002558605756.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=C9BA57FB6DA2F1ED597C206BE8CC0FAE7BCDF5FFC1AFBC5EB406B1FDC5496EBC)
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
