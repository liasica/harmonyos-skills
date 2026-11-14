---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-faqs
title: Health Service Kit常见问题
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > Health Service Kit常见问题
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:21+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:90a93ec87902960d43c82a78574fe71efde95cf860d93fcacf690551b13471f1
---

## 读取今天的日常活动数据统计，与运动健康App页面数据不一致

[聚合查询](health-samplepoint-manage.md#聚合查询)接口读取今日日常活动数据，数据上报存在延时，读取实时日常活动数据建议使用[读取实时三环数据](health-three-ring-read.md)接口。

## 授权后仍然没有数据类型权限

鉴权时使用的权限是用户授权的权限与应用申请的权限的交集，需确认：

1. 应用已申请了对应的数据类型权限，申请步骤请参考[申请运动健康服务](health-apply.md)，数据类型对应的权限参考[权限说明](health-permission-description.md)。
2. 用户授权已勾选对应的权限。

## 在授权时上报1001502003错误

参考[配置Client ID](health-configuration-client-id.md)，请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，确认代码中配置的包名与client ID是匹配的。若问题仍未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

更多错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)。

## 在授权时上报1001502014错误

确保授权请求参数中的数据类型已经在**Health Service Kit**卡片中申请相应的权限，申请步骤请参考[申请运动健康服务](health-apply.md)，数据类型对应的权限参考[权限说明](health-permission-description.md)。

更多错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)。

## 用户隐私未同意，如何引导用户打开运动健康App

接口响应错误码1002703001，可通过以下方式引导用户打开运动健康App，同意隐私授权：

调用[canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)判断运动健康App是否安装。运动健康App Scheme：huaweischeme://healthapp/home/main。

* App已安装，调用[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口拉起运动健康App。运动健康App Scheme：huaweischeme://healthapp/home/main。
* App未安装，调用[应用市场推荐](appgallery-productview-loadproduct.md)接口，引导用户下载运动健康App，运动健康App包名：com.huawei.hmos.health。

## 申请运动健康被驳回的常见问题

以下为申请服务被驳回的高频典型问题，请您在申请前阅读以下内容以避免在您的申请材料中出现下述问题，若您已提交申请并被驳回，也可参考以下解决方案修改申请材料并重新提交。

### 权限说明缺失

要求：申请的每一个读/写数据权限都要在材料中说明。

解决办法：您提交的申请材料页签1和页签2中说明的权限少于所申请的权限，请检查填写的权限与所申请的权限是否一一对应，在页签1和页签2中补齐所申请的每一项权限的使用说明。

**说明** 

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

**说明** 

* 以上企业实缴注册资本数据以[国家企业信用信息公示系统](https://shiming.gsxt.gov.cn/socialuser-use-rllogin.html)中最新年报数据为准。
* 数据类型开放等级请参见[开放数据和权限总览](health-permission-description.md)。

解决办法：如您的资质不符合以上要求，需要由符合以上企业资质的公司作为保证人并提供《[担保函](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714003858.97794800280943716662489602627215:20750702004051:100005355:CBD4513F116D37E1E5BFE212973516547B1FE4DD61C5388E3248AC5086AEC255.docx)》。您需要通过**[hihealth@huawei.com](mailto:hihealth@huawei.com)**邮箱提供如下文件：

* 载明保证人对外担保流程的公司[《章程》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/plain/statutes/000/001/044/0000100000000001044.20240829085730.86499642368766203545820936006783:20740817085749:100005355:DBD975A8478DC681283B75DE2AD73917B3B11446827CA32763910C56B2011CE8.zip)。
* 符合保证人章程要求的决策文件：

  + 章程有要求的，按照章程要求提供决策文件，如[《股东（大）会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004023.16343515928607914481291350148827:20750702004051:100005355:8B4E5C1B220B83172183582BD53C8BCCF57BC737EFA1CF4F4599FEBFAD555A87.docx)、[《董事会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004003.08070939173044201994197977210474:20750702004051:100005355:48EA6076E27CA666DBABA8D928732D533089BF5EFF3B59659AA61450512C39BC.docx)等。
  + 章程无要求的，提供过半数表决权股东签字/盖章的[《股东（大）会决议》](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714004023.16343515928607914481291350148827:20750702004051:100005355:8B4E5C1B220B83172183582BD53C8BCCF57BC737EFA1CF4F4599FEBFAD555A87.docx)。
  + 公司为公司股东或者实际控制人提供担保的，必须经股东会或者股东大会决议，相关股东或受相关实际控制人支配的股东，不得参加表决，且表决由出席会议的其他股东所持表决权的过半数通过。
  + 上市公司提供担保，需要公开披露。
* 保证人盖章的《[担保函](https://hihealthbase-drcn.things.hicloud.com/healthkit/fileServer/getFile/protected/docTemplateZh/000/001/044/1000000000000001044.20250714003858.97794800280943716662489602627215:20750702004051:100005355:CBD4513F116D37E1E5BFE212973516547B1FE4DD61C5388E3248AC5086AEC255.docx)》。

**说明** 

《担保函》、《股东（大）会决议》文件中的“保证最高限额”，保留一个选项。

### 个人开发者接入资质不符合审核要求

要求：个人开发者应用未上架华为应用市场，或者个人开发者应用非移动应用，暂不开放运动健康服务数据；申请访问开放等级为基础的用户数据，个人开发者不得有个人信用不良记录。开放等级为高阶的用户数据暂不向个人开发者开放。数据开放等级请参见[开放数据和权限总览](health-permission-description.md)。

解决办法：将您的移动应用上架至华为应用市场，或重新注册企业开发者账号申请运动健康服务；申请运动健康服务时，仅勾选开放等级为“基础”的用户数据。

若仍未解决您的申请被驳回的问题，您可以选择以下方式寻求帮助：

1. 通过华为开发者联盟的[智能客服](https://developer.huawei.com/consumer/cn/customerService/#/bot-dev-top/faq-top/faq-talk-top)获取快速帮助。
2. 通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)获取人工帮助。
3. 通过华为开发者论坛的[运动健康](https://developer.huawei.com/consumer/cn/forum/block/huawei-hihealth)板块寻查答案或提问。

提交问题后，通常会在1~2个工作日内收到回复。有时需要您进一步澄清问题，请及时关注进展并予以回复，以便更好地解决问题。
