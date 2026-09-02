---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:753aa38ef1202fe34049ef8c84e021d612d46cc94ced6361a45eac463c3fb4de
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/z1lGhNJTRtSVoM5y60k2WQ/zh-cn_image_0000002530752758.png)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/vRS-6ksRT7-Q2RvTKKjT9A/zh-cn_image_0000002530912756.png)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-rNjhzKyStCcMBf7nq2DnA/zh-cn_image_0000002561752699.png "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

说明

已经执行完毕的函数不会高亮显示。
