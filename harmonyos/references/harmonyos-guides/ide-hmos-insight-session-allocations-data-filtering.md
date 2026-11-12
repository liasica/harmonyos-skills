---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:aea92ff9eaeef40c1bde04537b253e1178792e06ace8a925e15d6a2c675d42e3
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

在Allocation分析过程中，对Native Allocation泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在**Native Allocation**泳道的**Statistics**区域左上方的下拉框中，可以选择过滤内存状态：

* **All Allocations**：详情区域展示当前框选时间段内的所有内存分配信息。
* **Created & Existing**：详情区域展示当前框选时间段内分配未释放的内存。
* **Created & Released**：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/AnSzaVjnTx2v_KIVefIB2Q/zh-cn_image_0000002781471262.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=39FE22220A8A60848A23B3192BA8B98AF82A77B4C74E168F0A9DA8C945145F63 "点击放大")

## 通过统计方式筛选

在**Native Allocation**泳道的**Statistics**页签中，可以打开**Native Size**选择统计方式以过滤统计数据：

* **Native Size**：详情区域按照对象的原生内存进行展示。
* **Native Library**：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/wEYoQsrhSQafL1adcdTFRA/zh-cn_image_0000002781311326.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F25FF0DBFF97B5B7990378348DAF626DDF90FDCF6EAB5FD04FBBFDE4FD61103 "点击放大")

## 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/tpXkQcgeSt-Iq9e9beYUrg/zh-cn_image_0000002810630819.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E7A7A49EA6CD416D0DB9C2E415F7F0E1296300429F3D6932CA612CD06635BE6)按钮可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/2fKSdycASqaXzz4IvRixdg/zh-cn_image_0000002781311330.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D845A20BA97466B5D83F0D03ACC01EFA30648E1C10FB6702E10C64BF86DDBEB "点击放大")

## 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过**Call Trees**和**约束条件**选择框来筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* **按分配大小分离**：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* **隐藏系统堆栈**：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/WXOSdJXyTnagij-NPRfjUw/zh-cn_image_0000002781471266.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=47813A28705A8D8587D2C76FF480D52DB8BEDC3B17C6F427C1343D238F36D758 "点击放大")

**约束条件**选择框也包含了两种过滤条件：

* **Count**：根据指定的内存申请次数过滤内存分配栈信息；
* **Bytes**：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/PD91gEhCRBuUhDeTWaraYA/zh-cn_image_0000002781311328.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2C9B4CE83FFBD01001CA3CDE63EEE47FECF36DCD78DC3307E46BE48B094F92B "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Gg2iW-G4T3OK6WXMQcCT4A/zh-cn_image_0000002781471264.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C8595414E91B2EA57E00DA53702C43F11053844A161A199E2E62C1DAA8A3B27 "点击放大")

在Call Trees页签，可以通过右上角的**火焰图**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/LkaT_kc2SPmUEkE2lQ9ifA/zh-cn_image_0000002781471268.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E33042E385E5A1DCB2ED33AAECD31A07A592C7376817595A54616490C8CDF8B4 "点击放大")
