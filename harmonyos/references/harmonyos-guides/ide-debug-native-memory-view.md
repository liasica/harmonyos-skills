---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-memory-view
title: 查看内存信息
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 查看内存信息
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:79645bab11238d51104cc97ee54bcb27644c80e778bf228e7c48bf5c3a49c12e
---

在 native 调试窗口中，点击“Layout Settings”，勾选 Memory View ，打开内存查看窗口。

## 查看指定地址内存

在内存视图中，填写地址，点击“View”按钮，查看对应地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/TTZUMwDAQZiCGwmanpq-ZQ/zh-cn_image_0000002561753235.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=A974A3F769445600C593935FBE812AEA7CD00A67CE7A518DEA56E99371BBE109)

点击“Settings”按钮，设置进制、偏移量和内存数量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/4b76BMCeRwud7kSucETzPA/zh-cn_image_0000002530913292.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=A44B5F008732E4A05DE068113DA5A42F29A1DDD0A5CF76E9F7574D0778A916AD)

## 内存转换

通过点击某一个内存格子，右侧会自动将内存内容转换成各种类型的值。您也可以按住并拖动，从而选中多个内存格，以显示这部分内存的 ASCII 码转换结果。

## 查看变量内存

在“Variables”变量列表中的某一个变量处右键，在弹出菜单中选择“Inspect Memory”，自动跳转到内存视图展示变量存储地址处的内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/j-K5mo_lTZqEHeV52syxog/zh-cn_image_0000002561833219.png?HW-CC-KV=V1&HW-CC-Date=20260429T054644Z&HW-CC-Expire=86400&HW-CC-Sign=6857756B3B05BBC07FC927FCAF061A95439A599E195FEB531EEE6EB64682163B)

## 内存修改

您可以在内存格上双击，键入您想要修改的内存来修改对应地址处的内存值；您也可以在右侧的数据转换结果框中输入数据，从而修改该数据对应类型的长度的内存值。
