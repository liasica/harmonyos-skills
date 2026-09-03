---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis
title: ArkUI分析
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > ArkUI分析
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:14999035489a38843c9b6dba241c1d160b7af6f19bacc84264957b049c61a3ef
---

## 功能介绍

ArkUI模板用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：布局嵌套过多引起的性能问题；数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；父组件中的子组件重复绑定同一个状态变量进行更新；未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝等。

ArkUI模板支持的泳道包括：APP Frame、ArkUI Component、ArkUI State、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍ArkUI Component、ArkUI State泳道，其他泳道的详细信息请参考对应模板内容。

* APP Frame泳道的介绍请参考[Frame分析](ide-insight-session-frame.md)。
* ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* CPU Core、Process泳道的介绍请参考[CPU活动分析](ide-insight-session-cpu.md)。

**说明** 

任务分析前，需创建ArkUI分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看组件绘制耗时

开发者通过**ArkUI Component**泳道可以直观感知组件绘制频率、耗时等统计情况。

1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. **Summary**区域展示录制时段内自定义组件以及系统组件的绘制统计情况，包括绘制次数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/5T_PajfxSE-JHMWSOeM_fQ/zh-cn_image_0000002731541985.png "点击放大")
3. **Details**详情区域可以查看按照时间线排序的组件详情，同时**More**区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/XOB5Ydb4S-Ctq9KaGeso-w/zh-cn_image_0000002701662788.png "点击放大")
4. 点选ArkUI Component泳道中的条块，会打开**Slice Detail**区域，点击Slice Detail中的Name支持跳转至对应Process子泳道并选中trace信息，**More**区域展示以该组件为根节点的组件树信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/vX_wzUlnTtKHehBG6FQyag/zh-cn_image_0000002731382011.png "点击放大")

   **说明** 

   由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。

## 查看状态变量变化

1. 点击**ArkUI State**泳道，可在下方数据区查看录制过程中发生的状态变量变化。
   * **Summary**区域可查看状态变量名称、变化次数、状态变量类型、所属组件和所属类。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/H5Lgam44SPC42o3SxWQl1g/zh-cn_image_0000002701822712.png "点击放大")
   * **Current Value**区域以时间顺序展示状态变量变化，**Current Values**列展示变化后的值。选择**Current Value**中某一个数据，泳道区域将以虚线展示其时间位置，右侧**More**区域展示该状态变量影响的组件关联关系。打开页面下方的**Delivery Chain**开关，该状态变量影响的组件关联关系将以图形展示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/aJ_OBuvFSISt49MPGlLQlg/zh-cn_image_0000002731541989.png "点击放大")
2. 定位到可能造成卡顿的状态变量变化时间点，框选对应时间段，选择**ArkUI Component**泳道查看对应组件刷新时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Pyp5GokNRG6NhFEnB8eXSw/zh-cn_image_0000002731382015.png "点击放大")

**说明** 

* 由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
