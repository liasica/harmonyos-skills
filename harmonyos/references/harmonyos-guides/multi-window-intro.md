---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro
title: 智慧多窗简介
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 智慧多窗简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d671e53ebfcd7bd7e1e861a363aa8da13789fddcb3f39a85f2407c6c341ce542
---

智慧多窗是一种多任务处理解决方案，它允许用户在同一时间、同一屏幕上以悬浮窗、分屏或全景多窗的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。

## 悬浮窗

悬浮窗是一种在设备屏幕上悬浮的非全屏应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

针对手机，一个屏幕内最多支持显示一个悬浮窗；在折叠屏手机展开态、平板类设备上，一个屏幕内最多支持显示两个悬浮窗。在超出悬浮窗显示最大个数限制时，打开新的悬浮窗会替换最近久未操作的悬浮窗。

### 悬浮窗的类型

**悬浮窗的常见类型主要分为如下两种：**

* 竖向悬浮窗：一般用于新闻资讯、社交以及购物类应用等场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/pIucQSlQSeyzu3ptLn9Qsg/zh-cn_image_0000002589244485.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=AF45849DA7BE19D2B8CF63E4C4AC613F8F2D0CDE765A3726DB15DB76FB79846F)
* 横向悬浮窗：主要用于横向游戏和视频全屏播放的场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/0MJgGXVFQKaxMEHujwwW9Q/zh-cn_image_0000002558764678.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=C9280C97294B34490525F6DCF433C75F4B86FE17D8714B8580C1C966207205DC)

### 悬浮窗的触发及恢复方式

**悬浮窗的触发方式有以下几种：**

* 手势触发：应用全屏时从屏幕底部向上滑至右上方热区，松手后可开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/31v4HkktQMaVcXbpa7oAJQ/zh-cn_image_0000002558605024.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=D95AB8EED3BFD5253244DEEE33F976E620946021B722F08C1F5CE825E4B47819)
* 通知消息下拉触发：在系统接收到通知消息未收起时，可直接下拉此通知消息开启悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/UXa0yIuSQ7Sp9-YkIQICNQ/zh-cn_image_0000002589324549.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=3C1DF6AF79A59CDD1CA83A18B89DA42361CCD390E44D9656CBAFF70994A3FF2E)
* 侧边Dock触发：侧滑调出侧边Dock栏，点击Dock上的应用，支持悬浮窗的应用以悬浮窗模式开启。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/IpvGj2yJTdWu9Sspb_Lttw/zh-cn_image_0000002589244487.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=78AA44D4B2F575EE697826C94557D1A47C26AC4B71C113267545EEA85A46EC1D)
* 分屏切换悬浮窗：分屏时，按住分屏应用顶部横条，拖拽到相应的热区，应用从分屏切换到悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/bpWvjIefTh2BFlBK3kaQ5g/zh-cn_image_0000002558764680.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=CDCE0CDE3242BE09375366EA71CFBC92138ECE667B824EFE2F1DEC88B9FE43E9)

**悬浮窗的恢复方式主要有以下两种：**

* 多任务中心中恢复：对于已开启悬浮窗模式的应用，在进入多任务中心时，悬浮窗应用同全屏应用一起显示在多任务中心，用户选择点击悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/gj10OdMxRXWoT8J345WWXg/zh-cn_image_0000002558605026.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=F1D4DC124F9EB3A24A20F4E019087757C834BEAEED0346A80F4D1B9242205498)
* 侧边条恢复：对于已开启悬浮窗模式的应用，其最小化后会暂存在屏幕上的侧边条中，点击或者长按侧边条可展开任务选择界面，选择点击侧边条中悬浮窗应用卡片时可恢复悬浮窗模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/fC0nztgqScCq2ZUCkWRqxw/zh-cn_image_0000002589324551.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=9BC13DC653F7002503DF9824DFDB40040467C5B2F13E8F6D6DA9665F4292E3C1)

### 适配注意事项

针对在Tablet设备上运行的PC应用，不支持悬浮窗。

当应用module.json5配置文件中的设备类型[deviceTypes标签](module-configuration-file.md#devicetypes标签)包含"2in1"且不包含"phone"时，系统判定其为PC应用。

## 分屏

分屏一般用于两个应用长时间并行使用的场景。例如：边看购物攻略边浏览商品；边看视频边玩游戏；看学习类视频的同时做笔记等。

### 分屏的触发方式

* 分屏通过手势触发：应用全屏时，从屏幕底部向上滑至左上方热区，进入待分屏状态，点击桌面另一个支持分屏的应用图标或卡片，可形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/W1X1wMYMQRyziIGZCT96oQ/zh-cn_image_0000002589244489.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=CFF9B4FCD4814273581BEFC17145AD507CCC24E94DD5D9974C30ED98C2A5302B)
* 应用自主启动分屏：除了通过手势触发分屏之外，应用可以自主选择启动分屏，具体步骤可见[应用内分屏](multi-window-support.md#应用内分屏)。
* 侧边Dock栏触发：长按Dock栏中的应用图标并拖出，和前台支持分屏的全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/ABSa2oGOTsOw_Z2-H6De7g/zh-cn_image_0000002558764682.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=30104FB5589FE53B6036F787949BF920909A40F40DF6A59C42D45ACC09F9BE3C)
* 悬浮窗切分屏：按住悬浮窗顶部横条，拖到相应热区，悬浮窗和前台全屏应用形成分屏。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/YEmrYGMCTjWPEQlZKiJnGg/zh-cn_image_0000002558605028.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=CDE2736F3DB57B3F77B4210ECFBF17CE1608BFFA3E5BD1118B70ABB2DC81D3A6)

## 全景多窗

从HarmonyOS 5.0.1开始，折叠机、部分Tablet设备支持全景多窗。

全景多窗旨在帮助用户在折叠机设备展开态时高效处理多个任务。通过全景多窗，用户可以突破物理屏幕的围墙，实现在同一屏幕上同时运行多个应用，并在这些应用之间快速切换。

全景多窗在折叠机设备上最多可支持三个窗口同时运行（部分Tablet设备最多可支持四个窗口）。

### 全景多窗的样式

目前全景多窗在双折叠设备上支持小窗口与大窗口两个档位显示，在三折叠与Tablet设备上支持小窗口、中窗口、大窗口三个档位显示，且窗口的档位与位置支持调节。

* 双折叠设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/uGwchG59Q26_NuKzFyjUOA/zh-cn_image_0000002589324553.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=FF19ACBC2341B3AC323DD802EFDAB9EFF0A28654282786581DCF5F10D4632BF3)
* 三折叠与Tablet设备全景多窗窗口档位及窗口宽高比：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/HXycJfuySnyv_sb7nmEk-g/zh-cn_image_0000002589244491.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=4651114C2AC60CD4837823CE6B01303E584E47E8422F9864ABB99A5C687154F6)
* 窗口状态分为平铺和侧身两种状态：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aF682OGURKmgE34XmM3Kyg/zh-cn_image_0000002558764684.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=13380F3FDC9D6FED471D50B4C2984796756F1E5DB93AF9A999139FCAB5C0D66D)

### 全景多窗的进入方式

* 全景多窗通过手势触发：

  应用全屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/zKYTCJ34TMiXbzhzQ5N2kg/zh-cn_image_0000002558605030.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=FB1ED8774E3A8D58BB1FCE75A22DECCF48221AF42E5DF92B148AB0E5DA0D884B)

  应用分屏时，从屏幕底部向上滑至上方中间热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CGsXfL00Su2fzDnVdMZ0Gw/zh-cn_image_0000002589324555.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=E8397C2A4037E1F14322294DFAFB35F95163DD8A0299C153F01EE36CD025CC07)

  应用分屏时，从屏幕底部向上滑至左上方热区，点击桌面另一个支持全景多窗的应用图标或卡片，可形成三小窗全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/FZak1Pe5QlKms0mvpg2b6g/zh-cn_image_0000002589244493.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=0026DC4D8074BC739809BE4B64CC5AFFBECE364A3BFAE2254C7E608919050CDA)
* 全景多窗通过顶部横条触发：

  应用全屏时，点击全屏应用顶部横条，选择“全景多窗”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/AoxxmgmgRteTW30o7hFxcA/zh-cn_image_0000002558764686.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=9D00B91DF9F71F7F5767CDA60618DBA935EF4946DF243A69A490FA51C088DD04)

  应用分屏时，点击分屏应用顶部横条，选择“增加窗口”，点击桌面另一个支持全景多窗的应用图标或卡片，可形成全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/3qY36biVQse5PVal0H6u0g/zh-cn_image_0000002558605032.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=95D9B486C4872F9A2C12E7BAC10E9815485767476D4AD8B9FDFD1E11D16F4B04)
* 全景多窗通过分屏拖拽触发：应用分屏时，调节分屏比例到相应热区，进入全景多窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/JKR3sgc7SEefd7RxC9CUsQ/zh-cn_image_0000002589324557.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=65547A4F9F7BB51CB3C2F2EA73F0BE1C368ED9E7E99F96AA3BE950F620FD5969)

### 适配注意事项

全景多窗侧身窗口为不可见窗口，可以通过监听[on('windowVisibilityChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowvisibilitychange11)感知应用是否处于侧身。
