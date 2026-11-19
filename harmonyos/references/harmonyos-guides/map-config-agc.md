---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7f9ba42e4e06b7593b5fbc727c16a1c41e228d0a2faacb9a139ae918ad0668c7
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/hnOacSHARaOHyYIHzGTotQ/zh-cn_image_0000002791726434.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=3163F8AC3286C63D27AAE20E806C9AE81330D4CAAE653DDE541766E8AB9CD837)
2. 选择文件，点击项目结构。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZnClyh2ESfKoHDwF1AZhSw/zh-cn_image_0000002791566462.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=66F4DE0E3B8F07FBE2F8F9609E069C2BE6C75903A981D585C37340CA26ED312E)
3. 进入“Signing Configs”页面，点击“Enable open capabilities”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/esffr5U1QCWjkJARsuL0MQ/zh-cn_image_0000002820526415.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=358EFD5AC64132F152D4971F8A30B48FAAE01756BDA654427F5BB220B817F1AB)
4. 勾选“Map Kit”选项，点击“OK”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/rCKBikAERkG8HI0uwo897Q/zh-cn_image_0000002820406415.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7AE722F5A39BAE74CA4E7490D04762A5C92FCAC7BD9E275404DA2BE00F30EF9)
5. 选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/mETbgVQ1TVC7ig_CVBQ3RQ/zh-cn_image_0000002791726436.png?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F731543ECCD662C54708DD99090B15F6724DD4C3B7C5398691ACCBC1795BD8D)

方式二：通过HarmonyOS 开发者中心网站开通地图服务。

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html#/home/)网站，选择“应用管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/1mi6U9WISz2fpxFGZMKDwg/zh-cn_image_0000002791566464.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAD978631C4D8060C8E9EC41462A2C029D8E840D43FBA69873C3D54D1C5BE135)
2. 选择开放能力管理，找到“地图服务”开关，打开开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/o3lH18gmQ_mn-yTG-5PxbQ/zh-cn_image_0000002820526417.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014810Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB49DA1869E49AB09D24EDB2AFED4B0925F6CC66FCD157604F4151A69B85BCC0)
3. 确认已经开启“地图服务”开放能力，并完成签名。

   * 调试阶段必须[申请调试证书](../app/agc-help-add-debugcert-0000001914263178.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启"地图服务"后重新[申请调试Profile文件](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing-manual.md)。
   * 发布前请确保开通地图服务，然后请参考[发布应用](ide-publish-app.md)。

     **说明** 

     若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
