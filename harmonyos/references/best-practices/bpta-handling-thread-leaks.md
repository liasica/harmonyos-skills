---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-thread-leaks
title: 运维态高效处理线程泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理线程泄漏
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:9d04a97e73a7d324685848f84740d14afb60a359f3d153b66d39c01d1f91f6ed
---

## 概述

线程泄漏是指程序在运行过程中，动态创建了线程，但没能正确释放或终止这些线程，导致线程数量持续增长。每个线程会占用一个线程栈，线程泄漏会导致内存泄漏。如果线程持续占用CPU，还会使CPU资源耗尽，最终导致应用前台闪退或系统查杀后台应用。本文主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行线程泄漏的监控、分析、定位与修复整套处理方法。

## 运维态线程泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/mk7rvwZlQS2oz0sTuN_oKw/zh-cn_image_0000002729540781.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E97B2FD92841EA652F7CCEB454F9563AEE5322A077B297EA48750369D5F97E3 "点击放大")

**排查步骤**

**1.故障预警配置**：在APMS平台配置线程泄漏监控告警规则，设置监控时段、频率和触发条件。

**2.问题发现与筛选**：通过故障预警或主动分析页面，筛选THREAD\_LEAK类型的泄漏问题。

**3.关键信息提取**：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级的问题。

**4.根因定位**：通过证据链、现场数据和创建线程调用栈，深入分析泄漏原因。

**5.修复与验证**：根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/SnOJsn8VQSu9DC5BI2bfLg/zh-cn_image_0000002699661556.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5C8DA2EC77841BE71F4F101BDA70206B1B89BC0EF5A33DB6DAA03EDD0534CF8 "点击放大")

**关键指标说明**

* **问题特征ID**：按照故障模块信息生成的哈希值。
* **故障模块**：发生泄漏的模块或组件，用于定位问题范围。
* **发生次数（占比）**：泄漏问题发生的频率，帮助判断问题严重程度。
* **影响设备数（占比）**：受影响的设备数量，评估问题影响面。
* **最大泄漏数**：单次泄漏的最大线程数量。

**故障详情页关键信息提取**

故障详情页如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/8ow9kewGQwOgkuYfBSBuFA/zh-cn_image_0000002729420829.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=616332680E3DF4CFBF157449DED1DDC45C51D8DC06D6B8A859EF3CD4D6431BFC "点击放大")

**证据链**

证据链列表包含以下诊断依据：

* Top 10泄漏线程：按泄漏数量从高到低排序；
* Top 10线程故障模块信息：按线程名称和堆栈聚合，展示对应调用栈帧，按调用频次排序；
* Profiler：呈现线程创建时的原始调用栈；

综合上述信息，将线程名、故障栈、创建栈与业务代码关联分析，可系统性地追溯线程泄漏的根本原因。

证据链列表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/AYEMeerARH62DPffJnaQ4w/zh-cn_image_0000002699821464.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF8CB4825A972F5AF7155AF076719752C587C0312FE8C143C6573C82E79D4C33 "点击放大")

**现场数据**

现场数据展示的是线程泄漏时线程内的调用栈，并按同名线程数量的大小排列。疑似泄漏点为数量最多的线程中最后调用的应用栈帧或非公共系统栈帧。非公共系统栈帧指系统框架层中非公共实现的函数调用帧，区别于无分析价值的公共系统基础栈帧。开发者可根据疑似泄漏点分析线程未退出的原因。

现场数据页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/PlihXdwGQkKb2ZGY97iPWw/zh-cn_image_0000002729540783.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FAE12DA4D339A8B87F230575E8EE1C8F68C493495E112909EF3E8E41E6D3AC8 "点击放大")

**创建线程调用栈信息**

创建线程调用栈信息中可查看创建线程的详细调用栈，通过分析泄漏线程创建时的调用栈信息，并关联业务代码进行综合诊断，可有效锁定导致泄漏的具体线程及其创建逻辑。

创建线程调用栈信息页面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Tv_bi6nDSPSaKilDjEoueQ/zh-cn_image_0000002699661558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=92F09C7D47E1620F5E6D2827D28B1D2A7EFF86A46FF82B6BBF6580E474BF6518 "点击放大")

## APMS平台线程泄漏分析案例

### APMS故障预警

可以在故障预警平台的故障告警页面新建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中线程泄漏对应的指标类型为THREAD\_LEAK（线程泄漏）。

故障预警配置界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/UiqAlqEPQFOW5ivUfAu53g/zh-cn_image_0000002729420831.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=4943C124F7241699E307C62E2E05FF477EA42180B884AF0C67185B6FEED5E379 "点击放大")

创建告警之后，故障触发后台会开始收集数据。当泄漏达到告警阈值后，会触发故障预警。

故障预警通知如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/aF-4-94JSTS9mIWcggQdNw/zh-cn_image_0000002699821466.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=C71435FCD7779C0CDAB709EC2969648C903B789D58DB72C2EDE5FAC318A4CF7C "点击放大")

### 问题查看与聚类

**聚类规则说明**

聚类规则请参考[线程泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#线程泄漏聚类规则)。

**Top问题查看**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为THREAD\_LEAK，单击查询按钮过滤出此应用的线程泄漏问题。

线程泄漏查询界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/KvCkOcelTH6U1SVrHVXy-w/zh-cn_image_0000002729540785.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BEAACB403D181B81E40EE98B29BAF38C2E5796C0BE9941ABAF31616CA6AB603 "点击放大")

在资源泄漏信息详情中，可查看当前应用的线程泄漏情况。

资源泄漏信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/4q6S19s_Q1KzYbNDXYavQg/zh-cn_image_0000002699661560.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=D127D6828C409F89B95DF0B8519F765AC13A5C7667A34D7DAF1C345E359D36E3 "点击放大")

### 根因定位与分析

**证据链分析**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、堆栈及优化建议，定位并修复问题代码。

经分析，本次泄漏核心为线程example.test（泄漏数量1002），关联模块libentry.so及方法LibuvAsyncStartLeakTask()应作为排查重点。

证据链详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/QtGP1A0SRtmGgopz18lxfg/zh-cn_image_0000002729420833.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7181ECD0DBAB0D7558375F256CD9736E492640CEBDDF11822338A74E1B7B64F "点击放大")

**现场数据分析**

现场数据按照线程名称和线程堆栈进行聚类并按线程数量的大小排序，进行堆栈还原（上传符号表将异常堆栈解析成源码对应的堆栈）后，开发者可根据疑似泄漏点定位到具体的代码行并结合代码分析线程未退出的原因。

现场数据详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/nkS-hwkQTXaPUe9hJut6wA/zh-cn_image_0000002699821468.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0596F08B02AE18DE6EB132B97EA1EEB53D4D41F607C73C9346CB02824B345AD5 "点击放大")

**创建线程调用栈信息分析**

创建线程调用栈信息是应用发生线程泄漏故障后，系统抓取创建线程的详细堆栈信息。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因，并进行修复。

创建线程调用栈信息详情如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/bXkSIigxRQ2gXHEYYn-7Yg/zh-cn_image_0000002729540787.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D03D37DF49A49C03278236CCD84BFC320452D5B9787B364F2A9756DD2B13BE3 "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

下钻分析界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/T9m60l5GTlyeBTpzOHZWKA/zh-cn_image_0000002699661562.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=30E7F67E42775D4F44A042A99C7150D75FB304727722A1A457FE6F38DDC15A3F "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/93nfwTt_TRChAjkSUS1JMA/zh-cn_image_0000002729420835.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=36750ECA4758B16BC3C5580B7DD13D421D634201468BF37C4BC661B74F4F81F3 "点击放大")

### 问题分析

**分析证据链**

证据链列表汇总了线程泄漏详情。开发者可依据泄漏线程、故障模块及Profiler信息，定位并修复问题代码。

Operation Analyzer证据链界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/720VQ1ZrReCGqOf2WD8_uQ/zh-cn_image_0000002699821470.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC48E120BAE613EE62DD7150FCFAA8212713B193ADE7BE42969386A8A80C499F "点击放大")

**分析现场数据**

现场数据按照线程名称和线程堆栈进行聚类，并按线程数量的大小排序，优先查看线程数量最多的线程堆栈。

现场数据界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/IfdB4xmYQrCSQVagKw4c2A/zh-cn_image_0000002729540789.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CA75D7A5329FD81CD475590E3DD0DBFE7905499F472C0395F89567F627BB282 "点击放大")

**分析创建线程调用栈**

创建线程调用栈信息是应用发生线程泄漏故障并达到一定条件后，系统抓取的堆栈信息，存在一定的滞后性。开发者可参考泄漏堆栈，进行堆栈还原后，结合代码分析具体的线程泄漏根因。

创建线程调用栈界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/9HPI6BYzR7WoV3nvfe3u3g/zh-cn_image_0000002699661564.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F42B887AB79539F4306D58CA4AD532614F681F52218749E3833A8C8B7F416C7 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

关联离线符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/BHsQfbatRPCm6AlWhN1HQQ/zh-cn_image_0000002729420837.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CEC2862147A6EFB04C753D81CEBA216BC69A7069DEE00A5A15390EDF85D5898 "点击放大")

上传符号表界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/pt7pbwGFQDehqlN-_e69Uw/zh-cn_image_0000002699821472.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=D97951A6338A687006E106C84AD9A27981777B54EE6AB3BF3DB86B3FC9BE757D "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

关联代码界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/NQV2tkGDQDq5CbZjVW8kkA/zh-cn_image_0000002729540791.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=E28799C1895BB47E604A35611D0FB0BF40E71F1937B0ADE402DEC36D53292A0D "点击放大")

查看故障处源码步骤如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/HAVk9TayTtaKNXnqKt4YQQ/zh-cn_image_0000002699661568.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B72C268177D82314D90092BB59BBC5AB83B3A9D14CC99E84706AF6045D5D69FB "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

问题修复界面如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/eS084hWTRsuPg087BT87vg/zh-cn_image_0000002729420841.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=29507AF667A495EF88F57DAB908C98557D83275559872710D5E6D2C209CD705F "点击放大")
