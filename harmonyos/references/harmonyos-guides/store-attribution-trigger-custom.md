---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:16d9d58290ec87cf38337d30565fb23272f549b1f8b9adaec8a2a0db84ac3596
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/t3YtCdfAQsK_2Olnitpstg/zh-cn_image_0000002788307908.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=605B91AFF0FA94F68D24C1818F7218F002E2F5459BBA0264D3A0687F399F8994)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/cIvnuaq4Q_eMUl09aBfiMg/zh-cn_image_0000002817427271.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7512649BCFA68072B017D8BBD52058DECA8FCD0D696B8815B0ED126672805F6)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/bkLrEkJuSBWQO2UlglrInA/zh-cn_image_0000002788467852.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=281EF9446504B659CE3E2A60EDD564918CD65F2DD3B46C89BB97D29A31575A28)

**说明** 

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Klve6CL2QFiwgoe5DeZtCQ/zh-cn_image_0000002817507341.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=E019F00DCC5C9C37215F8FE03562F7D511BAA3B715039F83A242425F5E796939)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wVl2lqe5TBm0jVBADoYDKg/zh-cn_image_0000002788307910.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C8A06E6AC82E4E32C0BD3072753541E9374E99FD4DC93270C792D342661FEAD)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/IJ5DlRciSl-678GPIce8RQ/zh-cn_image_0000002817427273.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C0AFC263AFC9D592D61E179DD947A65C073D5FD727B27D252ACA426D26C2CEB)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

**说明** 

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/g0GUyna0Q6OY7FlZsJ1uIA/zh-cn_image_0000002788467854.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=48CCC9B0D356F07114976494C3D2B98E908C457F7426C41151DD43BD469897A1)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/a5D-8hlKTBe8-lUE5rHvWA/zh-cn_image_0000002817507343.png?HW-CC-KV=V1&HW-CC-Date=20261114T004812Z&HW-CC-Expire=31536000000&HW-CC-Sign=86592DF75F0165400F18D033361BD51CB1C815B470B36C53E8176C16888858D1)
