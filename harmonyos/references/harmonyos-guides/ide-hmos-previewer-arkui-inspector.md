---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-arkui-inspector
title: 查看应用组件树
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 查看应用组件树
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a209ea3194082e567d65db0722905621e93bdbe134b76d59f911e3d2065fcfce
---

开发者可以在多设备预览器中从运行模式切换至预览模式，实时查看当前应用所对应的组件树，并支持跳转至对应代码，快速分析定位UI界面存在的问题。

预览模式支持的功能包括：

* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* UI组件源码跳转，选中UI组件后点击源码跳转按钮即可跳转至源码位置。

## 使用约束

* 跳转代码需要启用源码行跳转功能，启用方法请参考[UI组件源码跳转](ide-hmos-arkui-inspector.md#section44774145517)。

## 操作步骤

1. 点击多设备预览器界面下方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/LtI7DepXTai2iCHuh5-YSw/zh-cn_image_0000002779608609.png)图标进入预览模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/8rcqX7UORZisw3OCJOnUwQ/zh-cn_image_0000002750169584.png)
2. 在预览界面中可以查看当前页面的组件树和各个属性，支持组件搜索，展开和折叠组件树。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/h_vpoSrMRhqotZrtsg4I8g/zh-cn_image_0000002779728757.png "点击放大")
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/18huNih1QX6ZkHSvo1hGQw/zh-cn_image_0000002750009698.png)图标，勾选**显示统计数据**，可显示组件树节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/4atrMR7EQrSBOGJXBe1igA/zh-cn_image_0000002779728759.png "点击放大")
4. 选择要进行源码跳转的UI组件，在组件属性详情面板显示源码跳转链接，点击链接即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dOA6KOJmSy-mECjlyQ-0uw/zh-cn_image_0000002750009696.png)
