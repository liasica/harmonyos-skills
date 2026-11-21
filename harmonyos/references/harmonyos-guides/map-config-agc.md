---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d098e1455fddcff6164f380c850bcb12bc8c71ac2bb41a8bd1e955c4aebc4e52
---

请优先[开通地图服务](map-config-agc.md#开通地图服务)后，再参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，然后再继续进行以下开发活动。

**说明** 

* 从HarmonyOS 5.0.2(14)版本开始，开发者无需配置公钥指纹和Client ID。
* 从DevEco Studio 6.0.0 Beta5版本开始，支持在DevEco Studio中开通地图服务。

## 开通地图服务

Map Kit提供2种方式开通地图服务：

* 通过DevEco Studio开通地图服务。
* 通过HarmonyOS 开发者中心网站开通地图服务。

方式一：通过DevEco Studio开通地图服务

1. 登录DevEco Studio应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/lJaiod5bQZW3BnUGz773TQ/zh-cn_image_0000002821838021.png?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DFB11D2C08A74E5834419325CDCD1975B0C8A27DF05019D702B07D010D630F3)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/qd6Ua-3iSHOawzCpyuVh2A/zh-cn_image_0000002821758023.png?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E07403ACF19A12CC99C21BDA5A69A04A78F781070F2DBCB163A80D1A118A0E1)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/y_bwiIp0TXqW6OfJqJ4czQ/zh-cn_image_0000002793038086.png?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DC8E0C3061F2DD2F9B08506D38ACFB41DF72F2690B44FFE6FB547523088D483)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/UIt8KHLrTDCmfADuopqkKA/zh-cn_image_0000002792878116.png?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B853C755837A73960D7E4D8F5A91BD206B2D7FEC66F313D0170D7AB5641C2CE)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/wbVqzsJWTLaGeA4vPqsmfA/zh-cn_image_0000002821838023.png?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=B02E50F0D61DEEEE3286F4982C82EFE6B3BAE1B6C4C7B6BD7DC3761E9D747C7A)

方式二：通过HarmonyOS 开发者中心网站开通地图服务。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)网站，选择“应用管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/9o8r1jOGSWSHcbIaaVUGvQ/zh-cn_image_0000002821758025.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=5669834DDDF709D75C8B3889FD7A036F1EC02730F884355823B00BE255CEEFC1)
2. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/Me81_OI5QdqnTFyvqk8ElA/zh-cn_image_0000002793038088.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011103Z&HW-CC-Expire=31536000000&HW-CC-Sign=51A0F898B196EA423892D839398E649C43E03E3054BD34618ED12869980165A6)
3. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing-manual.md)。
   * 发布前请确保开通地图服务，然后请参考[发布应用](ide-publish-app.md)。

     **说明** 

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
