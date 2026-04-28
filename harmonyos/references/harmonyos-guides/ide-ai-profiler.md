---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler
title: 智慧调优
breadcrumb: 指南 > 使用AI智能辅助编程 > 智慧调优
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3715d822067c2089817cbd5e30ddd81638ebe7303306767945a86636fd366849
---

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄露次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

## 操作步骤

1. 首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

   **方式一：**若Launch、Frame、Allocation、Snapshot模板已录制完成，点击**Session**窗口中该条会话上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/8mwe71J1QQW8h8MsXFX7pA/zh-cn_image_0000002561832823.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=14B9E6316AC977C2FCA5AC45C61CC428D2E7A3CBC43AA2AF16A1B22B55305CAE "点击放大")图标，即可开始智慧调优分析。录制方法具体请参考[性能问题定位：深度录制](deep-recording.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/BOgGJfDGSyeg0i9SUfPMeg/zh-cn_image_0000002561832825.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=BDD4B9F17C293C3ECDC20DDD63DC066B175F931A3D2EA4DCB9773274266824B2)

   **方式二：**切换至**Assistant**窗口，点击**Create Session**开始录制调优任务；或点击**Open File**按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/4PCP0sQsTO26b8Ea_8vjTg/zh-cn_image_0000002561752851.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=13FDE731702F2EA9612092E741A389AB11244CBF6D0ECA82D3EF8F1241904586)
2. 对于方式二，在**Assistant**页面，点击**Create Session**按钮，从**Launch**、**Frame**、**Snapshot**、**Allocation**中选择一个分析模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/nW6k7joZSFeBDRUV_kq6vA/zh-cn_image_0000002561832833.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=63FEF6EAD70418A6ADD12B17179297E7D99488BD7E938DEC8DC081A77C2C6C95)

   说明

   使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/oVtkAYQpS4OmHZgNnW_UOg/zh-cn_image_0000002530752910.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=090AE1035D4318AD61A6C44480C088E9CC43A676E27BD928699537A63D8F72CE)
3. 以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/eCqFksAsTuSqV3bikaYHpA/zh-cn_image_0000002561752843.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=1230404D3AC6D165228C5FF6E0271910B052AC71CB73619B493DA8CF5CE14BE6)
4. 等待AI完成初步分析。左键点击高亮的泳道名称，点击**Analyze**进一步分析该阶段的具体内存信息，点击**View Lane**在右侧查看具体的泳道信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/G-KrK7wyQ-ui2i_hzm0XDQ/zh-cn_image_0000002530912904.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=C009B9C0F978DCAF0A1077385D30D03BC87F5A05294877996CE43E3F747C160B)
5. 点击**Analyze**后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/azu4PibwQuCce9KVmsX0HQ/zh-cn_image_0000002561752855.png?HW-CC-KV=V1&HW-CC-Date=20260427T235515Z&HW-CC-Expire=86400&HW-CC-Sign=6CD2DBB1EE3D2ECF5B2D18B7838B223C51C6BA0771B74D6F8456DF89907A2BCD)
