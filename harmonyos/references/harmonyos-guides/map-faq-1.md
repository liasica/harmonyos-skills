---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:06+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:1a6a9b87175df32ab979c51ea1f0dff06287e3e171eb4023bf053d8734ac3b3e
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/5lKciqsORbaO4jG9AIw--w/zh-cn_image_0000002820526475.png?HW-CC-KV=V1&HW-CC-Date=20261119T014906Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6C42FD206DDB2F5F3558ACB0F0C7A822C4E8F5DC53D0D8EC5C6718FD050B218)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/X1paG-GeQz-7CBHgPXGoxA/zh-cn_image_0000002820406475.png?HW-CC-KV=V1&HW-CC-Date=20261119T014906Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1F0AD21E8A0C9FC91586080CAEDCFCB1FEA9DBE5430D0770A36A8B33D09AD56)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/3Apr_nO6QDSKQLzrNsETeQ/zh-cn_image_0000002791726496.png?HW-CC-KV=V1&HW-CC-Date=20261119T014906Z&HW-CC-Expire=31536000000&HW-CC-Sign=A723E615C794A3090B1A9E1B396D3A02B113CE3376448F969260DBEAA8698113)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/PgpUZgfWS7aFosKnBLvF9w/zh-cn_image_0000002791566524.png?HW-CC-KV=V1&HW-CC-Date=20261119T014906Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7C9FB0EE676807AAB5A8DFC4DAB3D36F2F15431C47BA30ED62FBF6C4DF804F8)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
