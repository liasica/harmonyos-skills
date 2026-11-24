---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:49+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a0cdfac1e33293333de490ac5871f066bd77c12025ed6b31b87c9f6c418a7d27
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

在Allocation分析过程中，对Native Allocation泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在**Native Allocation**泳道的**Statistics**区域左上方的下拉框中，可以选择过滤内存状态：

* **All Allocations**：详情区域展示当前框选时间段内的所有内存分配信息。
* **Created & Existing**：详情区域展示当前框选时间段内分配未释放的内存。
* **Created & Released**：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/VxYu78AmQLi2KX9n-sfodA/zh-cn_image_0000002820680911.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8217183A658BC097B1F576396DADF2A8B995DFF98315410093C655541838115 "点击放大")

## 通过统计方式筛选

在**Native Allocation**泳道的**Statistics**页签中，可以打开**Native Size**选择统计方式以过滤统计数据：

* **Native Size**：详情区域按照对象的原生内存进行展示。
* **Native Library**：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/Tjc7Rw_TSQCxxbNxz6gRVQ/zh-cn_image_0000002820680907.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A512B543994ABFC745113E7D74237DA85C8C459A43C84A0FE7F7087996A0005 "点击放大")

## 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/yN5YPtBzShW2P06-0e4tCg/zh-cn_image_0000002820720913.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5BE4B7FDD62831A0A97F6E5E84F6C040931B276C8B6D29C6E4E5EC5ED7FB8EC)按钮可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/4DyHxCwEQ-aBk3AX4px2aA/zh-cn_image_0000002792000948.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=074A2B10DCC62B93F30F603D28EE2EE36E8327209F6396FFC191021654516DA5 "点击放大")

## 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过**Call Trees**和**约束条件**选择框来筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* **按分配大小分离**：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* **隐藏系统堆栈**：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/NBaivVwGTtKsmjDzCuuzDg/zh-cn_image_0000002792000944.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=B84D76F4C81F76B0BAED914AB50F5E607EB34073C31C0DE77A5456E28CB55CA7 "点击放大")

**约束条件**选择框也包含了两种过滤条件：

* **Count**：根据指定的内存申请次数过滤内存分配栈信息；
* **Bytes**：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Ho6XscdqQx6VFj3DVLbepA/zh-cn_image_0000002791840972.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=8042617FB1966DE74BBE831A1A1CED4D801744E8FF81E7ACD18A3E2B6E0F389F "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/I37D9XaTQL2Nz53LC2_3uQ/zh-cn_image_0000002820720911.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DD1AEA4084B755A32D7D757CE7EF2D5017C8C3DDB0775FF6F7602BA7E1F9CFC "点击放大")

在Call Trees页签，可以通过右上角的**火焰图**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ZmLkeMRjRjis7eEvRFN6TA/zh-cn_image_0000002791840976.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B91E000973BFE5666EE16E345EAA9C591FDF1D38F0FD0ADD6CAF5E74CFC27B1 "点击放大")
