---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eb47c446e1387fa914540c6f1961286582356f1016ce6c54c87f0114688e8a16
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/yb3_AvyIQEa6n0oPzzLLRA/zh-cn_image_0000002779406508.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=B25257056B339AB6C0865461656E8FB40009272242C1433FFDECCDC2679169FC)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/byo59k4PQLOw3t6LMRTqCA/zh-cn_image_0000002779406510.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=405E9EA8A84612AB887A80220FF0F9B81B70D6957B7B23CAB9859BDE9EA0A695)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/7qnyb8PDQhu8y-mayPQKXg/zh-cn_image_0000002779566486.png?HW-CC-KV=V1&HW-CC-Date=20261114T004859Z&HW-CC-Expire=31536000000&HW-CC-Sign=83BF8EE5456C8569AFACA8443B6D5539C34B511A8A36C65DD3D2A7119FA987CD "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

**说明** 

已经执行完毕的函数不会高亮显示。
