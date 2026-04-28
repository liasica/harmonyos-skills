---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c990a99a65c00cfee6ffea9caa1a159202d1e731b3b2c3d3542ac455b33be633
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/EUIJAFLNTiSGPAYPjYsWzQ/zh-cn_image_0000002552959054.png?HW-CC-KV=V1&HW-CC-Date=20260427T234955Z&HW-CC-Expire=86400&HW-CC-Sign=FB8EC2FBBDD34B1F1832522408B85F818DAB00E32A3A881534C6D0D3B36D6D1C)

   请在应用的module.json5文件中配置获取网络状态的权限。

   ```
   1. {
   2. "module" : {
   3. // ...
   4. "requestPermissions": [
   5. {
   6. "name": "ohos.permission.INTERNET",
   7. "usedScene": {
   8. "when": "always"
   9. }
   10. },
   11. {
   12. "name": "ohos.permission.GET_NETWORK_INFO",
   13. "usedScene": {
   14. "when": "always"
   15. }
   16. }
   17. ]
   18. }
   19. }
   ```

   请检查应用日志中是否存在日志：The network is unavailable。日志存在，说明设备网络存在问题，请检查网络状态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/r39pggNaS8GX3hvfidF6eg/zh-cn_image_0000002583479055.png?HW-CC-KV=V1&HW-CC-Date=20260427T234955Z&HW-CC-Expire=86400&HW-CC-Sign=45516D44EB2764D3D84066A5A2B7926CC5AEE3BC5009CFB3FC342DE3215989BB)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/jz3YwPr2SmS8yrefIwnREw/zh-cn_image_0000002552799406.png?HW-CC-KV=V1&HW-CC-Date=20260427T234955Z&HW-CC-Expire=86400&HW-CC-Sign=06CF61CB4A00F8749065BE470F2F9151D3B9917E609138C213EB7546DD38FBE9)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/FFjQtNHcTDS4eGcMRusRxQ/zh-cn_image_0000002583439101.png?HW-CC-KV=V1&HW-CC-Date=20260427T234955Z&HW-CC-Expire=86400&HW-CC-Sign=4D1A46EF7E65700AA73DD498697B3BFC9E6A31B3810B7EBFE556F11EFC26F764)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
