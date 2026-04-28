---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d76450e41595acee19babcf53e7538e340ccc3e42def755c226c43efb857d9f
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/NeOiI5-kRgmfLHJflFguVA/zh-cn_image_0000002583478187.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=D5AAB7E25ABD2AB98304E2240A380E916F05859F41712F1ADA1805CAED3712FE)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/_wrHuH84TcSbngc2trOeUw/zh-cn_image_0000002552798538.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=BB8F56D9F1795B1206EFD1102B81E3EF3563B46FA452A1E357D3B364C7E26E3C)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/egPkO6s-TkC59dL_KhPt6w/zh-cn_image_0000002583438233.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=B4D47367262BE1C434E647DC99485638AD03E9CA54A35D574BF3F150456E2B19)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/bR6DtqC1RN-KTQTj5zKyOQ/zh-cn_image_0000002552958188.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=1AB75FBA9C72C7D70BC894D21E7EEC354C57ECA329524C3AEA85CB2815589A10)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/-lkk4waQTZSWNL_SbA-xZQ/zh-cn_image_0000002583478189.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=9B6D1A092C773AD0782F7DA7B7E8550BC9B6F2873E8BB7C722B0EDDF358D2A43)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/o_jnA_KlQR2EcgeqIiTcAg/zh-cn_image_0000002552798540.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=78155FC5CDD4BB22232AB01C9C9D0BE9569CBD957AF0860E372A6C5BC4D0F013)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/NUryH0YnRDyHN9qhTYmoiw/zh-cn_image_0000002583438235.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=88EE32EC007E580D3553A8E35DEBB7B832F1FCA42824F55C960A866EA2530AA8)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/eMLKbK-pTlm1U9P_dFUIxw/zh-cn_image_0000002552958190.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=AF8F9FC7E356361046A2BDF86F4B21E8A3E1B36738E1C6037B41894B129DBF55)

### 适配注意事项

针对在Tablet设备上运行的PC应用，不支持悬浮窗。

当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/MziQ62akQMah9HlpWrSSog/zh-cn_image_0000002583478191.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=ACD5C3A4B0B3C7B34B7077C87EC18AC9DF89F9150B95420677EFED77AD6828EB)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/p-LI4D3LSka0Xh_n7THFcA/zh-cn_image_0000002552798542.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=D6EA6ED6F7EBC2CDA8043E1A5F39846C490779D0E748414177628440D041DE94)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/7bOcHPL1S-OkWWi_hKowVw/zh-cn_image_0000002583438237.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=43978AE56B943715339171BD875A2C2783D7942DDD03BC2CA804C57742FAB1C3)

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ULPgDdgMTVCXeD-ukVcWgQ/zh-cn_image_0000002552958192.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=F03EF9880E93C513046667323AE438F8D3B21A4431CD30899A70BAEAB2956B4F)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/L8WLQLKRRNeVv559_gvDrg/zh-cn_image_0000002583478193.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=F23CA222D46D2A19833D354E095EECA0F3A5B42243E3C7CFBCA7FF05212B4764)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/-FXem8jTRFO1yWlJYV0LXQ/zh-cn_image_0000002552798544.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=C7FFFE321635F62A08A2A60A2518ECA22CA037A71761538D0B757DA10025E916)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/eAisOxCqSa-mbnDzOAZfqw/zh-cn_image_0000002583438239.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=A2596C7B60B84F6BA4061E63A8F0F179E849A4826E155253D4647D37AAF08201)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/JFfBBIa8QOSB0feYzOMIBw/zh-cn_image_0000002552958194.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=6C02D89F38EEF23A38BE332E7489A7384F405183BA7591C023E576E570AF202F)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/-ER6EvOgRamxxe4dEgPGXg/zh-cn_image_0000002583478195.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=07F25CC86AA87F7D9F4CD9760F9EB077C2BA07D779951D3012E4FC23A67FFCBC)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/mZRlj52LR4GmKx_cg7Y5UQ/zh-cn_image_0000002552798546.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=D5DA7A71C7D70132D1CA29C369D5130D0B4B2AE3567A7005340A3210A0D8DCC1)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/tYSyaCk0T-6X6g4rjAEWJw/zh-cn_image_0000002583438241.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=727FD4F501CF51756BF083F5B4EB9D70E49B6E24824FA82A0BB3F3FFD59D429C)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/wOZ35snOSPGyNyd93NzIew/zh-cn_image_0000002552958196.png?HW-CC-KV=V1&HW-CC-Date=20260427T234043Z&HW-CC-Expire=86400&HW-CC-Sign=19C6594FB615D090EE65AEAE45B1369C3672BE470AEE0D0BA40AD80F904B381A)

### 适配注意事项

全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
