---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:16+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:d760e293fcf56b4c17514596024f6178c7f987ca3b973f9290f99f03a694c982
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/21WQSQD8Ts-iG5RGGGswiA/zh-cn_image_0000002793037074.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FC1E23522A42E97301655CB3A6866568ED46D715F98FC4F0C49817388F9477C)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/2fmFbol2RRm1mKAN11nDmA/zh-cn_image_0000002792877104.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9B07AA6A65B41D2892BE003432FE888176EEE1C5FB7D30E6E6FF1C99B80D88B)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/YIH8BKf8RPS0JtlpydZFRw/zh-cn_image_0000002821837011.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=89BBD3C0E17E1EFA122B63CE9FB556BA48DDAA38B97CBBDB3BF33A7B7420F7D0)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/SyXQYkxvRFqjXy8WgUur5Q/zh-cn_image_0000002821757013.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=1049AE2DA44C97A6F7B64D24EBCBCBF1BDEEC446A5DFC3E15377CFE1776E5A8A)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/AHoEZBTOQcGnwiJOyM8xxg/zh-cn_image_0000002793037076.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=79EC56469FFBD4CAD0CFD8946B61C89879AAE7BC482EED1EA72BA7C01B435EE0)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/2jEilEH4S4GzMmuFE9U_XA/zh-cn_image_0000002792877106.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=7098B3858EAD233CC3B0DD12BEEAFBC6B577D27C2D1B64F49244FE42222D0759)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Gf5gaGzZSLuzS0HMLd2zPQ/zh-cn_image_0000002821837013.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=D300A98EB5F1208A93A72EF385943B34BA17B4BAFD5F58F5A9CEAA2B3525DBD2)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jFbGCcBARaWIXxM0OyNZgg/zh-cn_image_0000002821757015.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=5851903A782967344420119C9DE3E565B3292F2272FA5B233F0298392330F83C)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/i6VqxtDHSH2FPQVJ7wy_DQ/zh-cn_image_0000002793037078.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=82B3CCCDEB6222CD8EE776F69748975A56CC0AF0BE7F856C55763005055FE1C9)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/tTszfc45TICNxZ0EAimSLg/zh-cn_image_0000002792877108.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACE0062C31F4D0370E5C283BA381D23C08670AA30E21F8A98A9426A0317D3F38)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/NkpM8X3sQNSJFnMeeq-thw/zh-cn_image_0000002821837015.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8070F1EA4B59A9A1F57A2AC00F1DBB73F296E4DC92FFEEEDA1955BE33F15E8A)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/eE0gCfW6T-KQKfU7tIIM1Q/zh-cn_image_0000002821757017.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=50CEDAAD4433A3C5E1ADBDE30F951DCF7B6F54349905A8149B60E6C54FE3DBC0)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/aeN42uFTSq-eUbvhLMlkYQ/zh-cn_image_0000002793037080.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=33D43BB9D984AADE0CF4AE3A7789830C9F116F4A5A5BBF69C6F5470184D76D5A)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/vqldvAIBSvyqzmh8iGnI_g/zh-cn_image_0000002792877110.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=4689A2E74E1DD9E3057560B654C6753D0EDEC2E3829F1BFF95C8995D602898D4)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/3laGT3FOQZ6hfyRZVfQWRQ/zh-cn_image_0000002821837017.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AF310474FBFC289DF819BD1F9AC3B740FB064066CA692E8931D809EC8DFFAB3)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/hIS6_b49Tr2W_8yM5gTY6A/zh-cn_image_0000002821757019.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=26A921E2CB4AE10BFEEB80D55B2EFE33B4A9ED9DB3017CC44FE4C10302F04AFB)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/JEcIecpoQOCCmWe2ctTmpw/zh-cn_image_0000002793037082.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C914262267D825D6DE51922CBEB080A6068A0A30674B5E7144283EA94ACAF52)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/lMTWZQivTP-YoSGDI9TsFg/zh-cn_image_0000002792877112.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABA9E45ED6E9E850BEFB07908B3920887626DBF497B8EA0F97B7F95F4324C07F)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/TLIxXiu1QsCWtXtM4ZB5Pg/zh-cn_image_0000002821837019.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=821AE199FA8CB9E42DD7886B1C925B36D0936F2873BC26067063EE74834CD47D)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/DkQPNB0XRPKHXSnI0oIyhg/zh-cn_image_0000002821757021.png?HW-CC-KV=V1&HW-CC-Date=20261121T010951Z&HW-CC-Expire=31536000000&HW-CC-Sign=90E8BFD4FA03B7ADA4787786436C17180FCDF5C5864C1919A042D18974BF92CE)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。
* 在Tablet设备上，全景多窗不支持模拟器。
