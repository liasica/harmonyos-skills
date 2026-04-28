---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis
title: ArkUI分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > ArkUI分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:31+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:db0d5a30b9402d2f7a705149d22e5bc4b39b4e519d75de110c12a01ba7d13102
---

ArkUI分析用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：

场景1：布局嵌套过多引起的性能问题；

场景2：数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；

场景3：父组件中的子组件重复绑定同一个状态变量进行更新；

场景4：未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝。

## ArkUI Component 泳道：查看组件绘制耗时

开发者通过ArkUI Component泳道可以直观感知组件绘制频率、耗时等统计情况。

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区Summary列表给出录制时段内定制组件以及系统组件的绘制统计情况，包括绘制次数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/g8Gp08VLSNieaRGRgnI3rg/zh-cn_image_0000002530912850.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=35C86E87E4B2C5847269FC654BC8A00DFAE4EF9DB38A7035BEB95E3758CB2B1F "点击放大")
3. 详情区Details列表可以查看按照时间线排序的组件详情，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/miW3bqeSQh2Ad3VL3rh-gw/zh-cn_image_0000002530752844.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=27814EAC76195D26BCE4DAF22249136818BA379CBF0956512B58D66F28B34106 "点击放大")
4. 点选ArkUI Component泳道中的条块，展示Slice Detail数据，Slice Detail中的Name支持跳转至对应Process子泳道并选中trace信息，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/U8eEAA9iRBSUtlJoCJCWOA/zh-cn_image_0000002530912840.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=8B43295AF592D62871943BEA017DF2111FBBF3C748F58452EA02966763EE6E9A "点击放大")

   说明

   由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

## ArkUI State 泳道分析

1. 点击ArkUI模板创建session并启动录制，录制过程中触发组件刷新。
2. 录制结束等待处理数据完成。点击ArkUI State泳道，可在下方数据区查看录制过程中发生的状态变量变化。Summary区域可查看状态变量名称，变化次数，状态变量类型、所属组件和所属类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/g99t72PQTGeJ1xLApnGnAA/zh-cn_image_0000002530912844.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=F41E02F081937CFABDE4DA199876784B8AD1160C234F29EF955E67591FC6B925 "点击放大")

   Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/-JT4h5M-Qc22-ph_y8uqBA/zh-cn_image_0000002561752783.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=524080183199AC47435D8A776D942D0EFCCE257036E05DC0CB5237E87B5E4B45 "点击放大")
3. 选择Current Value中某一个数据，泳道区域将以虚线展示其时间位置。同时，右侧More区域展示该状态变量影响的组件关联关系。打开页面下方的**Delivery Chain**开关，该状态变量影响的组件关联关系将以图形展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/BLoWpHHkS-efwHsDrTrTsw/zh-cn_image_0000002530912846.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=6D2FB3217430374322539A2A6C1C51CF6D3F41B4E23714FEE3227C60843C4E87 "点击放大")
4. 定位到可能造成卡顿的状态变量变化时间点，框选对应时间段，选择ArkUI Component泳道查看对应组件刷新时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/-ZtAl0J4TnSROjlmHMkuzg/zh-cn_image_0000002561832767.png?HW-CC-KV=V1&HW-CC-Date=20260427T235730Z&HW-CC-Expire=86400&HW-CC-Sign=8D6B514D3735BEB52D0FA7BD40ECBE66485CA3BACFBE07505A920A651F419E86 "点击放大")

说明

* 如需查看其他泳道信息，请参考[Frame分析](ide-insight-session-frame.md)。
* 由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
