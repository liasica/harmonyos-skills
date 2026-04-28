---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f52a2ad657d4e2d2104b1e43c89238128900d34c2ff1a22c308eb3e3ff068949
---

Build Analyzer可以展示编译构建过程的重要信息，开发者能够通过Build Analyzer的可视化分析来排查构建过程中的性能和内存问题。

## 进入Build Analyzer

Build Analyzer会在每次构建应用时默认生成一份报告，并在Build Analyzer窗口进行展示。

可以在构建完成后通过以下方式打开Build Analyzer窗口：

* 点击菜单栏**Build > Build Analyzer**进行查看。
* 在Build窗口中的Build Output页签，点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/2377JzhBSB25cJqD1m1V4g/zh-cn_image_0000002561832627.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=CBB33F627181BD4550E9A19C0415A2F8D7D5192B78FB9979966E5293A1AB9356)，打开Build Analyzer页签。
* 构建成功且使用构建分析能力时，在Build窗口Build Output页签下的日志下方点击链接，跳转至Build Analyzer页签。

## 查看构建历史记录

Build Analyzer左侧的Build History窗口中按时间顺序显示构建历史记录，包括本工程的构建历史数据和[导入的日志数据](ide-hvigor-build-analyzer.md#section26761217305)。点击构建历史记录可以显示对应概览和可视化图谱界面。

说明

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/DCbHrMbfTimFhIUM8JRJBw/zh-cn_image_0000002530912714.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=EA1EBE4D1A623A2E0CC2B8D05853BE5D7F3429F068DC5374782852980CD531D4)

## 查看构建任务时间图谱

完成构建后首次打开Build Analyzer 时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/cGzJHKJcRp-nP2uhGQXlMg/zh-cn_image_0000002530752716.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=2F59228BE3FD281D98A0DA7D29E5801142F6E5629E84305D3BEBBA439CBD116C)

如需查看构建任务时间图谱，请从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/0uulxXxnRwCyCyU3IAHRxw/zh-cn_image_0000002561752649.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=8DFC206B86B2926FF85380B98B23F9164158A18E41FC44BECCD966723C5D3404)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击Build TimeLine的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

说明

Build Analyzer不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。

点击日志，可与上方图谱和右侧Details模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/WCz5ODjpRwe_fsM8EgMu_A/zh-cn_image_0000002561752651.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=33A2DF0FC771BD0C67DB9F6C0CF064A2D3C91E7A8C3A99581486AD3B88857352)

## 查看构建任务占比图谱

如需查看决定构建时长的任务的占比细分数据，请点击概览页面上的**Common views into this build**下方链接 ，您也可以从下拉菜单中选择**Tasks**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Tosh4UrASluldjeX3PZNuA/zh-cn_image_0000002530912700.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=76F42410E5575A768251647269D1BBD54E334D6BB165697607F957071EF50B87)

说明

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。从DevEco Studio 5.1.1 Beta1版本开始支持。

点击概览页面上**Common views into this build**下方的链接**Memory Usage During Build**，也可以从下拉菜单中选择**Tasks**和**Memory Usage**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YuLosoU1Tiej_24JJPFbLQ/zh-cn_image_0000002530912708.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=0985CF1C8DE0BA5C217B85F33F5AF59162F6A2148566E3A97C6C33825E42787A)

## 导出日志

如需查看本次构建日志，您可以点击导出按钮进行日志导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/5HWF0dX6TIecPjpE-HtMcA/zh-cn_image_0000002561832637.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=E40CEEE880D4D22ABEECB847B76773E0F8824FDD8239612C3F8610BCF461C936)

导出内容有：

* 分析统计本次构建的html文件。
* 记录构建日志的build.log文件。
* 记录构建daemon日志的daemon.log文件。
* 记录构建任务耗时的report.json文件。
* 记录构建过程内存消耗的report-monitor.json文件。

## 导入日志

如需查看历史或其他工程的构建日志，您可以点击导入按钮导入report.json文件，导入的文件保存在工程./hvigor/report/upload目录下，导入后可在Build Analyzer左侧的Build History窗口中查看。upload目录下最多保存10条记录，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/R5JAvGCrQPOdvtDZwvqBmw/zh-cn_image_0000002561752643.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=18D7D03F1B7D9F8C9B3EFCCBF78CDB78234D943DC7676BE28B77A6D0CD42B75C)

## 设置构建分析模式

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**下，查看**Use build analysis mode**选项：

* 勾选此项：
  + 模式选择为Normal，即为普通模式（默认选项），记录简单打点数据进行分析。
  + 模式选择为Advanced，即为高级模式，记录详细打点数据进行分析（此模式下，建议搭配使用node 18版本）。
  + 模式选择为Ultrafine，即超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。从DevEco Studio 6.0.0 Beta1版本开始支持。
* 取消勾选，即为不记录该次构建数据，不进行分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/yxuAs4-KTP6m8RVbmLVw1Q/zh-cn_image_0000002530912698.png?HW-CC-KV=V1&HW-CC-Date=20260427T235717Z&HW-CC-Expire=86400&HW-CC-Sign=0D5744E721FBB9B24E704F6FED09FB490DEA4C151909485AF99E49D501F05F37)

## 生成构建可视化html文件

* 通过命令行方式生成构建可视化html文件。如生成HAP模块的构建可视化html文件，命令如下：

  ```
  1. hvigorw assembleHap --analyze=normal --config properties.hvigor.analyzeHtml=true
  ```

* 通过[hvigor-config.json5](ide-hvigor-set-options.md)配置文件中properties.hvigor.analyzeHtml字段生成构建可视化html文件：

  ```
  1. {
  2. "modelVersion": "6.1.0",
  3. "dependencies": {
  4. },
  5. "execution": {
  6. },
  7. "logging": {
  8. },
  9. "debugging": {
  10. },
  11. "nodeOptions": {
  12. },
  13. "properties": {
  14. "hvigor.analyzeHtml": true  // 生成构建可视化html文件
  15. }
  16. }
  ```

  再执行构建，例如执行以下命令：

  ```
  1. hvigorw assembleHap --analyze=normal
  ```

执行以上命令后，在工程的.hvigor/report目录下生成对应的html文件，该文件可直接在浏览器中打开。
