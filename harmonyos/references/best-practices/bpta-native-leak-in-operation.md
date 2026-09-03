---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-operation
title: 运维态高效处理Native泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理Native泄漏
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:02887c4721c1dcc5f3f247106e714c1ac6ab3ada375386a14bffa21f73e3c0ce
---

## 概述

Native内存泄漏是一种常见的泄漏类型。本文档主要介绍在运维态下如何利用[APMS](../app/agc-help-apms-0000002235870062.md)平台完成Native内存泄漏的监控、分析、定位及修复全流程。

## 运维态Native泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/3wj0FtWqTDWSNxULoIBcBQ/zh-cn_image_0000002645091436.png "点击放大")

**排查步骤**

1. APMS故障预警配置：在APMS平台配置Native泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题查看与聚类：通过故障预警或主动分析页面，筛选PSS\_MEMORY和RSS\_LEAK类型的泄漏问题，查看Native泄漏趋势与TOP问题列表。
3. 根因定位与分析：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。查看问题详情，通过证据链、分配栈信息和符号表还原堆栈，深入分析泄漏原因。
4. 修复与验证闭环：根据修复建议优化代码，并验证修复效果，形成闭环。

具体排查操作步骤可参考：[APMS平台Native泄漏分析案例](bpta-native-leak-in-operation.md#section14745785205)。

### 指标监控与关键信息提取

**Native泄漏监控信息详情**

在故障分析页面中，APMS基于堆栈关键行对同类异常进行精准汇聚，将具有相同泄漏根因和主泄漏方法的异常报告自动聚合成同一类问题，并按照发生占比排序。开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，高优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/gP7v6lFKRAyFRiuiMvSb7Q/zh-cn_image_0000002644931526.png "点击放大")

**关键指标说明**

* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/OBSIZNDSSRGBPS2rfImqSQ/zh-cn_image_0000002675091233.png "点击放大")

**故障详情页关键信息提取**

故障详情页面可以通过证据链和堆栈信息进一步分析泄漏的原因。

* 证据链

  根据泄漏堆块的分配内存大小区分主次泄漏堆块。展示主次可疑泄漏方法详情以及对应的修复建议。排查优先从主泄漏堆块切入，核查主泄漏方法是否存在异常。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/PrHB8YUCRZS2Z_-QI0lxPA/zh-cn_image_0000002675011391.png "点击放大")
* 分配栈信息

  展示当前选中的泄漏堆块和泄漏方法对应的堆栈信息。通过堆栈分配详情、堆栈树分配和火焰树三种不同的形式展现，以便开发者更直观更便捷地查看分配栈信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/maAgup8pROKjXJftMC1sQQ/zh-cn_image_0000002645091438.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/WuOPFsqESKq3_LwNx4b80Q/zh-cn_image_0000002644931528.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/nc_TXZ_wQ3K_ILpDm36vLQ/zh-cn_image_0000002675091235.png "点击放大")
* 还原堆栈（符号表上传）

  通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/RGmC5xWzQjuNL6w393AP0g/zh-cn_image_0000002675011393.png "点击放大")

## APMS平台Native泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集](../harmonyos-guides/hiretrieval-intro.md)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

可以在故障预警平台的告警规则页面，新建告警任务。结合实际业务场景，选择合适的监控时段、监控频率、告警触发条件及其他告警指标，其中Native泄漏对应的指标类型为MEMORY\_LEAK。

建议配置以下告警规则：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/G-y0v26iTDyuOThSppsH0A/zh-cn_image_0000002645091440.png "点击放大")

配置告警规则后，当应用触发Native泄漏事件，设备会上报故障信息。系统开始收集后台数据，满足告警触发条件后，系统将发出预警。可参照下图步骤查看故障告警：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/GLmZn4-YQqiser3g4xJD_A/zh-cn_image_0000002644931530.png "点击放大")

收到预警后，可点击“查看”进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Mqj2j4ABTH2YPNGlNANZaQ/zh-cn_image_0000002675091237.png "点击放大")

故障指标页面包含趋势分析、维度分布和TOP问题列表。开发者可以在界面设置不同的筛选条件对冻屏问题进行个性化分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/RL_RXH0-Scets8xxK6amFA/zh-cn_image_0000002675011395.png "点击放大")

点击TOP问题列表中的查看，可以进入问题详情页查看问题详情，进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/d-tiGkkxShC2xvjJnbphnA/zh-cn_image_0000002645091442.png "点击放大")

开发者也可直接点击故障分析页面，通过条件筛选查看具体的TOP问题列表，点击查询按钮进入问题详情页进行进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/b4RZ-szDQuShmGiaJYPDKQ/zh-cn_image_0000002644931532.png "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。

**TOP根因聚类**

在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似泄漏堆栈的异常报告自动聚合成一个问题。开发者可点击“查看”进入问题详情页查看详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/J6g_BKnPQRypMlfkq7gD7w/zh-cn_image_0000002675091239.png "点击放大")

### 根因定位与分析

**基础信息定位**

点击问题列表中的某个问题进入详情页后，APMS 将提供以下核心分析信息，帮助开发者高效定位根因。

问题概要：展示问题的核心身份信息，包括故障类型、故障模块，帮助开发者快速判断崩溃的基本属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/WGhvZZ5HTp6N3nKEayTvkQ/zh-cn_image_0000002675011397.png "点击放大")

聚类数据：基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。

分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。此处demo展示的故障模块是leak\_thread。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/nTEmqkFnTBWz6ZglZm8tPg/zh-cn_image_0000002645091444.png "点击放大")

**证据链分析**

证据链展示主泄漏和次泄漏具体方法位置。开发者可根据平台解析出的泄漏堆栈和故障原因，参照优化建议定位问题代码，完成修复与验证。

根据故障详情分析得出：可以看出规格为4096B的堆块为核心泄漏堆块，libanon.so为核心泄漏库，leak thread为核心泄漏方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/IMIFgt1eQmW7XgkzCVjRew/zh-cn_image_0000002644931534.png "点击放大")

堆栈信息分析：三种形式（堆栈分配详情、堆栈树分配和火焰树）用于查看方法调用关系和疑似泄漏故障处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZyAIvn0fSQ268Tv_M-KlxQ/zh-cn_image_0000002675091241.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/nZL0dRSaSVGYDQmHS_Qmjg/zh-cn_image_0000002675011401.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jzCDvYRGQ9a7goZYQag68g/zh-cn_image_0000002645091446.png "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/WsxBUd8ISh-YM87hEFWpdA/zh-cn_image_0000002644931536.png "点击放大")

### 修复与验证闭环

**修复建议**

故障详情页面会提供修复建议，开发者可根据建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/vx1BpR8gTq2PaATgtSfLzw/zh-cn_image_0000002675091245.png "点击放大")

**修复建议与闭环**

1. 修改问题之后，可以在分析页面对应的泄漏对象标记已修改，并关注新版本的崩溃数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

**故障模式库**

故障模式库中会收录常见的Native泄漏事件，针对不同的Native泄漏事件提供最佳实践和修复方案，并且还会提供案例库、收录Native泄漏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer是DevEco Studio的插件，通过该插件可查看应用故障数据，数据与APMS平台一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击资源泄漏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/GyLgIhkiSFuQfHkH_7Cxlw/zh-cn_image_0000002675011403.png "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/DmHULWz4TOCnpwYYAOG5kw/zh-cn_image_0000002645091448.png "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据进行具体分析，符号表页签支持上传符号表，还原堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/W_bGc-hoRl-qxvHoxJxwew/zh-cn_image_0000002644931538.png "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qVMAe6hQRrKkG4qIWSzCNg/zh-cn_image_0000002675091247.png "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/u4NHTvyCT5yNdGiEizFn3w/zh-cn_image_0000002675011405.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/KSHsvmi2RriU3Pbp-bO8vQ/zh-cn_image_0000002645091450.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/KvGMavxFRYm3fKQT6lMQQA/zh-cn_image_0000002644931540.png "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/rkUqeoGFQG-pLBYAJtjibg/zh-cn_image_0000002675091249.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/y68MKflzSOaJiSMm18Klcg/zh-cn_image_0000002675011407.png "点击放大")

### 问题修复

Operation Analyzer平台会给出泄漏堆块、泄漏函数与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/IzAGNQ7TRUS4atm340m5Rw/zh-cn_image_0000002645091452.png "点击放大")
