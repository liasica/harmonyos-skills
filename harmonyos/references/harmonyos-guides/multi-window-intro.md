---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:12+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:d79969e1206ce61bc63a844fe48eec1f7b2fffc9c4ed8c4809702323d6703d44
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/4O1LLIDaSwmxqntC-7SKgw/zh-cn_image_0000002817506553.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D62CDC47A9C65B6EF341E41866135C9A5D6395B2F1104B7C711A27073D4F651)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ZKOV2775TCmV7aoG6G806g/zh-cn_image_0000002788307124.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=7E22EC9B0E778810B8AFD72A374E3E194B9A207FD13793F9A9BD8E017B3CA390)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/dZZUtaKRR7WSMKKD_kWmYQ/zh-cn_image_0000002817426487.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=F932B44FBE1981254AF70B2B996E05C2994214284FB11A3BC7FE88C700A3ABA2)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hI9bfeJzRw23GZnRhDvyxg/zh-cn_image_0000002788467068.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD108593378B1F2D4AFBD8753B742086C72359ADA47AF77F4374DE1F4EDA89DB)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/HtCN0UG2SbiMWOrf3xjTsg/zh-cn_image_0000002817506555.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E53FDE7A1F69A9475D13887D87B6442C86E1BD821607359092236AF3DFC6AC8)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/rJd9bUsGSuWfTDk8be2DlA/zh-cn_image_0000002788307126.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=52CB0E025FC6FF6C74090E7085E8DD494C10DE205CB573E0AC9BED50BFDEB833)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/pieseWsdSQqyW1A-_pxb7w/zh-cn_image_0000002817426489.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=86BC02F2A805B19632777BDB1ED4D14F07F8A3E4A21A042CCA711D2EF534375F)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/fEaoqZV_Qwe7qpylhIl09g/zh-cn_image_0000002788467070.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC5856C333E087D1501104329B8851892B11E66CE92388837B7AF746D0729E2)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/qdZR5OoTR_OEFkXSZ2kF6A/zh-cn_image_0000002817506557.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=787E539E5DB83FFB822108589FC2479F1CFF293CF768187EC992B0DE2E5C36FB)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/vRsLv5-6TUaop6fQQXWacg/zh-cn_image_0000002788307128.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=F50B4D3222DCA11868A9B96F1646396272C24130DF8BA1CF6B57771C17146F02)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/sAFPPEtnR323YGrfa171Hw/zh-cn_image_0000002817426491.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=87385235790A242DF31AD274979674451A64AF9C1A21650E7085291BB8E3667A)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/cm4fzghKTHWJZ3WXxxRUmg/zh-cn_image_0000002788467072.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=D50EFB70224CCF764DE79B81E8779236836D5669983E6D57C025DDE1C0A178A4)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/yNmWwAcxQXa-VHQBpmtycQ/zh-cn_image_0000002817506559.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=24796792572D4B4044A6C874FC6AD18BC289947B3BF0C88040CD8A04B89A4535)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/5GtAT7erT32R-RpiwI_v7A/zh-cn_image_0000002788307130.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACD283497225CB35D08DA417E876A08C55E1ACEEA51517856908CDD946D9E299)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/FU2YOwZKTgueWi2zfvdl4g/zh-cn_image_0000002817426493.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=5408F6F6639105DD59F406F10F2FF6D1FEBEAEE4F448FA3019B004A5EC21BF5F)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/rqu3qhnoTCmWY6Clmp0c1w/zh-cn_image_0000002788467074.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E325D8E4D13511010B597C19A709C19821494808F18DCCDC46D760B9BD197BE7)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/rU-E9TWiRZSjRxljtQr_Dg/zh-cn_image_0000002817506561.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=7ABACD0F544804BD1A5F912FBE25FE30137AB9DABC90761733E8A0B9D5C01C7E)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/KcTJ48IZQR6A1OW2m7AyiA/zh-cn_image_0000002788307132.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=5635C359D0B9BFAD7C37D8BB8BF8764B426B32D1392498C12654C758AB71F645)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/dG3iwntiRF2zoViosnTknA/zh-cn_image_0000002817426495.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=72294936255191B0201F50029B968F7AC6BD29638C39D50A09DCBFD80E3854D7)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Twj8rhioRhiLZGRDjmDcmA/zh-cn_image_0000002788467076.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=A335B9642F0A8A1AF05934BAF7AA3DC1A3C57DD2F71680A55B5CD9136E7CB195)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。
* 在Tablet设备上，全景多窗不支持模拟器。
