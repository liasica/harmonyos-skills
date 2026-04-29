---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-data-filtering
title: 内存分析数据筛选
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 内存分析数据筛选
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b083410590202eff8051baa7751b617fabb5b1191f98fe83309e3435bac86f88
---

Allocation分析过程中提供多种数据筛选方式，方便开发者缩小分析范围，更精确地定位问题所在。

## 通过内存状态筛选

从DevEco Studio 6.0.2 Beta1版本开始，支持对Native Allocation泳道、Graphic Memory泳道的内存状态信息进行过滤。

从DevEco Studio 6.1.0 Beta1版本开始，支持对All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道

Graphic Memory泳道的内存状态信息进行过滤，便于开发者定位内存问题。

在泳道“Detail”区域左下方的下拉框中，可以选择过滤内存状态：

* All Allocations：详情区域展示当前框选时间段内的所有内存分配信息。
* Created & Existing：默认选中，详情区域展示当前框选时间段内分配未释放的内存。
* Created & Released：详情区域展示当前框选时间段内分配已释放的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/w6t0onm_QQCkNQ8mWz74WA/zh-cn_image_0000002530753792.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=5568CADD5437E6AB67D3E6B52F25E116DA03DADAEEC5FE522A9A0F166ADB4ABF "点击放大")

## 通过统计方式筛选

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的“Statistics”页签中，可以打开“Native Size”选择统计方式以过滤统计数据：

* Native Size：详情区域按照对象的内存进行展示。
* Native Library：详情区域按照对象的so库进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/rdiB-B7eSdOCntEbjy3_1A/zh-cn_image_0000002561753729.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=BF0A6848B4AC52ACCC388E4737B085C7EB7721486F6A913C9DB260E9308F27BD "点击放大")

## 通过so库名筛选

非统计模式下，在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的“Allocations List”页签中，可以单击“Click to choose”选择要筛选的so库以过滤出与目标so库相关的数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/6cZiGQcOTIScg5W3unsj8g/zh-cn_image_0000002561833705.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=59E44C5546DC03631A8FE7695FB8B4C6868E20ED08CBBE19127A413B32562F72 "点击放大")

## 通过搜索筛选

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的页签中， 根据界面提示信息输入需要搜索的项目，可定位到相关内容位置，使用搜索框的<、>按键可依次显示搜索结果的详细内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/3UbVdMXjRo66_pxxOD82Lw/zh-cn_image_0000002561833709.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=8D92E649784062761367AC4D88E0A80CF57E769BAF0C1F83E3FAA08B06C62500 "点击放大")

## 筛选内存分配堆栈

在All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道、System Resources泳道、Graphic Memory泳道的Call Trees页签中，可以通过底部的“Call Trees”和“Constraints”选择框筛选和过滤内存分配栈。

Call Trees选择框包含两种过滤条件：

* Separate by Allocated Size：在内存分配栈完全相同的情况下，会按照每次分配栈申请的内存大小将栈分开；System Resources泳道中不包含该过滤条件；
* Hide System Libraries：隐藏内存分配栈中的系统堆栈。

说明

“Category”字段表示函数调用类型，将调用栈类型归类如下：

* ArkTS：程序正在执行ArkTS代码；
* NAPI：程序正在执行的NAPI代码；
* Native：程序正在执行的Native代码；
* Native(G)：程序正在执行的Native代码所申请的Global Handle对象，DevEco Studio 6.1.0 Beta2版本新增；
* Native(L)：程序正在执行的Native代码所申请的Local Handle对象，DevEco Studio 6.1.0 Release版本新增；

  其中每一个类型的亮色和灰色分别代表开发者和系统的代码。其中，亮色代表开发者自定义的代码，灰色代表直接使用模板中代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/7-zw9bzET2y3UFLSbu2gew/zh-cn_image_0000002530913782.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=1B77FAD9D31A543481C3EBD8535F48EF02B7239C4D11FFC09BF2E681343CBE46 "点击放大")

Constraints选择框也包含了两种过滤条件：

* Count：根据指定的内存申请次数过滤内存分配栈信息；
* Bytes：根据指定的内存申请大小过滤内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/rof-8FxZS1K3GMNYpsNdUA/zh-cn_image_0000002530753788.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=E9B7F676FB587740205DE351576CAA2B50D0C5D96BA90004CE18027BC5C2641C "点击放大")

在Call Trees页签的More区域，单击“Heaviest Stack”旁的隐藏按钮可以单独控制是否显示More区域最大内存分配栈中的系统堆栈。System Resources泳道中不包含Bytes字段。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/88qFgKdjRBqlx_E-iq3PjA/zh-cn_image_0000002530913778.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=C0AF9979528804BD07E11945343ECD2987307378D99F30896EB567C4CE79D53F "点击放大")

在Call Trees页签，可以通过底部的“Flame Chart”切换到火焰图视图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/U8HeQ-S5Qfmf-bFPBxt5cg/zh-cn_image_0000002561753725.png?HW-CC-KV=V1&HW-CC-Date=20260429T054733Z&HW-CC-Expire=86400&HW-CC-Sign=762ACE65A8FDD519144D859CC90CB03E41E58C2805123F31F7BA99CF26AC5A97 "点击放大")
