---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-variables
title: 检查变量
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:45+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ea13dd2b5a4bc2257d76131985037e885ff1248d1b7e58f6a617a56caf49e41b
---

调试时，在“Variables”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击“Edit Configurations...”打开调试配置，在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示全局/静态变量。

## Simplify STL

在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Debugger > C++ Debugger”，通过勾选“Display STL variables as visualization in the Variables Pane”在变量列表中展示简化后的 STL 变量值，或去掉勾选以展示其原始结构。

## 变量监视

在"Watches"列表中输入表达式，然后点击Add to Watches 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/eH6BlrwBR72iMnItB2mkjg/zh-cn_image_0000002561753711.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=9275E5FC22F5FBE4B589D5F8E59F01903AD3A401BFD87FF7AFBEEB31C4B558B3)，或在某个变量右键菜单中的“Add to Watches”添加监视的表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/RnMqh_URSOSJA4sxTxVu6Q/zh-cn_image_0000002561833687.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=3C5328DF75BB693943224B80C671D9D62420970D5A04695F91ACDEFE2E6A5C9B)

## 表达式求值

通过点击“Evaluate Expression...”按钮，或Watches 页面中的输入行中，输入表达式进行计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/nEo7ZA1RScONqmeLiR3X7Q/zh-cn_image_0000002530753770.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=A87D962B018C2257DFE8A7CBE390248F4767F504A6FFFF74AC5A0E7A36702EAC)

## 查看十六进制视图

在“Variables”页面点击鼠标右键，弹出框中选择“Show As Hex Values”，此时页面中的整型变量会以十六进制进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/iHG8z2uuRcuG-dKDgWUfGA/zh-cn_image_0000002530753766.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=A3EA3519EFC52396E4F099B8FBC72154F1FD56853D59A80DDF18983DC283B14C)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/sKsAqjkITnqXlKN_RaYbyA/zh-cn_image_0000002561753707.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=702202D9342E2E1F79A395AF2F7D7A4CFEF5EABBFD5FA0314EAC4B541CD09AF8)

说明

* 无法查看长度超过64位的数据结构。
* 无法查看引用类型返回值。
* Step Out返回的位置存在断点时，无法查看函数返回值。

## 其他说明

对于特定类型的变量，还支持查看bitmap预览、查看较长的字符串等功能。

* ...View Bitmap：支持在调试时查看bitmap预览。

* ...View：支持展开查看较长的字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/pvqWC20OQReUeSBzZoCHXQ/zh-cn_image_0000002530913764.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=0BB9018C2B64D9D51D49188B303E264D3D8842970137F2334BAAD2C5DE856271)
