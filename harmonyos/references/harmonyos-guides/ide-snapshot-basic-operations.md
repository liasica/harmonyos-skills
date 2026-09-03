---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations
title: Snapshot模板基本操作
breadcrumb: 指南 > 优化应用性能 > 内存泄漏：Snapshot分析 > Snapshot模板基本操作
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:78813276741e34d1a1ac716b42093b505ac3b9c6571d27689d22124ef243e749
---

## 功能介绍

针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

Snapshot模板支持的泳道包括：Memory、ArkTS Snapshot。本文介绍ArkTS Snapshot泳道，Memory泳道的详细信息请参考[Allocation分析](ide-insight-session-allocations-memory.md#li6600547121414)。

## 约束与限制

由于隐私安全政策，已上架应用市场的应用不支持使用Snapshot分析模板。

**说明** 

任务分析前，需创建Snapshot分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看快照详情

1. 单击**ArkTS Snapshot**泳道的**options**下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/lzjk-AgFTmSiKxNRKI3vuw/zh-cn_image_0000002731382995.png)
2. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/N5MbCPIhTYOMD2cBwtobtQ/zh-cn_image_0000002731382997.png "点击放大")启动一次快照，一次快照完成后会在**ArkTS Snapshot**泳道出现紫色区块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/gOUfmdneRQ6ccL7WRLWHcA/zh-cn_image_0000002701823696.png "点击放大")

   点选ArkTS Snapshot泳道的紫色区块，**Statistics**区域显示当前快照的详细信息：

   * Constructor：构造器。
   * Count：该对象的数量。
   * Distance：从GC Root到这个对象的距离。
   * Shallow Size：该对象的实际大小。
   * Retained Size：当前对象释放时，总共可以释放的内存大小。
   * Native Size：该对象所引用的Native内存大小。
   * Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
   * 带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/vG_f0QRKToO3DCWDLfcTtg/zh-cn_image_0000002731542957.png "点击放大")标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/UiMXcnJgSFeqgZO-BR_dvg/zh-cn_image_0000002731542951.png "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

## 比较快照差异

在**ArkTS Snapshot**泳道的**Comparison**区域，点击任一快照作为base，在**CompareTo**下拉框选择的快照作为Target，即可得到两次快照信息的比较结果。比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/oxL4Y0pCScWFFG5rvlTFlw/zh-cn_image_0000002701663762.png "点击放大")

## 应用对象名称解析

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始， **ArkTS Snapshot**泳道支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

1. 系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以\_GLOBAL开头。
2. 方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：

   ```screen
   com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)[MainModule] //格式为BundleName/SelfModule@Version/FilePath/File#Class(line: xx)[RefModule]
   ```
3. 其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

* Module：模块信息。
* Class：属性名称。
* Path：编译后的源码路径。支持通过点击属性名称旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/dk62WTNKSH-cSo-QrmSlAQ/zh-cn_image_0000002731382973.png)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/VKUhMT1OSnuqB4XR5kQD6Q/zh-cn_image_0000002731542963.png "点击放大")

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/CVeogH5MRZyHxMWGcW9LAw/zh-cn_image_0000002731382987.png "点击放大")

**说明** 

* 确保工程代码路径与解析信息匹配，否则跳转可能失败。
* 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
* 对象名称后的line=0时表示无效行号，不支持跳转。

## 查看节点属性和引用链

在**ArkTS Snapshot**泳道的**Statistics**区域和**Comparison**区域中，展开所有实例对象节点，可看到**fields**和**references**，分别表示该实例对象的属性和该实例对象的引用链信息，或者点击实例对象，在右侧**More**区域中查找Fields和References。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/E90aJl5-Q4uJKkwAAnFejg/zh-cn_image_0000002731382975.png "点击放大")

## 节点跳转

在“**ArkTS Snapshot**泳道的**Comparison**区域中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的**Statistics**区域并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/XLgTum7KSbqAEaBWJlCj4w/zh-cn_image_0000002731542949.png "点击放大")

## 历史节点前进和后退

当在ArkTS Snapshot泳道的**Comparison**和**Statistics**之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ehQYw8_SRaScAs0Eeg9tNQ/zh-cn_image_0000002731542953.png "点击放大")

## 获取节点支配树

从26.0.0版本开始**，ArkTS** **Snapshot**泳道支持一键获取节点支配树，系统会以GC Roots为根节点构建内存对象的支配树。选中一个实例结点后，在右侧**Dominator Path****s**页签查看支配树。

在支配树结构中，若到达目标对象的任何路径都必须经过某节点，则该节点即为其支配者。通过展示从GC Roots到目标实例在支配树上的支配链，系统能够剥离错综复杂的冗余与交叉引用，直接定位到内存泄漏的支配者。断开路径上的支配者即可释放关联内存，从而更精准、高效地解决内存泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/WghM-ZzeR9u53rbvz5Y9cQ/zh-cn_image_0000002731542947.png "点击放大")

## 引用链向最小引用距离展开

**ArkTS** **Snapshot**泳道支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

### DevEco Studio 6.1.0 Beta2及之后版本

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧**Shortest Paths**页签展示。

从26.0.0版本开始，点击**Shortest Paths**页签左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/HOwV7HPsRue39eADOQo-jw/zh-cn_image_0000002731382985.png "点击放大")按钮，可将页签中的数据导出到本地进行保存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/ExYv4DQLQv2X1o-1qEMO_w/zh-cn_image_0000002731382983.png "点击放大")

从26.0.0版本开始，若应用编译模式为release，且启用了源码混淆，**Constructor**将展示混淆后的源码路径。若调试应用工程存在对应的nameCache文件，点击**Show SourceClassName**按钮，即可显示混淆前的源码路径，否则需要导入调试应用对应的nameCache文件后再点击按钮。

此外，若调试应用工程存在对应的SourceMap文件，点击源码路径旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/IlZsNRMCQUC1ia-OLkCigg/zh-cn_image_0000002701823688.png)图标，可直接跳转至工程中的代码位置，方便开发者快速调试，否则需要导入调试应用对应的SourceMap文件后再点击按钮跳转到源码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/RBiRm3EYTPuqSJ8hUGDylg/zh-cn_image_0000002731382981.png "点击放大")

### DevEco Studio 6.1.0 Beta2之前版本

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/QrKbHeRtSIWKtGYhgOK3Qg/zh-cn_image_0000002701663774.png "点击放大")

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/CogoCBS9SauTjOo7lBoQxw/zh-cn_image_0000002731542955.png "点击放大")

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/FbrlhOKjSS-76ghiqTn8pg/zh-cn_image_0000002731382991.png "点击放大")

## 合并展示最小引用距离

从DevEco Studio 6.1.1 Beta1版本开始，在**ArkTS Snapshot**泳道的**Statistics**区域中，选中一个构造器或实例结点，点击底部搜索栏的**References**按钮并确认，在右侧**Merged Incoming References**页签可查看该节点构造器下的所有实例到GC Roots的最短路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7ehDAKLCS4mhpaVV4xcdsw/zh-cn_image_0000002731542965.png "点击放大")

## 支持聚类展示

从26.0.0版本起，**ArkTS Snapshot**泳道的**Statistics**区域支持按不同聚类规则展示构造器或对象。

当前支持的构造器类型包括：JSObject、JSSharedObject、JSArray、Proxy和 (string)，对象类型包括：LocalHandleRoot、GlobalHandleRoot。

当前支持的聚类规则包括：Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths、ClassName、NativeList、Merge ClassName and NativeList。

* Merge Shortest Paths：最短引用链聚类。以对象到GC Roots的最短引用链进行聚类展示，用"->"拼接。
* Merge Same Property：属性聚类。
  + JSObject、JSSharedObject：以“属性名 :: 属性值”进行聚类展示，用","拼接。
  + JSArray：以“属性名”进行聚类展示，用","拼接。
  + Proxy：以属性“target”的值进行聚类展示，用","拼接。
* Merge Same Property and Shortest Paths：属性+最短引用链聚类。属性聚类后与最短引用链聚类后，用"|"拼接。
* ClassName：类名聚类。将fieIds下相同的属性名进行聚类展示。
* NativeList：原生列表聚类。将右侧Native List区域的实例对象Native堆栈信息进行聚类展示。
  + 若无Native List区域或Native List区域无数据，以“NoNativeCallTree”进行聚类展示。
  + 若Native List区域均为系统代码，以“全部调用栈”进行聚类展示，用"->"拼接。
  + 若Native List区域包含开发者自定义代码与系统代码，以“开发者自定义代码”进行聚类展示，用"->"拼接。
* Merge ClassName and NativeList：类名+原生列表聚类。类名聚类后与原生列表聚类后用"|"拼接。

构造器或对象适用的聚类规则如下：

| 构造器或对象 | 支持的聚类规则 |
| --- | --- |
| JSObject | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths |
| JSSharedObject | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths |
| JSArray | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths |
| Proxy | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths |
| (string) | Merge Shortest Paths |
| LocalHandleRoot | ClassName、NativeList、Merge ClassName and NativeList |
| GlobalHandleRoot | ClassName、NativeList、Merge ClassName and NativeList |

**说明** 

对于LocalHandleRoot和GlobalHandleRoot对象，不同模板支持的聚类规则有所差异，具体为：

* [Allocation模板](ide-insight-session-allocations.md)支持ClassName、NativeList、Merge ClassName and NativeList三种聚类规则。
* Snapshot模板和[Commemory模板](ide-commemory.md)仅支持ClassName一种聚类规则。

选择构造器或对象后，底部搜索栏按钮呈可点击状态。点击该按钮并配置聚类规则，展开构造器时将按规则展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-MTuEzWRTUW015YzOogdDg/zh-cn_image_0000002731542969.png "点击放大")

## 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，**ArkTS** **Snapshot**泳道支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/yuXXtiQXQsOyJjikf_Si4g/zh-cn_image_0000002731542967.png "点击放大")

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

* Retained Size：按照Retained Size从大到小展示周边节点。
* Distance：按照Distance从小到大展示周边节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/smzLvoxgSM6P7Vfp6Eod7Q/zh-cn_image_0000002731382977.png "点击放大")

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/NkNISBvMS8SsLNChLRDY8g/zh-cn_image_0000002701823694.png "点击放大")

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

* **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
* **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
* **Redraw with this node**：以该节点为中心重绘。
* **Reveal in Statistics**：在Statistics页面中显示该节点。
* **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/4kChOxuRQVGdHsBY4bhlaA/zh-cn_image_0000002701823686.png "点击放大")

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/8D7KRJ1YTLS2mthumo3jlQ/zh-cn_image_0000002731542961.png "点击放大")

## 搜索内存对象

**ArkTS** **Snapshot**泳道的**Statistics**区域和**Comparison**区域支持按对象名称搜索内存对象，在底部搜索框中输入对象名称即可进行模糊查询。

从26.0.0版本开始，**Statistics**区域底部搜索框支持通过对象id精确定位目标对象，格式为：@id。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/HoNBoNJzT026DLnPZLQmgg/zh-cn_image_0000002701823684.png "点击放大")

## 离线导入内存快照文件

26.0.0及以上版本，支持单独导入一个或多个.rawheap文件，同时工具会自动导入匹配的.jsleaklist文件，若匹配的.jsleaklist文件不存在，则导入失败；支持导入一个或多个.jsleaklist文件后，工具自动导入匹配的.rawheap文件；也支持先导入一个或多个.heapsnapshot或.rawheap文件，再手动导入匹配的.jsleaklist文件。

26.0.0以下版本，支持先导入一个或多个.heapsnapshot或.rawheap文件，再手动导入匹配的.jsleaklist文件。

**说明** 

* 导入文件时，选择的 .rawheap 文件与匹配的 .jsleaklist 文件需位于同一文件夹下。
* 单个.heapsnapshot和.rawheap文件文件大小不超过1.5G，单个.jsleaklist文件大小不超过30M。
* 批量导入的文件数量不超过10个。
* 支持同时导入.rawheap和.jsleaklist文件。
* [JSLeakWatcher](../best-practices/bpta-js-leak-watcher.md)生成的文件中，.rawheap文件和.jsleaklist文件的文件名相同，则认为是匹配的。.jsleaklist文件与.heapsnapshot文件通过文件中的hash值匹配。

1. 在DevEco Profiler主界面的Create Session区域中，单击**Open File**，导入.heapsnapshot、.rawheap或.jsleaklist文件。
2. 离线导入文件成功后，在**Leaks**区域展示JSLeakWatcher监控采集到的内存泄漏对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9q_p15vVRDS7fuzV9BdFwA/zh-cn_image_0000002731382989.png "点击放大")

## 解析内存对象

从DevEco Studio 6.1.0 Beta2开始，DevEco Profiler支持导入[代码混淆产物nameCache](ide-exception-stack-parsing-principle.md#section19215122372720)文件和[ArkTS调试产物sourceMap](ide-exception-stack-parsing-principle.md#section666114451518)文件，还原文件名称和文件路径。以nameCache文件为例。

文件导入前，Class为d8。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/5H3LL1WiSviCCCNBM6Nt8Q/zh-cn_image_0000002731382979.png "点击放大")

点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/b_nVGEWxTNqRTmiKill4qQ/zh-cn_image_0000002701663764.png)按钮，导入nameCache文件，Class显示为文件名称MyAbilityStage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/lt8wSro9T6mNeXOLYoTsHA/zh-cn_image_0000002701663760.png "点击放大")
