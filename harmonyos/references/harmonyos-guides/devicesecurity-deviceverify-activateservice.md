---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b89c3af751ce97850fe632816a0e6f425339bf7a031d14d6680052555cb5fdc7
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

说明

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测能力、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/n8BBLyRRSBulnvnBZFlaiA/zh-cn_image_0000002552958380.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=A627C9C37BF6F4A644D295B508ED336741CDB4D6045DC526C2E40C01C14CC0F1)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/l4efeaKgR6uhneVwzhNU3g/zh-cn_image_0000002583478381.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=E119969D56B39286188352F88F77BF36B5305F92729BC21DCD90FEDB612DA486)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/e6cZs7hoTnacmsLUDaJhtg/zh-cn_image_0000002552798732.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=0864C3F208514C4C0D856EDD3615B3C0365373194F7663B0884983ECBF17C6FC)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/M7WDdPXsQOm_-T1N0BsDJQ/zh-cn_image_0000002583438427.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=A774C6BBFA6E324F345DF343EA36BB13D33A8933D00122E17F9B656DE976CF42)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     说明

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/AgBQ37wmTTC8bY06ts2Qpw/zh-cn_image_0000002552958382.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=25FE9A572F38BE89AE7F70B3E9B35C357AC57B347F2FDF0EA480450D5F7FF2BF)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/0Evm6sOJR_2wvwVu7tNO5Q/zh-cn_image_0000002583478383.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=26D5DF3ECDF1DB2ACFCE356B35A08C4EF7FD417452384386AD7B46161B066F11)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8cjh4SNLRnGuduVN2aEW_w/zh-cn_image_0000002552798734.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=CC49D9CE979C50214611846EE5D74980924D395C49D5AA84E956EAA45E8D036A)

     说明

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
   * **数字盾服务**：点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“数字盾服务”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/zMx7r6WuTWa_XkMwa3BsNw/zh-cn_image_0000002583438429.png?HW-CC-KV=V1&HW-CC-Date=20260427T234039Z&HW-CC-Expire=86400&HW-CC-Sign=E15037119A493C5A3C469AE5D3823D4F81184150F8AA9EB72C6BE45E20E08ECD)

     说明

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   说明

   在开通服务后，需要重新申请Profile（.p7b）文件。
