---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-immersive-light-sense-overview
title: 沉浸光感简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 沉浸光感 > 沉浸光感简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:18+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:7045c49b237ee0e874afa0ba1f4291ab61d2c3ba0c4e72d0f4d500c248940530
---

从API版本26.0.0开始，ArkUI新增沉浸光感。

沉浸光感是ArkUI提供的一套从“视觉层”到“感知层”的体验，将光影材质与交互动效表现相结合，帮助应用建立清晰的视觉层次，并在不同设备上保持和谐一致的观感。例如：用户展开菜单时，伴随着形变弹出打破生硬的规整边界，边缘流光勾勒着面板轮廓，将菜单的弹出操作转化为富有沉浸感的体验。

沉浸光感包含两部分能力：

* **沉浸式系统材质**：为组件赋予轻盈通透的质感，让内容透过系统材质层自然渗透，配合折射、高光、阴影等多层效果，使弹窗、菜单、工具栏等浮层元素在内容之上建立清晰的视觉层次。系统提供从超薄到超厚的五种材质样式，覆盖从浮动工具栏到弹窗的不同透光需求。
* **沉浸式空间动效**：为弹窗和菜单的弹出过程增添形变、流光等动态表现，让每一次弹出都灵动自然。

沉浸光感会根据设备算力和用户在系统中设置的沉浸光感效果，自适应地调整沉浸式系统材质和沉浸式空间动效的表现程度，其中算力档位由设备定义且固定，可通过获取材质等级接口（[uiMaterial.getGlobalMaterialLevel](../harmonyos-references/arkts-apis-uimaterial.md#uimaterialgetglobalmateriallevel)）查询；用户在系统中不同设置下的沉浸光感效果请参考[用户体验与个性定义](../design-guides/immersivelight-0000002612101053.md#section11153104616255)。沉浸式系统材质还会随系统深浅色模式自动切换效果，确保应用在不同使用环境下都能呈现最佳效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/t2YhOAruToetS2Kkdn4asg/zh-cn_image_0000002736312817.gif)

## 关键技术

### 沉浸式系统材质

沉浸式系统材质为组件赋予轻盈通透的质感：材质滤镜、折射、高光、阴影等多层效果叠加，让底层内容透过材质层自然渗透，带来远超纯色背景的高端视觉表现。开发者只需[开启沉浸光感](arkts-immersive-light-sense-enable.md)，组件的背景、边框、阴影等视觉效果即由沉浸式系统材质统一接管，随深浅色模式与设备算力自动适配。

沉浸式系统材质提供从超薄到超厚的五种样式，不同样式的对比效果请参考[设计与开发](../design-guides/immersivelight-0000002612101053.md#section91711926192713)。开启沉浸光感后不同组件的默认样式存在差异，具体请参考[组件适配沉浸光感](arkts-immersive-light-sense-component-adaptation.md)。

| 样式 | 说明 | 适用场景 |
| --- | --- | --- |
| ULTRA\_THIN | 超薄样式，材质层具有很强的透明效果。 | 高度透明的背景，如浮动工具栏。 |
| THIN | 薄样式，材质层具有较强的透明效果。 | 较强透明度的场景，如搜索框。 |
| REGULAR | 常规样式，材质层厚度常规。 | 通用场景。 |
| THICK | 厚样式，模糊效果强。 | 较强模糊背景的场景，如菜单。 |
| ULTRA\_THICK | 超厚样式，模糊效果很强。 | 完全模糊背景的场景，如弹窗。 |

此外，沉浸式系统材质还支持材质赋色、自动反色、阴影开关、交互形变与点光源等个性化配置，具体使用方法请参见[沉浸式系统材质视效](arkts-immersive-light-sense-common-capability.md)。

### 沉浸式空间动效

沉浸式空间动效，将光的行为凝练为三种相互呼应的动效类型，具体请参考下表。沉浸式空间动效会根据设备算力与用户在系统中设置的沉浸光感效果自适应调整，开发者无需额外适配。

| 动效类型 | 说明 | 支持的组件 |
| --- | --- | --- |
| 非线性形变 | 实现光影形体的动态蜕变，打破规整边界带来柔和自然的空间过渡。 | AlertDialog，具体示例请参考[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-alert-dialog-box.md#示例9设置弹窗的沉浸光感效果)  CustomDialog，具体示例请参考[示例14（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-custom-dialog-box.md#示例14设置弹窗的沉浸光感效果)  ActionSheet，具体示例请参考[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-action-sheet.md#示例9设置弹窗的沉浸光感效果)  菜单控制，具体示例请参考[示例24（设置菜单的沉浸光感）](../harmonyos-references/ts-universal-attributes-menu.md#示例24设置菜单的沉浸光感) |
| 边缘流光 | 流光塑造视觉焦点与层级秩序，依靠光流走向引导用户的视线流转。 | AlertDialog，具体示例请参考[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-alert-dialog-box.md#示例9设置弹窗的沉浸光感效果)  CustomDialog，具体示例请参考[示例14（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-custom-dialog-box.md#示例14设置弹窗的沉浸光感效果)  ActionSheet，具体示例请参考[示例9（设置弹窗的沉浸光感效果）](../harmonyos-references/ts-methods-action-sheet.md#示例9设置弹窗的沉浸光感效果)  菜单控制，具体示例请参考[示例24（设置菜单的沉浸光感）](../harmonyos-references/ts-universal-attributes-menu.md#示例24设置菜单的沉浸光感) |
| 粒子动画 | 粒子承载信息具象表达，以粒子光点传递信息变化。 | Slider参考[示例10（设置滑动条的沉浸光感效果）](../harmonyos-references/ts-basic-components-slider.md#示例10设置滑动条的沉浸光感效果) |

## 约束与限制

沉浸光感生效范围请参考[开启沉浸光感](arkts-immersive-light-sense-enable.md)。

沉浸光感开启后，除了弹窗类组件或方法、Slider、Toggle，其他组件仅在以下区域中生效：Navigation/NavDestination标题栏，或横向Tabs中barPosition为BarPosition.End的底部TabBar中。

弹窗类组件或方法包括：Popup、Tips、Menu、BindSheet、showActionMenu、AlertDialog、CustomDialog、ActionSheet、CalendarPickerDialog、DatePickerDialog、TextPickerDialog、TimePickerDialog、Toast、Select、AlphabetIndexer气泡弹窗、Text设置copyOption后长按或双击触发的文本菜单、SelectionMenu（结合bindSelectionMenu一起使用）。

## 与相关Kit的关系

[UI Design Kit](ui-design-introduction.md)同样提供了沉浸光感能力，但其适用范围与ArkUI存在差异：

* UI Design Kit：支持HDS导航和HDS底部页签两个组件的沉浸光感能力，开发者可以通过[TitleBarStyleOptions](../harmonyos-references/ui-design-hdsnavigation.md#titlebarstyleoptions)或[HdsTabsFloatingStyle](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)的systemMaterialEffect设置沉浸光感视效，具体请参考[UI Design Kit](ui-design-introduction.md)下的[沉浸光感](ui-design-hds-component-material.md)。
* ArkUI：沉浸光感生效范围请参考[开启沉浸光感](arkts-immersive-light-sense-enable.md)。

开发者可以根据实际需求选择，如果应用使用HDS导航和底部页签组件，可以直接通过UI Design Kit快速开启沉浸光感；如果需要为更多组件或弹窗类组件添加沉浸光感效果，则使用本文介绍的ArkUI沉浸光感能力。
