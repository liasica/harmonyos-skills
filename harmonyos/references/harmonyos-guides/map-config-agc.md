---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30eda5e934c738ef78fb5d10e34639fa544ca093ee013004ba3211f85e284c16
---

请优先[开通地图服务](map-config-agc.md#开通地图服务)后，再参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，然后再继续进行以下开发活动。

说明

* 从HarmonyOS 5.0.2(14)版本开始，开发者无需配置公钥指纹和Client ID。
* 从DevEco Studio 6.0.0 Beta5版本开始，支持在DevEco Studio中开通地图服务。

## 开通地图服务

Map Kit提供2种方式开通地图服务：

* 通过DevEco Studio开通地图服务。
* 通过AppGallery Connect网站开通地图服务。

方式一：通过DevEco Studio开通地图服务

1. 登录DevEco Studio应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/FeTtZuZfTmGLVWMffg7Gng/zh-cn_image_0000002552958998.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=7EC835A9D1070200DDD656F083977918D8BDF1C0FA59C5050390275DC1E29470)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/QLBeDVg-QT6LoGfCVd7Wdw/zh-cn_image_0000002583478999.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=CFA67D173062A516E44E406F470611AF9C57D5FD92E6BF2F117B315E130377FE)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/M9tdbr1ATpmloEL83RWxiA/zh-cn_image_0000002552799350.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=628EB4AD4A4BE6C3852F83CF950FB47E5588BB08050672FE19F9097D93337948)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/lLwL3O0AS1GUKDv-Eq3K0A/zh-cn_image_0000002583439045.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=074DB1DE3019322FEA57B1E16873B03C5125700378FB916F838F3F49CF8D3CA6)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/1UTPBU62Tu-FLd1ARYmzKg/zh-cn_image_0000002552959000.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=6E41CE3ECF4FBD76D38F21B9BE9AB306B8DF190CBA2E22D03E2E406B062FADAA)

方式二：通过AppGallery Connect网站开通地图服务。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/PbBTX8KLTt2_9ib57sJ8nw/zh-cn_image_0000002583479001.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=EE3A73ECAC3CA22ADB787AB3595EB2439866BF7282FE058C4B7632E650E94166)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要打开“地图服务”的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/wDjMU-bJQZGvvskg6YuGQg/zh-cn_image_0000002552799352.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=08297470FAC61802B9C174045C51910453E52632DCD67186C8C6C0D97C6C5D55)
3. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/2gdi8h1VQfOK8sZ-Hu-B8Q/zh-cn_image_0000002583439047.png?HW-CC-KV=V1&HW-CC-Date=20260427T234941Z&HW-CC-Expire=86400&HW-CC-Sign=FFFD1A88B135BF0AF68918F4706CA28BCD70BD1E721A02378D736ED5A2DE1B74)
4. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing.md#section297715173233)。
   * 发布阶段必须[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、开启“地图服务”后重新[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)文件，并[配置签名信息](ide-publish-app.md#section280162182818)。

     说明

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
