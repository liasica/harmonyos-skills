---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-filesystem
title: IO耗时：FileSystem分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > IO耗时：FileSystem分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:9027b023b89e48f062b2692fff27ba0ad596acef5e4ba43556f0b231874513b9
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

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ndZ8ssJtTNa7au7OltpS6Q/zh-cn_image_0000002779406854.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCEBE6185832A31CB2009139816C68192BDACFDF775FC5079A0C9B2A48C77E52)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/S-J9TBK4RQGKGWGLm04tPg/zh-cn_image_0000002808766421.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=40E2F03852E6C27460A682EDE0CB425F25E464EB3655C0A20964D33295A5AF26)Logical Read Bytes：逻辑读的累计次数及字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/JRSMkKZhTtSTVoBz1zSsSw/zh-cn_image_0000002808766415.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=360D58D6F65E3BE42E02DB5A121E5103FF709434C4702BBE51515369C09E0231)Physical Write/Read Bytes：物理读写的累计次数和字节数。

框选**APP Name IO**主泳道，通过**Statistics**区域和**Details**区域查看选定时间段内的统计数据。

* Statistics区域：以进程维度展示了选定时间段内IO的统计数据，包括进程信息、IO类型、累计次数、累计字节数、最小时延、最大时延、平均时延、平均方差时延。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ruFGzKmdQrWB1pLtupJeBQ/zh-cn_image_0000002808886497.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7DB94A375EC3BEF3E49A4F53A1295E4A401013639E02C562D29FDD7800D97D7 "点击放大")
* Details区域：展示详细的IO数据，包括开始时间、进程信息、线程信息、IO类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/RCqcyZoqR7-B6SnH80FlnQ/zh-cn_image_0000002779566830.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A77F7EF6C6AB7066C4570C5E76E84A0B0AF38DA16F2CF711D6D74877D72D006 "点击放大")

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes展示应用逻辑写的详细数据，Logical Reads展示应用逻辑读的详细数据，Physical Writes/Reads用于展示应用物理读写的详细数据。通过点选子泳道中的条块或框选子泳道，查看特定的统计数据。

* 点选子泳道中的条块，**Slice Detail**区域展示详情数据，包括IO的开始时间、所属进程、所属线程、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/NyYtGNOXQI22x67PXP2WvQ/zh-cn_image_0000002808886505.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B81DE4F3777978A87FDCCA09DFB4C2FF1ED3736D82B6907769BE9829FFF8346 "点击放大")

* 框选子泳道，**Details**详情区查看选定时间段内的详细数据，包括IO的开始时间、进程信息、线程信息、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/foulRtE0QPC23LOr7LKR5Q/zh-cn_image_0000002808766419.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=40F54873CBBB35CD91E92F624A7CC33FC78E0409CBC74DE577A475D3EC83DE22 "点击放大")

## 查看整机IO耗时

File System IO泳道显示整机的逻辑读、逻辑写、物理读写累计次数和字节数，具体统计项如下。默认显示所有的统计项，如需取消查看某项数据，可在File System IO泳道的右上角取消勾选。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/6NqGkma-SiWB_gfvfYsu_w/zh-cn_image_0000002808886501.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED307A2C790E47BF10760AE1729907C0062D6460DDA42DCADDD0BEEACEBBA350)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Wht9-78zRyaMttizfmitLQ/zh-cn_image_0000002779406860.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD0230065C95FB01DF88E46275D540AA8839739B04AB3F9557A83BD74D5365BD)Logical Read Bytes：逻辑读的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BI0dWsBdRwSZwf3QWQ17CA/zh-cn_image_0000002779406852.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=098ABB068AD756CBF264A1274FD47C3777730CA2F9F254AB9BC33C7CED58A5EF)Physical Write/Read Bytes：物理读写的累计次数和字节数。

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes子泳道展示整机逻辑写的详细数据，Logical Reads子泳道展示整机逻辑读的详细数据，Physical Writes/Reads子泳道展示整机物理读写的详细数据。

框选File System IO主泳道或子泳道，**Statistics**区域以进程维度展示选定时间段内的IO统计数据，包括进程信息、IO类型、次数、字节数、最小时延、最大时延、平均时延、平均方差时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/VO0cuxblQTCBe77XvtN90g/zh-cn_image_0000002808766417.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABC5BCE79B2A80F2FDBBE9CFF2E775EEAA470814AA6108216DA0DCE65A55566E "点击放大")

单击主泳道或子泳道的Statistics区域中任意一行，右侧**More**区域中会显示详情数据，包括IO的开始时间、线程信息、单次时延、单次字节数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_oLKii-VQEGK6ygCzYSNtQ/zh-cn_image_0000002808886499.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6345CD89B78D7B8AC6A57178BEBBC1A6C19E799C62DDEA5BB43D4E89F540E2BC "点击放大")

点选子泳道中的条块，展示条块对应时间区域的整机IO聚合数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/wKQy2t2uQi2jLkLfSNAv9g/zh-cn_image_0000002779566840.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE4605BAE009CD25790EDC95F9B3C5E2B7ACF3FD226150181D692DF4988620E1 "点击放大")
