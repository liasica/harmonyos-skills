---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2fe98170c3adf25ade6f48d885b44e7240ddcf44eddf96a898ffafed5fb90cbf
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/ZBTLSO9DTAW23i6Y0XpJYA/zh-cn_image_0000002781311068.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EE6D905CFAB0103DADAC184DDD13294158DD87595DC1E45DD4CC10355876182)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/OpAoSlZbReiPl988BhYLwA/zh-cn_image_0000002781471002.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=542617311244392AC7BF31BDAB512EF43AF536C99CD0EF457685A02279FFB6AA)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/YkkjSL9OSxK8u48DwnDOPQ/zh-cn_image_0000002810750665.png?HW-CC-KV=V1&HW-CC-Date=20261114T004916Z&HW-CC-Expire=31536000000&HW-CC-Sign=3442C81890F904A926F54817BD46E1E20CC616925BCE57D3709D80FD304A4CED)
