---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-apply
title: 申请运动健康服务
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发准备 > 申请运动健康服务
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:58+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:f9c44fa991a6088a19ce2bdc77bc970d7bfc81b4524da2dee846f90e2ec1512e
---

申请运动健康服务前，请先参考[应用开发准备](application-dev-overview.md)，确认开发环境并完成[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)、[添加公钥指纹](application-dev-overview.md#条件必选添加公钥指纹)等基本准备工作，再继续进行以下开发活动。

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console#/)，进入“开发者管理 > ID、证书和Profile > APP ID > 开放能力管理”页面，在应用列表下选择需要申请的应用。
2. 点击**运动健康服务**对应的**管理**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/MnUFKyFgRx6RnbVp8iy59w/zh-cn_image_0000002820406319.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA2978A68AF37BA7B4368AB2D4799976410A0732A1C4264EAB149D17EDCCE972)

   **说明** 

   * 暂不支持团队账号下的成员账号独立使用运动健康开发服务，详情请参见[团队账号](../start/team-account-guides-0000001053785552.md)。
3. 单击**申请Health Service Kit服务**，同意协议后，进入数据权限申请页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/D1zjpRjqTZCpoyQplqRStw/zh-cn_image_0000002791726340.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAA9301DCB31CB33CC4BEC22DA8DF6FF3CDC4B42D966EFA0DA036AB6C661C031)
4. 产品类型选择**HarmonyOS应用**，并填写申请信息，勾选产品必需申请的数据权限。

   **说明** 

   * 添加运动健康服务时，遵循权限最小化原则。数据访问权限应与业务相符，不可申请超出业务范围或者暂不使用的权限。
   * 在应用或服务发布后，华为会对权限使用情况进行不定期抽查，抽查形式包括但不限于对已发布的应用进行抽样检查、对API调用情况进行监控、派遣专员核查等。您可以通过在申请运动健康服务前签署的合作协议，了解核查标准以及核查后的处理方式。
   * 数据类型对应的OAuth权限请参见[权限说明](health-permission-description.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/ecMj9g-ETV6-WzV-lfH-PA/zh-cn_image_0000002791566368.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E3A0B148CEB6D473B3638A213C2A9CCB9B02C44F3E4D53F2DA8E19F92AB00CB)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CG9UoKs0TC2W8a3IzLNtog/zh-cn_image_0000002820526321.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBCC40CEB2242FC019952D4A3BA931C3C8E7DDE551D57D2CAEE34C29E40D4B17)
5. 为保障用户隐私和数据安全，运动健康服务需要开发者反馈相关材料和信息，以确保应用向用户请求数据权限是合理的。

   **说明** 

   请在提交材料前先阅读[申请运动健康被驳回的常见问题](health-faqs.md#申请运动健康被驳回的常见问题)，以避免在您的申请材料中出现同类问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/55GkvhYqQNWi0KvdB_AQHA/zh-cn_image_0000002820406321.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=770829A2058785DA939FE010DDE7EA2BA71DCA430AF754BC85A024DA745122F5)
6. 申请开通测试权限。

   您提交的申请需要经过人工审核，审核周期约10个工作日，请耐心等待，审批结果将以短信和邮件的形式通知您。

   * 如果提交的材料不满足要求，审批将不能通过，请您根据短信或邮件通知中的驳回原因进行修改并重新提交。重新提交的审核周期约为10个工作日，如有其他疑问，请通过[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)反馈。
   * 如果审批通过，即可进入“已开通测试权限”阶段，应用可调用相应的接口获取运动健康服务数据进行测试开发。

     **说明** 

     + 首次申请开通测试权限后权限将及时生效，若业务范围发生变动，修改权限并重新提交申请，请修改测试权限1小时后进行测试验证。
     + 当前审核通过仅以开发测试为目的，测试阶段有用户数量的限制，仅前100位用户可使用您申请应用中的华为运动健康服务。为解除用户数量的限制，请在应用完成开发测试验证后提交验证申请，具体请参见[申请验证获取正式权限](health-verification.md)提交验证申请。
     + 测试权限开通后，请于一年内完成[申请验证获取正式权限](health-verification.md)操作，否则平台将关闭您已开通的测试权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/5K3OENZaRT2Ep77elikKwg/zh-cn_image_0000002791726342.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=A58A3D1570F7D6D997EC2CF0DBA4C58898628395BE4DD115BBE6EB3989ADEC4F)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/2KkPednVQ9WNMQKVSbBtCg/zh-cn_image_0000002791566370.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D9B14A4ADFF203314D080EA9F7D4E13E07C096D40D0736C3D9163B1A57D4435)
7. 权限管理。

若您的业务范围发生变动，需要修改相应的数据权限，您可以单击“管理”更新权限再次提交申请。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/N0Jidsa1TwSdTc6YRCKwMQ/zh-cn_image_0000002820526323.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=E91FE172919603AC62B3A1B355CA4FEF869B013BA5BC871EA3EDAC4D23217C8E)
