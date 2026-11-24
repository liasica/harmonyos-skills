---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler
title: 智慧调优
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智慧调优
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7c31735058a73a9b64bc288b97c695cbda863dc1706a1aa16fd78b51c1eb706c
---

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄漏次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

## 操作步骤

1. 首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

   **方式一：**若Launch、Frame、Allocation、Snapshot模板已录制完成，点击**Session**窗口中该条会话上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/mSkjjTYIQRWWX8gxUpkh2w/zh-cn_image_0000002779566690.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=4201362E74E3933037A69238BDF55302B8A4AA32C1CB6B26D5A78CF92AF54B1D "点击放大")图标，即可开始智慧调优分析。录制方法具体请参考[性能问题定位：深度录制](deep-recording.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Zwh5ttRgQtKi9aVXwuSk5g/zh-cn_image_0000002808766273.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=13923E216EB1C0A96792333A2D94CA2B8DBBECBCCB926A63B74F07185B0E7742)

   **方式二：**切换至**Assistant**窗口，点击**Create Session**开始录制调优任务；或点击**Open File**按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/v0rJ8WcMQ6uK0n1E084Wcg/zh-cn_image_0000002808766279.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=E72FB55D757B535D522044910FF6201865B4A848D8983F497209F7E1D9F080AC)
2. 对于方式二，在**Assistant**页面，点击**Create Session**按钮，从**Launch**、**Frame**、**Snapshot**、**Allocation**中选择一个分析模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/vlzbVMCaRNW_lARAMSNk-Q/zh-cn_image_0000002779566696.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=6ED0BF8A1993FE030953EE6DC45C8A455A22C3DC04DAEE85C74EBE07DBA9874A)

   使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Is5UFu60TkG-rWKmRno0Kw/zh-cn_image_0000002779566694.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CA95C0BDFBD850DE2A0A1015D02A653407564827DC080EA04898DB54D2F4655)
3. 以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/a-ezj8aDT1yDgEe4JYh1-Q/zh-cn_image_0000002779406714.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A151F7040D0E51EDEE3D15988DB6A62286B5B3296949C81953FED13B5E229A7)
4. 等待AI完成初步分析。左键点击高亮的泳道名称，点击**Analyze**进一步分析该阶段的具体内存信息，点击**View Lane**在右侧查看具体的泳道信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/S5SVQvCBTFGDi7mFeUSQcw/zh-cn_image_0000002779406718.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=093485C618C7C460E986713E0A4C37897AC649DE1211917B49F624DF52FD7849)
5. 点击**Analyze**后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ZyYu-_IoTSCfIvHT6qSZFg/zh-cn_image_0000002779406722.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC64E1172750EEF97A0BAE47A276A522300F3679EB9565AB288E22C54816F5AD)
