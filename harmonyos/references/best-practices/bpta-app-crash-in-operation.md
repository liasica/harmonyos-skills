---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-crash-in-operation
title: 运维态高效处理应用崩溃
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用崩溃类问题分析 > 运维态高效处理应用崩溃
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:c5bf9c534459075b704819ce5fe1c6125254cb79799b5be7383cf2b6e9b4472c
---

## 概述

应用崩溃是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用崩溃事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用崩溃分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/3QbuehGNR6SJxdpEJbrvYg/zh-cn_image_0000002644931502.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A57B83208589A7AD61CDA5B42E0A21964C39BF23E7454378124739C73DE4CAEC "点击放大")

**排查步骤**

1. 在APMS平台配置应用崩溃监控告警规则，设置监控时段、频率和触发条件。
2. 通过故障预警或故障指标页面，筛选崩溃问题。
3. 分析发生次数、影响设备数等关键信息，定位TOP问题。
4. 通过堆栈深入分析崩溃原因。
5. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**故障分析页面总览**

进入故障分析界面，设置不同的筛选条件对崩溃问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。（可按照提示步骤1、2、3操作）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/uMCx7XygQM-U1pCoEVBDyg/zh-cn_image_0000002675091209.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E5B7E46B211292EB46508260888A8DABC5B7ED3C0032797F4D593DA9A5E0015 "点击放大")

**关键信息提取**

在异常分析区域界面，也可以设置不同的筛选条件查看指定时间范围和条件下的三类指标数据，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Q4q5xqFuTAKmuunV9MXQwg/zh-cn_image_0000002675011367.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=18AD5AFDA632ADE8A40C636F0CFA93616ABC82CF202324C3775CF2719CBDA0F3 "点击放大")

**关键指标说明**

* 故障模块：发生崩溃的模块或组件，用于定位问题范围。
* 发生次数（占比）：崩溃问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/nrnkZEu8SQa4LHvt9711MA/zh-cn_image_0000002645091416.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=847A99731945A38AFF3AEDD430156B3D4ED6D8FF25D7A7075831F0E8B49EEFC2 "点击放大")

## APMS平台应用崩溃问题分析案例

### APMS故障预警

**告警总览**

点击告警总览列表可展示指定时间段内的所有告警概览，点击“查看”可查看该告警的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/8a41dZVkRiisRcUVRLS00w/zh-cn_image_0000002644931504.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=178B94B68CFE85BDE6D3EC324D8A7294A25AFB41CFF025910A5BD793A4178067 "点击放大")

**告警规则配置**

点击告警规则配置，开发者可以根据需要进行告警规则配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/nIYH03DFTRyYv7z89hVYIA/zh-cn_image_0000002675112215.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7096F0291630E7E67082EC657327DF62D922848BB231A77774FA2AF5725372D6)

### 问题查看与聚类

在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似崩溃堆栈的异常报告自动聚合成一个问题。

**聚类规则**

* 相同根因类型：将具有相同故障根因的问题聚合在一起。
* 相同故障模块：同一模块的崩溃问题会被归类。

**TOP问题查看**

进入故障分析界面，筛选崩溃问题状态，设置不同的筛选条件（如问题定界、崩溃类型、故障模块、发生次数、影响设备数等）对崩溃问题进行个性化分析。筛选条件设置完成后即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/_32Yz3pgQGOUTtTjdGBODQ/zh-cn_image_0000002675011369.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=74904F399CE6293B6A85B1F4741AE0955A5B9FAFFA73A8E0CEFE8AE67903F33A "点击放大")

### 根因定位与分析

**基础定位信息**

* 故障分析页面总览

  点击问题列表中的某个问题进入详情页后，APMS将提供以下核心分析信息：错误类型、故障模块、故障详情、堆栈信息、现场数据、符号表等，帮助开发者快速判断崩溃的基本属性和高效定位根因。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Op-epaZdQPSFAG7Cia1gcQ/zh-cn_image_0000002645091418.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E61C9AC9E9D52D7CAB18022DD5A808AF8F9964374290075BE8B6C5CF3C2EF765 "点击放大")
* 聚类数据

  基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/v9WOdSSSRfe7y9QNMEBSBg/zh-cn_image_0000002644931506.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F5954EF2250644E3E29C19D109C469334462512B6208A3F50B8137C0FB3584B "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/R_yDrgf7TKaUcLE7x29b9g/zh-cn_image_0000002675091213.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=09AA83C1738227001A55D608E3862C381E78E21308A80002F627297C70E6BAED "点击放大")

**下钻分析**

下钻分析（Drill-down）是一种从汇总的宏观数据出发，沿着特定维度层次逐步深入到更详细、更细颗粒度的数据层面，以探究数据变化原因、定位业务问题的分析方法。核心逻辑是将一个汇总的指标或表象问题，拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/0LBIj7koRye8VuxTrWOFkg/zh-cn_image_0000002675011371.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A888F7DAFAF1F2DDDA4970041564F9C59BB604E90B0FF48A46E6F5CD5F45E372 "点击放大")

### 修复建议验证与闭环

**分析报告**

提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、应用版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/USZk2KVuSvuppOgTdI0Rig/zh-cn_image_0000002645091420.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=78F2E142FC0D99F849FF5D1F43036DDB30BFF248CE4B97241FF6999212D07380 "点击放大")

**修复建议**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Wj-4J_LxQTK4BDhF2mHKuA/zh-cn_image_0000002644931508.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=976867F3D12B05FFD21A1DE38A9DF79A873E762712BDED83E96DD97F0C1A3A43 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用崩溃事件，针对不同的崩溃事件提供最佳实践和修复方案，并提供案例库，收录崩溃问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer 插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者在DevEco Studio上也可以使用相同的方式分析运维态的崩溃问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用崩溃即可查看该类故障数据，具体操作如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VtBOOzneQoim6HrQE596wQ/zh-cn_image_0000002675091215.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=95EECC0EAB8723F1C1DED6149A15DF8C6D7324C37688367B9A08B4FC7F603B7C "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/umRzA0vuRuOOwfSEAM0ZHA/zh-cn_image_0000002675011375.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D406C5D2251A59E21EF45E32F9642DBA15CFE16A8F27F19AB0EC5E0719B5958D "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件筛选需要查看的问题，可点击列表下具体的问题进一步查看问题详情。基本的操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/_SM46UQgTcmOZK2PtKysaQ/zh-cn_image_0000002645091422.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CEB541FC21C41B243A0B6623F57CD9EB6582184AF04B2D752AEEA2AB8C8C161 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看堆栈信息、上下文数据、符号表进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/fMBIvGMyQguJwxg2QRN20Q/zh-cn_image_0000002644931510.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=50D1FF5CC1866734E5F4537541FC575F616FE5D49B78DCC8DAD4AA9B078506B2 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/vKAUglhpTKGqMy-fpdR7xQ/zh-cn_image_0000002675091217.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A8FEFF2586CBFBE2184E1549D8352CB698D80FA68FBDB0BC24B4A28AD356EAE "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原（通过符号表将堆栈地址转换为可读的函数名和行号）的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/l5BahhlMTi20x6R7VUtf5Q/zh-cn_image_0000002675011377.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8821E260C156A58EDE8BF887A316CE635EE24F950BF56F83302723298D504D36 "点击放大")

上传符号表步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/tq3ThAPiRHe7zWffM2Rz2Q/zh-cn_image_0000002645091424.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DFBD4A4D691889EA0CCBF08D0E884CEEDF7963D734EDD7C41DC4020B9B6E585 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/VJXtI2AmRqmpDsgcK-t9_w/zh-cn_image_0000002644931512.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFC5256CD1EADDAE2D852E855E3F000C824B3365C0794A1B8FB5F840186F46B6 "点击放大")

查看故障处源码步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/kq4VutyHScOriQIFr-C1HQ/zh-cn_image_0000002675091221.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1CF8969F7B777BE218601370211C7495FEDF53E6D0D2C2F66C5A44D569FF495 "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码（Best Practices为问题定位指导链接）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/b0cEnaVrQjGAd31Bh-Fi9Q/zh-cn_image_0000002675011379.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=19ED81FBC4E724CEB655293797657B1B28898134373E87AEBCB22B45202E5EB5 "点击放大")
