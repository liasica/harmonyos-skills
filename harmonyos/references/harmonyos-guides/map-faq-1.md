---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-1
title: 地图不显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 地图不显示
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9d56ad4a20e9c17437ce1df71d1e71fa86b5968357ca3e19acc79de5aeae7ca6
---

**现象描述**

无法加载地图。

**可能原因**

1. 无网络。
2. 应用身份校验失败或地图权限未开通。
3. 未完成基本准备工作。

**处理步骤**

1. 检查是否存在日志：get network status error, code: 201, message:Permission denied。日志存在，说明应用缺少获取网络状态的权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/1o0zuKuYS02UgjAk4R-F_g/zh-cn_image_0000002558765556.png?HW-CC-KV=V1&HW-CC-Date=20260429T053918Z&HW-CC-Expire=86400&HW-CC-Sign=20C571B76C37A38B74397B6EC7524DFA5162CADC94FABE59A09921926DE68231)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/jLcOt3vCQAaylDJymoIN7Q/zh-cn_image_0000002558605900.png?HW-CC-KV=V1&HW-CC-Date=20260429T053918Z&HW-CC-Expire=86400&HW-CC-Sign=A7DCBD0A7E05448E1600B151AC535BB1BCC33C979511ED329E254843E0002D86)
2. 请检查应用日志中是否存在日志：The app does not have map permission。日志存在，说明应用身份校验失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/R8kH-oaKTSeztnOpAGCTDQ/zh-cn_image_0000002589325427.png?HW-CC-KV=V1&HW-CC-Date=20260429T053918Z&HW-CC-Expire=86400&HW-CC-Sign=8CF7B3DE57798060F4062F4AAE2D192C702D246870E160AAE26852BDE48A158B)

   查看com.huawei.hms.mapservice进程日志，检查是否存在该日志：App authentication failed. code: 1002600003。参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/3HcmPdm7QLCRR4UmwGPxWw/zh-cn_image_0000002589245365.png?HW-CC-KV=V1&HW-CC-Date=20260429T053918Z&HW-CC-Expire=86400&HW-CC-Sign=B8A94205626484D12F60BDA957073DC6DC37A58E69303716155670FCC5A565B2)
3. 请参考“[应用开发准备](application-dev-overview.md)”检查是否完成基本准备工作。
