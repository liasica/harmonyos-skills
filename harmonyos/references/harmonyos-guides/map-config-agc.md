---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3eb5aecd16a0858ef9b807152f2dd3d80bd9f3ef5f44e723e38130175ff460d4
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/X7eJRxSkQ5iva6jw5YnfvA/zh-cn_image_0000002817427495.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F09A03D69532E447859C8B89692CE4EE0BAC0939041391F7A535F5F101602D8)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/qNgrOLhhTD2TmWtvyU1jGQ/zh-cn_image_0000002788468076.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FCC49A4B52559C4EF9A4A35C2AAE4240454145AB81A0F38F8A37FDA02C0509C)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/rDk07l6tSCu2wdoF12u5Rw/zh-cn_image_0000002817507565.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=62956661F489E0AC0530B669C0940016632573271EE9344C653CABE03499D9DB)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1hs99a6ZTfGgudOLq_1o9w/zh-cn_image_0000002788308134.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=857A3427018FC3ACFD9D430983559351F554D7709C90642650AC2FBA9FE09D7E)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/L3EXZ-0xTlagxF2cg1Yoqw/zh-cn_image_0000002817427497.png?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=3516F712CC989331E55F622C2D7D06A5C68098C2446BA634452C14D4392EE265)

方式二：通过HarmonyOS 开发者中心网站开通地图服务。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)网站，选择“应用管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/sBe6njImT4i83pAOAjPpqA/zh-cn_image_0000002788468078.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDD3A6E61EA125CC16A952A5773E02373673D511264DE8CC023938EED2DABCAF)
2. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/u0Ng7diDTAiZ_FPmF7Mtcw/zh-cn_image_0000002817507567.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004823Z&HW-CC-Expire=31536000000&HW-CC-Sign=454E158F6C4F96619AA9E9E06A01A01B19DE090901000D68B4598A4E221260BF)
3. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing-manual.md)。
   * 发布前请确保开通地图服务，然后请参考[发布应用](ide-publish-app.md)。

     **说明** 

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
