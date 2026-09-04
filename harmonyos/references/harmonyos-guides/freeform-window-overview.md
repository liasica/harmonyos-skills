---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/freeform-window-overview
title: 自由窗口简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 自由窗口 > 自由窗口简介
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:08+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ab7f956f4027803824215af01c4ab9ba907bb3689d274b9f6bba3678ea789373
---

## 自由窗口

自由窗口是一种允许用户在同一屏幕上以自由大小、自由位置显示的窗口状态。自由窗口支持拖拽、缩放和分屏组合，从而实现多任务处理。

自由窗口按照打开或者获取焦点的顺序在Z轴层叠排布。当自由窗口被点击或触摸时，将导致其Z轴高度提升，并获取焦点。

启动新的自由窗口时，默认以一定间距在上一个窗口的右下方层叠显示。

每个自由窗口默认会在窗口上方显示窗口标题栏，标题栏左侧显示应用图标，右侧显示三键控制按钮（窗口最大化/还原、窗口最小化和关闭窗口），且窗口标题栏支持额外的[沉浸式配置](../best-practices/bpta-multi-device-window-immersive.md#section359241062916)。

自由窗口可以通过拖动窗口边缘调节窗口大小，可以通过拖动标题栏移动窗口位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Wv0umO0YQYCMJbhxxQ_YOA/zh-cn_image_0000002742123185.png)

当前设备支持情况：

* **PC/2in1设备：** PC/2in1设备上的窗口，默认为自由窗口。
* **Tablet设备：** 部分Tablet设备，支持开启[自由多窗模式](freeform-window-overview.md#自由多窗模式)（通过下拉控制中心，点击“自由多窗”按钮开启）、[电脑模式](freeform-window-overview.md#电脑模式)（通过下拉控制中心，点击“电脑模式”按钮开启），开启后，应用窗口默认为自由窗口。
* **Phone设备：** 部分Phone设备，支持开启[自由多窗模式](freeform-window-overview.md#自由多窗模式)（通过下拉控制中心，点击“自由多窗”按钮开启），开启此模式后，应用窗口默认为自由窗口。

### 自由多窗模式

自由多窗模式是一种支持用户在移动设备上进行多任务处理的交互方式。

自由多窗模式下，允许用户在一块屏幕上同时显示多个应用窗口，此时的应用窗口为[自由窗口](freeform-window-overview.md#自由窗口)。

部分Tablet设备上，可通过下拉控制中心，点击“自由多窗”按钮开启自由多窗。

部分Phone设备上，可通过下拉控制中心，点击“自由多窗”按钮开启自由多窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/32B_oNIdR6yKX5c8G6pBFA/zh-cn_image_0000002712244272.png)

### 电脑模式

电脑模式是一种支持用户在移动设备上进行多任务处理的交互方式。

电脑模式下，允许用户在一块屏幕上同时显示多个应用窗口，此时的应用窗口为[自由窗口](freeform-window-overview.md#自由窗口)。

部分Tablet设备上，可通过下拉控制中心，点击“电脑模式”按钮开启电脑模式。

## 典型场景

自由窗口适用于多任务并行的场景，可在同一屏幕内处理多个窗口任务。比如：

* 当一边使用浏览器上网课，一边使用笔记进行记录时，笔记窗口为自由窗口，可对其进行位置的拖拽、窗口大小的缩放等，使其既不遮挡网课核心内容，又能有合适大小的窗口记录笔记。
* 在进行方案设计时，可同时打开多个应用窗口，调整其位置和大小，使其在同一个屏幕上呈现，以实现多种方案对比且互不遮挡的效果。

由于自由窗口支持大小缩放，且主窗口默认存在标题栏，与非自由窗口状态下存在差异。应用如果是通过屏幕宽高计算布局，未适配窗口宽高变化时，缩放窗口可能会导致界面截断、遮挡或控件叠加等问题。因此需要进行自由窗口的适配，具体可见[应用适配自由窗口](application-adaptation-freeform-window.md)。
