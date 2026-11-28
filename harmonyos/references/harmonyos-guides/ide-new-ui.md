---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:26+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f7a61151c35cfbdb9754e9620b9710dc1e0f2bf6cad7f7d9f0657900574bfcec
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

从26.0.0版本开始，启动DevEco Studio时，默认开启新UI。26.0.0以下版本，启动DevEco Studio时，将有弹窗提示是否启用新UI。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/rQAT5DyoSi-juZhDiJNsMw/zh-cn_image_0000002779407560.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9F24F7755B9A390DC09EF3003AB550E922548002366B354D0D605B0D44FA557)

此外，也可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RN3_knFRR5yKl3NZaPcIqg/zh-cn_image_0000002808767115.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=B61A50671B3FA494A15C5E603A22AC74789387DE9695D2139C1187C351334AEA "点击放大")

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/yP1xta8kQgCZyNttsPxFBQ/zh-cn_image_0000002808887199.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=57618A4D92D71E1FBB9521C8FFC511C984442F8566B5BE1C8BA84206C466A686 "点击放大")图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/2hE0xLxoQZScY2e-4tjC1g/zh-cn_image_0000002779567536.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=732CFEBA56776AD9256F150371ECA96D79437252BDB12C9E614FABE6B668170A "点击放大")图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/rSL_yYrKSoeB1zWKqfj5QQ/zh-cn_image_0000002808767113.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3055B53CFAF517179A6D9FF82C4B01993FAEBBF7421E44A5771F10F41D5A732 "点击放大")

如需将菜单栏展开并固定在主界面。从26.0.0版本开始，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，在Main menu下拉选项中选择**Show above Main Toolbar**，点击**Apply**；26.0.0及以下版本，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，勾选**Show main menu in a separate toolbar**，点击**Apply**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/WpbVomG-S3mWDuZAjAXMJg/zh-cn_image_0000002808887201.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF79FDD756598FD7716BDCFBFF81BD9CF9BABABDC6DAD9E7A387BED66A7AC0BF)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Mj_g7fhPQaWWOeLjc38b4g/zh-cn_image_0000002779407562.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA5FCEF2C07EE1308D7CE7D28C1B6DCAC32A2A05388F825866B3AB9DC5DAA0ED "点击放大")图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/vARvhp7BSZmAFDsoW4nNGA/zh-cn_image_0000002779407558.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4F2DAD90C596557E7E2CC208D98AD4B403460FD3C3679DEEF337D2FDA93CF11 "点击放大")

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Cb8xnhvGRlWM3hDzaLkCkQ/zh-cn_image_0000002808887197.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BE1B5F2D3D948F9E7F252B61964AEDB4AFD20735B2AF2987946D0306556D75E "点击放大")

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/WT3gdFPGQlyWrS6Ur1tmLg/zh-cn_image_0000002779567534.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEC1DE19618DE58D1AEAC47BBB0D055461FCB4021698570EA754348EF9DE2019 "点击放大")

**说明** 

更多新用户界面变化详情，请参见[New UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
