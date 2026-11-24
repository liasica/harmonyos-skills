---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-freeze-in-operation
title: 运维态高效处理应用冻屏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 应用冻屏类问题分析 > 运维态高效处理应用冻屏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:d4b92c3f598cfe1ebe1c96848991db3170c78c85d732700961dea9185fa22d18
---

## 概述

应用冻屏是应用性能优化的重要问题，本文介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）对应用冻屏事件进行标准化排查、分析、定位和修复的闭环流程。

## 运维态应用冻屏分析流程

### 标准化排查流程

排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/UglTHk46Qwy5cYuJ-Z7x6Q/zh-cn_image_0000002644931542.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CC2D298610F2CCCBE37D0055A99AC92B42CD5AF43A46CAC68C4B0CA46B0DECC "点击放大")

**排查步骤**

1. 在APMS平台配置应用冻屏监控告警规则，设置监控时段、频率和触发条件。
2. 通过APMS故障指标、APMS故障分析页面，可筛选冻屏类型问题，查看冻屏趋势、TOP问题列表与TOP耗时函数。
3. 分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。查看问题详情，通过AI分析、证据链、现场数据、采样栈数据，深入分析冻屏原因。
4. 根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**1、应用冻屏监控信息详情**

在故障分析页面中，开发者可查看应用的TOP问题列表，结合业务对问题进行描述，标记优先级与问题状态，优先处理未修复的高优先级问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/2XMpRcsRSF2eNAir_oTNfw/zh-cn_image_0000002675091251.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8401A45E6A3AEFB990B004399063389D345AD9B18E820551CB929A7C35F74BB3 "点击放大")

页面也展示应用的TOP耗时函数，开发者可重点关注问题高发的函数并结合业务优先级进行修改优化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/3GnH_x2LSh-KTO9FZQycwQ/zh-cn_image_0000002675011409.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A76BDBA75942E6F78F92BB26F603464E735E29DE25B65BD637E2F06464F86EE4 "点击放大")

**2、关键指标说明**

* 故障模块：发生冻屏的模块或组件，用于定位问题范围。
* 发生次数（占比）：冻屏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/esqd2CadQDae0lb1wYc-xQ/zh-cn_image_0000002645091456.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3180109CCCCFEA8CB632E198CF88EA272AA0E45D6AD6A9019AC2C46070B48E6E "点击放大")

**3、关键信息提取**

开发者在分析冻屏问题时，需要重点关注问题详情页的以下信息：

* 冻屏趋势图表

  在问题详情页下钻分析可设置筛选条件，查看冻屏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类冻屏量激增，通常表明新引入的问题。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/XHQLS_tsSsmeOacDw6n_xg/zh-cn_image_0000002644931544.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8151379165262923C984FF581AB6EA3921496C7895B81311650E700F9AD9E9A5 "点击放大")
* 环境上下文

  包括设备信息、系统版本、应用版本、前后台状态等，帮助判断冻屏发生的具体环境。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ZC-wHe8cS1Co7Gd5YRsS8Q/zh-cn_image_0000002675091253.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5A6CAA412812FE0CF920DB25782A4B9AC62F008199546A2DBEADC305107ED58 "点击放大")
* 证据链

  证据链可查看堆栈信息，问题堆栈会有红色高亮显示，可查看问题发生的业务代码位置。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/niKy6wbcStO6XBjQF9YUhg/zh-cn_image_0000002675011411.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C817D4321FDFA3C6AA6CE5F2F3E43DD33FCD448AB992F1704E2EFBF5154430D "点击放大")

## APMS平台应用冻屏问题分析案例

### APMS故障预警

可以在故障预警平台的告警规则页面创建告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件等，应用冻屏的指标类型是属于APP\_FREEZE。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/1nN6iKSzTo-TQlkBNlEibQ/zh-cn_image_0000002645091458.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D59669F7813CDB57A995D186AB954060DAC50944C84F4EDFE44CCFFFA9F0721 "点击放大")

配置告警规则后，当应用触发冻屏事件，设备会上报故障信息。系统会开始收集后台数据，当满足告警触发条件后，会触发预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/3ob3DDIuR7GHD_DEig7MQA/zh-cn_image_0000002644931546.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C40190ABEFF455C6235CAF05B2CFD53717E3A85FBA091B40CD6DFC7909609828 "点击放大")

收到预警后，可以点击查看进入故障指标页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/BEMvNUMeTRSRc4t8yoQYjA/zh-cn_image_0000002675091255.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=64767A0258850312CB35ED3294ED4DA9C4396449452A12B0C72A9278A9F0D7A7 "点击放大")

页面包含趋势分析、维度分布和问题列表。开发者可在界面上设置不同的筛选条件，对冻屏问题进行个性化分析。点击TOP问题列表中的“查看”，可进入详情页查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/38GN2Jy5QJqRyiiw2W_C7A/zh-cn_image_0000002675011413.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A86CA6F8EA39A7FB459083FC743BCDA7BEAA46B06EF0D38B2A5F4C04CA7E9AFF "点击放大")

开发者也可以直接点击故障分析页面，经过条件筛选后可查看具体的TOP问题列表，点击查看可进入问题详情页进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/b7SEhV4_S7uTbJjNW847rA/zh-cn_image_0000002645091462.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=715B4B50E9E8204E1FEC690C2A809EEFC9BB1FF4A574B3584677B19949D7E86C "点击放大")

### 问题查看与聚类

**聚类规则说明**

平台根据以下规则进行问题聚类：

* 相同特征ID：将具有相同特征ID的问题聚合在一起。
* 相同函数名：同一函数发生的冻屏问题会被聚合在一起。

**TOP问题查看**

进入故障分析界面，筛选冻屏问题范围：

在界面可以设置不同的筛选条件对冻屏问题进行个性化分析。筛选条件设置完成后点击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括冻屏率、冻屏次数、冻屏设备数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/LNmQb7NOSYOgaeRiuTg53Q/zh-cn_image_0000002644931548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=194B53321C4ADE71CA0900B04EED987A27A5014F2F4FFBB99845C62BC622F4CC "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一条记录，并按照发生次数进行排序，开发者可高优处理TOP问题。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/1DKR6oSES9qosC_E6uhPtA/zh-cn_image_0000002675091259.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=4994DE5964A45D1EAD0892FF5C4F4F04B58DAAE6D749BDCFD807983571A290AA "点击放大")

开发者也可以查看TOP耗时函数，APMS会根据函数名，将相同函数发生的问题聚类成一个记录，并按照故障出现次数进行排序，开发者可根据函数名排查自己的业务逻辑。点击“查看”进入问题详情页，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/JpzFRLvfQe-oaKAva2SiBA/zh-cn_image_0000002675011415.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFDB571103275AD0C8DCC59BBBE6B332F11FB2F09C17484BB5185B8F5C4B28FB "点击放大")

### 根因定位与分析

**基础定位信息**

点击应用冻屏信息详情列表某个问题进入详情页后，APMS将提供以下核心分析信息，帮助开发者定位根因。

* 问题概要：展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断冻屏的基本属性。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/TkZiodZ-Qoa2_TBe6UMOnw/zh-cn_image_0000002645091464.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FFC199F3A1A8384D999995A9339943760CA0B3E35A33E551B394732B1313A87 "点击放大")
* 聚类数据：基于堆栈关键行和过滤条件，筛选同类故障并进行聚类，从而帮助开发者评估问题的影响范围与严重程度。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iyNLEktyT8CoPl4lTh4Pyg/zh-cn_image_0000002644931550.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E59F4089E76F0D7E1F0A0EC8EA8C57C8C5FB94478204CA4F5C9A09AE7987739 "点击放大")
* 分析报告：提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM 版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/8lY0MFcTQ3uY-9lu8iT3uA/zh-cn_image_0000002675091261.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=0ED9D5AD92102AF8375B6D64DECA16A5FE98DCFD9CD4C3A5735AAA1499C98141 "点击放大")
* 故障详情：可根据平台解析出的故障原因，参照修复建议定位代码问题，完成问题修复与验证。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/oZp0MV6GSDyB-vQgSpa3kQ/zh-cn_image_0000002675011417.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=879260AA9C95670DB27A7F956683E20AD41C0858523A1AD606D4B6A87E072556 "点击放大")
* 证据链：证据链会展示问题发生的堆栈并标出故障处，同时会说明问题根因的判断依据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/HqY9DJB8Q3KJ0f4cIAQrEQ/zh-cn_image_0000002645091466.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=07185C3A9334F046FDD3594443EDCE76C2D15CD673D85B75D671A66C3326CDA4 "点击放大")
* 现场数据：现场数据为开发者提供冻屏时刻的完整运行上下文（包含堆栈信息、页面导航轨迹、CPU信息、内存信息与热档位等），便于精准还原用户操作路径与触发场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/lzvmK5HnQBOa8iQSruFLfQ/zh-cn_image_0000002644931552.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=056B920920C6CD785B527AF99FC4699688EEF062C5356DBE4CA083B7D6DE8D26 "点击放大")
* 采样栈还原堆栈：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/3w8lGqCmSJCvhLa1YyGlqA/zh-cn_image_0000002675091263.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=6964D744F4FB5476EA3D51EC7D88A62FF054789AF64B5B5A4E70D82E71DF53EA "点击放大")

**下钻分析**

下钻分析的核心逻辑是：从一个汇总的指标或表象问题出发，将其拆分为多个组成部分，然后挑出最关键的线索继续向下拆分。重复这一过程，直至定位到具体的根因。平台会根据聚类id或pathname（函数/so路径名称）进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/UyWM9goaT-WXv9qoFfZngg/zh-cn_image_0000002675011419.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=76F9A27D9ABB9D15B9CD56F4D992CEE512AEAAA83EE25BBCF58F36724D9F0794 "点击放大")

**AI分析**

平台提供了AI分析日志的功能，会解析问题堆栈，并给出问题根因以及修复建议，协助开发者处理问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/blQlt5fRQsSgE9fuvtdqIA/zh-cn_image_0000002645091468.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1108BDC88E9F4121A87C2573E6AD358340BF6AD261C2D63C2AAA6505F5C82589 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jcjVRIZmQ4KoOFSSoYDl6Q/zh-cn_image_0000002644931554.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2C5011F633D9A6E3B6A706C99B920E0E6396E924573521A7B47D6CA2C7F8000 "点击放大")

### 修复建议与问题闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Q_tMLrPSSsGOY2fq0reSSQ/zh-cn_image_0000002675091265.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=436113265F6F0033CD04457806288680619B37D23B79759EA600EDAA87D7AFD8 "点击放大")

**问题闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修复，并关注新版本的冻屏数据。
2. 对比修复前后的问题发生率，确认修复是否有效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/wesjlQaWTE21BzJSeDG6JA/zh-cn_image_0000002675011421.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3490675AD7F216BF6419B72EF17C4EBDDDD4FEBEBD6E63D9D848529D68C21B59 "点击放大")

**故障模式库**

故障模式库中会收录常见的应用冻屏事件，针对不同的冻屏事件提供最佳实践和修复方案，并提供案例库，收录冻屏问题案例和解决过程。开发者可以根据故障匹配到对应的案例，更方便高效的优化问题。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

### Operation Analyzer平台入口

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，点击后选择应用，再点击应用冻屏即可查看该类故障数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/uwI7k09pRK6prMqThG-jbw/zh-cn_image_0000002645091470.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1966F38909F35405946E48725F4E1ACF1C2DAA2B8DD84099130A5FCEA310E641 "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/5qSj-RK8SXavb0R7C2LIzw/zh-cn_image_0000002644931558.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E6D6253D65499FA21450CDBE61DCF19CDDD70E7765CE072E0EFDCC6CCF0FD4F "点击放大")

### 问题分析

**Operation Analyzer平台问题查看**

开发者可自定义筛选条件来筛选需要查看的问题，可点击功能列表下具体的问题进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/WUKPTjZqR_e-z7YwuNl1qA/zh-cn_image_0000002675091269.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=510E38A8B9C0092276D60161DFA31F516E2D5CA2CFF00891B91EA3BEEAE6C2EB "点击放大")

开发者也可以点击耗时函数列表，然后点击具体的耗时函数，进一步查看问题详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/KoCX7h8XT_2kaCSGwQCy5g/zh-cn_image_0000002675011423.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FF286A076716BA8E7516F10EEDCEABA98E6717DFFAE433042B0C73DC22F7901 "点击放大")

**Operation Analyzer平台问题详情**

平台的问题详情页同APMS平台功能相同，开发者可查看故障分析与修复建议排查问题。如果修复建议不能支撑解决问题，可进一步查看证据链、现场数据、采样栈日志进行具体分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/pYrkthj-T6q64nVL9-tL9g/zh-cn_image_0000002645091472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=33E631B287D7DEF8B02671969312143BD2AC78B27C5A0BB6EB858DBE4280FAFB "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/M4777pvhQFGq1blSig6cgg/zh-cn_image_0000002644931560.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E74F2B0FC89FFAB9D516948208A6A2F975559A44C3A0C763DAAF0109A3C5C911 "点击放大")

**Operation Analyzer关联离线符号表**

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/-mtPpnh8Tk2jLvDAFidrRw/zh-cn_image_0000002675091271.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D31CF87CF85AAACCF61E84AF964196BEE8BD99E2CDECD91F4F4F9528C63034B9 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/ewy-X7wUTl-RS7fKU6rzsQ/zh-cn_image_0000002675011425.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1635BB5745F30B4453B20DDED1F4E3465A9B462D13FB211550335F9823F6971E "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/yLahylcIQpCAhiaxrcAlUg/zh-cn_image_0000002645091474.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=26A94CC5D9B8D6BB139AFAE37ED3EEC37FC1BA4F71E1977B07579F7FF9F0BA9A "点击放大")

**Operation Analyzer关联代码**

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/LrGYwshZTUSdGsj10clrmA/zh-cn_image_0000002644931562.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBF09629BEE97E2C32EBDFC914C3F011AEC2E509B6DCFBB6DA2AA05D9C4AFB6B "点击放大")

点击故障处可跳转到源码中对应的代码行，可辅助开发者更高效的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/XI84G4CSRi-CvfAnnLFLSA/zh-cn_image_0000002675091273.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FDAC3975F9DE123CACA3FF3685586CAF4BD422B43288A8B3F8EDBDF7C8780A8 "点击放大")

### 问题修复

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/EXkKiN3bRemYRrK8KOO82Q/zh-cn_image_0000002675011427.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=5485129AE862A6B7F8BBF3ECC4C8491FA4374EC3FD7589674C876C7642C42347 "点击放大")
