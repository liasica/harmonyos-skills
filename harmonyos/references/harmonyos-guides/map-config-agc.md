---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6562cb3e9adb8852eada9a8b068d7042c16a5acd3c22ccc31b9305a9ba9a43f
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/fMt3zUK8QcqUNaRP9EI54A/zh-cn_image_0000002558765500.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=3B837372CA48761FF0D7DED1DAC34D922EAA8FC8C7BF721D8A7D3C412BF4CFF9)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ZfOLNrxER1SIygnKKp-htA/zh-cn_image_0000002558605844.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=3AC30F5149E87D7DFA5521B2CC1E4A6D0B3B482CE13E736B6CBF339C422CBB5F)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/0VRP3hCMTBy2nrzJA0FCmA/zh-cn_image_0000002589325371.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=4F7F7CE3CBEF2C38CF0AAE1E0710ECA8A3360388F20F847401AA9FD167836CF8)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/D8lzBLOFTEWlju_x6a1ghQ/zh-cn_image_0000002589245307.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=06B6BAFFE343B1788EDAF92E7A532BC9C8832B5B0422DD6537AE8F2CCDD1E35C)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/pYc4RzYKRYOoE-Y35xJ-nQ/zh-cn_image_0000002558765502.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=3460C8D1A774715EBD3C61D703DFAC95FD22E05E3AB2B982974656EBAE22A51F)

方式二：通过AppGallery Connect网站开通地图服务。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/7rHYvaUbTFOTr4xmiP50IA/zh-cn_image_0000002558605846.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=C21DF4CBBB39977F7DDDE0CC8D2647C8FD9FFC88323E5790C739D5DF252EE946)
2. 在项目列表中找到您的项目，在项目下的应用列表中选择需要打开“地图服务”的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sFErM1FKTu2kKAY2g7RyjA/zh-cn_image_0000002589325373.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=F2196374C1C0D7401DED7C2498F760DECB4A3FF0042665CA0276523FC9320E8A)
3. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3DifoHtmS3uuEqDAFx6TSg/zh-cn_image_0000002589245309.png?HW-CC-KV=V1&HW-CC-Date=20260429T053858Z&HW-CC-Expire=86400&HW-CC-Sign=DD0DE118C0572246374AD96F71A887B33A0418494F95E4B02069AB2D04DA0F6E)
4. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing.md#section297715173233)。
   * 发布阶段必须[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、开启“地图服务”后重新[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)文件，并[配置签名信息](ide-publish-app.md#section280162182818)。

     说明

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
