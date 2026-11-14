---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:19+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0cd46523ea8068a0517847bc8fc20b074d4839e1aac76e2a7e3d6afb1ca50d69
---

构建分析器可以展示编译构建过程的重要信息，开发者能够通过构建分析器的可视化分析来排查构建过程中的性能和内存问题。

## 进入构建分析器

构建分析器会在每次构建应用时默认生成一份报告，并在构建分析器窗口进行展示。可以在构建完成后点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/0BDmPG-aRX6pCXcoPamWMA/zh-cn_image_0000002781311306.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=A19FBB684E500D181F9C57B87403A94C090C03D6A8C212A399170D0272213673)按钮打开构建分析器窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/UmT8jVdyQVua1f9i6Ljz0g/zh-cn_image_0000002781471242.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=8808F340F99E32BDE6BCC998CDD451E238A694AD5E3028E29A4BA3D5987410E4)

## 查看构建历史记录

构建分析器左侧的**构建历史**窗口中按时间顺序显示构建历史记录。点击构建历史记录可以显示对应概览和可视化图谱界面。

**说明** 

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最早的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/hhf_Xc2sQHWg_VqJvN9u5Q/zh-cn_image_0000002781471240.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=F36DBC0D7C04B4DC63D6E9C7DE3F731D587C8DF9F35166D27AB2641EBE6C7828)

## 查看构建任务时间图谱

完成构建后首次打开构建分析器时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/c228jkaWQ4K9mjIlhefhLw/zh-cn_image_0000002810630795.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=517EBE38A68E31ABBDAD9CA77597B0F491DF948B4B2D6CFBF3BA074CB5D21A8A)

如需查看构建任务时间图谱，点击下拉菜单选中并点击**任务视图**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZQV87rDbSkKW78h_TRwgGQ/zh-cn_image_0000002810630797.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=46617CF1DFABDCCED90028B867F5656789E732872781AFCFA51A7104AC3E5005)

默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/i5Ogxj1YTzGcsvmHZagPWg/zh-cn_image_0000002810750905.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=03FC07A78EC8B5786A1930A0BBC9DD95841680B3459E591B86B01DB3D7BDD918)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击**构建时间线**的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

**说明** 

构建分析器不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。点击日志，可与上方图谱和右侧**详情**模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/DK7n5aSMT9KbQcXG34dWcw/zh-cn_image_0000002781311302.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DD748803B65045F1582D1F4C3DDD8ED19C88A1A7B9DCF392CC12CF285D355C5)

## 查看构建任务占比图谱

如需查看决定着构建时长的任务的占比细分数据，请点击概览页面上的**本次构建通用视图**下方链接 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/5X70ca3BSTaAm3KN_o9abg/zh-cn_image_0000002810750907.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=D81D4651096314427ECC7A915A6690BB764640C391CFE82B215C8486838B2481)

也可以从下拉菜单中选择**任务视图**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/7XW--Y7ZSuO1RD8wA3Agrg/zh-cn_image_0000002781311304.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C5D327E3B41FE9B45AEA172B05966DB7C22D5458F137E6E4A44947387B5FEE2)

**说明** 

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hmos-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。

点击概览页面上**本次构建通用视图**下方的链接**构建过程内存使用**，也可以从下拉菜单中选择**任务视图**和**内存使用**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ndOyGx8YRuGz7PZm8rEUCQ/zh-cn_image_0000002781311308.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=8333AEDBEF8691782F73EBB3387515484FBABD13B2B18B4AE3779146231F742A)

## 设置构建分析模式

进入****文件 >** 设置 > 扩展 >** **Hvigor**下，查看**设置构建分析能力模式**选项：

* **None**：不记录该次构建数据，不进行分析。
* **Normal**：普通模式（默认选项），记录简单打点数据进行分析。
* **Advanced**：高级模式，记录详细打点数据进行分析。
* **Ultrafine**：超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/nRlMy9u0Qxa1Hn6W5iZaOw/zh-cn_image_0000002781471238.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC715F767152EC9EA05FBB0BB2CCAB86932D77CF07A6296C0383DF8A04C44F2E)

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
