---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-trigger-custom
title: 自定义转化事件
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理转化事件 > 自定义转化事件
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec2a12edef9b9b3aac8a3caec977e5e0007895911814f36a96915ecfbd3e024e
---

**开发者角色的合作伙伴在转化事件管理页面可以做如下操作**：

新增、修改、删除、查看自定义转化事件。

新增、修改、删除自定义转化事件时，相应的操作会被运营人员在后台审核通过或驳回，仅被审核通过的自定义转化事件才能生效。

## 新增

1. 在左侧点击转化事件管理菜单栏，进入自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/2utX1kwtT8aejGBTN4-tjQ/zh-cn_image_0000002786520104.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9361D4D4F2B3088915976E656A96497660728A68F033B89115B60D5AFEE63B0)
2. 点击右上角“新增”按钮，进入新增自定义转化事件页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/VNCPFGS2TPWzRmnJgzotzQ/zh-cn_image_0000002786360176.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A15E911AB5194FC207B0AB09EB0018E3294BE9132B814D1A3FB33888A13DFEC)
3. 填写“转化事件名称”、“转化事件编码”、“含义说明”信息，点击“确认”按钮后会生成一条状态是“新建待审核”的自定义转化事件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/YznnOG5ISd6VGVQXBuZhIA/zh-cn_image_0000002815559597.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=378AB5B8CA57C9F6EC65413A4C937AB4E168833E06BC6B0F3783D1C81744FD36)

**说明** 

* 转化事件编码范围只能为[501, 600]。
* 转化事件名称或转化事件编码不能重复。

## 修改

1. 点击处于已生效或者驳回状态的自定义转化事件列表右侧“编辑”按钮：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/836K5FeUQWqwILNSu0__fg/zh-cn_image_0000002815399681.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A75DC62D4070E5AC59E2CBFA6BEC66D303A2DF7C8669A9810EA38715B6AEBE4C)
2. 进入编辑页面，修改“转化事件名称”、“转化事件编码”、“含义说明”信息后点击“确认”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/iTxiZzjlQoar9srWicjSnQ/zh-cn_image_0000002786520106.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0C5ABD57903BEA062725CFF23552E467D583880719E3E8C9B9FF2362EABCEEE)
3. 修改后的数据状态为“修改待审核”或者“新建待审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/guhEv8oYROKTtpC49Ly8lg/zh-cn_image_0000002786360178.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D13C959A69AFF22FEC63B6958FF0D96DFB814701AA0FE354AB56E90A23C8605D)

“修改待审核”状态的自定义转化事件被审核通过后才能生效，如果被驳回，则维持修改之前的转化事件名称和转化事件编码值。

**说明** 

* 修改后的转化事件名称或转化事件编码不能与已生效或者审核中的转化事件名称或转化事件编码重复。
* 对驳回状态的自定义转化事件进行编辑修改，修改后的状态为“新建待审核”。

## 删除

点击列表右侧的“删除”按钮，并在弹出框中点击“确认”。

状态为“已驳回”的自定义转化事件可以直接删除。

状态为“生效”的自定义转化事件，点击“确认”后该条自定义转化事件的状态由“生效”变为“删除待审核”。

删除待审核的自定义转化事件需要审核人员审核通过后，才会被删除。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/Zw_XtGojSsOSNaqjm1IBjw/zh-cn_image_0000002815559599.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7253F93C3D8B76AC9F5799FE1D4A9DF8DB6B308754851311CD3532CD156058F7)

## 查看

点击左侧转化事件管理菜单栏，进入自定义转化事件页面查看自定义转化事件信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/PWMZRzLRRqqOs_uZOlniBg/zh-cn_image_0000002815399683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233236Z&HW-CC-Expire=31536000000&HW-CC-Sign=29DBDF937A10922638FF077241A90EC6AC05C0A239EB69C50D1E0639986D51D7)
