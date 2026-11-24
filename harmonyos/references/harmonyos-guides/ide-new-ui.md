---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:19+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:98e8bae5801b3a6b21bcf87bfae942d03b1f485bcae005baf6b637e0fddfaae6
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

从26.0.0版本开始，启动DevEco Studio时，默认开启新UI。26.0.0以下版本，启动DevEco Studio时，将有弹窗提示是否启用新UI。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/_exnoRC8T-2CSJz2n3d1kQ/zh-cn_image_0000002779407560.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=779C071C26DED84915F92499A6F96AFEFCE49655FCE72CC3FAF48DB13481C6C5)

此外，也可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/tcXSPsa8SsW_H3zN5vGI_g/zh-cn_image_0000002808767115.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D1F586F344E4DDFB6892712B05FE9476A81B8DBA180A1A79D58DFBE6590EA4E "点击放大")

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/ZkyYFMQlS12QPrOjhx2PsQ/zh-cn_image_0000002808887199.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD8CEAF5CAA47B7E103A0015ADA3F9E08A121CB7DF65D8BCD4111014D2C66C47 "点击放大")图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/sFFCU2N8SiChdn9xHuJGQQ/zh-cn_image_0000002779567536.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=226F7BCB7C226CECFF501CFD30CB877A2D1D9B120D3133DB0AF852675EF3733A "点击放大")图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ayJw8hsmT2OrVNFiI3oKLA/zh-cn_image_0000002808767113.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D4E17E564827166D3564ADB32F10D76FAB001EB1BA13C9783E3E30B76036A5C "点击放大")

如需将菜单栏展开并固定在主界面。从26.0.0版本开始，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，在Main menu下拉选项中选择**Show above Main Toolbar**，点击**Apply**；26.0.0及以下版本，在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**，勾选**Show main menu in a separate toolbar**，点击**Apply**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/br0QJ4EcTLaxm4i28_gc6Q/zh-cn_image_0000002808887201.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8CBA126F225606A764D182BA9B402DC4E275204346D335C7E6CABA0866782E6)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/V8uUePILQ9y56cqKq0uCcw/zh-cn_image_0000002779407562.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FEF0190B2E1E4F79857DC846AE4F6500D50EF4BD94197CDB260B88BF0058BF5 "点击放大")图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/JtAqYtepQh66nVPe1N5KIQ/zh-cn_image_0000002779407558.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2075CCB115D7A9D335643E8B6E2185B846E744926DDF0DE69F43343CE55F883 "点击放大")

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/RLYSHC6ZRKyOJ0zzPmflRA/zh-cn_image_0000002808887197.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3EAB8E2F7531B97338B53D07DABDFC13DA14534E563A33DE00425FB5506606F "点击放大")

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/oqqLxsMiTYeZMyqiOBc5YA/zh-cn_image_0000002779567534.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B795256A76571363F70EBB6E5B1123F78FE196524586F0D37F43E0B389944AC "点击放大")

**说明** 

更多新用户界面变化详情，请参见[New UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
