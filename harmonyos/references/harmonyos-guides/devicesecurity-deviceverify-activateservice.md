---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:06+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:c31a03a5dfe0462a4bdca871b45ac2e1a704dc5895a78a8d4a4f373bd67a1f55
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

**说明** 

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/JOyYm0zCQfy89jlC6WJDyA/zh-cn_image_0000002791565718.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=21124290A93F5744E5D347DE2424EC925DDE226BAC68593D94A4F04C63965E7E)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/SyadfUUvSqCAdxBOWn5yGw/zh-cn_image_0000002820525671.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8D8BD3CDE8A42E5FB71200EA3499C7F9E275E16855067491C4EB33115A2ABE7)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/W_OoAxBuSXGdkB1VzeLEEw/zh-cn_image_0000002820405671.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=891EC79FB3C4849777AB81E2F76836105130A2F681A65934693F98C879930A14)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/HjImuEKwTTSFqbKzcG2tkw/zh-cn_image_0000002791725692.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B9B29F31FA685A5E1FCC24684BE965FC24F74207CA99C0A4C36A6F220AAD74E)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     **说明** 

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/7UWpIlOFSeSJDkSmEQGIpQ/zh-cn_image_0000002791565720.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB70B4EC8F0138489791D49DD3AD01B8DB5DCDA6317C2510AD2911393EA317D1)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1rq2_oBBR_GpK2y159XBPw/zh-cn_image_0000002820525673.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=74CFCBC8992566E7C9F7CC3D8F0FF0FACE37E07C72D4A26EA41208EF0AC022C0)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、申请使用的服务、使用该服务的场景，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DzG32BIGRPO8rY6dHJc1kw/zh-cn_image_0000002820405673.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=98AEAA8F95D411FC1D0CCE51F1B0659B531B9916B37977EA7EDB3D449C87E69D)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
   * **数字盾服务**：申请本服务前，需于[华为开发者联盟](https://developer.huawei.com/consumer/cn/)完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。认证通过后，您将在“开放能力管理”界面中查找到相应服务入口。

     ① 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Lwp9IJcuRveM_sWcx8M6DQ/zh-cn_image_0000002791725694.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF900704EF59E805043E4B449371C3505E9A26A00866A64C1F344CFAC85825B0)

     **说明** 

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。

     ② 审核通过后勾选对应服务并点击“保存”该服务配置。
   * **星盾机密风控引擎**​：在申请“星盾机密风控引擎”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ① 点击“星盾机密风控引擎”右侧申请按钮，接入“星盾机密风控引擎”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/YIzjqye1R9GEtxGlBAuS5A/zh-cn_image_0000002791565722.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=10F9BFB7862A37A5246BB1CE7A3DEF64441041EBA0D02F9DDD9BF1C203CB061B)

     ② 参考“申请原因”中的模板，提供申请必需的相关信息，包含公司名称、应用用户规模、使用场景及用途，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/6ryn2cijS3O6dlDLSsQsqg/zh-cn_image_0000002820525675.png?HW-CC-KV=V1&HW-CC-Date=20261119T014714Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CE6B362505E534991B41B72B9EF2DBE73B91C4AD63B35BB978AEC45D4A22544)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   **说明** 

   在开通服务后，需要重新申请Profile（.p7b）文件。
