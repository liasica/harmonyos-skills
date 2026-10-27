---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-34
title: Native工程中如何使用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native工程中如何使用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:56+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0aeeb03e4bed0ef35093670ef34c1c9fadc780cf0e2d6bd30856f2d45008949f
---

1.将编译好的so库放到Native工程的entry/libs/arm64-v8a/目录下，并将so库对应的头文件放到entry/src/main/cpp目录层级下（可以在cpp目录下增加一个文件夹专门存放三方so库的头文件）。

2.在CMakeLists.txt文件中链接so库。

3.在Native侧 .cpp文件中引入头文件使用so库的相关能力。

示例如下：

在Native侧集成三方库Curl

1. 将移植后的Curl的so库放到Native工程的entry/libs/目录下，并将移植后生成的、包含头文件的include目录放到entry/src/main/cpp目录下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Mn2S8pxiTICszcThkMpj-A/zh-cn_image_0000002654835205.png "点击放大")

2. 在CMakeLists.txt文件中链接Curl对应的so库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/0QJfPwuCTfyicicaAgHcaQ/zh-cn_image_0000002654795271.png "点击放大")

3. 在Native侧.cpp文件中通过引入头文件curl.h来使用Curl的相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/oOk7t4C8Sd-eRxdrV0DKEg/zh-cn_image_0000002624635806.png "点击放大")

**参考链接：**

[在NDK工程中使用预构建库](../harmonyos-guides/build-with-ndk-prebuilts.md)
