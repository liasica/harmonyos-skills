---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:2fbfb67aca763ee4cc485a4de2a574543ed8ec597e0f468f87287cd411c725e6
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/CxNnUDJOQg2uGlkpfBibeg/zh-cn_image_0000002815398895.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBFB3A6E8377AF1CA3D86D124AA2F5E79C3D74F3A1E2B4E25ED8496EECA5D7A4)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/2lN2JqLYQti8nyiJBBJkUw/zh-cn_image_0000002786519320.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=70C8249E4AC6B129E60342BE363886354F1B1E83EAED99AAA171DF7EBFF2E505)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_Yo_cAXEQDmOSEQojbui7g/zh-cn_image_0000002786359392.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=86C340124E8A09225EC5B39C09DBAB8E64FAF6A53B8AEABBD912BDEA2D67F744)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/l0iBsi7pTNKIOSODTGklaw/zh-cn_image_0000002815558813.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=911CB76369C4604BA571BDBB3665E440F9D1315F3ABDA9325F64509E371E5010)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/B6OnYggFRNSXDN7SslOeTA/zh-cn_image_0000002815398897.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=98E1BF86E7D2A6697E8974185FF55D256E62C316750FF82A6BD13291150C2CAA)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/b_SGHZQDR5yFyWr2XGv67g/zh-cn_image_0000002786519322.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B037D07B3181A46A16E6B52937E92764BB91B4B1B53C2D07E8A501D98D0D305)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/iHZ9uG8tRWC47xpRlKVt1g/zh-cn_image_0000002786359394.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA1E6C9EBB7C85F3E43AD94A4BEB50BDFBDDCB532BF169864A2B6DB91780F07D)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nv4bFY3FQTy08Qu-7zeGhw/zh-cn_image_0000002815558815.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAC131D82A3785304DE95DFF22DEF22CAD1165D3EB05DE00D3EEDE58FD31C926)

### 适配注意事项

* 针对在Tablet设备上运行的PC应用，不支持悬浮窗。

  当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/0pyuonhgQM6_OfyWBBtjlg/zh-cn_image_0000002815398899.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=7285B9382F988B51CF0E27D9AC454A5CDE45C7868EF3C14340BE7DBF0D5EB321)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/4zR72WWETMerQ6vcytSw0A/zh-cn_image_0000002786519324.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=18EDE2CAFD94F050F75571630AA10DAEB1772659F30219E47BB564DE2E8775C8)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/IyudsRIXQcyhpxfEnqvH0w/zh-cn_image_0000002786359396.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=7423E615744554A2BF053C7699194FA3EB57F8B08A19199270ADC72C22D02E77)

### 适配注意事项

* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/0ohK0cnYTKKuizgIzJtxmA/zh-cn_image_0000002815558817.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D62914D81530F484586561139532F06CE35E97B47E67BE0987BE5F742289162)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/xPkB3Tm1R7Sssi0b4OmxjQ/zh-cn_image_0000002815398901.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A3135DAB0C7304C37AA577C854922E0BB4E12B7B41BEAE4E32CB0105758C610)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/kpMSWgUdRY29EBbOb_J9_A/zh-cn_image_0000002786519326.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FBF8C3751C529D825021926DB766C6EF67D93DE99B691AB35B4C556942DFC51)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/0IsiO9ryQWqCQj8EuVmvXQ/zh-cn_image_0000002786359398.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF210AEEE1C35C35FEDB76C4467D51EE4A90541353114B294A3631B47967543B)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/dfdSEmKxT8maAq00MuTUkA/zh-cn_image_0000002815558819.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=28CEF9FF71651E857FC04A71C3FFD9477EA8B3566D8BEDBD9C07A07FA6572A01)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/h_7tTln3QP28tlEDnFFTqw/zh-cn_image_0000002815398903.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=5659C7E2B7F8A50807C74B9DFD9393E47FA1CE5DA6FAB3018F530B5E3F2BF13A)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/JpkTlu8fT0u4Ef61T8a_Hg/zh-cn_image_0000002786519328.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6DFE763270C812F1D257E404B3D2C7CABB74BCFDD0BB13C09E756AF3F63E727)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/oxuGZqGZQq6qWl2jQKS9Jw/zh-cn_image_0000002786359400.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D3938356F375E7EF5CBEA1F82DC4D6A9DD820BBCF3EEA85731FDA9282AC9AA5)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/SLyBkZoNS0i1wuHX3RCoqw/zh-cn_image_0000002815558821.png?HW-CC-KV=V1&HW-CC-Date=20261112T233234Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDAFAEE2C67B6751B8ABCB19F8070B570E0A19C570189D4F6B75A4EEFCB3D004)

### 适配注意事项

* 全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
* 在智慧多窗的显示模式下，窗口尺寸由系统决定，不受[WindowLimits](../harmonyos-references/arkts-apis-window-i.md#windowlimits11)约束。
* 在Tablet设备上，全景多窗不支持模拟器。
