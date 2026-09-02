---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations
title: Snapshot模板基本操作
breadcrumb: 指南 > 优化应用性能 > 内存泄露：Snapshot分析 > Snapshot模板基本操作
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33cd674a5f05120d9c3f38184be9bc4ae87a81aacd4845d563f1e721db0fbabc
---

针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

在DevEco Studio 6.0.2及之前版本，Memory泳道统计时支持选择PSS/RSS/USS中的一个或多个，可以从多维度度量当前进程的物理内存使用情况。从DevEco Studio 6.1.0 Beta1开始，Memory泳道统计时固定为PSS、GL、Graph总和，在会话区不支持选择PSS/GL/Graph。

## 查看快照详情

1. 创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。
2. 设置Snapshot泳道。

   单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/zCBRkCuESFOnFwPv6AhQwQ/zh-cn_image_0000002561753311.png)进行泳道的筛选，再次单击此按钮可关闭设置并生效。
3. 单击ArkTS Snapshot泳道的“options”下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/n9cbZT3nSR-68_RWzXkVCw/zh-cn_image_0000002561833297.png)
4. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/WpS7_f-fSs2X5YCxOMHQcA/zh-cn_image_0000002530913368.png)启动一次快照。

   “ArkTS Snapshot”泳道的紫色区块表示一次快照完成。

   说明

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Q_iFvEhoS_uEvnUy1BHVCw/zh-cn_image_0000002530753366.png)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/sgl-sAevTduPnTyV4l8ZhQ/zh-cn_image_0000002561753281.png "点击放大")

   在“Statistics”页签中显示当前快照的详细信息：

   * Constructor：构造器。
   * Count：该对象的数量。
   * Distance：从GC Root到这个对象的距离。
   * Shallow Size：该对象的实际大小。
   * Retained Size：当前对象释放时，总共可以释放的内存大小。
   * Native Size：该对象所引用的Native内存大小。
   * Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
   * 带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/jcz7lw4CTt-ZLUTdNtU9aA/zh-cn_image_0000002561753279.png)标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Htu91X7qQLOTt2tfGkasaA/zh-cn_image_0000002530753358.png "点击放大")

   说明

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴；或使用快捷键W/S缩放时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。

## 应用对象名称解析

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始，支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

1. 系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以\_GLOBAL开头。
2. 方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：

   ```
   1. com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)[MainModule] //格式为BundleName/SelfModule@Version/FilePath/File#Class(line: xx)[RefModule]
   ```
3. 其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

* Module：模块信息。
* Class：属性名称。
* Path：编译后的源码路径。支持通过点击属性名称旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/pUrHBn03QWKqiml3B3hUdQ/zh-cn_image_0000002530753336.png)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/MqBgLcMeTBmka8wov4fljw/zh-cn_image_0000002561753257.png "点击放大")

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/J8XmkH7ZRh6rkkJwjIrbqQ/zh-cn_image_0000002530913346.png "点击放大")

说明

* 确保工程代码路径与解析信息匹配，否则跳转可能失败。
* 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
* 对象名称后的line=0时表示无效行号，不支持跳转。

## 节点属性与引用链

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/5QR7VR8iTiygdsqZ0_kE3Q/zh-cn_image_0000002561833277.png "点击放大")

## 节点跳转

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/F4JgcwKiRDqwCr_zPO9q_A/zh-cn_image_0000002530913334.png "点击放大")

## 历史节点前进/后退

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/cx8EnVGWRc-ZBIHFQ441oA/zh-cn_image_0000002561833241.png "点击放大")

## 比较快照差异

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/TlCNyrSsQkmn8kE8L0oCOw/zh-cn_image_0000002530913354.png "点击放大")

在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/gU2tJDkQQYiBmJK2U-TbRQ/zh-cn_image_0000002561833269.png "点击放大")

## 引用链向最小引用距离展开

Snapshot分析支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

### DevEco Studio 6.1.0 Beta2及之后版本

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/wnbesvVOTmSAsWVxuGp-fw/zh-cn_image_0000002530753348.png "点击放大")

### DevEco Studio 6.1.0 Beta2之前版本

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/J6p2_nUhT42VIHA5Z3Pebg/zh-cn_image_0000002561753293.png "点击放大")

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yoYZZuYDSZGNq4oxZ9sJrg/zh-cn_image_0000002530913328.png "点击放大")

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/a4-RwIPeShigcef1Z5Ln-g/zh-cn_image_0000002530753354.png "点击放大")

## 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，Snapshot模板支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/pqceJLhPSbeivF7tIz-U1A/zh-cn_image_0000002530753370.png "点击放大")

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

* Retained Size：按照Retained Size从大到小展示周边节点。
* Distance：按照Distance从小到大展示周边节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Gme_xAJYSQuH0wVFeWKUgA/zh-cn_image_0000002530753362.png "点击放大")

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/8BbJqgpnR_aIlQ8x5-hkAg/zh-cn_image_0000002561753263.png "点击放大")

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

* **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
* **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
* **Redraw with this node**：以该节点为中心重绘。
* **Reveal in Statistics**：在Statistics页面中显示该节点。
* **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/4FOweJj4S0af3lxXB_XZOg/zh-cn_image_0000002561753265.png "点击放大")

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/HMVOxrMIT6mHA-BR18nn1w/zh-cn_image_0000002530753346.png "点击放大")

## 离线导入内存快照

DevEco Profiler支持离线导入内存快照功能，可导入一个或多个.heapsnapshot及.rawheap文件。

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot或.rawheap文件。

说明

* 导入的单个文件大小不超过1.5G。
* 批量导入的文件数量不超过10个。
* .rawheap文件是应用发生Out of Memory现象时产生的原始内存文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/MncZkNlKRvGn0oW1-BMxmw/zh-cn_image_0000002530913322.png "点击放大")

离线导入内存快照成功后，可以导入与.heapsnapshot或.rawheap文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

说明

* 导入的单个jsleaklist文件大小不超过30M。
* 导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
* 可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/BBSajLL4S9uMkCd-fzcMQA/zh-cn_image_0000002530753340.png "点击放大")

## 解析内存对象

从DevEco Studio 6.1.0 Beta2开始，DevEco Profiler支持导入[代码混淆产物nameCache](ide-exception-stack-parsing-principle.md#section19215122372720)文件和[ArkTS调试产物sourceMap](ide-exception-stack-parsing-principle.md#section666114451518)文件，还原文件名称和文件路径。

以nameCache文件为例，文件导入前，Class为d8，

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/vPeeI85dS4OXiRwIkVeLvA/zh-cn_image_0000002561753285.png "点击放大")

点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/SRPbM9rbQ4eFyoGatIGZ2A/zh-cn_image_0000002530913326.png)按钮，导入nameCache文件，Class显示为文件名称MyAbilityStage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/UFsznpprQvWNh75B1Dvg1A/zh-cn_image_0000002530753368.png "点击放大")
