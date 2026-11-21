---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:32+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:fe2fe6740f6b2c8762959146e59064720a416fab20d60f62f99321f10b96a667
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/1pbx7oW9Tn6lENmCQuj7wA/zh-cn_image_0000002793038146.png?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD43F2B1151AF54E4A8C5FDDEE0EF107CEDDD8CFE260E77D262DCA0650E69869)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/hxUc8ZiVSKaozBAeANfZOg/zh-cn_image_0000002792878176.png?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE2413E2ADD28CBEC9BD8BA7D04AEA1D26B1FBD0DAE17148798C8DDD65A92076)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Y8amN_HQQZGhlNfeEfOrpw/zh-cn_image_0000002821838083.png?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD15929D9819699FA49F87D705D5EEF7A354DB0EEF0201788269788B0E061A16)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/IOAuzMurRReH0LcL8O3riw/zh-cn_image_0000002821758085.png?HW-CC-KV=V1&HW-CC-Date=20261121T011104Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C8D1C9E8F46CE82F3C20AB1EA86801CBF5B2C155037943E4D4CD38313A782E1)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
