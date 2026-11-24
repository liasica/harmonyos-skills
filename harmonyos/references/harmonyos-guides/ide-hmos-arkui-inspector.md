---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:db2488422cafd3932c5e576098fd3ef0cdf7ef80ee4a3e18335e70e52c5b9f2b
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

1. 在DevEco Studio右侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/5kgTgdgkTLKpobcNyXZn9w/zh-cn_image_0000002792001126.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E1B9C74A854DFCB4A3401D9E9115B4E9CDCB01628EFE0D57F571405FEA2DD38 "点击放大")图标展开ArkUI 界面检查器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/mi0oZq-LScyFeie8Xjf6Vg/zh-cn_image_0000002820681085.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E62460E993E30D5F036B377701B004DEB6E7CF723952BD12E322B255ED6A946)
2. 在设备应用列表选择要查看的设备和设备上的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/IABPzS0GTziweDn-xqmRSQ/zh-cn_image_0000002820721089.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCCC1EFE705296345CE352E1A9B361E006BECB131D618867A3091E3635102AA9)
3. ArkUI 界面检查器上方区域显示当前设备的UI界面，左下方区域为当前的组件树结构，右下方区域为选中组件的属性信息。

   可以在左下方区域组件树上或在上方UI界面点击选择组件。当设备上UI发生变化时，可点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/J-BEoSZ7TzqZYAZNIlZ-rg/zh-cn_image_0000002792001122.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=6079136D25A92678F04464AC1B689E4A4563874BCD3C2B2C5597AF8CA9583EF6 "点击放大")按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/ZQfcWFNYSsuRyV_08gAeZw/zh-cn_image_0000002792001120.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAB86D1151B02C2D645465ADFB1E8A553E963494543E46FD0CDA6312405F0D26)
4. 点击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ObzajXG7TDai66G1cbjsXw/zh-cn_image_0000002791841150.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=61C7D37A33CACDD302D773DA0E4D61F49A5772BA4E457E33A4AE4FE0DC5885EF)按钮，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/e7T3J91ES0KARh7VKm-MHw/zh-cn_image_0000002820721091.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=181042F19C3F26F56F1E52C60758B390AE2A2D6531D65EBC341D4E463A4FE436)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/FdFrvqJiSoO6yRrr9aoIZg/zh-cn_image_0000002820721087.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A73FEA04FB8260A5C3CED25408428ADC87726C0B426AB0AB63F845A8B14F017E)，勾选**显示统计数据**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/sFy-ofbiTwiEkNKaia12gQ/zh-cn_image_0000002820681079.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D976C85EDEB5997B36A219ED8BD97F47C80617ACCB9AD6B82FFFF92ED2D4B5AD)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/5KqHD1WSTd6r2IQEwf8IZA/zh-cn_image_0000002820721093.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C755A7CE196F1F9EE8C46A7FA8FB54E9560AD4D1A975A0A6A96FEF665D2D0D46)，勾选**显示隐藏组件**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/FfIy6ZOhSdCM1WkVPpo-Eg/zh-cn_image_0000002791841146.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=116EBCFEA12B5E86C698218C081B12DB08BCFE009C16401D456951CB362399F8)

## UI组件源码跳转

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/HPXfVuiYRtWbrKoUZ07jdA/zh-cn_image_0000002791841148.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0C68AD1A6B2E78815DE732AA651930F86092B1542D26EE75DC31F132D07F18D)按钮，在菜单中点击**Application**并选择相应模块，点击右侧编辑![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/-MKHmo27RDmxSEv6TR2OPA/zh-cn_image_0000002792001124.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=562891A9FB88E77DEA33C38EBED9E63D8F554A4E9862A96EED525270F0BBFF8F)按钮打开配置界面。在**通用**中，勾选**启用源码行跳转**，重新运行工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/hHPknCT3QzCxBTWvyYweug/zh-cn_image_0000002820681083.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=652FB86D8C832D0C33B373EC1F5C47656661E8265E3D8BFCF9D8EF16B52B9B7F)
2. 在ArkUI 检查器中，选中要进行源码跳转的UI组件。点击右下方的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/gCEhwfpOQMawL_hZKdcM5g/zh-cn_image_0000002820721085.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=C68C2AC06DC249D9D1AB404AD1EA6AE381F32DD478148FA35B4E6D6902722A39)

## 显示布局边框

点击组件树上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Y025loxTSj--Gjx5GjxtSw/zh-cn_image_0000002820681081.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=97E9D5445005C9A77AA464FF921F273A441A9038D1DF69DD62EE89DB8D69E647 "点击放大")按钮，可显示当前页面组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/ANXrGHeIRm2N0SrXdTJchg/zh-cn_image_0000002791841152.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF6E69D551D3E1000DD4E7CF50B0B720CF34A39E75D1959C9E1E18A3FF2B2CF4)

## 查看UI组件的状态变量

点击组件，可以查看组件的状态变量，以及状态变量影响的下一层组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/-LUFd1vuR7ad9-jdiEMcrw/zh-cn_image_0000002820681087.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=33CA63EEA92E3D528C32B930023B896CF396F1F2F16BC7B1F68613A0A6E72937)
