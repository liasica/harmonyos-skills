---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-gpu-kernel-leaks
title: 运维态高效处理GPU内核泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理GPU内核泄漏
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:4549d2f3fa0c32afd707a976d501a95fa5ad994d10d871ac2567af9916c57ab8
---

## 概述

GPU内核泄漏是常见的泄漏类型，也是应用稳定性优化的重点方向。本文档主要介绍在运维态下通过应用质量管理（APMS）（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行GPU内核泄漏的监控、分析、定位与修复的完整处理方法。

## 运维态GPU内核泄漏分析流程

### 标准化排查流程

**整体流程图**

整体排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/YpsMcdMKRPOzYaul8KLcgQ/zh-cn_image_0000002671626374.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE405CB1F098647E1DFC8E9BFAAB12F1A65A7581A0515F487AAB32BDB033183C "点击放大")

**排查步骤**

1. [创建灰度任务](bpta-handling-gpu-kernel-leaks.md#section15567161021317)：在端侧集成应用灰度采集功能，通过云端平台发布应用灰度任务，圈选设备开启故障日志精准采集。
2. [APMS 故障预警](bpta-handling-gpu-kernel-leaks.md#section0763145018135)：在APMS平台配置内核泄漏监控告警规则，设置监控时段、频率和触发条件。
3. [问题查看与聚类](bpta-handling-gpu-kernel-leaks.md#section1182182471617)：通过APMS故障指标、APMS故障分析页面，可筛选GPU内核泄漏的问题，查看泄漏趋势图与TOP问题列表。
4. [根因定位与分析](bpta-handling-gpu-kernel-leaks.md#section161116262205)：通过分析故障模块、发生次数、影响设备数与最大泄漏数等关键信息，定位高优先级问题。查看问题详情，通过证据链与现场数据，深入分析泄漏原因。
5. [修复建议验证与闭环](bpta-handling-gpu-kernel-leaks.md#section1150784112617)：根据修复建议优化代码，并验证修复效果，形成闭环。

具体排查操作步骤可参考：[APMS平台GPU内核泄漏问题分析案例](bpta-handling-gpu-kernel-leaks.md#section9116152181116)。

### 指标监控与关键信息提取

**查找内核泄漏关键问题**

进入故障分析页面，单击资源泄漏，在泄漏类型处选择MEMORY\_LEAK/GPU\_LEAK，单击查询后再单击TOP问题即可查看GPU\_LEAK类型的问题数据。开发者可选择问题状态为未解决或者处理中的问题进行处理。同时，开发者应关注如下指标，进一步分析问题。关键指标说明如下：

* 故障模块：发生GPU内核泄漏的模块或组件，用于定位问题范围
* 发生次数（占比）：GPU内核泄漏发生的次数及占比，帮助判断问题出现的概率
* 影响设备数（占比）：受影响的设备数量及占比，评估设备层面的影响
* 最大泄漏数：GPU内核泄漏的内存大小

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/HvO553WDRjO4nqkcBw7AGw/zh-cn_image_0000002701226099.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=68AD7762A5DABC8528550B40F6892E010926B833E17275138D081FD9671E6EAA "点击放大")

TOP问题列表根据最大泄漏数进行排序，开发者可单击查看按钮进入故障详情页查看问题的详细信息，进一步分析问题。

**提取故障详情页关键信息**

进入故障详情页后，需要重点关注问题详情页的以下信息：

* 泄漏趋势图表

  进入问题详情页后，单击下钻分析可设置筛选条件查看当前根因的GPU内核泄漏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类泄漏量激增，可以提示新引入的问题。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/w4v9fysiTK6ZSWja49Cgjw/zh-cn_image_0000002701346199.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=07BD6BE5432681FACBDAB55384AA49F2C09A8CF85700FFA2C40BFBB78C7DFEB5 "点击放大")
* 分析报告

  分析报告包括设备信息、系统版本、应用版本、ROM版本、前后台状态等，帮助开发者判断GPU内核泄漏发生的具体环境。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/Wb9oE1jGRFqWgPVckRKgXg/zh-cn_image_0000002671466522.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=D516E8A41FAF387246CAE2F9C8E674FAA033C6923B1421AA61BBBAA80F6993C7 "点击放大")
* 证据链

  开发者可以通过单击证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注，帮助快速定位泄漏信息。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/-Jt071Y4RrOtz8pBG_NFcA/zh-cn_image_0000002671626376.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=969C91FAC807AF4C10C0D57ADDF6DD9F8CF23F70439A2D0C3A0ECBA5AD017BD2 "点击放大")
* 现场数据

  单击现场数据可查看GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/gTmPkwDaQmCIWg0idqvMUQ/zh-cn_image_0000002701226101.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B63C6CD07DF31D565607E5A1266EB0782972D1D7A1A2D88B5B1D80D44E73ACDD "点击放大")
* 采样栈还原堆栈

  通过上传.map或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/tisJwo7ESwi8yr4t737R2A/zh-cn_image_0000002701346201.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7FDCB26F92F5B2E3AAFF2BDFAEA5D07BFF98C8AA2C579E0DE87DAF497FC280A "点击放大")

## APMS平台GPU内核泄漏问题分析案例

### 创建灰度任务

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS 故障预警

1. **配置告警规则**

在故障预警平台的告警规则页面创建告警。根据实际业务情况，选择合适的监控时段、监控频率、告警触发条件等。平台将GPU\_LEAK归属到MEMORY\_LEAK，因此开发者在配置告警规则时指标类型需要选择MEMORY\_LEAK。配置完告警规则后，平台才会触发告警。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/5ySfto_MQ_O7DCwe1skZMw/zh-cn_image_0000002671466524.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=445E49521EECFCC707F1951FDCE9A27D06F9D5A79F4B4E44A63C245379B1DCE5 "点击放大")

2. **查看告警**

配置告警规则后，当应用触发MEMORY\_LEAK事件后设备会进行上报故障信息。APMS平台会开始收集后台数据，当满足告警触发条件后，会触发预警。收到预警后，单击查看可进入故障指标页面。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/QdtovUPeStuEdFvMfWOkUA/zh-cn_image_0000002671626378.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBD240B54C4FAAF692C68736BFAA78933229ABB57B554C511FC7FCE9D34C408A "点击放大")

3. **查看故障数据**

查看故障数据的方式有两种，分别是通过故障指标页查看故障数据和通过故障分析页查看故障数据。

* 通过故障指标页查看故障数据

  故障指标页面包含了趋势分析、维度分布和TOP问题列表。开发者可以在界面选择GPU\_LEAK泄漏类型并设置筛选条件，以过滤出GPU内核泄漏数据，从而进行个性化分析。TOP问题列表根据最大泄漏数进行排序，开发者可结合问题状态筛选需要优先处理的问题。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/HN4TZ5OdSHqQ7K1szbdOXA/zh-cn_image_0000002701226103.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E89DEA7F2B1A89E499091AD48FE120C63BF753A376C84CBC75D40C986090195 "点击放大")
* 通过故障分析页查看故障数据

  开发者也可以直接单击故障分析页面，经过条件筛选后可查看具体的TOP问题列表。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/nV_4bRKLTxm23Ss7qEW_sA/zh-cn_image_0000002701346203.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=42FF3046F6B7D3A98F995C0FDD8A678BEA4F2D7DC927DD52F8D4F756A3C3FBC5 "点击放大")

### 问题查看与聚类

**聚类规则说明**

相同特征ID：平台会将GPU内核泄漏的数据根据相同故障模块聚合成一条记录，生成问题特征ID。

**TOP问题查看**

筛选GPU内核泄漏问题范围：在界面可以设置不同的筛选条件对GPU内核泄漏问题进行个性化分析。筛选条件设置完成后单击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括泄漏率、泄漏次数、泄漏设备数。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/5R6b3nq2TvenRC9PorITOA/zh-cn_image_0000002671466528.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=63A694D17F8FC734CC9B8C550A2E6A4584C4BE297587269665F0DFFC9BB9259F "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一个，并按照发生次数进行排序，开发者可高优先级处理TOP问题。单击“查看”进入问题详情页，进一步查看问题详情。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/4I0wPmTaQlKZuIseJ-Sgmw/zh-cn_image_0000002671626380.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2EFEFF9F238B16159D66622DEAFFD38D19F6AAE23B3C0AEE34823D39310537D "点击放大")

### 根因定位与分析

单击资源泄漏信息详情列表某个问题进入详情页后，开发者可按照如下步骤定位问题根因。

**基础定位信息分析**

1. 查看问题概要：问题概要会展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断GPU内核泄漏的基本属性。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/1gFhzflJQBmZoByAFLmCLQ/zh-cn_image_0000002701226107.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4ED20BA3D794943FCC856EC4DA9B7118162C41D79470D1BC5CC7352A2DD4597 "点击放大")

2. 查看分析报告：分析报告会提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/q5ALc0i3RNyfeVqn5yEijA/zh-cn_image_0000002701346205.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B10D13E703803A73711F5CBE3F97C9944439EBAE282BBE5DE91F54864AF64DDC "点击放大")

3. 查看故障详情：开发者可根据平台给出的修复建议定位代码问题，完成问题修复。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/9Mo1ioJRQwO9w2pbllcu_A/zh-cn_image_0000002671466530.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A6DA1B532A0FC609C42ADB5CA11022403360660BC688863924077F0BB43832E "点击放大")

4. 查看证据链：开发者可以通过证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注。开发者可结合分配栈中的方法信息定位到业务代码中的泄漏处。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/BcWC_CrVTFyaUPi2CRAiqQ/zh-cn_image_0000002671626382.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=E50D736E0AF16248D559D7BAC29707BA8150B8EBCA39627F443B95418DF659DC "点击放大")

5. 查看现场数据：现场数据展示了GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/VFHmz8owSgWxpfYYW_9M8g/zh-cn_image_0000002701226109.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=101DB901A8368A383DBEAFE9C842BEC5AABA540D5ECE72F606836C388579BAAD "点击放大")

6. 查看采样栈信息：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Za5FeUS1Q1OcfUjOdZ864w/zh-cn_image_0000002701346207.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2A771F54B8F767D04B7DBAE2DA29B6FA02B5D655722828A8AEAAE9CC135AB12 "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分。然后筛选出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确地定位问题。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-YCsvW7XTcipZ1zRaeArxA/zh-cn_image_0000002671466532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7C28F6D88C6577314B656283690CF83A7F3C650B9A206CC296B6D38006C2AF4 "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/EKpzyriFQRCbBHNjFyFMnQ/zh-cn_image_0000002671626384.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD3E55A4C33816A67FD88153D4D236230C9B4D1ACE1F7991A6C9F9CE5664D65C "点击放大")

**修复建议与闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修改，并关注新版本的GPU内核泄漏数据。
2. 应用发布后，可在故障分析页面筛选新版本数据和旧版本数据，对比修复前后的泄漏率，确认修复是否有效。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/U0IevHXAR8-YTy7a2tfrYw/zh-cn_image_0000002701226111.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=C576CD02E55C52A196A6915DBB9130DDE19223541202E58728C83DFC1DFFAFB7 "点击放大")

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

**Operation Analyzer平台入口**

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，单击后选择应用，再单击资源泄漏，查看GPU\_LEAK类型的数据。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/4ScST0YbTOGE-fDSz8-57A/zh-cn_image_0000002701346209.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=641AC6E05792EA2A6B44F3EDD02A4DDFFED437C338E4A18F3120E5B0A1078CDB "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/D_MEkU3ZSh6QJqG_IzPuCA/zh-cn_image_0000002671466534.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=57CCB84246B48823F3A52A32C2F1199D2035B8003D6379684B422C26251F3CAA "点击放大")

**问题分析**

* Operation Analyzer平台问题查看

开发者可自定义筛选条件，筛选需要查看的问题，单击TOP Issues，选择下方类型为GPU\_LEAK的数据，单击即可查看当前GPU内核泄漏问题的详细信息。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/OvxwAT2_TiSQXknvanJnkA/zh-cn_image_0000002671626386.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CAC448591616C8D14557AC6D301ECAA518DB339410B6D92D5A2D1BD97FDB62B "点击放大")

平台的问题详情页同APMS平台功能相同，开发者可参考修复建议进行修复。如果修复建议不能支撑解决，可进一步查看证据链、现场数据进行具体分析。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/KKfFjLzzTgGtDRiFx5s1ig/zh-cn_image_0000002701226115.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0862D435E5B44047026942674EB445FC398E8EDDAC1D9D06871C0584BB6E68C0 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_98-uL1QRFaWgifqIASuNg/zh-cn_image_0000002701346211.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B8B4DABB068B9E635C54E42CE1745A9A7A7B6A3BF5BA257164D1FFB83C5427A "点击放大")

* Operation Analyzer关联离线符号表

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

选择本地符号表，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/J4crsAlkT6eD318XXYisgw/zh-cn_image_0000002671466538.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=79D5E9F513AC1250901710EB49B176F7EEEE4430F1A89184775A0077919FFE73 "点击放大")

完成堆栈还原，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/MdIyM8luRoee_rE0ughq_Q/zh-cn_image_0000002671626390.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=10C29A53BBDE24607C658D5560CFF65F253120FB60E5C58635446B742C788FCD "点击放大")

* Operation Analyzer关联代码

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效地定位问题。

关联项目代码，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/RbyN_aeoTwGhbBCgXLY28A/zh-cn_image_0000002701226117.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=20057B1D15AF9D59872224826FC2C6D1D50D4FA9F20E549C47387B436B86E389 "点击放大")

关联效果确认，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Uua8RY-KREy1hBppRODYsg/zh-cn_image_0000002701346213.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=66542CDD776BAE680248D2B49FCC64692FD7A54AD8BDA9AF415786E2DE3E2078 "点击放大")

**问题修复**

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/yANYZX0RS32XVYPAuRoJiw/zh-cn_image_0000002671466544.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=A740A17BB8D2D58BE7B4DE87D02A2EDDCA55FCB38DBED7ED2AD6D546950AFA02 "点击放大")
