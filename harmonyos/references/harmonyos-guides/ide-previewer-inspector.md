---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-inspector
title: Inspector双向预览
breadcrumb: 指南 > 编写与调试应用 > 界面预览 > Inspector双向预览
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:1b5f36be1366b454de44d507790187a6f3869986ae2a465c03872ef15a3b5466
---

DevEco Studio提供HarmonyOS应用/元服务的UI预览界面与源代码文件间的双向预览功能，支持ets文件与预览器界面的双向预览。使用双向预览功能时，需要在预览器界面单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/lXJ7PXumQOaZO-b4lo4btw/zh-cn_image_0000002701822900.png)图标打开双向预览功能。

**说明** 

不支持服务卡片的双向预览功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/nLL_53xRTa-5nmt5h8GkzA/zh-cn_image_0000002731382201.png "点击放大")

开启双向预览功能后，支持代码编辑器、UI界面和组件树三者之间的联动：

* 选中预览器UI界面中的组件，则组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
* 选中布局文件中的代码块，则在UI界面会高亮显示，组件树上的组件节点也会呈现被选中的状态。
* 选中组件树中的组件，则对应的代码块和UI界面也会高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/qcfP-o2GQoCY69m_KFMDRA/zh-cn_image_0000002701662976.png "点击放大")

在预览界面还可以通过组件的属性面板修改属性或样式，修改后，预览器会自动同步到代码编辑器中修改源码，并实时刷新UI界面；同样的，在代码编辑器中修改源码，也会实时刷新UI界面，并更新组件树信息及组件属性。

**说明** 

* 如果组件有做数据绑定，则其属性不支持在属性面板修改。
* 如果界面有使用动画效果或者带动画效果组件，则其属性不支持在属性面板修改。
* 多设备预览时，不支持双向预览。
