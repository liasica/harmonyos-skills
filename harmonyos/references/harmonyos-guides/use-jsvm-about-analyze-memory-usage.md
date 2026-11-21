---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:52+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:7fec7454e270c478610cccd4e8ce605ee89d0a747f054b9c35a2d1b533db1518
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ChTzunxXTROLa9SvB9a8Jw/zh-cn_image_0000002793038498.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=7425BED3CD9BC4A39FC349AA9077D0F8ECFB0D39C248EBCE689868914379241A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/pmbRhw21Tkyo50sQM8ImDQ/zh-cn_image_0000002792878528.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD2BE155DDD78BFE8B730E4F66D9C1266197DE754EF0DAE2DBE1299E5384CD84)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor)：表示对象的构造器。
* 距离(Distance)：与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/3undi68aQ-yqhof7IAhsxw/zh-cn_image_0000002821838435.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD642C981583D28FA4E14BDFE2B2E12006C84F4366F45938FBAFE1B650476E93)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/CWh5GJX6Tk-Uc7XwUlEwvw/zh-cn_image_0000002821758437.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AD10F9E70EA30EE7AD1F3A91F18444B153033689EB4BCFEC0F18DD9DB0DFE40)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/YLPsF0XRSs6L26JwLUs-WA/zh-cn_image_0000002793038500.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D4DC656D6801F1F5C9195E1A9C00E394AD4DBB4CA89EDE646AE598EE86916AB)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/8Ipj_4w2SjOultOP8xdRzA/zh-cn_image_0000002792878530.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=95D951385C0DC41D22D9E699834359BC5035FAFC0D0745E846E4BD1CF73EED20)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/HFTWzuIvQB6b0bzcanbx8g/zh-cn_image_0000002821838437.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1D888FD1D680640AC6CDC99ACA6B4D90917EAEAF05FEE8DE23DEA2629BC160A)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/9RgfNXCNRP-JSYv8-9KZ9g/zh-cn_image_0000002821758439.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=08C73AB966A66DED4F6CBE74DD8E07FCDB89AEFF7F27A4FF2F09FA227E333EF1)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/jbY8JuXASHaJbG0DNp5U0Q/zh-cn_image_0000002793038502.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=04FBE286065432E404E3A97B2C5D638E8C28C367EFDE6209F86FE77F4E8B871B)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/SkzTCRWmQQ-2qcUXO58axQ/zh-cn_image_0000002792878532.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=92725DD0D2C404C897095AC6CB72826D761C3BFD408B99DD90C7F12760A95996)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/61mC4pmkQROJvnKrNWozDg/zh-cn_image_0000002821838439.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=67D1AE8652071C0315AC5908CF352B5E759953D9E8321ECA553A5AC2D16150E9)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/04tcARPBRM6Ntd-YC46qpA/zh-cn_image_0000002821758441.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=26EC0EF84E1A0DDF52336405A6E9924104F4750CE42A3F3FD335F1E3247D3A71)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/9xaRFMdCTcSc_hhbsWCkcA/zh-cn_image_0000002793038504.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=640233BEDCD3E3514A33DD08877752D9F8221AAF68EEE3B9513E4BF8FC2BA9A1)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/h8Y4MlYhSDuROR08pXIj9Q/zh-cn_image_0000002792878534.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEA9373B04AE59F03B5A7376C18421D3F81968480E98CDF4A3B20CE7A4BA8729)
