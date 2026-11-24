---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-thread-leaks
title: 运维态高效处理线程泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理线程泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:b949a77ffcb0e61f7c76e30e202a5c7d911a6a23d4be7757a023256e01ae854f
---

## 概述

线程泄漏是指程序在运行过程中，动态创建了线程，但没能正确释放或终止这些线程，导致线程数量持续增长。每个线程会占用一个线程栈，线程泄漏会导致内存泄漏。如果线程持续占用CPU，还会使CPU资源耗尽，最终导致应用前台闪退或系统查杀后台应用。本文主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行线程泄漏的监控、分析、定位与修复整套处理方法。

## 运维态线程泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/IZGcljtQShafmiav9TAueg/zh-cn_image_0000002729540781.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=76FC01B3E193FDC9BCEA5ABD41C6759951CFB168B8664E0A08BC78543AB2E4A0 "点击放大")

**排查步骤**

**1.故障预警配置**：在APMS平台配置线程泄漏监控告警规则，设置监控时段、频率和触发条件。

**2.问题发现与筛选**：通过故障预警或主动分析页面，筛选THREAD\_LEAK类型的泄漏问题。

**3.关键信息提取**：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级的问题。

**4.根因定位**：通过证据链、现场数据和创建线程调用栈，深入分析泄漏原因。

**5.修复与验证**：根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/_97Xwc4EQruveICspdsMGw/zh-cn_image_0000002699661556.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=EAAC021372DAEE45FBEB89F69B8D937874A45EE382A8C1C67806722EBE963951 "点击放大")

**关键指标说明**

* **问题特征ID**：按照故障模块信息生成的哈希值。
* **故障模块**：发生泄漏的模块或组件，用于定位问题范围。
* **发生次数（占比）**：泄漏问题发生的频率，帮助判断问题严重程度。
* **影响设备数（占比）**：受影响的设备数量，评估问题影响面。
* **最大泄漏数**：单次泄漏的最大线程数量。

**故障详情页关键信息提取**

故障详情页如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/qeYhJM3MTP-R9ltq6F24rg/zh-cn_image_0000002729420829.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BC29CF1E1EFED69413C278EC03331C9B6219BAB1B2E856BEB0A42D66A55EF11 "点击放大")

**证据链**

证据链列表包含以下诊断依据：

* Top 10泄漏线程：按泄漏数量从高到低排序；
* Top 10线程故障模块信息：按线程名称和堆栈聚合，展示对应调用栈帧，按调用频次排序；
* Profiler：呈现线程创建时的原始调用栈；

综合上述信息，将线程名、故障栈、创建栈与业务代码关联分析，可系统性地追溯线程泄漏的根本原因。

证据链列表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/98CInmsMSp-vYBUkLbs71w/zh-cn_image_0000002699821464.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=006D76819BCF3BF25F8111DB7F2B5E0517537716244A348B230D4214A677414E "点击放大")

**现场数据**

现场数据展示的是线程泄漏时线程内的调用栈，并按同名线程数量的大小排列。疑似泄漏点为数量最多的线程中最后调用的应用栈帧或非公共系统栈帧。非公共系统栈帧指系统框架层中非公共实现的函数调用帧，区别于无分析价值的公共系统基础栈帧。开发者可根据疑似泄漏点分析线程未退出的原因。

现场数据页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/dS57c8PXTaOyjpvSJyRbRA/zh-cn_image_0000002729540783.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A1AB81B978AB08D18D0C493DB6F18CBE5856DA1D1DC3ACD24FAC9228CECE5A "点击放大")

**创建线程调用栈信息**

创建线程调用栈信息中可查看创建线程的详细调用栈，通过分析泄漏线程创建时的调用栈信息，并关联业务代码进行综合诊断，可有效锁定导致泄漏的具体线程及其创建逻辑。

创建线程调用栈信息页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/q2LPHaUlTz-TsAfS6CGH3Q/zh-cn_image_0000002699661558.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7F00B02DB0C5E4173ADBB225262BFF990DCC19BB76EBB1326330621CCBDDB6F "点击放大")

## APMS平台线程泄漏分析案例

### APMS故障预警

可以在故障预警平台的故障告警页面新建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中线程泄漏对应的指标类型为THREAD\_LEAK（线程泄漏）。

故障预警配置界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Y5adoN4PSlOzFu4HshNNhQ/zh-cn_image_0000002729420831.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=6557C7DFB16408BA657CA221733FD79B2DA2F84919F54FB179C1C04DA83D028F "点击放大")

创建告警之后，故障触发后台会开始收集数据。当泄漏达到告警阈值后，会触发故障预警。

故障预警通知如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ha0c-LsDS8G5zjVaYX3DQw/zh-cn_image_0000002699821466.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DE50B4E1F58CB26B448CC6E3CB7AD973957453ECA29F04A449C0A01F565176E "点击放大")

### 问题查看与聚类

**聚类规则说明**

聚类规则请参考[线程泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#线程泄漏聚类规则)。

**Top问题查看**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为THREAD\_LEAK，单击查询按钮过滤出此应用的线程泄漏问题。

线程泄漏查询界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/7j60Xx6uR_C2Ct28j7K6SA/zh-cn_image_0000002729540785.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C68268198B96C39443F5088FF57322ED219B22219700768A82430C7300BB8AD1 "点击放大")

在资源泄漏信息详情中，可查看当前应用的线程泄漏情况。

资源泄漏信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Eub7-aHDRy-Ksx6HJJFDVw/zh-cn_image_0000002699661560.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=55F5E3799BA37CFEE87FE006D7212355006151B840014E6AC3D38727B6D7D5D5 "点击放大")

### 根因定位与分析

**证据链分析**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、堆栈及优化建议，定位并修复问题代码。

经分析，本次泄漏核心为线程example.test（泄漏数量1002），关联模块libentry.so及方法LibuvAsyncStartLeakTask()应作为排查重点。

证据链详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/YHft-eAtTZi4ziZVjQDnyg/zh-cn_image_0000002729420833.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C8F89090DC1D80240820D999EC5EB2BA96C445837F0D328B3B3AB36231A1440 "点击放大")

**现场数据分析**

现场数据按照线程名称和线程堆栈进行聚类并按线程数量的大小排序，进行堆栈还原（上传符号表将异常堆栈解析成源码对应的堆栈）后，开发者可根据疑似泄漏点定位到具体的代码行并结合代码分析线程未退出的原因。

现场数据详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/OZX-fL6QRmmPvaiRaOyPtQ/zh-cn_image_0000002699821468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=68FC9B94AA052BB26E8D979FEE10CA02FE05036048D51DCD0131339A5297B020 "点击放大")

**创建线程调用栈信息分析**

创建线程调用栈信息是应用发生线程泄漏故障后，系统抓取创建线程的详细堆栈信息。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因，并进行修复。

创建线程调用栈信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/G2UnLCP6T1ypUoNvkQf7XQ/zh-cn_image_0000002729540787.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=697605E86DDEFA3D09D0E75D69136C44064803A4AF18E47A5C70E20F9EEACD7D "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

下钻分析界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/wVrTBYTBTyS49B08v4nqnQ/zh-cn_image_0000002699661562.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2975276D8FD49DBB337EC66F604AF4B903A32DD4B63E5806FCBCAE0EFEA90D14 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/1A4zElMiRzCNuMbw6a7KSg/zh-cn_image_0000002729420835.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=28747A0661F740E9993E8A41FF6D22007FC9706D9E206BAB7EFA272D6F93EEEA "点击放大")

### 问题分析

**分析证据链**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、故障模块及Profiler信息，定位并修复问题代码。

Operation Analyzer证据链界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/j-904IiuT4uOEgGzcB4LjQ/zh-cn_image_0000002699821470.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D86A8512F227D3F400DD876F9145B2DCF4DBC202EBA5542DE34F09BC6F05C4DA "点击放大")

**分析现场数据**

现场数据按照线程名称和线程堆栈进行聚类，并按线程数量的大小排序，优先查看线程数量最多的线程堆栈。

现场数据界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/9cVdLPnSReit7OB5ug2oZw/zh-cn_image_0000002729540789.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD36D3C7F85526017CCFD409E3B45EA1803ACBCDE2B3917849C1FB0FAB08E8B9 "点击放大")

**分析创建线程调用栈**

创建线程调用栈信息是应用发生线程泄漏故障并达到一定条件后，系统抓取的堆栈信息，存在一定的滞后性。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因。

创建线程调用栈界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/LGQrefAKSZKFyQQwTq4JCw/zh-cn_image_0000002699661564.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF5AF7AF425FC38A61FC56387511874A91917AC319ACA2BA7AE661F5BC691962 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

关联离线符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/-7JjUNjiQsKAiQ2cAsTEMQ/zh-cn_image_0000002729420837.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A01ED386EB6A816EEF61CEA05A5723397C2FB4429CCF1BB860E3943F97455936 "点击放大")

上传符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/C_hPteLXSGSnlFmOLuQ8nA/zh-cn_image_0000002699821472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D804CE165A9A2234422916812062DF183C63A530B52AE7A640D9BD6897123B9 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

关联代码界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/2py88R6AT5-rGaoSMCl6_w/zh-cn_image_0000002729540791.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B6607DF170F799DB2E917A00B43CE47D555A4D26617119A350487DC829E523D "点击放大")

查看故障处源码步骤如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/sW-Yi_N8Se2U9_2RACvWqA/zh-cn_image_0000002699661568.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ADCB58EC7EC4DBACFC3725C910FE8D27E31CF04FF26D65B85BC69C69C981758 "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

问题修复界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/OvyiOMMuTcqQGmuVEXj5JA/zh-cn_image_0000002729420841.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0617CEF9E9689C14360BBD544C41D2E7EB434C91363486DFF2E1A1FFB570A8B "点击放大")
