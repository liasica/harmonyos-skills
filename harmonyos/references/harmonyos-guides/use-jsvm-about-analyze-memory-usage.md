---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:45+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:e44a475549e8a9d8a8542f208996d4396c5a2a99c7990d26989585ef62d00494
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/0I3pZKZ-QNm2dBIxpKGTFA/zh-cn_image_0000002817427907.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1FFB9D61CC476A95705746A5EE9EEBFC01CE2A231D57393D46B99E4A9E0E8DA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/MZaPUQE4See69f6QNC7Raw/zh-cn_image_0000002788468488.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB4F7FBD79BCA939C33C7994952CAF595BC8E3386E6F55988E21B4955A983DD2)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor)：表示对象的构造器。
* 距离(Distance)：与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/WYMpDagPTj-LonShZGqj9A/zh-cn_image_0000002817507977.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=975494FCA8438A11ADC36E154C55F9CC30D66395A761EA154AF753C6829EDB83)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/0-ln0yFaQvCa174io208IA/zh-cn_image_0000002788308546.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2F4B5E19DDCB347BEF3A5F164981D94609A350C604E061B116D614D9CE4E968)

### 比较(Comparison)

在比较(Comparison)中可以将当前快照与另一个快照比较，跟踪对象属性和内存占用的变化。其中：

* 构造函数：对象的构造器。
* 新对象数(New)：该对象构造器下有多少新的对象被创建。
* 已销毁(Deleted)：该对象构造器下有多少新对象被销毁。
* 增量(Delta)：新对象与被删除对象的差值。
* 分配大小(Alloc Size)：两份快照间分配的内存大小。
* 已释放大小(Freed Size)：两份快照间释放的内存大小。
* 大小增量(Size Delta)：分配大小和已释放大小的差值。

可以根据比较界面不同快照间的差异分析内存问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/DzQ9Q7WyQTq1aLKMiC1-Hw/zh-cn_image_0000002817427909.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=96D9C7D0712F1C9BBB3F93327DBA4AE43ABF29D6FA30249F5B6FF499BF813E52)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1VVZQuoNTDq8mrdo5d0C5Q/zh-cn_image_0000002788468490.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA83D26E9FCE9EEACA3F152995075EEB059EE688E74271B2B258D5A247D0FC19)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/b_QMQGiCQUeIIncEijT5MA/zh-cn_image_0000002817507979.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CE1EA2C96A6D6DF539AFBC070A3FC161A33310DAE08FA40DBA77B4E71F37D42)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/X4tcMMcIQDGRzXVBRVJfhQ/zh-cn_image_0000002788308548.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=35C0A9720DD090A29ADD2CC05EA5902AA8A3F155808BE65136244A30ED28F343)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/WVs4YHagRf6UsF6QD5kJKg/zh-cn_image_0000002817427911.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=323ECB6152243E42DF72CB9F2D4455C8ABA269CE2BE292C6A8C487723491C514)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/oriYe_fyS9-h_ZO0xb5pLA/zh-cn_image_0000002788468492.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D1FF193D9E23E5BFEDDE3F41AD642D12CF7D31C852BBE0E0503777749319C1)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/h3N-evtGTOW2-gLWGJaFbw/zh-cn_image_0000002817507981.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC95D2E02BAD7255A172AC038327938428E8B20EA5877C418DA561ABB1A8B550)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/paovaFVWQbeg5ZmHxdxM7A/zh-cn_image_0000002788308550.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6CFC8F45BD716C16CF513D2F3DD9253EA4082B71265ED42CF45D61D18D0895A)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/6QrClV71TVm-vkpNky6ljA/zh-cn_image_0000002817427913.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8E0D1E9F1F9DA488BAABF7F9129BD6F8432A57F6997A7EA297D3E76F406FE01)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/o2pvMwzVS_m4KpkpYsT1sA/zh-cn_image_0000002788468494.png?HW-CC-KV=V1&HW-CC-Date=20261114T004659Z&HW-CC-Expire=31536000000&HW-CC-Sign=57780B9B5C57DBA0B39850A3EF26CD84F9F3F3C8EE481D25DBDA07F45DA9C06F)
