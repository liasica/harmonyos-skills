---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:29+08:00
doc_updated_at: 2026-03-31
content_hash: sha256:6a0730173a360a0657141e6d958485ea87523417ff6f65927828bc2818047781
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/SxovUoDqQj6C2kYm32Qjsg/zh-cn_image_0000002561833603.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=D3B0E529DF6A014F59977932FA409299A785E84419C0EF95BCC718E89BF9081E "点击放大")

DevEco Profiler左侧为会话区，可以分为三个部分：

① 调优目标选择区域：选择设备及要分析的应用和进程。

选定被调优的设备、应用包及应用进程作为后续调优会话的分析对象。依次点击设备、应用、进程列表完成选择。

② 会话列表区域：列出当前已创建的调优分析会话。

单击列表中的会话后，界面右侧数据区将显示其数据内容。选择设备、应用和进程后，此处默认显示“Realtime Monitor”任务。

会话区将记录当前所有的会话。每一个会话都会包含：会话的名称（图例中的"Launch"）、会话当前状态（图例中的"Recorded"）、会话对应的录制时长信息（图例中的"7s 605ms"）。会话支持拖拽方式调整顺序。

**录制/删除会话**：通过鼠标悬停在名称后方的信息图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/hXSh_U5oSZqM7kUg335fmg/zh-cn_image_0000002561833623.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=A2AA741C0A03E551F18DD642E6389D8049104F9B6082D694C38743DDBCBF1770)上，会话所要观测的调优对象的基本信息将会以Tooltip的形式展示。点击会话的右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CjyJjOjlSMm1f1ZSb1thbw/zh-cn_image_0000002530913694.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=16852D09A698BD692E4BA623996D909E674ABFEF3E7D45A4FF3E2D80032220F4)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/87ZBCcvTSfGwcnKwjG3OiA/zh-cn_image_0000002561833611.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=BC499740EF6E2C727FA51BBA0C69CB7DF97C34779F63146A6985DFF4C1F30E21)按钮，开启/停止会话录制，此时工具开始抓取性能数据，开发者可以操作应用复现性能劣化场景；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/b8CQFgafRzWd7fHFuWjB-g/zh-cn_image_0000002561833617.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=A50E83CDFF15703A0F497C1075E95C73EEC67580F25B45C56932182870097315)将删除该会话。

说明

* 会话区存在两种会话类型：活跃会话和历史会话。活跃会话可在此区域内直接看到，历史会话需要点击界面下方**View Successful Sessions**前往查看。开发者主动选择新的调优目标后，活跃会话会清空，相关会话进入历史会话。
* 历史会话中支持删除会话和数据导出。
* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。
* 会话录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/wu5nXgpNTZa8dmAvvNBSag/zh-cn_image_0000002530913680.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=55FF6AD3670F1631B2AC834613180924D909018F8A8834F05E1BBB7931AB0E0A)图标，表示数据处于解析状态，请耐心等待解析完成。
* 支持的最大会话个数（活跃会话个数+历史会话个数总和，重复不计入）为15个。

**数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/G-_69tvmSkShJkC2Jp2bCw/zh-cn_image_0000002530913688.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=9451B86617F697C043F6425D093A34D9F319518502C4552BDA1527D3A2BF9DCD)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便的在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。

**智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/F6PpEKMATOyOSZQurpK4VA/zh-cn_image_0000002561833621.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=3B7DFA62D51112FA52E086C03F800DBBF5B7E3114913D61B9C9CB29614ED5739 "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。

③ 场景化模板选择区域：新建会话的入口，DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4sto2x3IRUyrkHGSssuYzw/zh-cn_image_0000002530753704.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=8C860C0C0CA087080FE989F4799CD0C5AD42BC97DA4A16740613C16D3D460990)：Frame卡顿丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/M_7JW5_6SoWJ0n7U7IAWuA/zh-cn_image_0000002561833597.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=287E3C54E1DEC18192BEA0475FD87DEC3342CE498C9C3F8CD1B9CB7A9BAA3C6C)：Launch冷启动场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/lRoPBhsvSPeRngW8c2L1UQ/zh-cn_image_0000002561753651.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=3CEBB0FBEB5962B82F5963478DD4C4C01B8A61263F16DCB1B5F272DF9C2736ED)：Snapshot ArkTS内存泄漏场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/pu53xsRHRf6PpMglwTD78w/zh-cn_image_0000002561753643.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=85BFACA6F230E597B73D0168400FD623D0A6C4F9A2620C0653AAF105BD82BFCB)：Allocation Native内存泄漏场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/0v-TThSDSOCzfelgySOpwQ/zh-cn_image_0000002561833615.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=8EB9D5A325E15950F49F1BC75BAAEA25EC5F29AB20491D2DC4A4AD58D201C764)：ArkUI卡顿丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ooqk6GsWR4aMUyPxqK3Zjg/zh-cn_image_0000002561753649.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=ED98D1A89BFDE2B401F653624C19219C500591F0AB0B55AFBCB03CA17E0D9A33)：Energy能耗诊断场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/0-Z9p_yqQRmOhV10nzgEWg/zh-cn_image_0000002530753680.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=B5C854DAC9A58812E1E93157A8BDA6019607DB05985E8B5C88211D3E1D085718)：ArkWeb加载丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/cdgZaSG_RrqszyQZ3mSjmw/zh-cn_image_0000002561753621.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=6FCBB34DF1857279D4F225B8EC015EBA2B7798A2E078CF750C074E399BC5851F)：Network网络诊断场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/MKPfUyjLSUKP5w3wkxMaAA/zh-cn_image_0000002530913700.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=DA9F8357EDEF12EFEB22A89D8C4F1AE41E9D2BC50AF343DED1DAA0117B6AD9CA)：Concurrency并行并发场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/9uBnnqA3S6OV1YnDPrmEpA/zh-cn_image_0000002530913690.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=A095B82969425916368BA0BF4EB00D5DA44DC11321585D24C3A37810FC11B14D)：GPU活动场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/GigRebYxRhCn_yDLp_iKuw/zh-cn_image_0000002530753692.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=B3F9585D6AD0E85D4746D754CB5AC8529EB1772BDBB4B295B056A4EECCE671F3)：Time函数耗时场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ILL0Et6GQkufBMYw3U6tew/zh-cn_image_0000002530913676.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=F7F449D6F56753DE28636A760CA759014548C83C72180EB8042A259080479954)：CPU调度场景化模板。

选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。

**数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件）文件的导入。

**配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/2zjpVoFZSBylUbta3kVS1w/zh-cn_image_0000002530913682.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=E87D5C6CF84221B5FEC0A9118CC98F6C225D6C63C19F1A9FCCF70DAFC2AB5958)设置按钮，会弹出文件选择器，设置Profiler缓存文件的保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/nM_6iS1bTVqfVNafDetVRw/zh-cn_image_0000002561753655.png?HW-CC-KV=V1&HW-CC-Date=20260427T235728Z&HW-CC-Expire=86400&HW-CC-Sign=3CE499C564EFE51257662801C7C087F0E4AF15F30BDB3B173DC2A6FBBE0A9A37)
