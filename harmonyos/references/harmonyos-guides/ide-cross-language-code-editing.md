---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6e474cdf803ff5f3f0347df51e206108a3714e80080e16f3162caf4d24167c85
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/p-JSRdxmTdaLW6rDrww1Bw/zh-cn_image_0000002530753010.png?HW-CC-KV=V1&HW-CC-Date=20260429T054629Z&HW-CC-Expire=86400&HW-CC-Sign=DBE2D9F1B732A3D39B5900909E3C05887F89898B534231AAC91A2A9FF59C7A45 "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/oSzZyghCQH6-dXHqXmJVeA/zh-cn_image_0000002561752951.png?HW-CC-KV=V1&HW-CC-Date=20260429T054629Z&HW-CC-Expire=86400&HW-CC-Sign=C2FEB2684C5BF63547904589C56EF95FD1673B50C94D01B3030E2E83C3D809A3)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/k4aCBf7FTFyoCwO1L2hKyg/zh-cn_image_0000002530913012.png?HW-CC-KV=V1&HW-CC-Date=20260429T054629Z&HW-CC-Expire=86400&HW-CC-Sign=9167BBA01E99ED385B4A1FCBF20CFE4BF9E7795ACEA85F6F08A21662183116D8)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Id5ymgFcRJeatPVOeyC6xQ/zh-cn_image_0000002530913006.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054629Z&HW-CC-Expire=86400&HW-CC-Sign=BACC5D70CDC15E67FE962EA34E3BE526C93F14D935EC2D045B49B236A7966622)
