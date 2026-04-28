---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-34
title: Native工程中如何使用其他三方so库
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native工程中如何使用其他三方so库
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:34+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7d9326f9cf0aac070f4f7343c44e9176cf8e14eeb11c53a14b4b0c887927719e
---

1.将编译好的so库放到Native工程的entry/libs/arm64-v8a/目录下，并将so库对应的头文件放到entry/src/main/cpp目录层级下（可以在cpp目录下增加一个文件夹专门存放三方so库的头文件）。

2.在CMakeLists.txt文件中链入so库。

3.在Native侧 .cpp文件中引入头文件使用so库的相关能力。

示例如下：

在Native侧集成三方库Curl

1. 将移植后的Curl的so库放到Native工程的entry/libs/目录下，并将移植后生成的、包含头文件的include目录放到entry/src/main/cpp目录下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/kmD3epy2RjCsVXLS4EJ1kA/zh-cn_image_0000002194158760.png?HW-CC-KV=V1&HW-CC-Date=20260428T002433Z&HW-CC-Expire=86400&HW-CC-Sign=60619057FDD17D6D7E16596781BA4BA43744128D3FDB68BA0850C5131E2537BB "点击放大")

2. 在CMakeLists.txt文件中链接Curl对应的so库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/tHkwIzSvT6SIKdFLWe9EKQ/zh-cn_image_0000002194158764.png?HW-CC-KV=V1&HW-CC-Date=20260428T002433Z&HW-CC-Expire=86400&HW-CC-Sign=D33CD83BA350B19665D5098E6F86C6838FFA84DE0F90EA2ABF28AEA4F922610D "点击放大")

3. 在Native侧.cpp文件中通过引入头文件curl.h来使用Curl的相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/7V_lFzBPQVKPBGRcw7TGhA/zh-cn_image_0000002229758629.png?HW-CC-KV=V1&HW-CC-Date=20260428T002433Z&HW-CC-Expire=86400&HW-CC-Sign=3FB559C298F5705575376F9FD6B12F6C8E02FBDC9314CF21687BE058B2255310 "点击放大")

**参考链接：**

[在NDK工程中使用预构建库](../harmonyos-guides/build-with-ndk-prebuilts.md)
