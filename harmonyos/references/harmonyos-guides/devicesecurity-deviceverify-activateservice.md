---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:32+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:ca9507cb5167b6a7f9ea0f190e32a53ce88fc98871466e63319da42f674a08a3
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

**说明** 

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/r9egkcRxS-eGFRrx9Ha3vA/zh-cn_image_0000002821757279.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=55965A8A799FC954D845B603C7810D79F5E9E14BCD5CD1242C9F25F8E7C34941)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/tcom35PdRfanHkQgV31aDg/zh-cn_image_0000002793037342.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=D76A5FB37AD6C2421E0F208E3CACB603A0587B49CD5D860D895BBB8225FDC26D)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/yn10FOVaRKS6_YobRChHOw/zh-cn_image_0000002792877372.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AF704EBEDDAF94652F375C935DD573C4E1BCE265F2CE9A58BBCE32CCDC2093D)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/BRInbsoiT96YOXMTa1FY_g/zh-cn_image_0000002821837279.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=C430719505080F0C9A793F61B01028B4D4712E5A0A6C5F50A95F508F7DB98C1D)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     **说明** 

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/BOhmEI7xRsuvhJIaL6SyMw/zh-cn_image_0000002821757281.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B5D649B0AD74D051EE0DD3E5A1F6B00542A3B2CF02B008398A2E450FC9F75B2)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/H-YDFqQjRd2uYlOlZ9NcIQ/zh-cn_image_0000002793037344.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=D61C282429B03864A50F6872C9CCF23D074CA9651FC933E3AE53C66303E7681B)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、申请使用的服务、使用该服务的场景，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/sGpuJIckQqSHQijvzBOuqw/zh-cn_image_0000002792877374.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=63614FE46544B8B136E9BB6A6D9057137F0997E3210283594D268077B94FFDD1)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
   * **数字盾服务**：申请本服务前，需于[华为开发者联盟](https://developer.huawei.com/consumer/cn/)完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。认证通过后，您将在“开放能力管理”界面中查找到相应服务入口。

     ① 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ct-4FmiNTd-wQqGrdKV7Yg/zh-cn_image_0000002821837281.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=658113FF21303ABE90B9F1EEEF9D5C54B6983EAC3BE0D521DE6722BC195BE7B4)

     **说明** 

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。

     ② 审核通过后勾选对应服务并点击“保存”该服务配置。
   * **星盾机密风控引擎**​：在申请“星盾机密风控引擎”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)。

     ① 点击“星盾机密风控引擎”右侧申请按钮，接入“星盾机密风控引擎”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/RdDy7DF6QSa-1PxVGRmSHA/zh-cn_image_0000002821757283.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACB6191FA22F6B79B0BDB3571494D47DF985D0CB0C98D641C05FBCD8387119B9)

     ② 参考“申请原因”中的模板，提供申请必需的相关信息，包含公司名称、应用用户规模、使用场景及用途，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/X9OHR9ONSiWb9WoHrQ0_VQ/zh-cn_image_0000002793037346.png?HW-CC-KV=V1&HW-CC-Date=20261121T011132Z&HW-CC-Expire=31536000000&HW-CC-Sign=431D9A691A0D4B09EF0B065DF76868907513A0EAE2E934F1F0F1B6D5D8CF4672)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。该能力暂不支持In-house应用。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   **说明** 

   在开通服务后，需要重新申请Profile（.p7b）文件。
