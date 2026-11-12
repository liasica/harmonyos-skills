---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:50abb38a8d6d93bde78605a9d447205fb2fd4b6bb6ac4285844963c27b830621
---

DevEco Profiler左侧为会话区，可以分为三个部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/CyhSpc3rSiGayt--kQXWEQ/zh-cn_image_0000002779567528.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6FA0CB4E8D6F3CE66292194BC24F1C08B90851B15D24615412C6623DF9E90BB "点击放大")

① 调优目标选择区域。用于选择设备及要分析的应用和进程。

② 会话列表区域。

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/gVXjMi39Spajhqg--_Lx3w/zh-cn_image_0000002808767111.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=426A7CFE67D34489688E997E2C0277547F5FEB683BE6EA506AFA5DDE2147AD99)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/25_M1ampQqa_Fqrzhm0eEQ/zh-cn_image_0000002779567530.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=176EE913A4DEC7510E7AD4EBAF92E02C080A1DD167307DE84DF66611A2E83183)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/rEbNqVWoQR2BKC76FdaX_A/zh-cn_image_0000002808767107.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E1FD6B2DD2F51CA97ABEC89C3913253A6E221E525B388533C6CF1E8AD6B621E)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Y68thf4jSS6LnFxrUCbOsQ/zh-cn_image_0000002808887195.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DC4A20BB5BCFC6A75B1BF308FE40002D8E5F206913B42F75829531B4C7C56FF)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/RDllaAzHRB-s0vjZjvupVw/zh-cn_image_0000002779407554.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A8AF20B779424F90B5A0FEE7C4133FC15BE244B8BB1BDD627DCE2EF6645BE03)将删除该会话。

**说明** 

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/i7EUSVupQ7ubMCJQyb3rNQ/zh-cn_image_0000002779567532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=338EAD542146900BC149633A516E30CC9E1BA76E86FAB0C2563A85D68FAA1252)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/rIeYBtGiRtyMMiDQgEZruQ/zh-cn_image_0000002808767109.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=017F2508876AE5E67FF8085C9CF0920EC4C7FB761CAD97177EF958C8EDAA7F96 "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域。

* **创建会话：**DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[ComMemory](ide-commemory.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)、[FileSystem](ide-profiler-filesystem.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。
* **数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件，.zip（包含.htrace、.rawheap和.binpb文件，或只包含.htrace文件）。从26.0.1版本开始支持导入.zip文件。

* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ou2yj9OyQKGU2D_c8Y_1cA/zh-cn_image_0000002808887193.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A210C17B7E77D3162F5ADDAC1758EB8C834A72DE82EC90981EBC27F56279BAA "点击放大")设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/I2cdFReHTg2eox4QHV7T_w/zh-cn_image_0000002779407552.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7588198783FCEA228B42D137FDB9B26CDA2DAA5E77CA0F41A1CC26E2577122FF)
