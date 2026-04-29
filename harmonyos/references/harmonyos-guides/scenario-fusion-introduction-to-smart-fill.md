---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-to-smart-fill
title: 智能填充概述
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 智能填充概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9f46a68105f8b033b60ed9a68ae1da9c45b743cabf8f9095df5301fd45bcc5a
---

智能填充服务提供场景化的输入建议，完善应用/元服务的系统开发能力，实现用户对复杂表单的一键填充，助力打造HarmonyOS极致输入效率。开发ArkUI输入组件后（[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)以下统称输入组件），一行代码配置快速启用功能。

## 约束与限制

智能填充支持Phone、Tablet设备，并且从5.1.0(18)版本开始，新增支持2in1设备。

## 申请接入智能填充服务

### 接入须知

* 智能填充服务仅提供给[已完成认证的企业开发者](../start/edrna-0000001062678489.md)使用。
* 智能填充支持的填充字段满足应用使用智能填充的业务场景需求。字段请参考[ContentType使用场景说明](scenario-fusion-intelligentfilling-appendix.md)。

### 接入操作

智能填充服务开放能力接入需要申请与审批，申请接入流程如下：

1. 请参考[创建HarmonyOS应用/元服务](../app/agc-help-createharmonyapp-0000001945392297.md)完成为HarmonyOS应用/元服务创建APP ID工作。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“**开发与服务**”。
3. 选择应用后，在“开放能力管理”栏，找到智能填充服务的开放能力，点击右侧“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/bO8i162PReGNCqne0l1Zkg/zh-cn_image_0000002558765648.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=6588FE4691B6FDD30106E9FAB71B277666E2CB3672AA31599DA69A946C969CCE)
4. 在“新建业务申请”窗口填写申请原因，选择上传附件，然后点击“提交”。

   * 申请原因：请详细描述使用**智能填充的具体场景**。（例如：\*\*\*应用是\*\*\*（应用简介），希望在\*\*\*场景中使用智能填充\*\*\*字段信息，以提升用户表单填写效率。）字段信息请参考[ContentType使用场景说明](scenario-fusion-intelligentfilling-appendix.md)。
   * 上传附件：提供接入智能填充场景的页面图片或视频。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/zPt5l1LbQha5pOsR_Tb0og/zh-cn_image_0000002558605992.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=E6794B25F72F56783718BDBC35AE629977BBF49748A73C6278A783E5A202BF0F)

   说明

   请根据场景所需，申请必要的字段信息，并谨慎使用。若存在不合理使用的情况，我们将收回该服务授权。
5. 进入互动中心页面，可看到申请已提交的消息。
6. 返回“开放能力管理”页面，能力开关置灰，“申请”显示为“申请中”状态。
7. 申请审批通过后，互动中心将收到通知。至此，已成功接入智能填充服务。

   说明

   审批通过后，预计30分钟生效。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关，页面中可查看“关于智能填充与隐私的声明”和“权限使用说明”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/84ha5tgpRJym3DTsNkAbyg/zh-cn_image_0000002589325519.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=B05DF639D7E7F6863A2E8A93963634548AD87174BC6C7F6C3DF548F5BE184969)

* 应用/元服务的输入组件的[ContentType](scenario-fusion-intelligentfilling-appendix.md)属性配置对应场景，即可触发智能填充功能。
* 设备已连接互联网。

## 表单智能填充

### 表单填充推荐场景

点击表单中任一配置了ContentType属性的输入组件，将在其下方弹窗展示推荐的填充数据，填充数据来源请参考[推荐数据源及推荐逻辑说明](scenario-fusion-intelligentfilling-explain.md)。

* 点击表单中ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件时，将同时推荐表单中其他ContentType类型的数据（以下统称多输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/SNIQALUsQ7SQokgS-W_b3A/zh-cn_image_0000002589245457.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=376D9E6562CBC0B06BE7E3F396387C19483961AE7B97646784900FD3E20AB7DE)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/6L9m7X3FSQCY7etk_iGjtg/zh-cn_image_0000002558765650.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=2B7C9CE2ECA05BF4FD4F185F1FA28B969E41992D13CAF8CA9E53B2D7B02067D3)

* 点击其他ContentType的输入组件时，只会推荐对应场景数据。例如点击ContentType为“NICKNAME”（昵称）的输入组件时，仅会在弹窗中推荐昵称数据（以下统称单输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/HkzhfFqyTs6NMGdvqHew7Q/zh-cn_image_0000002558605994.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=28A5AE43A83CE29277B69A995B44B3B6671376A0BD1C065CBF0D99D52FEAAB54)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且其中已填入信息，在点击其他已配置ContentType的输入组件时，将根据已填入的姓名信息进行信息匹配推荐。例如姓名填写“张三”，点击“手机号码”输入组件仅推荐数据源中“张三”相关的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/cWh8JgW3RrKMthretp6YvA/zh-cn_image_0000002589325521.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=A206BF787393D479E909AADBE7E1AE996EA0B8E2FA28DCF9A0F5B8E3D222DF38)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且存在地址输入组件，在点击用户姓名类和地址信息类的ContentType输入组件时，若推荐的数据包含华为账号数据源的数据，且华为账号数据源的推荐数目少于推荐的华为账号收货地址数据时，可点击“更多地址”按钮拉起选择其他收货地址页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/pKsrLkOBRCqgHenDaXGBpg/zh-cn_image_0000002589245459.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=D9D7BB162E2DA1752CF0621F6DB39AA6F6AB332CE8259403461C70CB880B3321)

### 昵称填写推荐场景

当表单中需要昵称填写时，可从华为账号信息来源获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/oWioW0iNRHe-rOc0_TueJw/zh-cn_image_0000002558605994.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=EB85C601CDA1A5B11F3FF77571A146BD58F09795372EF92B73EB2C2D97169303)

### 日程信息推荐场景

当表单中的输入组件仅配置了ContentType为“FORMAT\_ADDRESS”（全量地址）时，会从日程信息中获取2小时内的数据进行填充推荐。

说明

日程数据源推荐场景目前仅支持中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8XF33cuoSryvrPHsCDOV3A/zh-cn_image_0000002558765652.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=32D9AC85EA51DBC08015250BED72C15124720F543ED56D8B12B86D2901BC7BC0)

### 联系人信息推荐场景

点击配置了ContentType为“PHONE\_NUMBER”（手机号）的输入组件时，若表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且已填入信息，将根据其填入的信息来推荐联系人数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Skikc3m_Qw-ZOXiWA2W1Pg/zh-cn_image_0000002558605996.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=1E99A3D8CF41A9E17C730C26EFE381EBEE1C732E7D2A6A2A6D7C868CEE811373)

### 车牌信息推荐场景

从5.1.0(18)开始，支持智能填充的推荐车牌号场景。

当表单中需要车牌号填写时，可从历史表单输入数据源中获取机主本人的车牌信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/wbsnHkG-T9yonsL08QWMgA/zh-cn_image_0000002589325523.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=2FCD4EB51B599D22A89275434602345F9657C1D9930CE6C0111B923441FEB49B)

### 护照信息推荐场景

从5.1.0(18)开始，支持智能填充的护照信息推荐场景。

表单中存在ContentType为“COUNTRY\_ADDRESS”（国籍）、“PASSPORT\_NUMBER”（护照号）、“VALIDITY”（有效期至）、“ISSUE\_AT”（签发地）的输入组件，在点击姓名类输入组件时，可从历史表单输入数据源中推荐护照信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/l-0kbxJsQBqtl-pIK3pI6g/zh-cn_image_0000002589245461.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=5F8DBD528118BE0A245B833767B3CFF7893B90E6FF2288E0F11F97239218B7F8)

### 发票抬头推荐场景

从5.1.0(18)开始，支持智能填充的发票抬头推荐场景。

当表单中存在ContentType为“ORGANIZATION”（名称）和“TAX\_ID”（税号）时，点击名称框可从华为账号数据源获取数据进行主动推荐，或根据输入内容进行匹配推荐，名称单框不支持推荐；税号框则根据名称框内容进行匹配推荐，名称框为空则进行主动推荐，税号单框不支持匹配推荐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/6zmMV0AjR4uiJyiDrvhSQw/zh-cn_image_0000002558765654.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=09D903F3CEED906F1804F0864008294B97DE8585C977CCEE234806B4913FED78)

## 历史表单输入

保存在应用/元服务中填写的表单信息，用于后续表单填充推荐。

### 保存历史表单输入场景

填写表单信息时，表单中存在配置了ContentType属性的输入组件触发历史表单输入保存页面，选择“保存”后智能填充弹窗提示开通服务，开启智能填充开关后填写表单进行一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/wPAoHIkISJqFf2F0Othr2Q/zh-cn_image_0000002558605998.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=6E899C91F85893946B2F18B275427AD5624DA43576B8EC42638E251448C59F7F)

说明

* 当使用智能填充功能的表单页面在切换或退出时，会自动触发[requestAutoSave](../harmonyos-references/js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)接口进行历史表单输入保存请求，将弹出“保存至历史表单输入”页面。也可主动调用该接口触发历史表单输入保存。
* “保存至历史表单输入”页面在点击“保存信息”按钮之后，若智能填充功能开关未打开，则弹出智能填充服务打开引导弹窗，点击“同意”按钮之后，智能填充开关会打开并将表单输入数据保存到历史表单输入中。
* “保存至历史表单输入”页面在点击“忽略”按钮后，该应用24小时之内不会再次询问。该设备累计忽略5次后，页面中将显示“忽略后不再询问”勾选框，勾选之后点击“忽略”按钮，后续将不再询问。

### 更新已有历史表单输入记录

当表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）的输入组件时，且表单还存在其他任一配置了ContentType的输入组件，在触发保存时若历史表单输入记录中存在该姓名的记录且其他数据存在差异，则拉起页面提示“更新已有记录”或“保存为新记录”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/R4x7kh12Qkq-D0sDSRXIgA/zh-cn_image_0000002589325525.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=4CA8EDBA7682578262CC9200260B9FD93CA2CE85DAA51D2B03565E68529078EF)

### 手动新增/修改历史表单输入场景

在智能填充页面或个人信息页面可以对历史表单输入进行管理。当历史表单输入中无数据，可点击“新增表单信息”进行新增；也可对已保存的信息进行修改或删除（当设备设置锁屏密码，进入历史表单输入时，需要输入锁屏密码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/bPdYDry7S4Gl9mvbtJEfyQ/zh-cn_image_0000002589245463.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=BFA29C551BB1A180863C63F4B3E2AF7F881622AE1F4509E181DDB070AA19C265)

## 云空间同步数据

同一华为账号下通过云空间实现数据上云保存，用于多设备数据同步。

### 云空间多设备同步数据场景

登录华为账号后“云空间服务 ”中 智能填充开关默认开启，可以实现多设备同步历史表单输入数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/GUtWB8OTQzazlH_-lrLujg/zh-cn_image_0000002558765656.png?HW-CC-KV=V1&HW-CC-Date=20260429T054016Z&HW-CC-Expire=86400&HW-CC-Sign=582DF489A339408B078F5F217C4C0205C80F4C9E876D6607CFCD50D2B468F928)
