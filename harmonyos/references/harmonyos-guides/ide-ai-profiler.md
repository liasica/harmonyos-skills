---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ai-profiler
title: 智慧调优
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智慧调优
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cd7d6e5e587788a5d458b9a181b9dc85a511f514eb0b30eb6fe007be820e5e1f
---

DevEco Studio的Profiler工具中已集成智慧调优能力，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因。

从DevEco Studio 6.0.0 Beta1版本开始，支持对Launch冷启动问题和Frame卡顿丢帧问题进行智慧调优分析。

从DevEco Studio 6.0.0 Beta3版本开始，支持对Allocation内存分配问题和Snapshot内存堆快照问题进行智慧调优分析。

从DevEco Studio 6.0.2 Beta1版本开始，增加了OOM内存溢出场景的分析能力，主要包括ArkUI组件、NAPI、闭包等内存问题场景。

从DevEco Studio 6.1.0 Beta1版本开始，增加了Snapshot对比场景的分析能力，主要包括监听事件、动画资源、泄漏次数分析等内存问题场景。

从DevEco Studio 6.1.0 Beta2版本开始，支持在智慧调优中使用和切换模型。

## 操作步骤

1. 首次使用请先根据界面提示完成CodeGenie授权登录。当前支持如下两种开启方式：

   **方式一：**若Launch、Frame、Allocation、Snapshot模板已录制完成，点击**Session**窗口中该条会话上的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Pu2BbX36Qqa5M59d8aaTaQ/zh-cn_image_0000002779566690.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C084831E97DD1E090456B3B99D16713BC47F86100010B25E5F8CBB90CEFA28A "点击放大")图标，即可开始智慧调优分析。录制方法具体请参考[性能问题定位：深度录制](deep-recording.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/RKM5o4uZS9ytvt709pzTog/zh-cn_image_0000002808766273.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5975F1B71D0FDA91CF0A2CD425748B59FDA43DDAE693BA22F1EE50696A37C7A)

   **方式二：**切换至**Assistant**窗口，点击**Create Session**开始录制调优任务；或点击**Open File**按钮导入已有的调优数据文件，当前支持导入的文件类型包括.insight、.heapsnapshot、.rawheap。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/0tFA25XNR0q2HeKA3wAQmg/zh-cn_image_0000002808766279.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A898FD7CF9F1A2CBC776FCC4B6C18E03C1F3587705BC14B5A62FE318709699A)
2. 对于方式二，在**Assistant**页面，点击**Create Session**按钮，从**Launch**、**Frame**、**Snapshot**、**Allocation**中选择一个分析模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Y8okP-nrSSuNVsymGjiGpA/zh-cn_image_0000002779566696.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFC5756D3BE3493749AD0E1F78860483256883C527F79E37D90D687785119E2B)

   使用Snapshot模板对堆快照问题进行分析时，支持在对话框中选择单个Snapshot分析，或选择两个Snapshot进行对比分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/6RR888zRQMibVhYVDzbvcQ/zh-cn_image_0000002779566694.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=136FCBE09954BA65270F9173E1E0F840B228DDDCF53B7295A6D3BFF6705C8A10)
3. 以Allocation为例，录制新的调优任务或导入本地已有的调优数据模板文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/ZWiAWyQiRUOScUWrTZYLug/zh-cn_image_0000002779406714.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D86202FB639F7AEFE256A563FE4E90CF27B653FC5A4038A86F66244558DA933)
4. 等待AI完成初步分析。左键点击高亮的泳道名称，点击**Analyze**进一步分析该阶段的具体内存信息，点击**View Lane**在右侧查看具体的泳道信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/Mh2OXtTCT5OAtarivbLtyw/zh-cn_image_0000002779406718.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=000CDA46BDBD2A042D3A8CD35B7D9AED67138B3E80F5B20D53103F575135186E)
5. 点击**Analyze**后，逐步深入挖掘当前异常场景，找到影响性能的可能原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/j2J1D7HCRFqCYT4QkMZcpw/zh-cn_image_0000002779406722.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=4802A4F3DCB73D83374879A720C519522CCD6A4718031FCF1DD8A50BC4381016)
