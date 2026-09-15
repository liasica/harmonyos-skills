---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-freeze-in-operation
title: 运维态高效处理应用冻屏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用冻屏类问题分析 > 运维态高效处理应用冻屏
category: best-practices
scraped_at: 2026-09-16T06:55:15+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:437ff357e42cce60ca7a2e6e0fc6085664457a0911f5b01e507c287fed43dc61
---

## 概述

应用冻屏是应用性能优化的重要问题，本文介绍在运维态下如何通过[应用质量管理（APMS）](../app/agc-help-apms-0000002235870062.md)平台对应用冻屏事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用冻屏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/w5awtrRbSsWsBSKyI8z_Pg/zh-cn_image_0000002644931542.png "点击放大")

**排查步骤**

1. 在APMS平台配置应用冻屏监控告警规则，设置监控时段、频率和触发条件。
2. 通过APMS故障指标、APMS故障分析页面，可筛选冻屏类型问题，查看冻屏趋势、TOP问题列表与TOP耗时函数。
3. 分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。查看问题详情，通过AI分析、证据链、现场数据、采样栈数据，深入分析冻屏原因。
4. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**1、应用冻屏监控信息详情**

在故障分析页面中，开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/JCQ5iLkmQquI-oTAZl19ig/zh-cn_image_0000002675091251.png "点击放大")

页面也展示应用的TOP耗时函数，开发者可重点关注问题高发的函数并结合业务优先级进行修改优化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/SNEnyz-ST9CTyS9F7YHUXg/zh-cn_image_0000002675011409.png "点击放大")

**2、关键指标说明**

* 故障模块：发生冻屏的模块或组件，用于定位问题范围。
* 发生次数（占比）：冻屏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/ghSHwdX8Sg2ajR_4LQb-nQ/zh-cn_image_0000002645091456.png "点击放大")

**3、关键信息提取**

开发者在分析冻屏问题时，需要重点关注问题详情页的以下信息：

* 冻屏趋势图表

  在问题详情页下钻分析可设置筛选条件，查看冻屏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类冻屏量激增，通常表明新引入的问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Qw1qNdWzT6CPvOzdopVS3Q/zh-cn_image_0000002644931544.png "点击放大")
* 环境上下文

  包括设备信息、系统版本、应用版本、前后台状态等，帮助判断冻屏发生的具体环境。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/IYSpKIGAT9m5giCtRmHIAw/zh-cn_image_0000002675091253.png "点击放大")
* 证据链

  证据链可查看堆栈信息，问题堆栈会有红色高亮显示，可查看问题发生的业务代码位置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/zX_dTz0bSuCpugeDgCji1w/zh-cn_image_0000002675011411.png "点击放大")

## APMS平台应用冻屏问题分析案例

### APMS故障预警

可以在故障预警平台的告警规则页面创建告警。根据实际的业务情况，选择合适监控时段，监控频率，告警触发条件等，应用冻屏的指标类型是属于APP\_FREEZE。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/stucWfI4TBOCu5LZlq3JEA/zh-cn_image_0000002645091458.png "点击放大")

配置告警规则后，当应用触发冻屏事件，设备会上报故障信息。系统会开始收集后台数据，当满足告警触发条件后，会触发预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/nScptsHeREmnckUwT6JVhA/zh-cn_image_0000002644931546.png "点击放大")

收到预警后，可以点击查看进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/78LHy79XTx2c-R0SiQoOew/zh-cn_image_0000002675091255.png "点击放大")

页面包含趋势分析、维度分布和问题列表。开发者可在界面上设置不同的筛选条件，对冻屏问题进行个性化分析。点击TOP问题列表中的“查看”，可进入详情页查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/DqKD-qbBTJ2Ybp4V4XfljA/zh-cn_image_0000002675011413.png "点击放大")

开发者也可以直接点击故障分析页面，经过条件筛选后可查看具体的TOP问题列表，点击查看可进入问题详情页进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/jHlOz5mkShih4rwpTUWSkg/zh-cn_image_0000002645091462.png "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。
* 相同函数名：同一函数发生的冻屏问题会被聚合在一起。

**TOP问题查看**

进入故障分析界面，筛选冻屏问题范围：

在界面可以设置不同的筛选条件对冻屏问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括冻屏率、冻屏次数、冻屏设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/LxxtU8hFTZOcfxvKjkcFaQ/zh-cn_image_0000002644931548.png "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一条记录，并按照发生次数进行排序，开发者可高优处理TOP问题。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IGctkeFmQqyddHmsugVg6g/zh-cn_image_0000002675091259.png "点击放大")

开发者也可以查看TOP耗时函数，APMS会根据函数名，将相同函数发生的问题聚类成一个记录，并按照故障出现次数进行排序，开发者可根据函数名排查自己的业务逻辑。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/hFXfHAvKThiYr2pHBApxVg/zh-cn_image_0000002675011415.png "点击放大")

### 根因定位与分析

**基础定位信息**

点击应用冻屏信息详情列表某个问题进入详情页后，APMS将提供以下核心分析信息，帮助开发者定位根因。

* 问题概要：展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断冻屏的基本属性。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/VTqBp8SrQMKcznKIQW06Qw/zh-cn_image_0000002645091464.png "点击放大")
* 聚类数据：基于堆栈关键行和过滤条件，筛选同类故障并进行聚类，从而帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/x1e_9UqrSryWtYEC6r43yw/zh-cn_image_0000002644931550.png "点击放大")
* 分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM 版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/mWbweZJsRo6VIEwnmTP0Kg/zh-cn_image_0000002675091261.png "点击放大")
* 故障详情：可根据平台解析出的故障原因，参照修复建议定位代码问题，完成问题修复与验证。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DEJd8zCMSmKyRhfhWTrjiQ/zh-cn_image_0000002675011417.png "点击放大")
* 证据链：证据链会展示问题发生的堆栈并标出故障处，同时会说明问题根因的判断依据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Q_bg6KuRT1e3HDdJJewvnA/zh-cn_image_0000002645091466.png "点击放大")
* 现场数据：现场数据为开发者提供冻屏时刻的完整运行上下文（包含堆栈信息、页面导航轨迹、CPU信息、内存信息与热档位等），便于精准还原用户操作路径与触发场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ps4YjiFrRIein8FN8pmRGw/zh-cn_image_0000002644931552.png "点击放大")
* 采样栈还原堆栈：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Rnz-gmDFTHW2Aq50b_kgCw/zh-cn_image_0000002675091263.png "点击放大")

**下钻分析**

下钻分析的核心逻辑是：从一个汇总的指标或表象问题出发，将其拆分为多个组成部分，然后挑出最关键的线索继续向下拆分。重复这一过程，直至定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Ol21P6afRLORqkaSTkx4DA/zh-cn_image_0000002675011419.png "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/AzLggTeuRL-kbf8PBfJDyw/zh-cn_image_0000002645091468.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/LiM3rZ6hQ4mQEF9vl7Fslw/zh-cn_image_0000002644931554.png "点击放大")

### 修复建议与问题闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/_g98ew6LSFyrk067cf7Mow/zh-cn_image_0000002675091265.png "点击放大")

**问题闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修复，并关注新版本的冻屏数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/pHCpbGLjTXyTnocPWf8qOg/zh-cn_image_0000002675011421.png "点击放大")

**故障模式库**

故障模式库中会收录常见的应用冻屏事件，针对不同的冻屏事件提供最佳实践和修复方案，并提供案例库，收录冻屏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用冻屏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/XGjZenG0RaiiN5twPAkuJg/zh-cn_image_0000002645091470.png "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/T-frBJPKSF-nX1X69cnCkw/zh-cn_image_0000002644931558.png "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件来筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/UYszhvr7RAuQKgNPj2-qtQ/zh-cn_image_0000002675091269.png "点击放大")

开发者也可以点击耗时函数列表，然后点击具体的耗时函数，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/2ct691m_T2WucIo7FiL91g/zh-cn_image_0000002675011423.png "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据、采样栈日志进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/tLt9Af5CRbyYVNHk0N7tnA/zh-cn_image_0000002645091472.png "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/yokSZ-s6Tmmuj_AtuWRRpg/zh-cn_image_0000002644931560.png "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/qWb2vTXKRTaKeg1uJSRvSw/zh-cn_image_0000002675091271.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/9MlvYb3WRRujjEV-L4FBnw/zh-cn_image_0000002675011425.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/XpkyEWc7SmmbqgJAWnOc9A/zh-cn_image_0000002645091474.png "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ujbx-CljTjSTSO3UyuC0iQ/zh-cn_image_0000002644931562.png "点击放大")

点击故障处可跳转到源码中对应的代码行，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/4-YcB8sAQSuViNu-MrnH3A/zh-cn_image_0000002675091273.png "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/udBDnlV2QZyrBRGe3OGISw/zh-cn_image_0000002675011427.png "点击放大")
