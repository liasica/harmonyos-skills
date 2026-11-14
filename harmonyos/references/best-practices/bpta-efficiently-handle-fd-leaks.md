---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-efficiently-handle-fd-leaks
title: 运维态高效处理FD资源泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理FD资源泄漏
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:c9dce087e829d6aedee6f2325ee0a7f6484fae19e4b2435488a8f4c819a816c7
---

## 概述

FD（全称：File Descriptor，文件描述符）资源泄漏是一种比较常见的泄漏类型，也是应用稳定性优化的重要问题。本文档主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行FD资源泄漏的监控、分析、定位与修复整套处理方法。

## 运维态FD资源泄漏分析流程

### 标准化排查流程

**整体流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/FbyFdJRkQMCs2auNQCmRxA/zh-cn_image_0000002671650762.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1000780EDDBF21C2B28BCFD469FE46CC1757E6F641201DFD8AFBF88E4DB905E "点击放大")

**排查步骤**

1. **故障预警配置：**在APMS平台配置FD泄漏监控告警规则，设置监控时段、频率和触发条件。
2. **问题发现与筛选：**通过故障预警或主动分析页面，筛选FD\_LEAK类型的泄漏问题。
3. **关键信息提取****：**分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。
4. **根因定位****：**通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. **修复与验证：**根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

如下图所示，页面入口：故障分析->资源泄漏->资源泄漏信息详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/IpSEBX1RRJ6Uv-bD6R0f2Q/zh-cn_image_0000002701370585.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A98DF9A2AF5D35A68F9A2F400A3817952FABAC089870607FE1733C1D7776951 "点击放大")

**关键指标说明**

* 问题特征ID：故障模块的哈希值，同类故障模块会聚类到一起。
* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大句柄数。

**故障详情页面介绍**

通过点击查看按钮，进入到故障详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ep_qENugR7-BoypGGrsdOw/zh-cn_image_0000002701250493.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=42B0C0C733A00B2D4DD8A888F44A0F86C933C967D02F5490ADDE5CC7AF87EAA9 "点击放大")

故障详情页面可以通过证据链、现场数据、句柄栈信息进一步深入分析泄漏的原因。

**证据链**

证据链列表根据泄漏数量的大小排序，优先查看泄漏数量最大的句柄名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/fSzmujh-TG61PyigEZjjaQ/zh-cn_image_0000002671490912.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=238613E76091AF521F516A9F2C36391EC6AE69A4C409E25B2844691638F9CEB8 "点击放大")

**现场数据**

现场数据展示了当前FD泄漏的Top10的句柄名称，可结合代码、日志分析对应的FD泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/vNwSqj8hT7m3ODX9Hgqvew/zh-cn_image_0000002671650764.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E004B182706785781422E97ADF86D475ADA196AD4B8978249AC15A192E6A8D85 "点击放大")

**句柄栈信息**

句柄栈信息中可查看对应的堆栈信息，以及疑似泄漏点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/IX4h15Q8QEmAqZuFWT1FXA/zh-cn_image_0000002701370587.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2E57299E8872F0B5EBD29DE849D0E670A3A86071215323C63AD42D23F373DC2 "点击放大")

## APMS平台FD泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度采集功能（可参考：[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)）后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

在故障预警平台的告警规则页面新建FD泄漏告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中FD泄漏对应的指标类型为FD\_LEAK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/g-ReZ7F_RzeLEbxjuyIm8Q/zh-cn_image_0000002701250495.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=154D8D10403F651BF0731B6388800F57DD96504A7928219F55AFCD099E56DE1F "点击放大")

创建告警之后，后台会开始收集数据。当达到设置的告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Cw_-u7wUQcSVjmrO2fUszA/zh-cn_image_0000002671490914.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AC2DD20AC2D3282D55597C3FC9EEB0E7DEF96F6571E91D037F1D2738EBEBDE2 "点击放大")

### 问题查看与聚类

**聚类规则说明**

FD资源泄漏聚类规则请参考[句柄泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏聚类规则)。

**问题查看**

* **Top问题查看**

通过故障告警的指引，在故障分析页面筛选出FD\_LEAK的泄漏类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/_ppj7X3-SA2LFv1cAdpMIA/zh-cn_image_0000002671650774.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A4C46B812516B1E439509A3C5C7B1C2AC799B58F9181E7F33ED6670DFB824FF "点击放大")

点击查看按钮，即可跳转到Top问题查看页签下的FD资源泄漏问题列表。

* **资源泄漏信息详情Top问题**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为FD\_LEAK，点击查询按钮，过滤出此应用的FD资源泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/SK1YVb_nQBqPDcvaaTUiZg/zh-cn_image_0000002701370625.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DB8E5E8977000AD183A023C2087C7D369409106B727918CFBE6935BA10D2539 "点击放大")

在资源泄漏信息详情中，可查看当前应用的FD资源泄漏情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/QbIThFVHQkGiLXyFflDPNA/zh-cn_image_0000002701250559.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B27457DC9C3455C4B9F78CEB3338BDE03DAD67E0D0982C55A146B1EA94EA4064 "点击放大")

### 根因定位与分析

过滤出FD资源泄漏故障列表后，点击查看按钮，进入到问题个例分析详情页，可查看当前故障的分析报告，包含故障发生时间、泄漏句柄、故障模块、版本信息以及修复建议等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/ZMQqMq68Tuy4eYKGqs5XSQ/zh-cn_image_0000002671490976.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=A901622AE1F8491F457FB5570D85B7B1EE87F4E7CB6F79762B9B7E7CEC208ADB "点击放大")

**证据链分析**

证据链列表中按照泄漏数量倒序排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。同时提供了日志下载功能，便于进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/zOWGCAKnQbqS8EGQwyskww/zh-cn_image_0000002671650846.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C8C5251B671679B43A7BA2149B880909BC3FA325807E792970FFD2708812389 "点击放大")

**现场数据分析**

现场数据页中，将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/wpaFSRoORuSJMRK58q5v-g/zh-cn_image_0000002701370681.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=37FB562C7614ACEE2AEC539EDDC4306201525E62C0CA2703BE4A7B01F7280753 "点击放大")

**句柄栈信息****分析**

句柄栈信息是发生FD泄漏故障并达到一定条件后，系统从堆栈中抓取的堆栈信息，存在一定的滞后性。开发者可参考堆栈中的疑似泄漏点，进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/t20M6DoSRkKLk0gMZra4HA/zh-cn_image_0000002701250593.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3E249218009D4723058D7169202B23FF3AEA203A59C53E6B90E36BF5E49ECEF "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选Top应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/6r8KQPDHSXKcpSg4qvN3GA/zh-cn_image_0000002671491006.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9281F1D898C823868D4FD17453A877455D5241C2AC613C33743EA2F96CBA8ABF "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/jRvgPLUhTMG2mBH9GzEVAg/zh-cn_image_0000002671650858.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=50FA86942CACB4277ECB05ACDEFF1FB5A5372333CB32AD647481798546CD9AA0 "点击放大")

**问题修复与闭环**

* **问题修改**

开发者根据修改建议，在工程中释放FD泄漏对象。

* **问题标记**

优化之后，可以在分析页面对对应的FD泄漏对象标记。

* **应用发布**

应用发布之后，更新平台告警规则，并持续关注新版本的FD资源泄漏数据。对比修复前后的问题发生率，确认修复是否有效。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件，通过该插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者使用该插件以相同的方式分析运维态的泄漏问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在Tool Windows栏的Operation Analyzer进入平台，点击后根据包名选择应用，再点击资源泄漏（Resource Leak）即可查看该类故障相关数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/36Q0GjW0Q6ygBD_O7iWJLw/zh-cn_image_0000002701370683.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBDDAEAC9296EC36824DC78AC7B7A8FC79D5BCEA0A4FFFDE1E273857884D5B41 "点击放大")

### 问题分析

**证据链****分析**

证据链列表中按照泄漏数量排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/cqgzHJoCRka4R7rTakpxzQ/zh-cn_image_0000002701250595.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1BC2013212A3BA08CF0D63946710DD701A73F402A77A95A7D7058A428723592 "点击放大")

**现场数据****分析**

现场数据页面将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/PsemXEFLRrKGo2AKKdlgKw/zh-cn_image_0000002671491008.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C4465317E5F66ABDFE083BFEB521B3622A7FA4193C10D2510B762DB77EC535E "点击放大")

**句柄栈****信息****分析**

句柄栈信息中将抓取的堆栈信息中疑似泄漏点进行展示，开发者进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/d5rDLpI9S_GaPgbRFSz3sQ/zh-cn_image_0000002671650860.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD8297DCA2CCE25316B1DE5E6B8A42135C36A02D107254981149762A01080B1E "点击放大")
