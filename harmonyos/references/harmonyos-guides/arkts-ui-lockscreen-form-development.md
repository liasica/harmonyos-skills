---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-lockscreen-form-development
title: 锁屏卡片开发指导
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS锁屏卡片 > 锁屏卡片开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:32+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f4709d9cf8e1f87d390a56573143bd95a311447fca76ccf3d72d395073a7990d
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/O7HaC_YeTn6rt-HOp1RH5A/zh-cn_image_0000002583478301.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=47FE8DE385E9A54F86F24E0F071268866CAD58736BC0D03D18D05564C47F804F)

## 约束和限制

* 设备限制：仅手机、平板设备支持使用。
* 界面限制：

1. 锁屏卡片只支持 1\*1、1\*2尺寸的卡片。
2. 锁屏卡片不推荐展示涉及用户的隐私敏感数据，具体界面约束请参考[卡片内容设计](../design-guides/system-features-service-widget-0000002087671904.md#section248mcpsimp)。

## 开发步骤

卡片创建完成后，需要完成锁屏卡片配置，并接入锁屏卡片开放能力，其他开发流程与普通卡片一致，具体步骤参考如下。

### 锁屏卡片配置

在form\_config.json配置文件中，锁屏卡片必须配置renderingMode和supportDimensions字段。其中renderingMode字段仅支持配置为“singleColor”或者“autoColor”，supportDimensions字段取值中必须包含"1\*1"或"1\*2"，具体参考[配置文件字段说明](arkts-ui-widget-configuration.md#配置文件字段说明)。renderingMode字段在API version 18版本后，配置方法有变动。

```
1. // 在API version 18及以上的版本，renderingMode的配置方法如下
2. // entry/src/main/resources/base/profile/form_config.json
3. {
4. "forms": [
5. {
6. "name": "widget",
7. "displayName": "$string:widget_display_name",
8. "description": "$string:widget_desc",
9. "src": "./ets/widget/pages/WidgetCard.ets",
10. "uiSyntax": "arkts",
11. "isDynamic": true,
12. "isDefault": true,
13. "updateEnabled": false,
14. "scheduledUpdateTime": "10:30",
15. "renderingMode": "autoColor",
16. "updateDuration": 1,
17. "defaultDimension": "1*2",
18. "supportDimensions": [
19. "1*2",
20. "2*2"
21. ]
22. }
23. ]
24. }
```

```
1. // 在API version 18之前的版本，renderingMode的配置方法如下。value值“0”表示“autoColor”，value值“1”代表“fullColor”，value值“2”代表“singleColor”
2. // entry/src/main/resources/base/profile/form_config.json
3. {
4. "forms": [
5. {
6. "name": "widget",
7. "displayName": "$string:widget_display_name",
8. "description": "$string:widget_desc",
9. "src": "./ets/widget/pages/WidgetCard.ets",
10. "uiSyntax": "arkts",
11. "isDynamic": true,
12. "isDefault": true,
13. "updateEnabled": false,
14. "scheduledUpdateTime": "10:30",
15. "updateDuration": 1,
16. "defaultDimension": "1*2",
17. "supportDimensions": [
18. "1*2",
19. "2*2"
20. ],
21. "metadata": [
22. {
23. "name": "renderingMode",
24. "value": "2"
25. }
26. ]
27. }
28. ]
29. }
```

### 锁屏卡片开放能力申请

因为锁屏卡片会展示在设备的锁屏界面，出于数据隐私安全考虑，需要开发者申请上架开放能力。

因此在应用调试或发布时，必须使用[手动签名](ide-signing.md#section297715173233)，并在手动签名[申请Profile](../app/agc-help-debug-profile-0000002248181278.md)过程中[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)，创建应用时参考如下指导为应用接入开放能力。

1. 在“开放能力接入”页面，点击锁屏卡片对应的申请按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/nwrjlrI6R3mD_GBDfuCs4w/zh-cn_image_0000002552798652.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=B717E13BFBC8F9AA960A8D6B2C69CCB03704F3B558F5E12EEA80FF09A9520328)
2. 在“新建业务申请”窗口填写申请信息，然后点击“提交”。申请原因：必填，不超过256个字符。上传附件：选填，仅可上传1个附件，大小不超过500MB。支持文本、表格、图片、视频、压缩包格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/3PPlNkqASweu15-Yo6lHlA/zh-cn_image_0000002583438347.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=10070CFC2851E26D47BFC7FD3FA6FBEEAE402BAB2346B94AD9A619A831FF8C94)
3. 返回“开放能力接入”页面，原“申请”按钮变为“申请中”，1-3个工作日反馈申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/SsLY45YWSLqa6nNDC2fpLg/zh-cn_image_0000002552958302.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=5F17E656501CE2928F12876C713C4A0EB6350D83C687BAFB37188BC081EE4257)
4. 申请审批通过后，互动中心会发送通知给您，同时“申请中”按钮会变为置灰显示的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/aEv0OchERrWr_3cObaBXmQ/zh-cn_image_0000002583478303.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=B4B2DBB63FB14433550D18D49E8F5D9469E86D255B0648FC6F7388E16E03713F)
5. 能力申请通过后，勾选锁屏卡片的能力开关，点击右上角“保存”。至此，您的应用已成功接入开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/PCcdowMUQjKdbQpb-kBQqw/zh-cn_image_0000002552798654.png?HW-CC-KV=V1&HW-CC-Date=20260427T234131Z&HW-CC-Expire=86400&HW-CC-Sign=EC57A41C079F4F6BE63B69A8942DC69E8EE22CBE37E118A52903C34BDA39C266)
