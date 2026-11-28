---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-variables
title: 检查变量
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 检查变量
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0c1213e10302840612e238f3cc0245117a1d420fb90ecf6ce67b02b4e6cb1578
---

调试时，在“Variables”页面查看变量，支持查看全局/静态变量、寄存器变量和局部变量。

## 查看全局/静态变量

点击“Edit Configurations...”打开调试配置，在 native 调试配置界面中勾选“Show static/global variables in the Variables Pane”，调试过程中变量列表会展示全局/静态变量。

## Simplify STL

在菜单栏点击“File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Debugger > C++ Debugger”，通过勾选“Display STL variables as visualization in the Variables Pane”在变量列表中展示简化后的 STL 变量值，或去掉勾选以展示其原始结构。

## 变量监视

在"Watches"列表中输入表达式，然后点击Add to Watches 图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/LaEDea7sQWGi7VmLjDBedA/zh-cn_image_0000002808886967.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=57961FC938FD42BBC76DD3DBA232542600A1E269E3FE119F7E727B20318E4C2A)，或在某个变量右键菜单中的“Add to Watches”添加监视的表达式，在每次程序停住之后会计算表达式的值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/p4lY3uKERZmnYTGr04a0iQ/zh-cn_image_0000002779407324.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=1933995E15454385256E9EC2BCA99327F8C3E4238980EDF73602B8B810B4FC4A)

## 表达式求值

通过点击“Evaluate Expression...”按钮，或Watches 页面中的输入行中，输入表达式进行计算。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/J6E3Vc5BRByZ3hthHWk2iw/zh-cn_image_0000002779567304.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=64F7CE8F0AE53D0CDDBC213F6CCED245D83FB00CAFA168A749832F270CC20E8A)

## 查看十六进制视图

在“Variables”页面点击鼠标右键，弹出框中选择“Show As Hex Values”，此时页面中的整型变量会以十六进制进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/eO-9TQF6R8mnWhQLC1qe1Q/zh-cn_image_0000002808766881.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3854F86FDEADF2F26E2205C075248ABCEBC9021E568292A7593A009FD4605A8)

## 查看函数返回值

当使用“Step Out”从一个函数内步出后，变量列表中的“ReturnValues”会展示所步出函数的返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/Ca6MMtVvR-WtwP9G6biHSQ/zh-cn_image_0000002779567302.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=84057D25191F1AA4B8C1088CAC5739A96ACCDCE55B8B191F55B5DB6CC01CFD48)

**说明** 

* 无法查看长度超过64位的数据结构。
* 无法查看引用类型返回值。
* Step Out返回的位置存在断点时，无法查看函数返回值。

## 其他说明

对于特定类型的变量，还支持查看bitmap预览、查看较长的字符串等功能。

* ...View Bitmap：支持在调试时查看bitmap预览。

* ...View：支持展开查看较长的字符串。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/uYAC6WL2RKq51P_IEKqfoA/zh-cn_image_0000002808766885.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D737BF6FE3F2C51C8D600C7937D9626DEE307A79B63DD56DF9739EF2248B362)
