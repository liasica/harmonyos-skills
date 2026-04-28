---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-introduction
title: UI Design Kit简介
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > UI Design Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cca3bd4cf5318b2879b3b3dc119404b9e7bcac61913dcb534b2ad3e36023ae54
---

UI Design Kit是华为提供的符合HarmonyOS Design System规范的UI界面开发套件集合。通过提供多样式的扩展组件、丰富的光影效果，支撑开发者高效构建高端精致的界面（参见[HarmonyOS设计理念](../design-guides/design-concepts-0000001795698445.md)），确保应用在HarmonyOS全场景设备上达成一致的视觉体验与设计品质，遵循[HarmonyOS设计规范](../design-guides/general_overview-0000001929599380.md)。

| **扩展组件** | **光影效果** | **多设备适配** |
| --- | --- | --- |
| 多样化的组件样式 | 丰富UI界面光影 | 全场景一致体验 |

## 功能全景

### 增强型UI组件

| 组件分类 | 组件描述 |
| --- | --- |
| **[组件导航（HdsNavigation/HdsNavDestination）](ui-design-navigation-dynamic-blur.md)** | 提供HdsNavigation组件作为路由导航的根视图容器，HdsNavDestination作为子页面的根容器，实现灵活跳转操作；扩展标题栏交互，支持动态模糊与菜单气泡。 |
| **[侧边栏（HdsSideBar）](ui-design-sidebar-overlay-mode.md)与[侧边栏菜单（HdsSideMenu）](ui-design-side-menu.md)** | 侧边栏：提供可显隐的侧边栏容器，支持自定义内容区。  侧边栏菜单：配套菜单组件支持一、二级菜单样式及新消息红点提醒。 |
| **[底部页签（HdsTabs）](ui-design-hds-tabs-split-line.md)** | 支持视图切换，提供分割线动态显隐、背景模糊、图标出血及半屏居中布局等增强样式。 |
| **[即时操作（HdsSnackBar）](ui-design-snackbar-resident-notification.md)与[核心操作栏（HdsActionBar）](ui-design-actionbar-main-buttons.md)** | 即时操作：提供非模态通知组件，支持图文展示与快速操作按钮，用于轻量化交互反馈。  核心操作栏：组合多个按钮，支持主按钮展开/收起的联动动效。 |
| **[列表（HdsListItem）](ui-design-set-hds-slide-horizon-listitem.md)** | 封装高端卡片样式，内置横滑删除动效，适配多设备系统风格。 |
| **[应用内多窗（MultiWindowEntryInAPP）](ui-design-multiwindowentryinapp.md)** | 单应用多窗口入口，支持自定义图标、背板颜色与大小，实现多窗并行。 |

### HDS沉浸视效

| 光效功能 | 功能描述 |
| --- | --- |
| **[物理光感系统](ui-design-visual-effect-point-light.md)** | 提供点光源、边缘流光及背景流光。特有“自带背景双边流光”接口，完美适配胶囊组件与屏幕边缘发光场景。 |
| **[按压交互阴影](ui-design-visual-effect-background-color.md)** | 提供按压阴影接口，自动计算组件在按压交互时的背景色变化效果，增强触控真实感。 |
| **[沉浸光感材质](ui-design-hds-component-material.md)** | 提供HDS标题栏组件和底部页签组件的沉浸光感材质能力。提升组件层次感和空间感，带来更具沉浸式的视觉和交互反馈。 |

### 资源与图标能力

| 能力分类 | 能力说明 |
| --- | --- |
| **[应用图标处理](ui-design-layered-process.md)** | 支持单层或分层图标的合成、剪切、缩放及描边，提供高效的批量处理能力。 |
| **[自定义 Symbol](ui-design-custom-symbol-res-register.md)** | 支持注册应用侧图标与动效资源，配合 ArkUI 组件展示，保持系统级视觉一致性。 |

## 与ArkUI基础能力的关系

UI Design Kit的导航、页签、列表、光效、应用交互等能力是基于ArkUI以下能力维度的扩展。

| 能力维度 | ArkUI基础能力 | UI Design Kit能力 |
| --- | --- | --- |
| 组件导航 | 基础跳转 | **沉浸式体验**：动态模糊标题栏、半模态样式、标题栏自定义区域、文字/图片双类型图标等 |
| 底部页签 | 基础切换 | **视觉增强**：分割线动态显隐、页签栏模糊、图标出血设计、半屏居中对齐 |
| 列表交互 | 普通展示 | **高端动效：** 内置横滑删除、统一样式卡片、多设备适配 |
| 光影视觉 | 基础平面/材质 | **增强视效**：提供点光源、流光、按压阴影等系统级沉浸渲染能力 |
| 应用交互 | 单窗口 | **多窗并行**：提供应用内多窗组件，支持自定义背板、图标与文字样式 |
| Symbol图标 | 依赖系统预置 | **解耦灵活：** 应用内注册自定义Symbol，不需提前预置系统 |

## 约束与限制

### 支持的国家和地区

UI Design Kit当前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

| UI Design Kit提供的能力 | 支持的设备类型 |
| --- | --- |
| [图标处理](ui-design-layered-process.md) | Phone、Tablet、PC/2in1、TV |
| [组件导航](ui-design-navigation-dynamic-blur.md) | Phone、Tablet、PC/2in1、TV |
| [侧边栏样式](ui-design-sidebar-overlay-mode.md) | Phone、Tablet、PC/2in1、TV |
| [侧边栏菜单样式](ui-design-side-menu.md) | Phone、Tablet、PC/2in1、TV |
| [底部页签](ui-design-hds-tabs-split-line.md) | Phone、Tablet、PC/2in1 |
| [即时操作](ui-design-snackbar-resident-notification.md) | Phone、Tablet、PC/2in1、TV |
| [核心操作栏](ui-design-actionbar-main-buttons.md) | Phone、Tablet、PC/2in1、TV |
| [列表](ui-design-set-hds-slide-horizon-listitem.md) | Phone、Tablet、PC/2in1、Wearable、TV |
| [应用加载自定义Symbol](ui-design-custom-symbol-res-register.md) | Phone、Tablet、PC/2in1、TV |
| [HDS视效](ui-design-visual-effect-point-light.md) | Phone、Tablet、PC/2in1 |
| [应用内多窗](ui-design-multiwindowentryinapp.md) | Phone、Tablet |
| [沉浸光感材质](ui-design-hds-component-material.md) | Phone、Tablet |

### 能力限制

**HdsNavigation/HdsNavDestination：** 横屏且导航栏为[Stack模式](../harmonyos-references/ts-basic-components-navigation.md#navigationmode9枚举说明)时，不支持合并工具栏到菜单栏。标题栏默认采用层叠布局（位于内容区上层）。

### 规格限制

* **图标批量处理接口：** 最大并发数为 10，单次最大处理量 500 个。
* **Symbol资源注册接口：** 仅支持注册 1 组图标资源与动效参数资源，最大支持 10 个自定义图标与动效参数资源注册。

## 模拟器支持情况

本Kit支持模拟器开发，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 不支持HDS沉浸视效，包括点光源效果、按压阴影、双边边缘流光、背景流光、自带背景的双边流光和沉浸光感材质。
