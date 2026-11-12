---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ca1ebc11af0f1a64431fa855dd8f92fed6224e05b0709c0f89d014cb09e3ac12
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/elKZVIO8QHemetOiymPDgQ/zh-cn_image_0000002786360400.png)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/vZiDAGEGSL-RXshuqQLFog/zh-cn_image_0000002815559821.png)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/95Gw2iqvQ7u8UQWpVfglgQ/zh-cn_image_0000002815399905.png)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/fE1W14x6Tdayi9-Y9neCew/zh-cn_image_0000002786520330.png)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3x2MVosiRZmXIoMmeHjh1g/zh-cn_image_0000002786360402.png)

方式二：通过HarmonyOS 开发者中心网站开通地图服务。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)网站，选择“应用管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/4-d7VN3iS2ORL_MrV04QqA/zh-cn_image_0000002815559823.jpg)
2. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/-Xa_npnvTwOmHCj41KJvlg/zh-cn_image_0000002815399907.jpg)
3. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing-manual.md)。
   * 发布前请确保开通地图服务，然后请参考[发布应用](ide-publish-app.md)。

     **说明** 

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
