---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7210dd59a98031d5e14d11ef365643e270efd11592870f4b05e2cf43f67f8c95
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/vzSaypqRSnW-wgyCuRwxiA/zh-cn_image_0000002792877890.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BE5BC1D582AC5BF21B84CC72C94A939FF9C489F9AB0E57AEC1606B2EE3982D6)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fKu_ywKZTUC4hHn3Z7yq9w/zh-cn_image_0000002821837797.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=774A8CF26961C532F9F78F427E760B0C747DC49E643B164CB7AEE8AB56CA740D)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/M_LKCUqiRZaKRzwCm3qTPw/zh-cn_image_0000002821757799.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=094F9570D971826286CECBF36A3002AB6FA6592F07B9233E2307A99DBEC40978)

**说明** 

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/7sd_v7rqSGq2vCk5NS-Srg/zh-cn_image_0000002793037862.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=B89B1962C319DD7B10A198F5045998F5F86062DA2F77F63280D397EA6E8B2C1F)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/8eT0Cm7zQmKGqgNavELLvA/zh-cn_image_0000002792877892.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE9D8D4AF416D252174B03C860187FAA57CFB4F12B32055A5F7376B8C3C4C3AC)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NBXlnB0xSryHo5jAKUz0rg/zh-cn_image_0000002821837799.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD48AE414C51AFD06072AEE9378323336A8EA93BA0E0A2C5A4075A0165F5300B)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

**说明** 

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/8xWi6BklSQekgoieqTqLuA/zh-cn_image_0000002821757801.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDD20569859E978D8004ED71E3D6D103ACB62188CA2089B9DD04D596D2D1A21B)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/NaKDzuCYQXa7eJuEpPofzg/zh-cn_image_0000002793037864.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF68A90CAEE10EFDFC2759DBB076482821A40A3AE10D8DAF9DEAF41641672104)
