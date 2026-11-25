---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-leak-in-develop
title: 开发态快速定位ArkTS泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位ArkTS泄漏
category: best-practices
scraped_at: 2026-11-25T11:33:38+08:00
doc_updated_at: 2026-11-24
content_hash: sha256:34e5b1033916b8b4fa743fa783c921bac4c67d46831efea1b3be6d05ec95e846
---

## 概述

在ArkTS中，开发者无需手动管理内存。但如果代码中存在不合理的引用，系统就无法正确回收内存，从而引发内存泄漏。本文将通过常见泄漏场景和ArkTS内存泄漏分析案例，帮助开发者快速定位应用中的内存泄漏问题。

## ArkTS泄漏根因

ArkTS运行时采用[HPP GC](../harmonyos-guides/gc-introduction.md#hpp-gc)（即高性能部分垃圾回收），将对象按生命周期划分为新生代和老年代。GC使用标记-清除（mark-and-sweep）算法回收内存：标记所有可达对象为存活，回收不可达对象。每次GC都从根节点开始遍历，根节点即GC Root。如下图所示，GC回收从GC Root不可达的Node H、I、J节点：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/NcKZMNAEQHmyb0jqLz_AaQ/zh-cn_image_0000002793526498.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FEBDCD8F8AD6A3144A4F083B3F0A91FE2F40139E62C15C67DB9BF8F13FF2EFB)

理解垃圾回收（GC）机制的核心，在于把握一个根本原则：GC仅回收那些从GC Root不可达的对象。换言之，只要一个对象仍处于引用树的路径之上，即便程序逻辑已遗忘该对象、不再实际需要它，GC也无力回收。内存泄漏的本质不是GC失效，而是开发者留下了不该留的引用链。因此排查内存泄漏的关键，是找到从GC Root出发、让无用对象“存活”的引用路径，并在适当位置切断该路径。

## 常见泄漏场景

### VMRoot类型持有导致内存泄漏

常见构成VMRoot引用的来源包括：

* 模块导出对象：底层SourceTextModule系统对象持有export出的对象，且模块在应用生命周期内不卸载。
* 全局对象属性：通过globalThis.xxx=xxx挂载的对象，globalThis是贯穿应用始终的根对象。
* 内置原型链扩展：修改Array.prototype、Object.prototype等内置对象原型，导致意外全局持有。

一旦业务对象挂载到上述根节点上，即使页面销毁、组件卸载，VMRoot依然强引用该对象，GC无法回收。

### Native句柄引用导致的内存泄漏

在HarmonyOS的JS-Native交互中，Native代码可通过NAPI（Node-API）访问或持有JS对象。Native代码引用JS对象时，主要使用两种句柄类型：napi\_value、napi\_ref。其中，napi\_ref是一种引用计数的句柄，用于保持对JS对象的引用，防止垃圾回收器在Native代码持有引用期间回收该对象。

* Local Handle（napi\_value）：通常指在Native代码执行上下文中创建的、作用域较短的引用。Native代码执行环境切换时，系统通常自动清理这些Local Handle。Handle Scope管理Local Handle，具体规则如下：

  + 同步调用、NAPI框架异步调用等大部分场景下，系统自动为创建的Local Handle添加Handle Scope。
  + libuv异步调用等场景下，系统不主动添加Handle Scope，应用须自行添加，否则系统无法回收JS对象。
* Global Handle（napi\_ref）：指作用域为整个应用生命周期的引用。一旦创建，除非显式删除，该句柄会一直保持对JS对象的引用，通常用于跨模块、跨上下文、跨JS线程访问的JS对象。由于其持久性，开发者使用不当时，该句柄容易成为JS对象泄漏的根源。

当Native代码通过Local Handle或Global Handle持有JS对象时，两者之间即建立强引用关系。此时GC的可达性判定规则如下：

* JS代码清除对象的所有可达性引用（如JS代码内部引用、组件树等）后，若无Native句柄指向该对象，GC即可回收该对象。
* 若存在Native句柄指向该对象，该句柄则构成一个阻止根。Native代码持有该句柄期间，该对象对GC而言“可达”，GC无法回收该对象，可能导致内存泄漏。

### FrameRoot类型持有导致内存泄漏

正常情况下，函数执行完毕退栈后，栈帧销毁，其中的临时引用自动失效，内存随之释放。然而，若函数长期不退栈，FrameRoot将持续锚定局部变量/参数所引用的对象，此时即便业务逻辑已不再需要这些对象，GC也无法回收。

常见导致栈帧滞留的情形包括：

* 死循环或无限递归，函数永不返回。
* 在函数内启动了一个长期运行的同步阻塞操作（如同步网络请求、大文件同步读写）。
* 函数内部创建闭包，外部长期持有该闭包，且闭包捕获了该函数栈帧中的变量（导致整个栈帧无法释放）。
* 使用了生成器（Generator）或async/await但未正确消费，导致协程挂起，栈帧保留。

## 标准化排查流程

1. 复现与观察：使用DevEco Profiler的Realtime Monitor（Memory泳道），重复多次进出目标页面，观察内存曲线是否呈阶梯状上升。
2. 识别泄漏点：在操作前后各采集一次堆快照，使用Snapshot对比功能，关注新增对象数量和Shallow Size，从而识别泄漏点。
3. 查看对象引用链：在Snapshot快照的对象引用链中找到异常存活对象（如本该销毁的Component实例），通过“Shortest Paths”分析引用链情况。
4. 是否VMRoot持有：若引用链顶端为VMRoot/SourceTextModule，多为模块导出单例或全局变量未清理。
5. 是否Local/Global Handle持有：若泄漏对象的Distance为1，则多为Native侧持有未释放导致。可分为两种场景：

   * Local Handle：napi\_value未使用napi\_open\_handle\_scope()，或未成对使用（即调用了napi\_open\_handle\_scope()但未调用napi\_close\_handle\_scope()释放）。
   * Global Handle：napi\_ref未调用napi\_delete\_reference()释放，或未成对使用（即调用了napi\_create\_reference()但未调用napi\_delete\_reference()释放）。

   在这两种情况下，无法基于引用链分析，需要通过Allocation模板开启Local Handle及Global Handle录制选项来进一步分析。
6. 是否FrameRoot持有：若非VMRoot和Local Handle/Global Handle持有，则多为函数不退栈或外部持有闭包捕获的对象。
7. 代码审查：根据引用链中的关键节点（如EventHub、Timer、全局变量、napi\_ref、闭包上下文）定位代码中的持有关系。
8. 修复与验证：修改代码后重复步骤1~2，确认内存曲线回归平稳。

标准化排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/RZsALwEdRDeGV4Om-7XiCA/zh-cn_image_0000002793686476.jpg?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=44CF7D83BF7B5180FACE78F8638B8DB756CA453514BA0ED245A4D34C74172EBE "点击放大")

## ArkTS内存泄漏分析案例

### 案例背景

**现象**：本案例中，通过复现“首页至消息页面”的反复进出操作，观察到应用内存占用呈现“阶梯式持续增长”趋势。在循环操作10次后，应用出现显著卡顿现象。

**初步判断**：典型的“阶梯式内存增长”，高度疑似内存泄漏。

### VMRoot类型泄漏分析流程

1. **Memory泳道确认泄漏**

   1.1 打开DevEco Studio，连接真机，单击Profiler工具的Realtime Monitor（也可使用Snapshot模板的Memory录制观察，本文以Realtime Monitor为例）。

   1.2 启动应用，选择设备与应用进程。

   1.3 单击录制按钮，在设备上重复执行“进入消息页面→停留2秒→返回首页”的操作。

   1.4 观察内存曲线：正常预期为每次退出后内存回落至基线附近，整体呈锯齿状；本案例实际现象为曲线呈阶梯状上升，多次操作后内存增长至314.1MB且无明显回落，存在内存泄漏，内存曲线如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/BrQYjk-GTJihwUiHdBl_sg/zh-cn_image_0000002822486383.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=90784D2D08C34C6010676857BBFEB265DDE31E7BCBFDE4634C398B39F5383C78 "点击放大")
2. **堆快照对比定位异常对象**

   2.1 在Profiler中切换到Snapshot模板，请参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)：选择Profiler工具→选择设备与应用进程→选择Snapshot模板→创建Session→启动录制，操作入口如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/IjL7JAr_TKCcvGZQR82L7w/zh-cn_image_0000002822366405.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=497EAD0AC429C69F3FA46BCBCA7F2B95F2A54277801142B9A1BB50675D30FF2E)

   2.2 抓取快照1：首次进入消息页面之前，单击“Take Heap Snapshot”，操作如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/yawmRzVoRDqvMuiWx6FmTQ/zh-cn_image_0000002793526500.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=35E06EC446FB73BED68ADFD8994E5D3E0CD40E50FD6A2B7828A80602039E4C0F "点击放大")

   2.3 抓取快照2：重复进出消息页面10次后，回到首页，单击“Take Heap Snapshot”，再抓取第二次快照，并停止录制，操作如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/XcLXC9QuR_Ch01vLTV8njg/zh-cn_image_0000002793686478.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1EC89E532455D15973188CDAD394F2174BDC3A087082C15DCE5E0F2BA626C54 "点击放大")

   2.4 在快照对比视图Comparison中，选择CompareTo Snapshot1，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/CgDp3YB6QyWU4ekVXGviwA/zh-cn_image_0000002822486385.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=65405BD8F406DA72AB36DC091DAC6D290DEB611122ACBC5165A3D8EAC157218F)

   2.5 查看对象新增销毁情况，优先关注以下两类对象：

   * 数量为操作次数的整数倍或整数倍+1的对象（export出的对象本身也有一条引用链）。
   * 业务对象，即Constructor的结构为“包名/模块名/文件路径#泄漏对象”的对象。

   对比视图中的异常对象如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/nqIb3bxJRi6ZIqHNlFr_Hg/zh-cn_image_0000002822366407.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=021D03E8EA6A3DE1743F914E94BEECC40A75FFCCD751D217E15ED0341A8C150C "点击放大")

   关键发现：

   * 对比结果中，Test、LeakB、LeakC、LeakD等对象实例数量从0个增加到11个，上述对象实例泄漏。
   * 正常情况下，页面退出后垃圾回收器应回收组件实例，快照2中应只剩1个Test对象（export持有该对象）。
3. **追踪引用链**

   **方法一：基于聚类功能追踪引用链**

   自26.0.1版本起，构造器节点均支持聚类展示，详见[聚类展示构造器或对象](../doccenter-deveco-studio/ide-snapshot-basic-operations.md#section16681149195317)。在“Statistics”标签页中，使用Ctrl+单击（macOS中为Command+单击）选择Test、LeakB、LeakC、LeakD等构造器。单击底部搜索栏的References按钮并确认，即可合并展示这些构造器下所有实例到GC Roots的最短引用链。具体操作请参考[合并展示最小引用距离](../doccenter-deveco-studio/ide-snapshot-basic-operations.md#section1759111226)。在右侧“Merged Shortest Paths”标签页中快速定位异常对象的GC Root。聚类结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/EmIeElSAQSCSEdddomuMBw/zh-cn_image_0000002793526502.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB04186656F2330C981DA1BA046B7ED1D3E1D6AA6869F6013CA42FCC1C8B22FE)

   合并之后可以看到从GC Root到叶子节点的完整路径，各对象的引用链如下：

   * Test对象：SourceTextModule(GC Root)->Test
   * LeakB对象：SourceTextModule(GC Root)->Test->LeakB
   * LeakC对象：SourceTextModule(GC Root)->Test->LeakC
   * LeakD对象：SourceTextModule(GC Root)->Test->LeakD

   **方法二：基于快照对比视图追踪引用链**

   在快照对比视图中，展开并选中一个Test对象实例，优先选择Distance数值较大的实例（此处选择Distance为“6”的实例），并打开右侧详细信息面板，操作如下图所示：

   注：优先选择Distance数值较大的对象实例，是因为此类实例创建频繁且未及时释放，表明存在潜在的内存泄漏问题，需要进一步调查以确定具体的泄漏源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/FBLuCNhqSquogcXZ9bj1pg/zh-cn_image_0000002793686480.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=14F39A1CD3B1C5916879E5162869990686AC1291D34A9B72FEA699D3B98D08D8 "点击放大")

   单击“Shortest Paths”，获得如下Test对象实例的最短引用链：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/WgROIKNhRVa_i53XWZEY2Q/zh-cn_image_0000002822486387.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F0940CCA667A0AE7EE7C85120A80E1D4434812FCDBA6DB07207A30869A1C874 "点击放大")

   同上，查看LeakB、LeakC以及LeakD对象的最短引用链。
4. **分析VMRoot类型持有导致泄漏问题**

   4.1 根据步骤3得到的Test对象实例的最短引用链分析，该引用链的GC Root为SourceTextModule，符合模块导出对象持有导致的VMRoot泄漏类型场景，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/bv43rqH_RnWPvJ1qYq026A/zh-cn_image_0000002822366409.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3DDEDEFBD57BB890115229A3DFA93C16773E4C5FB65663484F68A28BA7D4006 "点击放大")

   4.2 沿引用链向GC Root方向排查，找到第一个业务对象：CacheTest.ts文件中的CacheTest对象，其cache属性持有Test对象未释放。单击后面的跳转图标，打开CacheTest对象实例详细面板，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/S4wAf6LpRA2zAHXeWpmfJg/zh-cn_image_0000002793526504.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=73D475B73B00C222B595C1B34050F603E7A19140E163087C4241369F64D6F18F "点击放大")

   4.3 在CacheTest对象实例面板中，单击对象名后的跳转按钮，跳转到对应代码行，操作如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/yO7WPTvPQ2K6nGuO2agGoQ/zh-cn_image_0000002793686482.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BA5D740FD9E47D3B374F9CC49EB97C155F57D61B51436D9E86218EAA71267A9)

   4.4 跳转到代码后分析：CacheTest对象存在静态属性cache，该静态属性中保存了Test对象，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/i9b2AM_pSW6bh9GqZBscew/zh-cn_image_0000002822486389.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=D341B902AE4FD9AC76103BCA3504FA91CA514B225F6DDFEFAABA2225A6D1B287 "点击放大")

   4.5 结合业务代码分析：MessageCenterPage组件创建时向CacheTest保存了一个Test对象，但组件销毁时未清理该缓存，导致内存泄漏，如下代码所示：

   ```screen
   @ComponentV2
   export struct MessageCenterPage {
     // ...

     aboutToAppear(): void {
       try {
         CacheTest.cache.add(this.testObj);
       } catch (error) {
         const err = error as BusinessError;
         Logger.error(TAG, `Failed to add test object to cache, code: ${err.code}, message: ${err.message}`);
       }
       // ...
     }

     // ...
   }
   ```

   4.6 修改代码，将如下代码中KEEP\_LEAK\_ON\_EXIT改为false，在页面销毁时清除缓存。

   ```screen
   // Demo switch: when true, cached objects are kept leaked on page exit for memory profiling
   const KEEP_LEAK_ON_EXIT: boolean = true;

   // ...

   @ComponentV2
   export struct MessageCenterPage {
     // ...

     aboutToDisappear(): void {
       if (KEEP_LEAK_ON_EXIT) {
         return;
       }
       try {
         CacheTest.cache.removeLast();
       } catch (error) {
         const err = error as BusinessError;
         Logger.error(TAG, `Failed to remove last test object from cache, code: ${err.code}, message: ${err.message}`);
       }
     }

     // ...
   }
   ```

   修改后重新复现操作7次，并抓取快照验证：Test对象创建数量正常；但Proxy对象数量异常，创建70个未销毁，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Lq87V4joTXSfeT_uB58j6Q/zh-cn_image_0000002822366411.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=1EE1EA9A2FCEB553BA1D91CD67A37C3E8D09867DB114149DD9D46E5262A10617 "点击放大")

   4.7 参考“步骤3：追踪引用链”，找到最短引用链。该Proxy对象的Distance为1，说明GC Root直接持有该对象，即Native侧句柄持有该对象未释放，属于Local Handle或Global Handle引用JS对象导致的内存泄漏，最短引用链如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/mcDgkXUCT2Wx7RlvJHNYJw/zh-cn_image_0000002793526506.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BDF8B5DD0B18FCD82A887C6EFB0BCF41666B89F70C33FDC495161E86C42D2A5 "点击放大")

   4.8 查看Distance为1的Proxy对象的References信息，确认Global Handle引用该JS对象导致内存泄漏，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vgSJ1ndSRWKFsPckMbaVgA/zh-cn_image_0000002793686484.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=6172DDC16D4010FD9DCC7F580039CF5C5D49BF3E77CE188B176EDB7D29B8C0C2 "点击放大")

### Native句柄类型泄漏分析流程

上述步骤4已确认：Global Handle引用Proxy对象实例导致内存泄漏。此类Native句柄引用的泄漏无法基于引用链直接分析，需要通过Allocation模板捕获句柄相关的内存分配事件，定位创建该引用的Native调用栈。

1. **配置Allocation录制模板**

   1.1 连接真机并运行项目：①单击Profiler工具；②选择对应的真机设备及进程；③选择Allocation模板；④单击Create Session按钮创建Session。操作如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/RwN5lnV0Qiiz_OSIr5JDbw/zh-cn_image_0000002822486391.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A1BE50CF99D2D13F14A22AFFEFB23468608059FF05F9CE04BAD585030475AFF)

   1.2 配置开关：勾选“Local Handle”和“Global Handle”，这是关键配置。Allocation将专门捕获与JS-NAPI句柄相关的内存分配事件。如果底层镜像不支持该功能，则会提示“当前镜像版本不支持，请升级镜像”，配置界面如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ILvt49BATwGYKXlsXMBBFA/zh-cn_image_0000002822366413.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=602A13064D5D3D89186DD966726D51E6FCE908F5A618B2D7C9CBF4FE2A37D2C3 "点击放大")

   1.3 配置泳道范围：勾选ArkTS Snapshot泳道。Allocation将在录制结尾时自动抓取一份Snapshot快照用于关联分析，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/bpF0S8jmTce9tDw7shOc-Q/zh-cn_image_0000002793526508.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=61C4FF71ED246BC5F95C629B864685EEAC90C5A5AEF508898F0BF8C514ACE3C8)
2. **启动录制并捕获数据**

   2.1 启动录制：勾选“Local Handle”开关后，若本次为应用生命周期内首次录制Local Handle数据，系统会弹窗请求重启应用以便录制对应信息，此时单击OK允许重启即可，弹窗如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/sxtuMx54SdSUzyprYYxg4Q/zh-cn_image_0000002793686486.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=3FFA8B9DE0EADE2D1AE5E96BBF6614E979D03BF008B019D2D0D361FEB8A4860A "点击放大")

   2.2 运行应用程序：运行目标应用，反复执行疑似引入内存泄漏的业务操作，以增加内存压力并捕获更多内存分配数据。

   2.3 停止录制：停止后系统自动抓取一份Snapshot快照用于关联分析。单击快照，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DLmHh28bQHmcsKTNo1094w/zh-cn_image_0000002822486393.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0B5093D9F512B469A3DDD161AB5DEDAC06166AD992D3F581AC1881501B1A903)
3. **定位泄漏对象并分析Native句柄引用**

   * 虚拟节点handle：Snapshot内存快照中，虚拟节点handle包含四种RootType的虚拟节点信息，对应四种GC Root类型：VMRoot、FrameRoot、LocalHandleRoot、GlobalHandleRoot。RootType虚拟节点仅代表GC Root的类型，根据持有GC Root的RootType虚拟节点即可判断其类型。其中，API24及之后版本的内存快照支持查看LocalHandleRoot和GlobalHandleRoot，API26及之后版本的内存快照支持查看VMRoot和FrameRoot，handle节点如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/U_2PAjP1QRy3mRAmz9hxfQ/zh-cn_image_0000002822366415.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=29A650B679D1146DFB6E2297D99B601052D47B79AF9201077249D0F0AEE74188 "点击放大")
   * GlobalHandleRoot聚类分析：本案例为Global Handle引用导致的内存泄漏，因此选择GlobalHandleRoot进行聚类分析。在“ArkTS Snapshot”的“Statistics”标签页中，选中并展开handle虚拟节点，选中GlobalHandleRoot，对GlobalHandleRoot进行聚类，如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/0b7f3epIQO6jafYXgOMnoQ/zh-cn_image_0000002793526510.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=C81C3662CAADB641EE4CFC356540EE37C27A0EB483680FE047973A057EBAC876 "点击放大")

     **说明** 

     GlobalHandleRoot聚类分析功能自DevEco Studio 26.0.0版本起支持，低版本DevEco Studio的Profiler中不提供该功能。具体可参考[聚类展示构造器或对象](../doccenter-deveco-studio/ide-snapshot-basic-operations.md#section16681149195317)。

     展开并选中一个Proxy对象实例，并在右侧“Native List”标签页确认节点信息，可以看到调用栈底层的符号为ArkGlobalHandle，如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/7M92h-V1RzCdg3WcHlkSWQ/zh-cn_image_0000002793686488.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C21C113A9543020BAD27083FB9AC977A73A7790F933F12156C6D26C5116062F "点击放大")
   * 关键信息：通过调用栈定位应用Native代码（可能是ArkUI框架代码或应用自身代码）中创建napi\_ref的位置。

   **注意** 

   若该JS对象不是Local Handle或Global Handle引用的对象，则会提示“No Detail”；若Local Handle或Global Handle确实引用该JS对象，但对应的Native内存分配发生在本次录制开始之前，则本次录制结果无法展示对应的内存分配调用栈。此时需要重新录制，并尽量在业务逻辑开始执行前启动录制。
4. **分析内存分配调用栈**

   在“Native List”标签页中查看调用栈，定位对应业务代码。关键排查点如下：

   * 检查是否在适当的时机调用对应的句柄释放接口，如napi\_delete\_reference()。
   * 梳理这段Native代码引用ArkTS对象的合理性，识别引用的生命周期是否过长，是否应在某个条件满足后释放。
   * 对于napi\_ref，其引用计数是关键。确保在不再需要引用时正确调用napi\_delete\_reference()。注意，引用计数可能因其他代码路径的创建或删除操作而意外增减。
   * 检查libuv异步调用等场景中，句柄作用域是否正确添加Handle Scope。

   调用栈分析结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1iynKUrST1GnuA5Nfjj2YA/zh-cn_image_0000002822486395.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=10697BEAE12F28331D7DE68F0685CBB54496A451AAEC3B1CB8E77B296E82AFC8 "点击放大")

### 优化修复

1. 根据上述调用栈分析结果，在Native代码中调用napi\_delete\_reference()释放引用，需要将如下代码中KEEP\_REFERENCE\_LEAKED设置为false：

   ```screen
   // Demo switch: when true, the created napi_ref is kept leaked for memory profiling
   static const bool KEEP_REFERENCE_LEAKED = true;

   static napi_value ReferenceLeak(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value args[1] = {nullptr};

       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       napi_value proxy = args[0];
       TaskRef* taskRef = new TaskRef();
       napi_create_reference(env, proxy, 1, &taskRef->ref);

       if (KEEP_REFERENCE_LEAKED) {
           delete taskRef;
           return nullptr;
       }
       napi_delete_reference(env, taskRef->ref);
       delete taskRef;
       return nullptr;
   }
   ```
2. 重新运行应用，再次使用Memory泳道监控。
3. 重复多次进出消息页面。
4. 验证结果：

   * 内存曲线恢复锯齿状，每次退出后回落至基线。
   * 再次抓取快照对比，多次操作后业务对象实例数量无明显增长。

优化修复后的内存曲线如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/IpPS36pITTu8EDsiWT97mQ/zh-cn_image_0000002822366417.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B531300EF8B21672546D01AC9E9E61B4EE9630C2E2489042C24FBE1A05F03E6 "点击放大")

快照对比结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wEX64F_ySauCq1h_b7xe6Q/zh-cn_image_0000002793526512.png?HW-CC-KV=V1&HW-CC-Date=20261125T033338Z&HW-CC-Expire=31536000000&HW-CC-Sign=C93779FC75F79A9DBDDBDB339F35C819AE83762E9572E3914DC7EAA20BFC96F3 "点击放大")

## 术语介绍

本文涉及的关键术语如下表所示：

| 术语 | 解释 |
| --- | --- |
| **GC Root** | GC Root（Garbage Collection Root，垃圾回收引用链根节点）是垃圾回收器进行可达性分析的起点。从GC Root能访问到的节点对象是“存活的”，垃圾回收器回收其余对象。 |
| **引用链** | 在ArkTS中，“引用链”就是从某个GC Root（如VMRoot、FrameRoot等）出发，经过一连串的对象引用，最终到达目标对象的路径。  如果该路径存在，则该对象是“存活”的，GC不回收该对象；  如果从任何GC Root都无法找到一条到达该对象的引用链，该对象就是“不可达”的，GC将其标记为垃圾对象并回收。 |
| **VMRoot** | VMRoot是ArkTS虚拟机层面的根引用集合，代表GC遍历的起点。 |
| **FrameRoot** | FrameRoot是函数调用栈帧在GC遍历过程中的根节点。函数调用时，当前栈帧引用函数的局部变量和入参对象，这些对象从而成为GC的“可达”起点。 |
| **Local Handle** | Local Handle（本地句柄）是一种短期引用，用于在本地作用域（如函数调用栈）内持有对象，防止垃圾回收器回收对象。当作用域结束时，系统自动释放这些句柄。 |
| **Global Handle** | Global Handle（全局句柄）例如napi\_ref，用于长期持有对象引用，确保对象生命周期内垃圾回收机制不回收该对象。使用此类句柄时，开发者需要手动管理其生命周期，包括创建和销毁，以避免潜在的内存泄漏问题。 |

## 示例代码

[基于ArkTS实现应用内存泄漏检测](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/tree/master/ArkTSMemoryLeak)
