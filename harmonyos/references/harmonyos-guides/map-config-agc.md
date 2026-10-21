---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-10-22T07:05:51+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:737ad9a6239aab04e4ea6dbc1a95e8f3691262ffc99f502493342945272456ff
---

请优先[开通地图服务](map-config-agc.md#开通地图服务)后，再参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，然后再继续进行以下开发活动。

**说明** 

* 从HarmonyOS 5.0.2(14)版本开始，开发者无需配置公钥指纹和Client ID。
* 从DevEco Studio 6.0.0 Beta5版本开始，支持在DevEco Studio中开通地图服务。

## 开通地图服务

Map Kit提供2种方式开通地图服务：

* 通过DevEco Studio开通地图服务。
* 通过AppGallery Connect网站开通地图服务。

方式一：通过DevEco Studio开通地图服务

1. 登录DevEco Studio应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/d6xg3R8eQv2CU_nNl8wE8Q/zh-cn_image_0000002797301445.png)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/g67aCcPISvGXSmKNnkezWQ/zh-cn_image_0000002767861514.png)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/7Zo-CtI6RHWCy9MrshOomA/zh-cn_image_0000002797181477.png)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/griw1Ai8Rayl6pjuJ1XVxA/zh-cn_image_0000002768021498.png)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/wNtSszoISGaQ2P2ztgSa0Q/zh-cn_image_0000002797301447.png)

方式二：通过AppGallery Connect网站开通地图服务。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Zp4-V7EvSCqL2W07fzoleQ/zh-cn_image_0000002767861516.png)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要打开“地图服务”的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Mxis9q8sT7eVxglThPPfnA/zh-cn_image_0000002797181479.png)
3. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/6IyLYjq0TGGnXVRUfOXw5g/zh-cn_image_0000002768021500.png)
4. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing-manual.md)。
   * 发布前请确保开通地图服务，然后请参考[发布应用](ide-publish-app.md)。

     **说明** 

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
