---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-to-smart-fill
title: 智能填充概述
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 智能填充概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:12+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:2e7811ca4b4b0405b6fec0b4ed8f95301b539bb55391c2f6c4ace31ca955944e
---

智能填充服务提供场景化的输入建议，完善应用/元服务的系统开发能力，实现用户对复杂表单的一键填充，助力打造HarmonyOS极致输入效率。开发ArkUI输入组件后（[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)以下统称输入组件），一行代码配置快速启用功能。

## 约束与限制

智能填充支持Phone、Tablet设备，并且从5.1.0(18)版本开始，新增支持PC/2in1设备。

## 申请接入智能填充服务

### 接入须知

* 智能填充服务仅提供给[已完成认证的企业开发者](../doccenter-getting-started/hdc-edrna-0000002752527889.md)使用。
* 智能填充支持的填充字段满足应用使用智能填充的业务场景需求。字段请参考[ContentType使用场景说明](scenario-fusion-intelligentfilling-appendix.md)。
* 从HarmonyOS 7.0.0.109开始，智能填充新增智能识别模式，兼容开发者适配ContentType与智能识别两种模式。其中，智能识别模式仅支持已接入智能填充的应用使用；该模式通过智能识别页面填表字段类型，使开发者无需适配ContentType即可完成接入，从而获得智能填充体验。

### 接入操作

智能填充服务开放能力接入需要申请与审批，申请接入流程如下：

1. 请参考[创建HarmonyOS应用/元服务](../app/agc-help-createharmonyapp-0000001945392297.md)完成为HarmonyOS应用/元服务创建APP ID工作。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“**开发与服务**”。
3. 选择应用后，在“开放能力管理”栏，找到智能填充服务的开放能力，点击右侧“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/MbQq2koRQlyExo7wWnA9sA/zh-cn_image_0000002820406575.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CC84C9F9E21E0490B0CB350EFB50B1DBF869C133CA3278B8B41CA7D6BE9F6D1)
4. 在“新建业务申请”窗口填写申请原因，选择上传附件，然后点击“提交”。

   * 申请原因：请详细描述使用**智能填充的具体场景**。（例如：\*\*\*应用是\*\*\*（应用简介），希望在\*\*\*场景中使用智能填充\*\*\*字段信息，以提升用户表单填写效率。）字段信息请参考[ContentType使用场景说明](scenario-fusion-intelligentfilling-appendix.md)。
   * 上传附件：提供接入智能填充场景的页面图片或视频。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/ZndI8vVXQLeIKeAMBV7Wcw/zh-cn_image_0000002791726596.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=63A6405CE0233CA2CCBC69A05C4563E73A04AD34EE1EC158F0F41B42EA3650B4)

   **说明** 

   请根据场景所需，申请必要的字段信息，并谨慎使用。若存在不合理使用的情况，我们将收回该服务授权。
5. 进入互动中心页面，可看到申请已提交的消息。
6. 返回“开放能力管理”页面，能力开关置灰，“申请”显示为“申请中”状态。
7. 申请审批通过后，互动中心将收到通知。至此，已成功接入智能填充服务。

   **说明** 

   审批通过后，预计30分钟生效。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关，页面中可查看“关于智能填充与隐私的声明”和“权限使用说明”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/EG1hsP4TQim0obnbW7UOVg/zh-cn_image_0000002791566624.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=034DB591D19C92B5174C5010FF8D07EC6C497FE8E5E2E3D6F3C7937E4AD57722)

* 应用/元服务的输入组件的[ContentType](scenario-fusion-intelligentfilling-appendix.md)属性配置对应场景，即可触发智能填充功能。
* 设备已连接互联网。

## 表单智能填充

### 表单填充推荐场景

点击表单中任一配置了ContentType属性的输入组件，将在其下方弹窗展示推荐的填充数据，填充数据来源请参考[推荐数据源及推荐逻辑说明](scenario-fusion-intelligentfilling-explain.md)。

* 点击表单中ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件时，将同时推荐表单中其他ContentType类型的数据（以下统称多输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/b5xOSL6aR_WoMJu5liSBvA/zh-cn_image_0000002820526577.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=4646ACF75B897DCAE53FA278F584E831541B72ACD512434DD878E4715DA205B6)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Y-3JFugMQAygXgDmhvNScg/zh-cn_image_0000002820406577.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=65082FBC824FDC2DEBD1B3E9A6DBCAB54EC84AAAD7C786543B24614ABCBF6BFF)

* 点击其他ContentType的输入组件时，只会推荐对应场景数据。例如点击ContentType为“NICKNAME”（昵称）的输入组件时，仅会在弹窗中推荐昵称数据（以下统称单输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/jiDGJ2Q3RNu1RGX_i_OMXw/zh-cn_image_0000002791726598.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA74E48B59771F83366C98D3D69AEDF379C1C92D8EA1008A21F4450D3E5960B0)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且其中已填入信息，在点击其他已配置ContentType的输入组件时，将根据已填入的姓名信息进行信息匹配推荐。例如姓名填写“张三”，点击“手机号码”输入组件仅推荐数据源中“张三”相关的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/cobPUSpPTICpRAuBj6ZY0w/zh-cn_image_0000002791566626.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=0254A680613EBB66BFAA7C43AB2AEE4C5D392A1D28F46F6086CE00C91E500A24)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且存在地址输入组件，在点击用户姓名类和地址信息类的ContentType输入组件时，若推荐的数据包含华为账号数据源的数据，且华为账号数据源的推荐数目少于华为账号收货地址总数时，可点击“更多地址”按钮拉起选择其他收货地址页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/sttW95qPRhGb0zbU7BNymg/zh-cn_image_0000002820526579.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD46D0432F5F86BF92BA9C1A083B3316007AF5985CC5CE4BC9F5EA2068132CB7)

### 昵称填写推荐场景

当表单中需要昵称填写时，可从华为账号信息来源获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/VERkOacGSGaCKVKSImXJ_A/zh-cn_image_0000002791726598.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDA0D95641CCFEAB7788ADC2E814E5DBAAF8D8BA07B4EA12227520F141C04C2F)

### 日程信息推荐场景

当表单中的输入组件仅配置了ContentType为“FORMAT\_ADDRESS”（全量地址）时，会从日程信息中获取2小时内的数据进行填充推荐。

**说明** 

日程数据源推荐场景目前仅支持中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/cPUYYp6vSmOYRWm-3Ow22g/zh-cn_image_0000002820406579.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=F177F0AB6AEDC3EDEED9C5B3404A8D12EB707719F73790806FC62CC8C00EDE7C)

### 联系人信息推荐场景

点击配置了ContentType为“PHONE\_NUMBER”（手机号）的输入组件时，若表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且已填入信息，将根据其填入的信息来推荐联系人数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Y0PKjb0RQWG2Vr2ShqoJLA/zh-cn_image_0000002791726600.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FB17479DA900E001AB1DC4A3B4A0A27651F54D683A0B18E7D75A8FF6964DAFD)

### 车牌信息推荐场景

从5.1.0(18)开始，支持智能填充的推荐车牌号场景。

当表单中需要车牌号填写时，可从历史表单输入和华为账号数据源中获取车牌信息。

**说明** 

从API版本26.0.0开始，支持华为账号数据源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/dK6Y8C41RaKC8Ml43F38KQ/zh-cn_image_0000002791566628.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=330E1BF3E964C188F55790A3EBFE09F711510E7E47A1AB91F96D3FEC86AE0F80)

### 护照信息推荐场景

从5.1.0(18)开始，支持智能填充的护照信息推荐场景。

表单中存在ContentType为“COUNTRY\_ADDRESS”（国籍）、“PASSPORT\_NUMBER”（护照号）、“VALIDITY”（有效期至）、“ISSUE\_AT”（签发地）的输入组件，在点击姓名类输入组件时，可从历史表单输入数据源中推荐护照信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/itr8BlE7Qo6bVMZoJxF1vA/zh-cn_image_0000002820526581.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=115DD1CBF9F9D430763FCB389F02246C8F90B73EA4697203B80E87FA72F2B17E)

### 发票抬头推荐场景

从5.1.0(18)开始，支持智能填充的发票抬头推荐场景。

当表单中存在ContentType为“ORGANIZATION”（名称）和“TAX\_ID”（税号）时，点击名称框可从华为账号数据源获取数据进行主动推荐，或根据输入内容进行匹配推荐，名称单框不支持推荐；税号框则根据名称框内容进行匹配推荐，名称框为空则进行主动推荐，税号单框不支持匹配推荐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/YCk1wZcfQiODyTix-JGHvg/zh-cn_image_0000002820406581.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E584287426E9BEB8799F5740156E9C9E2D6E08D33DBA797FAAE0EF4154BB8EF)

### 智能识别模式下通过导航条拉起智能填充进行填充推荐场景

从HarmonyOS 7.0.0.109开始，支持智能识别模式下通过导航条拉起智能填充进行填充推荐场景。

**说明** 

* 仅支持已接入智能填充的应用使用，接入请参考[接入操作](scenario-fusion-introduction-to-smart-fill.md#接入操作)。
* 使用智能识别模式前需在设备上选择“设置 > 隐私和安全 > 智能填充”，开启“智能识别表单”开关，并在“设置 > 小艺 > 小艺建议 > 导航条主动服务”，打开“页面感知”开关。

当表单输入组件未配置ContentType时，可通过智能识别页面表单字段类型完成填充数据推荐。在进入到表单页面时，若有能够填充的表单数据，导航条会提示智能填充选项，用户点击后拉起推荐数据半模态，选择其中一条数据即可完成表单填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/4RrMNl2NSgKTL4DwSK4ngw/zh-cn_image_0000002791726602.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BE3B01ED83834906C4D709175BA057A6495D449DAC37545CEC50F1E6C4337E2)

若进入到表单页面时，表单有“姓名”或“姓+名”的输入组件且已有数据，会进行匹配推荐，若有能够填充的表单数据，导航条会提示智能填充选项，用户点击后拉起推荐数据半模态，选择其中一条数据即可完成表单填充。

**说明** 

若需要使用小艺帮记数据源进行填充，请在设备上选择“设置 > 隐私和安全 > 智能填充 > 小艺帮记”，开启“使用小艺帮记作为填充建议”开关。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/g50BvCTCRaCcTFt4ZAadoQ/zh-cn_image_0000002791566630.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F3CE2FA332A1866210589B8A9EAF9CCA7A1D5654573A9EE974ADDB1D7515769)

当处在表单页面时，用户可通过长按导航条触发智能填充，若有能够填充的表单数据，导航条会提示智能填充选项，用户点击后拉起推荐数据半模态，选择其中一条数据即可完成表单填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/DLlQauYjTJmN9KBmhHw4rg/zh-cn_image_0000002820526583.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B9BF30AA09C488992D3BE7AD4D0B96D3E005C6712B5555A02BE1803CB8D403C)

## 历史表单输入

保存在应用/元服务中填写的表单信息，用于后续表单填充推荐。

### 保存历史表单输入场景

填写表单信息时，表单中存在配置了ContentType属性的输入组件触发历史表单输入保存页面，选择“保存”后智能填充弹窗提示开通服务，开启智能填充开关后填写表单进行一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/NKiH3Q_mSQSVwj54gW5hJg/zh-cn_image_0000002820406583.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=B75FB690DEE1CC3DE7287F33AAC005DA0BE78CA1610BACAF3ED0AB2360FADE46)

**说明** 

* 当使用智能填充功能的表单页面在切换或退出时，会自动触发[requestAutoSave](../harmonyos-references/js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)接口进行历史表单输入保存请求，将弹出“保存至历史表单输入”页面。也可主动调用该接口触发历史表单输入保存。
* 当应用通过条件渲染方式控制表单填写场景的显隐时，需主动调用[requestAutoSave](../harmonyos-references/js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)接口触发历史表单输入保存。
* “保存至历史表单输入”页面在点击“保存信息”按钮之后，若智能填充功能开关未打开，则弹出智能填充服务打开引导弹窗，点击“同意”按钮之后，智能填充开关会打开并将表单输入数据保存到历史表单输入中。
* “保存至历史表单输入”页面在点击“忽略”按钮后，该应用24小时之内不会再次询问。该设备累计忽略5次后，页面中将显示“忽略后不再询问”勾选框，勾选之后点击“忽略”按钮，后续将不再询问。

### 更新已有历史表单输入记录

当表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）的输入组件时，且表单还存在其他任一配置了ContentType的输入组件，在触发保存时，若历史表单输入记录中存在该姓名的记录且其他数据存在差异，则拉起页面提示“更新已有记录”或“保存为新记录”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/mCs8NoUJR568pJjfV_ssow/zh-cn_image_0000002791726604.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=249E477F6F69C0DA3FC77F1F487BF8819B9E366AAD3A57A57DF042B8A151D8EE)

### 手动新增/修改历史表单输入场景

在智能填充页面或个人信息页面可以对历史表单输入进行管理。当历史表单输入中无数据，可点击“新增表单信息”进行新增；也可对已保存的信息进行修改或删除（当设备设置锁屏密码，进入历史表单输入时，需要输入锁屏密码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/COQdBglVTgeRtdnnjqCXyQ/zh-cn_image_0000002791566632.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF9A3E6220AACF17543CB34D1DD981D7F8C4B625ACD70446E1403FB0DD9D4D51)

## 云空间同步数据

同一华为账号下通过云空间实现数据上云保存，用于多设备数据同步。

### 云空间多设备同步数据场景

登录华为账号后“云空间服务 ”中 智能填充开关默认开启，可以实现多设备同步历史表单输入数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/BsiQGLk_SNyWxkKL9PxcLg/zh-cn_image_0000002820526585.png?HW-CC-KV=V1&HW-CC-Date=20261119T014911Z&HW-CC-Expire=31536000000&HW-CC-Sign=B401D73DDD38724DFBB0CFEBC560DC2AD64D8D1D4AFB5F20D78E7A426F88668A)
