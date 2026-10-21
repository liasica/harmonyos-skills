---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-10-22T07:05:52+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:b559aea867b9b0e011ef875f1f9e3fe1d70a8e28dd5d2d8904e553f785d5ae90
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/cZOdxGf0Rc-ks1qRB9RAbQ/zh-cn_image_0000002797301507.png)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/RODOaedSTW6ahk-Jd_vZpQ/zh-cn_image_0000002767861576.png)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/u92H0XbdS56H7OqlhEMYGQ/zh-cn_image_0000002797181539.png)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/EUbWusulT5Ox5CJZmDfGMA/zh-cn_image_0000002768021560.png)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
