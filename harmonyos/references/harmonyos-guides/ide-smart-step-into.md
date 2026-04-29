---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smart-step-into
title: 智能步入
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 智能步入
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:47+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:8f7d8263ae153a1e87de49a7291432fd049e59ae7d34c8b86bbe83273788d6b4
---

进行C++调试时，当前代码行有多个函数调用时，开发者可以使用Smart Step Into功能![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/z1lGhNJTRtSVoM5y60k2WQ/zh-cn_image_0000002530752758.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=3F7719CC8C5D1578FD35F4CEF6F5F30C5CECE3BBA78E4EEDA42F8C19A69DDAC8)直接Step Into到其中某一个函数的实现中。

## 操作步骤

通过点击调试窗口“entry-Native”调试器下的Debugger窗格中的按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/vRS-6ksRT7-Q2RvTKKjT9A/zh-cn_image_0000002530912756.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=E4FA2BCF6F9D10C9AEC8729A1B4FD0D3D34DA20081AAC1B040791035F9EBABBF)（或使用快捷键**Shift+F7**）触发Smart Step Into功能后，DevEco Studio会将当前代码中可以进行跳转的函数进行高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/-rNjhzKyStCcMBf7nq2DnA/zh-cn_image_0000002561752699.png?HW-CC-KV=V1&HW-CC-Date=20260429T054646Z&HW-CC-Expire=86400&HW-CC-Sign=A4546AAECD37C6475F56A9D6C23B22A2C4CA957972A7CF1CEB921613765D34F4 "点击放大")

开发者点击需要跳转的函数，程序会运行到目标函数的实现内。

说明

已经执行完毕的函数不会高亮显示。
