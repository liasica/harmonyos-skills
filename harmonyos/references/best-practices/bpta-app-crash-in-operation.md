---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-crash-in-operation
title: 运维态高效处理应用崩溃
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用崩溃类问题分析 > 运维态高效处理应用崩溃
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:5efaa3808fb421096eaf6f5a02856ab217638ba21003141b28f391da546d15cf
---

## 概述

应用崩溃是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用崩溃事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用崩溃分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aAGIkC-GTTmEqh9FYlPpxg/zh-cn_image_0000002644931502.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1AD2EFBDB25F446EA9F4BF97A3817B70335AEF6BDDB67D473BD022E5D1503DF "点击放大")

**排查步骤**

1. 在APMS平台配置应用崩溃监控告警规则，设置监控时段、频率和触发条件。
2. 通过故障预警或故障指标页面，筛选崩溃问题。
3. 分析发生次数、影响设备数等关键信息，定位TOP问题。
4. 通过堆栈深入分析崩溃原因。
5. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**故障分析页面总览**

进入故障分析界面，设置不同的筛选条件对崩溃问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。（可按照提示步骤1、2、3操作）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Fc2PnYZZQRuTm2NAe4U_EQ/zh-cn_image_0000002675091209.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C5A2B7E2F46DF309848D4E88F191D6D96E0520F52EBFAB1A1264C5F5052CC9B "点击放大")

**关键信息提取**

在异常分析区域界面，也可以设置不同的筛选条件查看指定时间范围和条件下的三类指标数据，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/6rITBZK2QHilykHOex8sCQ/zh-cn_image_0000002675011367.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=5BA1B4D4E86A0E127A09B87C0742C3356FC55DD49BF9AC91FF6016C8DD9BAF16 "点击放大")

**关键指标说明**

* 故障模块：发生崩溃的模块或组件，用于定位问题范围。
* 发生次数（占比）：崩溃问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/dTCF6XkDTaiCgGugn0_tzQ/zh-cn_image_0000002645091416.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=AECA68E3D810A5BECD023929705CF7AD0A6B4A1B1ED212395C1B094EE5F61547 "点击放大")

## APMS平台应用崩溃问题分析案例

### APMS故障预警

**告警总览**

点击告警总览列表可展示指定时间段内的所有告警概览，点击“查看”可查看该告警的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2sG4AJYkTQitWMO3mKRBag/zh-cn_image_0000002644931504.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2AA889C72330275B82B71D84A1902FCAB75BA44AE05AEE0C9BE2B3A0B525A4A "点击放大")

**告警规则配置**

点击告警规则配置，开发者可以根据需要进行告警规则配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/2k_Mk0qMTySluJ3qzhuLnQ/zh-cn_image_0000002675112215.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9CDA29819744BF29A54245ADA6F77B01CFEAA752C59F3B5AB13E7D688ECFDBA)

### 问题查看与聚类

在问题列表中，每个问题都是同一类问题的汇总。APMS基于堆栈关键行进行准确的同类异常汇聚，将具有相同或相似崩溃堆栈的异常报告自动聚合成一个问题。

**聚类规则**

* 相同根因类型：将具有相同故障根因的问题聚合在一起。
* 相同故障模块：同一模块的崩溃问题会被归类。

**TOP问题查看**

进入故障分析界面，筛选崩溃问题状态，设置不同的筛选条件（如问题定界、崩溃类型、故障模块、发生次数、影响设备数等）对崩溃问题进行个性化分析。筛选条件设置完成后即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括崩溃率、崩溃次数、崩溃设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/BpN6zmWtQRuh6Vs7jwakkw/zh-cn_image_0000002675011369.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB0EDB56FA4C558E3E8A5F30073A5EBA4AC89D44DDE68D345AA4B849F610F64F "点击放大")

### 根因定位与分析

**基础定位信息**

* 故障分析页面总览

  点击问题列表中的某个问题进入详情页后，APMS将提供以下核心分析信息：错误类型、故障模块、故障详情、堆栈信息、现场数据、符号表等，帮助开发者快速判断崩溃的基本属性和高效定位根因。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/KxeBlUe8Qea5_QjVTOjcGw/zh-cn_image_0000002645091418.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=90F68779C60407855F5875E7FB105D5AB27FFB74960996D8FE38EA731D37BA05 "点击放大")
* 聚类数据

  基于堆栈关键行和过滤筛选跳转聚类同类故障，帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/6sxRy89dTrajwQ9DaX6XfQ/zh-cn_image_0000002644931506.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=21416C147FCA07B79CF6BE8B380089941BC64E3742642BC1B1CA5AF250DD1D03 "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Bvyc-sGEQlW7U9yfkTXafw/zh-cn_image_0000002675091213.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=F35997EF7F2BF7DD2C3A726F32EE0003BF98883D063BCE1FF687AB0C332E3EF0 "点击放大")

**下钻分析**

下钻分析（Drill-down）是一种从汇总的宏观数据出发，沿着特定维度层次逐步深入到更详细、更细颗粒度的数据层面，以探究数据变化原因、定位业务问题的分析方法。核心逻辑是将一个汇总的指标或表象问题，拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/QJutss2-TdyZeeQZFgTrwg/zh-cn_image_0000002675011371.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=C92B8FD19A0F369DC02A08E882722658B5DD5C6D588CF4CA05CFD41AC8B4634E "点击放大")

### 修复建议验证与闭环

**分析报告**

提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、应用版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/t_-oXSOdReG33YC-xjx0Pg/zh-cn_image_0000002645091420.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=954CA1EA83E21BC2D787F96C7FB9D3545DE1B4156E2CED03F03B8317361BB5A4 "点击放大")

**修复建议**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/nOl6UY2jTm-nCdvqSr0e9A/zh-cn_image_0000002644931508.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=838035708EBBDE9E1AF1FF43E67901D215A2EB82DB9EA0F6805DDA8C4BC6CB15 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用崩溃事件，针对不同的崩溃事件提供最佳实践和修复方案，并提供案例库，收录崩溃问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer 插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者在DevEco Studio上也可以使用相同的方式分析运维态的崩溃问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用崩溃即可查看该类故障数据，具体操作如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/rScLIr_VS0ybPGV6yZTlGg/zh-cn_image_0000002675091215.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A3C4BAFB54EEFF888EC37280DD6F5BC317FBD52916A5E877D815CFE95B2AD68 "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/dD3jRYt6TemIB8P3LRrgGg/zh-cn_image_0000002675011375.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EA841ECF48FB039F3861395F2B57BC3133A18EC4D1DA9523135D3331931DAD6 "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件筛选需要查看的问题，可点击列表下具体的问题进一步查看问题详情。基本的操作步骤如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/9a7W4EbaRkKdPKjIE3tQjA/zh-cn_image_0000002645091422.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BC459222B811DF231333C4B74C923A957C6687A403C33D94A257E0BAF973B82 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看堆栈信息、上下文数据、符号表进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/kzsuuEaIRbeGpXF49tSkng/zh-cn_image_0000002644931510.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFCA79F53F3428180BD3D1E6FCE9EB35FD254E7D50162B134D6B3D83AD8A2C95 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/LiC63_1pTRui6xnhkH-O4g/zh-cn_image_0000002675091217.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A7351DAC738697B9E95AEF5273F0303A67AC1E30509E13C11428D55DADD0EF4 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原（通过符号表将堆栈地址转换为可读的函数名和行号）的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原（已有符号表则不需要上传），辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/u16z8sz7QJarwZJjl5k73Q/zh-cn_image_0000002675011377.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=B970A87D830B5D6327873294A006324FE5196ACE147B7706593B7D69707166DD "点击放大")

上传符号表步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2NlG23NMQD6g4okIc0X9MQ/zh-cn_image_0000002645091424.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=166290CD903D5D95331B5EE7B02D3CE10034F274CDF6AA381F5EA00F77848D38 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，点击故障处可跳转到对应源码中，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/w9OxwlV9QwaYPJ-t2GkH5Q/zh-cn_image_0000002644931512.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C41031F2415C35D617CB8A022897650DDA961FA823703F623A4AE58F9DBFE2E "点击放大")

查看故障处源码步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/-JMhIhMHTL60hU4PTsI8bg/zh-cn_image_0000002675091221.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF2053E93DD23740A8A9D50EEA50B3EF8ED1090E08C33D131EC75DE64C1AB5EA "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码（Best Practices为问题定位指导链接）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/4eRHM2UxSYah7tWfesxmTg/zh-cn_image_0000002675011379.png?HW-CC-KV=V1&HW-CC-Date=20261114T005135Z&HW-CC-Expire=31536000000&HW-CC-Sign=27717D0B6A92ACC7418EC6902830090683C7A8B4CA85506183FFF612574AD19E "点击放大")
