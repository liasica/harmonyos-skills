---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:57+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:097ff5f2287a27971aad1f31a51644de61f8c0c452bec7a19de954241d1a9974
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/VHlSC7FERx-M6bSoYEdfHw/zh-cn_image_0000002779406876.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=F64D8D6E06F6BCBF0A0D2DAD7647E706BC4F54F84C908AD7180647FD5EF78E26 "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/UGU-cLGQRHqrrHM1Q__d2w/zh-cn_image_0000002779566854.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=3CE4C5D369A68C1009A591C06188BA6ACD25154EDE54C426B49FD671BD5332D0)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/RFWzv3kPRbqexse3kqa0QA/zh-cn_image_0000002808886519.png?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8A4F676538BEAF561655B3043CC0D110EE29D8B5775C6C2728323BE86FB79B2)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/0-C10gVST32PYXsKFAA_Mw/zh-cn_image_0000002808886517.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004857Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD63048B56242AFBEDE24667B805A2BCC3E9AB8548CE032F1FC3EBF3E075239E)
