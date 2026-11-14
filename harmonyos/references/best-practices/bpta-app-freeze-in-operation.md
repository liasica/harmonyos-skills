---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-freeze-in-operation
title: 运维态高效处理应用冻屏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用冻屏类问题分析 > 运维态高效处理应用冻屏
category: best-practices
scraped_at: 2026-11-14T08:54:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:6e12cb9157926879adc63f40a1344e4a777389cf2bdd1bf23c4be707668da87c
---

## 概述

应用冻屏是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用冻屏事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用冻屏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/6oTfYjlvQj2zgnKmEbHuvA/zh-cn_image_0000002644931542.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=54634676B12A3E2A2B1A3EA7B4981D1B208117C94B5AD03613ECF108718852A6 "点击放大")

**排查步骤**

1. 在APMS平台配置应用冻屏监控告警规则，设置监控时段、频率和触发条件。
2. 通过APMS故障指标、APMS故障分析页面，可筛选冻屏类型问题，查看冻屏趋势、TOP问题列表与TOP耗时函数。
3. 分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。查看问题详情，通过AI分析、证据链、现场数据、采样栈数据，深入分析冻屏原因。
4. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**1、应用冻屏监控信息详情**

在故障分析页面中，开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/KArg8LVMSI2FyTgotvr_fQ/zh-cn_image_0000002675091251.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE9BB7C102BB37E5A45D484C93135A3ED8B6673BA4088F555C12F70767354C3E "点击放大")

页面也展示应用的TOP耗时函数，开发者可重点关注问题高发的函数并结合业务优先级进行修改优化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/1KR5nd7uTWu8G7HknfxPbQ/zh-cn_image_0000002675011409.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=469696911A1C1BF547C500092D4790DE82378881BB96F8C19C7BE0993DA69F7C "点击放大")

**2、关键指标说明**

* 故障模块：发生冻屏的模块或组件，用于定位问题范围。
* 发生次数（占比）：冻屏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/4HRo8q-CSRSYaCgtfHY0MA/zh-cn_image_0000002645091456.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5872D9A582DA72927BC8ADB7CFCFD7E90F3720DA02685AA08CEE33D47D5FCB37 "点击放大")

**3、关键信息提取**

开发者在分析冻屏问题时，需要重点关注问题详情页的以下信息：

* 冻屏趋势图表

  在问题详情页下钻分析可设置筛选条件，查看冻屏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类冻屏量激增，通常表明新引入的问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/lyV72xOlRIaWolyJsNN9Yg/zh-cn_image_0000002644931544.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=078E137B3496AB52A5F99A565836F42C5C9FF8C0500236027D59F4E4B8977123 "点击放大")
* 环境上下文

  包括设备信息、系统版本、应用版本、前后台状态等，帮助判断冻屏发生的具体环境。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ZwyLGIP4Q7i3zwEf-wK1IA/zh-cn_image_0000002675091253.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=92C11FB570D13D7941774B49D32C8EAEEA7580D51DAF4165AA2CE60EE4C4A69E "点击放大")
* 证据链

  证据链可查看堆栈信息，问题堆栈会有红色高亮显示，可查看问题发生的业务代码位置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Jrd4hyWET1qqVcvDfjpS5A/zh-cn_image_0000002675011411.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=30A63A0080B9F20E389417C987400B472C8705DDBD61E441224E1C2490C38A79 "点击放大")

## APMS平台应用冻屏问题分析案例

### APMS故障预警

可以在故障预警平台的告警规则页面创建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件等，应用冻屏的指标类型是属于APP\_FREEZE。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/XSA2A0fETTKTvJmog6k4Ng/zh-cn_image_0000002645091458.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=28D2B3CFDDB137CFFBEF8ABA15ED77965015E43057FA70A6735FC18DB1B847D8 "点击放大")

配置告警规则后，当应用触发冻屏事件，设备会上报故障信息。系统会开始收集后台数据，当满足告警触发条件后，会触发预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Fs0EdTzsTMCMaSjRZe05wg/zh-cn_image_0000002644931546.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=37E4E3E44D5FA6B7C17BB60633EF6F35109614EE292F51C7A73AC6266835160E "点击放大")

收到预警后，可以点击查看进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/MqiJ3UjvTxiCwAYHsa8UEg/zh-cn_image_0000002675091255.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B1CDB558906A19A60EE4AD695A3EF4109EB53EDB57C1DDB9D561332BAE79E9B "点击放大")

页面包含趋势分析、维度分布和问题列表。开发者可在界面上设置不同的筛选条件，对冻屏问题进行个性化分析。点击TOP问题列表中的“查看”，可进入详情页查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/FWqmsTnLQoSFyqY0PH0_5w/zh-cn_image_0000002675011413.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A43E2EC8677A069D8AF3F3B175BC674554B242D8264B2637DC41C0E819ECC43 "点击放大")

开发者也可以直接点击故障分析页面，经过条件筛选后可查看具体的TOP问题列表，点击查看可进入问题详情页进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/JIZtltobQKeMFC2jrkhigQ/zh-cn_image_0000002645091462.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AF31C759C54C1B3690DFA83FFDCCA583268E1FDC9E1E000C8FC347D42256A3B "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。
* 相同函数名：同一函数发生的冻屏问题会被聚合在一起。

**TOP问题查看**

进入故障分析界面，筛选冻屏问题范围：

在界面可以设置不同的筛选条件对冻屏问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括冻屏率、冻屏次数、冻屏设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/PKnIQIEYQcuynO4oCGni1g/zh-cn_image_0000002644931548.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A5C067BE38AC85BA20FDA322FDB27DC3D1BBC53C79CB036097E07767038EF36 "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一条记录，并按照发生次数进行排序，开发者可高优处理TOP问题。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/YzynY8G3T4ONepdH0qQfUA/zh-cn_image_0000002675091259.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=83EDD748774117C6D594E4F98873EEBE4C4C2C8FC625E079BA47EFDDE7539EEC "点击放大")

开发者也可以查看TOP耗时函数，APMS会根据函数名，将相同函数发生的问题聚类成一个记录，并按照故障出现次数进行排序，开发者可根据函数名排查自己的业务逻辑。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/AMxxX0F5QxSnyJaqDPIdMw/zh-cn_image_0000002675011415.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=71B7B630B7507BA653BC04FB00F4306CBC989C8420664E9A2ABDFCC5C7364A91 "点击放大")

### 根因定位与分析

**基础定位信息**

点击应用冻屏信息详情列表某个问题进入详情页后，APMS将提供以下核心分析信息，帮助开发者定位根因。

* 问题概要：展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断冻屏的基本属性。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/JlGlTsEVRJWsZbB_hRU0_g/zh-cn_image_0000002645091464.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=35BE379269EC4FEEBDAF7E1925A635644C7EA39333905F1DDD0BCABDF022975F "点击放大")
* 聚类数据：基于堆栈关键行和过滤条件，筛选同类故障并进行聚类，从而帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/N6FGcGgUSHKx8EV568hrpw/zh-cn_image_0000002644931550.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E20E92F2BD50BA9A6BF361BD9A4E0671E7635325F3EAB62775638E2ED86A80DE "点击放大")
* 分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM 版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/r0WQ1A2ISzGH5fdu9oE01g/zh-cn_image_0000002675091261.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C117B58AB6CE0596AC938215CF2E2C44D4D39695E620C8EEF6EF9F61CF0A439 "点击放大")
* 故障详情：可根据平台解析出的故障原因，参照修复建议定位代码问题，完成问题修复与验证。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/4Ky-CvmsQEi1uAsZ9BBh2g/zh-cn_image_0000002675011417.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=F74ACD2F2B2F383EC8ABCAFD0BA9160A908D972BE2BADE365514BB1CB4068343 "点击放大")
* 证据链：证据链会展示问题发生的堆栈并标出故障处，同时会说明问题根因的判断依据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/lQ47IybNRUCC8JyET5BfoQ/zh-cn_image_0000002645091466.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7A2E3B3F3299F4D9C017AB11C84D22D9A367FB84DF24D8F5285EE8F34974CA2 "点击放大")
* 现场数据：现场数据为开发者提供冻屏时刻的完整运行上下文（包含堆栈信息、页面导航轨迹、CPU信息、内存信息与热档位等），便于精准还原用户操作路径与触发场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/eabWsXQDQg-ZONSIHrAD9Q/zh-cn_image_0000002644931552.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D347065980F761B595BA40DCABABC0BD5A5BE25F9D51DF2CFF1A51A3E570DD0 "点击放大")
* 采样栈还原堆栈：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/yPafYYW0RBqPSVKgOlSveQ/zh-cn_image_0000002675091263.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=29778A2AEA503207979A8720B1BFF2EE215C732EAE35CCB406CDD06753A7EDDE "点击放大")

**下钻分析**

下钻分析的核心逻辑是：从一个汇总的指标或表象问题出发，将其拆分为多个组成部分，然后挑出最关键的线索继续向下拆分。重复这一过程，直至定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/62FwHTpoTriO2HWGrujTbg/zh-cn_image_0000002675011419.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=D193B1FBDD00E1E68D0B97AA39E6FA70BDA0B8EC4764408EEB63A5D615EB8AA5 "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/nj7Ec94wS2-7LMYlrjZlog/zh-cn_image_0000002645091468.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=14A685AA9A5D1C880EE0DAF1D86664EDB0E47A6AFE5709D972E40082105D14E8 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/ZlLI1tgHSwy1gcFcLMSqFA/zh-cn_image_0000002644931554.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E389F3D0D1A298CFE42BAC4357B8BAE48EA1F398DA5FB36FECF3C4B3AA6E19B "点击放大")

### 修复建议与问题闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/8f_2fK-pRByC6bhHziuQSw/zh-cn_image_0000002675091265.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7CACD3CE931DA2D3998DDE904C8DE0F1EA3BD0E899133A687D39DA792F7F8F7 "点击放大")

**问题闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修复，并关注新版本的冻屏数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/6r3cmxn0R2GA3SUlaHTGDQ/zh-cn_image_0000002675011421.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE996F1797D6962FFB31FF9F288617441FDB064455C43CCF059619A652FD7BF8 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用冻屏事件，针对不同的冻屏事件提供最佳实践和修复方案，并提供案例库，收录冻屏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用冻屏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/4H2GODmKSzaDGAG1-nA19Q/zh-cn_image_0000002645091470.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=5806A9D68D4E289AA49E098E50CB6D7808D09C4FED053E5953A12050C9FE5280 "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/M1sncIwKTJaiBcuD9RtpwQ/zh-cn_image_0000002644931558.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=335099241869932E70582F82036B4307A0993257969D23F34730F16B02FF9688 "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件来筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/2OZI_CZpS-6b0M7xGyexMQ/zh-cn_image_0000002675091269.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DDC25C38E42B77A13A7E9B5ECF71B993B61BF664B87A7A277D04486CCB9AACF "点击放大")

开发者也可以点击耗时函数列表，然后点击具体的耗时函数，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/EZBtbhxRR-i-FgB95hGm-A/zh-cn_image_0000002675011423.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3DB522257630C70CE5B068DBD62168E5CEC84DC8312EAFBAA3C3A61F2EE8F54 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据、采样栈日志进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/nX-7NsA7RAWMVVJjHbre_w/zh-cn_image_0000002645091472.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B3B04235393093C44425248E1B58F0D35EE0BE5F4211C426077217BBA546A09 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/oPLg8YhBSPmKyaPuFebzaw/zh-cn_image_0000002644931560.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD3E55672268DD3E32118F0003D452812B22E349EFD1AF81A2F2DD3B19012AB9 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ZEZ2Y3xiR9aaCVuJLM0biw/zh-cn_image_0000002675091271.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=148B218CA2910621BF4DE0361CDF1F0E240FAE0849EF9740774BD3BA13AF4A6D "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Mho-l_OSQVKaGJGV2RquRQ/zh-cn_image_0000002675011425.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=B5A6ECF323F1A1D453981FF1E4B8357D1EAB383836F9B3C0FD287E37A51533B6 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/wgtjqQCxRLqF90ctVZEtoA/zh-cn_image_0000002645091474.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE9BBC6461A809193824B49806F64044D1841DC3709C2D1C68C0D8630E8420C8 "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/zgVfP86jRsiyweMb6UFGRQ/zh-cn_image_0000002644931562.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A8CCE4A2A7EABBEA6CB188429EF83A359247087AF020E626156560437C9B937 "点击放大")

点击故障处可跳转到源码中对应的代码行，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/jKZyNAm_S6-Ya4V6m0l9-Q/zh-cn_image_0000002675091273.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=30F512FCFBEBE6625210E3B30226816FEB860EB576482062A857DAEF4A05B1AC "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Gc0Hzh9ER9e0gvJVFgxj2w/zh-cn_image_0000002675011427.png?HW-CC-KV=V1&HW-CC-Date=20261114T005421Z&HW-CC-Expire=31536000000&HW-CC-Sign=58F92A3281178155339E9A9A562A772C713DDA5304067E0A6D6EF4CB70C0E7BB "点击放大")
