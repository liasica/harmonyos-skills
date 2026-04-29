---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-session
title: 会话区
breadcrumb: 指南 > 优化应用性能 > DevEco Profiler调优工具简介 > 会话区
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:30+08:00
doc_updated_at: 2026-03-31
content_hash: sha256:2dbb42e1fef2d22eb91ebc506ccdaa1feeb7a7db459152137739c4500ef07a27
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/gf8JorrbSy6065WqTSvV8Q/zh-cn_image_0000002561833603.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=443C621F1FE7D742E30A030F2D5968D263EDB23CEE5FD9142F2C34C886643505 "点击放大")

DevEco Profiler左侧为会话区，可以分为三个部分：

① 调优目标选择区域：选择设备及要分析的应用和进程。

选定被调优的设备、应用包及应用进程作为后续调优会话的分析对象。依次点击设备、应用、进程列表完成选择。

② 会话列表区域：列出当前已创建的调优分析会话。

单击列表中的会话后，界面右侧数据区将显示其数据内容。选择设备、应用和进程后，此处默认显示“Realtime Monitor”任务。

会话区将记录当前所有的会话。每一个会话都会包含：会话的名称（图例中的"Launch"）、会话当前状态（图例中的"Recorded"）、会话对应的录制时长信息（图例中的"7s 605ms"）。会话支持拖拽方式调整顺序。

**录制/删除会话**：通过鼠标悬停在名称后方的信息图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/xvyqmEnWSf-4k2xAWG_dDA/zh-cn_image_0000002561833623.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=04C592E4A034C307D9DD193006088565961436F6A10F4B3F98409EE4CE14B4A4)上，会话所要观测的调优对象的基本信息将会以Tooltip的形式展示。点击会话的右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/0z58spdcSr6m7fIHns_7yQ/zh-cn_image_0000002530913694.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=6ADAD5964CCB935EB53459C4C7F10760F82E186A0CB96DDD330AF5DFF6D70D0C)/![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/0uDrsujrTBuvUt3eFl6YnA/zh-cn_image_0000002561833611.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=3BCB81802A9A132414605BD265EEB3F2E5C865FC429890C1AE92F5047604EAA8)按钮，开启/停止会话录制，此时工具开始抓取性能数据，开发者可以操作应用复现性能劣化场景；点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/v6PE8dOUSBSx6E3QxnBdkg/zh-cn_image_0000002561833617.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=02ECE3CB7128302911C7E5067626968C921950851A469751C126D47B425F81EA)将删除该会话。

说明

* 会话区存在两种会话类型：活跃会话和历史会话。活跃会话可在此区域内直接看到，历史会话需要点击界面下方**View Successful Sessions**前往查看。开发者主动选择新的调优目标后，活跃会话会清空，相关会话进入历史会话。
* 历史会话中支持删除会话和数据导出。
* 仅成功录制或导入的session可长期存留在任务列表中；录制失败或未启动录制的session，在设备/应用切换时自动从任务列表中清除。
* 会话录制完成出现![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/dEiZm5KfTS-y53pld8y7bA/zh-cn_image_0000002530913680.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=F1D86CB3F62D846ACC5BB621D650779D955D39B8644E8BAD5B5F6210F8E9074B)图标，表示数据处于解析状态，请耐心等待解析完成。
* 支持的最大会话个数（活跃会话个数+历史会话个数总和，重复不计入）为15个。

**数据导出**：待数据解析完成后，会话便会进入数据展示状态，将数据可视化展示到右侧的数据区中。此时可以点击会话面板中出现的数据导出按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/bnFZ2fWTRU2BonquqmYGaw/zh-cn_image_0000002530913688.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=63A4E3D15EE49C8DAE54840F8650BC4FBBAABE17B3443F6FCDA9D14356DD7766)，将录制到的数据导出到本地进行保存，借助这个能力，开发者可以方便的在团队内共享录制到的性能数据，也可以防止采集到的性能数据丢失。

**智慧调优**：提供[智慧调优](ide-ai-profiler.md)功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/KoiYAjMqT9SmO_x679WqXg/zh-cn_image_0000002561833621.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=84CA0B2B6486049D1A8D789E10D869277F9BC0D5CD14AF86C31E1072F1541E8C "点击放大")，支持通过自然语言交互，分析并解释当前实例或项目中存在的性能问题，帮助开发者快速定位影响性能的具体原因，目前支持对Launch、Frame、Allocation、Snapshot模板进行智慧调优分析。

③ 场景化模板选择区域：新建会话的入口，DevEco Profiler提供[Frame](ide-insight-session-frame.md)、[Launch](ide-launch-overview.md)、[Snapshot](ide-insight-session-snapshot.md)、[Allocation](ide-insight-session-allocations.md)、[ArkUI](ide-arkui-analysis.md)、[Energy](ide-profiler-energy.md)、[ArkWeb](ide-profiler-arkweb.md)、[Network](ide-profiler-network.md)、[Concurrency](ide-parallel-concurrency-analysis.md)、[GPU](ide-profiler-gpu.md)、[Time](ide-insight-session-time.md)、[CPU](ide-insight-session-cpu.md)等场景化分析模板，提供对不同性能问题场景的数据分析方案。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/9OI1gWjBQuKw5MEIGI5ROw/zh-cn_image_0000002530753704.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=33392526D1514E2F3F5E7C95A61BF5EE2BC03A0217755ED63C5A19730DD3577A)：Frame卡顿丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/4xx0lnddRYmjFRIIi-OJgA/zh-cn_image_0000002561833597.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=BCE5307FBC487D9F5A1482C8D3761D3F7C04773AB443CA86A7665EA1574B5C86)：Launch冷启动场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Oy8omtyFSsaRGjEoxFsLaA/zh-cn_image_0000002561753651.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=861FF1B4518ADAAABFFB77499DB03F564B7550A17CC0797429DE3985B6A626CC)：Snapshot ArkTS内存泄漏场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/YqtNLCKASoaVCZYcehXBow/zh-cn_image_0000002561753643.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=D7B28E98934C2879CF90362AB178D2FB35127B44486E47CF2788CB0EFC9C30FF)：Allocation Native内存泄漏场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/XixonKcBRNS7wTWjikBtEg/zh-cn_image_0000002561833615.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=AAE49D7C07B1EBCB02C45BE15BF5ABA2DE509BB23324451E0BD44ED4F0BBDE0E)：ArkUI卡顿丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/PTSA5p3TQOmc6BSZj4HTdA/zh-cn_image_0000002561753649.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=74D3B77F9DEFBCB538F3D3F38D254575FDF7FE3FA60DE208B6F1C8A0206416B5)：Energy能耗诊断场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/5m5hYypwQ32LmdAw9iB4ew/zh-cn_image_0000002530753680.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=2A54C714881FE4B88FA13DFB2CB54E4D3DBBDEDD2F820EFA9FD66DFDC9B4233F)：ArkWeb加载丢帧场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/m4JIPkGkSgqTMpkiQq3Xsw/zh-cn_image_0000002561753621.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=9CD0727C4A437EE37021101A0EF39A6504BDF5EEE57F73450EE7F2018EE726FC)：Network网络诊断场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sATI0y1fTVGidgMRA6XZkg/zh-cn_image_0000002530913700.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=6C62457F68C7420CA26DC355F918953C72014DB4ACCB2A3D4C09EA81B5CDD2ED)：Concurrency并行并发场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/sI5ewkTNRKa9QHXcf85iWw/zh-cn_image_0000002530913690.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=0240171FB62AA98DC22BA5F81F87D033FB6E7B85CB4F143D8FF482239F9171B4)：GPU活动场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/0bWY34ehQmKeoRAiVkrfpA/zh-cn_image_0000002530753692.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=EE09E740F7097F072FD9D481E8DFC1FDBEC24D09D2F35617F24B0B85ABD4FC8D)：Time函数耗时场景化模板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/OzGWEJwYTriJJg5B7X0Uwg/zh-cn_image_0000002530913676.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=55FAC0BD7EC1F080A2B28943EA521E67E42844B9772E2C152CA47427CC2D8405)：CPU调度场景化模板。

选中任意模板图标，点击下方**Create Session**按钮，即可创建出一个全新的会话。

**数据导入**：在③场景化模板选择区域，点击**Open File**按钮，即可选择数据进行导入。当前支持.insight，.htrace， .ftrace，.heapsnapshot，.rawheap, .sys，.perfdata，.data，.nas（包含Native Allocation数据的文件），.txt（包含Native Allocation数据的文件）文件的导入。

**配置Profiler缓存路径**：在③场景化模板选择区域，点击左上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/xxvEsWbNTT2OCJ8aWEnSCA/zh-cn_image_0000002530913682.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=66D135CBB4FEFBF57057C5789A09D1B19DBDE63E80441F3D7076CDF2979E2982)设置按钮，会弹出文件选择器，设置Profiler缓存文件的保存路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/rmRXv8-jRwWDgKPK7Q5WkA/zh-cn_image_0000002561753655.png?HW-CC-KV=V1&HW-CC-Date=20260429T054728Z&HW-CC-Expire=86400&HW-CC-Sign=D3216853045FFC029B9390FC9E2E0FD2FDFC1C2F583D76175D143E231E63E9D3)
