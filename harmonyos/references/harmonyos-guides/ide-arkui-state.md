---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state
title: 查看ArkUI状态变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > 查看ArkUI状态变量
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c72fdc0719d94d2f5846a4ac9f3a9b938559e8d604afe354db95221467c3db3
---

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Tl3PNEZdQcG76FB3ooczcg/zh-cn_image_0000002561832669.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=5F9248E3BFC631710A141164383CE17132E28437FEE3956F71A115AC7496AF05)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/yfD3-foXRHmn8dm5QfAfGA/zh-cn_image_0000002561752693.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=B75988FA0E3C58C75230BDEDC5815EBCCC98DB93788533CB75F2D4970B1B568D)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

* 总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/etPRHfNLRJ2YupEJP0a8cA/zh-cn_image_0000002530912750.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=F3E74CA00BD0F2478586A44C06BF83B835BCCF95A74119F3DA09A469D86CA640)
* 当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/4T4dRmGITMGO7ZTqJOuPGw/zh-cn_image_0000002530752746.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=0F4A5D1792EF222F1F21D95AADEB42FC1E3AEE161E179F07E5A341D21250ADA0)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/GGldNu4qSrGGjP59pJXcPg/zh-cn_image_0000002561752689.png?HW-CC-KV=V1&HW-CC-Date=20260429T054647Z&HW-CC-Expire=86400&HW-CC-Sign=908652E923C96F16B36077794A02AB4A4046B625B8617D8A6929592D624AB959)

说明

* 打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
* 同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
