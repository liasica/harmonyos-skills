---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-freeze-in-operation
title: 运维态高效处理应用冻屏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用冻屏类问题分析 > 运维态高效处理应用冻屏
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:a9fb0499926269b1ed679adcf2fe495e7037f57b0e01a360b1d650647aa1f560
---

## 概述

应用冻屏是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用冻屏事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用冻屏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/a6hMpH8OSp-6kOTfFG2i3w/zh-cn_image_0000002644931542.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA27A7C5F18A0F7FDC0AE4FAD1EF64A62878168B25DAE12C35CB464BBE45C986 "点击放大")

**排查步骤**

1. 在APMS平台配置应用冻屏监控告警规则，设置监控时段、频率和触发条件。
2. 通过APMS故障指标、APMS故障分析页面，可筛选冻屏类型问题，查看冻屏趋势、TOP问题列表与TOP耗时函数。
3. 分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。查看问题详情，通过AI分析、证据链、现场数据、采样栈数据，深入分析冻屏原因。
4. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**1、应用冻屏监控信息详情**

在故障分析页面中，开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/yvAfjI-MRla9GdxwIGhnPQ/zh-cn_image_0000002675091251.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C67A7019C8A684571AEFCE5984016E685390EE702945BA4964B81BF54E01AC5 "点击放大")

页面也展示应用的TOP耗时函数，开发者可重点关注问题高发的函数并结合业务优先级进行修改优化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/B42w9GULSTWaDaBaNFPUMQ/zh-cn_image_0000002675011409.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEF50E2017C4964FEBA962BC5BEE9E24D7E145D71842536B823347BED51AF7CD "点击放大")

**2、关键指标说明**

* 故障模块：发生冻屏的模块或组件，用于定位问题范围。
* 发生次数（占比）：冻屏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/dR6_I9ALSyaSKqJ1da4whA/zh-cn_image_0000002645091456.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBF2A019F5C14DF5927697D7B52E54533CFAC4D25D9283008C4C786B4ADCCEF7 "点击放大")

**3、关键信息提取**

开发者在分析冻屏问题时，需要重点关注问题详情页的以下信息：

* 冻屏趋势图表

  在问题详情页下钻分析可设置筛选条件，查看冻屏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类冻屏量激增，通常表明新引入的问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/92MyPwBGQqeB2QAs4oDxVw/zh-cn_image_0000002644931544.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=C573BABA1C9DC4C953EC05682276AD23FF42833DB4D57A3BAA7A350B8EC13AB3 "点击放大")
* 环境上下文

  包括设备信息、系统版本、应用版本、前后台状态等，帮助判断冻屏发生的具体环境。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/M6SqUGBTQ_2uf0kSRoLqlg/zh-cn_image_0000002675091253.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E7C6B5DF16F3178FE768F8A6447222DFF1FA359482A8D20FA48AE613C794A7A "点击放大")
* 证据链

  证据链可查看堆栈信息，问题堆栈会有红色高亮显示，可查看问题发生的业务代码位置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/zV1vDmUMRoOIRBcydtXNQw/zh-cn_image_0000002675011411.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EBDC68B4A6F30257E5FF1E5B0C4BDDFD958CD4AA9283122CC254E6D268B6F07 "点击放大")

## APMS平台应用冻屏问题分析案例

### APMS故障预警

可以在故障预警平台的告警规则页面创建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件等，应用冻屏的指标类型是属于APP\_FREEZE。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/YsCrEZnASiWecKgCAXx6Xw/zh-cn_image_0000002645091458.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB880E74CE7D44B3B90DD59DECAFCA36E1E62B48DF2D2346E7D27BACBD555767 "点击放大")

配置告警规则后，当应用触发冻屏事件，设备会上报故障信息。系统会开始收集后台数据，当满足告警触发条件后，会触发预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/xTocQ0iSR3Okk0b0ZB_TWg/zh-cn_image_0000002644931546.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=74E2C59A693D321806941CDBF3D5A1AF0F6F944642246B63B7CBE2D48B88A938 "点击放大")

收到预警后，可以点击查看进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/bsFyqWcMSDa4AvLMj_hchA/zh-cn_image_0000002675091255.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF3CB9779B43E0C6F0863BF537DC33964F186BC420D9C1E33C63A42AE15D5758 "点击放大")

页面包含趋势分析、维度分布和问题列表。开发者可在界面上设置不同的筛选条件，对冻屏问题进行个性化分析。点击TOP问题列表中的“查看”，可进入详情页查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_ZsG_Fy2QyCZgsQoOi_Zpg/zh-cn_image_0000002675011413.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=86CCCF0BF536DEBE47C3263EE3BEDBB47C434D9AB5763D668E0F91001E360208 "点击放大")

开发者也可以直接点击故障分析页面，经过条件筛选后可查看具体的TOP问题列表，点击查看可进入问题详情页进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/7ahYQM_hQGe_lv2Kwj2EKg/zh-cn_image_0000002645091462.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=31F2F9F319537D790E5D05E110E06FDD749982FE4B2D1D435AFC2BA01CF838FD "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。
* 相同函数名：同一函数发生的冻屏问题会被聚合在一起。

**TOP问题查看**

进入故障分析界面，筛选冻屏问题范围：

在界面可以设置不同的筛选条件对冻屏问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括冻屏率、冻屏次数、冻屏设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Xq-shn5IRpe3ggZ2wpSUnQ/zh-cn_image_0000002644931548.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=A880D256D488253D44465FCAFBCD8A4EF061173F861F44CB08ECEC23E053A6D5 "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一条记录，并按照发生次数进行排序，开发者可高优处理TOP问题。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/BZXPRXmtQ1aB7_iST1JlTg/zh-cn_image_0000002675091259.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=573B2EB4EE5E18B156FA3BB76CE31DFB32511524FCA9B7E0461869B9D411AD38 "点击放大")

开发者也可以查看TOP耗时函数，APMS会根据函数名，将相同函数发生的问题聚类成一个记录，并按照故障出现次数进行排序，开发者可根据函数名排查自己的业务逻辑。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/AUAWMINHRhCY7052x9Mz1w/zh-cn_image_0000002675011415.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=08933303F085ABFBD21F231F40111CCEEE7C67D4A0A44549EF0B436B95AA1E88 "点击放大")

### 根因定位与分析

**基础定位信息**

点击应用冻屏信息详情列表某个问题进入详情页后，APMS将提供以下核心分析信息，帮助开发者定位根因。

* 问题概要：展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断冻屏的基本属性。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/SImm_fO9TGCYwtT10c-dzQ/zh-cn_image_0000002645091464.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6208EFF9A03B54FD645C5E378CB01080A9CC3BDAD90854C2B561357F500844BC "点击放大")
* 聚类数据：基于堆栈关键行和过滤条件，筛选同类故障并进行聚类，从而帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/YY01oRhBQbKO9jaCU6nGXg/zh-cn_image_0000002644931550.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6ECFA26BC6B1474AC76108437AE1B170496593F68A4D2037B498662F8D4AEAB7 "点击放大")
* 分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM 版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/1XfSAnK4TEGIR8sdSDjTqA/zh-cn_image_0000002675091261.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=E344C176B2149C98AE7A3E8F2CFB8ACA81E372514693C9A99DB544260958F9BB "点击放大")
* 故障详情：可根据平台解析出的故障原因，参照修复建议定位代码问题，完成问题修复与验证。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/wRmEcs7PQueKyIocTew_Cw/zh-cn_image_0000002675011417.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7105656D2BCABFCAB1C60B5701270383A52F1D9DB694B9947B97E5A1BDE7BC6 "点击放大")
* 证据链：证据链会展示问题发生的堆栈并标出故障处，同时会说明问题根因的判断依据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/rs4PzMeYTNmEUPltv7ruNQ/zh-cn_image_0000002645091466.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D284AA6938A707E907C2352320959BFA3A5B45410B5328CD8FB876D650CF6BD "点击放大")
* 现场数据：现场数据为开发者提供冻屏时刻的完整运行上下文（包含堆栈信息、页面导航轨迹、CPU信息、内存信息与热档位等），便于精准还原用户操作路径与触发场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/3Uhpr-I0Q3iBtbVlpw_Zuw/zh-cn_image_0000002644931552.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD3D71C713C3CB8CF59B97D0D8E5135F67DA5DAE2E4BF7B1E45E9CB028325338 "点击放大")
* 采样栈还原堆栈：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/BgjYJ76MSrqvzf_boCQS5w/zh-cn_image_0000002675091263.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8B05835516C5C179B2B265E20235CA6200BE47839C7A1CE2BAB47D29CE9FACF "点击放大")

**下钻分析**

下钻分析的核心逻辑是：从一个汇总的指标或表象问题出发，将其拆分为多个组成部分，然后挑出最关键的线索继续向下拆分。重复这一过程，直至定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2SzwLuPPSh2cVsF1K6AJGg/zh-cn_image_0000002675011419.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=433537E85606B7449FF88AFF15839E173F4F85EC6D0BCB4E05AE5F2F62B57710 "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/4RAw4RrTRRa-9IwGMs97tw/zh-cn_image_0000002645091468.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=A22906ECDDB6D6C016895EF1BB8E8A1D8F2B464938E634D2AD47660293EB8D21 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/fT7us6hLSFqpGYKbnPLTYg/zh-cn_image_0000002644931554.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=540DD5BE97698AD3DA1462B7516DB151F48BDB80771C57533DD22E4E244DC912 "点击放大")

### 修复建议与问题闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/0jC3tdrhRSKoRVHIEJEz6w/zh-cn_image_0000002675091265.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF5CAE5EE33D9F7722210FD8726D32B06B020A28F36DCBC7FB15131C92E32C6B "点击放大")

**问题闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修复，并关注新版本的冻屏数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/n4XZLn0jS9i9MiLXh6JALw/zh-cn_image_0000002675011421.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8E90B8F54E67DD577300AEF913C30363980AE5A29F901901CCF1F942790F461 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用冻屏事件，针对不同的冻屏事件提供最佳实践和修复方案，并提供案例库，收录冻屏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用冻屏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/z7ApeuheSA6bqCS-D-xOSQ/zh-cn_image_0000002645091470.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=24BAA8CEE65137C7D5BCCDA8B198FB3AF1A8D7771446F862E38F435F9B869917 "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/f-vLZ_uFRbGOy_uMa3Z-Kw/zh-cn_image_0000002644931558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=953855A8354268B2359758FD38FEBBB1676C375CA94252EE780EDADD9C265717 "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件来筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/DiTkDkLURQCKtMkI6wOw1Q/zh-cn_image_0000002675091269.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=1620C7E7C044EB1ED0C27F2ECDB33FCC4E2E05E714EB205C46C093B8EAF30EB0 "点击放大")

开发者也可以点击耗时函数列表，然后点击具体的耗时函数，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/tyNF-FuGTPq6p8oXUL-xag/zh-cn_image_0000002675011423.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7B093E510602D1B05F8319DF29C92909CEDA5A0C65F12FB28C0030D2D4FBF9E "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据、采样栈日志进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/cbFNnhI5TcO-7aFobP4QAA/zh-cn_image_0000002645091472.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=960603624C92A052A67F79DF24E8759216B1F7CD4EBDF08512C6D0209AD46686 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/LssUXjaTRfuxBHbJGmVuKA/zh-cn_image_0000002644931560.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=E11D80EB1B1E736269B14B4D7A81472684A55295C5BE7F84DC1EC646F24CE9C2 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/rtxpDWNGSsq1m1La_btPLg/zh-cn_image_0000002675091271.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0B144C358395E2569E992C039DF4F53EBDC440AB5ACECAEE79058625E8847B0 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/HgdQbjI8RdOuIkoUKe5i1w/zh-cn_image_0000002675011425.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=55A5EB15E63997E8FD7E4C96DA0E622757DAAB4E8CEAAC7C235F4C55689E6162 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/X1gucWOxRXGss5wLFpJB5Q/zh-cn_image_0000002645091474.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D46BEC3D5B3397FF350785153CC741AEE0C3009A95D77938E48F1CC46AC36D3 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/32orJyK3RnGrRzWPHVACfg/zh-cn_image_0000002644931562.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FF3B913058C6874258FABDE794146E1393CB8FA55F308E3433659BA0565DA92 "点击放大")

点击故障处可跳转到源码中对应的代码行，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/0EkTY9iGQii_hw1Y3TFSKA/zh-cn_image_0000002675091273.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=872EBD0FE0C4E12DC013D9DDDE2B750649B5D04F8BB1396A7170C1320FED52D8 "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/zWL2OoxqToyGkz6wsY11Bw/zh-cn_image_0000002675011427.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF718AA7430A6A4016DDA342BBD4CE20D08BB33B2E484000881389F81D06FA08 "点击放大")
