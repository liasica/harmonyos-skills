---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-leak-in-develop
title: 开发态快速定位ArkTS泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位ArkTS泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-11-24
content_hash: sha256:1d5ac9c209890994da2a2561fa65e202ffd72e7ebebebccc34a2b5a18f073637
---

## 概述

在ArkTS中，开发者无需手动管理内存。但如果代码中存在不合理的引用，则会导致内存无法被正确回收，从而引发内存泄漏。本文将通过常见泄漏场景和ArkTS内存泄漏分析案例，帮助开发者快速定位应用中的内存泄漏问题。

## ArkTS内存泄漏根因

ArkTS运行时采用[HPP GC](../harmonyos-guides/gc-introduction.md#hpp-gc)（即高性能部分垃圾回收），将对象按生命周期划分为新生代和老年代。使用标记-清除（mark-and-sweep）算法回收内存，可达对象被标记为存活，其余对象将被回收。GC从根节点开始遍历，根节点因此被称为[GC Root](bpta-arkts-leak-in-develop.md#table17319174010236)。该树的快照如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/niprJVt9S8CFY9FibK34Kg/zh-cn_image_0000002793686490.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=A721D4D93D6F69E3A6CA378DAE4FFF2CCB1248273C9C3C363CA58743D915897B "点击放大")

理解垃圾回收（GC）机制的核心，在于把握一个根本原则：GC仅回收那些从GC Root不可达的对象。换言之，只要一个对象仍处于引用树的路径之上，即便它已被程序逻辑遗忘、不再被实际需要，GC也无力将其回收。内存泄漏的本质不是GC失效，而是开发者留下了不该留的[引用链](bpta-arkts-leak-in-develop.md#table17319174010236)。因此排查内存泄漏的关键，就是找到那条从GC Root出发、让无用对象“存活”的引用路径，并在适当位置将其切断。

## 常见泄漏场景

### JS对象被VMRoot类型持有导致内存泄漏

常见构成[VMRoot](bpta-arkts-leak-in-develop.md#table17319174010236)引用的来源包括：

* 模块导出对象：export出的对象被底层的SourceTextModule系统对象持有，而模块本身在应用生命周期内不被卸载。
* 全局对象属性：通过globalThis.xxx = ... 挂载的对象，globalThis是贯穿应用始终的根对象。
* 内置原型链扩展：修改Array.prototype、Object.prototype等内置对象原型，导致意外全局持有。

一旦业务对象挂载到上述根节点上，即使页面销毁、组件卸载，该对象依然被VMRoot强引用，GC无法回收。

### JS对象被Local Handle/Global Handle引用导致内存泄漏

在鸿蒙的JS-Native交互中，JS对象可以通过NAPI Native代码访问或持有。Native代码为了引用这些JS对象，会使用两种主要的句柄类型：napi\_value、napi\_ref。其中，napi\_ref是一种引用计数的句柄，用于保持对JS对象的引用，防止其在Native代码持有引用期间被垃圾回收器回收。

* [Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)(napi\_value): 通常指在Native代码执行上下文中创建的、作用域较短的引用。当Native代码执行环境切换时，这些[Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)通常会被自动清理。Local Handle受Handle Scope管理，大部分场景下（如同步调用、napi框架异步调用等）系统会为创建的Local Handle添加Handle Scope，但仍有部分场景（如libuv异步调用等）系统不会主动添加Handle Scope，需要应用自行管理，否则就会导致JS对象无法回收。
* [Global Handle](bpta-arkts-leak-in-develop.md#table17319174010236) (napi\_ref): 这是一种作用域为整个应用生命周期的引用。一旦创建，除非显式删除，否则它会一直保持对JS对象的引用。通常用于需要跨模块、跨上下文甚至跨JS线程访问的JS对象。由于其持久性，如果不加注意，很容易成为JS对象泄漏的根源。

当Native代码持有（无论是local还是global）一个JS对象时，它实际上建立了一种强引用关系。在JS引擎的垃圾回收机制中，如果一个JS对象的所有可达性引用（包括JS代码内部的引用、DOM树等）都被清除，该对象就可以被回收。然而，如果存在一个Native句柄指向它，那么这个句柄就构成了一个阻止根，使得该JS对象在Native代码持有该句柄期间，从垃圾回收器的角度看，它是“可达”的。这就阻止了JS对象被回收，从而可能导致内存泄漏。

### JS对象被FrameRoot类型持有导致内存泄漏

正常情况下，函数执行完毕退栈后，栈帧销毁，这些临时引用自动失效，内存随之释放。

然而，若函数长期不退栈，局部变量/参数所引用的对象将持续被[FrameRoot](bpta-arkts-leak-in-develop.md#table17319174010236)锚定，即便业务逻辑已不再需要它们，GC也无法回收。常见导致栈帧滞留的情形包括：

* 死循环或无限递归，函数永不返回。
* 在函数内启动了一个长期运行的同步阻塞操作（如同步网络请求、大文件同步读写）。
* 函数内部创建了闭包并被外部长期持有，且闭包捕获了该函数栈帧中的变量（导致整个栈帧无法释放）。
* 使用了生成器（Generator）或async/await但未正确消费，导致协程挂起，栈帧保留。

## 标准化排查流程

1. 复现与观察：使用DevEco Profiler的Realtime Monitor(Memory泳道)，重复多次进出目标页面，观察内存曲线是否呈阶梯状上升。
2. 识别泄漏点：在操作前后各采集一次堆快照，使用Snapshot对比功能，关注新增对象数量和Shallow Size，从而识别泄漏点。
3. 查看对象引用链：在Snapshot快照的对象引用链中找到异常存活对象（如本该销毁的Component实例），通过“Shortest Paths”分析引用链情况。
4. 是否VMRoot持有：若引用链顶端为[VMRoot](bpta-arkts-leak-in-develop.md#table17319174010236)/SourceTextModule，多为模块导出单例或全局变量未清理。
5. 是否Local/Global Handle持有：若泄漏对象的Distance为1，则多为Native侧持有未释放导致。可分为2种场景：
   * [Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)：napi\_value未使用napi\_open\_handle\_scope 或未成对使用（即使用napi\_open\_handle\_scope但是未使用napi\_close\_handle\_scope 释放）。
   * [Global Handle](bpta-arkts-leak-in-develop.md#table17319174010236)：napi\_ref 未调用 napi\_delete\_reference 释放或未成对使用（即使用napi\_create\_reference但是未使用napi\_delete\_reference 释放）在这2种情况下，无法基于引用链分析，需要通过Allocation模板，开启Local Handle及Global Handle录制选项来进一步分析。
6. 是否 FrameRoot 持有：若非VMRoot和Local Handle/Global Handle持有，则多为函数不退栈或闭包捕获对象被外部持有。
7. 代码审查：根据引用链中的关键节点（如 EventHub、Timer、全局变量、napi\_ref、闭包上下文）定位代码中的持有关系。
8. 修复与验证：修改代码后重复步骤 1~2，确认内存曲线回归平稳。

标准化排查流程整体流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/wDsVlsikRb2rgX4xTzQxHQ/zh-cn_image_0000002793686492.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=F98A3E9AF8892F0C739099DF53381DAFF31640EA80B9FCADF1C744CF04FDD84A "点击放大")

## ArkTS内存泄漏分析案例

### 案例背景

**现象**：本案例中，通过复现“首页至消息页”的反复进出操作，观察到应用内存占用呈现“阶梯式持续增长”趋势。在循环操作10次后，应用出现显著卡顿现象。

**初步判断**：典型的“阶梯式内存增长”，高度疑似内存泄漏。

### 分析流程

1. **Memory泳道确认泄漏**
   1. 打开 DevEco Studio，连接真机，点击Profiler工具Realtime Monitor（也可使用snapshot模板的Memory录制观察，以下是使用Realtime Monitor观察）。
   2. 启动应用，选择设备与应用进程。
   3. 点击录制按钮，在设备上重复操作：进入消息页面 → 停留2秒 → 返回首页，重复多次。
   4. 观察内存曲线：
      * **正常预期**：每次退出后内存回落至基线附近，整体呈锯齿状。
      * **实际现象**：曲线呈阶梯状上升，多次操作后内存增长至314.1MB且无明显回落，存在内存泄漏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/UIgi-heZTKuk3Cb8S8XQ5A/zh-cn_image_0000002793526516.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A81AF7CD554BF55A92ED5BF0F4FEE4375B6CD6956A1CDA003EF652D4928019B "点击放大")
2. **堆快照对比定位异常对象**

   在 Profiler 中切换到Snapshot模板，请参考[Snapshot模板基本操作](../harmonyos-guides/ide-snapshot-basic-operations.md)：选择Profiler工具 → 选择设备与应用进程 → 选择Snapshot模板 → 创建Session → 启动录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/SkA7NgCDQ5uV7whCqbT1WQ/zh-cn_image_0000002822486397.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=82BCFB9FECA811C680A8F2E89467CA4C151B6A021C03FD1CA9905D5860D6C152 "点击放大")

   抓取快照1：首次在进入消息页前，点击“Take Heap Snapshot”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/OfP67SMYTeWQ06j0fa3_0A/zh-cn_image_0000002793526518.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=F42C39BCF72F8EB46E730C5F7A5A1BD04A6648BF562A6D718262D8EB291DA1FF "点击放大")

   抓取快照2：重复进出消息页面7次后，回到首页，点击“Take Heap Snapshot”，再抓取第二次快照，并停止录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/DAyUxBtSTdSR5o9TX1_tBQ/zh-cn_image_0000002822366419.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=C172C5C22FA9832B29FBD6D8A1C14083949E3DF1A0BC241E34D13455D0FC4700 "点击放大")

   在快照对比视图Comparison中，选择CompareTo Snapshot1。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/ymMaZC6jQw2fhoIGFZUWpA/zh-cn_image_0000002793526520.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2BA044B33D6FC10E1A00096478E100B83394AC8C16E79D1F2C925F4A6381C7E "点击放大")

   查看对象新增销毁情况，优先关注：

   操作次数的整数倍或整数倍+1（因为export出的对象本身也有一条引用链），业务对象，即Constructor的结构为包名/模块名/文件路径#泄漏对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/GBoWwmmtR4-sSPTmZoMajQ/zh-cn_image_0000002822366421.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=535071A9D96E59E34885D639486C96203B59F61D5E87080AD359B83CFA6E7DB6 "点击放大")

   关键发现：

   * 对比结果中，Test对象实例数量从0个增加到8个，Test对象实例泄漏。
   * 正常情况下，页面退出后组件实例应被回收，快照2中应只有1个Test 对象（被export持有）。
3. **追踪引用链**

   在快照对比视图中，展开并选中一个Test对象实例，优先选Distance数量较多的，此处我们选“6”的，并打开右侧详细信息面板。

   注：选择Distance数量较多的对象实例，主要是因为这些实例频繁地被创建且未能得到及时释放。这表明存在潜在的内存泄漏问题，需要进一步调查以确定具体的泄漏源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FfK14Es-TU6t-0czlAjoRw/zh-cn_image_0000002793686494.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7ACBF64554F8FE1AB5A607CDF79374A6EC47B24B43473B5584D29CCA8AC480C "点击放大")

   点击“Shortest Paths”获得如下Test对象实例的最短引用链：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/8kc-6u5xTACpt-wnERxieA/zh-cn_image_0000002822366471.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=28B8F29F115A55D7DC92F58483A35D24483F8C2ADE04031F99F0A33419AEAD36 "点击放大")
4. **分析****VMRoot类型持有导致泄漏问题**

   1. 根据步骤3得到的Test对象实例的最短引用链分析，该引用链的GC Root为SourceTextModule符合被export模块导出对象持有，[VMRoot](bpta-arkts-leak-in-develop.md#table17319174010236)泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/WI3jqhzqQoSfCiQumjxLXw/zh-cn_image_0000002822486447.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C697631F24EFC50357498D4E218B115E75F456AB5D785508547EA681D810FA9 "点击放大")

   2. 从GC Root向上排查引用链，找到第一个业务对象，即CacheTest.ts文件中的CacheTest对象的cache属性持有了Test对象未释放。点击后面跳转图标，打开CacheTest对象实例详细面板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/dDR1eKEFTbexrCxfYOaLGA/zh-cn_image_0000002793686544.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=00CFFE72049E72B00F114684DE3B935CEFE8DB13FF24E014154F56DD021818F7 "点击放大")

   3. CacheTest对象实例面板中，点击对象名后跳转按钮，跳转对应代码行。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/5ursnjG6RbKtIvhrM6vWgw/zh-cn_image_0000002822366473.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A032CAB7EB5BCD73536B004938EAFE0567ADF7FA379339D8BF3DBDD3FF2529C "点击放大")

   4. 跳转代码后分析，CacheTest对象存在静态属性cache，该静态属性中保存了Test对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/IwzIXGAVQoOq_baDuevZBw/zh-cn_image_0000002822486449.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEE8EC198EAE047E6A470F3C5AB3647188D0584BB165D2FA755A721B2E53AE36 "点击放大")

   5. 结合业务代码分析，MessageCenterPage组件创建时会保存一个Test对象到CacheTest中，但组件销毁时未清理该缓存导致内存泄漏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/gSTY_C5fTv2QRHBWjcKpug/zh-cn_image_0000002793686546.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1F87E4D912EC2C295DED1B14B62EA0112239E77734DDE68C193DF3E8DED568B "点击放大")

   6. 修改代码，在页面销毁时清除缓存。修改后重新复现操作7次，并抓快照验证，Test对象创建数量正常。但分析发现Proxy对象数量异常，创建70个未销毁。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/usP0oo16RtOCO9C7to9O8A/zh-cn_image_0000002793526570.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=001320353C7FCD4E62BA6956C80029304726FC4B8BA4AF2BF032004082EEC768 "点击放大")

   7. 参考“步骤3：追踪引用链”，找到最短引用链，发现该Proxy对象的Distance为1。说明其为GC Root直接持有的对象，被Native侧直接持有未释放，即JS对象被Local Handle/Global Handle引用导致内存泄漏。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/7SXxjg9BSmCDBXgNl9Ejuw/zh-cn_image_0000002793526572.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE157BCFA7A29511DDD98BD4F0B79C176A92F8A312D20C6D51AD20157D95568B "点击放大")

   8. 通过Proxy对象的Distance为1的References，确认内存泄漏是由JS对象被Global Handle引用导致的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/g2A3bCOeTjSzEAL_alxeXQ/zh-cn_image_0000002822486451.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F2C73576A012269489814F8AF92AC0CD1C010A6342D67551FFA06C9CC5E5C27 "点击放大")
5. 分析Local Handle/Global Handle类型持有导致泄漏问题

   基于步骤4分析，Proxy对象实例可能被[Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)/[Global Handle](bpta-arkts-leak-in-develop.md#table17319174010236)引用导致内存泄漏，可通过以下步骤继续分析定位：

   1. 配置Allocation录制模板并捕获数据

   * 打开DevEco Studio：确保你的工程已加载，并连接了目标设备或模拟器。
   * 进入Profiler模块：在主界面下方菜单栏，找到并点击Profiler选项卡。
   * 选择应用进程：运行应用，并在“区域2”选择目标设备和应用进程。
   * 创建Allocation录制模板：选择“Allocation”并点击Create Session创建录制模板。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/96aG2_lXSnif4CIgBSPcGg/zh-cn_image_0000002822366475.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=C743DEFE47C1C1CE52C31D408173611CD4EA020098A310B151A75AD34EB2857C)
   * 配置录制参数
     + 配置模式：选择详情模式（即关闭Statistics Mode）。当前仅详情模式支持进行ArkTS和Native的关联分析。
     + 配置开关：勾选“Local Handle”和“Global Handle”，这是关键配置。这将使Allocation专门捕获与JS-NAPI句柄相关的内存分配事件。如果底层镜像不支持该功能，则会提示“当前镜像版本不支持，请升级镜像”。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/jHyWEPIqQnmXV9I8I7bQ6A/zh-cn_image_0000002793526574.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=D095DFDD75880D45D5C40BC6E7BD332F3C6D3EBA3A53B2D9C9F408EFF8AE03B5 "点击放大")
     + 配置泳道范围：勾选ArkTS Snapshot泳道。这将使Allocation在录制结尾时自动抓取一份Snapshot快照用于关联分析。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Anc9PwS3RAqlo2CqSIBMqQ/zh-cn_image_0000002793686548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BFE656D5E44474671CF6BA647729767A3FE8FF090FB87B75FAFCA63D8383513 "点击放大")
   * 启动录制：勾选了[Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)开关后，如果是在应用本生命周期内首次录制local handle数据，会触发弹窗请求重启应用以便录制对应信息，此时点击OK允许重启即可。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/PAkprkPXQZSupLDHei2ztQ/zh-cn_image_0000002793526576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8D94DD838BA3951D5BBF0E2B30A6473C7375C2E2D98309AB7E800AB3BD31562 "点击放大")
   * 运行应用程序：运行目标应用，执行相关被怀疑引入内存泄漏的业务操作，持续一段时间以增加内存压力和捕获更多数据。
   * 停止录制：自动触发抓取一份Snapshot快照用于关联分析。点击快照，查找到疑似泄漏对象Proxy 。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/pcfCq9A7QEmil3_JVN-O3A/zh-cn_image_0000002793686550.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=82D07FBEB3BB5954862170D48C0CA00C60430E87126F081BD403D210BF49AE63 "点击放大")

   2. 配置Allocation录制模板并捕获数据

   * 定位可疑ArkTS对象：选中一个怀疑被泄漏的ArkTS对象实例（或对象类型），查看扩展标签页。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/xSUrDKu3SciH9p-JoNv-Bw/zh-cn_image_0000002822486453.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=D44AB9400F90902CD1256BF8E3208F20BA5B2F424223A7E490706A3DA1B3724B "点击放大")
   * 查看Native List：若某个ArkTS对象的distance值为1，则可以通过扩展标签页中的Native List标签页，查看所有当前与该JS对象关联的Native句柄引用，以确认该JS对象是被Local Handle或Global Handle引用的对象。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/CXfM4EOFTV6xZwUUKu3r1Q/zh-cn_image_0000002822486455.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=F413BA30B73222ADE40204AEDC1CDA5FE24A1FAD47CF1DC357FD37BE9D258722 "点击放大")
   * 关键信息：
     1. 句柄类型：调用栈底层的符号ArkGlobalHandle或ArkLocalHandle判断泄漏类型。
     2. 调用栈：通过调用栈，可以定位到应用的Native代码（可能是ArkUI框架代码或你自己代码）中创建napi\_ref的地方。
     3. 注意点：
        + 如果该JS对象节点不是一个被[Local Handle](bpta-arkts-leak-in-develop.md#table17319174010236)或者[Global Handle](bpta-arkts-leak-in-develop.md#table17319174010236)引用的对象，则会提示“No Detail”。
        + 如果该JS对象被Local Handle或Global Handle引用，但对应的native内存申请事件在此次录制前已完成分配，则本次录制结果无法展示该内存申请的调用栈，需重新录制。重新录制时，需将业务逻辑范围尽量提前。

   3. 分析内存分配调用栈

   * 排查调用栈：“Native List”标签页中的调用栈，找到对应业务代码。
   * 关键排查点：
     1. 检查是否在适当的时候调用了对应的句柄释放接口如napi\_delete\_reference等。
     2. 梳理这段Native代码需要引用ArkTS对象的合理性，识别这个引用的生命周期是否过长，是否应该在某个条件满足后被释放。
     3. 对于napi\_ref，其引用计数是关键。确保在不再需要引用时正确调用了napi\_delete\_reference。注意，引用计数可能因其他代码路径的创建或删除操作而意外增减。
     4. 检查libuv异步调用等场景中，句柄作用域是否正确添加Handle Scope。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/JDrURYG-T3azye8IEmu02g/zh-cn_image_0000002822366477.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=36B513306D582825D4938E601DB9AE91F34A2B868F1FBDEF96238B417EFFFE7D "点击放大")

### 优化修复

1. 重新运行应用，再次使用Memory泳道监控。
2. 重复多次进出消息中心页。
3. 验证结果：
   * 内存曲线恢复锯齿状，每次退出后回落至基线。
   * 再次抓取快照对比，多次操作后业务对象实例数量无明显增长。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/zNJdVT5uRjiyH3w4wbOSoA/zh-cn_image_0000002822366479.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0A81ECC548486D4587E515CAD9FCFCC9D042933F9ECF35413C65D1C009966EC "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BgnxAjzISvqBlm6V2aU5lQ/zh-cn_image_0000002793686552.png?HW-CC-KV=V1&HW-CC-Date=20261124T044757Z&HW-CC-Expire=31536000000&HW-CC-Sign=A35542EB27E046AFF69431598A4E7CB692783740370800EFA286C368A0C4B643 "点击放大")

### 术语介绍

| 术语 | 解释 |
| --- | --- |
| **GC Root** | GC Root（Garbage Collection Root**，**垃圾回收引用链根节点） 是垃圾回收器进行可达性分析的起点。从GC Root能访问到的节点对象是“存活的”，否则会被回收。 |
| **引用链** | 在ArkTS中，“引用链”就是从某个GC Root（如VMRoot、FrameRoot等）出发，经过一连串的对象引用，最终到达目标对象的路径。  如果这个路径存在，则该对象是“存活”的，不会被GC回收；  如果从任何GC Root都无法找到一条到达该对象的引用链，该对象就是“不可达”的，会被标记为垃圾对象并回收。 |
| **VMRoot** | VMRoot是ArkTS虚拟机层面的根引用集合，代表GC遍历的起点。 |
| **FrameRoot** | FrameRoot是函数调用栈帧在GC遍历过程中的根节点。当函数被调用时，其局部变量和入参对象会被当前栈帧引用，从而成为GC的“可达”起点。 |
| **Local Handle** | Local Handle（本地句柄）是一种短期引用，用于在本地作用域（如函数调用栈）内持有对象，防止对象被垃圾回收。当作用域结束时，这些句柄会自动释放。 |
| **Global Handle** | Global Handle（全局句柄）例如napi\_ref，用于长期持有对象引用，确保在对象生命周期内不会被垃圾回收机制回收。使用此类句柄时，开发者需要手动管理其生命周期，包括创建和销毁，以避免潜在的内存泄漏问题。 |
