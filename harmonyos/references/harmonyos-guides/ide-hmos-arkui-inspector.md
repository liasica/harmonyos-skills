---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e34799290dc9a7c5a51c3190d7b278cce19b5f0a3e2c830fff0c50e43205c7cf
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

1. 在DevEco Studio右侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/l-swsKxXRiWw7qFME-LbUA/zh-cn_image_0000002779728895.png "点击放大")图标展开ArkUI 界面检查器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/39j5fBvzT5ieWbv4Yuc1Uw/zh-cn_image_0000002750169726.png)
2. 在设备应用列表选择要查看的设备和设备上的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ehWV3dlQSfyizcPpjieE3g/zh-cn_image_0000002750009830.png)
3. ArkUI 界面检查器上方区域显示当前设备的UI界面，左下方区域为当前的组件树结构，右下方区域为选中组件的属性信息。

   可以在左下方区域组件树上或在上方UI界面点击选择组件。当设备上UI发生变化时，可点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/5Pvb8_edS6mL7GgUsqBwDg/zh-cn_image_0000002779608745.png "点击放大")按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/xK-_S35wREeTbxu5pQ81cg/zh-cn_image_0000002779608743.png)
4. 点击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/8GjkV6_6Tyeqklb-79V1rQ/zh-cn_image_0000002779728901.png)按钮，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/phzzVo2ySBmEASlTxZxleg/zh-cn_image_0000002750169730.png)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/idAK5nyNQ9-pgrKInOBuyA/zh-cn_image_0000002750169722.png)，勾选**显示统计数据**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/92mYVV2gRgqaw5R-1WgCvg/zh-cn_image_0000002779728899.png)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/sy0JeC7oRsqLg4xxXQw9ZQ/zh-cn_image_0000002779728897.png)，勾选**显示隐藏组件**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/gvBlkBBPSySYK5FQA8IrTw/zh-cn_image_0000002779728903.png)

## UI组件源码跳转

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/gviRnNuqT1-X8fDEB8yUSg/zh-cn_image_0000002750169724.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧编辑![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/m9WQXYqBRJG_2VrjMOOpIQ/zh-cn_image_0000002750009828.png)按钮打开配置界面。在**通用**中，勾选**启用源码行跳转**，重新运行工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ExsWN9aiRDelGrMGXPl41A/zh-cn_image_0000002750169732.png)
2. 在ArkUI 检查器中，选中要进行源码跳转的UI组件。点击右下方的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/sj_JrNm7SGeFjk1hQk3FBw/zh-cn_image_0000002779608741.png)

## 显示布局边框

点击组件数上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ZQSt77XLSHG4gAjuIiLKaw/zh-cn_image_0000002750009832.png "点击放大")按钮，可显示当前页面组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/b0bFFRVyQHqQ8GKBkQ521A/zh-cn_image_0000002750009834.png)

## 查看UI组件的状态变量

点击组件，可以查看组件的状态变量，以及状态变量影响的下一层组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Jsb9pekcQUSStbyS46gshA/zh-cn_image_0000002750169728.png)
