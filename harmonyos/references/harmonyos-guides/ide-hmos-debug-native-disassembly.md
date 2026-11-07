---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b03d6f22ce8026ef897663d5af7a9a06578c5024dd493726e8f405951b7f08b5
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ca_K3CAfRdmObePot8pcYw/zh-cn_image_0000002781311068.png)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/N7gVnaV4RV-MPYVjiklrGA/zh-cn_image_0000002781471002.png)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/A4IXagzjQIuLCc1pdt8Ywg/zh-cn_image_0000002810750665.png)
