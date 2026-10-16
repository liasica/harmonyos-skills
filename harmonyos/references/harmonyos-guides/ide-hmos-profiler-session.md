---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:50+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f1a2a8e2539767e2a40b73ead00326ec7168e5a35a67ed89592101615b16d2cf
---

DevEco Profiler左侧为会话区，分为两个部分：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/RaPN1VvFR76Qsb-AVbT-mQ/zh-cn_image_0000002750009796.png "点击放大")

① 调优目标选择区域：选择被调优的设备、应用包及应用进程作为后续调优会话的分析对象。

② 会话列表区域：记录当前已创建的调优分析会话，每一个会话都会包含：会话的名称、会话当前状态、会话对应的录制时长信息。单击列表中的会话后，界面右侧数据区将显示其数据内容。

**说明** 

会话录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/54kO9aJIT4KvV5PXIFlOPw/zh-cn_image_0000002779608705.png)图标，表示数据处于解析状态，请耐心等待解析完成。

* **创建会话**：点击会话列表![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/U_SYXT6sTTuX0E8rrydMjQ/zh-cn_image_0000002779728855.png)图标，在弹窗中选中任意模板，点击下方**新建会话**按钮，即可创建出一个全新的会话。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/aQnxaQioT_Cm16OoumAuqg/zh-cn_image_0000002750169686.png "点击放大")
* **数据导入**：单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/D0_0yxASRZKccDuTVSAMCw/zh-cn_image_0000002750009798.png)图标选择.insight文件，即可导入历史数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/qVOYj5MeS7K8SyOAItEeYg/zh-cn_image_0000002779728861.png "点击放大")
* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/E-gdNO71RL6url2XC-BwBQ/zh-cn_image_0000002779608709.png "点击放大")，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
