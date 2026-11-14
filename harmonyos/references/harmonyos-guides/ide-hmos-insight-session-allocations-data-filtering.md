---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:86e96c67b13d53d2653d9a0f8f32bde8334cdf13d0531d18a3b84c8ab60a41d1
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

在Allocation分析过程中，对Native Allocation泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在**Native Allocation**泳道的**Statistics**区域左上方的下拉框中，可以选择过滤内存状态：

* **All Allocations**：详情区域展示当前框选时间段内的所有内存分配信息。
* **Created & Existing**：详情区域展示当前框选时间段内分配未释放的内存。
* **Created & Released**：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/MGCJ9GQSQ5uQKSI4z6LLmw/zh-cn_image_0000002781471262.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=A88F7A5BB58F3B6F19623E009F43AC462964C09C61697EB2A27A87BDE1E8FF60 "点击放大")

## 通过统计方式筛选

在**Native Allocation**泳道的**Statistics**页签中，可以打开**Native Size**选择统计方式以过滤统计数据：

* **Native Size**：详情区域按照对象的原生内存进行展示。
* **Native Library**：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ebWc_YzVReqMGgrG-6c8Gw/zh-cn_image_0000002781311326.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D8C884C3D381A0DD25B90DFCCD0CE3FDAD91AAF18C221ADCA80E1D1B458EF63 "点击放大")

## 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/GEguh05ySIWq2uevWKpz_Q/zh-cn_image_0000002810630819.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E6FEB80392884FEB33465281D9728D37BDD46F6F9B5ECE9732BE2BBEF0420E7)按钮可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/pXLHjNbURdShs_kafmfegg/zh-cn_image_0000002781311330.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=05C1A0D1F2176F807D9EE0377863674117DD2C990907E0DC4994A3BC8C79411D "点击放大")

## 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过**Call Trees**和**约束条件**选择框来筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* **按分配大小分离**：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* **隐藏系统堆栈**：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/_eDbhnyPQ0CCg9jbN7kJkg/zh-cn_image_0000002781471266.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9B7EE9A0B6BC98B0955A34B5DE425DC1048E1AD18A5B18E94E90DA529DF3602 "点击放大")

**约束条件**选择框也包含了两种过滤条件：

* **Count**：根据指定的内存申请次数过滤内存分配栈信息；
* **Bytes**：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/c_ngBPlpQLOGS1YnYIY2Nw/zh-cn_image_0000002781311328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE5897EC3308F441AE3168CFAD608E21917A13D64C99BCE1B56569DCD2A41E88 "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/_UXFMrJ2TLSNc0rV_gItyw/zh-cn_image_0000002781471264.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4B3A9189B914B51E9D0671A1B50340CA4344DDB10ADA46F70C0C86884761A4C "点击放大")

在Call Trees页签，可以通过右上角的**火焰图**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/nEdJotgqQE6zDkh_f3JPzg/zh-cn_image_0000002781471268.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=066B2974E2F682CA9DB80F330065EE2F5A81E8ADA34014CA3B926AE797B42223 "点击放大")
