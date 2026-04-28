---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d73c9686f89e4836baeb7450eeb686bded0abf598b78c876418293756261e72e
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/e1dpnmZ9Q16CeprWgmpVjw/zh-cn_image_0000002552799730.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=2E12CC880E6EA078B5912BD5C389B9E03B979BA949F8346C72B49BC15F1FA5CA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/2qhmO-mrR_Se4n5fkUJYOA/zh-cn_image_0000002583439425.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=EF54B69F4FE956E127582239E599D8C64F82B880B02C889935A0AC0E55FA133D)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor):表示对象的构造器
* 距离(Distance):与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/9GhBwdj0T42QWMDXDka3eQ/zh-cn_image_0000002552959380.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=0A9E37253DF1290288A6D665AD6CE08B5FFF756F314CF9B83460B5EB7FD2B381)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/T_JTtguTS4GYXQPmweJ6rg/zh-cn_image_0000002583479381.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=C925B8DCE38481277CDF9DAAA088CB067E17B8C9540E8984E2B18D754E5C9956)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/UCGPhWgZRY6ACa0TSApT1A/zh-cn_image_0000002552799732.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=D9086F737710EF7858B7EBC6BE0945D6CA249C6727E6C83D208A0634812591AB)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/MS5OFm7FSL2YMnzsUEdSGw/zh-cn_image_0000002583439427.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=8DDEF6531EDF6515A55A6A77812F547AFD3BB5BE7976E0AAEF047F0F5282B0D4)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/HTWILsBMRvOvy_qNvDWwIw/zh-cn_image_0000002552959382.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=3FA7C7937101486D450A8BE42B2ACE8E1994D396A4BFCDA0CAE5D1351AC4C04D)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/sLYPuOBVQTq9s4jVb7FGZg/zh-cn_image_0000002583479383.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=AB8E4E724FFAEAB7895C79602067ADA3B42C6E20D3599CA4AB2A845691C45CDB)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/jkV16rINRv-NZRcEl9ugFQ/zh-cn_image_0000002552799734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=CDABFACD5BB0234EFED672FB4B79CA45E3DD7EF18DBD0E508C685D1F2AB75B8B)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/uN8DG8C1QyuQZsiwGUC3Uw/zh-cn_image_0000002583439429.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=2722471B3E2599E1713229156D76A14D75F2873AB51533DE2335E64498C4BA43)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Y3ZKHwtITEijg21Ebxr2uQ/zh-cn_image_0000002552959384.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=76215B01791003D01721C456F2F47FB9B10738618A7DCD8E0015BA2170919075)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/vo1278_UTgiSsiYaOLaRTA/zh-cn_image_0000002583479385.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=9EB4B8379B1D8B4B5A1861666386FD59D2F33C131A8C13E0CFBC9356491150D1)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/vfj51JTdQYqsOT5M2Mrv3w/zh-cn_image_0000002552799736.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=60FCF55541904D4DBEF3264AF90AC7343C1803A93C3F15DEF649DA6654E5F17E)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/UwXAs9QwR4G79bmbIvYyAA/zh-cn_image_0000002583439431.png?HW-CC-KV=V1&HW-CC-Date=20260427T235427Z&HW-CC-Expire=86400&HW-CC-Sign=B5281588B6AD64A5D494B8878791690A95D7F4FB710B932EE31FFD7C7AC017D6)
