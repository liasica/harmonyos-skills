---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-arkui-inspector
title: 查看应用组件树
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 查看应用组件树
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:043f80c1d16940cc80b6d6fed6c5add7eb200c00f4f59f11ca430398f97bf7e0
---

开发者可以在多设备预览器中从运行模式切换至预览模式，实时查看当前应用所对应的组件树，并支持跳转至对应代码，快速分析定位UI界面存在的问题。

预览模式支持的功能包括：

* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* UI组件源码跳转，选中UI组件后点击源码跳转按钮即可跳转至源码位置。

## 使用约束

* 跳转代码需要启用源码行跳转功能，启用方法请参考[UI组件源码跳转](ide-hmos-arkui-inspector.md#section44774145517)。

## 操作步骤

1. 点击多设备预览器界面下方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/KfVP_ElYQEa25nSJBN9UkQ/zh-cn_image_0000002810750713.png)图标进入预览模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/sjOLY3RRRwO14-gDoxKI3A/zh-cn_image_0000002810630605.png)
2. 在预览界面中可以查看当前页面的组件树和各个属性，支持组件搜索，展开和折叠组件树。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4LOr7eHfS0ScqMP2pAPA-g/zh-cn_image_0000002810630603.png "点击放大")
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/agamsllwTBysgLcXupqbvQ/zh-cn_image_0000002781471052.png)图标，勾选**显示统计数据**，可显示组件树节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/8GCKR7x9T4Cht1SB1RM4hg/zh-cn_image_0000002810630601.png "点击放大")
4. 选择要进行源码跳转的UI组件，在组件属性详情面板显示源码跳转链接，点击链接即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/1i_qtbuOQO6UHD0IqfR1aw/zh-cn_image_0000002810750711.png "点击放大")
