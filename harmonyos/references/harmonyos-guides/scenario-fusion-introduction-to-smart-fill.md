---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-to-smart-fill
title: 智能填充概述
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 智能填充概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:05b377d5572e71949e573fe89505b997dbe6abdb86c5b9c360a1656782b4faf7
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qbWspQlsQvKHNryRZweZkA/zh-cn_image_0000002583479147.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=D0589A57106B30A84247BFDBA4CD6B574616BE8BB45206BAAB3C5D7DC21748BC)
4. 在“新建业务申请”窗口填写申请原因，选择上传附件，然后点击“提交”。

   * 申请原因：请详细描述使用**智能填充的具体场景**。（例如：\*\*\*应用是\*\*\*（应用简介），希望在\*\*\*场景中使用智能填充\*\*\*字段信息，以提升用户表单填写效率。）字段信息请参考[ContentType使用场景说明](scenario-fusion-intelligentfilling-appendix.md)。
   * 上传附件：提供接入智能填充场景的页面图片或视频。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/jLJUEcpmQZG2ZX_VRx8qQA/zh-cn_image_0000002552799498.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=251ADD70891103BBA02750A71CC2F338FB9C9CB5AF637BD6440BDA9229DEAB78)

   说明

   请根据场景所需，申请必要的字段信息，并谨慎使用。若存在不合理使用的情况，我们将收回该服务授权。
5. 进入互动中心页面，可看到申请已提交的消息。
6. 返回“开放能力管理”页面，能力开关置灰，“申请”显示为“申请中”状态。
7. 申请审批通过后，互动中心将收到通知。至此，已成功接入智能填充服务。

   说明

   审批通过后，预计30分钟生效。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关，页面中可查看“关于智能填充与隐私的声明”和“权限使用说明”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ROjQzy7QQ_ijMkvW_ZJHcg/zh-cn_image_0000002583439193.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=4F6AC3C02E8A8BF9B6F04D8D423EEF1F318BB0E2E2B55DBFFCD9C849C50F4E8E)

* 应用/元服务的输入组件的[ContentType](scenario-fusion-intelligentfilling-appendix.md)属性配置对应场景，即可触发智能填充功能。
* 设备已连接互联网。

## 表单智能填充

### 表单填充推荐场景

点击表单中任一配置了ContentType属性的输入组件，将在其下方弹窗展示推荐的填充数据，填充数据来源请参考[推荐数据源及推荐逻辑说明](scenario-fusion-intelligentfilling-explain.md)。

* 点击表单中ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件时，将同时推荐表单中其他ContentType类型的数据（以下统称多输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/CFCmd4SxQJa5Tx5eo7hGNQ/zh-cn_image_0000002552959148.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=401A60718C489965E1B3B20552279A798FCD7E9584F4D84D1412CF7EE4F16B00)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/r81qWYvTRz2_jW8NMSThWw/zh-cn_image_0000002583479149.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=B8D1EFEA3508539E4D93BCE11E7DAE312E8F972B1356E9D9393EFBC0A5E796B9)

* 点击其他ContentType的输入组件时，只会推荐对应场景数据。例如点击ContentType为“NICKNAME”（昵称）的输入组件时，仅会在弹窗中推荐昵称数据（以下统称单输入框场景）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/V7rRScNjT1itHTx-btuJBw/zh-cn_image_0000002552799500.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=09761A5A2EA45B9AB026AC4F9ABD36C917B5CAA1410AF6E5675C4C335EBBBB64)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且其中已填入信息，在点击其他已配置ContentType的输入组件时，将根据已填入的姓名信息进行信息匹配推荐。例如姓名填写“张三”，点击“手机号码”输入组件仅推荐数据源中“张三”相关的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/UIxjcTcJQ3OzqEaropw7-A/zh-cn_image_0000002583439195.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=1D862692428B4B5CF00B2DD045E989678F9C52138E957CF1B9100D0D961EE160)

* 表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且存在地址输入组件，在点击用户姓名类和地址信息类的ContentType输入组件时，若推荐的数据包含华为账号数据源的数据，且华为账号数据源的推荐数目少于推荐的华为账号收货地址数据时，可点击“更多地址”按钮拉起选择其他收货地址页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/xBjrCYviSRGa7xja3tDzTw/zh-cn_image_0000002552959150.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=E7168A1BE4F4109F82379526671453B3BFDF2EB393D91C47411676EDA69B9101)

### 昵称填写推荐场景

当表单中需要昵称填写时，可从华为账号信息来源获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/4juc3PpDTLa8tH3lq6E8Ag/zh-cn_image_0000002552799500.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=3A26DD618E69EF66A686DF8C03415AA5A826D9371AD66641DCD358EAB2CB90F5)

### 日程信息推荐场景

当表单中的输入组件仅配置了ContentType为“FORMAT\_ADDRESS”（全量地址）时，会从日程信息中获取2小时内的数据进行填充推荐。

说明

日程数据源推荐场景目前仅支持中文地址。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/W56oG-1nRtaXeO2MhwlfXg/zh-cn_image_0000002583479151.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=AEEB0AA4CBDFF10C2E6DEA147D2BADCA7D0356B6F4AB61A3B282216A2F93B7B4)

### 联系人信息推荐场景

点击配置了ContentType为“PHONE\_NUMBER”（手机号）的输入组件时，若表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）或“PERSON\_LAST\_NAME”（姓氏）、“PERSON\_FIRST\_NAME”（名字）的输入组件且已填入信息，将根据其填入的信息来推荐联系人数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/lyLw5kh2QfKOkbNx9kdMIA/zh-cn_image_0000002552799502.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=3F082B75B29E76F87557C075742BB3661B236831704811F180D46AA740A566CC)

### 车牌信息推荐场景

从5.1.0(18)开始，支持智能填充的推荐车牌号场景。

当表单中需要车牌号填写时，可从历史表单输入数据源中获取机主本人的车牌信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Vq4FUqwKQqCdgyGLhDXMFw/zh-cn_image_0000002583439197.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=9D3D90C78A4E62112DD784B7A9D4CBD99803F29E278D63BDB9AD663D0B161BD2)

### 护照信息推荐场景

从5.1.0(18)开始，支持智能填充的护照信息推荐场景。

表单中存在ContentType为“COUNTRY\_ADDRESS”（国籍）、“PASSPORT\_NUMBER”（护照号）、“VALIDITY”（有效期至）、“ISSUE\_AT”（签发地）的输入组件，在点击姓名类输入组件时，可从历史表单输入数据源中推荐护照信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/3glsC3uyRvCZsC42Mqm9gQ/zh-cn_image_0000002552959152.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=EF615AF6258EB60F3D8D5500D6206E5BF2715C77C118254DB22BBBADEF19FB5F)

### 发票抬头推荐场景

从5.1.0(18)开始，支持智能填充的发票抬头推荐场景。

当表单中存在ContentType为“ORGANIZATION”（名称）和“TAX\_ID”（税号）时，点击名称框可从华为账号数据源获取数据进行主动推荐，或根据输入内容进行匹配推荐，名称单框不支持推荐；税号框则根据名称框内容进行匹配推荐，名称框为空则进行主动推荐，税号单框不支持匹配推荐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/MQb7MgKwRQybjLQAVydAPw/zh-cn_image_0000002583479153.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=9244F0694E09BA13C13E12DAA122841695FF21D2072C4D1C141B3A0A3B2E44C3)

## 历史表单输入

保存在应用/元服务中填写的表单信息，用于后续表单填充推荐。

### 保存历史表单输入场景

填写表单信息时，表单中存在配置了ContentType属性的输入组件触发历史表单输入保存页面，选择“保存”后智能填充弹窗提示开通服务，开启智能填充开关后填写表单进行一键填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/r9i7KsuPQWu3bJ-JOOHiUQ/zh-cn_image_0000002552799504.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=057D56764215A944CFFAC1C4CBB3893A8BC63CB897B2ECEE546EF93230F0887A)

说明

* 当使用智能填充功能的表单页面在切换或退出时，会自动触发[requestAutoSave](../harmonyos-references/js-apis-app-ability-autofillmanager.md#autofillmanagerrequestautosave)接口进行历史表单输入保存请求，将弹出“保存至历史表单输入”页面。也可主动调用该接口触发历史表单输入保存。
* “保存至历史表单输入”页面在点击“保存信息”按钮之后，若智能填充功能开关未打开，则弹出智能填充服务打开引导弹窗，点击“同意”按钮之后，智能填充开关会打开并将表单输入数据保存到历史表单输入中。
* “保存至历史表单输入”页面在点击“忽略”按钮后，该应用24小时之内不会再次询问。该设备累计忽略5次后，页面中将显示“忽略后不再询问”勾选框，勾选之后点击“忽略”按钮，后续将不再询问。

### 更新已有历史表单输入记录

当表单中存在ContentType为“PERSON\_FULL\_NAME”（姓名）的输入组件时，且表单还存在其他任一配置了ContentType的输入组件，在触发保存时若历史表单输入记录中存在该姓名的记录且其他数据存在差异，则拉起页面提示“更新已有记录”或“保存为新记录”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/zCTavXgQSxyVG6pLrJEtIQ/zh-cn_image_0000002583439199.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=9A88944770111EDDB33955AD4C01E9E08797C357941809AB82CFF9D3C8DF2593)

### 手动新增/修改历史表单输入场景

在智能填充页面或个人信息页面可以对历史表单输入进行管理。当历史表单输入中无数据，可点击“新增表单信息”进行新增；也可对已保存的信息进行修改或删除（当设备设置锁屏密码，进入历史表单输入时，需要输入锁屏密码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/9GE0nrvBSziDTU7-QTjvZQ/zh-cn_image_0000002552959154.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=BD28BCF9E9F74FEBF2D48519578B8EE079C2FC42E90395B554CBF3B950071AF2)

## 云空间同步数据

同一华为账号下通过云空间实现数据上云保存，用于多设备数据同步。

### 云空间多设备同步数据场景

登录华为账号后“云空间服务 ”中 智能填充开关默认开启，可以实现多设备同步历史表单输入数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/avPM94brS9itEk14g7Bbtg/zh-cn_image_0000002583479155.png?HW-CC-KV=V1&HW-CC-Date=20260427T235044Z&HW-CC-Expire=86400&HW-CC-Sign=EDEDCA73E5BB1F5E7A8E8F41DC085FACA2ADC24D9B32FD602C2D7E51A9BF044C)
