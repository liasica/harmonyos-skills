---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/calendar-service
title: 注册并管理一键服务日程
breadcrumb: 指南 > 应用服务 > Calendar Kit（日历服务） > 注册并管理一键服务日程
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b9c21f41f5235121406096e472607c0ca04692adbdd4017824be80a82ad0c5d
---

## 场景介绍

Calendar Kit提供日程一键服务功能，比如一键入会、一键追剧、一键购物、一键查看等。注册日程一键服务后，用户可通过点击对应按钮拉起跳转链接，一步直达服务落地页，方便快捷。

## 服务器注册（配置一键服务跳转链接）

若需使用“日程一键服务”功能，需要按照以下步骤完成注册。

1. 进入[开发者管理中心](https://developer.huawei.com/consumer/cn/console/overview)，登录[企业账号](store-attribution-config-agc.md)（暂不支持个人开发者）。企业主账号无需手动添加权限；若使用团队成员账号，请确保使用企业主账号为其添加“小艺开放平台”的管理员权限，具体添加可见下图。

   选择团队账号，点击编辑，为对应的账号添加权限。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0RnFrtyISBiWnqEMo0mj3A/zh-cn_image_0000002583478815.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=0B60915A0A6406B0CE35744C850117F4F6FB6D515BFE4F95BC058374D28E602C)

   确认对应的信息后，点击下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/qL_zLU6TTwKcQyHKTyGT9A/zh-cn_image_0000002552799166.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=5515E29552F0A3732F44EE31898E3A4214F10F754AAA83F9E3BF050DA440FFD5)

   勾选小艺开放平台管理员，选择下一步。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/cPuHwlA-QXm-c81R8KY_Wg/zh-cn_image_0000002583438861.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=7B8F06D8F34B64A89F3AC93D1FD4820595FA96C9A9C9BAA6E89A2A51630D9058)
2. 登录成功后，在侧边栏菜单中**生态服务**下选择**智慧服务**，点击进入**小艺开放平台**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ixPQmrvvQbqwyUgrEhk1PQ/zh-cn_image_0000002552958816.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=FB416F8173CAC75862168E4B884223914C0EAE338555BBE2D6E59152C502809E)
3. 进入页面后，选择右侧**资源管理**，点击选择**其他服务**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Br5BBJe3QxyMQBNCgFLCUQ/zh-cn_image_0000002583478817.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=51C9EC18927D11633FD4F1A8FBA2ECC44F2C2F5BF8B6D938EED9C5E09C881D20)
4. 进入页面后，点击右侧**创建服务**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/O-P-uPZWT--OtExS4U9wOw/zh-cn_image_0000002552799168.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=12775DCA063FDD30F3801D5D781D40B2706A10F0EED7DA66C3F1E0BED0198232)
5. 选择服务模型。

   选择**自定义模型**，填写**服务名称**、**服务分类**、**默认语言**，点击**创建**按钮。

   **服务名称**：可由用户自定义，推荐使用“应用名+日历一键服务”的组合命名形式。

   **服务分类**：开发者根据实际业务类型自行选择。

   **默认语言**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Ca3m-gEcTlqdgZlNjSx2rQ/zh-cn_image_0000002583438863.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=211CCD1E460448930E50876AC7106D65C3C5FAD38AAFFF0A15DFCE22D0E34748)
6. 创建完成后，填写服务的**基本信息**，点击**保存**按钮。

   **服务分类**：选择实用工具/日历。

   **服务版本号**和**版本描述**可由开发者自定义，平台审核不关注此信息。

   **服务分级**：由开发者根据业务选择配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/5n-0aJoqS0uMB65dxKMfpA/zh-cn_image_0000002552958818.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=78E99CFE7DDEA10B49EAA8EF2BC37CB45C3C0883E58E1CAEE09E5B7AA283F4E7)
7. 填写**服务呈现信息**，点击**保存**按钮。

   此页面必填字段均由开发者根据业务选择配置。建议在服务预览处上传用户界面示意图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Cre_ER5XRJ-ZGa1HQuaYsg/zh-cn_image_0000002583478819.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=6F6A81336C405972AF0180A83986A540CD7ECD6F83CBB0E558E2E75AC9F05F42)
8. 进入**配置**，选择**新增用户意图**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ERQI-d7FSb6yRspgoqex2g/zh-cn_image_0000002552799170.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=324EBCDC798EB8B434BAFD6DCE31B90FE10E9136CF411111D344528094CFA994)
9. 配置意图。

   1. 设置**意图标识**、**意图名称**和**意图分类**，勾选一键服务。意图分类选择“查日历”。
   2. 勾选一键服务之后，选择**服务类型**（请与Calendar Kit提供的日程服务类型[ServiceType](../harmonyos-references/js-apis-calendarmanager.md#servicetype)一致），点击**添加关联**按钮，输入**app包名**及**app名称**（请确保app包名及app名称准确匹配，否则一键服务无法生效）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/L9OWcM9uSDii8_D4IGTPbw/zh-cn_image_0000002583438865.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=07EFA845DEE3337BA3140C82BAC08792742376C60AA1831E3EEE1424DF9E7B7C)
10. 配置意图的**实现类型**，选择**APK/RPK/FA/H5 link**，选择**新增实现**，点击**配置**按钮。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/YtnFInJ8RmONoLh088F-uw/zh-cn_image_0000002552958820.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=672B1DE132099EE6C07D4B645F7371D1825D53B8C643251DD894D318853AA7DB)
11. 进入新增实现页面，填写**基本信息**和**配置方式**后，选择**保存**。

    1. 填写基本信息。实现名称由开发者根据业务自定义，推荐使用“应用名+一键服务类型”命名。
    2. 选择配置方式，勾选**HAP LINK**。

       填写准确的**App名称**（若下拉菜单中无匹配项，可直接输入）和**App包名**。

       填写**跳转链接**，即用户在系统日历中点击一键服务按钮拉起的落地页；请勿打开**跳转参数**开关。

       说明

       跳转链接为链接模板，实际[EventService](../harmonyos-references/js-apis-calendarmanager.md#eventservice)填入的uri需遵循此模板。例如，若填写跳转链接为“demo://mobile/player?params=”，则对应可匹配的uri为“demo://mobile/player?params=AAAABBBBCCCCDDDD”，其中“=”及“=”之前的部分为强校验，“=”之后的部分可由业务方根据需要自定义。

       其他必填字段，由开发者根据业务自行配置。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/BtiHWx7IRjSvxEi5UztJEQ/zh-cn_image_0000002583478821.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=73736EDA31C2E3377281161EED9E144286615AC86794C01FED86DC14D9A877BC)

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/h0cf4Hm3RtaHDychnbQTMA/zh-cn_image_0000002552799172.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=D00537C5E1481029734DF9CE140F795437BFD3756B16B564B1C29ED90700DE5B)
12. 完成以上所有配置后，切换到**发布**模块，点击**上架**按钮，等待后台审核后，完成意图发布。

说明

若已完成上架的服务，支持根据上文步骤再次调整修改，修改完成后，点击**升级**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/LDESyheYTESZlW0hZg40nQ/zh-cn_image_0000002583438867.png?HW-CC-KV=V1&HW-CC-Date=20260427T234832Z&HW-CC-Expire=86400&HW-CC-Sign=DDAF1FD773049951E61AA4C77326B62EDE2A67FBCA076A15727550B485A797F2)

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
