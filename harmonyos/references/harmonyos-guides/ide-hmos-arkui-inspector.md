---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-arkui-inspector
title: 布局分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 布局分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c18633f00f8fafa2ac17f5abc7f1a3d6db127d1d9cd9790f9527b2bf218eb415
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

1. 在DevEco Studio右侧边栏点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/sawnrH1XQmq_RkAH8-QfUA/zh-cn_image_0000002810630751.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E384B4E10464425AF5E2901523746E501AD6D3A8E2819414314ED4A42AB57FA "点击放大")图标展开ArkUI 界面检查器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/LuTxXmFISTKT4R4BRGzSRw/zh-cn_image_0000002810630755.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=64F3FBD87B8D366391C75F34B948535BE8EEF0E5895629C2DDB605E4CC9DA8D8)
2. 在设备应用列表选择要查看的设备和设备上的进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/b43t81VISlWc0iL8MbISUw/zh-cn_image_0000002810630747.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7E3D30EC36584F460258AE3B37F05062CED681F12C7D9F481A0F1B313EAC849)
3. ArkUI 界面检查器上方区域显示当前设备的UI界面，左下方区域为当前的组件树结构，右下方区域为选中组件的属性信息。

   可以在左下方区域组件树上或在上方UI界面点击选择组件。当设备上UI发生变化时，可点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/JB-EkZKPSRCE5EVf5WFhQw/zh-cn_image_0000002781311266.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6A93812911285D5B605F653113FD41474C9367C32C2BC7110B4086E97ADCD60 "点击放大")按钮同步设备上的UI效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/6hkxBad7QWCuJrh31ogMSA/zh-cn_image_0000002810750855.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=05C47A2ECED5B3516B8E46C0AE18DA22CA5C1F0CA3FE3FDAB1694749CF3F90EE)
4. 点击右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/RXHXogaPRkSWHJPedF8Fsw/zh-cn_image_0000002810630757.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=78D9E2B642F200853A1CCD29F47E82991565E891D6B4B0F050E643F3C1352594)按钮，可断开与设备的连接。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/CVcbWnfcR6KikSG-15GocA/zh-cn_image_0000002781311272.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A620F87D2C014073D30C2ED701073EF4873C527367FE99E9BA83D026FCB89E8)

## 显示组件信息

* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/bJkK0zaiQY2KlxlUiAMGew/zh-cn_image_0000002810630749.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=09CCB3CE8FE294CCBCF7824695207F0FF33B5DF6D45D4DD04E56D01383EC1A6C)，勾选**显示统计数据**，可显示组件树组件信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/GDrFREQXQYOOZXK0tn8uvQ/zh-cn_image_0000002810750863.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=74E7C23AE0615CDBEE47AEBF051124820A77772B532036835468049A5CBF0237)
* 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/bd0D5GEkQPu7Y-EjxqEEfg/zh-cn_image_0000002810750861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9E681786AFE882651C2EAEC75FB04F86E9E490618C68A43C2CD447DD91E7D93)，勾选**显示隐藏组件**，可显示隐藏的组件。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/3G4KJw9xRFK5we4LyppHRA/zh-cn_image_0000002810750865.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=13F5A9CCCC9758B84F400632D8ACE7B2432D5E98B3DDACC95FEA60828DD3F2EF)

## UI组件源码跳转

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/NcSq-tm9TM2viCrHdmeSgg/zh-cn_image_0000002810750859.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=583485F83DEFE2095F8EDFC0D51E37BA9C268C6467D7A1F1228C729DA4B4EAAA)按钮，在菜单中点击**Application**并选择相应模块，点击右侧编辑![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/IZi15-l9Rha_1GlSB2ZeqQ/zh-cn_image_0000002810630745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A899B309EAAA0AF74245A3EB7131E212D0646F03DE999EEE66DD57494FA5D0C)按钮打开配置界面。在**通用**中，勾选**启用源码行跳转**，重新运行工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/xm8Lw3VKTq6ncmITyJTjHw/zh-cn_image_0000002781471206.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE82760EE16807738C6E878C92D3EC070C3CA683327401A98A41A8F019F9E96B)
2. 在ArkUI 检查器中，选中要进行源码跳转的UI组件。点击右下方的源码跳转，即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/4VlwB-J9Q1yJyqUYBXflMA/zh-cn_image_0000002810750853.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2003C87F3D3F163E0650635B2AE04EC32FFA4F9B4BA1701D554578B6C7541FB)

## 显示布局边框

点击组件数上方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/7uCGpI7nSracQ7OfdEo9Hw/zh-cn_image_0000002810750857.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=8241FC7E3C5D8A844CB818E783014AC0481F89D3678DC600AD12A73ABC3A237C "点击放大")按钮，可显示当前页面组件的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/xL7Ol65rSXiAqvbAuEr6dw/zh-cn_image_0000002810630753.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=32522FB9628C96D087A0087A25740BFF3CE55AD184FE2D107F467859B1B23DA6)

## 查看UI组件的状态变量

点击组件，可以查看组件的状态变量，以及状态变量影响的下一层组件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/is4mFF6eTYiQDBX0EfOQWw/zh-cn_image_0000002781471204.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=83EE092B4F56A1AA46A533F004314C6F65044867693C86B57B84E0769AC053CF)
