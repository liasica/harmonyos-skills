---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:ff8197cc5a2875f81efe11ca0ad86f2f583c58517c32cfd6b3eb3c50c8341f66
---

开发者可以使用ArkUI 界面检查器，在鸿蒙电脑DevEco Studio上查看应用在真机上的UI显示效果，并通过查看多次操作后的界面状态，快速分析定位UI界面存在的问题。

ArkUI 检查器支持的功能包括：

* [查看设备上应用的UI显示效果](ide-hmos-arkui-inspector.md#section754645394618)。
* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* [UI组件源码跳转](ide-hmos-arkui-inspector.md#section44774145517)，选中UI组件后点击源码跳转按钮即可跳转至源码位置。
* [查看当前页面上所有组件显示区域](ide-hmos-arkui-inspector.md#section141101548183310)。
* 在组件树上选择自定义组件，属性列表显示当前组件配置的[状态变量信息以及影响组件](ide-hmos-arkui-inspector.md#section1267731618213)。

## 使用场景

针对界面较复杂的应用：

* 通过组件树查看组件的父子关系，检查是否存在冗余组件。
* 针对应用在真机上运行出现UI界面显示异常，尤其经过多次界面复杂操作后产生的界面错误以及后台逻辑错误，进行问题分析定位。

## 使用约束

* 已连接设备并运行应用或启动调试。
* 仅支持查看运行在前台的应用。
* 仅支持全屏应用。
* 不支持应用市场上架的发布签名应用。

## 操作步骤

1. 在DevEco Studio右侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/dq7MaVrxTMCaB2uvJDibxA/zh-cn_image_0000002792001126.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9C00CDAC1FBA898DEBD0E91ABBE0C6260A505CD8F4CEF74409C2337126319FC "点击放大")图标展开ArkUI 界面检查器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/iYLA1FnKRBusDlK2ORoZmQ/zh-cn_image_0000002820681085.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF86E7AA3A96D8EF5AC88AB6FB269E1D6438310D51546BF6FFB26223A8D2EEFF)
2. 在设备应用列表选择要查看的设备和设备上的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/f-es62D_RbuMJRd7wXmr2A/zh-cn_image_0000002820721089.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=7629388E5E47B30BA425C86914C42A71FE913EB7BC106052278D5FCF49FE61E6)
3. ArkUI 界面检查器上方区域显示当前设备的UI界面，左下方区域为当前的组件树结构，右下方区域为选中组件的属性信息。

   可以在左下方区域组件树上或在上方UI界面点击选择组件。当设备上UI发生变化时，可点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/jpAQSzG9QAyMWtx9cUepew/zh-cn_image_0000002792001122.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=C84896D32CA56DE0B0E343F8903ACFCC99038BE5D4D71FAA9583B30FBFA75A48 "点击放大")按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/YiAy8G7LRjy7hs9bh6Ye0w/zh-cn_image_0000002792001120.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADC6D89326CAE60CAC4613A2E91E30D87D4E2E0539204960BD57B0189DCE3AE6)
4. 点击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/DHyBKg8CTzG4ZhHIcdGWvQ/zh-cn_image_0000002791841150.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=499749C3696B8EBABDE2BC4C856100F780E26BA4C737691FC744003DEB31DB6D)按钮，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/KBR6Ksc6RCaFxUSP8n5jKw/zh-cn_image_0000002820721091.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=36F4ADB46EBC99BC7B6A0C5991DEF5250326ECA56C92B281B0D9CF3CE5C216AD)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/80U7dOanQY-3p7-v18-9vA/zh-cn_image_0000002820721087.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CC881EEDEDBE03F39E2567EB148086238A44BD36F281DB9CDEEF64404E8767F)，勾选**显示统计数据**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/3F_MqLt-S9i22ylQvytYgQ/zh-cn_image_0000002820681079.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E2D3C257B9FF790A034A2CB915ED222B9A2EE8800C8E39B822DBA1BA428426B)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/tVSxzR2kRsmXw9P0D0ttsA/zh-cn_image_0000002820721093.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=182559B4208791C397EC57394AB94B7EB5B9F7EEDD593031AE1EB21A42350FED)，勾选**显示隐藏组件**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/paG0QVMrQDyvlhkj8ooslw/zh-cn_image_0000002791841146.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=27D3F7E97CB969E24D61E82D0C1D91A3540D4D629501B5F18D7361F9A8BE6CBE)

## UI组件源码跳转

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/0dC4ezmBRDeXZMW8hKoBlw/zh-cn_image_0000002791841148.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=E39BEA5278C8012A3DE5A6918379B1F94702DA16E463B8383402DD308E358D4A)按钮，在菜单中点击**Application**并选择相应模块，点击右侧编辑![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/CwiXSUbqRvOEIghPkExNmg/zh-cn_image_0000002792001124.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4B9E1F77F67F99C11778FEFD9E6597372540B16D554B002264F0E09672398A0)按钮打开配置界面。在**通用**中，勾选**启用源码行跳转**，重新运行工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/rNvsZlztTja_MKDqPitiOw/zh-cn_image_0000002820681083.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BBC800CD85E857134E9B5CBF89F91A157664D21B990FB8C0A580220A3990CD1)
2. 在ArkUI 检查器中，选中要进行源码跳转的UI组件。点击右下方的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/9oE8XubLQ1W7XGeKCQldAw/zh-cn_image_0000002820721085.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=388707B4281CDD1DB2E76E4D04775D32F34106841CDD8D61539D1355DBE624F6)

## 显示布局边框

点击组件树上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/DNXY62fYRmW9q8CQlh11lg/zh-cn_image_0000002820681081.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=136FB35EE1AB383B961330D8F7C7474345019D89626F46F9C33E087B562B411D "点击放大")按钮，可显示当前页面组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/BMUiQFS0R82QQ0zuLxjn0g/zh-cn_image_0000002791841152.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=48FE073CF8336891F4F54299D704F08409AA61417529AEB7ACA749D024DE6FEF)

## 查看UI组件的状态变量

点击组件，可以查看组件的状态变量，以及状态变量影响的下一层组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qf3youcsS-yE2Q-EPG4m-A/zh-cn_image_0000002820681087.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A9B0BBEFF01A54F16938347032BBCAB73B8DB138B4451469546B10B9D2D1D86)
