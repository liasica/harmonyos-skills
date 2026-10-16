---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-filesystem
title: IO耗时：FileSystem分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > IO耗时：FileSystem分析
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:35+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:362ad4c5ec9868f987c8a6e553e10ed6b8892b221951491b5b6902afc02a9276
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

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/rAYysNxNQ32mKJiouiuOpQ/zh-cn_image_0000002731542331.png)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/9YV3ozKGRF6O9lIt5p2wzg/zh-cn_image_0000002701663128.png)Logical Read Bytes：逻辑读的累计次数及字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/PYBOTQJVRLeW9HUGUhhuuA/zh-cn_image_0000002731542317.png)Physical Write/Read Bytes：物理读写的累计次数和字节数。

框选**APP Name IO**主泳道，通过**Statistics**区域和**Details**区域查看选定时间段内的统计数据。

* Statistics区域：以进程维度展示了选定时间段内IO的统计数据，包括进程信息、IO类型、累计次数、累计字节数、最小时延、最大时延、平均时延、平均方差时延。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZRtDVaXoRhySmpALtUKNmw/zh-cn_image_0000002731542325.png "点击放大")
* Details区域：展示详细的IO数据，包括开始时间、进程信息、线程信息、IO类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/PNIpGIyXTdygFOwiLp2Zpg/zh-cn_image_0000002701663120.png "点击放大")

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes展示应用逻辑写的详细数据，Logical Reads展示应用逻辑读的详细数据，Physical Writes/Reads用于展示应用物理读写的详细数据。通过点选子泳道中的条块或框选子泳道，查看特定的统计数据。

* 点选子泳道中的条块，**Slice Detail**区域展示详情数据，包括IO的开始时间、所属进程、所属线程、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/XeskdBqNQnqTv9N4eYnU9w/zh-cn_image_0000002731542323.png "点击放大")

* 框选子泳道，**Details**详情区查看选定时间段内的详细数据，包括IO的开始时间、进程信息、线程信息、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/NCYyVXVeQM2uOe0qR7uaIA/zh-cn_image_0000002731382355.png "点击放大")

## 查看整机IO耗时

File System IO泳道显示整机的逻辑读、逻辑写、物理读写累计次数和字节数，具体统计项如下。默认显示所有的统计项，如需取消查看某项数据，可在File System IO泳道的右上角取消勾选。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/kUgYzcZHT6WtID5Lsm4_HQ/zh-cn_image_0000002701823054.png)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/JDaTWty-QbCrf2w4DXreqQ/zh-cn_image_0000002731382363.png)Logical Read Bytes：逻辑读的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/YTpX9XVNQ8qbqI_0lLcvXA/zh-cn_image_0000002701823048.png)Physical Write/Read Bytes：物理读写的累计次数和字节数。

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes子泳道展示整机逻辑写的详细数据，Logical Reads子泳道展示整机逻辑读的详细数据，Physical Writes/Reads子泳道展示整机物理读写的详细数据。

框选File System IO主泳道或子泳道，**Statistics**区域以进程维度展示选定时间段内的IO统计数据，包括进程信息、IO类型、次数、字节数、最小时延、最大时延、平均时延、平均方差时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/V_aGgqKFTV69QaIqA2wlIA/zh-cn_image_0000002731542319.png "点击放大")

单击主泳道或子泳道的Statistics区域中任意一行，右侧**More**区域中会显示详情数据，包括IO的开始时间、线程信息、单次时延、单次字节数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/naoY2hDFTva31_x-Uqnyjw/zh-cn_image_0000002701663134.png "点击放大")

点选子泳道中的条块，展示条块对应时间区域的整机IO聚合数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IxF7xHCfSCSYuJxrOvBxTQ/zh-cn_image_0000002731382347.png "点击放大")
