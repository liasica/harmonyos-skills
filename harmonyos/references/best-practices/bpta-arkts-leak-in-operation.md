---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-leak-in-operation
title: 运维态高效处理ArkTS泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理ArkTS泄漏
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:eb03825450d330281bbc132bf8f6c118f2a0ea5e2f8dee6c137ee61322f8bd74
---

## 概述

ArkTS泄漏是应用性能优化的重要问题，本文介绍在运维态下如何通过[应用质量管理（APMS）](../app/agc-help-apms-0000002235870062.md)平台进行ArkTS泄漏事件的标准化排查、分析、定位和修复闭环流程。

## 运维态ArkTS内存泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/sg1o7AycTz-NXNLoiHcOgA/zh-cn_image_0000002645091426.png "点击放大")

**排查步骤**

1. 故障预警配置：在APMS平台配置ArkTS泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题发现与筛选：通过故障预警或主动分析页面，筛选JS\_LEAK类型的泄漏问题。
3. 关键信息提取：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。
4. 根因定位：通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. 修复与验证：根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优先级的问题，并在问题状态和优先级这一栏做出标记，解决高优先级的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/HEHRveFbT2OtgDNPxNWRWQ/zh-cn_image_0000002644931514.png "点击放大")

关键指标说明如下：

* 问题特征ID：按照故障模块取的哈希值。

* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大对象数量。
* Retained Size：表示当垃圾回收该对象时，能释放的总内存大小（包括对象自身及其所有可达引用的对象）。

**故障详情页面介绍**

故障详情页面可以通过证据链和现场数据进一步深入分析泄漏的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/i8fI9xfDS1egq8kgZ4xFDQ/zh-cn_image_0000002675091223.png "点击放大")

**证据链**

证据链表格根据泄漏类型的大小，可以查看主泄漏对象和次泄漏对象，以及对象泄漏大小的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/O-IEnXzeQROh0vyM63xzZQ/zh-cn_image_0000002675011381.png "点击放大")

**持有链分布**

通过持有链可以查看各泄漏对象及其持有情况。一般来说应该从根节点入手，分析是否可以释放掉持有的子对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/GP2Tq_DBQU6Jf5-S2Ca0sg/zh-cn_image_0000002645091428.png "点击放大")

**现场数据分析**

现场数据是堆快照中TOP10的相同最短引用链的聚合情况。开发者可以通过现场快照分析最短引用链，也可以下载日志，结合日志进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/3-M0lWQWRaWjP9eW0fH2CA/zh-cn_image_0000002644931516.png "点击放大")

关键指标说明：

* Shortest Path To GCRoot：表示从垃圾回收根节点（GC Root）到目标对象的最短引用链。这条路径显示了对象为何无法被回收的最直接的引用关系，是定位内存泄漏的关键信息。
* Count：引用链数量。
* Shallow Size：表示该对象的实际大小，不包含其引用对象的大小。
* Shallow Size Ratio（%）：Shallow Size百分占比。
* Retained Size：表示Shallow Size的总大小加上因为此类对象而驻留（因此类对象引用而无法释放）的其他对象的总大小。
* Retained Size Ratio（%）：Retained Size百分占比。

## APMS平台ArkTS泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集](../harmonyos-guides/hiretrieval.md)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

可以在故障预警平台的告警规则页面新建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中ArkTS泄漏对应的指标类型为MEMORY\_LEAK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/iD1YiFEfRR-Cp5oHGsZ84Q/zh-cn_image_0000002675091225.png "点击放大")

创建告警之后，后台会开始收集数据。当泄漏达到告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/eH43HJX3S1-VRscd0Ar5yg/zh-cn_image_0000002675011383.png "点击放大")

通过操作查看选项可以跳转到故障指标页面查看故障详情。也可以在故障分析页面通过泄漏类型、应用版本等相关信息筛选出对应的泄漏信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/19VNXELMR_29fDX6jgk4dQ/zh-cn_image_0000002645091430.png "点击放大")

### 问题查看与聚类

**聚类规则说明**

聚类规则主要分为三种：名称聚类，引用链聚类和属性聚类。不同类型的对象需要使用不同的聚类方法。具体的聚类规则可以参考[JS泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#js泄漏聚类规则)。

**问题查看**

* TOP问题查看

  1. 通过故障预警的指引，在故障分析页面筛选出JS\_LEAK的泄漏类型。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/qgCKuFuNRoK2Xts6FPewcw/zh-cn_image_0000002644931518.png "点击放大")

  2. 开发者需要关注页面的故障模块，发生次数和最大泄漏数量。如果泄漏对象是开发者自定义对象，可以通过故障模块，确认自定义对象的位置，进一步缩小排查范围。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/XMUctfAsSLuxzUTDxYyItQ/zh-cn_image_0000002675091227.png "点击放大")

  3. 开发者可在问题状态、优先级、问题备注内填写信息，结合故障模块、异常发生占比与实际业务场景，筛选高优先级问题并完成标注。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/TpIzhgw2RAuiF7BQFZf-uA/zh-cn_image_0000002675011385.png "点击放大")

  4. 点击操作列的查看按钮，即可查看泄漏对象完整故障详情，进一步确认泄漏对象。
* TOP ArkTS泄漏对象聚合

  平台会根据ArkTS泄漏对象的类型做聚合，开发者通过这个页签，可以查看泄漏对象的对象信息、对象总次数、出现快照数、最大Retained Size和平均Retained Size等数据。

  当泄漏的对象为开发者自定义对象时，对象信息会显示出对应的对象名称，开发者可以通过名称找到业务代码中泄漏的对象，并优化相关代码。点击查看按钮可以查看当前泄漏对象故障详情，进一步确认泄漏对象。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/4RzJfUkuRp6GeqLOOahfkw/zh-cn_image_0000002645091432.png "点击放大")

### 根因定位与分析

通过TOP问题页签的查看操作或者点击ArkTS泄漏对象聚合页签查看个例按钮，可以跳转到泄漏故障详情页面。故障详情页面提供了证据链和现场数据等信息，帮助开发者定位到问题根因。

**证据链分析**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/P84OPbi-S_ijf_WXze-Arw/zh-cn_image_0000002644931520.png "点击放大")

* 主泄漏对象：泄漏问题中Retained Size占比最大的对象，主泄漏对象展示了泄漏对象的名称，Retained Size的大小，占总Retained Size的百分比以及存在实例个数。
* 次泄漏对象：泄漏问题中Retained Size占比最大之外的其他对象。
* 持有链分布：从GC Root到对象的引用路径，显示哪些对象持有该对象的引用。
* 持有链分布详情：泄漏对象的持有链详细信息。包含对象名称，数量，对象的实际大小，以及引用链关联的对象。

**现场数据分析**

以下是堆快照中TOP10的相同最短引用链的聚合情况，如果证据链中的泄漏信息不足以支持定位，可以查看最短引用链进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/3QzU-GHwS_qhhhB8wt4h_A/zh-cn_image_0000002675091229.png "点击放大")

**下钻分析**

下钻分析是指从宏观汇总数据，逐层点进来看更细的明细数据，用来定位问题、找到原因。平台会根据当前问题的故障特征ID，进行筛选，并展示应用版本TOP5、系统版本TOP5、设备型号TOP5这三个维度的信息，帮助开发者进一步缩小版本排查范围。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/62gypYi6SROTs3w14Gc-Fg/zh-cn_image_0000002675011387.png "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/2zHKxGrdTviTNu9Eyrskbw/zh-cn_image_0000002645091434.png "点击放大")

如需修改global handle，请参考[开发态快速定位ArkTS泄漏](bpta-arkts-leak-in-develop.md)。

**修复建议与闭环**

* **问题修改**

  开发者根据修改建议，在工程中优化掉主要的泄漏对象。
* **问题标记**

  优化之后，可以在分析页面对泄漏对象进行标记。
* **应用发布**

  应用发布之后，更新平台告警规则，并持续关注新版本的崩溃数据。对比修复前后的问题发生率，确认修复是否有效。

**故障模式库**

故障模式库中会收录常见的ArkTS泄漏事件，针对不同的ArkTS泄漏事件提供最佳实践和修复方案，并提供案例库，收录ArkTS泄漏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer 插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者在DevEco Studio上也可以使用相同的方式分析运维态的泄漏问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在Tool Windows栏的Operation Analyzer进入平台，点击后根据包名选择应用，再点击资源泄漏（Resource Leak）即可查看该类故障相关数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/WoyAAY4_R-6pR80eKWXJ_Q/zh-cn_image_0000002644931524.png "点击放大")

### 问题分析

**分析证据链**

数据和流程同[根因定位与分析](bpta-arkts-leak-in-operation.md#section1831731688)流程一致，开发者可查看故障分析与修复建议以排查问题，具体操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/eEU9RU51R2CzZuwZLb1s3w/zh-cn_image_0000002675091231.png "点击放大")

**分析现场数据**

数据和流程同[根因定位与分析](bpta-arkts-leak-in-operation.md#section1831731688)流程一致，具体操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/XJN5uHEnS32h_2Ulo1Dnnw/zh-cn_image_0000002675011389.png "点击放大")
