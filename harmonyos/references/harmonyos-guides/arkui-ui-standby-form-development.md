---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-ui-standby-form-development
title: ArkTS待机屏保卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS待机屏保卡片
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8f3b91f936f09e708eaa179ab975dad5dcb545eb5999bc0bb0ea89a82850294d
---

从API version 23开始，Form Kit提供在设备待机屏保界面（即横屏充电锁屏状态下显示的界面）上显示卡片的能力，用以展示重要信息，旨在待机下也可陪伴用户。待机屏保卡片用于展示天气、日历等信息，并支持用户个性化定制。

本文介绍了待机屏保卡片的使用步骤、约束限制，并给出开发指导。

**说明** 

在待机屏保界面下默认为深色模式不会跟随系统。

## 亮点/特征

* 丰富待机显示，提供个性美观的待机显示页面，打造全场景、个性化的“百变”心灵陪伴。
* 提供情感陪伴和情绪价值，在工作的时候，日程待办，提升工作效率；在学习的时候，作为时钟摆台，陪伴学习。

## 约束和限制

1. 待机屏保卡片只支持 2\*2尺寸的卡片。
2. 待机屏保卡片不推荐展示用户个人隐私敏感数据。
3. 待机屏保卡片有明确的UX设计规范。具体请参考设计指南中的[待机屏保](../design-guides/system-features-service-widget-0000002087671904.md#section966618274556)。
4. 待机屏保卡片只支持Phone中的部分机型。

## 开启方式

待机屏保功能在系统上默认是开启的，功能开关路径“设置>桌面和个性化>待机屏保设置”，开关界面如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/KF7_qCq_Sl-OrUWeziA67A/zh-cn_image_0000002821757163.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADC37FFDA933B62B85F0E32F6CFE8272C53A9A4872F5FC9C14543EC1A875B780 "点击放大")

## 使用步骤

待机屏保支持卡片展示与卡片编辑功能（添加、移除），具体操作步骤如下：

1. 进入待机屏保界面：插入充电器或开启“不充电可显示” 开关，设备横屏锁屏并与桌面夹角45°~90°稳定摆放（折叠机需切换为外屏；同时折叠机支持帐篷模式显示），即可进入待机屏保界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Bwh7FYbQSa6JZBt9eoVRjQ/zh-cn_image_0000002793037226.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=71E147738A4ED2EB75DDBC0E6C4FC1360E0573B0B0A9A92F4C2FC9365D6ADDED "点击放大")
2. 进入待机屏保编辑界面：在待机屏保界面长按或双指捏合即可进入编辑界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/FtEEcTWRRnSOQWu6ZzUIwg/zh-cn_image_0000002792877256.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=47FAEC193B908F5B66162C1B9DE38760B2C2C3C6B61838C92EBE59ABD580E3A7 "点击放大")
3. 进入待机屏保卡片中心界面：在待机屏保编辑界面，上滑左侧或右侧列表至最后，点击“+”弹出卡片管理页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/pxr1mEmuSNOXFePtfYCI-w/zh-cn_image_0000002821837163.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=116124F09EA33398FAC2E60D1376563B0B9745F8D4436311A9E9181CC62EE68D "点击放大")
4. 进入待机屏保卡片管理页面：在待机屏保卡片中心点击“建议”会显示推荐的卡片，或者点击应用列表中的应用，弹出对应的卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/DaNisrCpQPWrB3nfwg4FgA/zh-cn_image_0000002821757165.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=F55DD2FF802B80EF7CA2CF0BC00029F8F16B04EC1655FAE2D855F6FA6A82F935 "点击放大")
5. 添加卡片：在待机屏保卡片管理页面，选择好卡片后，点击“添加”按钮即可添加到待机屏保界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/I0MqymMcRVO7iERZlh_Bxg/zh-cn_image_0000002793037228.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C60F7A14B82FAD59EC5EC81E91D2A242CFD579EC1840328C4C688F3D761D170 "点击放大")
6. 移除卡片：进入待机屏保编辑界面，点击卡片右上角的“-”即可移除卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/kaMI731YT4mPDiJ9sZZYMQ/zh-cn_image_0000002792877258.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDF41168619453F7092A19B5CF8445ACD4A055E197712E6A048D66F836F93430 "点击放大")

## 开发准备

### 待机屏保开放能力申请

待机屏保卡片会展示在设备的待机屏保界面，开发者需申请上架开放能力，用以保护数据隐私安全。

因此在应用调试或发布时，必须使用[手动签名](ide-signing-manual.md)，并在手动签名[申请Profile](../app/agc-help-debug-profile-0000002248181278.md)过程中[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)，创建应用时参考如下指导为应用接入开放能力。

1. 登录AppGallery Connect，选择“开发与服务”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/V84zSAP4TwOgGYkC3kAWDA/zh-cn_image_0000002821757159.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BFA165A124B31E798751BC8C48806C6B4A886B9EF28D254B41CB28A3A208743 "点击放大")
2. 在项目列表中找到您的项目，并点击选择需开启开放能力的应用/元服务。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/DSb7HP2TSySw6_jzbh_X3A/zh-cn_image_0000002793037222.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=2802423505C59544EC56F962DCD67974A0C203EBDF45B008D33A857AB488AE23 "点击放大")
3. 在“开放能力管理”页面，点击待机屏保卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/RZ1UFi24SnyFJrCWJfGpDA/zh-cn_image_0000002821837165.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=64ED56F488854AD8E3CCCDFCD226F7DB4EB833AAB31ED631245FAEC1D38D2AFA "点击放大")
4. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。

   申请原因：必填，包括应用介绍、使用场景、申请用途，不超过512个字符。

   上传附件：选填，提供对应卡片UI设计释义材料，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/-m28OjsHSXmWY-9HfcHKLg/zh-cn_image_0000002821757167.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A979916ADC7B40BEBD910A8AC5D154A925C7BE8C8EAAE92EBEEAD950F03EFD7 "点击放大")
5. 返回“开放能力管理”页面，原“申请”按钮变为置灰显示的“申请”，待机屏保卡片的能力开关已勾选。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/UYgz_njdTie1hTOK6tFw_g/zh-cn_image_0000002793037230.png?HW-CC-KV=V1&HW-CC-Date=20261121T011123Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDFCC277978FE240EFFFF569DF8A207C61C9C4169FEC6AF6CEEDDB72360E4AD0 "点击放大")

   至此，您的应用已成功开通待机屏保开放能力。

## 开发步骤

下面给出示例，实现待机屏保卡片展示。

1. [创建卡片](arkts-ui-widget-creation.md)。
2. 配置卡片在待机屏保界面展示。

   如果卡片不需要展示在待机屏保界面，配置isSupported字段为false;如果卡片已适配待机屏保卡片UX规范，配置isAdapted字段为true，系统会把卡片布局组件中backgroundImage移除；如果卡片涉及隐私敏感信息，需要配置isPrivacySensitive字段为true，用户将卡片添加到待机屏保界面则会有蒙版覆盖。具体参考[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)。

```ts
  // entry/src/main/resources/base/profile/form_config.json
  {
    "forms": [
      {
        "name": "widget",
        "displayName": "$string:widget_display_name",
        "description": "$string:widget_desc",
        "src": "./ets/widget/pages/WidgetCard.ets",
        "uiSyntax": "arkts",
        "isDynamic": true,
        "isDefault": true,
        "updateEnabled": false,
        "scheduledUpdateTime": "10:30",
        "renderingMode": "autoColor",
        "updateDuration": 1,
        "defaultDimension": "1*2",
        "supportDimensions": [
          "1*2",
          "2*2"
        ],
        "standby": {
          "isSupported": true,
          "isAdapted": true,
          "isPrivacySensitive": false
        }
      }
    ]
  }
```
