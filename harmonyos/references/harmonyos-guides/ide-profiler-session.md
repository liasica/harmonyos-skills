---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ab74d2f7492b602bdd2bd0cd02dbd907cee905c566d0899a7f98ef5ce6660f56
---

DevEco Profiler左侧为会话区，可以分为三个部分。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/qoxfkYq-RAWDz3zlhqPImA/zh-cn_image_0000002779567528.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=960743D706FBD2F321640E35732114A404D6BD9D188E09E0E255724E3018295E "点击放大")

① 调优目标选择区域。用于选择设备及要分析的应用和进程。

② 会话列表区域。

* 记录当前已创建的调优分析会话，默认显示实时监控（Realtime Monitor）任务，每个会话包含：会话名称（图例中的"Launch"）、当前状态（图例中的"Recorded"）、录制时长（图例中的"7s 605ms"）；单击列表中会话后，右侧数据区将显示具体的数据内容；会话支持拖拽方式调整顺序。
* **录制/删除会话**：将鼠标悬停在图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/SmWPxeMTRaqt3wVwosX2Lw/zh-cn_image_0000002808767111.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=52292A81E392D7ED0128C1C25DF03DCD913C056547BFAAC923C7A9FC81192E6F)上，会话要观测的调优对象的基本信息会以Tooltip形式展示。点击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/urQYOy_QR1iubO8aC3szIA/zh-cn_image_0000002779567530.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=405E304D24E012DD801C0AF848127FE37805E915CEFB738BAB30F4F7A905AB34)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/EA7pCL74Ql6MLOoDcJMnXg/zh-cn_image_0000002808767107.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FB8B12153064E1ED23327EF60B8C5769C56689ED5043AB0CC0FEF1E96D1118E)按钮，开启/停止会话录制，开发者可以操作应用复现性能劣化场景；录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/TsufBGb1T16S-4212B8M4Q/zh-cn_image_0000002808887195.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=760C7E316735A843A356DFA0166579D5C83AE20C0D178762B0D4FA83D0CC04D4)图标，表示数据处于解析状态，请等待解析完成。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/okU3LbfwRgCBCOQQXoVIpw/zh-cn_image_0000002779407554.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=58DAF4A8D66F9CA49200E489C3E794273429AB1DAFF22A2BFCFE48FCAA845AB2)将删除该会话。

**说明** 

* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。

* **数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/cGNHhPozRdqp1vIr2tACLg/zh-cn_image_0000002779567532.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=80F3592B6CDAE4BFC4CB34730E1189CAE8410D205D09A8108E6B8E6975B71E4E)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便地在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。
* **智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/MY2e0s-LT9a2btVkiM8Uew/zh-cn_image_0000002808767109.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=A349FF9773BE020E90972E6CAACB6EF0ABB807A8A25F1B70BF94E8D76252F6AE "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。
* **查看会话：**会话区存在活跃会话和历史会话两种，活跃会话可直接看到，历史会话需要点击**View Successful Sessions**查看，两种会话总数量不超过15个。开发者主动选择新的调优目标后，相关会话进入历史会话。历史会话中支持删除会话和数据导出。

③ 场景化模板选择区域。

* **创建会话：**DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[ComMemory](ide-commemory.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)、[FileSystem](ide-profiler-filesystem.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案，选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。
* **数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持导入.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件），.acm文件，.zip（包含.htrace、.rawheap和.binpb文件，或只包含.htrace文件）。从26.0.1版本开始支持导入.zip文件。

* **配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/QcqNxXfCT0SSpPC-su2E4g/zh-cn_image_0000002808887193.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2CBAA588583C19F60E1BD8375A7730093AB3C04FABB937523A287C32A78E7B9 "点击放大")设置按钮，设置Profiler缓存文件的保存路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/gn03ZpG-QVKg9bUeQnLCqQ/zh-cn_image_0000002779407552.png?HW-CC-KV=V1&HW-CC-Date=20261114T004717Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9973AA1C849A8EEE6E3E7E28C1BF683424FC6C0BAD56A9E9D893ED8AA18677A)
