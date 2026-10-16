---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:d2bd67ea176601d0984b1f929a46f385cb21e60f61d6e592b784269905b09781
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/w5j0LGC8SwG4uvfb4WMhvA/zh-cn_image_0000002779728731.png)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/CZ7nafKcR1qql4R6onvSTQ/zh-cn_image_0000002750009668.png)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/BSZg7qoUQein9f3m73VBkw/zh-cn_image_0000002750169558.png)
