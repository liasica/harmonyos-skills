---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:50+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:c91091399988132d7f9e0149e9333ca66f933532981f95b04c53896b9cd36139
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/tQJoGGqfSpuH3PgbQ5XNqQ/zh-cn_image_0000002820525403.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=4619DF5E0508D5FED40E2D52DB083AB0CCEF2A5A62AD7E7B52EC72F8D9BC2E64)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/m5yrFtXAQpGUMSMI9G6NJQ/zh-cn_image_0000002820405403.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E62CD332F85B2DBBDBF57CDB2191DE1A9022D300CC8108B23787FAE583683BF)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/9l7blzbyRGWbV2VHu0KkMw/zh-cn_image_0000002791725424.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3F10DD57D2E379C0616FCA25D733F0D46EB8C4D52A78271A19F856951D2E734)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/K27h9FddTVauu0sM15kclg/zh-cn_image_0000002791565452.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=E34AC1EC31983787800CABD69FA223F216700293AC1245FB82A3E1F64E1BEDA1)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/QdqZ4xVQREChY5XLjcgAXw/zh-cn_image_0000002820525405.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=54471D4C5A1E69C9A18167136BF39C86D815290B95EEC815B2E32B7A03D41B5B)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/RdyQJHS3TECZIXduILbcdA/zh-cn_image_0000002820405405.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=6597117C21EF2B64D6FE9B92EE5083E5E9EE8B2B4E0633A2B74B4F3A053F4878)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/5XIkljWsSheltVf03bfghw/zh-cn_image_0000002791725426.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BB9A054CEE18B13DE02A38931D8E5C56C857AA72D61ED94B9D55667FB589839)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/soQ9sYNCRmqOrrTwyoYmhw/zh-cn_image_0000002791565454.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=B694FDBF80E8FF924D3AF9C37735C5683770E3BC86D9F0176BDB80A771030EFA)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qyJaUMwDSgSJ9HUsOXDGDg/zh-cn_image_0000002820525407.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=12E204DCE98D6DFAB5D56E614684F51168765E8761ED9AC9F13BACC2FEAEDACF)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/XDdwVYoWS8i3UVtxfi6wKw/zh-cn_image_0000002820405407.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=8808F6A0A79B8F32A034F249A7B689F539CEA9E0E81C4C10771AB68BE6417D9C)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4f-PcJg4QruAOW5xijforg/zh-cn_image_0000002791725428.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=C375FBD1DEE7FB012AF6219D2A5634702E28750C6C22375D97F25E934687F859)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/JsZIumNUSA-ocDpJsbIb4g/zh-cn_image_0000002791565456.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D224D188330061712ED4C3958C7BFFB1CDA53C5F5E119DB7A44DAC39546D066)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/OBQxL05fSH6P_HbsyeVYig/zh-cn_image_0000002820525409.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=F77CDCB54E13EBB84A87360982A5689A10EEDE80784A5A4E51D987FCD311E185)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/oLbAylcKT8KggaqSHdVPXQ/zh-cn_image_0000002820405409.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5D95B37FCE551950D905232E0C0EDB963CEDF438D3C28A99195E101AFA549C8)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/l0aD5k_aTwmwJ3XlDauOaw/zh-cn_image_0000002791725430.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AA4496BD9DB48E7B0388940A554C0C4691803446911ABA65EE69CE2C5F2BD56)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/3jvHlkxGQPCBEQb3e2xbyw/zh-cn_image_0000002791565458.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FCF9621E320987280656CFBC45B3C0E9A9D4DD90B5E50A1F8CA52A285F370F3)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/h9Rdk9WHT-2R0lF6UpXg0A/zh-cn_image_0000002820525411.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=F086755D93EEFDC18DF32201D55313B28027464F6365D94B2FB1705EBAC159A7)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/6idmjtEAQ9GQgdpdm9ZkyQ/zh-cn_image_0000002820405411.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F168CA150830AE5597637C20E0F4931C078E2DCC73145AE3851192C65F03DF0)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/K_A3WUB_QrSrdJdbyS6Efg/zh-cn_image_0000002791725432.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=00983A704F30DC152D93DF3E166E10C6938CFF4F86836975B15BACF07FEBF781)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/BD0vFmmFQSuzRI5oOlUdAA/zh-cn_image_0000002791565460.png?HW-CC-KV=V1&HW-CC-Date=20261119T014750Z&HW-CC-Expire=31536000000&HW-CC-Sign=501DD51396B78537EA77B40D6736C59914680E90CD0BA5508CF22277E54E3A0E)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。
* 在Tablet设备上，全景多窗不支持模拟器。
