---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-crash-in-operation
title: 运维态高效处理应用崩溃
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用崩溃类问题分析 > 运维态高效处理应用崩溃
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:6093a591002b82958d601aaa36178abe7228de186c33d35819f55d4594f6c409
---

## 概述

应用崩溃是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用崩溃事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用崩溃分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/EzRpa6vBS5K0Imm-bXSHYg/zh-cn_image_0000002644931502.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=017A71E6DF12F5D97B5F4C30CFD6FA1D5FF76A8760BA3DA1810BF729F65725B2 "点击放大")

**排查步骤**

1. 在APMS平台配置应用崩溃监控告警规则，设置监控时段、频率和触发条件。
2. 通过故障预警或故障指标页面，筛选崩溃问题。
3. 分析发生次数、影响设备数等关键信息，定位TOP问题。
4. 通过堆栈深入分析崩溃原因。
5. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**故障分析页面总览**

进入故障分析界面，设置不同的筛选条件对崩溃问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。（可按照提示步骤1、2、3操作）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/5m7AiCeFQ4-mouxVU-qIqg/zh-cn_image_0000002675091209.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FC3749766D28891C905C5FF6B163019E043C7E5A0F4B87A4A9904AE4BE9FBB4 "点击放大")

**关键信息提取**

在异常分析区域界面，也可以设置不同的筛选条件查看指定时间范围和条件下的三类指标数据，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/K6MClMdSRmqkaUOMDA5Liw/zh-cn_image_0000002675011367.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=323D5C81FED22E066981E8BA2A56EDC5C09245EFD546219B8777774B6DA06106 "点击放大")

**关键指标说明**

* 故障模块：发生崩溃的模块或组件，用于定位问题范围。
* 发生次数（占比）：崩溃问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/g4PyH4V5RfGRZcpN1PoM2g/zh-cn_image_0000002645091416.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=A477C25A13823AAD061609A54A6C63BCAC1AAFC0A6B8993569B57A27D2351C34 "点击放大")

## APMS平台应用崩溃问题分析案例

### APMS故障预警

**告警总览**

点击告警总览列表可展示指定时间段内的所有告警概览，点击“查看”可查看该告警的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/rCB0zm44R8GzCyzjwzhu5A/zh-cn_image_0000002644931504.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5384FAB6E7A91AA89D400E662B9890FBBE2B9C0D0D3C6E7DAEFAE0090D7185A "点击放大")

**告警规则配置**

点击告警规则配置，开发者可以根据需要进行告警规则配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/N2U07oxBRPGYDzs49LS0IA/zh-cn_image_0000002675112215.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=98B9DD8240E9069D11B2B67F545ADB55054886F3798FA1D4143B3F9FEDE2358D)

### 问题查看与聚类

在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似崩溃堆栈的异常报告自动聚合成一个问题。

**聚类规则**

* 相同根因类型：将具有相同故障根因的问题聚合在一起。
* 相同故障模块：同一模块的崩溃问题会被归类。

**TOP问题查看**

进入故障分析界面，筛选崩溃问题状态，设置不同的筛选条件（如问题定界、崩溃类型、故障模块、发生次数、影响设备数等）对崩溃问题进行个性化分析。筛选条件设置完成后即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/FGJINSVvTBiMmlDtYyBVIw/zh-cn_image_0000002675011369.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=2897A6C821699CA5671038659CCBB83D4915E53DB561B366F0451BBE3A1F9357 "点击放大")

### 根因定位与分析

**基础定位信息**

* 故障分析页面总览

  点击问题列表中的某个问题进入详情页后，APMS将提供以下核心分析信息：错误类型、故障模块、故障详情、堆栈信息、现场数据、符号表等，帮助开发者快速判断崩溃的基本属性和高效定位根因。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Wx6fxhxaSv2C9zZIw3ikng/zh-cn_image_0000002645091418.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=E891240D3DC5550AF361CC9F45A432CE2E2C35137F4D435607AF05525EEA862C "点击放大")
* 聚类数据

  基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/hjOgfVl2S9qEH0enI8cuNw/zh-cn_image_0000002644931506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=2514E28D2318AA8B4E1AA356CCAB267E83A22D783C5515D3DB58A4810DF18032 "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/bYjqVChoTbSJPDalm6mhFw/zh-cn_image_0000002675091213.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=58FC1AF5079B432305EBB7C5F7F0B4DEBDF81C517E7432E73E848AAB6A5D8016 "点击放大")

**下钻分析**

下钻分析（Drill-down）是一种从汇总的宏观数据出发，沿着特定维度层次逐步深入到更详细、更细颗粒度的数据层面，以探究数据变化原因、定位业务问题的分析方法。核心逻辑是将一个汇总的指标或表象问题，拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/cIdsIJL-Q8iKdRkChI5X1w/zh-cn_image_0000002675011371.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4E6F8896388DF1D145B3065ED7E8C4187B6D381BD613D3B7896560428FBE814 "点击放大")

### 修复建议验证与闭环

**分析报告**

提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、应用版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/lpvYQPuJT7mKIEdLZkwaDA/zh-cn_image_0000002645091420.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=15CC51E791C1BBFAA1F8845B9193715C9EBE18C601189A0E64C88568DEBE0478 "点击放大")

**修复建议**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Zs3RFtLnSlm97xXH1SkbrA/zh-cn_image_0000002644931508.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE88E60368A28571A1B57B40E523A6CCEF0EA515A218B7EC709FC34B037BFA25 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用崩溃事件，针对不同的崩溃事件提供最佳实践和修复方案，并提供案例库，收录崩溃问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer 插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者在DevEco Studio上也可以使用相同的方式分析运维态的崩溃问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用崩溃即可查看该类故障数据，具体操作如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/h8jCnQocSieWTFKkFHbfFg/zh-cn_image_0000002675091215.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=31F61A1D09F694CB94D5FF31D52BF1DDC255D418ECDE68DA4EB71E6F8CE6063A "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/mSqe6EKAR2qOaZhbru0RrA/zh-cn_image_0000002675011375.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=D58FD9C46DF5A4A764E81402BF1962380FBEC7BD3CB967C5A4BF462B704DEAED "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件筛选需要查看的问题，可点击列表下具体的问题进一步查看问题详情。基本的操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/upDgXJgGSHKDhurZahaJ7g/zh-cn_image_0000002645091422.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D27E5697708EC06E4F643126F8E974CDAE8C442751D593D9B6592676C81FB7 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看堆栈信息、上下文数据、符号表进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/hUeBFJH3QjOE33irA8hxHw/zh-cn_image_0000002644931510.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B68FE5F021F3734C27B28EF941C1127C388AD13EE24715FA6F1FA2FC3B26E2FC "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/R419zW_MQsyo5u1SjG2_Ng/zh-cn_image_0000002675091217.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C34C9192070BF7337640DD2A40EDAB125EA92082DEF243EDEF0160E5493E47F "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原（通过符号表将堆栈地址转换为可读的函数名和行号）的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ESKW210hRMSFcfSpBPDZQg/zh-cn_image_0000002675011377.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B615E887A228EF43381A3A3BC9BC11CF630A35CE82A4CF81785F2914B9859183 "点击放大")

上传符号表步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/b-xc5wm3Qj-nVKSUvcdb-A/zh-cn_image_0000002645091424.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C9949A3FE3972AC1155C89085B9B2A882263E4A7B1B4203CBF2A1DFBBB0B5B1 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ogt0_m9VRNa-ShRaRFoRfg/zh-cn_image_0000002644931512.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=491A2B2D4B2E6D26380AADF0E4D10B3F732DB5449EDC45DF380BE8D3BA0CF206 "点击放大")

查看故障处源码步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/yZLWtFAIQqKDt95luPpRCQ/zh-cn_image_0000002675091221.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=273F1AA8932FFE16ACFA0A942A8F4C1E1BD0C70AF55E621B8F466BC5B631EE3A "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码（Best Practices为问题定位指导链接）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/xzqAIxg5Ry6yuRnzPYDnsw/zh-cn_image_0000002675011379.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=854A1B87134A8F9D303BABC5F15672C74C7ECC59521B73FA15DB81B3B1A81F70 "点击放大")
