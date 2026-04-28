---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8f4540d844f6d295f0273361ac6d689b3c35cd2b7e92ea61986b25b66a991433
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/3hxyt2b5T4OcpVI_9elB9g/zh-cn_image_0000002561753235.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=29802FCD8BF8414E2F2125BC7003ED9D3D6592EF691005D74A09E738B49FDF87)

点击“Settings”按钮，设置进制、偏移量和内存数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/t_fsk_ckTPqTs1lNk01koA/zh-cn_image_0000002530913292.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=AD940D0C0DEA3C3174BCA3D4916D4ECEE295BED4071E9E1103077B7009F32823)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/8yrOPCVZRUmz6PGL24d4FA/zh-cn_image_0000002561833219.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=23CD0DFC4697BC38A8F0A22ADF892E9D28C0D948E515DFDE8E81E225ECDA63CA)

## 内存修改

您可以在内存格上双击，键入您想要修改的内存来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
