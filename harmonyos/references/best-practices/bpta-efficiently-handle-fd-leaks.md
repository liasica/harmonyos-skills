---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-efficiently-handle-fd-leaks
title: 运维态高效处理FD资源泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理FD资源泄漏
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-08-10
content_hash: sha256:224aeaff18a10c5fb4b18b3a152e5ba9c9324c257fbfe1cebd361084effb181b
---

## 概述

FD（全称：File Descriptor，文件描述符）资源泄漏是一种比较常见的泄漏类型，也是应用稳定性优化的重要问题。本文档主要介绍在运维态下如何通过[应用质量管理（APMS）](../app/agc-help-apms-0000002235870062.md)平台进行FD资源泄漏的监控、分析、定位与修复整套处理方法。

## 运维态FD资源泄漏分析流程

### 标准化排查流程

**整体流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ZzI6Fl52QSScZdcSIX71iA/zh-cn_image_0000002671650762.png "点击放大")

**排查步骤**

1. **故障预警配置：**在APMS平台配置FD泄漏监控告警规则，设置监控时段、频率和触发条件。
2. **问题发现与筛选：**通过故障预警或主动分析页面，筛选FD\_LEAK类型的泄漏问题。
3. **关键信息提取**：分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。
4. **根因定位**：通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. **修复与验证：**根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

如下图所示，页面入口：故障分析->资源泄漏->资源泄漏信息详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/jE2LAxdxQTSz9h9TKyfuBw/zh-cn_image_0000002701370585.png "点击放大")

**关键指标说明**

* 问题特征ID：故障模块的哈希值，同类故障模块会聚类到一起。

* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大句柄数。

**故障详情页面介绍**

通过点击查看按钮，进入到故障详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/kwN-9-YPTMepu7Vltsz9Jw/zh-cn_image_0000002701250493.png "点击放大")

故障详情页面可以通过证据链、现场数据、句柄栈信息进一步深入分析泄漏的原因。

**证据链**

证据链列表根据泄漏数量的大小排序，优先查看泄漏数量最大的句柄名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/DHVqH5BdQ1iyAjJfmBVOuA/zh-cn_image_0000002671490912.png "点击放大")

**现场数据**

现场数据展示了当前FD泄漏的Top10的句柄名称，可结合代码、日志分析对应的FD泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/alBkg_E5TAGf3T_R5JqatQ/zh-cn_image_0000002671650764.png "点击放大")

**句柄栈信息**

句柄栈信息中可查看对应的堆栈信息，以及疑似泄漏点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/wW7hX-M4Q6CrjmWXGPyFLg/zh-cn_image_0000002701370587.png "点击放大")

## APMS平台FD泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度采集功能（可参考：[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)）后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

在故障预警平台的告警规则页面新建FD泄漏告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中FD泄漏对应的指标类型为FD\_LEAK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/TSKaYfoXQNCEBxdM5mb7Mw/zh-cn_image_0000002701250495.png "点击放大")

创建告警之后，后台会开始收集数据。当达到设置的告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/kShDmDllTsSwEi8p8llVFg/zh-cn_image_0000002671490914.png "点击放大")

### 问题查看与聚类

**聚类规则说明**

FD资源泄漏聚类规则请参考[句柄泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏聚类规则)。

**问题查看**

* **Top问题查看**

通过故障告警的指引，在故障分析页面筛选出FD\_LEAK的泄漏类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/X6G9KzNmRRO7ozl5K1fcGw/zh-cn_image_0000002671650774.png "点击放大")

点击查看按钮，即可跳转到Top问题查看页签下的FD资源泄漏问题列表。

* **资源泄漏信息详情Top问题**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为FD\_LEAK，点击查询按钮，过滤出此应用的FD资源泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/DXklORPhR5-wqz_fKoKhcQ/zh-cn_image_0000002701370625.png "点击放大")

在资源泄漏信息详情中，可查看当前应用的FD资源泄漏情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/zag3Y1YNS9On27HtSAfcyQ/zh-cn_image_0000002701250559.png "点击放大")

### 根因定位与分析

过滤出FD资源泄漏故障列表后，点击查看按钮，进入到问题个例分析详情页，可查看当前故障的分析报告，包含故障发生时间、泄漏句柄、故障模块、版本信息以及修复建议等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/kbHrsplrQxOhQt-vOtFPdQ/zh-cn_image_0000002671490976.png "点击放大")

**证据链分析**

证据链列表中按照泄漏数量倒序排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。同时提供了日志下载功能，便于进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/LHwLsdoNQJa4LJIiSQsH2g/zh-cn_image_0000002671650846.png "点击放大")

**现场数据分析**

现场数据页中，将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/L-1yIvh2TJuvsTGRrGFVSw/zh-cn_image_0000002701370681.png "点击放大")

**句柄栈信息****分析**

句柄栈信息是发生FD泄漏故障并达到一定条件后，系统从堆栈中抓取的堆栈信息，存在一定的滞后性。开发者可参考堆栈中的疑似泄漏点，进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/t1swT28FQ8mwBa0J-hci_Q/zh-cn_image_0000002701250593.png "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选Top应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/UEGDUZuCRVKgLW-Q5FFaBA/zh-cn_image_0000002671491006.png "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/PEmegY65S4i5Mslr84k0XQ/zh-cn_image_0000002671650858.png "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/-dREj2gDSC26Blxm4aqZlA/zh-cn_image_0000002701370683.png "点击放大")

### 问题分析

**证据链****分析**

证据链列表中按照泄漏数量排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/yEy4l3bFSuSMtst7QhNq5Q/zh-cn_image_0000002701250595.png "点击放大")

**现场数据****分析**

现场数据页面将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/OE9Xpj75R4CGW_Ei-H1dtA/zh-cn_image_0000002671491008.png "点击放大")

**句柄栈****信息****分析**

句柄栈信息中将抓取的堆栈信息中疑似泄漏点进行展示，开发者进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/DpyNN4x4T9ucWwZCuaE3-g/zh-cn_image_0000002671650860.png "点击放大")
