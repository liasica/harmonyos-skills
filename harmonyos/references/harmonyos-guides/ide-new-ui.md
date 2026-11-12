---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e3566d710622fdbe6829bcefc574dc0b19320d6ebf288e41eb41214ef6d47f0b
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

从26.0.0版本开始，启动DevEco Studio时，默认开启新UI。26.0.0以下版本，启动DevEco Studio时，将有弹窗提示是否启用新UI。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/5iudnnGhQaKXbDxpjB3L7w/zh-cn_image_0000002779407560.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8C65E0118A624D906E46CFCC6D8962A3E49FD3D91051C6FFCCA6558C1349A72)

此外，也可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/OYENPiydSEKO7h1VyixP1g/zh-cn_image_0000002808767115.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=52D25BB1C6FD98AE799B60A31C6FDF288752AA5B26183205D090E619462A55B2 "点击放大")

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/cB1pIy7PR8SJr7yPshkXag/zh-cn_image_0000002808887199.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=84DAFC471CBC4BE61A1A02B41877A75363D3DA041A82672C86FEB4D8F3ACB6B4 "点击放大")图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ybegrhvXT6K_kHXsP3jdkQ/zh-cn_image_0000002779567536.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=276A175B9BFAF077419E1A201B686DF0DE6E32DEA81B851E500811BED7CF2C4C "点击放大")图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/bxyiyivgTgqIxsyKzJNPBw/zh-cn_image_0000002808767113.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7564566862E04F17680B056D658E7A15A77174F76486F6BF120ED37C0DD8FAE "点击放大")

如需将菜单栏展开并固定在主界面。从26.0.0版本开始，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，在Main menu下拉选项中选择**Show above Main Toolbar**，点击**Apply**；26.0.0及以下版本，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，勾选**Show main menu in a separate toolbar**，点击**Apply**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/rV-b3kM0RgGLgOVwC9i85w/zh-cn_image_0000002808887201.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE7E5B16F29462E94DB7BF9DDD0F7B788190DE11DBC4EF14621E572216D3102B)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZQQcPBImQ4eQo3Tg0qV2Ug/zh-cn_image_0000002779407562.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=51194DF5D5173664292E58EF6048CE503FF4BB9883220C278C45277382A04E27 "点击放大")图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/1dII1e5vR5-Ejrtm52gHnQ/zh-cn_image_0000002779407558.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=27648DE5FA7137FF60C7738A816F7ECB434FC4D99F7BA405411B568DE27D8DB9 "点击放大")

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/KvLjovIAQbeYVAeNIPFxxg/zh-cn_image_0000002808887197.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A0449169790820A3D35243D0A183035407BC41B21F48630C969E86DD9FFEE1C "点击放大")

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/OI3LT4RhS2qJ2NKLmtmp4w/zh-cn_image_0000002779567534.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CD7092A10B28A436F04BF048B0881E5FE06D3B7E4988025CF0E2E976E678CA2 "点击放大")

**说明** 

更多新用户界面变化详情，请参见[New UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
