---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-arkui-inspector
title: 查看应用组件树
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 查看应用组件树
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:7340b6820d70eb9d94115e4db0943ec451f4b614243a9f569c1859ef9d87bb5e
---

开发者可以在多设备预览器中从运行模式切换至预览模式，实时查看当前应用所对应的组件树，并支持跳转至对应代码，快速分析定位UI界面存在的问题。

预览模式支持的功能包括：

* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* UI组件源码跳转，选中UI组件后点击源码跳转按钮即可跳转至源码位置。

## 使用约束

* 跳转代码需要启用源码行跳转功能，启用方法请参考[UI组件源码跳转](ide-hmos-arkui-inspector.md#section44774145517)。

## 操作步骤

1. 点击多设备预览器界面下方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/8blYfYVuTsyxKyCBPJMaCA/zh-cn_image_0000002810750713.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACA59625A7C1A4235CD573470BCC72028DE6B135284B1EB5C7DF649DACF051AC)图标进入预览模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/1DURf7rIQiOZGlOn_mm2kg/zh-cn_image_0000002810630605.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=94B480194B0A1421EFB44BCD6736B213CF40E287D8CA50A4F163D4E046AE1B21)
2. 在预览界面中可以查看当前页面的组件树和各个属性，支持组件搜索，展开和折叠组件树。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Sm9efPXJQ5aWTB1X6EmoHQ/zh-cn_image_0000002810630603.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F46B8842A23E462898AAEC799D2C48F6A0310279EAB4F97E64AF52230DB8155 "点击放大")
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CPxf5pAFSoC7eC8K64TfwQ/zh-cn_image_0000002781471052.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=2587EF2311C85E1FDD0824FF7952F78055DB3D298771B30778FC4BD22BFB2356)图标，勾选**显示统计数据**，可显示组件树节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/e8WUNArSRGqykR0yWBKoaw/zh-cn_image_0000002810630601.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=100373F64F31970D888AFBB5F9F7FC915F742114BE08FF859E8987CEC588E231 "点击放大")
4. 选择要进行源码跳转的UI组件，在组件属性详情面板显示源码跳转链接，点击链接即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Kxu-N_XYQ72-4o170Tujfw/zh-cn_image_0000002810750711.png?HW-CC-KV=V1&HW-CC-Date=20261114T004727Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BE6F0F3A0738E572151D4E2B457F7E8893B14D6C8B50D6DD1124F6682D608E0 "点击放大")
