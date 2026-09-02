---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:45+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:48e259ad320ed42c3117e35e4241c70ccafa0a89ddb1d8fe87f92aa01618081d
---

DevEco Studio支持查看汇编和汇编代码调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编代码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择“**Disassemble Frame**”，可以查看该栈帧对应的汇编代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/Ull6Vz3aSg-2Q_uTCslBBw/zh-cn_image_0000002561753551.png)

支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/b8PfT0lmTEu5nmVyip3DMQ/zh-cn_image_0000002530913612.png)

## 汇编断点

可以在汇编视图设置断点，程序运行到对应地址时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/qZqBVk8UR1WhlKCjxYYiAg/zh-cn_image_0000002530753620.png)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/3y-koEQySl-WfEy3nkLE3A/zh-cn_image_0000002530913608.png)
