---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-apply
title: 申请运动健康服务
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 申请运动健康服务
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:18+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:e49a2c8c75a0f20eb6a288202d17ab549bfcbf3e1f66b57661a312978f4021dd
---

申请运动健康服务前，请先参考[应用开发准备](application-dev-overview.md)，确认开发环境并完成[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)、[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹)等基本准备工作，再继续进行以下开发活动。

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/)，进入“开发者管理 > ID、证书和Profile > APP ID > 开放能力管理”页面，在应用列表下选择需要申请的应用。
2. 点击**运动健康服务**对应的**管理**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/3NxNBXPeR3KVhBhGzh9jJg/zh-cn_image_0000002788308038.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=D385FB048EEE1A5405C515E46DB1875A64BC2C9C360DC5688F74A110A146B2D9)

   **说明** 

   * 暂不支持团队账号下的成员账号独立使用运动健康开发服务，详情请参见[团队账号](../start/team-account-guides-0000001053785552.md)。
3. 单击**申请Health Service Kit服务**，同意协议后，进入数据权限申请页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/XDL674B8Te6PQGjreiWSRQ/zh-cn_image_0000002817427401.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8DF3D6ADACBD8D1B681A38B8DBB091C1012D343AF3BBF450E53A324D61B8FE0)
4. 产品类型选择**HarmonyOS应用**，并填写申请信息，勾选产品必需申请的数据权限。

   **说明** 

   * 添加运动健康服务时，遵循权限最小化原则。数据访问权限应与业务相符，不可申请超出业务范围或者暂不使用的权限。
   * 在应用或服务发布后，华为会对权限使用情况进行不定期抽查，抽查形式包括但不限于对已发布的应用进行抽样检查、对API调用情况进行监控、派遣专员核查等。您可以通过在申请运动健康服务前签署的合作协议，了解核查标准以及核查后的处理方式。
   * 数据类型对应的OAuth权限请参见[权限说明](health-permission-description.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/OATdE95QSGyvt-JHtVQucA/zh-cn_image_0000002788467982.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=90AA6E17D135BA8D8FD110550C78B79C891A69C649C301D6B22942E6BE28C9F6)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/QJRI6qYuRnyuR_NI3-EPJw/zh-cn_image_0000002817507471.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=F434A7ADB1ED3ACF1BED73F22604E1C4A094D2F7A27608219F966E9FE3002661)
5. 为保障用户隐私和数据安全，运动健康服务需要开发者反馈相关材料和信息，以确保应用向用户请求数据权限是合理的。

   **说明** 

   请在提交材料前先阅读[申请运动健康被驳回的常见问题](health-faqs.md#申请运动健康被驳回的常见问题)，以避免在您的申请材料中出现同类问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/bSbaRz02SCGQG1R0gucx2A/zh-cn_image_0000002788308040.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6C9B3C42AA43F392B037C732E2B3D23A12D30B6D92FD65321BE75126E1A6653)
6. 申请开通测试权限。

   您提交的申请需要经过人工审核，审核周期约10个工作日，请耐心等待，审批结果将以短信和邮件的形式通知您。

   * 如果提交的材料不满足要求，审批将不能通过，请您根据短信或邮件通知中的驳回原因进行修改并重新提交。重新提交的审核周期约为10个工作日，如有其他疑问，请通过[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)反馈。
   * 如果审批通过，即可进入“已开通测试权限”阶段，应用可调用相应的接口获取运动健康服务数据进行测试开发。

     **说明** 

     + 首次申请开通测试权限后权限将及时生效，若业务范围发生变动，修改权限并重新提交申请，请修改测试权限1小时后进行测试验证。
     + 当前审核通过仅以开发测试为目的，测试阶段有用户数量的限制，仅前100位用户可使用您申请应用中的华为运动健康服务。为解除用户数量的限制，请在应用完成开发测试验证后提交验证申请，具体请参见[申请验证获取正式权限](health-verification.md)提交验证申请。
     + 测试权限开通后，请于一年内完成[申请验证获取正式权限](health-verification.md)操作，否则平台将关闭您已开通的测试权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/5KEdp2MPRguzVPBG2Xh4sg/zh-cn_image_0000002817427403.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=10A709719D95F754A57383064F91D4F819162E8744E653DE3D4EEAFF907261AD)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/8juyryfFTfqag1dizGheDg/zh-cn_image_0000002788467984.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDA6FF8740D92FB7A6978F425F3E86AF339463E5A5A0F684A9DB842E443FD815)
7. 权限管理。

若您的业务范围发生变动，需要修改相应的数据权限，您可以单击“管理”更新权限再次提交申请。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/U25DzEx-SNavqorKCHaNsg/zh-cn_image_0000002817507473.png?HW-CC-KV=V1&HW-CC-Date=20261114T004818Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E03EF069E316479B1F7B63ABFFB18667F8F7337D59A079275AA8A548990D1B8)
