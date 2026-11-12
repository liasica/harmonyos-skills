---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:bd7f99269fc93e66470c1786d6126c85239a3fe732665e812f6b4076ad1ef75a
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

**说明** 

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/qUvSEpn0QNuyMP3GCx8i5w/zh-cn_image_0000002815559079.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCB9250A415A8953910FCC3D36B5ECF8CBF1C45BC763995FF669507BC8E345AC)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/AOfNDON4R0ekMjfsaBfZRQ/zh-cn_image_0000002815399163.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF2D8ABDDEACF50131609DFC8256C2DA2119E9E5EA819721E22F03AD28F5B180)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/z6S0rgx2TfWXpsWNiHaQDg/zh-cn_image_0000002786519588.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=387629DBD456DE9ABF7DD34012234D54246C8E064DC72EC7917D60F9FF06D35C)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/LtB2yk8mSEKjrngp0sx9Cw/zh-cn_image_0000002786359660.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6759554DD5DAD8E9196EB6B1334C7DD7224835B86BA2FC5FC39118E6DF35CC)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     **说明** 

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/I6xMtYj0S9qc_6DPcshzsA/zh-cn_image_0000002815559081.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=62BA5A55B6301785DBB2F40FD93843D61A17C4630EFF6A43B0D274021BD8691E)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Q9kC8et2QNCS7pfNfz_CWQ/zh-cn_image_0000002815399165.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7401D1E67CF444059BF122EA318B4A725FADD3938F1741C0063E7D3F2A04437)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/U49YTYAuTRSK58QB7to9fQ/zh-cn_image_0000002786519590.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0A4310183E3ABB4AE5CE85A7E2D3E523F5351791CD42FB247F4472945E005A0)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
   * **数字盾服务**：申请本服务前，需于[华为开发者联盟](https://developer.huawei.com/consumer/cn/)完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。认证通过后，您将在“开放能力管理”界面中查找到相应服务入口。

     ① 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/CJZ1d-aWSyGGAlInNbR1bg/zh-cn_image_0000002786359662.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDA661C6F3FBBD86752A9B4E20C3771845FA702CC6485B02BF6E1BE87CB037C7)

     **说明** 

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。

     ② 审核通过后勾选对应服务并点击“保存”该服务配置。
   * **星盾机密风控引擎**​：在申请“星盾机密风控引擎”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ① 点击“星盾机密风控引擎”右侧申请按钮，接入“星盾机密风控引擎”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/q8wJTO28Sg6EMZW2iA1mIg/zh-cn_image_0000002815559083.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CF4C9EDF081E1087660E3A48507D8AC8996FC832E15785D3EE53624403BD6F1)

     ② 参考“申请原因”中的模板，提供申请必需的相关信息，包含公司名称、应用用户规模、使用场景及用途，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/eXE2ExNNRSiaJPHdv5bxZw/zh-cn_image_0000002815399167.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=85D46B2352267E3147A29BFC3A2C2C6BBCF199643F489673C0626A319C4FD089)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   **说明** 

   在开通服务后，需要重新申请Profile（.p7b）文件。
