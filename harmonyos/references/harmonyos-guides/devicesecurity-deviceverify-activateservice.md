---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-10-15T07:04:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2e3821e970c8914908b19c74f93b36fe99699f343f209350cb555403efb9394e
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

**说明** 

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Y_jeZADlRci7ZX_RQE0BFw/zh-cn_image_0000002762500286.png)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/wRuYlYkdQ9mMVCbB6L_Niw/zh-cn_image_0000002791738949.png)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/AEcDxGnKSyi2X_N13OYAug/zh-cn_image_0000002762340368.png)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/vrzPIilARUi_-cHgAqPJ1A/zh-cn_image_0000002791859167.png)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     **说明** 

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/8MrWWAk5SMqsHzwUKKKrlw/zh-cn_image_0000002762500288.png)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/vpplRAqAS7a3KnPNgO9RFA/zh-cn_image_0000002791738951.png)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/RGn5UqjmQaa8J4ryJf7AwQ/zh-cn_image_0000002762340370.png)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
   * **数字盾服务**：申请本服务前，需于[华为开发者联盟](https://developer.huawei.com/consumer/cn/)完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。认证通过后，您将在“开放能力管理”界面中查找到相应服务入口。

     ① 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/pdbCZDv0S36-UrrLs9MFAw/zh-cn_image_0000002791859169.png)

     **说明** 

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。

     ② 审核通过后勾选对应服务并点击“保存”该服务配置。
   * **星盾机密风控引擎**​：在申请“星盾机密风控引擎”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ① 点击“星盾机密风控引擎”右侧申请按钮，接入“星盾机密风控引擎”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/EB80A25_R_GoElxkW_rrJg/zh-cn_image_0000002762500290.png)

     ② 参考“申请原因”中的模板，提供申请必需的相关信息，包含公司名称、应用用户规模、使用场景及用途，然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/iuqZAjyhQvC6CzaT-BFmwA/zh-cn_image_0000002791738953.png)

     **说明** 

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   **说明** 

   在开通服务后，需要重新申请Profile（.p7b）文件。
