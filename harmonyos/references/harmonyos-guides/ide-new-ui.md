---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-new-ui
title: 使用新UI
breadcrumb: 指南 > 开发环境搭建 > 使用新UI
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:33+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ea29065358e49586840e6cdbc5a218144e19154999d41a1e531108c5fb078819
---

从DevEco Studio 6.0.0 Beta1版本开始，IntelliJ 2024.3.3底座升级，提供全新的用户界面（User Interface，简称UI），简化工具布局，优化图标、窗口等显示效果，带来更简洁的外观及开发体验。

## 开启或关闭新UI

启动DevEco Studio时，将有弹窗提示是否启用新用户界面。点击**Enable and Restart**，将重启DevEco Studio开始体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Yth3vq50T-qa5TH_IcLlgg/zh-cn_image_0000002561753667.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=318ADA899453E064FAFA7A94B96E083FF80A093459C25E63124BF972622731EA)

此外，可以在菜单栏进入**File > Settings...**（macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启完成后体验新UI。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/_ROg28kHSaSpv5sbD7ecyg/zh-cn_image_0000002561753673.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=9AEBBC23E2BCB57015999ADD725DD14A9B9C367D9D26D7D113D174B13B5E11CB)

如需切换回原有的经典UI，在界面左上角点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/WcWg3O5qTz2YfX10XiJO8A/zh-cn_image_0000002530753730.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=EDDBBD4252265761C939C025E84655C7DBD9FCA20F18A850CBFD3A72453C8F30)图标，进入**File > Settings...** （macOS系统为**DevEco Studio > Preferences/Settings...**）**> Appearance & Behavior > New UI**，取消勾选**Enable new UI**，点击**Apply**，在弹窗中点击**Restart**重启即可完成切换。

## 菜单栏体验变化

原有固定于界面上方的菜单栏，在新UI中收起到页面左上角工具栏中Main Menu主菜单![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/3mGnO806RmafHilnU7LJFg/zh-cn_image_0000002561753671.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=A19DE428E0780ECBC182DD99B1C2FD1D4D83CFB3CC2F95657A40525DC7689F1B)图标内。点击图标即可展开菜单，继续选择需要执行的功能或操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/A6Jj_J-UTUq1D-CaoyAiVQ/zh-cn_image_0000002530913718.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=88F46AE6832FEF8D7DB7C9036EC572CC348AEAD4550CED920F4D5308FA2E4C3E)

如需将菜单栏展开并固定在主界面，可以在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **UI Options**中，勾选**Show main menu in a separate toolbar**，点击**Apply**在主界面固定显示菜单栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/68264awKQSGri-23BpZSsw/zh-cn_image_0000002530753728.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=49A9826399CCBC0A6CC99FADE920CD9ED8FB9C5B45A746D13AEA163354688783)

## 工具窗口优化

主窗口两侧的工具窗口提供更丰富的功能选择。与经典UI相比，ArkUI Inspector、Services、Terminal、Problems、Version Control等功能图标在左侧工具窗口中呈现。点击工具窗口中Project![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/0glY9rFNTVSU54c93jhBMA/zh-cn_image_0000002530753736.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=0E60FE1F63CAAE5F535F780DCEB4EE5A269596762C8533F555229D08983947C1)图标，显示当前工程目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/KIsoDZMtRRaG6AYR8--FOw/zh-cn_image_0000002561753665.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=107B2DA030E7316C2F69946D835C5C79927B2C9812D8AACE0316AA73B1FFA5EF)

在菜单栏进入**File > Settings... > Appearance & Behavior > Appearance** > **Tool Windows，**勾选**Show tool window names**后点击**Apply**，或将鼠标放置于工具窗口区域右键选择**Show Tool Window Names**，选择在界面中展示各功能图标的名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ak0ry8lKRwKlqfNAffSRrQ/zh-cn_image_0000002561833641.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=0125FC725E8B9CF9112A8CE072BDE41AA73A669CBC5CE490111EE1942A46EBC7)

## 文件路径展示位置变化

在新UI中，当前编辑的文件所在的工程路径将展示在页面左下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/71cRBhRrQnaJnV73L-QNbw/zh-cn_image_0000002530753734.png?HW-CC-KV=V1&HW-CC-Date=20260429T054432Z&HW-CC-Expire=86400&HW-CC-Sign=BB59CB14DFD8A88A55817463D90771900265A904A9DB235F0345156F30A1DA65 "点击放大")

说明

更多新用户界面变化详情，请参见[new UI](https://www.jetbrains.com.cn/en-us/help/idea/2024.3/new-ui.html)。
