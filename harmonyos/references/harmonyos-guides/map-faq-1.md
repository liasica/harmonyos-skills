---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:121dbfd2df249f930f2b8c2eb0ed6a256b39cf45b9728de822710fdd677e903a
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/C2eyIcA4SYK4Cj_90BMaKg/zh-cn_image_0000002815399965.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=18FD87336F5D77A4E1F738EDD4EFD856A8877F852B02B03B47A7B0186A8162E9)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/xtxmVeqAQsm4SEfbhI_4LQ/zh-cn_image_0000002786520390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFC17D8375B28D3838DEF17DC903F0B6A77A63AB83525CE6175FFE7D30B47C48)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/fprUeGyZSDSagDGEFIyaWg/zh-cn_image_0000002786360462.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9DE70BFECD307D95F566E8EBEA2229E869C64C1BC63188D013F6B1811CF74F0)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Wyd0KupaScyIDEAGvuUVlg/zh-cn_image_0000002815559883.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1EB432FF03B86E6E35829E6C39DDF6924AD71AC82C88ECDEE212C07D4543669)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
