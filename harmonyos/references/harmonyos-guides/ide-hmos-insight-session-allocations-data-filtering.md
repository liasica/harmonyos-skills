---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:58+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:65db5f83353df188ed31ba756680b4ced352aeeb8365ccc151e190dc3029ab1e
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

在Allocation分析过程中，对Native Allocation泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在**Native Allocation**泳道的**Statistics**区域左上方的下拉框中，可以选择过滤内存状态：

* **All Allocations**：详情区域展示当前框选时间段内的所有内存分配信息。
* **Created & Existing**：详情区域展示当前框选时间段内分配未释放的内存。
* **Created & Released**：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/HC17BrixT7y52DD1fpfCTw/zh-cn_image_0000002820680911.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7B2FD3A3646BA8A4542D9D6FC770DF36BBCE4942CA23736918F204F1182EE4E "点击放大")

## 通过统计方式筛选

在**Native Allocation**泳道的**Statistics**页签中，可以打开**Native Size**选择统计方式以过滤统计数据：

* **Native Size**：详情区域按照对象的原生内存进行展示。
* **Native Library**：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/4Qm2Di8LRGmfyS_X6oZVIA/zh-cn_image_0000002820680907.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=9115AF9B6DCD7E1501885547E395C316457F737EEC64F68F8A360BD1EFAF190A "点击放大")

## 通过搜索筛选

在**Native Allocation**泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/1wWzdzy9Rm2hFxaXCfIQxw/zh-cn_image_0000002820720913.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE2D0F964387DF80DF0F662CD5AC69B2CC319E9D5F1944A75D36B312A45AA53D)按钮可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/eDpkH_W4RBON8fBngzx8TQ/zh-cn_image_0000002792000948.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=17993F3DB61303D55E018EC190CC19826FF56C1729498109F152003F52E727B7 "点击放大")

## 筛选内存分配堆栈

在Native Allocation泳道的Call Trees页签中，可以通过**Call Trees**和**约束条件**选择框来筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* **按分配大小分离**：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；
* **隐藏系统堆栈**：隐藏内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/MVu31ucAS2-4g_AW8uQ8RA/zh-cn_image_0000002792000944.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF1A903D827C056E3BB829EFDC0D262BE4C3BF85D8E356F3057A27207AB58DF8 "点击放大")

**约束条件**选择框也包含了两种过滤条件：

* **Count**：根据指定的内存申请次数过滤内存分配栈信息；
* **Bytes**：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/zfDGFysoTziu6BRBmjXRYg/zh-cn_image_0000002791840972.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=464D25517AA7CE54B5F9013F089D5F0454AAC0247B54DB5C1F6639BEA0FDA309 "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/cCVuZLuITSaBdcbNYvP2Lg/zh-cn_image_0000002820720911.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AAA96C60FC6E11427575460572A6A01BC2A4D4E4820D92F2C1C2E34C5E11085 "点击放大")

在Call Trees页签，可以通过右上角的**火焰图**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/_D7NcMuBRFK_pXsvcOxPfg/zh-cn_image_0000002791840976.png?HW-CC-KV=V1&HW-CC-Date=20261128T023458Z&HW-CC-Expire=31536000000&HW-CC-Sign=75A05FA3D846909EA7BEC40C1F7849614ECC62FACF296A5FBB8060D18FAED4AD "点击放大")
