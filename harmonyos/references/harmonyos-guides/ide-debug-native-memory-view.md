---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cb5ca871bb2cb53fafdadaa00b8c2fcc3060d79c3524076dfc80255abb8031ed
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/_AweQvSdRfaoWrmn6qYAmw/zh-cn_image_0000002779567148.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=215C9D19609C8DB57DFA6C66B7F20A26161F1CC311CFA3D7C59B86252BFBA2F7)

点击“Settings”按钮，设置进制、偏移量和展示的内存字节数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/-bsVfLmlQ6mZsJo8-h-EVw/zh-cn_image_0000002808886811.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E6DEC3C4BE1371C098E923EE16C11798ACDB8C1438AF23C32560A58833ACFD9)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/9TewB6YhSNqzQwl8BnKyzQ/zh-cn_image_0000002779407172.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=094CE62E28A79753AC123C75F3CD02EAD722605F5D294AB740DEBDDCFDAB9965)

## 内存修改

您可以在内存格上双击，键入要修改的值来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
