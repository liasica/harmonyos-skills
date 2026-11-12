---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:ed963a78274b3c94de63ebd214552f9c78ca988dd91332f62716502c70794b53
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Hp9aREXSQiu1peJdKoEBaw/zh-cn_image_0000002815400315.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=558D1532068D73BF8BDAAC20F548E43189753713A045538C91FAA73E410D747E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/90skAvAFRSCMIpW-FnJQ7g/zh-cn_image_0000002786520740.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=35BFD3992BCB9CC17CFC8FDE9E7D94647D839FECF6D61B19D9BA7E8AF6254154)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor)：表示对象的构造器。
* 距离(Distance)：与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/fvrErjB-RFKXKdfOPKI2gQ/zh-cn_image_0000002786360812.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=00CAC4B93A7076C91C62D41D046625421A76F9508C47DF8383588185E1A40E4F)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/wr_r-E5USNeqjr0C2LcmEA/zh-cn_image_0000002815560233.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=828F999E3E8C02E8679D52BB7943557DDE93E8B10280BA56B7F01C72DC750614)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/RJjKkrD9Re2L8sNwp6Ip7Q/zh-cn_image_0000002815400317.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=5721CF22DDD1D50912633A013F4875BE151CF691617A9AA790150A5B99BBF491)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ZuAuLEvoROaFxMdbFGi-uA/zh-cn_image_0000002786520742.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=436BADE717324A1B40D9FFEABE542AAACD9042B63C9871D7F11EE1212FEB4215)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/A-4JvzS-TQi0h_Fwnd7-1g/zh-cn_image_0000002786360814.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DD7A76EED09E16ECAA0774F06CF68C6ABD593051017387E76067CB69A161043)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/ADZ3OWmbS0SqTdj5g0C5ng/zh-cn_image_0000002815560235.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=090CF7EF8918B76CEE26794E5142004DDF442CEF1E5FF8044DF6EA476394FDFC)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/s_2QLG0bQpaZpn19y45FoQ/zh-cn_image_0000002815400319.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=74992873861560F472E947E59B8C4FBC9DD6134AD6B6E1514E5BD135B0DEF7D1)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/sEXm4suGTMmx50GPPIWrxg/zh-cn_image_0000002786520744.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=016D795D880E83B25496C89A8537CFEE0DA3E1DE5CE8171BC4D7F3ECA4AC6EE2)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/MJ-42SlyQg-6N511lDvn4w/zh-cn_image_0000002786360816.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D37CD058F808106AE42A0C6529F99BE5FE78E4372FF7C679070327DE1B84922)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/pkjMvs1kRbmHERPxtWbRwQ/zh-cn_image_0000002815560237.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=C70EF79AB807B1F340EE5A26F42172A5805EC536DE69ABE256EF5C124E000C3E)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/cVWsYr7aTHuRW2Zne4_w6w/zh-cn_image_0000002815400321.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=3993AA1112ED78B33FF89BC4AA1548FBF01DCCD1A4E6758D988737CE74EB43BF)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/LyF6mMC_TsCZgz8uQ-iFYw/zh-cn_image_0000002786520746.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E18CD0842BA4C1C865561A56F695946F7A2F8F2EB277AEFB419D28A398C3CEB)
