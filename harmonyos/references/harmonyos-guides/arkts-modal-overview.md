---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-overview
title: 绑定模态页面概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 绑定模态页面 > 绑定模态页面概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:242068d07dcaf1b1fd501e9b6598c440e187b13c2f745bea2f68d996e2024abc
---

模态页面是一种大面板交互式的弹窗，和其他弹窗组件一样，通常用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作。相比于其他弹窗组件，模态页面的内容都需要开发者通过自定义组件来填充实现，可展示的视图往往也很大。默认需要用户进行交互才能够退出模态页面。ArkUI当前提供了**半模态**和**全模态**两类模态页面组件。

* **​半模态：​**开发者可以利用此模态页面实现多形态效果。支持不同宽度设备显示不同样式的半模态页面。允许用户通过侧滑，点击蒙层，点击关闭按钮，下拉关闭半模态页面。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/DZ1fMDByS1GD98IOd56kLA/zh-cn_image_0000002558604756.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052757Z&HW-CC-Expire=86400&HW-CC-Sign=64B7CECBA2DC22AAA83B4DA0F0BCB3624C1B598A33AADF95535572369E89062C)
* **全模态：​**开发者可以利用此模态页面实现全屏的模态弹窗效果。默认需要侧滑才能关闭。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/YyKQHQCnR5y4PALiDb3APQ/zh-cn_image_0000002589324281.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052757Z&HW-CC-Expire=86400&HW-CC-Sign=7FEEECAC6F27E8E43B0A70FFC57441814619E86015686135451C22C7F2D91361)

## 使用场景

| 接口 | 使用场景 |
| --- | --- |
| [bindContentCover](arkts-contentcover-page.md) | 用于自定义全屏的模态展示界面，结合转场动画和共享元素动画可实现复杂转场动画效果，如缩略图片点击后查看大图。 |
| [bindSheet](arkts-sheet-page.md) | 用于半模态展示界面，如分享框。 |
| [openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)/ [updateBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#updatebindsheet12)/ [closeBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#closebindsheet12) | 用于不依赖UI组件的场景，如全局拉起、更新、关闭。 |

## 规格约束

* 建议使用UIContext中的弹窗方法。其他规格约束可参考[openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)、[updateBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#updatebindsheet12)、[closeBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#closebindsheet12)说明。
