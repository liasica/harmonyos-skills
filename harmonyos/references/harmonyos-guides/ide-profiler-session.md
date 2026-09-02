---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f736b50785f9521af3218ec7ce338bdc2c3d6bc3bc9a979f45069630fa880dfc
---

DevEco Profiler左侧为会话区，可以分为三个部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ZETsRNyQQ0GBOvQYMgdQLA/zh-cn_image_0000002701663872.png "点击放大")

① 调优目标选择区域。用于选择设备及要分析的应用和进程。

② 会话列表区域。

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/aRcoXd7AQGy_8r13vMu5kg/zh-cn_image_0000002701663890.png)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/kTSpSXJyQou1A2apX-wwrw/zh-cn_image_0000002701823804.png)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/2hspIsdLQ9SF6cWeQtIpBg/zh-cn_image_0000002701823798.png)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/X_DxhxOkQH-xb7sMfJZAqw/zh-cn_image_0000002701823810.png)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/G38hvf4HR7OWwlleRM3EVw/zh-cn_image_0000002701823820.png)将删除该会话。

**说明** 

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/kYNdt_1kQluQNwI1uiG2CQ/zh-cn_image_0000002701663884.png)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/VBiEuEybTv2oaeGtK5pLCQ/zh-cn_image_0000002701823814.png "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域。

* **创建会话：**DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[ComMemory](ide-commemory.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)、[FileSystem](ide-profiler-filesystem.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。
* **数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件。

* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ZbqoYFurQT-OawQfQSDlgw/zh-cn_image_0000002701663896.png "点击放大")设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/hO6wCWMcRn22XVk9YXvOFg/zh-cn_image_0000002701663878.png)
