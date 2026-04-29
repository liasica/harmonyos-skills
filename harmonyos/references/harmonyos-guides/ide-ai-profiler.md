---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler
title: 智慧调优
breadcrumb: 指南 > 使用AI智能辅助编程 > 智慧调优
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:12+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:084fdddb4fd79e721585ab739d6fa4cc20ed58f04cf929a040d1033395e6941f
---

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄露次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

## 操作步骤

1. 首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

   **方式一：**若Launch、Frame、Allocation、Snapshot模板已录制完成，点击**Session**窗口中该条会话上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/qHD3gK8VRWu8rBFuuNPEGA/zh-cn_image_0000002561832823.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=0C139000EE7CD697AE1493A07F1BA2A3ADD6B90EB8C0709964E6ABF7FF96A3CF "点击放大")图标，即可开始智慧调优分析。录制方法具体请参考[性能问题定位：深度录制](deep-recording.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/dQkmczfsRI2NK7yAmv085w/zh-cn_image_0000002561832825.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=7F814AF769370F8F1CA1D02EA1429198644997DE8130E7BF0CAADB4EF5E47DF1)

   **方式二：**切换至**Assistant**窗口，点击**Create Session**开始录制调优任务；或点击**Open File**按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/YghRh9TVQ9uDdkjnth1Yfw/zh-cn_image_0000002561752851.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=5700CB812E6C1D6CBE376380AE7F3BF1736ED65C395290062C42D7E3EA89C2CD)
2. 对于方式二，在**Assistant**页面，点击**Create Session**按钮，从**Launch**、**Frame**、**Snapshot**、**Allocation**中选择一个分析模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/FCKMECtqSvGf4mwJbabSJg/zh-cn_image_0000002561832833.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=5BAC173F728BC998D5079C37EA0A8FB03578030E68027C2008149263483087BA)

   说明

   使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/c7ifib-yStSJ630BRrQLsg/zh-cn_image_0000002530752910.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=50E99B4980BFAE11BDDB4A91379D4F16DE45755B4A41A38628E7218CB74C6C57)
3. 以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/K9WXqDgATRafOzQ1I-y_Qg/zh-cn_image_0000002561752843.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=AB42319B35E7D9E08F5268421957415C468C7FBFDF9B0757CF067985001698CB)
4. 等待AI完成初步分析。左键点击高亮的泳道名称，点击**Analyze**进一步分析该阶段的具体内存信息，点击**View Lane**在右侧查看具体的泳道信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/dvnPOf_HSw-4LxKugYRL8A/zh-cn_image_0000002530912904.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=5251FF1766599F47AB92B25885EC5BDBFE9F4DE969B71FEC5B51475B9EEA75D9)
5. 点击**Analyze**后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iOKw59IgTq-mPRm2ogI2QQ/zh-cn_image_0000002561752855.png?HW-CC-KV=V1&HW-CC-Date=20260429T054511Z&HW-CC-Expire=86400&HW-CC-Sign=DE7DC4F5BB7585EB068536490258AC584623ECA3627CB8E906977AE4B93B80A2)
