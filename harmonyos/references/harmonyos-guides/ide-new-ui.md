---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c633246c120ea9e56b0b8f4f12e7624f2d854fb66379fcb8bb3eb04c690deb29
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

从26.0.0版本开始，启动DevEco Studio时，默认开启新UI。26.0.0以下版本，启动DevEco Studio时，将有弹窗提示是否启用新UI。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/yyw03O87RvOthQ0cMeEG1A/zh-cn_image_0000002779407560.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=71CFA56507FF4282C633349525CA8CBDC9B5EA72FF34CABE4F2455D2C3A28FE8)

此外，也可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/QgVFz1vQRo-5AUQZDb1p1g/zh-cn_image_0000002808767115.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B5BF5D2D1E9F4BFBD3CC58B0E22D72B1552FAF3DD698A1C10AB193C835DFBA9 "点击放大")

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ilNIxOAUQbuyeVUyCjkTnA/zh-cn_image_0000002808887199.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=38D3290806A07AAAC1C221B1D38E9B6532077E4D3C1582614E49AAB7220292D5 "点击放大")图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/_8QAHiH1SSClcqhW8fbsEA/zh-cn_image_0000002779567536.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=9425B958DA6122C8E23E097CDCF5F89851419D12DBF9A75AD60C8E0255D89FBE "点击放大")图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/g3B01pV3TbyJMzhRrzyTjg/zh-cn_image_0000002808767113.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=99570239ADFF5E68777D3C086FB3B7E52C7C87C5A899D2250C9A1774FB85ED5C "点击放大")

如需将菜单栏展开并固定在主界面。从26.0.0版本开始，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，在Main menu下拉选项中选择**Show above Main Toolbar**，点击**Apply**；26.0.0及以下版本，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，勾选**Show main menu in a separate toolbar**，点击**Apply**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/PduCdxGcR-Gej8Zh8ajPqw/zh-cn_image_0000002808887201.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0A83B3840B8A4244C58E1A9D36E2068F88C9DB70F4BE2CD9C60060F3926B3C5)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Qq8iNOulQ86fqXHGQsI19w/zh-cn_image_0000002779407562.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=63319EB1130C68C9C8472B4C30527EBF1ACCCFD64773D592A1234AB46C91002F "点击放大")图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/uQ_nBBFLRP-YpiAXWQnElQ/zh-cn_image_0000002779407558.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CAB2F951313BCE793CBEDCEF891FC01BBA9E962F775A701BEA17C1686473849 "点击放大")

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/WdYU5Fa3TnKCPS-zEOHzBQ/zh-cn_image_0000002808887197.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA7E9F06A3ADD077B51BB868F4A54AFD369EE9217C48E4F8D5B7A67D62B087DE "点击放大")

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/-g2daD-5R1OfXuBEpDksGA/zh-cn_image_0000002779567534.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED3D5AB1953EACBC7C9B33BE1A8539183D9849E460B9EB557187BD347380629B "点击放大")

**说明** 

更多新用户界面变化详情，请参见[New UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
