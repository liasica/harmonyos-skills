---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:49+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:3946f85bf0dfbf44bd58c195776545a71702e3e55108b17439af50c46498ca87
---

DevEco Studio支持查看汇编和汇编代码调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编代码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择“**Disassemble Frame**”，可以查看该栈帧对应的汇编代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/1kvjoObTR5OnRKZwOWs5Fg/zh-cn_image_0000002561753551.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=0A17B7F34051EF3FAD42DFB7684771850F7BA7965927CAA773AB6DACA259CAA4)

支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/bs7_DgzORta_HL6V10kSOQ/zh-cn_image_0000002530913612.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=3777F1CF4DE42A86AC736C8AC0092DFBEE7F0D234061327830DEA58D12A16D9D)

## 汇编断点

可以在汇编视图设置断点，程序运行到对应地址时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/GZJoaO2lRxa0kBFEh0yUGw/zh-cn_image_0000002530753620.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=579733BDAB90A600DEBE4E93C71D971B119A2F470A04EC7E85CEA4A998F4A622)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/sqZuC60eR2aBotxpNX5VIQ/zh-cn_image_0000002530913608.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=63E97A17C6B24B3C1C8DD5597E058BCD75FFEAB8BFF68A2DE6B60BAC2ED1BAB5)
