---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:6c98f01c8bcdf3d2389187f55faccab479f0db936b8134e38842e3b3740d4d2f
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Qs3mWK7PRiqJjMkd8LCdpA/zh-cn_image_0000002817507625.png?HW-CC-KV=V1&HW-CC-Date=20261114T004641Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFBEC63C6B1788C6C9B8BB0772EABFA5001B43DACCFE8D739D9292B8893EC954)

   请在应用的module.json5文件中配置获取网络状态的权限。

   ```typescript
   {
     "module" : {
       // ...
       "requestPermissions": [
         {
           "name": "ohos.permission.INTERNET",
           "usedScene": {
             "when": "always"
           }
         },
         {
           "name": "ohos.permission.GET_NETWORK_INFO",
           "usedScene": {
             "when": "always"
           }
         }
       ]
     }
   }
   ```

   请检查应用日志中是否存在日志：The network is unavailable。日志存在，说明设备网络存在问题，请检查网络状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/8aS08htWSs2Vg1t3BvD6Ww/zh-cn_image_0000002788308194.png?HW-CC-KV=V1&HW-CC-Date=20261114T004641Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4367A950D843D67675896D5210F23A27C28B3275865D0184238B802AC208691)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Qmvn_r8ATgKH2TasxHujCQ/zh-cn_image_0000002817427557.png?HW-CC-KV=V1&HW-CC-Date=20261114T004641Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FB84922E4C2E0D1E00D8FA802C8C426C5D1F3E90B8F45F17B5AB88D00369F17)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/kTyVGTGtTIusLGkhuhFJOg/zh-cn_image_0000002788468138.png?HW-CC-KV=V1&HW-CC-Date=20261114T004641Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA2202F8D2C3DCBFB24A9ED5FFE43420F63EDFC85C4B4373B9E14210D16F2A8F)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
