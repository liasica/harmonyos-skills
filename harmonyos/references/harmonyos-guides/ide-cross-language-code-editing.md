---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:efde28454abb23bf3fe41e19862c35bdd864a7d0e61e9c225e3e6998895291f3
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/esftXwDSSGCYW8GsL2ONjw/zh-cn_image_0000002731542361.png "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/6woBA-8gS9GRG61l0dGgwg/zh-cn_image_0000002701663166.png)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/WA5pRzvmSdCF9bUaZlhAjA/zh-cn_image_0000002701823090.png)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/w2kM1HCkQzmGQ7xjvFHPQQ/zh-cn_image_0000002731382389.gif)
