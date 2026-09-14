---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler
title: 智慧调优
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 智慧调优
category: harmonyos-guides
scraped_at: 2026-09-15T07:03:57+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:75176d63ca29403bf5b2b8f5389f162317585a3a845937df1ada2641e16385f8
---

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄漏次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

## 操作步骤

1. 首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

   **方式一：**若Launch、Frame、Allocation、Snapshot模板已录制完成，点击**Session**窗口中该条会话上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/QLAOoUSoT8mdfS3M2t_4uA/zh-cn_image_0000002701662872.png "点击放大")图标，即可开始智慧调优分析。录制方法具体请参考[性能问题定位：深度录制](deep-recording.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/RylP0Ae1SPKnqdx3Q1p-cQ/zh-cn_image_0000002731382095.png)

   **方式二：**切换至**Assistant**窗口，点击**Create Session**开始录制调优任务；或点击**Open File**按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ehVAmzcWTd6d8v7qwD1gjA/zh-cn_image_0000002731382101.png)
2. 对于方式二，在**Assistant**页面，点击**Create Session**按钮，从**Launch**、**Frame**、**Snapshot**、**Allocation**中选择一个分析模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/rZmWmGqOTU2_CRewamcPdw/zh-cn_image_0000002701662878.png)

   使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/lEChDEOjTuCZahyoDmYzEQ/zh-cn_image_0000002731382097.png)
3. 以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/sbtZ_TRKQamh0j5_PK_VAA/zh-cn_image_0000002701822796.png)
4. 等待AI完成初步分析。左键点击高亮的泳道名称，点击**Analyze**进一步分析该阶段的具体内存信息，点击**View Lane**在右侧查看具体的泳道信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/27GzX5oyRzOq9y30hKJ1DA/zh-cn_image_0000002731542071.png)
5. 点击**Analyze**后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/PbvW4SBNRN-6dcFXczmSqw/zh-cn_image_0000002701822802.png)
