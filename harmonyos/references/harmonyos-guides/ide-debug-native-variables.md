---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-variables
title: 检查变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:67b59f6480af923196f1b0f4098ae0e50b2499b8c6575bbdd27b044461b9dcca
---

调试时，在“Variables”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击“Edit Configurations...”打开调试配置，在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示全局/静态变量。

## Simplify STL

在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Debugger > C++ Debugger”，通过勾选“Display STL variables as visualization in the Variables Pane”在变量列表中展示简化后的 STL 变量值，或去掉勾选以展示其原始结构。

## 变量监视

在"Watches"列表中输入表达式，然后点击Add to Watches 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/o7Q9XU7mT-ayVX_GAmNdRQ/zh-cn_image_0000002561753711.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=42F60B2276F01D018A8188F4AC163D10EFB61CEF485009EC8631EF0437349C9B)，或在某个变量右键菜单中的“Add to Watches”添加监视的表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Jfcknl3jTluiCp5HOh4RRg/zh-cn_image_0000002561833687.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=F99E6E406E02289A6F8C4DD23A103150C333A7C9310950F413248E0BB24E4BE7)

## 表达式求值

通过点击“Evaluate Expression...”按钮，或Watches 页面中的输入行中，输入表达式进行计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/zH7HpfQhRcaqnxOTTJS1_A/zh-cn_image_0000002530753770.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=2DABBB6AFCC0C53D3D50C38DCC150DE4A6C8A6975BD649221C8363A5503DEEB6)

## 查看十六进制视图

在“Variables”页面点击鼠标右键，弹出框中选择“Show As Hex Values”，此时页面中的整型变量会以十六进制进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/l7wqyMLtRi-MMmupi9c0ow/zh-cn_image_0000002530753766.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=383E18D9851BA3F6752ED3D577226E85C5ED550A96B43E39AE9614446BE8E8E6)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Hxi_hYlLTyiPuii_0Ofihg/zh-cn_image_0000002561753707.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=3C3F6694BF897F5A4821B01794BFD31712FD16AEFE35C43A58391AAB61CAB8F1)

说明

* 无法查看长度超过64位的数据结构。
* 无法查看引用类型返回值。
* Step Out返回的位置存在断点时，无法查看函数返回值。

## 其他说明

对于特定类型的变量，还支持查看bitmap预览、查看较长的字符串等功能。

* ...View Bitmap：支持在调试时查看bitmap预览。

* ...View：支持展开查看较长的字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/IInWLismQh-ST-ZzF-PZXg/zh-cn_image_0000002530913764.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=9DE07C0759673E3AC0C8DB5821EBBF6262A9C1423334F2F09B4F2D76B19138F6)
