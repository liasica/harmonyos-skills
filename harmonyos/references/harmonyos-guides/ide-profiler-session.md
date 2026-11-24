---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d3790af68e0d58aaaaf96133d963aac167c1a278ecf9b1078b30c01a861a3753
---

DevEco Profiler左侧为会话区，可以分为三个部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/uUAbmyfESmyR3RJS5CcwEw/zh-cn_image_0000002779567528.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9836146073B8E5A401709F02ED3647177EBC60FAF1394734AEF4D1AF93F133A "点击放大")

① 调优目标选择区域。用于选择设备及要分析的应用和进程。

② 会话列表区域。

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/L_MaJSnoSCe8oOJdGDatGQ/zh-cn_image_0000002808767111.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=578F0AD108C9C890F6679A362679649335089CADA71B89286B560BF377A2A189)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/NF8FKQyYTzqcTMFA5AsTHw/zh-cn_image_0000002779567530.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=95EB5D39C8062D395AA5FD5A441851A059DE33902A092E69EC8C47D295C97728)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/cPLh2YkkQZii-ljI8iLzVA/zh-cn_image_0000002808767107.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=76CDFB270D2C7A69B55C0A124311DAF47941BE3EC55C38D1E26DC0B5F9466C7C)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/QJ8ZXcB8RDubUUpWwM9klg/zh-cn_image_0000002808887195.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC88F7D6852030F9D2D350F8AB092A254796C46DDBE6603BB8CB9FEDED843C3A)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/As1Mf-VEReKaOmd2_ajilw/zh-cn_image_0000002779407554.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=F214CD416FD5D423A986AD88F8CAA7400C35DE11A1A8525A482606C9F0D7BA65)将删除该会话。

**说明** 

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/k4mMjqcaTjC4Uv_k7c2s3w/zh-cn_image_0000002779567532.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0595250617D71546D70DA79CF95B10CF475BCE35EA243C4DF2E6DF0CD64B00A2)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/u56Uep1bRMqGl6h0-2yDJA/zh-cn_image_0000002808767109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFCA97274D8D2591EA917A881283EAC694872B35C58EA5948920BE4768CF2C6B "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域。

* **创建会话：**DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[ComMemory](ide-commemory.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)、[FileSystem](ide-profiler-filesystem.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。
* **数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件，.zip（包含.htrace、.rawheap和.binpb文件，或只包含.htrace文件）。从26.0.1版本开始支持导入.zip文件。

* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/wkMpPfiPQuasBHl59ckrhA/zh-cn_image_0000002808887193.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D4960B2A80502CA09E9F71D2724085A59A03CBF56BBC59BB7437E3B604F5A3A "点击放大")设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/OSTd6Tk3RyOacA0iCcxGaA/zh-cn_image_0000002779407552.png?HW-CC-KV=V1&HW-CC-Date=20261124T044235Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C9B2C1CFAEB3AE67AC88918B23CE7932F27B754154142CE15A1192E1B020790)
