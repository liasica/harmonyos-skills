---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0ac676ed41f7a2dcb939d6c281334c26c970e04a15a8ab3d561cb84db59322b0
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/eY6s1m_nTpuXR1Xy6FnvFQ/zh-cn_image_0000002779567148.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B12A1BE7FD6BF443F2A3B1A8574696F40C2E362D8CD8FB37C559E44D41A7965)

点击“Settings”按钮，设置进制、偏移量和展示的内存字节数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/-UljZt-tQqu4_kJRtw03JQ/zh-cn_image_0000002808886811.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=B97E46671A9EE4E2F1FD974537A4E74CC4E834E03BD9BEF7655E3E02E5A85D02)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4h_v_nXPQLKUkxl3tpMnHQ/zh-cn_image_0000002779407172.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8F4B51D96175B692ABB3C22B6D4E09921CB13019D3ADCA29FBD0084E29BC856)

## 内存修改

您可以在内存格上双击，键入要修改的值来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
