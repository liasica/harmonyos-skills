---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-previewer-arkui-inspector
title: 查看应用组件树
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 使用多设备预览器运行应用 > 查看应用组件树
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:45+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cd8148439b60e604c7978c6fb94ea4c8e4cd3d80d0824e3b619474edbde77990
---

开发者可以在多设备预览器中从运行模式切换至预览模式，实时查看当前应用所对应的组件树，并支持跳转至对应代码，快速分析定位UI界面存在的问题。

预览模式支持的功能包括：

* 在组件树上选择组件，UI界面自动框选对应组件，属性列表显示当前组件的属性信息。
* 在UI界面点击选择组件，组件树对应组件变化为选中状态，属性列表显示当前组件的属性信息。
* UI组件源码跳转，选中UI组件后点击源码跳转按钮即可跳转至源码位置。

## 使用约束

* 跳转代码需要启用源码行跳转功能，启用方法请参考[UI组件源码跳转](ide-hmos-arkui-inspector.md#section44774145517)。

## 操作步骤

1. 点击多设备预览器界面下方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/K0sKVtsMTWiUh3QWtlCOmg/zh-cn_image_0000002791840982.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A17581FFF02126A02A829731D82D05E032A8445C6FC3640C7C1F6090C68EAE9)图标进入预览模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/jOZowuipThegPkBtHWAmxA/zh-cn_image_0000002792000952.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=04338092A4B7A3DCB62C8ED9FE9385052FC135F60575DFC2271746076C182365)
2. 在预览界面中可以查看当前页面的组件树和各个属性，支持组件搜索，展开和折叠组件树。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/j4TFEhQZQF-32d2mEIRKgg/zh-cn_image_0000002820680917.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=57799280EA3B031CE176BD62E1C4BC6C30E653B06C58526261D008F66984D707 "点击放大")
3. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/bPNurVu2STOnt_6KUOQMBQ/zh-cn_image_0000002791840986.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=A43056A6777F16006EF6722E843FE682E3CD9E0B744AC54F5A9DFB6B6431CC1E)图标，勾选**显示统计数据**，可显示组件树节点信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/TzrfLFi8SByoCHQpF-ggdg/zh-cn_image_0000002820720921.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=96B842BE81463F1A383055E5526E2F975BE2B87D252FA2D2B36F4AAD98AA2ECC "点击放大")
4. 选择要进行源码跳转的UI组件，在组件属性详情面板显示源码跳转链接，点击链接即可跳转到UI组件源码位置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/BFEtSbAKTumSmuqHDSPMIw/zh-cn_image_0000002820720919.png?HW-CC-KV=V1&HW-CC-Date=20261124T044245Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F72534DF6C0B5F3B1B194E7F23EEDCAA97AAD2A166969CEF22776CA22E5505A "点击放大")
