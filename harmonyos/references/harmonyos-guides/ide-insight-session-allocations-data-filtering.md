---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:cea82d815bb2a67e16777c9eca470d90aaeac3e086227f13d6d3d819ce9c9250
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

从DevEco Studio 6.0.2 Beta1版本开始，支持对Native Allocation泳道、Graphic Memory泳道的内存状态信息进行过滤。

从DevEco Studio 6.1.0 Beta1版本开始，支持对All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在详情区域左下方的下拉框中，可以选择过滤内存状态：

* All Allocations：详情区域展示当前框选时间段内的所有内存分配信息。
* Created & Existing：默认选中，详情区域展示当前框选时间段内分配未释放的内存。
* Created & Released：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/yO1Obq-mQneu4oWIVddtsA/zh-cn_image_0000002779567442.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC97658DE9A6C6B639C719B227BD29C6FA1D55343F08F6B64230B9E06EC7FF28 "点击放大")

## 通过统计方式筛选

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的**Statistics**区域，可以打开**Native Size**选择统计方式以过滤统计数据：

* Native Size：详情区域按照对象的内存进行展示。
* Native Library：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/XBDKf72YR3e8v1YpHc_oKQ/zh-cn_image_0000002779567440.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=C96BCFA3C1C5E9179D6DE8EA159E005FF00105F7CD580D11D1381E9E219FC5E9 "点击放大")

## 通过so库名筛选

非统计模式下，在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的**Allocations List**区域，可以单击**Click to choose**选择要筛选的so库以过滤出与目标so库相关的数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/oNWEHlNYTpucLnG_cgr7Ww/zh-cn_image_0000002779407462.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD3B4136E0C5E13E6D44DE007B030BA5CE28B7564CFF975645917E5EA2F68CF3 "点击放大")

## 通过搜索筛选

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的<、>按键可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/hdhq243eQcemtMD3XGg3Ug/zh-cn_image_0000002808767025.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=12C098DA219CB4623F0634270FBB95B80F0B85ACC93537F3F11447C2EA30B68D "点击放大")

## 筛选内存分配堆栈

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的Call Trees页签中，可以通过底部的**Call Trees**和**Constraints**选择框筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* Separate by Allocated Size：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；System Resources泳道中不包含该过滤条件；
* Hide System Libraries：隐藏内存分配栈中的系统堆栈。

**说明** 

**Category**字段表示函数调用类型，将调用栈类型归类如下：

* ArkTS：程序正在执行ArkTS代码；
* NAPI：程序正在执行的NAPI代码；
* Native：程序正在执行的Native代码；
* Native(G)：程序正在执行的Native代码所申请的Global Handle对象，DevEco Studio 6.1.0 Beta2版本新增；
* Native(L)：程序正在执行的Native代码所申请的Local Handle对象，DevEco Studio 6.1.0 Release版本新增；

  其中每一个类型的亮色和灰色分别代表开发者和系统的代码。其中，亮色代表开发者自定义的代码，灰色代表直接使用系统中代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/K0srZy2URICVY2ldpTVgJQ/zh-cn_image_0000002779567436.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=73773F19D18A78760FF50B0D79468F4D34D79FEF7E861BCB6E0C226254D3FCB0 "点击放大")

Constraints选择框也包含了两种过滤条件：

* Count：根据指定的内存申请次数过滤内存分配栈信息；
* Bytes：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/nuC35_WpSreHKGTN8ykyLg/zh-cn_image_0000002808887105.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=07CE5CE86AEA4FB9E8ADE697D52DB9D192FB72279650ED8EE9C918DD6F7BF4FA "点击放大")

在Call Trees页签的More区域，单击**Heaviest Stack**旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。System Resources泳道中不包含Bytes字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/JQdLqxfrR-qaFXjpgtJxZA/zh-cn_image_0000002808887099.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=50D1CA6A179A6001097E4F98AD623310E2F7C9B6EA3D9CC231A6CE0C08AA0504 "点击放大")

在Call Trees页签，可以通过底部的**Flame Chart**切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/HZdol2hoQoGWePdpqKL5-A/zh-cn_image_0000002779407464.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF968330FDEB72F4AA516A89DECE00D5D3DC9E07E32BB6060D5E829B97310CDC "点击放大")
