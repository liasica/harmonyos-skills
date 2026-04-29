---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6ef8702632403579ee6da29a7e0c1009fbee659ba5d11341a97c0307d9a0e87
---

Build Analyzer可以展示编译构建过程的重要信息，开发者能够通过Build Analyzer的可视化分析来排查构建过程中的性能和内存问题。

## 进入Build Analyzer

Build Analyzer会在每次构建应用时默认生成一份报告，并在Build Analyzer窗口进行展示。

可以在构建完成后通过以下方式打开Build Analyzer窗口：

* 点击菜单栏**Build > Build Analyzer**进行查看。
* 在Build窗口中的Build Output页签，点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Px9u9vaySiyi5YfCARAplw/zh-cn_image_0000002561832627.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=BD0C49E40577EF5C7AB419ADA1E13F52591FFB07BF4CA1EF81879F014E35EE81)，打开Build Analyzer页签。
* 构建成功且使用构建分析能力时，在Build窗口Build Output页签下的日志下方点击链接，跳转至Build Analyzer页签。

## 查看构建历史记录

Build Analyzer左侧的Build History窗口中按时间顺序显示构建历史记录，包括本工程的构建历史数据和[导入的日志数据](ide-hvigor-build-analyzer.md#section26761217305)。点击构建历史记录可以显示对应概览和可视化图谱界面。

说明

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/pqH_bSGhSqiX06Nvlyk4BQ/zh-cn_image_0000002530912714.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=14200DB8B3832C91BFDEFA21CD15014CDAFDA293934554A3153BA38319118D51)

## 查看构建任务时间图谱

完成构建后首次打开Build Analyzer 时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/EU51RR33QziRHOexgWJ4ug/zh-cn_image_0000002530752716.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=A07076AB0A9FBC9A7B8473976B3CF4525149C8BA1091D7B21289BF13C97F8DB6)

如需查看构建任务时间图谱，请从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/JUe4GrROSdKR7hvOKrcRDA/zh-cn_image_0000002561752649.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=F3C7595FD1FAF1B1DD7F77F9F39E3D487885193BB5004A3916845C632877F49F)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击Build TimeLine的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

说明

Build Analyzer不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。

点击日志，可与上方图谱和右侧Details模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/-KxuTORhQHe7jZD0hK3-QQ/zh-cn_image_0000002561752651.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=A8FB30A626AA66ECD85C8B929328A44F9A530637AB75C04F74623E034D15303F)

## 查看构建任务占比图谱

如需查看决定构建时长的任务的占比细分数据，请点击概览页面上的**Common views into this build**下方链接 ，您也可以从下拉菜单中选择**Tasks**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/LRsgF_qXSDyQ8hjqbWx_rg/zh-cn_image_0000002530912700.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=5253208ED4530470281EAD54BDE7FCE69FC953AF72D24FD85AC3ADFD1F00D225)

说明

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。从DevEco Studio 5.1.1 Beta1版本开始支持。

点击概览页面上**Common views into this build**下方的链接**Memory Usage During Build**，也可以从下拉菜单中选择**Tasks**和**Memory Usage**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Xw1VeuQvREOxMv1HrxkpnQ/zh-cn_image_0000002530912708.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=8BCCA71FFCED986C9D9D06B323C87D312439D65576193202411FCAD38A113538)

## 导出日志

如需查看本次构建日志，您可以点击导出按钮进行日志导出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/TL_Ly4aNQeWKvOmBNbnlUA/zh-cn_image_0000002561832637.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=0F61399FABB9D4F1DB66FECC233D52F253C953CA87DC98796DD7D1470194EE6D)

导出内容有：

* 分析统计本次构建的html文件。
* 记录构建日志的build.log文件。
* 记录构建daemon日志的daemon.log文件。
* 记录构建任务耗时的report.json文件。
* 记录构建过程内存消耗的report-monitor.json文件。

## 导入日志

如需查看历史或其他工程的构建日志，您可以点击导入按钮导入report.json文件，导入的文件保存在工程./hvigor/report/upload目录下，导入后可在Build Analyzer左侧的Build History窗口中查看。upload目录下最多保存10条记录，超过10条记录后，最久的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/4Q60-BtbQWu2I3jYddDvPQ/zh-cn_image_0000002561752643.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=CF34ECCFBA69DDF6EA807E4F0F6D348DAF0D8F771EDA5E62558832CA7F6E2AB7)

## 设置构建分析模式

进入**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**下，查看**Use build analysis mode**选项：

* 勾选此项：
  + 模式选择为Normal，即为普通模式（默认选项），记录简单打点数据进行分析。
  + 模式选择为Advanced，即为高级模式，记录详细打点数据进行分析（此模式下，建议搭配使用node 18版本）。
  + 模式选择为Ultrafine，即超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。从DevEco Studio 6.0.0 Beta1版本开始支持。
* 取消勾选，即为不记录该次构建数据，不进行分析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/OGK2p9NKSxKKokB0DT4yaA/zh-cn_image_0000002530912698.png?HW-CC-KV=V1&HW-CC-Date=20260429T054717Z&HW-CC-Expire=86400&HW-CC-Sign=23585F1F087CBAB3422D457AC550C90AB3B6DA3232D30C87F3B6DEF5FD2E13A0)

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
