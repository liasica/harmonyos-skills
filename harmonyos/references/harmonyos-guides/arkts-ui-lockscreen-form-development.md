---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-lockscreen-form-development
title: ArkTS锁屏卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS锁屏卡片
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89ba8d86bd48482b31b9368f9a73a2dea9a0900b7ff741bbe03470fdd0330edc
---

从API version 18开始，Form Kit提供在设备锁屏界面上显示卡片的能力，用以展示重要信息或快捷操作，旨在让用户无需解锁即可获取关键资讯或执行常用功能。锁屏卡片常用于展示天气、时钟等内容，并支持用户个性化定制。

本文介绍了锁屏卡片的使用步骤、约束限制，并给出开发指导。

## 亮点/特征

* 应用信息浅层触达，不解锁即可查看，通过浅层信息持续获得用户关注，吸引用户复访。
* 应用快捷功能一键直达，提供更便捷的访问路径，提升操作效率。

## 使用步骤

锁屏卡片除了在锁屏界面显示卡片，还支持添加、删除、移动卡片，具体操作步骤如下。

1. 进入锁屏编辑态：在设备锁屏界面双手捏合手势进入锁屏编辑态，出现4个卡片添加位。 锁屏卡片只支持1\*1、1\*2尺寸的卡片，1\*1尺寸卡片对应1个卡片添加位，1\*2对应2个卡片添加位。
2. 进入锁屏卡片管理页面：点击卡片添加位会弹出锁屏卡片管理页面。
3. 添加卡片：在锁屏卡片管理页面选择任一卡片，例如运动健康和时钟，卡片就会添加到锁屏上。
4. 删除卡片：在锁屏编辑态，点击卡片右上角的减号即可删除卡片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/4oYHSzZqRoiX8Rv8cXIBXA/zh-cn_image_0000002742003351.png)

## 约束和限制

* 设备限制：仅手机、平板设备支持使用。
* 界面限制：

1. 锁屏卡片只支持 1\*1、1\*2尺寸的卡片。
2. 锁屏卡片不推荐展示涉及用户的隐私敏感数据，具体界面约束请参考[卡片内容设计](../design-guides/system-features-service-widget-0000002087671904.md#section248mcpsimp)。

## 开发步骤

卡片创建完成后，需要完成锁屏卡片配置，并接入锁屏卡片开放能力，其他开发流程与普通卡片一致，具体步骤参考如下。

### 锁屏卡片配置

在form\_config.json配置文件中，锁屏卡片必须配置renderingMode和supportDimensions字段。其中renderingMode字段仅支持配置为“singleColor”或者“autoColor”，supportDimensions字段取值中必须包含"1\*1"或"1\*2"，具体参考[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)。renderingMode字段在API version 18版本后，配置方法有变动。

```ts
// 在API version 18及以上的版本，renderingMode的配置方法如下
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
      ]
    }
  ]
}
```

```ts
// 在API version 18之前的版本，renderingMode的配置方法如下。value值“0”表示“autoColor”，value值“1”代表“fullColor”，value值“2”代表“singleColor”
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
      "updateDuration": 1,
      "defaultDimension": "1*2",
      "supportDimensions": [
        "1*2",
        "2*2"
      ],
      "metadata": [
        {
          "name": "renderingMode",
          "value": "2"
        }
      ]
    }
  ]
}
```

### 锁屏卡片开放能力申请

因为锁屏卡片会展示在设备的锁屏界面，出于数据隐私安全考虑，需要开发者申请上架开放能力。

因此在应用调试或发布时，必须使用[手动签名](ide-signing-manual.md)，并在手动签名[申请Profile](../app/agc-help-debug-profile-0000002248181278.md)过程中[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)，创建应用时参考如下指导为应用接入开放能力。

1. 在“开放能力接入”页面，点击锁屏卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/8tXeOaipSBeqtngvND_sUg/zh-cn_image_0000002712404364.png)
2. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，不超过256个字符。上传附件：选填，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/7lk6baogTnengSoqvF976Q/zh-cn_image_0000002742123313.png)
3. 返回“开放能力接入”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EOtCewzlSEGDkS7itOYOmg/zh-cn_image_0000002712244400.png)
4. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/bwXi8ZFXTPSxrgaj3xVZdA/zh-cn_image_0000002742003353.png)
5. 能力申请通过后，勾选锁屏卡片的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/t4OgORc5SB-RpQ5M33xAGg/zh-cn_image_0000002712404366.png)
