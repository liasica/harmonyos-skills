---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-apply
title: 申请运动健康服务
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 申请运动健康服务
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:24+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:a473d31f2e0b9f1ff949035904e70c661a93c859522152053525e0d6d0d8556c
---

申请运动健康服务前，请先参考[应用开发准备](application-dev-overview.md)，确认开发环境并完成[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)、[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹)等基本准备工作，再继续进行以下开发活动。

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/)，进入“开发者管理 > ID、证书和Profile > APP ID > 开放能力管理”页面，在应用列表下选择需要申请的应用。
2. 点击**运动健康服务**对应的**管理**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0govSnxAQPillkbZHyOWcg/zh-cn_image_0000002792878020.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=B36951B19A5FD09E143D075DF2CA26D63234CA09AA2D6BD6ACF34443A1BD274A)

   **说明** 

   * 暂不支持团队账号下的成员账号独立使用运动健康开发服务，详情请参见[团队账号](../start/team-account-guides-0000001053785552.md)。
3. 单击**申请Health Service Kit服务**，同意协议后，进入数据权限申请页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/72Zldp8IT2KjH13r9XuClQ/zh-cn_image_0000002821837927.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=205C2CD0F9979DC3988ECEAB10974B0C84B19DC5D1393BCC4C009CEB1F65373D)
4. 产品类型选择**HarmonyOS应用**，并填写申请信息，勾选产品必需申请的数据权限。

   **说明** 

   * 添加运动健康服务时，遵循权限最小化原则。数据访问权限应与业务相符，不可申请超出业务范围或者暂不使用的权限。
   * 在应用或服务发布后，华为会对权限使用情况进行不定期抽查，抽查形式包括但不限于对已发布的应用进行抽样检查、对API调用情况进行监控、派遣专员核查等。您可以通过在申请运动健康服务前签署的合作协议，了解核查标准以及核查后的处理方式。
   * 数据类型对应的OAuth权限请参见[权限说明](health-permission-description.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Xb83q9o0RLel8QyTcb9LFg/zh-cn_image_0000002821757929.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=43A7297AA62909AB4C29A8786995C01123AB6D7D64955A07C04AD0E84CC30149)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/WchM_-3ESrGL6PP_FOmfUw/zh-cn_image_0000002793037992.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=388041F0D205AFEA67E23A77B2D637E65B99FB261F7157BF2669F1557DD4D298)
5. 为保障用户隐私和数据安全，运动健康服务需要开发者反馈相关材料和信息，以确保应用向用户请求数据权限是合理的。

   **说明** 

   请在提交材料前先阅读[申请运动健康被驳回的常见问题](health-faqs.md#申请运动健康被驳回的常见问题)，以避免在您的申请材料中出现同类问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/J2rghl3PSrOoSILThwxL2g/zh-cn_image_0000002792878022.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB9CAACBFC0B14E13FEDF8C1E7BEC8EFFDFF92EC0646E818030FC184A8C83BD7)
6. 申请开通测试权限。

   您提交的申请需要经过人工审核，审核周期约10个工作日，请耐心等待，审批结果将以短信和邮件的形式通知您。

   * 如果提交的材料不满足要求，审批将不能通过，请您根据短信或邮件通知中的驳回原因进行修改并重新提交。重新提交的审核周期约为10个工作日，如有其他疑问，请通过[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)反馈。
   * 如果审批通过，即可进入“已开通测试权限”阶段，应用可调用相应的接口获取运动健康服务数据进行测试开发。

     **说明** 

     + 首次申请开通测试权限后权限将及时生效，若业务范围发生变动，修改权限并重新提交申请，请修改测试权限1小时后进行测试验证。
     + 当前审核通过仅以开发测试为目的，测试阶段有用户数量的限制，仅前100位用户可使用您申请应用中的华为运动健康服务。为解除用户数量的限制，请在应用完成开发测试验证后提交验证申请，具体请参见[申请验证获取正式权限](health-verification.md)提交验证申请。
     + 测试权限开通后，请于一年内完成[申请验证获取正式权限](health-verification.md)操作，否则平台将关闭您已开通的测试权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/pPl8_UprTpKqnSzwRZRcGA/zh-cn_image_0000002821837929.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCCD664B2D50FCB3D7986025B4B054AFD5FBF42A91E19206DCFD423EB1015C55)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/kMAfq9mTRWWT3v79g8uSzg/zh-cn_image_0000002821757931.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9A7335471D45C809EE67284618F0EB6067BAC218056738FBACBE125CFB32E44)
7. 权限管理。

若您的业务范围发生变动，需要修改相应的数据权限，您可以单击“管理”更新权限再次提交申请。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/zgIOOA46Sdm1z_4WrJAFpg/zh-cn_image_0000002793037994.png?HW-CC-KV=V1&HW-CC-Date=20261121T011224Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E91C65D0144BA93D50A231F78615564756F58068C08B5F181CB153C78A4DD57)
