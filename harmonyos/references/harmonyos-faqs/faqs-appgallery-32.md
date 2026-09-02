---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-32
title: HarmonyOS应用备案指导和常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS应用备案指导和常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:4b7120eaf3401cad3fd2cc2fecf1e9c6d03e1ca7ddec57e7eca7bfe123b25899
---

## 问题现象

应用上架需要填写备案信息，实际开发者在进行备案过程中可能会遇到各种问题，比如：所有应用必须备案吗，应该怎么备案？备案有哪些渠道，需要提前准备什么信息？如何验证备案完成等等。

本文将对应用备案做一个完整的阐述，帮助开发者了解备案的操作和常见问题。

## 背景知识

根据[《工业和信息化部关于开展移动互联网应用程序备案工作的通知》](https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2023/art_920db564162e4312916a01bed6540ad8.html)要求，APP主办者应当依据[《中华人民共和国反电信网络诈骗法》](https://www.miit.gov.cn/jgsj/zfs/fl/art/2022/art_d30139b442a141f48f05775d8c0b3cee.html)第二十三条"设立移动互联网应用程序应当按照国家有关规定向电信主管部门办理许可或者备案手续"相关规定履行备案手续。未履行备案手续的，不得从事APP互联网信息服务。因此APP应用上架应用市场必须先完成备案。

## 解决方案

1. 应用如何备案？
   * APP主办者需要在接入商备案系统提交备案材料，由接入商代为备案。常见的接入商有：华为云、阿里云、腾讯云、移动云、天翼云、联通云等。关于如何选择接入商具体还需要根据您所选择的服务器提供商而定。一般来说服务器选择的是哪家接入商，备案可以在同一个接入商网站完成。
   * 一般通用的流程如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/7sW4797RR8y6plXYibpicQ/zh-cn_image_0000002722888675.png "点击放大")
   * 具体根据不同接入商备案流程不一致，可以参考各大接入商具体流程：

     [华为云备案指引](https://support.huaweicloud.com/usermanual-icp/zh-cn_topic_0000002127712329.html)。

     [阿里云备案指引](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview?spm=a2c4g.11186623.0.0.abb4bcecUMrfca)。

     [腾讯云备案指引](https://cloud.tencent.com/document/product/243/97668)。

     [移动云备案指引](https://ecloud.10086.cn/op-help-center/doc/outline/35512)。

     [天翼云备案指引](https://www.ctyun.cn/document/10000037/10747389)。

     [联通云备案指引](https://support.cucloud.cn/document/127/593/756.html?id=756&arcid=1063)。
2. 应用备案特征信息中的公钥和签名怎么获取？
   * 登录AppGallery Connect，点击"证书、APP ID和Profile"，在页面左侧点击"证书"，下载需要备案的HarmonyOS应用/元服务开发者证书；
   * 使用文本编辑器（如记事本）打开已下载的证书，可以看到直接下载的证书链有3段，分别：根证书、中间证书和服务器证书；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/y3mb8A_9Q9mtuB4lU9Ew2g/zh-cn_image_0000002723008605.png "点击放大")
   * 删除根证书和中间证书，保留服务器证书后，点击保存；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/tkz-XSvzSBOnS0HOt7tkpw/zh-cn_image_0000002693209120.png "点击放大")
   * 双击打开已保存的证书，点击"详细信息-公钥"，获取APP的公钥信息；

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/dhxP0NOORWyGkbgMEPmILw/zh-cn_image_0000002693049260.png "点击放大")
   * 双击打开已保存的证书点击"详细信息-指纹"，获取APP的sha1签名信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/LCJpe3pQT1i50IHbdf73oA/zh-cn_image_0000002722888677.png "点击放大")
3. 如何校验应用已经完成备案？
   * 接入商网站查询。可以登录接入商网站查询备案进度和结果。
   * 短信通知。备案完成后一般也会通过短信通知给备案信息填写时提供的主办者手机号。
   * 工信部网站查询。可以登录[备案管理系统](https://beian.miit.gov.cn/)查询备案号和域名等信息。
   * AGC网站备案校验。登录AGC网站，左侧导航栏选择"应用上架>版本信息"，右侧页面进入"备案信息"区域，根据备案信息如实填写后，点击"校验证件号"查询。
4. 上架备案信息如何填写？

   上架备案信息涉及的信息如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/K-aBkmqTQOaHx01aMmioog/zh-cn_image_0000002723007625.png "点击放大")
5. 应用需要备案：APP服务器在中国大陆，且APP需要上架应用市场。
   * 选择APP类型信息选择"您的APP服务器在中国大陆"。
   * 主办单位类型，根据备案主办单位的实际情况勾选企业、个人或机构。
   * 主办单位与开发者账号主体是否一致，如您的APP备案主办单位与开发者账号主体一致，请勾选与开发者账号主体一致。

     **说明** 

     勾选主办单位与开发者账号主体一致时，需确保上述主办单位类型勾选正确，否则无法正常完成校验（如您的备案主办单位类型为企业/机构，请勿勾选个人）。
   * 确保提交审核时填写的应用名称、包名与备案时填写的应用名称、包名完全一致。
   * 在填写"主体证件号"时，要区分"数字5"和"字母S"，"数字1"和"字母I"，"数字0"和"字母O"。
   * 备案信息填写后，可以点击"校验证件号"查询。
6. 应用不需要备案：APP服务器不在中国大陆（境外应用）。

   备案信息勾选"您的APP服务器不在中国大陆"。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/sq58M4_LRq6b7Jt7VcouHQ/zh-cn_image_0000002693048818.png "点击放大")

   境外应用定义：由境外主体运营且服务器仅放置在境外的移动互联网应用程序。
7. 应用不需要备案：单机应用。

   备案信息勾选"您的APP为单机APP"。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/Qh0m-g8YQBio1I5fj7Y9nA/zh-cn_image_0000002723008369.png "点击放大")

   单机应用定义：未通过连接公共互联网提供互联网信息服务的移动应用程序。

## 常见FAQ

Q：在应用上架前，需要提交备案信息，其中包含统一社会信用代码、组织机构代码、身份证号等证件号，在校验证件号时提示验证次数已达上限怎么解决？

A：为了防止校验证件号功能被滥用，此功能每天有使用次数上限，超过上限将会提示验证次数已达上限。校验证件号功能验证次数次日会刷新，从而可以使用此功能。上述功能仅用于用户自验证证件号准确性，不影响提交应用上架审核功能。当天在确保备案信息已填写正确的情况下，依然可以提交应用上架审核，AGC应用市场会进行复核相关备案信息，具体审核结果以后续反馈的审核意见为准。

Q：提交APP审核时，无填写备案信息的入口，导致上架审核驳回，怎么解决？

A：如应用申请过APP备案白名单，AGC页面无备案信息入口，可以继续联系华为接口人或者[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/)反馈，取消白名单后页面会开放备案信息填写的入口，后续提交审核就可以填写备案信息进行校验。

Q：应用其他平台版本已经备过案了，HarmonyOS应用需要重新备案吗？

A：需要进行备案。如果一款APP已备案其他平台版本等平台，需要新增上架HarmonyOS平台（HarmonyOS应用/元服务），可申请变更备案，增加勾选HarmonyOS平台，并对应增加HarmonyOS平台的包名等特征信息（可添加多个）。

Q：同名应用和元服务的ICP备案号需要分别申请吗？

A：华为云的备案号与包名只能是一一对应的，需要分别申请。使用阿里云等其他机构可以用同一个备案号添加多个包名，无需再分别申请。

Q：怎么区分开发主体和开发者账户主体（上架主体）以及应用归属主体，备案应该谁来备案？

A：APP备案是某个主体下面的应用包名的平台类型备案。如果我们开发者账户的认证主体是A，但实际开发主体是B，这时候看应用归属权属于谁就由谁去备案，应用上架的主体可以和备案的主体不一致，只需要填写备案信息时选择主办单位是否和开发者账号主体一致。

Q：没有用到华为云服务器，在进行华为云备案时该如何选择资源类型？用云函数和数据库生成的服务端该如何备案？

A：华为云备案正常是需要使用华为云服务器进行备案的，如果没有华为云服务器可以使用其他账号的[备案授权码](https://support.huaweicloud.com/icp_faq/zh-cn_topic_0173231867.html)进行备案，后续在备案订单内【资源类型】选择【备案授权码】然后复制进去一串授权码数字即可。

Q：应用上架智慧屏幕是否必须视听备案号？

A：所有HarmonyOS Next/5.x智慧屏应用都需申请广电总局视听备案号(HarmonyOS 4.0版本已有备案号也需申请Harmony Next版本备案号)。音、视频类应用还需与牌照方合作对接，若有计费包，需同时对计费包进行备案。

Q：打开.cer证书获取的指纹是sha1指纹，有些接入商需要提供md5指纹，应该如何获取呢？

A：一般接入商可以直接使用sha1指纹进行备案，如果确实需要获取md5指纹，可以通过openssl命令获取。如下：

D:\>openssl x509 -fingerprint -md5 -noout -in myapp.cer

md5 Fingerprint=55:9F:F7:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:59:C9:9A:3A:08:8E

当然sha1指纹也可以通过命令获取：

D:\>openssl x509 -fingerprint -sha1 -noout -in myapp.cer

sha1 Fingerprint=15:3E:C8:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:DF:46:F1:53:AF:84:C9:BF:D0:61

Q：元服务是否也需要备案，流程和应用是否一致？

A：元服务备案流程和应用一致，都需要备案。华为云备案平台特为元服务提供了备案通道，您可以直接参考[元服务备案](../atomic-guides/atomic-service-filing.md)除此外，在三大运营商那边备案的。开发者在运营商的平台上去申请，按照快应用的方式或者叫快应用的载体进行备案即可。

Q：备案中的信息的空格和冒号是否要去掉？

A：在备案时，通常需要提供证书的公钥以及md5值。根据相关规定，公钥以及md5值中的":"号需要被删除。删除后，不需要使用空格代替，直接保留纯数字和字母即可。若备案平台没有空格字符校验，可以直接复制公钥填充。

Q：一台ECS弹性云服务器最多可以备案几个网址？

A：备案授权码由ECS弹性云服务器、华为云Flexus应用服务器（X实例，L实例）需包月3个月及以上生成，一台服务器可生成5个备案授权码，一个授权码只能备案一个网站或者APP，具体参考[备案限制](https://support.huaweicloud.com/icprb-icp/icp_01_0008.html)。

Q：APP需要在设置或者介绍等显著位置标注备案号吗？

A：应工信部要求APP主办者应当在APP显著位置标明其备案编号，并在备案编号下方按要求链接备案系统网址，供公众查询核对，参考[工信部发布开展移动互联网应用程序备案工作的通知](https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2023/art_920db564162e4312916a01bed6540ad8.html)，如果没有标识备案编号，会导致应用上架审核不通过，已上架应用下架等。

Q：备案需要多少时间？

A：备案所需时长主要分为两个阶段：服务商初审和工信部终审，具体时间如下：

* 服务商初审阶段：华为云等平台人工初审通常需要3-5个工作日。若初审发现问题需修改，需重新提交并再次等待3-5个工作日。
* 工信部终审阶段：初审通过后需在24小时内完成工信部短信验证。短信核验成功后进入通管局审核，耗时2-20个工作日（不同省份差异较大）。
* 整体时间预估：服务商初审（3-5天）+工信部终审（2-20天），总耗时约5-25个工作日。

Q：HarmonyOS App开发者账号的主体是A主体，备案到B主体，这种备案方式可以吗？

A：应用发布账号主体可以和备案主体不一致，您可以在AppGallery Connect应用信息配置页面的"备案信息"栏中勾选"与开发者账号主体不一致"，同时填写APP备案主体（主办单位）B的信息，包括主办单位名称和证件号。

Q：鸿蒙PC应用上架为什么一定要提供ICP备案，其他PC客户端没有这样的要求？

A：应用资质审核要求中未强制要求提交ICP备案，具体可参考[应用资质审核要求](../app/80301.md)。
