---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-efficiently-handle-fd-leaks
title: 运维态高效处理FD资源泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 运维态稳定性分析 > 资源泄漏类问题分析 > 运维态高效处理FD资源泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:0fa6f937269c5677b8a9a49c7b38ecdc559e3c11e7bfbaba279bfe88e617267a
---

## 概述

FD（全称：File Descriptor，文件描述符）资源泄漏是一种比较常见的泄漏类型，也是应用稳定性优化的重要问题。本文档主要介绍在运维态下如何通过应用质量管理（APMS）平台（[业务介绍](../doccenter-monitoring/agc-help-apms-introduction-0000002236333914.md)）进行FD资源泄漏的监控、分析、定位与修复整套处理方法。

## 运维态FD资源泄漏分析流程

### 标准化排查流程

**整体流程图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/atmy-raxQsmNwVB_50uDzA/zh-cn_image_0000002671650762.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBDA73A5A71F62975D93A66ABF0A345E6509B679C8B8068124A7F72F74D23C76 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/_lOW6ruyTfqldSRp67h7PA/zh-cn_image_0000002701370585.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEEDA4E1153DA42525680C9F86F6E6AF00A561AA50E7A952E94B252ECB9F111F "点击放大")

**关键指标说明**

* 问题特征ID：故障模块的哈希值，同类故障模块会聚类到一起。
* 故障模块：发生泄漏的模块或组件，用于定位问题范围。
* 发生次数（占比）：泄漏问题发生的频率，帮助判断问题严重程度。
* 影响设备数（占比）：受影响的设备数量，评估问题影响面。
* 最大泄漏数：单次泄漏的最大句柄数。

**故障详情页面介绍**

通过点击查看按钮，进入到故障详情页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/fuJuZnAPS3aG02CvT1oquw/zh-cn_image_0000002701250493.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CB2DDBF134437F20C7D8964FD96D73A8AFBD9832EC2E09D89C261E0F075985F "点击放大")

故障详情页面可以通过证据链、现场数据、句柄栈信息进一步深入分析泄漏的原因。

**证据链**

证据链列表根据泄漏数量的大小排序，优先查看泄漏数量最大的句柄名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/0oJYYvCpT8ijhCpmHHRpug/zh-cn_image_0000002671490912.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E055729D93B543CCFB11E5CF7A7C0F5153DD80A74F32C38AA1EA77FD84C23BA4 "点击放大")

**现场数据**

现场数据展示了当前FD泄漏的Top10的句柄名称，可结合代码、日志分析对应的FD泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/2NkPC9s3TKa7IQu6T8kEnA/zh-cn_image_0000002671650764.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=191739C0330782059D3E14CB0D098D04E13A7DEAA1880FCBCF8BE891E848DD59 "点击放大")

**句柄栈信息**

句柄栈信息中可查看对应的堆栈信息，以及疑似泄漏点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/nGtUmd3mQ3KYJwz76H8f6A/zh-cn_image_0000002701370587.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2637A85A1999C88AC7A43B6F5E02A6BF8E1095ECFAF77F8027C72064248D303 "点击放大")

## APMS平台FD泄漏分析案例

### 灰度任务创建

应用灰度特性是一种运维态功能，用于精准采集故障日志。开发者在端侧集成应用灰度采集功能（可参考：[应用灰度采集介绍](../harmonyos-guides/hiretrieval-intro.md)）后，该应用可参与应用灰度活动。通过云端平台进行[灰度采集](../app/agc-help-apms-gray-scale-collect-0000002619401669.md)，可圈选部分设备开启故障日志精准采集，帮助开发者快速定位故障。

### APMS故障预警

在故障预警平台的告警规则页面新建FD泄漏告警。根据实际的业务情况，选择合适监控时段、监控频率、告警触发条件以及其他告警指标，其中FD泄漏对应的指标类型为FD\_LEAK。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/evC1QV16QnGI1BqtbxDIOA/zh-cn_image_0000002701250495.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA91A545B892F796625619C219EC8895B0010C92B38D66BFEEADB32AA10376BE "点击放大")

创建告警之后，后台会开始收集数据。当达到设置的告警阈值后，会触发故障预警。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/p3xAQsLXRT6EpM__AN1b4g/zh-cn_image_0000002671490914.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DC392D8A76E951F797898A336C906D0C44865C57C97E77091869131E784E784 "点击放大")

### 问题查看与聚类

**聚类规则说明**

FD资源泄漏聚类规则请参考[句柄泄漏聚类规则](../harmonyos-guides/resource-leak-guidelines.md#句柄泄漏聚类规则)。

**问题查看**

* **Top问题查看**

通过故障告警的指引，在故障分析页面筛选出FD\_LEAK的泄漏类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/zO_nEOQfRja2FQ4cgk8EsA/zh-cn_image_0000002671650774.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1D4CD116850E9C500328134B9F40564F5318AF126E2B63385B79FBB3C2A7544 "点击放大")

点击查看按钮，即可跳转到Top问题查看页签下的FD资源泄漏问题列表。

* **资源泄漏信息详情Top问题**

在左侧页面APMS菜单下的故障分析菜单中，在资源泄漏页签下选择泄漏类型为FD\_LEAK，点击查询按钮，过滤出此应用的FD资源泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/C1qxWM7qRD2WBYTvtrUt_A/zh-cn_image_0000002701370625.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=79FE65CD06556F78403DB4C9568C24727479903E666E71EE30E8A1B7EA2A41E6 "点击放大")

在资源泄漏信息详情中，可查看当前应用的FD资源泄漏情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/C5mlJl7tSoW82mITF8H3Kw/zh-cn_image_0000002701250559.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=95B7C3C48A8F180E486DC72E0C4984535BD2652BD3A29C090AFAFF33EBC08221 "点击放大")

### 根因定位与分析

过滤出FD资源泄漏故障列表后，点击查看按钮，进入到问题个例分析详情页，可查看当前故障的分析报告，包含故障发生时间、泄漏句柄、故障模块、版本信息以及修复建议等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/JjsdpsgTQ564-0nbqzjalw/zh-cn_image_0000002671490976.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F16AA4CF37AD559ECC3EE85B85F2A1612CBCE56879953748702732CCC8ED51CC "点击放大")

**证据链分析**

证据链列表中按照泄漏数量倒序排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。同时提供了日志下载功能，便于进一步分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/5TqVWmHrR8KMLFsCJU_Mpw/zh-cn_image_0000002671650846.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=B99617DD4AB74C2E04685A335D3AE7949E8BE4D55F1230DBFEE16A7A9AB88B8A "点击放大")

**现场数据分析**

现场数据页中，将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/uoL6tssJSBuQJ8NraJKoZw/zh-cn_image_0000002701370681.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EFF4EA2D20F2FE1F2E1CFE644B0A5E494568F55747026B9A61F7A1F60EACE38 "点击放大")

**句柄栈信息****分析**

句柄栈信息是发生FD泄漏故障并达到一定条件后，系统从堆栈中抓取的堆栈信息，存在一定的滞后性。开发者可参考堆栈中的疑似泄漏点，进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/0PLkEORlQs27G1YARl7jsw/zh-cn_image_0000002701250593.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=D64A5B67A11098C44FD62C763205830FB10CB51BFC2F98D8583841267E792C40 "点击放大")

**下钻分析**

下钻分析的核心逻辑是从一个汇总的指标或表象问题出发，将其拆分成多个组成部分，然后挑出最关键的线索继续向下拆分，不断重复这个过程，直到定位到具体的根因。平台会根据故障特征ID进行聚类并筛选Top应用版本，系统版本以及设备型号。开发者可根据此重点关注问题高发的版本及设备，更精确的定位问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/h_lf_1XGTAOkMId_IdKcLA/zh-cn_image_0000002671491006.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF5F3137A7C77FA009ED7B7545A7FD434A293708BF1033E804D0A2519D59B692 "点击放大")

### 修复建议验证与闭环

**修复建议**

故障详情页面会提供修复建议，开发者可以通过给出的建议优化代码。

一般来说，开发者需要根据引用链尝试定位并断开应用侧的引用链路，释放对应的可疑泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/mK2rPe3YQUWmKTQAvptCjA/zh-cn_image_0000002671650858.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E3FA8AC1C5BEE2860A23648D92290295FA81DA1466CFEC4903E51D66987B753 "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Rjp45FNFQtG6uV5coT441A/zh-cn_image_0000002701370683.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=407EFE51BA2B8B9572A232624A32BA5277DAC3054F0839E90FDA2A7BAAEFB1A3 "点击放大")

### 问题分析

**证据链****分析**

证据链列表中按照泄漏数量排序，将FD泄漏的句柄名称展示出来，开发者可根据泄漏数量较大的句柄名称，结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/nkFJhfq5QUKuqxyfzu31Wg/zh-cn_image_0000002701250595.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=940F9E0762C7B7A5DA3CDE30914CAFED52B5B5990D200F4EE2429CD68621F324 "点击放大")

**现场数据****分析**

现场数据页面将展示Top10的泄漏句柄名称，开发者根据泄漏数量较大的句柄名称，并结合代码分析FD泄漏根因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Ko88k7n7QXaXPSWg6Jpbnw/zh-cn_image_0000002671491008.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3446DF1D82FE58475E6DDD3D5621E72D744AFBE2B78904C3F9B81B7A4EF6EE6C "点击放大")

**句柄栈****信息****分析**

句柄栈信息中将抓取的堆栈信息中疑似泄漏点进行展示，开发者进行堆栈还原后，结合代码分析具体的FD泄漏根因，并进行修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/FBepHSM7Tuy2YOOuv35Cjw/zh-cn_image_0000002671650860.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CA3C94823DC8FAC68C8E02891929B0A7AB8B0C627326C0E5F6131076544C9F0 "点击放大")
