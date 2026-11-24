---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-cross-language-code-editing
title: 跨语言代码编辑
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 跨语言代码编辑
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:88347ec6c5df807ecd8f61866cb2df3433a76809f9958266e1822346acfcb1b6
---

## 生成胶水代码函数框架

DevEco Studio提供跨语言代码编辑功能。当开发者需要使用NAPI封装暴露给ArkTS/JS的接口时，在C++头文件内，通过右键Generate > NAPI，快速生成当前函数或类的胶水代码函数框架。

1. 检查当前C++的entry > src > main > cpp路径下，是否已包含napi\_init.cpp文件。如不存在该文件，请在头文件（头文件支持类型：.hpp，.hxx，.hh，.h）中，将光标放置在任意函数名/类名处（当前支持bool，int，string，void，float，double，std::array，std::vector等参数类型），单击右键选择Generate > NAPI，生成胶水代码框架文件napi\_init.cpp。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/BC6Jv2wrShm0axV8YVw-aA/zh-cn_image_0000002779406876.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0101CA4001E83FBEA7BBE4E6916755CC6AFAC915A34E210193E537FA913147F "点击放大")
2. 若工程中已存在或创建完成napi\_init.cpp文件，请在头文件中需要被调用的函数/类名处，单击右键选择Generate > NAPI，将在napi\_init.cpp文件napi\_property\_descriptor字段中分别注册对应的函数/类的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/mP0Hu1KvRLaE4M2W26tobw/zh-cn_image_0000002779566854.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7207ABFA268874F7CAB478622313E5C392CB80DB8A7A783CD6646FA71CD9CCB)
3. 在napi\_init.cpp文件中TODO位置，补充相应的功能实现代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/5PIvpFOLTrOyJV7eWTTtcA/zh-cn_image_0000002808886519.png?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B44F26C761F1FE84961C6788D1B5714A1C936A1A5F1CA047D5EA7D3B11D41DD)

## 跨语言快速生成函数定义

当前支持在跨语言的d.ts文件中，通过Generate native implementation功能，一键生成C++文件中对应函数定义。

将光标悬浮在未定义的函数名处，在悬浮窗中点击**Generate native implementation**，或点击页面上出现的红色灯泡图标，选择**Generate native implementation**，生成函数定义。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/ksLwAKCfSKe-BVIvmneoZQ/zh-cn_image_0000002808886517.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044228Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CDC0A624EAF81515187910EB33D05CED47CCF98FDFED011CF7D5376F95FEC23)
