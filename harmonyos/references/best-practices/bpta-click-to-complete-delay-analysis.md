---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-complete-delay-analysis
title: 点击完成时延分析
breadcrumb: 最佳实践 > 性能 > 性能分析 > 点击完成时延分析
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:658b72f94c0ef6965af8304d67b68b21c0c9d54cf8ffb4435a3f552d3c283320
---

## 完成时延优化概述

在移动终端应用开发中，完成时延指用户从输入触控指令到界面完全刷新结束并达到可以阅读的稳定状态所用时间。点击完成时延分为页面内跳转和页面间跳转两种类型。完成时延在用户体验设计中至关重要，直接影响用户对产品的满意度和使用体验。完成时延反映了用户对响应速度的整体感受，影响触控交互的及时性和愉悦性。如图一所示，点击完成时延包含点击响应时延。有关响应时延阶段的优化分析，请参考[点击响应时延分析](bpta-click-to-click-response-optimization.md)。

应用性能体验建议中针对时延建议[应用或元服务应用内点击操作完成快](../harmonyos-guides/performance-delay.md#section2406192820717)（应用完成时延≤900ms，元服务≤1400ms），针对转场建议[应用或元服务应用内转场操作流畅](../harmonyos-guides/performance-frame-rate.md#section1591383182619)（卡顿率为0ms/s），当前AppAnalyzer工具已支持（或等效支持）上述指标项。

在一定时延水平以上，完成时延越短越好，但在达到一定阈值后，用户的流畅体验不会继续提升。本文将介绍相关分析工具、点击完成时延问题定位流程及常见问题根因分析。

**图1** 点击完成起止点示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/9l9ncCbES7WBw5ywRMROvg/zh-cn_image_0000002229450665.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D3479932207CC05AFF594F31CACEB34594D2E56197E8B88C3C82A19B4450BAC "点击放大")

**图2** 页面转场过程解析  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/0wTbcXKlQ0yPZQO4ytRFTA/zh-cn_image_0000002420747058.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D047B0CABB24C324FAD82D65F4C7A88DA86D96AFCC41B23A2191D3B2FF5559D "点击放大")

## 完成时延检测工具

影响点击完成性能的因素很多，使用DevEco Studio集成的分析工具，可以收集系统数据，自动执行重复任务，建立统一优化标准和流程，减少个人差异和误操作的可能性，帮助开发者了解性能瓶颈和优化潜力。分析优化过程中，可能用到以下工具中的一个或多个。

* AppAnalyzer：是DevEco Studio提供的检测评分工具，用于测试和诊断HarmonyOS应用或元服务的质量，快速提供诊断结果和改进建议。当前支持的测试类型包括兼容性、性能、UX测试和最佳实践。点击完成时延是性能测试中的一项检测规则，开发者可以使用该工具检测响应性能。

  具体使用可参考[AppAnalyzer](bpta-performance-detection.md#section135451444171)。
* ArkUI Inspector：是DevEco Studio中提供用于检查UI的工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。

  具体使用可参考[ArkUI Inspector](bpta-optimization-overview.md#section1465143164111)。
* DevEco Testing：DevEco Testing是一款专项集成测试工具，提供了多项测试能力。旨在帮助开发者高效完成应用的功能、兼容性、性能和稳定性测试，确保应用质量。

  具体使用可参考[Testing测试报告导入体检工具分析](bpta-performance-detection.md#section3783182023119)。
* Profiler Frame：性能调优深入分析工具，支持冷启动、卡顿丢帧、状态变量、并行化、网络耗时、ArkWeb、内存优化等场景化调优能力。其中Frame分析可以帮助开发者深度分析性能问题，通过录制应用运行过程中的关键数据，从而识别卡顿丢帧、耗时长等问题的原因所在。

  具体使用可参考[DevEco Profiler](bpta-optimization-overview.md#section2012922312284)。

## 问题定位流程

定位点击完成时延高耗时的简易流程如下图所示。

**图3** 问题定位流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/rCJae7b3RXG0CjX75vf2cA/zh-cn_image_0000002455895496.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D52AD8609657B66CF1A512E4C2BAFC661CA08CEF10A71B1CD0D8802F6F045DD "点击放大")

如上图所示，分析点击完成时延问题通常需要以下步骤：

1. 性能体检：使用性能检测工具AppAnalyzer检测和诊断应用是否存在性能问题。
2. 确定完成时延：根据性能检测工具AppAnalyzer检测结果，确定完成时延的耗时，判断是否符合[时延](../harmonyos-guides/performance-delay.md)体验建议中的规范。
3. 抓取Trace信息：使用性能分析工具DevEco Profiler抓取Trace，并确定Trace图中的起止点。
4. 分析问题：结合关键泳道Trace信息以及ArkUI Inspector布局分析工具来定位具体问题。

## 使用AppAnalyzer工具检测和分析

在应用开发中，UI线程应用自身方法执行耗时、网络请求响应耗时、UI组件自身创建耗时等，都会导致应用点击完成时延受到影响，合理优化代码逻辑可以提升应用点击完成时延速度，提升用户体验。开发者可以通过AppAnalyzer对应用点击完成时延进行检测，并优化检测报告中存在的点击完成时延未达标的问题。

使用AppAnalyzer工具检测点击完成时延步骤如下。

1. 在DevEco Studio中启动AppAnalyzer工具，详细参见[AppAnalyzer](bpta-performance-detection.md#section135451444171)。
2. 点击“手动性能页面间转场体检”按钮启动检测。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/w8ENGGvfQzuOikxYWhz7VA/zh-cn_image_0000002480207908.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=9360D500A6916C0CF3F69C208A8CA20C10785EBC8CC45C8DE386AB2905C28ADF "点击放大")
3. 开发者需根据提示，在应用中找到待检测页面，点击工具中的开始按钮，然后在应用中手动执行转场，操作后点击停止完成本次检测。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/wYAwbUpFSta-J1e-glp82Q/zh-cn_image_0000002482580170.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=34ACD39C5BFD6496EE19715B81CDD01FEC49FAEBD0006A1D48DC27A3F89E25DD "点击放大")
4. 检测结果分析，点击完成时延应小于或等于900ms。如果存在大于900ms的点击完成时延，判断为存在性能问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/LSw04Jx9TlieVf_-TUNR9g/zh-cn_image_0000002512327777.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C61727DF7F1CCD29801748DF1BCB33F7474D5EB464496C1E8BFCAEC8E6D2AC5)

检测出的点击完成时延报告中，可能会存在以下五种影响性能的故障原因。

* UI线程应用自身方法耗时长
* UI线程应用自定义组件创建耗时长
* 网络请求耗时长
* 主线程长时间被阻塞
* 图片大纹理

### UI线程应用自身方法耗时长

1. 获得检测结果后，点击详情报告中的“点击完成时延”，可以查看UI线程应用自身方法耗时长的检测结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/bDY4joc8QMSoWRBm0ic-0w/zh-cn_image_0000002480480340.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=F88AE3220CF572029B89188286809750E968AE68DD1C1EB25CD8078AC0955B9E "点击放大")

   检测结果中，可以根据方法总耗时的大小来判断该方法是否为耗时方法。如上图中，aboutToAppear[PageJumpSceneUseCase3.ets, 29]表示PageJumpSceneUseCase3.ets页面中的aboutToAppear()方法，其执行耗时较长。
2. 点击方法名，可跳转定位至PageJumpSceneUseCase3.ets页面中的耗时方法处。
3. aboutToAppear()中调用了如下方法。

   ```screen
   export function fun1() {
     for (let index = 0; index < 906666; index++) {
       console.debug('fun1 index:' + index);
     }
   }
   ```

   由于在该方法中执行了模拟长耗时的for循环代码，导致该方法在检测中总耗时过长。
4. 点击优化建议下的跳转链接[第2步：丢帧问题分析](bpta-zhenlv.md#section117831333645)，即可获取相应的优化建议。

### UI线程应用自定义组件创建耗时长

1. 获得检测结果。点击详情报告中的“点击完成时延”，可以查看UI线程应用自定义组件创建耗时检测结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/MqeCPbHCTgei88iz_8mMMw/zh-cn_image_0000002512328271.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B947F75812EA68EF96EDB5F5BBD384E282F2D7A73460B958AA5E84B834E31E6F "点击放大")

   检测结果中，可以根据总耗时列来判断自定义组件创建是否耗时。上图中，TestResponseLatency组件创建总耗时40.933ms，耗时过长。如下图，TextItem在页面中自定义组件被创建多次，导致创建耗时过长。

   ```screen
   @Entry
   @Component
   struct TestResponseLatency {
     @State arr:string[] = []

     aboutToAppear(): void {
       this.arr.push(...GetData());
     }

     build() {
       Flex() {
         Column() {
           Flex() {
             ForEach(this.arr, (item: string, index: number) => {
               TextItem2({ item: item, index: index })
             })
           }
         }
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 点击源文件定位到创建耗时的UI组件，根据提供的可能故障原因，对UI组件进行相应的优化，还可参考静态检测结果中的优化建议，来对组件创建耗时进行优化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/1T_UnZ58QEaJco7MFi2KVA/zh-cn_image_0000002512368293.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2DE0C3399FAAA1DF54235D811D3A4B4854F70CB677706B87C0DB0AA193ED6FF "点击放大")

### 网络请求耗时长

1. 获得检测结果后，点击详情报告中的“点击完成时延”，可以查看网络请求耗时的检测结果。
2. 根据检测结果中的请求耗时和点击离手到请求发起间隔可进行如下判断。
   * 网络请求本身耗时长

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/oJgLB4FnSp6CUdJPxXyJjQ/zh-cn_image_0000002480208772.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C9CDED169DD76D12B8F612088313D6CF0FFBB1A76BAF7B26C25438E0375016D "点击放大")

     网络请求本身是否耗时可通过检测结果中的请求耗时时长来进行判断，时间越长，则网络请求本身耗时越久。详细分析请参考：[网络诊断：Network分析](../harmonyos-guides/ide-profiler-network.md)。

     网络请求本身耗时长，可对该URL请求进行预连接和预解析来优化网络传输速度，提前完成DNS查询和TCP/TLS握手，即在应用启动或空闲时提前建立并维护一个持久的连接池；还可以使用CDN来优化网络传输速度，将静态资源部署到CDN上。
   * 网络请求发起太晚

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/BZJoHdM4Tji4E9H7GHB9Hw/zh-cn_image_0000002512368655.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=537D1567E7E0B2BB7BE2E488BDD6CA6FF7CEBAE413599B709C14EF4009F0279E "点击放大")

     点击离手到请求发起间隔则表示用户进行点击操作后，到真正向服务器发起网络请求的那一刻止，这中间所经过的时间。可通过检测结果中的点击离手到请求发起间隔时长来进行判断，时间越长，则表示网络请求发起的越晚。可通过提前发起网络请求，来进行优化。可参考：[网络请求提前发送](bpta-application-cold-start-optimization.md#section199911250658)。

如果开发者既无法优化网络请求本身耗时，也无法将网络请求提前发起，可以考虑提前将网络请求数据缓存，下次发起请求的时候直接加载缓存数据，再通过发送网络请求二刷刷新数据。

### 主线程长时间被阻塞

1. 获得检测结果。点击详情报告中的“阻塞主线程的任务”，可以查看主线程长时间被阻塞的检测结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/FgrENC8BTuyv5GfdS9qsVA/zh-cn_image_0000002512328837.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FD97AD3FF62847DECE57FC000EEB564E943A6DAFF8B8D3D0C1D9F1F4C1E840A "点击放大")

   通过关键线程识别技术，体检工具能够基于唤醒关系算法精确构建线程间依赖链路，同时结合传统调度分析方法，全面检测可能阻塞主线程的子线程任务。检测结果中，可以根据实际空闲时间判断主线程是否长时间被阻塞：空闲时间越长，则阻塞时间可能越久。通过识别并定位阻塞主线程的关键任务，可以快速找到对应的耗时代码位置。任务耗时代表诊断出的阻塞主线程任务本身的执行时长；主线程等待耗时表示任务结束点到主线程上一个 Running 结束点之间的时间，用于衡量该耗时任务对主线程造成的阻塞程度。
2. 可能存在以下5种诊断结果。
   * 子线程中耗时函数执行

     点击子线程中函数执行链接，跳转至子线程中耗时函数执行的源码，可发现主线程中的UI刷新需要等待子线程任务执行完成。

     ```screen
     const task = new taskpool.Task(blockFunc, 1350);
     taskpool.execute(task).then(() => {
       this.isShow = true;
       hiTraceMeter.finishTrace('loadSyncTask', 902);
       this.cost = new Date().getTime() - this.timestamps;
     }).catch((err: BusinessError) => {
       console.error(`Failed to execute. Code: ${err.code}, message: ${err.message}`);
     })
     ```

     应避免子线程执行的函数阻塞主线程，优化建议可参考解决指导中分析高耗时函数的内容。
   * 网络请求耗时过长

     可参考**网络请求耗时长**中的优化建议。
   * 系统接口请求耗时长

     点击系统接口链接，跳转至系统接口请求耗时长的代码部分。比如获取位置信息接口中，页面上位置信息刷新依赖于接口的返回结果。当系统接口响应较慢时，会导致主线程阻塞。

     ```screen
     getCurrentLocationInfo() {
       hiTraceMeter.startTrace('Napi', 1001);
       const requestInfo: geoLocationManager.LocationRequest = {
         "priority": geoLocationManager.LocationRequestPriority.FIRST_FIX,
         'scenario': geoLocationManager.LocationRequestScenario.UNSET,
         'timeInterval': 1,
         'distanceInterval': 0,
         'maxAccuracy': 0
       };
       try {
         geoLocationManager.getCurrentLocation(requestInfo)
           .then((location: geoLocationManager.Location) => {
             this.loadMsg = JSON.stringify(location);
             this.isShow = true;
             promptAction.showToast({ message: JSON.stringify(location) });
             hiTraceMeter.finishTrace('Napi', 1001);
           })
           .catch((err: BusinessError<ESObject>) => {
             console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
           });
       } catch (err) {
         console.error(`Failed to get current location. Code is ${err.code}, message is ${err.message}`);
       }
     }
     ```

     应避免系统接口串行发起请求，优化建议可参考解决指导中并发能力增强的内容。
   * 主线程在等待setTimeout

     点击主线程在等待setTimeout链接，跳转至setTimeout函数代码，可发现主线程中的UI刷新需要等待setTimeout执行完成。

     ```screen
     setTimeout(() => {
       this.isShowFirst = true;
       hiTraceMeter.finishTrace('setTimeout', 903);
     }, 500);
     ```

     应避免在主线程中使用setTimeout函数等待时间过长，或是减小setTimeout的延时时间。
   * [存在大量等待时间无法诊断](bpta-click-to-complete-delay-analysis.md#section1563932810516)
3. 可参考优化建议中的文章，来对主线程长时间被阻塞导致完成时延不达标的问题进行优化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/KG8J80x6Q52xhWrg4CBcSw/zh-cn_image_0000002480368946.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FAD98634EE242BE363469E0F6A29092E80AF3AADE97442EB1E5AB39586C9533)

### 图片大纹理

1. 获得检测结果。点击详情报告中的“点击完成时延”，可以查看图片大纹理的检测结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Q4_9I1qSQd-bnBWr158Trg/zh-cn_image_0000002512368913.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=0720B75E328371141FD6B6BA9400B63F0C57542D17022D04CF0FD7E26F7DC48F "点击放大")

   检测结果中，可以根据超出尺寸占比来判断是否需要优化。
2. 可通过图片组件所在源码文件进行定位，找到包含图片的源码文件。检测结果可以看出，源图尺寸与目标尺寸不同，超出尺寸占比较大。建议源图尺寸不要超过目标尺寸大小的10%。
3. 不同图片种类会有不同的优化建议，可根据优化建议进行相应的修改。

## 使用Profiler进行完成时延关键Trace分析

通过关键泳道可以分析关键Trace，它通过对Trace进行逻辑分组，可以快速聚焦关键问题。

### 关键泳道简介

关键泳道可从函数调用耗时、转场页面绘制耗时和转场动画时延三个角度进行分析。接下来，将依据这三个角度对关键泳道进行详细介绍。

* 函数调用耗时分析：

  ArkTS Callstack：提供ArkTS侧的方法调用栈信息，用于分析ArkTS代码执行和性能瓶颈；

  Callstack：提供Native侧的方法调用栈信息，用于分析Native层面性能问题；
* 转场页面绘制耗时分析：

  Frame：提供应用主线程的帧渲染信息，帮助识别未按时渲染的帧及其原因；

  ArkUI Component：提供ArkUI组件的创建、布局、渲染等详细信息，帮助识别耗时较长的组件；
* 转场动画时延分析：

  H:Animator：提供动画执行过程中的详细信息，帮助识别转场动画是否耗时较长；

  关键Trace说明如下

  | 序号 | 泳道 | Trace点 | 描述 |
  | --- | --- | --- | --- |
  | 1 | 应用线程 | ReceiveVsync | 接收Vsync信号 |
  | 2 | 应用线程 | OnvsyncEvent | 收到Vsync信号，渲染流程开始 |
  | 3 | 应用线程 | FlushVsync | 刷新视图同步事件，包括记录帧信息、刷新任务、绘制上下文、处理用户输入 |
  | 4 | 应用线程 | FlushDirtyNodeUpdate | 标脏组件刷新。页面刷新渲染的时候要尽量减少刷新的组件数量。当状态变量改变后，会先对状态变量相关的组件进行标脏，然后对这些组件重新测量和布局，最后再进行渲染 |
  | 5 | 应用线程 | JSAnimation | 显示动画，动画会影响组件加载完成时延 |
  | 6 | 应用线程 | FlushLayoutTask | 执行布局任务。在此阶段会对组件做布局测算，如果层级较深或者组件较多会影响性能 |
  | 7 | 应用线程 | FlushMessages | 发送消息通知图形侧进行渲染 |
  | 8 | 应用线程 | aboutToBeDeleted | 自定义组件生命周期函数，组件析构时出现，在未使用复用机制时，FlushDirtyNodeUpdate和LazyForEach predict下会析构组件，导致刷新时组件重复创建 |
  | 9 | 应用进程 | SendCommands | 应用UI提交到Render Service |
  | 10 | ArkTS Callstack | createHttp | 创建网络请求 |
  | 11 | ArkTS Callstack | request | 发送网络请求 |
  | 12 | ArkTS Callstack | parse | 解析数据 |
  | 13 | ArkTS Callstack | off | 取消订阅 |

### 确定起止点

开发者可以使用录屏辅助测试，通过录屏分析工具确定点击完成时延的起止点，从而判断是否存在需要优化的时延问题。

DevEco Profiler工具分使用方式可以参考[Frame分析](../harmonyos-guides/ide-insight-session-frame.md)。下面介绍如何使用DevEco Profiler工具确定点击完成时延Trace的起止点。

1. 搜索"H:DispatchTouchEvent"标签，找到type=1的那个DispatchTouchEvent，就是点击离手起点，将该时间戳设为起点。

   **图4** 确认Trace起点  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/TO3qfjEuRA2kvvz3iCo8cg/zh-cn_image_0000002456058024.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C541B724A0F513BF6497D52167DE271D550B5D82C1C354C7F1D9EB3D3EDC20D "点击放大")
2. 点击操作完成时延的终点位置在泳道图中没有明确的Trace点，需要通过录屏工具计算出完成时延的耗时时间。从起点往后拉相同的时间找到终点位置。

   **图5** 确认Trace终点  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/_Z3Z_lv0RH2PkYi7dJVz1g/zh-cn_image_0000002489137641.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABD8FD0B71E01CAB2A5D1572FE16E3F026AE0354DA4BE77B0EF53404B02ADB92 "点击放大")
3. 使用Profiler工具标记Trace起点与终点。

### ArkTS Callstack泳道分析ArkTS侧耗时函数

在ArkTS Callstack子泳道中，ArkVM是需要优先查看耗时情况的泳道，可以观察ArkTS侧方法的耗时。优先分析耗时最长的调用栈（program除外，program表示程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或Native调用ArkTS的情况，需要切换到Callstack泳道查看具体的调用栈信息，通常难以通过这里分析出有效信息）。逐级展开，可以看到具体耗时的文件。基于 [“HMOS世界”](https://gitcode.com/harmonyos_samples/hmosworld)切换tab页场景，抓取Trace信息。

**图6** ArkTS Callstack泳道图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/XbS_b6N2TTW-8Brc9S4k8g/zh-cn_image_0000002455898360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F342B19859EC0F0F7CC8A2667340333444E5D3F2F11663419A801CAE7DB5A61 "点击放大")

观察发现MainPage文件中匿名函数耗时350ms，展开该节点。

**图7** ArkTS Callstack泳道耗时函数详情  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Hs8cwVcHRNykggg2IKTkIg/zh-cn_image_0000002489177673.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D90B9F1E12D44A1FC46059D8B79FE69DBD6D26E9B4ED653102781298FC8CC92 "点击放大")

展开节点后发现函数调用链中AudioPlayerService中getInstance函数调用耗时327ms，接下来定位源代码。

```screen
// products\phone\src\main\ets\pages\MainPage.ets
Tabs({ index: this.currentIndex }) {
  // ...
}
.layoutWeight(1)
.scrollable(false)
.onChange((index) => {
  this.currentIndex = index;
  ContinueModel.getInstance().data.mainTabIndex = index;
  if (AppStorage.get('audioPlayerStatus') !== AudioPlayerStatus.IDLE) {
    AudioPlayerService.getInstance().stop().then(() => {
      AudioPlayerService.destroy();
    }).catch((err: BusinessError) => {
      hilog.error(0x000, 'testTag', `stop failed. Code: ${err.code}, message: ${err.message}`);
    })
  }
})
```

AudioPlayerService.ets相关代码如下

```screen
// commons\audioplayer\src\main\ets\service\AudioPlayerService.ets
export class AudioPlayerService {
  private static instance: AudioPlayerService | null = null;
  // ...
  public static getInstance(): AudioPlayerService {
    if (!AudioPlayerService.instance) {
      AudioPlayerService.instance = new AudioPlayerService();
    }
    return AudioPlayerService.instance;
  }
  public static destroy(): void {
    if (AudioPlayerService.isInstanceNotNull()) {
      AudioPlayerService.getInstance().releaseAudioPlayer();
      AudioPlayerService.instance = null;
    }
  }
  // ...
}
```

观察源代码发现AudioPlayerService调用getInstance()创建单例对象耗费大量时间，随即又调用destroy方法销毁对象。优化方式如下：获取单例对象前，先判断单例对象是否被实例化，若没有实例化则直接跳过获取与销毁，避免实例对象的无效创建与销毁，参考如下代码。

```screen
// products\phone\src\main\ets\pages\MainPage.ets
Tabs({ index: this.currentIndex }) {
  // ...
}
.layoutWeight(1)
.scrollable(false)
.onChange((index) => {
  this.currentIndex = index;
  ContinueModel.getInstance().data.mainTabIndex = index;
  if (AppStorage.get('audioPlayerStatus') !== AudioPlayerStatus.IDLE) {
    AudioPlayerService.getInstance().stop().then(() => {
      AudioPlayerService.destroy();
    }).catch((err: BusinessError) => {
      hilog.error(0x000, 'testTag', `stop failed. Code: ${err.code}, message: ${err.message}`);
    })
  }
})
```

优化后AudioPlayerService.ets代码如下：

```typescript
// commons\audioplayer\src\main\ets\service\AudioPlayerService.ets
export class AudioPlayerService {
  private static instance: AudioPlayerService | null = null;
  // ...
  public static getInstance(): AudioPlayerService {
    if (!AudioPlayerService.instance) {
      AudioPlayerService.instance = new AudioPlayerService();
    }
    return AudioPlayerService.instance;
  }
  public static destroy(): void {
    if (AudioPlayerService.isInstanceNotNull()) {
      AudioPlayerService.getInstance().releaseAudioPlayer();
      AudioPlayerService.instance = null;
    }
  }
  public static isInstanceNotNull(): boolean {
    return AudioPlayerService.instance !== null;
  }
  // ...
}
```

### Frame主线程泳道分析异常

查看Frame泳道中的应用主线程子泳道，观察app侧帧数据。如果在这个泳道中出现红色帧，通常表示该帧的渲染时间超过了预期，这可能是一个性能异常的指示。

如下图所示的第145帧

**图8** 超长帧Trace信息  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/t3FZ6yGpSSaxh1AnwNqlmQ/zh-cn_image_0000002489140921.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E535EE0DB0FE6867D8AB780227D3458C8B776DE5F55D9FE007A04AEF6EE42CC "点击放大")

每帧的预期耗时（ms） = 1000ms / 帧率。如上图所示，选中超长帧后，可以看到该帧的预期耗时Expected Duration为 8ms 330μs，说明帧率是 120。实际耗时为 92ms 571μs，远超预期耗时，因此被识别为超长帧。超长帧的长时间渲染会直接影响用户体验，导致点击完成时延不达标。

通过上图发现卡顿期间存在较长的ExecuteJS调用，需要查看具体的调用栈。观察ArkTS Callstack泳道无异常后，接下来查看Callstack泳道的函数栈。

关于首帧渲染的特别说明：页面跳转后，由于需要重新加载和渲染新的UI元素，首帧渲染时间往往较长，可能无法达到目标帧率下的预期耗时。因此，性能分析中首帧出现红色（即超出合理预期时间）是较为常见现象，不一定表示存在严重性能问题。但仍需关注首帧渲染时间，必要时进行优化。

### Callstack泳道分析Native侧耗时函数

Callstack泳道，该泳道显示Native函数调用泳道，也可以看到Native函数调用栈以及各函数的耗时情况，重点关注主线程和有内容的WorkerThread子泳道。

下图展示了超长帧案例中Callstack的主线程子泳道。

**图9** Callstack主线程泳道图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/zid2ne-YQP6vCSBZh1X4sw/zh-cn_image_0000002489180945.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BFBEAFCA1B44754E904FE283CA0CFCBBC2A4F8EB182254EE94E034D643124DA "点击放大")

滑动查看右侧权重最高的函数调用栈，定位到MainPage.ets文件第203行代码为主要耗时原因。

### ArkUI Component泳道分析组件绘制耗时

ArkUI Component泳道记录了自定义组件以及系统组件的绘制次数、耗时等信息，重点关注相对于其他组件耗时比较久的组件。

**图10** ArkUI Component泳道泳道图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Tp_a8oLjRaOJwTWAfmDD7w/zh-cn_image_0000002456061300.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=105C6272DE74892212458404350B5F5D45B368C5EFF4A7A1CADAD00EA8D00CED "点击放大")

然后可以在详情（Details）中使用下图中被框选的按钮过滤目标组件，查看组件在刷新过程中不同阶段的耗时情况。结合函数调用栈和ArkUI Inspector工具，定位目标组件绘制耗时过长的具体原因。

**图11** ArkUI Component泳道图Details信息  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/UtjMwNZtRv6TypPBDxPM1g/zh-cn_image_0000002455901644.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A20B20EEC2144B5AD4481B4F98D9B38CDF03F5D55DDAFE35707B3109564CF42 "点击放大")

### H:Animator泳道分析动画时长

在页面切换过程中，如果存在加载的 loading 动画，出于用户体验考虑，可将动画停止与网络请求的完成相关联。例如，展示“加载中”状态，直到数据加载完成。通过 H:Animator 泳道，可以观察到动画的耗时。

**图12** H:Animator 泳道图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/QgNX9ojjRoul9UbwS8uR8A/zh-cn_image_0000002489140945.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=79FDE8D42C162AFDD18559CE90F236C06F0833D26C15D755D175A8C38B3A8690 "点击放大")

## 完成时延解决方案

### UI线程应用自身方法耗时长影响页面首次加载时延

当UI线程应用自身方法耗时过长时，会影响页面首次加载时延。AppAnalyzer提供了场景化体验检测，能帮助检测出耗时函数，协助开发者快速定位到问题点，并提供相应的优化建议。UI线程应用自身方法耗时长可参考[第2步：丢帧问题分析](bpta-zhenlv.md#section117831333645)中的解决方案进行相应的代码优化。

### 网络请求耗时

在附带网络请求的页面跳转场景中，完成时延较长的绝大多数原因在于网络数据的HTTP请求时间较长。由于网络请求从操作系统侧发起和控制，并且网络环境存在不可控性，因此很难在业务逻辑代码中优化请求速度。因此，提前发起请求就显得尤为重要。通常可以从以下两个方面进行优化：

**避免在异步函数中发起网络请求**

由于ArkTS单线程EventLoop特性，异步调用的执行时机会被延迟到同步逻辑之后。如果将Http请求接口放在异步函数中，网络请求可能会被UI绘制阻塞，等待第一帧UI绘制结束才开始。如果页面首帧较复杂，这会导致网络请求的延迟时间显著增加。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/m1Rm--xZSOieKKp94CQByA/zh-cn_image_0000002194010436.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=868E9B01928885677B4BD3199E0899DFA25FDC53A7F45AD31CADA24FE4E8D597 "点击放大")

**避免在页面子组件中发起网络请求**

由于ArkUI组件的创建基于组件树结构，存在先后顺序。如果在页面的某一子组件中发起网络请求，该请求需要等待前面的组件创建完成。如果前面的组件创建耗时较长，会导致该请求被严重阻塞。

如下图情况，应用页面结构分为Header和Tabs两部分，如果将Tabs内容数据的Http请求放在Tabs组件中发起，由于Tabs组件在UI结构上依赖Header部分，则需要先创建Header，同时又因为Header内容的渲染也依赖网络请求，所以最终导致Tabs的数据请求严重延后。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/4gHXQpBxTJKZeTrOFelwcw/zh-cn_image_0000002193850836.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFE056496F160EA774E51C426810000050047A5BB9EAA728489D2566B463224C "点击放大")

### 动画时延耗时

页面转场动画对提升用户体验至关重要。动画时延过长会显著影响用户的点击完成时延。动画完成时间直接关系到用户何时可以开始与应用交互。动画时延的主要原因是动画时长设置过长。

常见的页面转场动画时长参数有：

1. [Tabs](../harmonyos-references/ts-container-tabs.md)组件设置TabContent切换动画时长，即[animationDuration](../harmonyos-references/ts-container-tabs.md#animationduration)属性。
2. [Swiper](../harmonyos-references/ts-container-swiper.md)组件设置子组件切换动画时长，即[duration](../harmonyos-references/ts-container-swiper.md#duration)属性。
3. [页面间转场 (pageTransition)](../harmonyos-references/ts-page-transition-animation.md)设置转场动画时长，即[PageTransitionOptions对象说明](../harmonyos-references/ts-page-transition-animation.md#pagetransitionoptions对象说明)中的duration字段。

使用Tabs组件进行页面切换时，当不设置BottomTabBarStyle时默认[animationDuration](../harmonyos-references/ts-container-tabs.md#animationduration)属性有300ms的动画时长，当该属性值设置过长时会导致完成时延变大。接下来将该属性值分别设置为100ms与1000ms来探究animationDuration属性对完成时延的影响。

实验一：设置animationDuration为100ms

```typescript
@Entry
@Component
struct TabsPositiveExample {
  @State currentIndex: number = 0;
  private controller: TabsController = new TabsController();
  private list: string[] = ['green', 'blue', 'yellow', 'pink'];

  @Builder
  customContent(color: Color) {
    Column()
      .width('100%')
      .height('100%')
      .backgroundColor(color)
  }

  build() {
    Column() {
      Row({ space: 10 }) {
        ForEach(this.list, (item: string, index: number) => {
          Text(item)
            .textAlign(TextAlign.Center)
            .fontSize(16)
            .height(32)
            .layoutWeight(1)
            .fontColor(this.currentIndex === index ? Color.White : Color.Black)
            .backgroundColor(this.currentIndex === index ? Color.Blue : '#f2f2f2')
            .borderRadius(16)
            .onClick(() => {
              this.currentIndex = index;
              this.controller.changeIndex(index);
            })
        }, (item: string, index: number) => JSON.stringify(item) + index)
      }
      .margin(10)
      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        TabContent() {
          this.customContent(Color.Green)
        }
        TabContent() {
          this.customContent(Color.Blue)
        }
        TabContent() {
          this.customContent(Color.Yellow)
        }
        TabContent() {
          this.customContent(Color.Pink)
        }
      }
      .animationDuration(100)
      .layoutWeight(1)
      .barHeight(0)
      .scrollable(false)
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/DGapdyRZSXi3mvaBoshqHg/zh-cn_image_0000002194010416.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=D54B76887CDD108D757D7B02D27B98D6B267050E03C0BB49EF1D397ECD202D6A "点击放大")

实验二：设置animationDuration为1000ms

```typescript
@Entry
@Component
struct TabsNegativeExample {
  // ...
  private controller: TabsController = new TabsController();
  // ...
  build() {
    Column() {
      // ...
      Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
        // ...
      }
      .barHeight(0)
      .layoutWeight(1)
      .animationDuration(1000)
      .scrollable(false)
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/I9cTWpdNQwCbiqoK279-Ng/zh-cn_image_0000002193850820.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FCA55F9B60F6C508357E1DA122153C906318A1675D9D9C88C64BFDB4F294533 "点击放大")

**表1** 运行效果图

| 设置animationDuration为100ms | 设置animationDuration为1000ms |
| --- | --- |
|  |  |

**表2** animationDuration属性值对比

| animationDuration属性值 | 完成时延 |
| --- | --- |
| 100ms | 99ms39μs |
| 1000ms | 1s7ms693μs |

上述示例通过减少animationDuration属性的数值，可以减小Tabs组件切换动画的完成时延。不设置BottomTabBarStyle样式时，动画时长默认为300ms。开发者可根据实际业务场景适当降低动画时长，以提高应用性能。

### UI组件优化

转场新页面的组件过于复杂、布局不合理以及资源全量加载等会影响页面首次加载时延，可以采取如下方法进行性能优化：

* UI优化：可以通过减少嵌套层级、减少渲染时间、使用缓存动效、LazyForEach懒加载、动态import等方式进行优化。相关原理介绍以及场景案例，请参考[UI组件自身创建耗时长](bpta-click-to-click-response-optimization.md#section1497610408322)。
* 全局自定义组件复用：使用自定义组件复用池，实现跨页面的组件复用，实现思路以及场景案例，请参考[组件复用](bpta-component-reuse.md)。
* 预创建组件：使用组件预创建，可以利用动画执行过程空闲时间进行组件预创建和属性设置。相关原理介绍以及场景案例，请参考[组件动态创建](../harmonyos-guides/arkts-ui-component-dynamic-creation.md)。

## 实践案例

### 存在大量等待时间无法诊断

在主线程长时间被阻塞的检测结果中，点击“存在大量等待时间无法诊断，请您确认”，打开Profiler工具，加载完成trace数据后，会框选主线程运行空闲的区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/EgsKbGS_QROjS7X0eSJvMw/zh-cn_image_0000002480446276.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=3389255662D0FAF9642C5B2606AC549F6DE3587EF9EAC0503192C1CB75F27402 "点击放大")

可以看到框选的397ms中，主线程主要处于空闲状态。放大该选中区域，并从框选的范围内，从后往前找Running前面的Runnable，点击查看Runnable详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/FXu6rN4IR8qzAdswlyrQlA/zh-cn_image_0000002455902388.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=53C1C22EA8A656301D07630863E6BFF10438D8818D36E205DEDAF0641177DC6E "点击放大")

通过Runnable详情中的WakeUP From Tid，可以看到是VSyncGenerator唤醒的主线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/e52RT6XiQwGi0X0NghDukg/zh-cn_image_0000002489181689.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4E7CFEDA233457FE2DB9F05F24F1990280ECB754A2223F091735D6A27A66051 "点击放大")

点击该线程名后面的跳转按钮，跳转到VSyncGenerator线程的Running详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/N-I5yOKgTFmzXo1oLsgerQ/zh-cn_image_0000002456062016.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=64CB83F93B1E7E6B4779B4CAB8FB5BAF859C1895FF2293F1A408459355A815FF "点击放大")

放大该区域，并点击该Running前面的Runnable，可看到详情中没有WakeUP From Tid，表示该线程此刻Running不是被其他线程唤醒的，且上一个状态是Sleeping，说明这条唤醒链路就断了。若该链路断掉，则需要回到主线程运行空闲的区域中，从后往前，继续上述查找步骤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/165PUoXIR-upBIrI4rokCQ/zh-cn_image_0000002489141661.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8FDF0948F4646EF05051D5BAC71B3E245C6426543257ABF2E2DA32F1FE155F5 "点击放大")

再次点击“存在大量等待时间无法诊断，请您确认”，回到主线程的空闲范围内，从后往前，继续找到上一个Running前面的Runnable，查看详情。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/GN2Sef7VTgSWpUnqWNP1MA/zh-cn_image_0000002455902392.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=90FB7E5E851498B7606727E6D8ECB1692F2252F8CA8DED846DEAACDAA972BAC8 "点击放大")

通过WakeUP From Tid，可以看到是OS\_FFRT\_2\_1线程唤醒的主线程，点击后面的跳转按钮，跳转到对应线程的运行泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/odDXmrvNTSir9VAAjAZWcQ/zh-cn_image_0000002489181693.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=B39CFACF064606612A6D2AD257DEEBBDC3DA201A419F67B9068D8EC610908089 "点击放大")

可以看到上一个状态是Runnable（Preempted），可能是CPU的时间片调度用完了，可继续查看该状态的前一个线程状态是否为Running。如果是，则缩小该区域，观察该线程是否连续在Running，并找到连续Running的开始时间。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/9lHY9g1JR_SZTQ26NtcXew/zh-cn_image_0000002456062020.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BC8845D36C151609F79BC772BA9A70AC03B4318D799E47F908495044AFD0F73 "点击放大")

通过连续Running的开始时间的第一个Running前面的Runnable，继续找线程唤醒关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/J4QAnIQcQMyfcZMvtux87w/zh-cn_image_0000002489141665.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=9AB44AB3DC8E16B6D54989818780EB46004DFED4D4EEF9C54D25EDA97BFECDEB "点击放大")

查看Runnable详情中的WakeUP From Tid，可发现此刻Running的线程是主线程的唤醒的，将该子线程泳道收藏，并通过跳转按钮找到主线程唤醒该子线程的位置。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/djB8J3seSkua6CvSFXyHEw/zh-cn_image_0000002455902396.png?HW-CC-KV=V1&HW-CC-Date=20261112T233136Z&HW-CC-Expire=31536000000&HW-CC-Sign=1DB5CF80ABA2B62FA74D5D0BF43D2C88AE8854759BEAFBAFFDCD77BD97264975 "点击放大")

可以看到该空闲时间段，主要是在等待子线程OS\_FFRT线程执行耗时任务导致，需要开发者判断主线程是否依赖子线程的返回，如果主线程依赖子线程返回，需要优化子线程的函数耗时，或者将耗时任务提前执行。
