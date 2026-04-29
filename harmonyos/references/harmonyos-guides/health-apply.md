---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-apply
title: 申请运动健康服务
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 开发准备 > 申请运动健康服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d95a3c52fee289bb9aedbb270b46053d8d199636bde4df1c15e20981e0d88c2
---

申请运动健康服务前，请先参考[应用开发准备](application-dev-overview.md)，确认开发环境并完成[创建项目](../app/agc-help-create-project-0000002242804048.md)、[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)、[添加公钥指纹](application-dev-overview.md#section1726913517284)等基本准备工作，再继续进行以下开发活动。

1. 登录[开发者联盟网站](https://developer.huawei.com/consumer/cn/)，单击进入“管理中心”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/tJ1zz19STqSGtU60_uvG5g/zh-cn_image_0000002558765408.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=B590C0E86CF83130700E8CD267CAFF9AC8E5A0FDBC2E1FF3B810C29628ED5C25)

   若您尚未注册开发者账号，请先完成[注册账号](../start/registration-and-verification-0000001053628148.md)和[实名认证](../start/itrna-0000001076878172.md)。开发者可实名认证为个人开发者或者企业开发者，认证前，请先了解二者的[权益区别](../start/dbiae-0000001336403980.md)。
2. 在应用服务中，单击**Health Service Kit**卡片。如果无“Health Service Kit”卡片，请单击右上角“自定义桌面”添加卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/gUBWqCK4Rm-JdqQaXCXtZQ/zh-cn_image_0000002558605752.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=4E3839AABE563162A7C40638467CB9E4F3714D2CF89E1AEBC36B726B6537140C)

   说明

   * 暂不支持团队账号下的成员账号独立使用运动健康开发服务，详情请参见[团队账号](../start/team-account-guides-0000001053785552.md)。
3. 单击**申请Health Service Kit服务**，同意协议后，进入数据权限申请页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/DK54QDYjRB2HCho3bDh1NQ/zh-cn_image_0000002589325279.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=6236A576178E066B2B697BC72E58A7971355848095F5B083C5894F9C2E08551E)
4. 产品类型选择**HarmonyOS应用**，并填写申请信息，勾选产品必需申请的数据权限。

   说明

   * 添加运动健康服务时，遵循权限最小化原则。数据访问权限应与业务相符，不可申请超出业务范围或者暂不使用的权限。
   * 在应用或服务发布后，华为会对权限使用情况进行不定期抽查，抽查形式包括但不限于对已发布的应用进行抽样检查、对API调用情况进行监控、派遣专员核查等。您可以通过在申请运动健康服务前签署的合作协议，了解核查标准以及核查后的处理方式。
   * 数据类型对应的OAuth权限请参见[权限说明](health-permission-description.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/rqHih7FZRnWmiwigPFr5-w/zh-cn_image_0000002589245215.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=F8CBAA4325A2597B1167D96320184680256E206B317C22D9E82EF20D13245C6B)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/eX4RrxqbS4ST455debVZ6g/zh-cn_image_0000002558765410.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=CDC3A5802F489F7983E0800E1BD5FD2E5EDC634A593BA91AC793C27069F4224D)
5. 为保障用户隐私和数据安全，运动健康服务需要开发者反馈相关材料和信息，以确保应用向用户请求数据权限是合理的。

   说明

   请在提交材料前先阅读[申请被驳回的常见问题](health-apply.md#申请被驳回的常见问题)，以避免在您的申请材料中出现同类问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/psXF2gPFSCa8PsvOsl5PmA/zh-cn_image_0000002558605754.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=D34C1DBC9BB7AA69F7F3CFA20C5E5B158972703B18C771C7003C8AA3D28FF534)
6. 申请开通测试权限。

   您提交的申请需要经过人工审核，审核周期约15个工作日，请耐心等待，审批结果将以短信和邮件的形式通知您。

   * 如果提交的材料不满足要求，审批将不能通过，请您根据短信或邮件通知中的驳回原因进行修改并重新提交。重新提交的审核周期约为15个工作日，如有其他疑问，请通过[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)反馈。
   * 如果审批通过，即可进入“已开通测试权限”阶段，应用可调用相应的接口获取运动健康服务数据进行测试开发。

     说明

     + 首次申请开通测试权限后权限将及时生效，若业务范围发生变动，修改权限并重新提交申请，请修改测试权限1小时后进行测试验证。
     + 当前审核通过仅以开发测试为目的，测试阶段有用户数量的限制，仅前100位用户可使用您申请应用中的华为运动健康服务。为解除用户数量的限制，请在应用完成开发测试验证后提交验证申请，具体请参见[申请验证获取正式权限](health-verification.md)提交验证申请。
     + 测试权限开通后，请于半年内完成[申请验证获取正式权限](health-verification.md)操作，否则平台将关闭您已开通测试权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/2h0QGpCXQMaDFmWw30mX3Q/zh-cn_image_0000002589325281.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=C63CB6AB2CE99C8F6E5EF3BE35363A13EC754B59FD2BA4792FC3CBEA15EB1E36)

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/lE7_KwR1RM2na5Op0VMFsw/zh-cn_image_0000002589245217.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=0B7FD670FEAF6FD262189199CB1941EF6AD91A9F8AA56646E14286B41074513A)
7. 权限管理。

   若您的业务范围发生变动，需要修改相应的数据权限，您可以单击“管理”更新权限再次提交申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/PZSdCDMdRVO-ldrPxBx_Rw/zh-cn_image_0000002558765412.png?HW-CC-KV=V1&HW-CC-Date=20260429T053818Z&HW-CC-Expire=86400&HW-CC-Sign=44B693808E0081F1EB4E31B0CCCD90F6687A27A4783545EDF1AF8418D78C779B)

## 申请被驳回的常见问题

以下为申请服务被驳回的高频典型问题，请您在申请前阅读以下内容以避免在您的申请材料中出现下述问题，若您已提交申请并被驳回，也可参考以下解决方案修改申请材料并重新提交。

### 权限说明缺失

要求：申请的每一个读/写数据权限都要在材料中说明。

解决办法：您提交的申请材料页签1和页签2中说明的权限少于所申请的权限，请检查填写的权限与所申请的权限是否一一对应，在页签1和页签2中补齐所申请的每一项权限的使用说明。

说明

如您申请的数据读/写权限的使用场景在应用开发过程中发生变化，请在申请验证前更新申请材料清单。

### 图标使用不规范

要求：图标的使用需遵循[标志使用规范](health-logo-usage-regulations.md)。

解决办法：您提交的申请材料中涉及华为运动健康图标展示的场景，按照[标志使用规范](health-logo-usage-regulations.md)中要求的视觉效果进行呈现。

### 必选内容未填写

要求：申请材料中每个标注“必填”的页签都需要填写。

解决办法：您提交的申请材料中存在未填写的页签，尤其是企业开发者需要填写“企业介绍”页签，若您为个人开发者，请填写“开发者信息”，并明确个人所在科研机构或大学等。

### 企业、事业单位/政府机构、社会团体实缴注册资本不符合审核要求

要求：

* 企业申请资质要求：企业以实缴注册资本为准，申请访问开放等级为基础的用户数据，企业实缴注册资本不低于50万元；申请访问开放等级为高阶的用户数据，企业实缴注册资本不低于500万元。申请主体存续且成立时间需1年以上；
* 事业单位/政府机构申请资质要求：如果申请主体为事业单位或政府机构，可免除资金和成立年限要求。事业单位或政府机构委托的企业，需遵循企业申请资质要求。
* 社会团体申请资质要求：社会团体以活动资金（注册资本）为准，申请访问开放等级为基础的用户数据，活动资金不低于50万元；申请访问开放等级为高阶的用户数据，活动资金不低于500万元。申请主体存续且成立时间需1年以上。

说明

* 以上企业实缴注册资本数据以[国家企业信用信息公示系统](https://shiming.gsxt.gov.cn/socialuser-use-rllogin.html)中最新年报数据为准。
* 数据类型开放等级请参见[数据开放总览](health-data-overview.md)。

解决办法：如您的资质不符合以上要求，需要由符合以上企业资质的公司作为保证人并提供《[担保函](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714003858.97794800280943716662489602627215:20750702004051:100005355:CBD4513F116D37E1E5BFE212973516547B1FE4DD61C5388E3248AC5086AEC255.docx)》。您需要通过**[hihealth@huawei.com](mailto:hihealth@huawei.com)**邮箱提供如下文件：

* 载明保证人对外担保流程的公司[《章程》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/plain/statutes/000/001/044/0000100000000001044.20240829085730.86499642368766203545820936006783:20740817085749:100005355:DBD975A8478DC681283B75DE2AD73917B3B11446827CA32763910C56B2011CE8.zip)。
* 符合保证人章程要求的决策文件：

  + 章程有要求的，按照章程要求提供决策文件，如[《股东（大）会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004023.16343515928607914481291350148827:20750702004051:100005355:8B4E5C1B220B83172183582BD53C8BCCF57BC737EFA1CF4F4599FEBFAD555A87.docx)、[《董事会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004003.08070939173044201994197977210474:20750702004051:100005355:48EA6076E27CA666DBABA8D928732D533089BF5EFF3B59659AA61450512C39BC.docx)等。
  + 章程无要求的，提供过半数表决权股东签字/盖章的[《股东（大）会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004023.16343515928607914481291350148827:20750702004051:100005355:8B4E5C1B220B83172183582BD53C8BCCF57BC737EFA1CF4F4599FEBFAD555A87.docx)。
  + 公司为公司股东或者实际控制人提供担保的，必须经股东会或者股东大会决议，相关股东或受相关实际控制人支配的股东，不得参加表决，且表决由出席会议的其他股东所持表决权的过半数通过。
  + 上市公司提供担保，需要公开披露。
* 保证人盖章的《[担保函](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714003858.97794800280943716662489602627215:20750702004051:100005355:CBD4513F116D37E1E5BFE212973516547B1FE4DD61C5388E3248AC5086AEC255.docx)》。

说明

《担保函》、《股东（大）会决议》文件中的“保证最高限额”，保留一个选项。

### 个人开发者接入资质不符合审核要求

要求：个人开发者应用未上架华为应用市场，或者个人开发者应用非移动应用，暂不开放运动健康服务数据；申请访问开放等级为基础的用户数据，个人开发者不得有个人信用不良记录。开放等级为高阶的用户数据暂不向个人开发者开放。数据开放等级请参见[数据开放总览](health-data-overview.md)。

解决办法：将您的移动应用上架至华为应用市场，或重新注册企业开发者账号申请运动健康服务；申请运动健康服务时，仅勾选开放等级为“基础”的用户数据。

若仍未解决您的申请被驳回的问题，您可以选择以下方式寻求帮助：

1. 通过华为开发者联盟的[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)获取快速帮助。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取人工帮助。
3. 通过华为开发者论坛的[运动健康](https://developer.huawei.com/consumer/cn/forum/block/huawei-hihealth)板块寻查答案或提问。

提交问题后，通常会在1~2个工作日内收到回复。有时需要您进一步澄清问题，请及时关注进展并予以回复，以便更好地解决问题。
