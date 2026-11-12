---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-efficiently-handle-fd-leaks
title: 运维态高效处理FD资源泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理FD资源泄漏
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:bcde0f9c7c0e94238acf14bf469b6100f9aa2f833d25d99c97ab995187574f9e
---

## 概述

FD（全称：File Descriptor，文件描述符）资源泄漏是一种比较常见的泄漏类型，也是应用稳定性优化的重要问题。本文档主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行FD资源泄漏的监控、分析、定位与修复整套处理方法。

## 运维态FD资源泄漏分析流程

### 标准化排查流程

**整体流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/BVwQl6mKQg2aMmCjlGHSDg/zh-cn_image_0000002671650762.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CB2BEA8A060C6169CAA5BC820792CF4ED40CE4F85116BD2CE97ED24992E4D06 "点击放大")

**排查步骤**

1. **故障预警配置：**在APMS平台配置FD泄漏监控告警规则，设置监控时段、频率和触发条件。
2. **问题发现与筛选：**通过故障预警或主动分析页面，筛选FD\_LEAK类型的泄漏问题。
3. **关键信息提取****：**分析故障模块、发生次数、影响设备数等关键信息，定位高优问题。
4. **根因定位****：**通过证据链、持有链分布和现场数据，深入分析泄漏原因。
5. **修复与验证：**根据修复建议优化代码，并验证修复效果，形成闭环。

### 指标监控与关键信息提取

**资源泄漏监控信息详情**

故障分析表格会将相同根因类型的故障聚类并排序。表格会展示故障模块、发生次数（占比）、影响设备数（占比）等关键信息，开发者可以通过发生占比和故障模块结合业务实际情况找出高优的问题，并在问题状态和优先级这一栏做出标记，优先解决高优先级的问题。

如下图所示，页面入口：故障分析->资源泄漏->资源泄漏信息详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Y5tVWb-bSY68QPwX36BHmA/zh-cn_image_0000002701370585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE769D4E42902503ED44D7D9D9BEB29E6199B1758248B417364F8F3492D325C0 "点击放大")

**关键指标说明**

* 问题特征ID：故障模块的哈希值，同类故障模块会聚类到一起。
* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大句柄数。

**故障详情页面介绍**

通过点击查看按钮，进入到故障详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/PmStdOWzTDCGM1mlfB00oQ/zh-cn_image_0000002701250493.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=305B03E93543317A6CA96F3F7B0AB8B73E5118ACD66190B9C9F48670252C17CD "点击放大")

故障详情页面可以通过证据链、现场数据、句柄栈信息进一步深入分析泄漏的原因。

**证据链**

证据链列表根据泄漏数量的大小排序，优先查看泄漏数量最大的句柄名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/jhaLB0sNTQi9_2ciiMvDeA/zh-cn_image_0000002671490912.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=3950E90884FA82D084A2E80A15ED2E175538A023B71F0DAACFEB30DE4D2AD5D7 "点击放大")

**现场数据**

现场数据展示了当前FD泄漏的Top10的句柄名称，可结合代码、日志分析对应的FD泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/PQADxx9YS-WErfYjnQWD_w/zh-cn_image_0000002671650764.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA7DAF092FA691EF06E6950C62C62FB7F3746C9AE65B534AD21FEE9AC6E6B268 "点击放大")

**句柄栈信息**

句柄栈信息中可查看对应的堆栈信息，以及疑似泄漏点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/i4QwUVP0R2mwUG0pBU3pSQ/zh-cn_image_0000002701370587.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=39D2E3C6209D734E07821910D0D303C5267010437F9F99A9935DFEA724FE9E68 "点击放大")

## APMS平台FD泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度采集功能（可参考：[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)）后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

在故障预警平台的告警规则页面新建FD泄漏告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中FD泄漏对应的指标类型为FD\_LEAK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/nHY7vlWETC6xJRomb1pLPw/zh-cn_image_0000002701250495.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F19DB4CA69CE2E1CEDA536B04D233EDD03C8E07D59721669652170B8433B613 "点击放大")

创建告警之后，后台会开始收集数据。当达到设置的告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/l8t8HZr4Rmm3Zl8SsxCAxg/zh-cn_image_0000002671490914.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=29213A4FBE6C61364A8B8FAA5086A06173E9F30FD13540D538DA963A32043008 "点击放大")

### 问题查看与聚类

**聚类规则说明**

FD资源泄漏聚类规则请参考[句柄泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏聚类规则)。

**问题查看**

* **Top问题查看**

通过故障告警的指引，在故障分析页面筛选出FD\_LEAK的泄漏类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/5Pv8VhIESwGwig5SEZvdqQ/zh-cn_image_0000002671650774.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2212AD5A20BF4DF0CDC05E1BA604DB3609D280C139DEDCC500121684A99FCFA "点击放大")

点击查看按钮，即可跳转到Top问题查看页签下的FD资源泄漏问题列表。

* **资源泄漏信息详情Top问题**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为FD\_LEAK，点击查询按钮，过滤出此应用的FD资源泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/qpSYqMx0T3yKuFsUbBHV6g/zh-cn_image_0000002701370625.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0140BE6D888BC8AC04955839FFB1C8D54AD3A05093565126EA339C64713868C7 "点击放大")

在资源泄漏信息详情中，可查看当前应用的FD资源泄漏情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/DkoavppDRJaREIDkDLpFaA/zh-cn_image_0000002701250559.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=60B412BB8FEB3E08E48680EC3A1427EC040A61EE3CBA19465C1F47BF56F60D33 "点击放大")

### 根因定位与分析

过滤出FD资源泄漏故障列表后，点击查看按钮，进入到问题个例分析详情页，可查看当前故障的分析报告，包含故障发生时间、泄漏句柄、故障模块、版本信息以及修复建议等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/UG9Vqb5gTieFkGAaoTLqeQ/zh-cn_image_0000002671490976.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E0ADB493B776F3424166C3266E3C4D1D318E94CC83D832824F8659205AF36E7 "点击放大")

**证据链分析**

证据链列表中按照泄漏数量倒序排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。同时提供了日志下载功能，便于进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/F-2OgDKKQaiElA3-nl-fFA/zh-cn_image_0000002671650846.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E1E64B5952D5E0093234D3C39933FE5CDF5E65E81FE43EBE5B01FF2BC100EAE "点击放大")

**现场数据分析**

现场数据页中，将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/naqweppgRxKL83z1w80OiA/zh-cn_image_0000002701370681.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF2BD0369A95E3DBF30A538CC5424F01BA96C3CB7908CFBD8D83A9218CBE8A33 "点击放大")

**句柄栈信息****分析**

句柄栈信息是发生FD泄漏故障并达到一定条件后，系统从堆栈中抓取的堆栈信息，存在一定的滞后性。开发者可参考堆栈中的疑似泄漏点，进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/6qCCaHVuTYWLs5YJTGsUKw/zh-cn_image_0000002701250593.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E469010BEFA83A593FB79572ABF7E9C83E119BB7ACB51464929CFBBD82F36DA "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选Top应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/yoHE0BPVR1SBUgj9gPqNkQ/zh-cn_image_0000002671491006.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=63E547D0AAEE6155F501D6EC856DAF74FCE4E675EEFE1F3221CCF5ED4936D54B "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/RglFv560Q1KZMTnpK-mmjQ/zh-cn_image_0000002671650858.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FACBD1CE2583DC7839AE9FA84C459663EE6116D0D8789D32A0C713D83F0AB9B "点击放大")

**问题修复与闭环**

* **问题修改**

开发者根据修改建议，在工程中释放FD泄漏对象。

* **问题标记**

优化之后，可以在分析页面对对应的FD泄漏对象标记。

* **应用发布**

应用发布之后，更新平台告警规则，并持续关注新版本的FD资源泄漏数据。对比修复前后的问题发生率，确认修复是否有效。

## 基于Operation Analyzer平台分析

Operation Analyzer平台是指DevEco Studio的Operation Analyzer插件，通过该插件查看到应用对应的故障数据，数据和APMS平台上一致，开发者使用该插件以相同的方式分析运维态的泄漏问题。

### Operation Analyzer平台入口

打开DevEco Studio后，在Tool Windows栏的Operation Analyzer进入平台，点击后根据包名选择应用，再点击资源泄漏（Resource Leak）即可查看该类故障相关数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/WXkqo7NhTheckao1D2MQcw/zh-cn_image_0000002701370683.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=905A16E5AEF7C56EECB21613BD4990DC9EF3EE32089345603654B5DEEC581F20 "点击放大")

### 问题分析

**证据链****分析**

证据链列表中按照泄漏数量排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/8z8xiW0sSJiW0-kT4xlFVw/zh-cn_image_0000002701250595.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABD7ED872B97E8DF37ABB21935AC83A5399AB48778FA5E07F31F48278C36E38D "点击放大")

**现场数据****分析**

现场数据页面将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/Rjyf_lv_SlCXRszGVVQZSw/zh-cn_image_0000002671491008.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD62025E06D240AAA4C0EC21B003AA70728A55453CDFFF6FAB95FF1ECCEF6B5A "点击放大")

**句柄栈****信息****分析**

句柄栈信息中将抓取的堆栈信息中疑似泄漏点进行展示，开发者进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/_MpMeWL7T_Olv5wFpfkgKg/zh-cn_image_0000002671650860.png?HW-CC-KV=V1&HW-CC-Date=20261112T233138Z&HW-CC-Expire=31536000000&HW-CC-Sign=733B8F6AF73B37285480ED1E293ACDF6EC8624F5BE674E4F104EFB69D00D92D5 "点击放大")
