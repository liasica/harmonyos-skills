---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0059dbf225134370aad77e7cbe65bb1fc9a570e321fda1ea1d858dc99b56c701
---

构建分析器可以展示编译构建过程的重要信息，开发者能够通过构建分析器的可视化分析来排查构建过程中的性能和内存问题。

## 进入构建分析器

构建分析器会在每次构建应用时默认生成一份报告，并在构建分析器窗口进行展示。可以在构建完成后点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/E2bSchKURieC-jsg3YTDTQ/zh-cn_image_0000002781311306.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=97AA0E1865A9FDEA60398ED212494454F93DB9499C8F9D885C72139BFDF8CD06)按钮打开构建分析器窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/jWXvRDB3STexnVeO_YOUYg/zh-cn_image_0000002781471242.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CFDB9EBE9A28A14B152B4077BF35B18EFA36F07B31CA0531EE1A2B151B2A231)

## 查看构建历史记录

构建分析器左侧的**构建历史**窗口中按时间顺序显示构建历史记录。点击构建历史记录可以显示对应概览和可视化图谱界面。

**说明** 

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最早的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/x-J1TddKT6WkyU1lEwhXuw/zh-cn_image_0000002781471240.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6027E4F0CE7858D717CD38B0FBB696DDDE464EC8EBF2C8B79904FC806855419F)

## 查看构建任务时间图谱

完成构建后首次打开构建分析器时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/y8jt_Pl2RY23_uZbPVeZ3Q/zh-cn_image_0000002810630795.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=15CA071D12F1D5B9FA69E1832B61003FD0896CDBEF6636DE5DCB256188F07B2A)

如需查看构建任务时间图谱，点击下拉菜单选中并点击**任务视图**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/jMmMRar-R6aDuMUiDw2ufA/zh-cn_image_0000002810630797.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD27D96018C41CA3D035374BFCF95B88B6BF34ADCA4507A8E575FE92232BCBDF)

默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/1YHKvCvkRGGkRJKq0Lti2A/zh-cn_image_0000002810750905.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF342BBAC08136F31EE175ECDF6283EAEFE5166D98CB2A601ED2691C61E6494B)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击**构建时间线**的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

**说明** 

构建分析器不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。点击日志，可与上方图谱和右侧**详情**模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jaTxtIqLTuyf5mHE6WJxOw/zh-cn_image_0000002781311302.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDCF0857EC41F4654A6DB92CAC3638F3C0AF511867CC09EB9EA6881956B8D3B7)

## 查看构建任务占比图谱

如需查看决定着构建时长的任务的占比细分数据，请点击概览页面上的**本次构建通用视图**下方链接 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/mYRhTTtQTEW_0EwfQJ6-CA/zh-cn_image_0000002810750907.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A41F31C0884624971509B816503E872F325E5046E557591ACFF5E72C484D3A4F)

也可以从下拉菜单中选择**任务视图**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/I_vT_Jr7RbqGTGSIu6ohlg/zh-cn_image_0000002781311304.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A525B2F30DAA9EE5C42EC2070FF9600A1556657174CF73136941B22D982CCE2)

**说明** 

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hmos-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。

点击概览页面上**本次构建通用视图**下方的链接**构建过程内存使用**，也可以从下拉菜单中选择**任务视图**和**内存使用**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/iRHNIg22TI2UT5iwSJUj1A/zh-cn_image_0000002781311308.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3DA872DB93C5BBEF0C23F63363F1BC0A85AB6D0EC51739C6CB087999D55892F)

## 设置构建分析模式

进入****文件 >** 设置 > 扩展 >** **Hvigor**下，查看**设置构建分析能力模式**选项：

* **None**：不记录该次构建数据，不进行分析。
* **Normal**：普通模式（默认选项），记录简单打点数据进行分析。
* **Advanced**：高级模式，记录详细打点数据进行分析。
* **Ultrafine**：超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/9YZYe6WGRXe-aE_IUkM5Yw/zh-cn_image_0000002781471238.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E03760FEF4DF9901BCEE797D68BADEA31735A6CF51A11F3F8E8B1088C0E66551)

## 生成构建可视化html文件

* 通过命令行方式生成构建可视化html文件。如生成HAP模块的构建可视化html文件，命令如下：

  ```bash
  hvigorw assembleHap --analyze=normal --config properties.hvigor.analyzeHtml=true
  ```
* 通过[hvigor-config.json5文件](ide-hmos-hvigor-set-options.md)中properties.hvigor.analyzeHtml字段生成构建可视化html文件：

  ```json5
  { 
    "properties": {
      "hvigor.analyzeHtml": true  // 生成构建可视化html文件
    }
  }
  ```

  再执行构建，例如执行以下命令：

  ```bash
  hvigorw assembleHap --analyze=normal
  ```

执行以上命令后，在工程的.hvigor/report目录下生成对应的html文件，该文件可直接在浏览器中打开。
