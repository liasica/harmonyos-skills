---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:33899817acaa43747f37aa731fd68c569d7453da62f442e680f34f2ce5bb3e5f
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/nbSGcAl6TTq8zkW6wtdQAA/zh-cn_image_0000002779728731.png)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1Q1XEIa7TrOkFuYS7UVtfw/zh-cn_image_0000002750009668.png)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/OTnNh3yhSEuO2sIrg7JAHA/zh-cn_image_0000002750169558.png)
