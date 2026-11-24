---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-disassembly
title: 汇编调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 汇编调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:619d74b8417be874d52833a1b7fcca1a325ae8574657dd005e6b1a36dd286974
---

鸿蒙电脑DevEco Studio支持查看汇编代码并进行调试，此外，当程序中断到没有源码的位置时（如step into到一个没有调试信息的函数中），DevEco Studio会打开汇编视图，让您了解程序当前停住的地址及对应的汇编码。

## 汇编视图

在某一个堆栈处右键，在弹出菜单中选择**打开反汇编视图**，可以查看该栈帧对应的汇编码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/4HbVWHJAR0KJRMXJlmDkEA/zh-cn_image_0000002820681167.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=83C397211129B5A4DDA6A8DD7E7E3D055B896BCB3AE060664668FA89352D9A59)

汇编视图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/iVD9nt9pSnCQIE7aGOKC7w/zh-cn_image_0000002792001204.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=453CAD3EE4316F0B7B662F5FEF7C5F47C96F98C3AEC6C5B7844B9C04C8584BE4)

## 单步调试

汇编视图下，单步按钮默认以汇编指令级别进行单步调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/BVtaOhQKR7qSySA6MdUh2w/zh-cn_image_0000002791841230.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0C593AD49DE4146E5B8082DCFEE042445757447B77CDEE7372C4621885D68CF)
