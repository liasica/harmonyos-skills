---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:37+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c3d889d95aa67540f26c5cb4142c05954a9dc1b281cedaba496cb3e34c56c48c
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/whlzoseDTditUh_Lp_V0Kw/zh-cn_image_0000002779406876.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C8EF175C55319E038FC652F5384E2870CA3EAA25653A14C38A089F0A41E22E6 "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/eEOAqnHDRFmhZy3vJjuFrw/zh-cn_image_0000002779566854.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BA5C0C646896D2BD11E3224B81CA33EBE2580C6228DF993178F594F1417ECFE)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/WmHv2s64S_auvi5U2lChiQ/zh-cn_image_0000002808886519.png?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=663BE495A2D84F9A31D3901505C6436CE11031E7A30BAAE7C278A7E0C503BB3B)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/iWMsH4iYSYiz84677GULZg/zh-cn_image_0000002808886517.gif?HW-CC-KV=V1&HW-CC-Date=20261128T023437Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D2672C37C9B7EA2C1C929AE6B77981B922FA18F0E71E1A9278F232C5F09764B)
