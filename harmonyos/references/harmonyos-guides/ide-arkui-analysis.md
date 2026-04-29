---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis
title: ArkUI分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > ArkUI分析
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:32+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:4c7312724f3ecf05507d4013c52bf621ec16f968ef1485981c35404d674b1536
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/hBmo4hoaQkiCw3Xth0VVdw/zh-cn_image_0000002530912850.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=917E4952B72E72D7258F12DCAB74C6EC14818BF59AE61CD26A2C9A86FA9325A3 "点击放大")
3. 详情区Details列表可以查看按照时间线排序的组件详情，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/vZMw-iQLQSKRk0cTruX-Ew/zh-cn_image_0000002530752844.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=C9C6685C915EEC05F2506ED4EA43ABF506B2565D8B139E03B56A5F721908366A "点击放大")
4. 点选ArkUI Component泳道中的条块，展示Slice Detail数据，Slice Detail中的Name支持跳转至对应Process子泳道并选中trace信息，同时more区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Utv88_7FSx2fjq3FzTGrIQ/zh-cn_image_0000002530912840.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=18B23656C23DAF8D3AC80B85C485D38B7904D87D0E732B56A35F938027020BD3 "点击放大")

   说明

   由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

## ArkUI State 泳道分析

1. 点击ArkUI模板创建session并启动录制，录制过程中触发组件刷新。
2. 录制结束等待处理数据完成。点击ArkUI State泳道，可在下方数据区查看录制过程中发生的状态变量变化。Summary区域可查看状态变量名称，变化次数，状态变量类型、所属组件和所属类。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/gU2-gqhHTCu2V2q2gtQMwQ/zh-cn_image_0000002530912844.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=46D72C60F4574BB5C56AD336A63BE81EEF15F9DE4ABCB65B0428816221522CCA "点击放大")

   Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/bR72-UdMTguDq8Us5iP9Nw/zh-cn_image_0000002561752783.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=3B8816CCCB75F4C6851243ACC49A864B8589162DF468264AF2C28501EF989A61 "点击放大")
3. 选择Current Value中某一个数据，泳道区域将以虚线展示其时间位置。同时，右侧More区域展示该状态变量影响的组件关联关系。打开页面下方的**Delivery Chain**开关，该状态变量影响的组件关联关系将以图形展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/VDZfDdWLSkmOZUQVj9imyw/zh-cn_image_0000002530912846.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=69647E3653A50AC7624BF1AA8CDFE0E15F817BAD8472659A8BEE14C61660D1E6 "点击放大")
4. 定位到可能造成卡顿的状态变量变化时间点，框选对应时间段，选择ArkUI Component泳道查看对应组件刷新时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/K9i_CkkzR1aY0ekOzosqng/zh-cn_image_0000002561832767.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=59E1B63583992FC7CBD601BA8E558F417BCED75E42C19CA5E1E4D00D523028FF "点击放大")

说明

* 如需查看其他泳道信息，请参考[Frame分析](ide-insight-session-frame.md)。
* 由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
