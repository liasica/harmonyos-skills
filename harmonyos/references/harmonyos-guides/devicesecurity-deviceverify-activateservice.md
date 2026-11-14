---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:27+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:b0d0b4abffbb2776f136415878fe47d1f7d151be711b3c23293cbdc476e924e7
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

**说明** 

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/UWIO6xz2RFiuQa977-DaoQ/zh-cn_image_0000002788467334.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=79F44ADEB0E9EA0BF220647A54BA46BCA2F91D088ABBCE394486D6D398884354)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/IjCrzoSoQOCPp127ndTp3g/zh-cn_image_0000002817506823.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3E6276C0AE0D360E1BAD7D840106ED9FEC492813C5F69D41C106DD6997AC43B)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Lfq8tpt4SoeXdEO3SY2QuQ/zh-cn_image_0000002788307392.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=513826EF1E95FC3307C83B9BE7EB8323CB1B30522AB727F9FEBD90AD970B919D)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/jDA_4MYVQqWUMVT3fSNnuA/zh-cn_image_0000002817426755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8FD4452848F239AE563C36ACA969C9CFC0CA903532F6DFCA9D0D1A5A3ECBF20)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     **说明** 

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/j3LR-VQRTeGJpBL9SaEggQ/zh-cn_image_0000002788467336.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=26ECF46DCF1B9BD426CBECFBA5145278ECBBC51C6CBCDA6FCC49826CDADC6D92)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/45WzV71ySUG_TaKn6ID3ag/zh-cn_image_0000002817506825.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED436DF2621353E9C7B401D3E7F229608789F5338B4D92E9AF6B7C6B78D77B43)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XhhpqZSlRG-Qw9gVuG48wg/zh-cn_image_0000002788307394.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0E79A97C072D4B09A67A05DC3C3E6D998B6F197BB87D15F7FF4D81747A1F7E7)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
   * **数字盾服务**：申请本服务前，需于[华为开发者联盟](https://developer.huawei.com/consumer/cn/)完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。认证通过后，您将在“开放能力管理”界面中查找到相应服务入口。

     ① 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ODWBPOL7Tba0kWVpdMJAMA/zh-cn_image_0000002817426757.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BB978718D18A1444EEF2296AFD1E679C92D033DD0F22EA00E5B1C68E6FF9157)

     **说明** 

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。

     ② 审核通过后勾选对应服务并点击“保存”该服务配置。
   * **星盾机密风控引擎**​：在申请“星盾机密风控引擎”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ① 点击“星盾机密风控引擎”右侧申请按钮，接入“星盾机密风控引擎”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/-k9z4658TIqW4inCKwl43A/zh-cn_image_0000002788467338.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=B51AC34FCD8F28C06118A268985513D32203721314C86894D19B0ACBA656590E)

     ② 参考“申请原因”中的模板，提供申请必需的相关信息，包含公司名称、应用用户规模、使用场景及用途，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/alUPCSzfQmGxV7AVV5llwA/zh-cn_image_0000002817506827.png?HW-CC-KV=V1&HW-CC-Date=20261114T004548Z&HW-CC-Expire=31536000000&HW-CC-Sign=C23AD7C09AE3A9AB340683A34CD473DA8030E8C0C277112959181D98B9BA1C0B)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   **说明** 

   在开通服务后，需要重新申请Profile（.p7b）文件。
