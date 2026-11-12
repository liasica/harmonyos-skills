---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4abbe65f9c52a93c034041f8c7e2b83c697fb7a15e607e1dbeeaa3b6a7071ea5
---

DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编代码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择“**Disassemble Frame**”，可以查看该栈帧对应的汇编代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/di0bp7V9QKqccEfLz57DsA/zh-cn_image_0000002808887169.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E2BB11A908A60EC1E8C653FB58645D135A8B1BDAA8CE65EA7D5E69C5F02EDCA)

支持在汇编视图中展示源码、函数名，可以跳转到对应源代码，汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/N4pK-2AcQGu5L4FeT72RBw/zh-cn_image_0000002808767085.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8206414414951760527FCFD21039D81C7A9A73BEFA1D9D1BD904BC4CB5DBE3FC)

## 汇编断点

可以在汇编视图设置断点，程序运行到对应地址时中断。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/UGAPLBdnQwq_fJyYTjSHcg/zh-cn_image_0000002779407530.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1503DC313FB6E20E6E29EE20EB85C74199DA0182A117972217F074B3B73FC17D)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/FmoH2rRySDKfKtVD5RMjxA/zh-cn_image_0000002779567506.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=62413206D9A9A32705867D3AA2224FD16EA1442456364AC9E0678D9C3F3DCB6E)
