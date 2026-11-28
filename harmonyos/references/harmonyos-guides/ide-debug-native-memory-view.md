---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5d1d6802d75741a96242ab23ed8e7324030b80ab8c0d2132e7e38b438973fa96
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ijVinVqdQyuU4rrYymORGQ/zh-cn_image_0000002779567148.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F832197355719E3C18595379CF66A39068D14031B5E848B7FBF3BBEA2C05FA0)

点击“Settings”按钮，设置进制、偏移量和展示的内存字节数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/7GBBXM0GQzidznUcxcdtpA/zh-cn_image_0000002808886811.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4A97DA42D109D94878B4C51434EA020F9C4016E2D7158B1C8149F612D9E24BD)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/u_nnI2buRgSZdyDbwKCnyA/zh-cn_image_0000002779407172.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=933FF039C23E03757911672D02A44A76060676EE99B37B71A3152C6DC49455C5)

## 内存修改

您可以在内存格上双击，键入要修改的值来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
