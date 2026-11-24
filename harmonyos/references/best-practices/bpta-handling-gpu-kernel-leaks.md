---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-handling-gpu-kernel-leaks
title: 运维态高效处理GPU内核泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理GPU内核泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:42c1b1e5cc13410df50b6b3df7e14192c25b30f491fea4abe1f9db486fb47e0f
---

## 概述

GPU内核泄漏是常见的泄漏类型，也是应用稳定性优化的重点方向。本文档主要介绍在运维态下通过应用质量管理（APMS）（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行GPU内核泄漏的监控、分析、定位与修复的完整处理方法。

## 运维态GPU内核泄漏分析流程

### 标准化排查流程

**整体流程图**

整体排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/jRC0z6h5QRuGvRwnEYwNUQ/zh-cn_image_0000002671626374.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=39F940E8B0FCA434E119AEC7AE036DEC30D318203125FE24FBD300EA22974F52 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/r--kTVv-R42xCIQeDsaP6A/zh-cn_image_0000002701226099.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFF0C86A3C1AA1A4F27E206DE9552AC888F3819C671D14FA9425D5E81CC28A43 "点击放大")

TOP问题列表根据最大泄漏数进行排序，开发者可单击查看按钮进入故障详情页查看问题的详细信息，进一步分析问题。

**提取故障详情页关键信息**

进入故障详情页后，需要重点关注问题详情页的以下信息：

* 泄漏趋势图表

  进入问题详情页后，单击下钻分析可设置筛选条件查看当前根因的GPU内核泄漏在不同时间、不同版本、不同设备维度的发生频率。例如，某次版本更新后该类泄漏量激增，可以提示新引入的问题。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/sV2DRhMtRYuEUM4OGPZJNA/zh-cn_image_0000002701346199.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=B56352ADBFA2ECFF91A2C0587AE561FA5DBBC5491CE463260E305944A6B78BC1 "点击放大")
* 分析报告

  分析报告包括设备信息、系统版本、应用版本、ROM版本、前后台状态等，帮助开发者判断GPU内核泄漏发生的具体环境。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SpeyniQ7R5SMnBtONvfU4A/zh-cn_image_0000002671466522.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=05C2FF251398A850296DEF812BCAF83A344F70D9F0E1E2D803126363CA6ACA55 "点击放大")
* 证据链

  开发者可以通过单击证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注，帮助快速定位泄漏信息。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Vkkais8pS9yKWSN_p0pk9A/zh-cn_image_0000002671626376.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C72385C61341DFF78C8A493B20EA7CCD9963A5406A4CB04D552E6C643CDC7EED "点击放大")
* 现场数据

  单击现场数据可查看GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/sXEL-RRqQu2yehUorUOaOA/zh-cn_image_0000002701226101.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=75BABC0C7FD02035552CA4CE38A1089E920D5210766EBB0BE766A492B70C6F84 "点击放大")
* 采样栈还原堆栈

  通过上传.map或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/IFKROLU6Qde5LZEWaHrEEw/zh-cn_image_0000002701346201.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF92CDFD811A4888C9D55AB6326EA6F213F3C925793AF00477F0B0A29554C137 "点击放大")

## APMS平台GPU内核泄漏问题分析案例

### 创建灰度任务

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)功能后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS 故障预警

1. **配置告警规则**

在故障预警平台的告警规则页面创建告警。根据实际业务情况，选择合适的监控时段、监控频率、告警触发条件等。平台将GPU\_LEAK归属到MEMORY\_LEAK，因此开发者在配置告警规则时指标类型需要选择MEMORY\_LEAK。配置完告警规则后，平台才会触发告警。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/D9kXC2_xTe2h96xliXGdSg/zh-cn_image_0000002671466524.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=06E34F32296CE20955BA380358217494106E7A42EB2F9F4933F94F1E58902F14 "点击放大")

2. **查看告警**

配置告警规则后，当应用触发MEMORY\_LEAK事件后设备会进行上报故障信息。APMS平台会开始收集后台数据，当满足告警触发条件后，会触发预警。收到预警后，单击查看可进入故障指标页面。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/MFNbIFgRTtSUMl1AVYMf8A/zh-cn_image_0000002671626378.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C2C1FEC7D77EAEE6FFA2EBE42C1ED1A67027DE5A28790100FAF361C6D369799 "点击放大")

3. **查看故障数据**

查看故障数据的方式有两种，分别是通过故障指标页查看故障数据和通过故障分析页查看故障数据。

* 通过故障指标页查看故障数据

  故障指标页面包含了趋势分析、维度分布和TOP问题列表。开发者可以在界面选择GPU\_LEAK泄漏类型并设置筛选条件，以过滤出GPU内核泄漏数据，从而进行个性化分析。TOP问题列表根据最大泄漏数进行排序，开发者可结合问题状态筛选需要优先处理的问题。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/h04nltjcQ7SPmA8Bji96Pw/zh-cn_image_0000002701226103.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA52463E7EE6AB08748C248929F7F7500DCD2B42DA60DA5426ED4236A2A8EA64 "点击放大")
* 通过故障分析页查看故障数据

  开发者也可以直接单击故障分析页面，经过条件筛选后可查看具体的TOP问题列表。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/1Qkqc5a1Q6ar_eCJ71PVTA/zh-cn_image_0000002701346203.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D3EB3A2D75AAA76E9F2C91FB6C325C07A7F9665C7B06BD73FAD9FC0F343501C "点击放大")

### 问题查看与聚类

**聚类规则说明**

相同特征ID：平台会将GPU内核泄漏的数据根据相同故障模块聚合成一条记录，生成问题特征ID。

**TOP问题查看**

筛选GPU内核泄漏问题范围：在界面可以设置不同的筛选条件对GPU内核泄漏问题进行个性化分析。筛选条件设置完成后单击“查询”，即可查看指定时间范围和条件下的三类指标数据的变化趋势，包括泄漏率、泄漏次数、泄漏设备数。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/KfpvjWu4SQmZ4NdGjO8JNA/zh-cn_image_0000002671466528.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1C0FFAB75F58DBCE987871B312D4FC970D2E2ECE0779C5B2C50F752ED5219B8 "点击放大")

**TOP根因聚类**

完成筛选后，开发者可进一步查看TOP问题列表，在问题列表中，每个问题都是同一类问题的汇总。APMS平台会将具有相同特征ID的问题聚合成一个，并按照发生次数进行排序，开发者可高优先级处理TOP问题。单击“查看”进入问题详情页，进一步查看问题详情。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/yqHFmop6SwyUWT7TJNOMUg/zh-cn_image_0000002671626380.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0A0C59556641B333416BA00E7FB280032CE7A09FE8B170535D78B35B6FA0FCE "点击放大")

### 根因定位与分析

单击资源泄漏信息详情列表某个问题进入详情页后，开发者可按照如下步骤定位问题根因。

**基础定位信息分析**

1. 查看问题概要：问题概要会展示问题的核心身份信息，包括问题特征ID、故障原因、故障模块，帮助开发者快速判断GPU内核泄漏的基本属性。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/NyUMyF8cQBKxqFzQKVDBBw/zh-cn_image_0000002701226107.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A6030BF8BDD202297BC6406D925A50AD84B30330C2F6DC7C9C0CB6D1C48BBAC "点击放大")

2. 查看分析报告：分析报告会提供问题发生时的完整上下文，包括环境信息（设备型号、系统版本、ROM版本、前后台状态等）、堆栈信息、日志文件，并基于分析结果给出修复建议，辅助开发者高效完成问题排查与闭环。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/WAzfHMoeSeKYUXVKp3nXxg/zh-cn_image_0000002701346205.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C279412DF3BE5B9DA79AA202BE8A9347907B5B3BCE3F2B288B612D9A0051A5D4 "点击放大")

3. 查看故障详情：开发者可根据平台给出的修复建议定位代码问题，完成问题修复。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/w1pv4yKfQaK3Rl-LkUTibA/zh-cn_image_0000002671466530.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D40CC4952E72126574DA4CFE167427658FBC349CFE84C98F09AACC990C6A6B2 "点击放大")

4. 查看证据链：开发者可以通过证据链查看主泄漏堆块、主泄漏方法以及分配栈信息，其中疑似泄漏点会高亮标注。开发者可结合分配栈中的方法信息定位到业务代码中的泄漏处。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/J11tyvREQuCGgZ5Rl3y2yg/zh-cn_image_0000002671626382.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=7248B9D328482A08B16A44E61B591FD90A34B2ADD032E936126CE9D14189FEF4 "点击放大")

5. 查看现场数据：现场数据展示了GPU内核泄漏的具体泄漏类型、图片大小、图片数据量以及总泄漏大小。开发者可结合证据链中的堆栈信息，对比图片数据分析泄漏原因，从而定位具体泄漏位置。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/lpJk5SVTRqm8mNbHxK1Ung/zh-cn_image_0000002701226109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB11FB2F524677A7500631FEE6CDD00F226FEE660CAD7CFB8A009D527F710848 "点击放大")

6. 查看采样栈信息：通过上传SourceMap或.so符号表文件，可将混淆后的堆栈地址还原为可读的代码行号与函数名。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/fSBL1BTqT5SeYHcHsLgnoA/zh-cn_image_0000002701346207.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC639632E1C418FB0D88F9F60B2322358B6BD7C4FEA80982CFC1E6CCE680C01E "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分。然后筛选出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选TOP应用版本、系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确地定位问题。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/W9iA6iPFRZCujFzIRGc_nw/zh-cn_image_0000002671466532.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=56A369027E360CE8458E6DD49126366E3F003E1929A88003FBFD26029A98309B "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会给到修复建议，开发者可以通过给出的建议优化代码。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/MPgpwvcnRM-scepHJESmXg/zh-cn_image_0000002671626384.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=806287C330B9205AE9ACA79922EC70DBA400A613905080319CC2502C89496253 "点击放大")

**修复建议与闭环**

1. 修改问题之后，可以在分析页面的问题列表中，将对应的问题处标记已修改，并关注新版本的GPU内核泄漏数据。
2. 应用发布后，可在故障分析页面筛选新版本数据和旧版本数据，对比修复前后的泄漏率，确认修复是否有效。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/iSzd7tExSZivZpT7q4Bw_w/zh-cn_image_0000002701226111.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C13877E4A5E6A9662E41366528A90C68EBDBBB16888C5C90844492DE658DB355 "点击放大")

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件。在DevEco Studio上可以通过此插件查看到应用对应的故障数据，数据和APMS平台上一致。

**Operation Analyzer平台入口**

打开DevEco Studio后，在左侧可看到Operation Analyzer图标，单击后选择应用，再单击资源泄漏，查看GPU\_LEAK类型的数据。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/yoXdl2GURlyZR_s2GTU-zQ/zh-cn_image_0000002701346209.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=0322E8E6D1E92640B06265E1C01A45E9BDF7FAB91CFB99B2811999FEAAF2BBB8 "点击放大")

如果左侧没有出现Operation Analyzer平台图标，也可通过上方导航栏的视图窗口进入。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/DPdZTVP8Sc2HxFXHR0kBbQ/zh-cn_image_0000002671466534.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE91EFFB348F26F579A151082D8DB8E7A609DB72DACF1CA2D677C9A1AB589FF4 "点击放大")

**问题分析**

* Operation Analyzer平台问题查看

开发者可自定义筛选条件，筛选需要查看的问题，单击TOP Issues，选择下方类型为GPU\_LEAK的数据，单击即可查看当前GPU内核泄漏问题的详细信息。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/OpW-Ypo7Q9OhcluKmzgowQ/zh-cn_image_0000002671626386.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D234856F481D566AB33D8C27D07A80725B02AB5A6BD712097A9D18DB13AEC9A4 "点击放大")

平台的问题详情页同APMS平台功能相同，开发者可参考修复建议进行修复。如果修复建议不能支撑解决，可进一步查看证据链、现场数据进行具体分析。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/UEC26NToSQSjSh9uvLdPaQ/zh-cn_image_0000002701226115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=12752103888610C3844D7DF8EB66A889DCCCB67CD2F7C681382A92ED3E7EB799 "点击放大")

开发者也可以查看问题分布图表，定位问题高发的应用版本、设备型号与系统版本，辅助进一步分析。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/JRyWkTRgR6igJHojUcF0Bw/zh-cn_image_0000002701346211.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=74B8D96CAF732C45C83242000DF3AEAF174041E25F48CA15DD204DE036590C9C "点击放大")

* Operation Analyzer关联离线符号表

Operation Analyzer平台提供了堆栈还原的能力，可以通过上传符号表（.so/.map/.json文件）完成堆栈还原，辅助分析问题。

选择本地符号表，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/blEcUpfeSDuXjhH61_EYzQ/zh-cn_image_0000002671466538.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1376FA194A9C5029AE032687E9E61A85A5E15261C57021379CCB51812601F8B "点击放大")

完成堆栈还原，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/UwWU_kt_QgGkBEg777hVfw/zh-cn_image_0000002671626390.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B7B079BB2DCC344505A7BD136BD12C4E77B84CC39979DB16D88AB52CB5F947A "点击放大")

* Operation Analyzer关联代码

堆栈还原后，Operation Analyzer平台可将故障处与项目代码相关联，单击故障处可跳转到对应源码中，可辅助开发者更高效地定位问题。

关联项目代码，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/kd72d0fxQKem1q_JBy7x_w/zh-cn_image_0000002701226117.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C478BD9C65BC34A3F4C5E216E9B4B3F2B59B95C9C32129F1B794E24B400C283 "点击放大")

关联效果确认，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/KgJBSAWqRJWU2_cZ1HdcbQ/zh-cn_image_0000002701346213.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFB5AD154DDE011CD5867A627739C5492C1D280715F3783D8BC3E0511E8E72B3 "点击放大")

**问题修复**

Operation Analyzer平台会给出故障分析与修复建议，开发者可根据修复建议修复问题代码。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/F1sBSBtHQ7qvb9aFOXKsSA/zh-cn_image_0000002671466544.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=18278593F5327C68AC1883705BF2401A52E7D43F8C1877CE50A329C11D3AFC93 "点击放大")
