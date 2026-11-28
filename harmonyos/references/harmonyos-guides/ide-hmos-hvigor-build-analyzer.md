---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-build-analyzer
title: 分析构建过程
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 分析构建过程
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:57+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a67c8d430b0f020bc3a659dc2d226811412b2b17c23bda9b6c76061539fcffff
---

构建分析器可以展示编译构建过程的重要信息，开发者能够通过构建分析器的可视化分析来排查构建过程中的性能和内存问题。

## 进入构建分析器

构建分析器会在每次构建应用时默认生成一份报告，并在构建分析器窗口进行展示。可以在构建完成后点击左侧边栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/8Umu4bmIQz-xPw3Rk3hE7Q/zh-cn_image_0000002820721157.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5A04DFF438399DB38757EDB8B3F9FBC08FB62D31495070635147A2429684630)按钮打开构建分析器窗口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/hR5LPj3uROKCVvFfOifmAQ/zh-cn_image_0000002792001190.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=50E81CD51B4C934C342E13B2276323ADAA2086352367AB7D3632E17BA2A6E902)

## 查看构建历史记录

构建分析器左侧的**构建历史**窗口中按时间顺序显示构建历史记录。点击构建历史记录可以显示对应概览和可视化图谱界面。

**说明** 

本工程的构建历史数据保存在./hvigor/report目录下，超过10条记录后，最早的历史数据将会被自动清理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/05Q2_tYSRj2M85RTRMTYnw/zh-cn_image_0000002792001194.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=284165B567C6B42D826251032DF6C42EAB9C9445E4CEACD91F32F73F7B4719A7)

## 查看构建任务时间图谱

完成构建后首次打开构建分析器时，窗口会显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/jtHh7DaqRH-aizGz_Kq3Vw/zh-cn_image_0000002820681153.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CFCA7FA794AEB5B513594C6BF7BC22E1EE5127787B031725CE780FDD8E95082)

如需查看构建任务时间图谱，点击下拉菜单选中并点击**任务视图**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/yLJl2t_AQU-6SaN_wi2udg/zh-cn_image_0000002791841222.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C238500BA4CE36B30DE1E93913877190F2B90E0C49FBD8A46B8E8C54E506340)

默认进入时间图谱界面。该界面会分块显示构建历史记录、构建任务时长图谱、构建日志以及对应的日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/5af86cFMTiu3xLe5imWzVA/zh-cn_image_0000002820721159.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E03DEEE7F855B1C7105534A2EE716B4A67A5321489C5223DAFDD85498B398BB)

图谱中的构建任务展示按照各个任务总时长占比，以相对长度进行展示。可以对时间块进行缩小放大，查看具体的任务名称及耗时信息。

图谱中构建子任务默认是折叠的，可点击**构建时间线**的节点信息，展开查看子任务的构建时长图谱。

图谱与日志信息是联动的，可点击图谱中的任务信息，即可联动对应的日志以及日志详情；相同的，点击日志时，也可联动对应的上方图谱信息。

**说明** 

构建分析器不会全部显示构建操作中的所有任务，而是重点显示决定构建总时长的任务。

图谱下方日志模块，展示每次构建的所有日志信息，并按日志级别（Info、Debug、Warn、Error）进行区分，并提供日志搜索功能。点击日志，可与上方图谱和右侧**详情**模块，进行联动显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/BNCZ0eMSTwu4D2Cp_29ldA/zh-cn_image_0000002792001192.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5BFE5FCD5BEB41EBBA215A01EF1C967398AFEB9C39AEAAA1CD92860214F6DE0)

## 查看构建任务占比图谱

如需查看决定着构建时长的任务的占比细分数据，请点击概览页面上的**本次构建通用视图**下方链接 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/TeoAgZ3wQpCh7gr9nocfFA/zh-cn_image_0000002791841220.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=D36DD71BBE46E05A478FCC31F3D714061C554414DE562486F6602D36310746AC)

也可以从下拉菜单中选择**任务视图**并确认您要的任务分组类别。任务以模块、业务类别、Target以及同一模块下的Target、同一模块下的业务类别和同一Target下的业务类别进行分组。图表中任务按照时间占比从大到小排列，点击子任务可详细了解其执行情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/-4ZxTNc8SJKQc4GQnfSs1w/zh-cn_image_0000002791841218.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C627BC7C11E98FA88EB932F73A266D0A6E5E65D39679445CE6CB6CFACAD7119)

**说明** 

1. 由于并行线程的存在，分类任务计算时间可能会比实际总时间长；

2. 饼图中Configuration代表未记录的任务占比。

## 查看构建过程内存消耗曲线图

如果要分析构建过程的内存消耗情况，需要先[设置构建分析模式为Advanced](ide-hmos-hvigor-build-analyzer.md#section207890565217)，启用内存监测，构建后会生成内存消耗曲线图。

点击概览页面上**本次构建通用视图**下方的链接**构建过程内存使用**，也可以从下拉菜单中选择**任务视图**和**内存使用**分组，查看内存消耗曲线图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/O-gT1zGWTgaH3RCy-QBMyw/zh-cn_image_0000002791841216.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=9210EDEDAAC2DF35F603D00B785753117E9F7956838B508EA9CD3A7D2A7783AC)

## 设置构建分析模式

进入****文件 >** 设置 > 扩展 >** **Hvigor**下，查看**设置构建分析能力模式**选项：

* **None**：不记录该次构建数据，不进行分析。
* **Normal**：普通模式（默认选项），记录简单打点数据进行分析。
* **Advanced**：高级模式，记录详细打点数据进行分析。
* **Ultrafine**：超精细化模式，与Advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/vJa6LFunQV29MRW28URoKA/zh-cn_image_0000002820681155.png?HW-CC-KV=V1&HW-CC-Date=20261128T023457Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F8B496DD426DAACA1AF485C605D0383F8CF057B0D6B6859E1C28C2C81E62C30)

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
