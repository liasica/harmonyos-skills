---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:12ca533736c16dfb61722b6e3f424893252cc89485ae52b9e5e4ba3e896d5c17
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

在Allocation分析过程中，对Native Allocation泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在**Native Allocation**泳道的**Statistics**区域左上方的下拉框中，可以选择过滤内存状态：

* **All Allocations**：详情区域展示当前框选时间段内的所有内存分配信息。
* **Created & Existing**：详情区域展示当前框选时间段内分配未释放的内存。
* **Created & Released**：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/pXOeEoE3SLKNZDV6sXjWTA/zh-cn_image_0000002781471262.png "点击放大")

## 通过统计方式筛选

在**Native Allocation**泳道的**Statistics**页签中，可以打开**Native Size**选择统计方式以过滤统计数据：

* **Native Size**：详情区域按照对象的原生内存进行展示。
* **Native Library**：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/wMjqY5-VR4iC_fBhVtLycA/zh-cn_image_0000002781311326.png "点击放大")

## 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/NgHclBnyQfC22bApl24qfw/zh-cn_image_0000002810630819.png)按钮可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/kKD6U1PCSx-Upb_R6eD27Q/zh-cn_image_0000002781311330.png "点击放大")

## 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过**Call Trees**和**约束条件**选择框来筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* **按分配大小分离**：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* **隐藏系统堆栈**：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/But3pN_NR_Sg23qNF-ZEIw/zh-cn_image_0000002781471266.png "点击放大")

**约束条件**选择框也包含了两种过滤条件：

* **Count**：根据指定的内存申请次数过滤内存分配栈信息；
* **Bytes**：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/wbycQjp2SFq0DAAlp-WtDQ/zh-cn_image_0000002781311328.png "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/YhEAuor3Tae2fga-0u4XzA/zh-cn_image_0000002781471264.png "点击放大")

在Call Trees页签，可以通过右上角的**火焰图**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/J95GSuDFTMOpxIbtVfBqaw/zh-cn_image_0000002781471268.png "点击放大")
