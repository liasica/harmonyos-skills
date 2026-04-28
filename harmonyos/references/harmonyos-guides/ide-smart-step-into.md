---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:51+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:a5925d2c1f8397185192e5de5e022d3cc466e3ff91c349d1da14b791d6700b30
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Fp1XlkCPQG2XRUmfzKHYJQ/zh-cn_image_0000002530752758.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=FD9D22F13BF2965BFF79F303174CC25A1AD6BE5369FD3196FE3DF75CF3D22C86)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/FUUbh8GRR5CVEgOkRrFAzw/zh-cn_image_0000002530912756.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=04E072DC00898A7ADA4E9F44BAC0AA5C2044D77AAADE029C8A9751D72EE2B40D)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/VF7nVtULT9iWyheQtBsG8g/zh-cn_image_0000002561752699.png?HW-CC-KV=V1&HW-CC-Date=20260427T235650Z&HW-CC-Expire=86400&HW-CC-Sign=5BAE9771EC19CB679954B82D2A43E6915D25F387278386989BB20EAA5CCC0D5B "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

说明

已经执行完毕的函数不会高亮显示。
