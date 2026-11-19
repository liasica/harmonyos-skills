---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage
title: 使用DevTools进行网页内存分析
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用DevTools进行网页内存分析
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:27+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:b51ad6a740243764d9bf7da0998e298053c43a21b7b3a8ddd4830ce294112c36
---

## 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

## 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/eYEeSq2kQ8yBIpEDL3Tp-g/zh-cn_image_0000002791726846.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F357672F6AB9DD471859A4CC3E4B87C1843B01441BDA9A2D3E514C75FCC6EA8)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/nQTruHQ8QBCBm0bhygD-aw/zh-cn_image_0000002791566874.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=43DAB5DCBBD88318A59C43C7F1EC9229B0B75FA792C8D8E91FCC34814267A37F)

## 堆快照分析

### 摘要(Summary)

摘要展示当前内存快照的概览。其中：

* 构造函数(Constructor)：表示对象的构造器。
* 距离(Distance)：与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
* 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
* 浅层大小(Shallow Size)：对象自身占用的内存大小。
* 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/qd5bhUkiQHSfgtLTgKob1A/zh-cn_image_0000002820526827.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FCE9BCBFE79C643CEDECDC390DBBA74926F9532141940E6FD711CC6BF1855C0)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9ooZu3xFRKOfAj8oGHvi1A/zh-cn_image_0000002820406827.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=24B19DBB39C5ADC1CA79547909259753331081BC3F27E94C03DAFA7CC1099A4E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2D7RFqgyTFqWBiZtwKQlLQ/zh-cn_image_0000002791726848.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=143B43AFE79FF441EEE3D8968D1C874BAE9A0728DAB33F5920F99AC55460FD9B)

### 控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/mfDMLzq3SKieog897_ZuFg/zh-cn_image_0000002791566876.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B4CFD6358DCF3A354C62475501693A9BAFBC0E6FB04833CD817EFFFD31707C5)

### 统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/HBg0VARPTHSBg2YJwe2AdQ/zh-cn_image_0000002820526829.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=98F0F1AEC86487807256049B0690DD74F14F71BB04950DE4CAA7654DCAF03897)

## 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/FSXwjU2-SQe0MfDcW0PW1A/zh-cn_image_0000002820406829.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F04F66F95E9479EC87941D5AE3A091713120DE9310EF41EE6DDE09707AD7169)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/XzI9IIiqSRuNmT_2hvy_iA/zh-cn_image_0000002791726850.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=57506FBFB994C30C916C047F134D779893FF6FF6A3BA74F8F36CAAE5B3B05D99)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/--aGjgR5QM2xxdJNVwxVhg/zh-cn_image_0000002791566878.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CCA95595A529572BA0A0F2EAF6E3708E15622294F0E81C6A7FE34F3BB906773)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/MT3qsIvhTpuF_JPWKJQO_A/zh-cn_image_0000002820526831.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=9212AD854833C97F2D2273297CD6DB504E339DF4F59C16E2A73FBE8F0A52A95D)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/FDsZamzSS-qt0UOFVPJW3A/zh-cn_image_0000002820406831.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AED7D213C31C01414ED47C0B75227ACDDEB94A38165B3B16FBE205BF7FF9FDB)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/62i8he6bRNKqetM1WEurog/zh-cn_image_0000002791726852.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=B548AD2C1EF4EE519FF250EE8E08FBED7F3BE6B58219C0236B5E19BE1B7D1487)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/47JRL7uqRAK-1uQFeujt9g/zh-cn_image_0000002791566880.png?HW-CC-KV=V1&HW-CC-Date=20261119T014832Z&HW-CC-Expire=31536000000&HW-CC-Sign=E89853AAB95D0FA49B7294EFAA26E65ED9CBC9272EB9AFE7C5C0DC3ADC48FD99)
