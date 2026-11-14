---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-filesystem
title: IO耗时：FileSystem分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > IO耗时：FileSystem分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:0ff160fbd02ef11de0be6b5f45e519c39ccf6566e27f4690a4377835b785ba4b
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

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/0C7vjvBbTcqARM77pmZ2jg/zh-cn_image_0000002779406854.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AAEC6632DD2806EB8DA170AD74A6749A2BE8D8D746C01B92CE67F5AAB17282E)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zl_Chop8T8a9iQFvl3_J3w/zh-cn_image_0000002808766421.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9145AB2CD94506F5EA2CD350F90A1173D6C51842DB5785D04D48A9D929149C7C)Logical Read Bytes：逻辑读的累计次数及字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/y9wK9jKHQQa7KmFtS0jMOQ/zh-cn_image_0000002808766415.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB72706F07F03F1C9039DF588E7ACC67DD3A2A793AE19F3AF31AC81420031AAE)Physical Write/Read Bytes：物理读写的累计次数和字节数。

框选**APP Name IO**主泳道，通过**Statistics**区域和**Details**区域查看选定时间段内的统计数据。

* Statistics区域：以进程维度展示了选定时间段内IO的统计数据，包括进程信息、IO类型、累计次数、累计字节数、最小时延、最大时延、平均时延、平均方差时延。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/Mjsx32qRQ0O3e3JkP-q0Jg/zh-cn_image_0000002808886497.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4CCB69C066DF66ED3151F2C56EF230D7A05E40E747D28127AD7B479268AB276 "点击放大")
* Details区域：展示详细的IO数据，包括开始时间、进程信息、线程信息、IO类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/bkZvrbagSlaqJOI6IF0aIA/zh-cn_image_0000002779566830.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2122407D5508E58590E2EA6DB9E55CE9647A6647B874F39760BA055A558132B7 "点击放大")

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes展示应用逻辑写的详细数据，Logical Reads展示应用逻辑读的详细数据，Physical Writes/Reads用于展示应用物理读写的详细数据。通过点选子泳道中的条块或框选子泳道，查看特定的统计数据。

* 点选子泳道中的条块，**Slice Detail**区域展示详情数据，包括IO的开始时间、所属进程、所属线程、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/gfPA8YgaT8CmUDrmaLNv6A/zh-cn_image_0000002808886505.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D91F8F9F8C0EE2D5FC1CF94DEFB116A6DA7F59E2ADECD2F166EEDA35EFC8BEBD "点击放大")

* 框选子泳道，**Details**详情区查看选定时间段内的详细数据，包括IO的开始时间、进程信息、线程信息、类型、单次时延、单次字节数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/nVEIIAeaRva8XzHKX_lElA/zh-cn_image_0000002808766419.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=009064BE2A724EC0A4151F95FCB3A30ED5C0A4525524FFCB035BAB04606BDD64 "点击放大")

## 查看整机IO耗时

File System IO泳道显示整机的逻辑读、逻辑写、物理读写累计次数和字节数，具体统计项如下。默认显示所有的统计项，如需取消查看某项数据，可在File System IO泳道的右上角取消勾选。

* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/O1YDV1F1Tb--SfJCLHYh5g/zh-cn_image_0000002808886501.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=38DA5354741392BBA84D7B73F642C6CC488ED9903C7135F61FA8C6958EB5AF61)Logical Write Bytes：逻辑写的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/MeMUhyGARKm70CSQJdNwcw/zh-cn_image_0000002779406860.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA5E7236E04E8377044AD390F85E774B22230366FD6CB26F094CD02E7BF2C158)Logical Read Bytes：逻辑读的累计次数和字节数。
* ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/fZ1Gnp5GSzyrhqD6hwQfSQ/zh-cn_image_0000002779406852.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=605F4280C32505E326FC3C8727C1D75D664C6E712B658B632299844AD44633B9)Physical Write/Read Bytes：物理读写的累计次数和字节数。

主泳道包括Logical Writes、Logical Reads、Physical Writes/Reads三条子泳道。Logical Writes子泳道展示整机逻辑写的详细数据，Logical Reads子泳道展示整机逻辑读的详细数据，Physical Writes/Reads子泳道展示整机物理读写的详细数据。

框选File System IO主泳道或子泳道，**Statistics**区域以进程维度展示选定时间段内的IO统计数据，包括进程信息、IO类型、次数、字节数、最小时延、最大时延、平均时延、平均方差时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/JqOm_eJ7T4OUD31wmWiotw/zh-cn_image_0000002808766417.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FE24498580243C370F6AE1DD310C57A9154DF6C44A7B9DAD7EC94EF46AD1D44 "点击放大")

单击主泳道或子泳道的Statistics区域中任意一行，右侧**More**区域中会显示详情数据，包括IO的开始时间、线程信息、单次时延、单次字节数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/MGgEo8o2SLeYTjl5v4ZYRA/zh-cn_image_0000002808886499.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A47162FD65D55F26C49BF72750C1FBC4BE202DCAE6E6173F6D78158A11E4991D "点击放大")

点选子泳道中的条块，展示条块对应时间区域的整机IO聚合数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/OLT4hSZOToiVCh_Lt3Qspg/zh-cn_image_0000002779566840.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1130D1255967F068128DAFC359644DD8C0ADC86DD8501DA124338A0A3C8E9AD5 "点击放大")
