---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:36+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ae5feab8f68b04ae946d5c8a74ccf203266e93acd1bb65fc4e776e8db2c1851f
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

启动DevEco Studio时，将有弹窗提示是否启用新用户界面。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/2m1Up_6-TEaD2P8cC4A68w/zh-cn_image_0000002561753667.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=AC968CD2349AFFAA865E05C1E18367AB9F4FBB15D75968876B567AD057D38CE3)

此外，可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Ash0Q2G2SkqFDM0uLdr_eA/zh-cn_image_0000002561753673.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=7C793B1CDB6D43E25E0FFB995F4D4FA5B286DC1E02FCA93F1B8EF7AFECE1DB61)

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/FdL52v1BTNaL9lFZwILVfQ/zh-cn_image_0000002530753730.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=34AFB4FDE5F944A78C9727C1BB8B5B777AB2DEBE91C17EF3FD3CDB331E8347A2)图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1zYcj0YbQGisDPvjXKiqYg/zh-cn_image_0000002561753671.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=0740C6ED1ED8CCE00E2BC162E31DE05EB73A61522F707876F335FF61D41FC09C)图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/lRJtvgLKSHi2oP25OR203w/zh-cn_image_0000002530913718.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=1BD7FA822474CB76250F4A7BD1CA5248F048551CF82E0977942BB0FD6170BD22)

如需将菜单栏展开并固定在主界面，可以在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**中，勾选**Show main menu in a separate toolbar**，点击**Apply**在主界面固定显示菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/6hngYcXxQDeGUek7jufC_A/zh-cn_image_0000002530753728.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=C17DE731ABCCCB8B16EEA52E609D3223E4F683EF9C00E704E5CC8A7402B867B4)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/B4LqYfjyTwi_k1KQXsqDqg/zh-cn_image_0000002530753736.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=290150BC5615DF5FEBC12D803133E03ACB1B8410851B721C9E33E69D27FC3CA6)图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/aR-kc5bLTPiSqmMSAZSmnQ/zh-cn_image_0000002561753665.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=0ABA04C788C4CB0F2977CEB97015945436419388DBA1C405F383EDF01ED115BF)

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/0rxBuCLNR4eZ4rBQVd4nsA/zh-cn_image_0000002561833641.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=B0890B9654D0CF05A761BFA6CFF16FCED76F180F80DC3BD0ED9742D4B6734641)

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2UqWFWK1Tb-pIu56tBDMPA/zh-cn_image_0000002530753734.png?HW-CC-KV=V1&HW-CC-Date=20260427T235434Z&HW-CC-Expire=86400&HW-CC-Sign=A5456B010ABD9DE2BCD36CD02189CFF14D2B0904E54F4FB57A50D07C92622AF7 "点击放大")

说明

更多新用户界面变化详情，请参见[new UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
