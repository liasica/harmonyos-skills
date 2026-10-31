---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:10+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:640d44ab4220d4ca0e9de646538f1c308f3ef1dd1f9eb94c72c6ba058db97466
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ZJEIZxj9SzyK80ZfhlnnPA/zh-cn_image_0000002779728731.png)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/lr_LZKGuTNi9K1-qX6Orjg/zh-cn_image_0000002750009668.png)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/NBYnYcEPQ4Ga9l7ONsYMOQ/zh-cn_image_0000002750169558.png)
