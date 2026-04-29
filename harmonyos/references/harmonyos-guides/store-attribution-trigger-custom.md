---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:86c1feda52d7820ee5cf97127d771d3888b8e885bae4092c70d274e997669bf2
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/UXlCyNYfR0yA5oMKS0htnA/zh-cn_image_0000002558765284.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=23F60BBD6528EF5FF01FE881EB7E85D6A962A089CC485AAC10B2C7FC907ADD08)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/I8OEQlRLS_iSkxJM58-mFg/zh-cn_image_0000002558605628.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=1DAA0A7164A916B595B4FA3C1B2A4CFD6EC151C17FC22F043091424954C5F9DE)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/UjkyW_OhRGqoVcgs2e2l0g/zh-cn_image_0000002589325155.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=8784E3D6AA5FF885D28D5277AD0044507FC0B8C7A920EF3E0EB0AD40E85A75A1)

说明

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/1UQaBDueR1aWwSDsSLy2eA/zh-cn_image_0000002589245091.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=D9098388606B6AAE9F009E653679DC4897998B4B3E78101C989A581F0FA8C744)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/8tCIfQM0SVC_LSqrIhLeAg/zh-cn_image_0000002558765286.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=CC639E5B0C3E77D4B904AB4D6DD9246F8F3155679AA9F5B48CF357504AC665BC)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/keWhz_ytTZyVX0ieM_hv-g/zh-cn_image_0000002558605630.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=D82EFDB23EBBA0DEE5CEB809D8B8AFA8DE6226D288D08BB0D84FB2D2280B767D)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

说明

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/NOQL2ucOQi25a-ErjZkYiA/zh-cn_image_0000002589325157.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=1F28989DCD6F2E29645D0B5BE4000C27CA1407CF994F196AB0C797C376E4E032)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/M-UFwHiLSp2P7KkZsIV0Wg/zh-cn_image_0000002589245093.png?HW-CC-KV=V1&HW-CC-Date=20260429T053712Z&HW-CC-Expire=86400&HW-CC-Sign=2E5CF0AAACCA3069BDDF0177B3CA6247A854E463F7EFE3BBD97E3C8C69DEC2B3)
