---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:af26d46a77c19c34a16d142c07949855245fb78d2781ecb4800ff01d5a9ff922
---

DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编代码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择“**Disassemble Frame**”，可以查看该栈帧对应的汇编代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/NApI2jsmQOSXOIRaO9xbsw/zh-cn_image_0000002808887169.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCB0A95E6C66A614E817C4CB0E9D1361F6F6A2997B16D07C5C8D62065263C7D5)

支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/D6-7o8qBSgWNon-9iO8eEQ/zh-cn_image_0000002808767085.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=00F0B6C5C0D1F8D62DD0476EA6873FBFF892CC289DB645BBFDA9625987C80607)

## 汇编断点

可以在汇编视图设置断点，程序运行到对应地址时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3_vXKQbDR1KDtWLSTjXQ9Q/zh-cn_image_0000002779407530.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BEF1F939E9AFBA388195C0FBF7B5439319339DE2F6047845FB2DD2FE8B4B6A0)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/wL5Cjma-Qhe9dTv-IHzz-A/zh-cn_image_0000002779567506.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB2D9B30462FEBCE652525526B928B8872ADA404813E4C3004E2BBE36D14F11A)
