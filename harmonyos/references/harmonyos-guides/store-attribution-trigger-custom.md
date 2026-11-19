---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48ef71d8f7e938878d6b935937129b3faa2dfc12b30bf92f3823e83bb2a6773c
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/XyCenNZzSKamMZh4gYgXeA/zh-cn_image_0000002820406189.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9A908F998113EEE7F40D1A2B0787FC28CDA8F6EE93302A12B610017613D75A1)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/yXCuEwCFSc67jxAe0q-C_A/zh-cn_image_0000002791726210.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=979867A9C6088AB6AD4F8869B1F6F5B76370416A9F05A0FBA9904B2B218539F7)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/fJBxgpofR-aecd3bIQgkkw/zh-cn_image_0000002791566238.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=0937BC7A64FBBEC9A9CD419CAE06F739A551026EE83D9341CF2F2813E6E20A80)

**说明** 

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/tmoKgxlpTRO31pwTD-QKNg/zh-cn_image_0000002820526191.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F42CE0AE328FC8A34E84160A50CC4BF8249379BBA63786FA5D6BFC2D5704EC3)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ZSNmPs7pSPaZiLue_mvDBw/zh-cn_image_0000002820406191.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED0F5C6E96354729CF7C13DAE972C6A247110DB874C13EB4871055077DACC369)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/yVoK1blBQj6AZsLMYIfFTw/zh-cn_image_0000002791726212.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=98F0CAC75E0FBF876D03EA5E351480CBCDCC0C715BE65CAAECCDB36A2F3BB950)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

**说明** 

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/0ErLFzUdSoSXj1Oc-aJJcg/zh-cn_image_0000002791566240.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=581B7CEBDFE40EF829CB9790575181FE4A1123ED1BC669E400C264ECB01BC6AE)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/LiwnFQhhQwyLAZps3aXu_Q/zh-cn_image_0000002820526193.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0ADB4BA034134AD3E88D09493F43E82A2DC6BA1011A636590C9D4F008932F02)
