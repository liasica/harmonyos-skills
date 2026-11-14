---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-leak-in-operation
title: 运维态高效处理ArkTS泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理ArkTS泄漏
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:dd141e161386dcb9b569ccfc5f71e6b72915b36a3af802a735bf94b079c1a87a
---

## 概述

ArkTS泄漏是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行ArkTS泄漏事件的标准化排查、分析、定位和修复闭环流程。

## 运维态ArkTS内存泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/AV0lwGYZSXu43Km8K6gEhA/zh-cn_image_0000002645091426.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA61D84F67C263EF91DF884524D06A3706CCE798954983DB4A633BB6726F8845 "点击放大")

**排查步骤**

1. 故障预警配置：在APMS平台配置ArkTS泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题发现与筛选：通过故障预警或主动分析页面，筛选JS\_LEAK类型的泄漏问题。
3. 关键信息提取：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。
4. 根因定位：通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. 修复与验证：根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优先级的问题，并在问题状态和优先级这一栏做出标记，解决高优先级的问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/uLcG-2JuQc6JcxfWfLORoA/zh-cn_image_0000002644931514.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=28192A0B9EE50B3E2A1BD4A5DDEB47E1DD5A1035D50722AEB7E7C0CEC7A3BBD3 "点击放大")

关键指标说明如下：

* 问题特征ID：按照故障模块取的哈希值。

* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大对象数量。
* Retained Size：表示当垃圾回收该对象时，能释放的总内存大小（包括对象自身及其所有可达引用的对象）。

**故障详情页面介绍**

故障详情页面可以通过证据链和现场数据进一步深入分析泄漏的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/XDvLBAEMRcKrWmUFOKwcGw/zh-cn_image_0000002675091223.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=1014991EFF77E622170DB03A7E663E496BF28F7EC6F0615CF556C52B198A0CB8 "点击放大")

**证据链**

证据链表格根据泄漏类型的大小，可以查看主泄漏对象和次泄漏对象，以及对象泄漏大小的占比。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/F0OJfzNXTSCXTHmz9xuNFw/zh-cn_image_0000002675011381.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=753E3B290A8C2A59B6536207F5C9A4E71221E70681386B892688D33F6BB434F6 "点击放大")

**持有链分布**

通过持有链可以查看各泄漏对象及其持有情况。一般来说应该从根节点入手，分析是否可以释放掉持有的子对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/z1TibG1ITR2K0OzA4kjIpA/zh-cn_image_0000002645091428.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FCB65503F02FD29F6A96641A68BC1E9337A31EE40F8E5CBBED5FCBD9B04A058 "点击放大")

**现场数据分析**

现场数据是堆快照中TOP10的相同最短引用链的聚合情况。开发者可以通过现场快照分析最短引用链，也可以下载日志，结合日志进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/FQAfSwrASD-cnXmNHuCBrA/zh-cn_image_0000002644931516.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EB442F3D4524C21EF0DC43C698D0C7E6ACA5BB9400715751A9FCCCC0F75C4E1 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/LFkjN5dAQUKXvyDHq4E2Pg/zh-cn_image_0000002675091225.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=214480CE995357036267E9E4AC6B103779FD760726AA87FE00BFEEAF9D50DA24 "点击放大")

创建告警之后，后台会开始收集数据。当泄漏达到告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/htzsBYLYSPWM2x1MAsh12A/zh-cn_image_0000002675011383.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5616924FF245F4C466937E2868E2A2954A8B97A06F8CC1937ABDA7F71F4BEB5 "点击放大")

通过操作查看选项可以跳转到故障指标页面查看故障详情。也可以在故障分析页面通过泄漏类型、应用版本等相关信息筛选出对应的泄漏信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VQQbFNbAS_-r7oWlMlIEqQ/zh-cn_image_0000002645091430.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BB34987EA1F4AE4F43A882E6DACDA7EA740BE65336FD8F2429CF5B07CC50E84 "点击放大")

### 问题查看与聚类

**聚类规则说明**

聚类规则主要分为三种：名称聚类、引用链聚类和属性聚类。不同类型的对象需要使用不同的聚类方法。具体的聚类规则可以参考[JS泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#js泄漏聚类规则)。

**问题查看**

* TOP问题查看

  1. 通过故障预警的指引，在故障分析页面筛选出JS\_LEAK的泄漏类型。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/IpnZJ0IPSlyQOqRh4WhfLQ/zh-cn_image_0000002644931518.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E6B1647ADE510478E6BAAEA21FD344318B985C98DDF5BD6B6DD7FAE76AE7975 "点击放大")

  2. 开发者需要关注页面的故障模块、发生次数和最大泄漏数量。如果泄漏对象是开发者自定义对象，可以通过故障模块，确认自定义对象的位置，进一步缩小排查范围。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0Ol8jq_yTtysLo7orHFz5w/zh-cn_image_0000002675091227.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=91821A5A98831B6B133466F151F33226145A4D707C530100BF08D1434E57EF40 "点击放大")

  3. 开发者可在问题状态、优先级、问题备注内填写信息，结合故障模块、异常发生占比与实际业务场景，筛选高优先级问题并完成标注。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/LqksBznGRYuGt9SlFNITLA/zh-cn_image_0000002675011385.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5525BF30C9B66232BD851E6D9D98FB7ADD6E346EB8E548553D9F4DD72DDD2592 "点击放大")

  4. 点击操作列的查看按钮，即可查看泄漏对象完整故障详情，进一步确认泄漏对象。
* TOP ArkTS泄漏对象聚合

  平台会根据ArkTS泄漏对象的类型做聚合，开发者通过这个页签，可以查看泄漏对象的对象信息、对象总次数、出现快照数、最大Retained Size和平均Retained Size等数据。

  当泄漏的对象为开发者自定义对象时，对象信息会显示出对应的对象名称，开发者可以通过名称找到业务代码中泄漏的对象，并优化相关代码。点击查看按钮可以查看当前泄漏对象故障详情，进一步确认泄漏对象。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/RxZrk3YgRsendat-E-1I_A/zh-cn_image_0000002645091432.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=138A63792C437E2DDF7B2C1DF09C13CD816DD03A8FA032EC50FF6CE10C2C8BDB "点击放大")

### 根因定位与分析

通过TOP问题页签的查看操作或者点击ArkTS泄漏对象聚合页签查看个例按钮，可以跳转到泄漏故障详情页面。故障详情页面提供了证据链和现场数据等信息，帮助开发者定位到问题根因。

**证据链分析**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/W9ojMZC-SCWN4hV0heX7xw/zh-cn_image_0000002644931520.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=70A4E58877F61DF80C638E76B393424947D77E1EF1E7F1E18B71A4E2D68A3A0C "点击放大")

* 主泄漏对象：泄漏问题中Retained Size占比最大的对象，主泄漏对象展示了泄漏对象的名称、Retained Size的大小、占总Retained Size的百分比以及存在实例个数。
* 次泄漏对象：泄漏问题中Retained Size占比最大之外的其他对象。
* 持有链分布：从GC Root到对象的引用路径，显示哪些对象持有该对象的引用。
* 持有链分布详情：泄漏对象的持有链详细信息。包含对象名称、数量、对象的实际大小、以及引用链关联的对象。

**现场数据分析**

以下是堆快照中TOP10的相同最短引用链的聚合情况，如果证据链中的泄漏信息不足以支持定位，可以查看最短引用链进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ZjIzklMjQj2l-W00htXINA/zh-cn_image_0000002675091229.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=24BB1CBF574A7DEE6E866755B6DD7931621F2E700D4BE3085CCFC2441BA95553 "点击放大")

**下钻分析**

下钻分析是指从宏观汇总数据，逐层点进来看更细的明细数据，用来定位问题、找到原因。平台会根据当前问题的故障特征ID，进行筛选，并展示应用版本TOP5、系统版本TOP5、设备型号TOP5这三个维度的信息，帮助开发者进一步缩小版本排查范围。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/sFI85wjkRF-FW-eVjiQTEw/zh-cn_image_0000002675011387.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B65595DB7D68EB72EA7F5BEF20D2DB70A2A2E1BAE3B688EAA2D16439B85E19BD "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/E3E9xc71RfyOrM4pswIEPA/zh-cn_image_0000002645091434.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=084AC2B4D6E85E498CCB8E9FD1B0CD7B97BF15999DE145D6D5A353E6151DB3C1 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/8yfW7lLARVijPb-p7_cQtw/zh-cn_image_0000002644931524.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=305EB8458BB475998A29FCCA02E05DC08B4505D06CD262184CE734817D683E5E "点击放大")

### 问题分析

**分析证据链**

数据和流程同[根因定位与分析](bpta-arkts-leak-in-operation.md#section1831731688)流程一致，开发者可查看故障分析与修复建议以排查问题，具体操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/zk5TQdFBTQu8YL9CWFknFg/zh-cn_image_0000002675091231.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E44B232532D1B80EC220EE0C97C020456CE979AD79D5B397F030767EAB8DD4C8 "点击放大")

**分析现场数据**

数据和流程同[根因定位与分析](bpta-arkts-leak-in-operation.md#section1831731688)流程一致，具体操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/AEyarS2QSDOJhCX6fYOjtA/zh-cn_image_0000002675011389.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=34BDA89A556086B1F3AD54FF3A4BCFC9D5288F708B28B9C3E15CA7433DA60352 "点击放大")
