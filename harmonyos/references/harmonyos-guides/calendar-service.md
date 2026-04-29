---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendar-service
title: 注册并管理一键服务日程
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 注册并管理一键服务日程
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0d50bfc998aba2f8ea401ac25c192b6ee7f0b8f1239fac0b532b20b883f6aae
---

## 场景介绍

Calendar Kit提供日程一键服务功能，比如一键入会、一键追剧、一键购物、一键查看等。注册日程一键服务后，用户可通过点击对应按钮拉起跳转链接，一步直达服务落地页，方便快捷。

## 服务器注册（配置一键服务跳转链接）

若需使用“日程一键服务”功能，需要按照以下步骤完成注册。

1. 进入[开发者管理中心](https://developer.huawei.com/consumer/cn/console/overview)，登录[企业账号](store-attribution-config-agc.md)（暂不支持个人开发者）。企业主账号无需手动添加权限；若使用团队成员账号，请确保使用企业主账号为其添加“小艺开放平台”的管理员权限，具体添加可见下图。

   选择团队账号，点击编辑，为对应的账号添加权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/zD1DFdLUSEyqLFP4nCZdRA/zh-cn_image_0000002558605658.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=F31AA24A9C364EF7510D7A1F0C9DE671AE721AA32846A02B881920F9A3B06CED)

   确认对应的信息后，点击下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/fOyJCEAMSvChZ7dekDty0g/zh-cn_image_0000002589325185.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=D86BDC4059F39AF657B73ED3D8A3D30FBAA32B04FD452CF7EB63991446AF98ED)

   勾选小艺开放平台管理员，选择下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Yf_y4EYsQQy63uKP_6zj4w/zh-cn_image_0000002589245121.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=20839E371908E4A5BC974140177BC72944ADFF572461FD36418934969124F565)
2. 登录成功后，在侧边栏菜单中**生态服务**下选择**智慧服务**，点击进入**小艺开放平台**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/zNFO3TQjTXWif0R50vWIsg/zh-cn_image_0000002558765316.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=E75AA4415A35DF594A4A2F9488226D98F3F0FC6D47C7126D15CD17B243BBB210)
3. 进入页面后，选择右侧**资源管理**，点击选择**其他服务**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/akIIQc_4RGe5UkLm2r9l7A/zh-cn_image_0000002558605660.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=6A69B6070B068A06F6C30DFB5F73BBB69B5329E3B3076FFB8ECE59F571A6950E)
4. 进入页面后，点击右侧**创建服务**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/_Ri4kq1OSsKctBOkJ8twuQ/zh-cn_image_0000002589325187.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=F381BA3D70157F3703523A5E420041FB7EDAFE81192978C73F5D0A53EF20F0A3)
5. 选择服务模型。

   选择**自定义模型**，填写**服务名称**、**服务分类**、**默认语言**，点击**创建**按钮。

   **服务名称**：可由用户自定义，推荐使用“应用名+日历一键服务”的组合命名形式。

   **服务分类**：开发者根据实际业务类型自行选择。

   **默认语言**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Rc1QXGKJTUKyEMI95eNkCw/zh-cn_image_0000002589245123.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=AB78A66108A3E32B9B929488C3B58E614D06D6F9190D52D83F83F99118287EB0)
6. 创建完成后，填写服务的**基本信息**，点击**保存**按钮。

   **服务分类**：选择实用工具/日历。

   **服务版本号**和**版本描述**可由开发者自定义，平台审核不关注此信息。

   **服务分级**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/TTYQmd-OQ9ejSNRJmFhVRw/zh-cn_image_0000002558765318.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=F813983C46F4D32D6DCF31A1FE9D33C8805D2B2C86AF4AE54513C8719AE0EE88)
7. 填写**服务呈现信息**，点击**保存**按钮。

   此页面必填字段均由开发者根据业务选择配置。建议在服务预览处上传用户界面示意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qZRG85RySFaNtQVUzmifIQ/zh-cn_image_0000002558605662.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=5B9035DDF0C86C5C3E797D2149B24279D2F02551DADE9D08B4AD0E752B57E7E6)
8. 进入**配置**，选择**新增用户意图**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/NPytmvSsRk-mnXJm1S7ZAQ/zh-cn_image_0000002589325189.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=832318A68447E5AAC859918DF7EE16A31933FBCA07034CF7A9F0C43ADB84DD74)
9. 配置意图。

   1. 设置**意图标识**、**意图名称**和**意图分类**，勾选一键服务。意图分类选择“查日历”。
   2. 勾选一键服务之后，选择**服务类型**（请与Calendar Kit提供的日程服务类型[ServiceType](../harmonyos-references/js-apis-calendarmanager.md#servicetype)一致），点击**添加关联**按钮，输入**app包名**及**app名称**（请确保app包名及app名称准确匹配，否则一键服务无法生效）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/HX_3Nuo3QBuJIJ_faK7OwA/zh-cn_image_0000002589245125.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=C746F98F9A7AB37A815E8F36F0B4DD1ACC4C563FB1840D4FDD0F536CBA6FCE0A)
10. 配置意图的**实现类型**，选择**APK/RPK/FA/H5 link**，选择**新增实现**，点击**配置**按钮。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/tXXvPOs8QGmQrfL4DDLQyA/zh-cn_image_0000002558765320.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=FF30528C8737F0DC413F426C900E971F11E4FB082D2A019769A39C68D2C71926)
11. 进入新增实现页面，填写**基本信息**和**配置方式**后，选择**保存**。

    1. 填写基本信息。实现名称由开发者根据业务自定义，推荐使用“应用名+一键服务类型”命名。
    2. 选择配置方式，勾选**HAP LINK**。

       填写准确的**App名称**（若下拉菜单中无匹配项，可直接输入）和**App包名**。

       填写**跳转链接**，即用户在系统日历中点击一键服务按钮拉起的落地页；请勿打开**跳转参数**开关。

       说明

       跳转链接为链接模板，实际[EventService](../harmonyos-references/js-apis-calendarmanager.md#eventservice)填入的uri需遵循此模板。例如，若填写跳转链接为“demo://mobile/player?params=”，则对应可匹配的uri为“demo://mobile/player?params=AAAABBBBCCCCDDDD”，其中“=”及“=”之前的部分为强校验，“=”之后的部分可由业务方根据需要自定义。

       其他必填字段，由开发者根据业务自行配置。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/y_XU4c0FTze6s3VFmGpUqQ/zh-cn_image_0000002558605664.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=9CC168ECD647A64D512D8245A9D4524F4BBA83C1EB39B3CBF123963B5188BA6E)

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/PGeautyiStqQzEBhZb1VXg/zh-cn_image_0000002589325191.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=204E342002893EA6DF00DFABF0254818E7552B6E4296B9074E21426C4A1C3AFC)
12. 完成以上所有配置后，切换到**发布**模块，点击**上架**按钮，等待后台审核后，完成意图发布。

说明

若已完成上架的服务，支持根据上文步骤再次调整修改，修改完成后，点击**升级**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/xe9J1sCcQJCk3z8wGOsOOA/zh-cn_image_0000002589245127.png?HW-CC-KV=V1&HW-CC-Date=20260429T053733Z&HW-CC-Expire=86400&HW-CC-Sign=B4CB98EE99AAA23BDB6FECEC3F1FC64DC37ADB4ADB541429D31A965EA1A76D60)

## 客户端添加一键服务日程

一键服务注册成功后，即完成系统日历跳转链接配置（支持在系统日历界面显示对应功能按钮）；若想实现一键服务体验，还需在客户端进行相关配置。

配置步骤如下：

1. 在module.json5文件中，配置相关字段。

   需配置"exported"字段为true。

   并配置["skills"](module-configuration-file.md#skills标签)中的"actions"字段，"actions"标识能够接收的Action值集合，取值通常为系统预定义的action值，也允许自定义。actions不能为空，actions为空会造成目标方匹配失败，常见的action取值可见[action常数说明](../harmonyos-references/js-apis-ability-wantconstant.md#action)。

   最后配置"uris"字段，"uris"需与注册时的链接模板相匹配。

   比如，服务器端注册时填写的uri模板链接若为"demo://mobile/player?params="，则“=”前的内容为强校验，“=”后的内容为**业务需要使用的参数列表**，可在使用日历服务写入日程时根据各业务实际情况进行指定。参数列表中不得直接包含字符“=”或“&”，请注意使用decodeURI()/encodeURI()进行转换。

   ```
   1. {
   2. "module": {
   3. "name": "xxx",
   4. "type": "xxx",
   5. // ...
   6. "abilities": [
   7. {
   8. "name": "xxxxxxx",
   9. // ...
   10. "exported": true,
   11. "skills": [
   12. {
   13. // ...
   14. "actions": [
   15. "ohos.want.action.viewData"
   16. ],
   17. "uris": [
   18. {
   19. "scheme":"demo",
   20. "host":"mobile",
   21. "pathStartWith": "player"
   22. }
   23. ],
   24. }
   25. ]
   26. }
   27. ],
   28. }
   29. }
   ```
2. 在被拉起的落地页EntryAbility中的onCreate、onNewWant接口中的[want对象](../harmonyos-references/js-apis-app-ability-want.md)内存在对应的拉起信息，开发者可通过对应参数实现对应跳转逻辑，本文不再赘述。
3. 调用[addEvent](../harmonyos-references/js-apis-calendarmanager.md#addevent)接口添加日程数据，后续即可见日历内出现含一键服务按钮的日程，点击即可跳转至对应落地页。

## 约束限制

* 普通日程（EventType.NORMAL）可以提供一键服务按钮的露出；重要日程（EventType.IMPORTANT）因数据结构和产品规格限制，即使配置正确也无法提供一键服务。
* 该服务仅在用户设备联网下载对应协议后，开发者写入的日程才会显示对应按钮。
* 一键服务按钮的展示规则为：日程详情内始终展示，月视图、桌面卡片在日程开始前15分钟展示。
* 在服务器端注册的服务协议完成上架，审核通过后，设备恢复出厂设置，或待当天零点后，功能可正式生效。
* 请确保服务器端填写的链接模版（[服务器注册（配置一键服务跳转链接）](calendar-service.md#服务器注册配置一键服务跳转链接)）、设备端三方应用侧写入的Event.Service.uri、module.json5配置的"uris"字段信息（[客户端添加一键服务日程](calendar-service.md#客户端添加一键服务日程)）相互匹配。
