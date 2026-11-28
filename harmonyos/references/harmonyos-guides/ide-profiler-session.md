---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:44+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0da7dacf3e27ade91b1ad33dd569d2443021fa7a7e02331880cce8dbc94d68ed
---

DevEco Profiler左侧为会话区，可以分为三个部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/7a9hwbTkRaawCRf2hdswVA/zh-cn_image_0000002779567528.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A402AD0E4DAE7D6C88AE7C77CFDE728D62D83DE0D2F8658651EE83A225E85D0 "点击放大")

① 调优目标选择区域。用于选择设备及要分析的应用和进程。

② 会话列表区域。

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ZT1BXdk1SOmc-YD_Y6ZDdw/zh-cn_image_0000002808767111.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=547ED3AD2FC94C36DC0F2D22564B41086808EE1815C85A59156E5FA5FD8AE2B9)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Og_Pw4CpQXW8zgpZUlE3jg/zh-cn_image_0000002779567530.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6471C577C34BC8422BAC451A684B5D47255333501CF322C3510A5C6520E364B)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/az8IdUbQSfCZxH88ImqLhg/zh-cn_image_0000002808767107.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=6942570DC2995DF638EEF3B6EE6D518718931A3C4193D62C114204C150868959)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/-beZvUGyS6qw_PLtKTOAzA/zh-cn_image_0000002808887195.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=81093E56D415322EE59DB6EA2E74B594008529AFF3B4F7382EEB9A83EA2FB98F)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/c8gm6Cy4SKWyNwskdjQ7lg/zh-cn_image_0000002779407554.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=C28FBAB3FA9E744CA4430D14E21A535F62946C3173677B006312845B0E607D6F)将删除该会话。

**说明** 

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ngTQTTQWTv6SrYW0DK1lkA/zh-cn_image_0000002779567532.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD09C39225E94A553FAE4F16A8CE5BD359DFB2D9E7416A3FEBBE42E68423FFB5)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/l8VgYfNtREORJ-sl17fZFg/zh-cn_image_0000002808767109.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=00DC2B11095960A667F0C7477E8C31A212B8B1113DF9FC6186102167B4755651 "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域。

* **创建会话：**DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[ComMemory](ide-commemory.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)、[FileSystem](ide-profiler-filesystem.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。
* **数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件，.zip（包含.htrace、.rawheap和.binpb文件，或只包含.htrace文件）。从26.0.1版本开始支持导入.zip文件。

* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/decjpcliThKFudf8UjftfA/zh-cn_image_0000002808887193.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBC380FAF858C100E053C2C38AAFEC1D099DD581D1E17B36DAEB24493E4C2444 "点击放大")设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/-i2YKbEdR9-X-3p2iL5d4g/zh-cn_image_0000002779407552.png?HW-CC-KV=V1&HW-CC-Date=20261128T023444Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0480D6085872CA391B7DBA90F4302614CCCD310D81BB17E950C57FC3A304ED7)
