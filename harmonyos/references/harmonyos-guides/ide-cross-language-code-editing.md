---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:38b1c4002ed3418868eaed7c8b1296fdd4390e2c4fe30422dd060c4dd06ea455
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/ZTxfpu-hQm-jAWwAAHi_0w/zh-cn_image_0000002779406876.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4C5D7FA6C415D95A9EBE9137E4F75ADD45CEA23EFA746DA435D2C6F63398705 "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gYx47a8ORKuenKQCrNA2QA/zh-cn_image_0000002779566854.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=7356D02717FCD7108C79D4B9A5127FD16A7D8D7D5152767D2EBFEE3A474C0C88)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/4p4VQoPqSoKzs1OU4gaKUg/zh-cn_image_0000002808886519.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CED7A6AACDE3D634ED7A90C3FB01116EF53D5A9C1D93BAA64E1D7E01BE8B292)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/fHMxh_JJRRCLA0-fFINrUQ/zh-cn_image_0000002808886517.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=31EDA193C568A20257AA96DC8CF6C53F76670711D300BEB4AE081BD3BA17EAE6)
