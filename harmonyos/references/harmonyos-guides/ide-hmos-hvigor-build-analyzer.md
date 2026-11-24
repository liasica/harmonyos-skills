---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:846aafd043d7395248afd819b2f0f48a069b8fe4b75cbdb96d8743ba3974d7d1
---

构建分析器可以展示编译构建过程的重要信息，开发者能够通过构建分析器的可视化分析来排查构建过程中的性能和内存问题。

## 进入构建分析器

构建分析器会在每次构建应用时默认生成一份报告，并在构建分析器窗口进行展示。可以在构建完成后点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/RA5AsmN7QveoyL7NZAHZqQ/zh-cn_image_0000002820721157.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=48241BB7E136DDCCE47E32C9CEA2F628981FA5E5633E0CDA2873CB5F83D67E85)按钮打开构建分析器窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/wxFz55ACR7eCPN_BaQnBfw/zh-cn_image_0000002792001190.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7907803043F93FDBA4E5EA033F75BC2E56460B9CFE1F32A47430867E0DD4B76)

## 查看构建历史记录

构建分析器左侧的**构建历史**窗口中按时间顺序显示构建历史记录。点击构建历史记录可以显示对应概览和可视化图谱界面。

**说明** 

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最早的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/5PmqPiH7Ty2YoMy3Y6u1ug/zh-cn_image_0000002792001194.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CDEC55821A9B1392C5C0455BD372AFEA41B05252AECAD3B73769EC34958F018)

## 查看构建任务时间图谱

完成构建后首次打开构建分析器时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/cloJigJlTnyf49vEIXEUWQ/zh-cn_image_0000002820681153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAC176EAC873D85F39592803718594ED7D4A90309E3540E797F0D9751D70DB3E)

如需查看构建任务时间图谱，点击下拉菜单选中并点击**任务视图**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/5Ih4CWlNRoqoToOAZiWSLg/zh-cn_image_0000002791841222.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=661FBB5E56878C3BE7DF2B426F671C77FEE9DABC51D2676AA984B2E3EB66FD12)

默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/DGCd_UgcSWa__3m9MVOtTg/zh-cn_image_0000002820721159.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A0D5B8173ECC6EA5892DDC09F0355ECB0304AE67DFE27051E80B1020A647203)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击**构建时间线**的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

**说明** 

构建分析器不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。点击日志，可与上方图谱和右侧**详情**模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/IV0pyLvvT5O_N2IUyh1k0g/zh-cn_image_0000002792001192.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=884CB2C478C91968B32AC537BD73032CE22DF08FB12BD9233F8B8E82AA810D5D)

## 查看构建任务占比图谱

如需查看决定着构建时长的任务的占比细分数据，请点击概览页面上的**本次构建通用视图**下方链接 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/vYHraxIxSgqu0A5KNb7nvA/zh-cn_image_0000002791841220.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=4396942FBAAD8CE60812EC75341541A685DC49EA203BB941ED9D7352F1DCC5A3)

也可以从下拉菜单中选择**任务视图**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2Cim7z0hTYa8ZJz5BmdmMA/zh-cn_image_0000002791841218.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE104EF9E970D9E469D4CE8CBBACE1E27047003B5DBFB4022A1F869F5070AE37)

**说明** 

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hmos-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。

点击概览页面上**本次构建通用视图**下方的链接**构建过程内存使用**，也可以从下拉菜单中选择**任务视图**和**内存使用**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/eVMz7fYCTauiFOUlmi7TWQ/zh-cn_image_0000002791841216.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F12DE59FFC7BF6680F9C474766F978CE54680890A716D0A93313BBBA80CB10E)

## 设置构建分析模式

进入****文件 >** 设置 > 扩展 >** **Hvigor**下，查看**设置构建分析能力模式**选项：

* **None**：不记录该次构建数据，不进行分析。
* **Normal**：普通模式（默认选项），记录简单打点数据进行分析。
* **Advanced**：高级模式，记录详细打点数据进行分析。
* **Ultrafine**：超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/UyzvV0gnScak9qYSCL4kaQ/zh-cn_image_0000002820681155.png?HW-CC-KV=V1&HW-CC-Date=20261124T044248Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4464D07E4A6C39D7D25F1088F9EB6481BDBA2720C674640E8603DD9BFA6CD7D)

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
