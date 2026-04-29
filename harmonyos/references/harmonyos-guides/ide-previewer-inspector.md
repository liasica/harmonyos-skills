---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-inspector
title: Inspector双向预览
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > Inspector双向预览
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:33+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:9c2813530ed15ae7a0dd5ff3e474299cb2df990b3706f2ccc686c6c48577be14
---

DevEco Studio提供HarmonyOS应用/元服务的UI预览界面与源代码文件间的双向预览功能，支持ets文件与预览器界面的双向预览。使用双向预览功能时，需要在预览器界面单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Vn5PjFYSTsCEKpp0fzFejw/zh-cn_image_0000002561832897.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=1EE6E774396EC8362847EF021D7AE857EB0ACB286A68C6D894777E7E6104B7E5)图标打开双向预览功能。

说明

不支持服务卡片的双向预览功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/m0OjxXA5RJ-s1BjRDaeB6w/zh-cn_image_0000002561752913.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=8D0C2D8CE329DB94F09CE1BCC8C821CA6CC1272251AAC74A4DACFB3829DDB6A9 "点击放大")

开启双向预览功能后，支持代码编辑器、UI界面和Component Tree组件树三者之间的联动：

* 选中预览器UI界面中的组件，则组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
* 选中布局文件中的代码块，则在UI界面会高亮显示，组件树上的组件节点也会呈现被选中的状态。
* 选中组件树中的组件，则对应的代码块和UI界面也会高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Hl1CndvqROGijlgjp4KwIQ/zh-cn_image_0000002530912970.png?HW-CC-KV=V1&HW-CC-Date=20260429T054632Z&HW-CC-Expire=86400&HW-CC-Sign=A81FC7CCDDCC77465232D328B88FB39CF67432B6392FDE41F37306D8BACFE886 "点击放大")

在预览界面还可以通过组件的属性面板修改可修改的属性或样式，在预览界面修改后，预览器会自动同步到代码编辑器中修改源码，并实时的刷新UI界面；同样的，如果在代码编辑器中修改源码，也会实时刷新UI界面，并更新组件树信息及组件属性。

说明

* 如果组件有做数据绑定，则其属性不支持在属性面板修改。
* 如果界面有使用动画效果或者带动画效果组件，则其属性不支持在属性面板修改。
* 多设备预览时，不支持双向预览。
