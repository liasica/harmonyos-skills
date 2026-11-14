---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-thread-leaks
title: 运维态高效处理线程泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理线程泄漏
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:a1d12bb3a835a79369c9be1e628e02b1d99560a4ab858ce2e2e95758909dd14b
---

## 概述

线程泄漏是指程序在运行过程中，动态创建了线程，但没能正确释放或终止这些线程，导致线程数量持续增长。每个线程会占用一个线程栈，线程泄漏会导致内存泄漏。如果线程持续占用CPU，还会使CPU资源耗尽，最终导致应用前台闪退或系统查杀后台应用。本文主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行线程泄漏的监控、分析、定位与修复整套处理方法。

## 运维态线程泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Gtob3mytSXihdao4B7HwJg/zh-cn_image_0000002729540781.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=53C2D94208F900CE8F3AD348E1CE0C6B024E019D02FC93DCE53C712DD93642B3 "点击放大")

**排查步骤**

**1.故障预警配置**：在APMS平台配置线程泄漏监控告警规则，设置监控时段、频率和触发条件。

**2.问题发现与筛选**：通过故障预警或主动分析页面，筛选THREAD\_LEAK类型的泄漏问题。

**3.关键信息提取**：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级的问题。

**4.根因定位**：通过证据链、现场数据和创建线程调用栈，深入分析泄漏原因。

**5.修复与验证**：根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/LNtvzwPwTeSGvV31rsQ-Zg/zh-cn_image_0000002699661556.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=11439733351AA17F0952E67F39B56171954791F301AF8646E2479694CDF35221 "点击放大")

**关键指标说明**

* **问题特征ID**：按照故障模块信息生成的哈希值。
* **故障模块**：发生泄漏的模块或组件，用于定位问题范围。
* **发生次数（占比）**：泄漏问题发生的频率，帮助判断问题严重程度。
* **影响设备数（占比）**：受影响的设备数量，评估问题影响面。
* **最大泄漏数**：单次泄漏的最大线程数量。

**故障详情页关键信息提取**

故障详情页如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/REwK9x8kSjyG6RbNzqY2PQ/zh-cn_image_0000002729420829.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=4065B3F04D1DFD5D7AD232015B6EDF54736E46B26E95F329ABBF494B3B0E6977 "点击放大")

**证据链**

证据链列表包含以下诊断依据：

* Top 10泄漏线程：按泄漏数量从高到低排序；
* Top 10线程故障模块信息：按线程名称和堆栈聚合，展示对应调用栈帧，按调用频次排序；
* Profiler：呈现线程创建时的原始调用栈；

综合上述信息，将线程名、故障栈、创建栈与业务代码关联分析，可系统性地追溯线程泄漏的根本原因。

证据链列表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/sJZqHFvdS7qF10ahpqhCOA/zh-cn_image_0000002699821464.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=648B982559CBFBD1129313C8D15829909F7EA7D66380340E6A026414C4ED8A2E "点击放大")

**现场数据**

现场数据展示的是线程泄漏时线程内的调用栈，并按同名线程数量的大小排列。疑似泄漏点为数量最多的线程中最后调用的应用栈帧或非公共系统栈帧。非公共系统栈帧指系统框架层中非公共实现的函数调用帧，区别于无分析价值的公共系统基础栈帧。开发者可根据疑似泄漏点分析线程未退出的原因。

现场数据页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/Chiz6hB4T0u-glWlB9vXvw/zh-cn_image_0000002729540783.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEFB0518832947B1B020FD1C6FF7A232930F6C0FAF6405C90031D19FD0E1121D "点击放大")

**创建线程调用栈信息**

创建线程调用栈信息中可查看创建线程的详细调用栈，通过分析泄漏线程创建时的调用栈信息，并关联业务代码进行综合诊断，可有效锁定导致泄漏的具体线程及其创建逻辑。

创建线程调用栈信息页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/_1wLu4VsSauJawVQp969rw/zh-cn_image_0000002699661558.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A885A4094BD0E65493EF885A6DA0591CE8EFE35ED45A5FCC7ECCF21F0ECF1A1 "点击放大")

## APMS平台线程泄漏分析案例

### APMS故障预警

可以在故障预警平台的故障告警页面新建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中线程泄漏对应的指标类型为THREAD\_LEAK（线程泄漏）。

故障预警配置界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/uR0dy2raSQmhxpO2QeRkFA/zh-cn_image_0000002729420831.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DEEF47A174DB307AA522877AB71BC501FBE4456235404888453F3EA8278824A "点击放大")

创建告警之后，故障触发后台会开始收集数据。当泄漏达到告警阈值后，会触发故障预警。

故障预警通知如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/4YtpJImKTYu7_iVIU1RzwQ/zh-cn_image_0000002699821466.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3A72F0D291AFDD0152B6D8E41C452506F0CB99C8B181FF6353FCE5D648408B0 "点击放大")

### 问题查看与聚类

**聚类规则说明**

聚类规则请参考[线程泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#线程泄漏聚类规则)。

**Top问题查看**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为THREAD\_LEAK，单击查询按钮过滤出此应用的线程泄漏问题。

线程泄漏查询界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/AtY43IR3TH2Yj_IR80EJrA/zh-cn_image_0000002729540785.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA9AE730698BC7C17E4E21D08F931EC6ABAA32481F78279BA802E8E1C3C65205 "点击放大")

在资源泄漏信息详情中，可查看当前应用的线程泄漏情况。

资源泄漏信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/J3_oej3aSMyql-HB43qI_w/zh-cn_image_0000002699661560.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F59CB2D73035D4A60AA87E7C6D8C6D8955998092E63E4E015320B0385E18E0D4 "点击放大")

### 根因定位与分析

**证据链分析**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、堆栈及优化建议，定位并修复问题代码。

经分析，本次泄漏核心为线程example.test（泄漏数量1002），关联模块libentry.so及方法LibuvAsyncStartLeakTask()应作为排查重点。

证据链详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/miKKqWtGR92H5L9OxaWaWA/zh-cn_image_0000002729420833.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD1EE5E92ED5CDB59A4439F9A767EFB6B2147CCCEE8B6A3219DF633B973187E9 "点击放大")

**现场数据分析**

现场数据按照线程名称和线程堆栈进行聚类并按线程数量的大小排序，进行堆栈还原（上传符号表将异常堆栈解析成源码对应的堆栈）后，开发者可根据疑似泄漏点定位到具体的代码行并结合代码分析线程未退出的原因。

现场数据详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/O0OpSrZLTwKYuN2T0t8pYA/zh-cn_image_0000002699821468.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9033A8025C4A142959BDBFF159D21577F00A58C3580D677EC078D7D2BF94E1D "点击放大")

**创建线程调用栈信息分析**

创建线程调用栈信息是应用发生线程泄漏故障后，系统抓取创建线程的详细堆栈信息。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因，并进行修复。

创建线程调用栈信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/tH3JBW5bSnW_wKZ_EED3tg/zh-cn_image_0000002729540787.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD7CFCDB0BC3C4D92DF62262C0CCD9AFC0E118EF8AB2285FD417B2CA96628635 "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

下钻分析界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/HCJhCg_VQf6TVBr90jfZKg/zh-cn_image_0000002699661562.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2F755E65E70CB24CBE2CF29CBBA161995863FB9AA4EFA406A3E062C0739395C "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

修复建议界面如下所示：

**应用发布**

应用发布之后，更新平台告警规则，并持续关注新版本的线程泄漏数据。对比修复前后的问题发生率，确认修复是否有效。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者在IDE上也可以使用相同的方式分析运维态的泄漏问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在Tool Windows栏的Operation Analyzer进入平台，单击后根据包名选择应用，再单击资源泄漏（Resource Leak）即可查看该类故障相关数据。

Operation Analyzer平台界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/phSypaWoQiWGw5OUtMpDPg/zh-cn_image_0000002729420835.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=A21431FC0D11A7ADBFC8C88D13B48F69B9B202872BFAA649DDE1A2161B998716 "点击放大")

### 问题分析

**分析证据链**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、故障模块及Profiler信息，定位并修复问题代码。

Operation Analyzer证据链界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/8FUg6DreSd24DiUe1nSOWA/zh-cn_image_0000002699821470.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=33017CC508E4791EECE1B63D375479F26F5B87BB249F3D3D32F3A361F8651270 "点击放大")

**分析现场数据**

现场数据按照线程名称和线程堆栈进行聚类，并按线程数量的大小排序，优先查看线程数量最多的线程堆栈。

现场数据界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/nGqo-yaUTKq21Nhc7HDFbw/zh-cn_image_0000002729540789.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=05861C750A46C12155B0E918D4E96EB9F1A8B7A48623A10DD9BCBF5F7C26E0C4 "点击放大")

**分析创建线程调用栈**

创建线程调用栈信息是应用发生线程泄漏故障并达到一定条件后，系统抓取的堆栈信息，存在一定的滞后性。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因。

创建线程调用栈界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/DunmAXeGREWWg0CLyleP2Q/zh-cn_image_0000002699661564.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=20C9F3CAA401414ED3754862B1B10769E51DBECF3E982F6D032087A02969BF9B "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

关联离线符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/qZzihCRERfa4kTvOYA1txQ/zh-cn_image_0000002729420837.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=2575CF6121057D9A69BBDD0753649DFE36EF441A2CB384AEA17A71D542524946 "点击放大")

上传符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/3KxkHThcT3WLgGRQhD8Qlg/zh-cn_image_0000002699821472.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CAD98EA142E8557887656C2A97C357E121605D7D92E732A74FE3ACEBE3A3472 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

关联代码界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/zTig5p6dRUGKeJ_bkbTurQ/zh-cn_image_0000002729540791.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D30C214DC393613E363E4E4259A143BC909175AE64BC7077920ED7E92AA3ABC "点击放大")

查看故障处源码步骤如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/U3--O09kSZOvp0s_wgmdDA/zh-cn_image_0000002699661568.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=24AF64314E40DAFEAF6C9E060DB244A6A3A5380EE0F54D96959686B24E7CA1ED "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

问题修复界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/xBmz1_BJRROoNTaQf1bZsQ/zh-cn_image_0000002729420841.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBCC4F86BF4B5F9EF1464A81A3E992955A8C553C1D8D2AE5E0AFDE98CAA20D32 "点击放大")
