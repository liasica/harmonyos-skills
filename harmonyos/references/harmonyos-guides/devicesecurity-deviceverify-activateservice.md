---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice
title: 开通Device Security服务
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 开发准备 > 开通Device Security服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7cd3610186efd3dead7843611c54eecc34fdb945693685ce6fea22a85db52ff
---

在开通Device Security服务前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作，再继续进行以下开发活动。

说明

Device Security包括应用设备状态检测、安全检测、可信应用服务、业务风险检测能力、数字盾服务，开发者请根据实际使用场景，选择开启某个或者多个能力开关。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择开发与服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/2XR2E-1ZRneO2wQ6f-xbxQ/zh-cn_image_0000002589324747.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=30E54E5E4DAC8E02E5FDEA648E192FCC2C3F54EBE561BC610BC0114B2AA181E6)
2. 在项目列表中找到需要开通Device Security服务的项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/QSKuw8ULRdOc1_-YNT7PYA/zh-cn_image_0000002589244685.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=4262A3A7943882C7BA0BBC7817D706E54DC2CC642DF281EC3884B79D092BF29F)
3. 选择“开放能力管理”Tab页，找到需要使用的功能，点击左侧的按钮，开通相应的功能。

   * **应用设备状态检测**：勾选“应用设备状态检测”并点击“保存”，接入“应用设备状态检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/28v97I2-QyeXmEZVSQnpvA/zh-cn_image_0000002558764880.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=71761F369A24691959B2F6957AB33A2AABCECA51F42802CF8869CE4809801ABA)
   * **安全检测**：勾选“安全检测服务”并点击“保存”，接入“安全检测服务”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/KjNM5T_eTLufroGQ2NLF3w/zh-cn_image_0000002558605224.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=DEF50C6CFFEB93CB8185B39F8A0B80BE5826E28E946B334422889D9CDF1B1E52)
   * **可信应用服务**：勾选“可信应用服务”并点击“保存”，接入“可信应用服务”。

     说明

     开通“可信应用服务”需要先申请进入允许清单，请将Developer ID、公司名称、应用名称、申请使用的服务和使用该服务的场景，发送到agconnect@huawei.com。AGC运营将审核相关材料，通过后将为您配置受限开放服务使用的名单，审核周期为1-3个工作日，请耐心等待。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/zQvT4_tjS0ux4adjPouKwA/zh-cn_image_0000002589324749.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=57D8A2A2872C6B397166AC212B4786755F073B05DC87C0CADC0F8B77D3816D01)
   * **业务风险检测-涉诈剧本检测**：点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“涉诈剧本检测”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“涉诈剧本检测”右侧申请按钮，接入“涉诈剧本检测”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/wH17bE5NQpOuSOUqj4sYvw/zh-cn_image_0000002589244687.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=623C745A80F83C72050CB12DBC25E2F16078E75BA0C7AE004BAE86875304A880)

     ③ 参考“申请原因”中的模板，提供申请必需的相关信息，包含Developer ID、公司名称、应用名称、使用场景、使用该服务的合法基础（应用使用该服务时需在其隐私声明中进行个人数据声明及用途说明，详细参考[个人数据处理说明](devicesecurity-personal-data.md)，并将合法基础的相关证明上传至申请附件），然后点击“提交”按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/P5fofVmBQ4eMksqBzzlYew/zh-cn_image_0000002558764882.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=402A78182EFAB56A6EABF7986D25447D66FF947CFDCD3E9F55CAF94B1E3501BE)

     说明

     提交申请后，AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
   * **数字盾服务**：点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ① 在申请“数字盾服务”前，需要在[华为开发者联盟](https://developer.huawei.com/consumer/cn/)网站上注册成为开发者，并完成[企业开发者实名认证](../start/edrna-0000001062678489.md)。

     ② 点击“数字盾服务”右侧申请按钮，接入“数字盾服务”，审核通过后勾选对应服务并点击“保存”该服务配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/kJquUGQCSi2PqEoHwH2HcA/zh-cn_image_0000002558605226.png?HW-CC-KV=V1&HW-CC-Date=20260429T053127Z&HW-CC-Expire=86400&HW-CC-Sign=D91BA401EE046B50F733E93EA75F8CC4A0E157BB3626BF09416D449A6E04E961)

     说明

     请您在申请框填写“数字盾服务”申请原因和应用场景。AGC运营将审核相关材料，通过后则可保存对应的服务配置，审核周期为1-3个工作日，请耐心等待。
4. 申请Profile（.p7b）文件，具体操作请参见[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)。

   说明

   在开通服务后，需要重新申请Profile（.p7b）文件。
