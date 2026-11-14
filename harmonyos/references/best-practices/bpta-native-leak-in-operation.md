---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-operation
title: 运维态高效处理Native泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理Native泄漏
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:2a7558e3d88fbd1ac9f64fdb3d659707c394063d7188bd1501261032ea836e82
---

## 概述

Native泄漏是一种常见的泄漏类型。本文档主要介绍在运维态下如何利用应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）完成Native泄漏的监控、分析、定位及修复全流程。

## 运维态Native泄漏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/4JFHNSKeRimxyLdGiqSTUw/zh-cn_image_0000002645091436.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA383B4BE032C10613DA6B08D48A7A30B58A25F1BD7BB8479F79AE8E78AEB1C7 "点击放大")

**排查步骤**

1. APMS故障预警配置：在APMS平台配置Native泄漏监控告警规则，设置监控时段、频率和触发条件。
2. 问题查看与聚类：通过故障预警或主动分析页面，筛选PSS\_MEMORY（Proportional Set Size内存）和RSS\_LEAK（Resident Set Size泄漏）类型的泄漏问题，查看Native泄漏趋势与TOP问题列表。
3. 根因定位与分析：分析故障模块、发生次数、影响设备数等关键信息，定位高优先级问题。查看问题详情，通过证据链、分配栈信息和符号表还原堆栈，深入分析泄漏原因。
4. 修复与验证闭环：根据修复建议优化代码，并验证修复效果，形成闭环。

具体排查操作步骤可参考：[APMS平台Native泄漏分析案例](bpta-native-leak-in-operation.md#section14745785205)。

### 指标监控与关键信息提取

**Native泄漏监控信息详情**

在故障分析页面中，APMS基于堆栈关键行对同类异常进行精准汇聚，将具有相同泄漏根因和主泄漏方法的异常报告自动聚合成同一类问题，并按照发生占比排序。开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/ASnextwaS9G4N-E9EqiHHQ/zh-cn_image_0000002644931526.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BECD6B77A11F99DC1D18E3119B1600B941E77FC80249F7125EA663FA056E1E2 "点击放大")

**关键指标说明**

* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/jwt9MpLYQwSut0jUiRWIPw/zh-cn_image_0000002675091233.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0F745FD1E02A72C1B4F3A4AC085CD1FEBBCB18354EA342F96476EC1055CF073 "点击放大")

**故障详情页关键信息提取**

故障详情页面可以通过证据链和堆栈信息进一步分析泄漏的原因。

* 证据链

  根据泄漏堆块的分配内存大小区分主次泄漏堆块。基于上述分析，平台将展示主次可疑泄漏方法详情以及对应的修复建议。排查优先从主泄漏堆块切入，核查主泄漏方法是否存在异常。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/FQjWWmEqSoycLY61mpy0sA/zh-cn_image_0000002675011391.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=05912F1FCA104A47FE67EC780D98610115A4708DCD615381AF64449B6AE6DC21 "点击放大")
* 分配栈信息

  展示当前选中的泄漏堆块和泄漏方法对应的堆栈信息。通过堆栈分配详情、堆栈树分配和火焰树三种不同的形式展现，以便开发者更直观便捷地查看分配栈信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/w_7MRlusSs2f-xRObTPJ6Q/zh-cn_image_0000002645091438.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCED203D16E86D98540E3DF2E564A413493762094BD67C7A60BEA582301AB5BA "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/wUS6MDDOSWS0jiVn8mydTA/zh-cn_image_0000002644931528.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=81DAB98390A8C306675560BE2BABC32E08F1CF78F64F9EBF11DF8EC6A8862061 "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/BLjxwXeTSNuwZN2euGj_dg/zh-cn_image_0000002675091235.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CA34BE8CF19D8DDE5AD2FEAABADCD484806913102802C2C635086EF8F9E28F4 "点击放大")
* 还原堆栈（符号表上传）

  通过上传SourceMap或.so符号表文件（JS/Web场景上传SourceMap，Native场景上传.so符号表文件），可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bzwfQn-gQzCznGaokjvhKg/zh-cn_image_0000002675011393.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=93717CCDC9BA1B3433FD0AA1DEBDAD5696C73C950005D140536ADD4646907840 "点击放大")

## APMS平台Native泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

可以在故障预警平台的告警规则页面，新建告警任务。结合实际业务场景，选择合适的监控时段、监控频率、告警触发条件及其他告警指标，其中Native泄漏对应的指标类型为MEMORY\_LEAK。

建议配置以下告警规则：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/LAw9-pplT0CQ0CJMVIPgug/zh-cn_image_0000002645091440.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=D869648460238F4FD8E9BC3F1BBB687EA94D5EA9E51D334DF20A0D79F9629B6C "点击放大")

配置告警规则后，当应用触发Native泄漏事件，设备会上报故障信息。系统开始收集后台数据，满足告警触发条件后，系统将发出预警。可参照下图步骤查看故障告警：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/4sbWLBhoSaKulDNTYtnO3w/zh-cn_image_0000002644931530.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=80D19824A04DBEF5B5717A9F1FAB97DEBBD784DB1D0A3C73C40844A657F34B8D "点击放大")

收到预警后，可点击“查看”进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YWtk4VBhQq2EcwIdG8h-uA/zh-cn_image_0000002675091237.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD7740127520E7061DC1BBD8EAFF335397FCDDBFD0AD595AA8C751EE71261C14 "点击放大")

故障指标页面包含趋势分析、维度分布和TOP问题列表。开发者可以在界面设置不同的筛选条件对Native泄漏问题进行个性化分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/hrYLSisKQyKhviyQrSzmRw/zh-cn_image_0000002675011395.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=32F92F99017DE1E87BEAB90CF88A02682C66DC72513238FD99A036256B81DD0B "点击放大")

点击TOP问题列表中的查看，可以进入问题详情页查看问题详情，进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/M0CYr6gBTbe_-s6mD7DmTg/zh-cn_image_0000002645091442.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E3E955F2A7FFA0646E098BFF6A7419169BCE7345128AE54E5BCC1C94D25DFD1 "点击放大")

开发者也可直接点击故障分析页面，通过条件筛选查看具体的TOP问题列表，点击查询按钮进入问题详情页进行进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/t44ppXYbR8CCeUZ2MeG5xQ/zh-cn_image_0000002644931532.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D4E2C10C0E4BA15ED0C07CA0E159167318F98484C43AB123C878CD3783F19B8 "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。

**TOP根因聚类**

在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似泄漏堆栈的异常报告自动聚合成一个问题。开发者可点击“查看”进入问题详情页查看详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/6HuxEcylS-en1lLb1mrBuQ/zh-cn_image_0000002675091239.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=479304BEC515684487BD2A64BE0337B75F9199AED5A9E4DBD90C4CD4BCF5EC64 "点击放大")

### 根因定位与分析

**基础信息定位**

点击问题列表中的某个问题进入详情页后，APMS将提供以下核心分析信息，帮助开发者高效定位根因。

问题概要：展示问题的核心身份信息，包括故障类型、故障模块，帮助开发者快速判断崩溃的基本属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/tC17cdR4SOSiUsoD_ZPAcA/zh-cn_image_0000002675011397.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F50740E2115B4971A6A792E9636BA246E6411E05920CDE5999CCFED4BD611693 "点击放大")

聚类数据：基于堆栈关键行和过滤筛选跳转至聚类同类故障，帮助开发者评估问题的影响范围与严重程度。

分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。此处demo展示的故障模块是leak\_thread。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/1SR5c7IcQlCWgwdlxCBqBg/zh-cn_image_0000002645091444.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=40D445E02EB967866F955FF4BEEEE5B1FC6572407F54BB96D72B63556076DCC6 "点击放大")

**证据链分析**

证据链展示主泄漏和次泄漏具体方法位置。开发者可根据平台解析出的泄漏堆栈和故障原因，参照优化建议定位问题代码，完成修复与验证。

根据故障详情分析，可以看出规格为4096B的堆块为核心泄漏堆块，libanon.so为核心泄漏库，leak \_thread为核心泄漏方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/1MrWFONOSM-36d118q_qdg/zh-cn_image_0000002644931534.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=631CED3737449BE382F75BDF5F7C774DA615616CAC9585D7462E793B92A13826 "点击放大")

堆栈信息分析：三种形式（堆栈分配详情、堆栈树分配和火焰树）用于查看方法调用关系和疑似泄漏故障点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/P30hh_GuQZ-vp6_WwRKN-A/zh-cn_image_0000002675091241.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E97AB1A00317CD621743012BC05FB076EC9CD4CB01795641DE699BAECEFEDEFD "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/L54aU7dMQIaVVN0k_hCHFA/zh-cn_image_0000002675011401.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=6307EB29C4047D1C9AD0D1E472D6833B5D0B447075FB03E865EA8345C7427CE0 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/mY4jXlFGSIGNtNg0FsTXSw/zh-cn_image_0000002645091446.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=392A804617D1E0DB9C2E08F9637A024F9FF1352E3E9942A49BF454D57381E280 "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/LMZ21B-KS7-iNgHlNCtfGg/zh-cn_image_0000002644931536.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=71DF3692D86A48F583BE4DCCE389CF5A1A11AFD9369D48D831F362D4790361B0 "点击放大")

### 修复与验证闭环

**修复建议**

故障详情页面会提供修复建议，开发者可根据建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/zIytIxmIQH60OkRB0UBy3g/zh-cn_image_0000002675091245.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=37D46F2F5636FA03F443C3087623472D2D80E0A46222451FA6D6ADF3A85A2C19 "点击放大")

**修复建议与闭环**

1. 修改问题之后，可以在分析页面对应的泄漏对象标记已修复，并关注新版本的崩溃数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

**故障模式库**

故障模式库中会收录常见的Native泄漏事件，针对不同的Native泄漏事件提供最佳实践和修复方案，并且提供案例库，收录Native泄漏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer是DevEco Studio的插件，通过该插件可查看应用故障数据，数据与APMS平台一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击资源泄漏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/dNoRJXz3TWGyPVh52AONrQ/zh-cn_image_0000002675011403.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=24FCF00017C0336AE96E97707DA29F0E517C5113F887B887FED3C741E0EAF53C "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/FLz5B09WRBmw_nD7aRS-gQ/zh-cn_image_0000002645091448.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6ECBAD6C209212B786CD71BCA98084E3EE4D946BD15145B3A6759A56DB2BCF6 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据进行具体分析，符号表页签支持上传符号表，还原堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/JreRFnPERouISnKLtopRuw/zh-cn_image_0000002644931538.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=35A470E5BD5904AAA3926F2FEA522A2C9DC2013449304C13D42C9A19E97F54F0 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/zF5gMBuEQ0iw1-9oMR8v_A/zh-cn_image_0000002675091247.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E36ADB227004FD14495B367BE1B821003BE6268354D30509A819E00B1C65D35D "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/6blQVoxoRlK-01SVHhlXXA/zh-cn_image_0000002675011405.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF4FA5EF686F64E29D7B7A66F060B2FEF5D7EE782F4DA5F17DF2D10E92459876 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Dc1PgBgWQ3amuEu2ByyIjA/zh-cn_image_0000002645091450.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B30B1452AEF642DED409C40163014D0C3301BECAC1101F45FD12B7D03B6F1AA "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/iyZ5JDKrRpSWf03FP3eVIw/zh-cn_image_0000002644931540.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=22A1CC1FBB57BA512DB49A307E0AF5BB588F9F620300C915C72F6AE3628E652B "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/lT4Sv7WzQoav1bClFrX0RA/zh-cn_image_0000002675091249.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA292B7543DEE447ECBD222542E6C98EA1B08C62853514CAB99592B26E9474FB "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SBbgH6oORz-3c2IHTbRN6Q/zh-cn_image_0000002675011407.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B85BFAD5D4A5E0B558561EAF32CE0F2DB111FE10F113B936BB20EB8BCC5AE433 "点击放大")

### 问题修复

Operation Analyzer平台会给出泄漏堆块、泄漏函数与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2t7LVuBfQCOqoTydLPfzhA/zh-cn_image_0000002645091452.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBB28CCE0828CFCA6B9A2E258C5E770B351EB5286503B3A5B0FEBA4EC70337D1 "点击放大")
