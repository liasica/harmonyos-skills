---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-filesystem
title: IO耗时：FileSystem分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > IO耗时：FileSystem分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:6029cc8c6341559758a837bb09935be9a00c1f59521870771a873ab9bce72f5c
---

## 功能介绍

应用在开发过程中，可能因为线程频繁切换、磁盘负载高等情况导致文件系统IO耗时问题。从26.0.0版本开始，DevEco Profiler新增FileSystem模板，可以结合应用逻辑IO和物理IO的读写耗时、整机（设备上所有应用）逻辑IO和物理IO的读写耗时等情况，定位IO耗时问题。

FileSystem模板支持的泳道包括：APP Name IO、File System IO、Callstack、Frame。本文介绍APP Name IO、File System IO泳道，其他泳道的详细信息请参考对应模板内容。

* Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。
* Frame泳道的介绍请参考[Frame分析](ide-insight-session-frame.md)。

**说明** 

* 任务分析前，需创建FileSystem分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。
* 仅应用触发逻辑IO读写时，Callstack泳道才会采集数据。

## 约束与限制

仅支持2in1设备。

## 查看应用IO耗时

APP Name IO泳道显示调测应用的逻辑读、逻辑写、物理读写的累计次数和字节数，具体统计项如下。默认显示所有的统计项，如需取消查看某项数据，可在APP Name IO泳道的右上角取消勾选。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/BL62Ws7xSMOfVeQAlsjT1Q/zh-cn_image_0000002779406854.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=75A77D229A5771CF5D911AB8DD2F898C7FADAB204C90C465A9EE06A8C3F710F8)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/AihKEKsaQ4axzEJ5z6PoNQ/zh-cn_image_0000002808766421.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=488A66271780EABB193C8B506F99B08259439504784AD702ADECD0CB5E083629)Logical Read Bytes：逻辑读的累计次数及字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/iqtKKNnLRA21RrhLq3rh-A/zh-cn_image_0000002808766415.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CE459A797C20043D83325D852DB811D3E86221AC94E3ADD416B602E8317E46F)Physical Write/Read Bytes：物理读写的累计次数和字节数。

框选**APP Name IO**主泳道，通过**Statistics**区域和**Details**区域查看选定时间段内的统计数据。

* Statistics区域：以进程维度展示了选定时间段内IO的统计数据，包括进程信息、IO类型、累计次数、累计字节数、最小时延、最大时延、平均时延、平均方差时延。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/iCMeqBddRvqi7NXcD4kPKw/zh-cn_image_0000002808886497.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=809F6A1564ECDFA8907A3F7613D2CE015E9390280C13AEED5F3505E838C258B2 "点击放大")
* Details区域：展示详细的IO数据，包括开始时间、进程信息、线程信息、IO类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/d-ck82OfSbKqUBqCZd-Pqg/zh-cn_image_0000002779566830.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD08081F625654A46BA42D1EDD5DC48AEE871D23FED3B5C0E1C508DB98EAB0FF "点击放大")

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes展示应用逻辑写的详细数据，Logical Reads展示应用逻辑读的详细数据，Physical Writes/Reads用于展示应用物理读写的详细数据。通过点选子泳道中的条块或框选子泳道，查看特定的统计数据。

* 点选子泳道中的条块，**Slice Detail**区域展示详情数据，包括IO的开始时间、所属进程、所属线程、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Nya0TkFPQEWkvnJ_cF95YQ/zh-cn_image_0000002808886505.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBB25BC815997D3B969CEFEDDAD5B3CBB31316080A24D9BBD87DBCE6AA4B4DCE "点击放大")

* 框选子泳道，**Details**详情区查看选定时间段内的详细数据，包括IO的开始时间、进程信息、线程信息、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/gpV0M6WQRUaUb90ueIDpSA/zh-cn_image_0000002808766419.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD3D53FCD2D103AB02F481372E019B915AE1E6B4EF437E5F42F4D84D00437880 "点击放大")

## 查看整机IO耗时

File System IO泳道显示整机的逻辑读、逻辑写、物理读写累计次数和字节数，具体统计项如下。默认显示所有的统计项，如需取消查看某项数据，可在File System IO泳道的右上角取消勾选。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/xBswhep_Q1eQrhPO6U36TA/zh-cn_image_0000002808886501.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC6EE343B9AFBBA6B5D5C3664A6857B043E34F0618212BA11D84C65A199DF4CD)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/xrbhdTfDT1qoeZLsf6SLMg/zh-cn_image_0000002779406860.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB08A1586671DA6CDB8DB7AD30B86991161F505B6CC0CAA892BD2084333DAEA4)Logical Read Bytes：逻辑读的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/2TluNXo5QGK2kXmH5U-Yag/zh-cn_image_0000002779406852.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A118471D7B9EAF02D020C23E398C8A2BC1D7DDDFE0DF00DE70E2D8A84DCB1027)Physical Write/Read Bytes：物理读写的累计次数和字节数。

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes子泳道展示整机逻辑写的详细数据，Logical Reads子泳道展示整机逻辑读的详细数据，Physical Writes/Reads子泳道展示整机物理读写的详细数据。

框选File System IO主泳道或子泳道，**Statistics**区域以进程维度展示选定时间段内的IO统计数据，包括进程信息、IO类型、次数、字节数、最小时延、最大时延、平均时延、平均方差时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Qac-0jwtQd6zjmtd7VNfUg/zh-cn_image_0000002808766417.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2E56B49D72D7375238D151EBB81FBDD668FF8A7273DADFE13E59B592AD7EE77 "点击放大")

单击主泳道或子泳道的Statistics区域中任意一行，右侧**More**区域中会显示详情数据，包括IO的开始时间、线程信息、单次时延、单次字节数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/U9lKVVnzSD6L-NSGP4Cn-Q/zh-cn_image_0000002808886499.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=47A0BEB60E4F32B443C3E439F1E4A9E9D72724FC948BCDC10E49AF740D067374 "点击放大")

点选子泳道中的条块，展示条块对应时间区域的整机IO聚合数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/o9UzaeAdS1adaboBdDrH2w/zh-cn_image_0000002779566840.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=60BE74A3E0252B358B780DB0747917CD94B0B448A5DA4951B9A41B83207C14D1 "点击放大")
