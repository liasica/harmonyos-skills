---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:34+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:cbdb05a7b32b52afa6e3e91ed1116decc29f643c9ae331d26b68ff607ab1cb0d
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/3Ot2CfxVQG-XQyBDVlLyAQ/zh-cn_image_0000002791859961.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/dFCK1OBjSvGkz99BKmEzxg/zh-cn_image_0000002762501086.png)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/PwVmrM-rT2ePbbmoizkqWQ/zh-cn_image_0000002791739745.png)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/M848qNGQSR-iZMEPlDI1NA/zh-cn_image_0000002762341166.png)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
