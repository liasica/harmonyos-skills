---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-10-11T07:21:15+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:c3918430efb15c62bdc55048d2df334d5dd2c538e79bfdecc9a16417209a62cc
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/XRPcfXeeSYGyMxUpPuQjjA/zh-cn_image_0000002755023828.png)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/IaZi7aOGRh26kvK3D1LluQ/zh-cn_image_0000002755183716.jpg)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/ZuiHeaQfStyT7switUGvYA/zh-cn_image_0000002784582583.jpg)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Cn7PVwckRIO0iCLNFpqk4Q/zh-cn_image_0000002784662763.png)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/5kO5-i0gRy6_fbhxBmMvSA/zh-cn_image_0000002755023830.png)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Vif05DnbTECupePqaWYjjA/zh-cn_image_0000002755183718.png)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/n6FWethBRQWKVtx3L9PVHQ/zh-cn_image_0000002784582585.png)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/65Qb_-ffTR-19CLK3NJMUQ/zh-cn_image_0000002784662765.png)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9MesJHkOROCNCkXDtMqQmQ/zh-cn_image_0000002755023832.png)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/1bdE8XslTSmdgOr2u5xBqQ/zh-cn_image_0000002755183720.png)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/mwlwDbuyTZqc-eCsagkD9w/zh-cn_image_0000002784582587.png)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/BOPIVYbWQKORzMJMkZLJkA/zh-cn_image_0000002784662767.jpg)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/CYI-S_mjQKunSrn2s657cg/zh-cn_image_0000002755023834.jpg)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/jayxtbaXSdOAro-JlRUjJA/zh-cn_image_0000002755183722.png)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/bGXuSADBT9-4XSlAEoUczg/zh-cn_image_0000002784582589.png)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/da-kJBaIQU-KeqZ89RMzVg/zh-cn_image_0000002784662769.png)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Zc6BjYSlSVyobMGkDryAfQ/zh-cn_image_0000002755023836.png)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Y44fKgNfR8S8_Hz9bAyamA/zh-cn_image_0000002755183724.png)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/KVSvJrV3S2moKWb-64AUfw/zh-cn_image_0000002784582591.png)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/77VaC9kVSoWd3tJPaVCJTg/zh-cn_image_0000002784662771.png)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。
* 在Tablet设备上，全景多窗不支持模拟器。
