---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations
title: Snapshot模板基本操作
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 内存泄漏：Snapshot分析 > Snapshot模板基本操作
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:223abeba55aaf2f63d526fc2b4b47181a915bd2ec1244a1137e80cbc7349220d
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/J6R5d6qyT2G4cEXrrFG16g/zh-cn_image_0000002808886943.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=54911B84DCE219E84E62F79EA74FCDD0E4823FFD9290581E441C75862A2D5AFC)
2. 开始录制后观察**Memory**泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wAn-gp9rQNGds-3Dr5GaUw/zh-cn_image_0000002808766865.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A12075C873F502A2D377AF8A73EA807EE1A4CB578EA1F683DE0DA900FAFB20B7 "点击放大")启动一次快照，一次快照完成后会在**ArkTS Snapshot**泳道出现紫色区块。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/2MkoUmyjQ6WaGRBxM0XuKw/zh-cn_image_0000002808766863.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D9A26B131D015C350C263893F60FD26272CA53944B7E1C2BD1551869E78FBCF "点击放大")

   点选ArkTS Snapshot泳道的紫色区块，**Statistics**区域显示当前快照的详细信息：

   * Constructor：构造器。
   * Count：该对象的数量。
   * Distance：从GC Root到这个对象的距离。
   * Shallow Size：该对象的实际大小。
   * Retained Size：当前对象释放时，总共可以释放的内存大小。
   * Native Size：该对象所引用的Native内存大小。
   * Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
   * 带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/ip3YnfvmSjm6ut3OH2C3Tw/zh-cn_image_0000002779407292.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=02CF6FE394A7D01E85E2AA89F517ED2F2E6CFD58525B8DDE0183076BD64C6608 "点击放大")标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jcV9xfmCSUW-kLAxipDFfA/zh-cn_image_0000002808886929.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF013F3004816879E01766AC143BEB2040D7D5352A4C79614E6A3A723A3F5586 "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

## 比较快照差异

在**ArkTS Snapshot**泳道的**Comparison**区域，点击任一快照作为base，在**CompareTo**下拉框选择的快照作为Target，即可得到两次快照信息的比较结果。比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/y34T2nnLTQCLl_APkxPx_Q/zh-cn_image_0000002779567272.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3A9AC34253E85028BD9B69A4E8013B7C8C91BBB143A7FA640B3C283C37A6FF3 "点击放大")

从26.0.1版本开始，**Comparison**区域中**Size Delta(Allocate/Free)**列名称变更为**Shallow Size Delta(Allocate/Free)**，以及新增**Retained Size Delta(Allocate/Free)**列，用于分析持有内存的大小增量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/7MnG8Q2_RD2HIVgOifRgGQ/zh-cn_image_0000002808886915.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=340608CEF9358F26E4D637E7679723DE3DC3E364151AB1B9ECD6D3A42BB02E2E "点击放大")

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
* Path：编译后的源码路径。支持通过点击属性名称旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/5HrQi5lJT0WfWzgyaeM31g/zh-cn_image_0000002808886927.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=845F81249CF6F9BFFC1B1EB1B04A8928DCA861E56B8605A4F1B64A53B52BDCE3)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/UZavEKSTT36yWNASoTa-nw/zh-cn_image_0000002779567278.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E064799D25E8E6217746F22065C62C764E157A976665CF95A40CB478CC3CD2A "点击放大")

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/IoAXq7hxSVC_Uy04nn4VVA/zh-cn_image_0000002779407296.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F9F72759C6EB50336590531354E4A3E1D5A0C5E8233205C7E9F1932C13F279C "点击放大")

**说明** 

* 确保工程代码路径与解析信息匹配，否则跳转可能失败。
* 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
* 对象名称后的line=0时表示无效行号，不支持跳转。

## 查看节点属性和引用链

在**ArkTS Snapshot**泳道的**Statistics**区域和**Comparison**区域中，展开所有实例对象节点，可看到**fields**和**references**，分别表示该实例对象的属性和该实例对象的引用链信息，或者点击实例对象，在右侧**More**区域中查找Fields和References。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/uMtUkmZtQSWDCOrYs5fJ3A/zh-cn_image_0000002808766847.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C875454C1D4A57B5300DC9CB18AB3AB6654156B66DF086A52BED85DCD10907A "点击放大")

## 节点跳转

在**ArkTS Snapshot**泳道的**Comparison**区域中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的**Statistics**区域并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/B22H49jiSnac1LdEW209NA/zh-cn_image_0000002779407280.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F3E589CF6A733B4477A1C855F41A8ECD3DE75B4216A4424516595F6983E2B2E "点击放大")

## 历史节点前进和后退

当在ArkTS Snapshot泳道的**Comparison**和**Statistics**之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/mirEn93vT5exPD9zDcnB_g/zh-cn_image_0000002808766849.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C4F6D30857BF87E77AD90FC0A095C17C381AAB0A1EF61A8F620967B8959D2C9 "点击放大")

## 获取节点支配树

从26.0.0版本开始**，ArkTS** **Snapshot**泳道支持一键获取节点支配树，系统会以GC Roots为根节点构建内存对象的支配树。选中一个实例结点后，在右侧**Dominator Path****s**页签查看支配树。

在支配树结构中，若到达目标对象的任何路径都必须经过某节点，则该节点即为其支配者。通过展示从GC Roots到目标实例在支配树上的支配链，系统能够剥离错综复杂的冗余与交叉引用，直接定位到内存泄漏的支配者。断开路径上的支配者即可释放关联内存，从而更精准、高效地解决内存泄漏问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/8e_qpB6cTU68ARvlHgr2FA/zh-cn_image_0000002779567258.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F20F99C5B935A9AF19949062806ECD8667F7516B89BB786476592F9B26F4F38 "点击放大")

## 引用链向最小引用距离展开

**ArkTS** **Snapshot**泳道支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

### DevEco Studio 6.1.0 Beta2及以上版本

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧**Shortest Paths**页签展示。

从26.0.0版本开始，点击**Shortest Paths**页签左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/VDVzxOXgTLyZePVIMrYPCw/zh-cn_image_0000002779407294.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=118ED56D12279CEAEC23783DBCEC7485923408FB7F7B35A0D7A48FAF102723A2 "点击放大")按钮，可将页签中的数据导出到本地进行保存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/YatGkohuSsuv4_2qqK3tew/zh-cn_image_0000002779567246.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB0B13F428B196D11045654A4A82450A40894EA9951D90E1892CE46E1C963C51 "点击放大")

从26.0.0版本开始，若应用编译模式为release，且启用了源码混淆，**Constructor**将展示混淆后的源码路径。若调试应用工程存在对应的nameCache文件，点击**Show SourceClassName**按钮，即可显示混淆前的源码路径，否则需要导入调试应用对应的nameCache文件后再点击按钮。

此外，若调试应用工程存在对应的SourceMap文件，点击源码路径旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/RijphDifTSKeJS2NB6JlTA/zh-cn_image_0000002779567276.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A1C326673A96E0F12C031FB3A5AAA04394C53FB14D8B385C7A0639AFC4236EA)图标，可直接跳转至工程中的代码位置，方便开发者快速调试，否则需要导入调试应用对应的SourceMap文件后再点击按钮跳转到源码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/sJ2t9gGlRneOTJx9hDLjNQ/zh-cn_image_0000002779407290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A928B31A3EB56B468570985D6E3519CFC2BC31A7D132C4D64DF95833981B54C "点击放大")

### DevEco Studio 6.1.0 Beta2以下版本

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/t36KnWX1SEaMhfyutiCSRw/zh-cn_image_0000002808886945.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FFC74E80B8A7D5858BB182713BDB80A335F560417F879BC5FFD901AAE947FC1 "点击放大")

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/2G5kSKIeRbeMjuOEzl4AGw/zh-cn_image_0000002779567270.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=94F5591875C14C4F3676EB1E6CCF5668D39AC753D203C581086865FCD8683255 "点击放大")

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/yY45W7E6RYyGcryCVLjVVA/zh-cn_image_0000002779407300.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=3967B9F6800911E5A2635BADCB2773F30040712FDCBB62585EF4DA79C0001FA1 "点击放大")

## 合并展示最小引用距离

从DevEco Studio 6.1.1 Beta1版本开始，在**ArkTS Snapshot**泳道的**Statistics**区域中，选中一个构造器或实例结点，点击底部搜索栏的**References**按钮并确认，在右侧**Merged Incoming References**页签可查看该节点构造器下的所有实例到GC Roots的最短路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/HBY8fBeYTcKsVa8YcTs39A/zh-cn_image_0000002808886941.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A8405DC29933BB4D4E0AB12F7C39C274340898566F5992913721EF91071D41D "点击放大")

从26.0.1版本开始，在**ArkTS Snapshot**泳道的**Statistics**区域中，选择一个构造器或者按住鼠标左键拖选（或使用快捷键Ctrl+Click，macOS中为Command+Click）多个构造器后，点击底部搜索栏的**References**按钮并确认，在右侧**Merged Shortest Paths**页签可查看构造器下的所有实例到GC Roots的最短路径，或者切换方向查看GC Roots到构造器下所有实例的最短路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Pmvg3J9DRtGPdJWZhtozhQ/zh-cn_image_0000002808886909.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=002CE046CDBEA09BFE415C13BE08F6EFC25D071FA908EBDD7394DED8339086DF "点击放大")

## 聚类展示构造器或对象

### 26.0.1及以上版本

**ArkTS Snapshot**泳道的**Statistics**区域支持的聚类规则、构造器或对象如下。

**当前支持的构造器类型包括**：所有构造器节点（GlobalEnv、GlobalObject、HiddenClass(NonMovable)、SourceTextModule、Promise、PromiseRecord、PromiseCapability、(handle)除外）。其中，(handle)中的LocalHandleRoot、GlobalHandleRoot对象支持聚类展示。

**当前支持的聚类规则包括**：Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths、Merge Same Name、Merge Native List、Merge Same Name and Native List。

* Merge Shortest Paths：最短引用链聚类。以对象到GC Roots的最短引用链进行聚类展示，用"->"拼接。
* Merge Same Property：属性聚类。
  + JSArray：以“属性名”进行聚类展示，用","拼接。
  + Proxy：以属性“target”的值进行聚类展示，用","拼接。
  + PromiseReaction：以属性“handler”的值进行聚类展示，用","拼接。
  + 其他支持该聚类规则的构造器：以“属性名 :: 属性值”进行聚类展示，用","拼接。
* Merge Same Property and Shortest Paths：属性+最短引用链聚类。属性聚类后与最短引用链聚类后，用"|"拼接。
* Merge Same Name：名称聚类。
  + LocalHandleRoot、GlobalHandleRoot：该节点下fields的显示规则为"序号 :: 属性名称"，将fieIds下相同名称的属性进行聚类展示。
  + 其他支持该聚类规则的构造器：将相同名称的实例进行聚类展示。
* Merge Native List：原生列表聚类。将右侧Native List区域的实例对象Native堆栈信息进行聚类展示。
  + 若无Native List区域或Native List区域无数据，以“NoNativeCallTree”进行聚类展示。
  + 若Native List区域均为系统代码，以“全部调用栈”进行聚类展示，用"->"拼接。
  + 若Native List区域包含开发者自定义代码与系统代码，以“开发者自定义代码”进行聚类展示，用"->"拼接。
* Merge Same Name and Native List：名称+原生列表聚类。名称聚类后与原生列表聚类后用"|"拼接。

构造器或对象适用的聚类规则如下：

| 构造器或对象 | 支持的聚类规则 |
| --- | --- |
| 所有构造器节点  （GlobalEnv、GlobalObject、HiddenClass(NonMovable)、SourceTextModule、Promise、PromiseRecord、PromiseCapability、(handle)、(string)、(closure)、(framework)、(array)除外） | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths |
| (string) | Merge Shortest Paths |
| (closure)、(framework)、(array) | Merge Shortest Paths、Merge Same Property、Merge Same Property and Shortest Paths、Merge Same Name |
| LocalHandleRoot、GlobalHandleRoot | Merge Same Name、Merge Native List、Merge Same Name and Native List |

对于不支持聚类的构造器节点，具体原因如下：

| 构造器节点 | 不支持聚类的原因 |
| --- | --- |
| GlobalEnv、GlobalObject | 虚拟机唯一对象，无需聚类。 |
| HiddenClass(NonMovable) | 虚拟机内部创建，与对象存放地址有关，开发者无需关注，无需聚类。 |
| SourceTextModule | 系统侧创建用于管理模块级对象的，每个SourceTextModule对应一个ts文件，已自动聚类。 |
| Promise、PromiseRecord、PromiseCapability | 异步任务创建时的内部使用对象，开发者无需关注，请参考PromiseReaction聚类结果。 |
| (handle) | 节点中的对象固定有四个，无需再做聚类。 |

**说明** 

对于LocalHandleRoot和GlobalHandleRoot对象，不同模板支持的聚类规则有所差异，具体为：

* [Allocation模板](ide-insight-session-allocations.md)支持Merge Same Name、Merge Native List、Merge Same Name and Native List三种聚类规则。
* Snapshot模板和[Commemory模板](ide-commemory.md)仅支持Merge Same Name一种聚类规则。

在Statistics区域选择构造器或对象后，底部搜索栏按钮呈可点击状态。点击该按钮并配置聚类规则，展开构造器时将按规则展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/3FNoInJ1QRawOJjGKjpjFg/zh-cn_image_0000002779567264.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=848357826122682A31AF07F98CB20B05FE90DF273386490463B5C131398E28EE "点击放大")

选择不支持聚类的构造器节点时，鼠标放在底部按钮旁的问号图标上，会有提示词弹出，提示不支持聚类的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/squKvgo5RkWATxb6_LGj4A/zh-cn_image_0000002808766825.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DEE32F219D6A2522E56D3F9DEC04B24CEC91D62B9AC453C08D6A06883B44059 "点击放大")

### 26.0.0版本

从26.0.0版本开始，**ArkTS Snapshot**泳道的**Statistics**区域支持按不同聚类规则展示构造器或对象。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/L0v-cYUYTQ-CxmQH_osBcA/zh-cn_image_0000002808766831.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C999071945BC40E2C494CC12D329653ACFC1A576B7D7A4D02ACD315AE43CA3A "点击放大")

## 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，**ArkTS** **Snapshot**泳道支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/WESji9BHR2mZJN7etHojqg/zh-cn_image_0000002779407302.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E0E268EC3F968D42E46A9E1B28F31CC1E803800CE5EB6C0B7B741E852419A02 "点击放大")

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

* Retained Size：按照Retained Size从大到小展示周边节点。
* Distance：按照Distance从小到大展示周边节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ZUuK1kIlT8CRULA6O-AYSg/zh-cn_image_0000002779407288.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=29840491A1AB7C15834F2343F950939BF8C748D962EB5465A6333A935F32DBBA "点击放大")

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/CCdiwajoQ6WgFRL3UqEEJA/zh-cn_image_0000002779567280.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=85B791178DD6CC25B07991DB2CBF152BA4903A8180CB46B45F659F29A7813DED "点击放大")

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References、Dominator Paths和Shortest Paths页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

* **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
* **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
* **Redraw with this node**：以该节点为中心重绘。
* **Reveal in Statistics**：在Statistics页面中显示该节点。
* **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/txwuwfqdTQurOPisLilXeQ/zh-cn_image_0000002779567274.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E365615E4EE29B4CDB324FCD640CD95320F3DF3B28E62FD68A6E960D3E2F679 "点击放大")

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/2KyGfAzaQJanUsaz21Gawg/zh-cn_image_0000002808766857.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=73D2E0D784D2D74465642C0286A34DBC86BA951E2C972D0A53082B1B1D577B66 "点击放大")

## 搜索内存对象

**ArkTS** **Snapshot**泳道的**Statistics**区域和**Comparison**区域支持按对象名称搜索内存对象，在底部搜索框中输入对象名称即可进行模糊查询。

从26.0.0版本开始，**Statistics**区域底部搜索框支持通过对象id精确定位目标对象，格式为：@id。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/jKYU4jdvQpSE-QWaxdR4Pw/zh-cn_image_0000002808766851.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6D119CA9602AE7668BF4EEEB011E38FE19E65B8CAB1BB993C358273DF6DE6E7 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/XbkQkGMxSS2mXhcKYVk7Yg/zh-cn_image_0000002808886939.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D49E3F66BED865E72D496916FE15AD8DF007A721668CE75576FE492D57F6614D "点击放大")

## 解析内存对象

从DevEco Studio 6.1.0 Beta2开始，DevEco Profiler支持导入[代码混淆产物nameCache](ide-exception-stack-parsing-principle.md#section19215122372720)文件和[ArkTS调试产物sourceMap](ide-exception-stack-parsing-principle.md#section666114451518)文件，还原文件名称和文件路径。以nameCache文件为例。

文件导入前，Class为y10。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/JsNGQFW8Tlao5O4eAGCS8g/zh-cn_image_0000002779567260.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B894ABEA97A2711ED72853B07676974DD447564FE2AC99DC0663CF7F9164144 "点击放大")

点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kXiL6ih3QlOlPqCr0LPX_Q/zh-cn_image_0000002808766855.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D02E17CC3A5AEC8E1240939FDEF191F6D57A0873BA065908FBD9E436079F24F3)按钮，导入nameCache文件，Class显示为文件名称TestLaunchPage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/sGZsghoERt-_aGCiqId_0w/zh-cn_image_0000002808766843.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A54198BBE59A9B49856FEB4BB72E9CD78AE80CD6CF469C44E3BA929202004500 "点击放大")
