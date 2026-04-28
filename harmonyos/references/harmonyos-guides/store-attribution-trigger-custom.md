---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a457105e0165c6ac58915791d16681dda6e5de969f080e58d4687159c439f226
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/bNPjbccUSOimoCAQ3yjDpQ/zh-cn_image_0000002552958784.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=F797F317F7D2E981C0667A9EA7F2AA023F580FB5E60F29153CE710B85896DAC1)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/YeOxDKc6TfegJQXga5RK_Q/zh-cn_image_0000002583478785.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=F180556F0CB95E4C8BB3DAE2264DCDC765D8A44D0BA13BBF131CAED7104EDD71)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Y2hgXcSzQF-kT1iCuiHs_w/zh-cn_image_0000002552799136.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=0B4DBD4A406FAF00FEA73B20F8B57B4138E1918BFEE8A68637129C104EC6877C)

说明

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/0KnTwIHLRkeGZvbbl3kFfQ/zh-cn_image_0000002583438831.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=2845EE6A994E617CE16C4ACCB2251305264597B4333EEC165422B22150D82EC1)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/TqyeM89QSnW3iWDIGdpbLA/zh-cn_image_0000002552958786.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=3302727FDAA0BA052AFD6FFDCEEE3F5FC8A16B22B25B22D0CEB5BFD908DED04E)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/PGMkt-GORqOtDYOi-SqFLg/zh-cn_image_0000002583478787.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=1FDB11AA872AEC9199294FE07178DF840FE5E1817FBBAA5AEC3138519FB9A912)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

说明

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/FbjVkW4bQ_ini2e-62AgPg/zh-cn_image_0000002552799138.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=948C86661DDE804ACA5CAA7582E5042404B2873210145C9C34084C57A52E047D)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/5QbJnfI9SWO2hghUKt8x9w/zh-cn_image_0000002583438833.png?HW-CC-KV=V1&HW-CC-Date=20260427T234819Z&HW-CC-Expire=86400&HW-CC-Sign=A090CB5051925D4BF82A833AED1E5CB80B78BFAFFB5887231B91F061A78C7730)
