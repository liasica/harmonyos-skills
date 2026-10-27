---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-9
title: 加载so库后App出现闪退如何解决
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 加载so库后App出现闪退如何解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:59+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0bb4584497334964c1ed02ae1e818a1481aa30836fffb700b177127e52bf9178
---

## 问题现象

在NAPI项目中链接so后出现APP启动闪退，CMakeLists.txt去除对应so链接后，APP无闪退现象。

## 背景知识

[在NDK工程中使用预构建库](../harmonyos-guides/build-with-ndk-prebuilts.md)时，可以选择使用.so动态库或者.a静态库。so文件是共享库（shared library）的一种格式，程序在运行时动态链接so库中的代码，而不是像.a静态库编译时静态链接。

## 问题定位

1. 查看crash日志。

   如下图，本次闪退为cppcrash，说明so加载链接完成，但是在代码运行时出现错误，根据下图Reason反馈得知由于空指针访问导致的报错。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/3X30TRK3TrCNo8jzR4bc6Q/zh-cn_image_0000002658907821.png "点击放大")

   若闪退并非cppcrash而是jscrash，如下图，则说明js在访问so或者so加载链接出现问题，需要进一步定位。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/dAk06TD_Rte4Y3t_Rr6nHw/zh-cn_image_0000002658787883.png "点击放大")

   ArkTS出错位置和so对外导出的头文件如下二图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/UbaEBDbNS2igFYSpluph_A/zh-cn_image_0000002628388610.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/xWs2YYXjTamwMdy2hNRuvA/zh-cn_image_0000002628548510.png "点击放大")
2. 解压HAP包，查看lib目录下是否存在对应的so文件。
   1. 在HAP文件后添加.rar扩展名，点击压缩文件打开。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/0UA44bkYSAGwDwdLRZloMQ/zh-cn_image_0000002658907823.png)
   2. 查看libs\arm64-v8a目录下是否存在对应的so文件，如果缺失so文件说明在编译链接过程中没有将so文件打包进HAP，需要定位具体原因。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/5xy-p8-TRAiCP8pg-9nnxQ/zh-cn_image_0000002658787885.png "点击放大")
3. 确认HAP中的so文件是真实的库文件。

   由于在不同平台中软链接格式不同，此处以Linux为例。在Linux平台进行交叉编译时，一些源码通过编译链接后会生成多个链接文件，如下图。libjpeg.so/libjpeg.so.62均为链接文件，占用空间很小，而实际的so文件则为libjpeg.so.62.4.0,如果只拷贝链接文件会导致无法链接到真正的so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/dKVsI5KQRnm_s2RLWQW5ag/zh-cn_image_0000002628388612.png "点击放大")
4. 确认so文件依赖so文件均已导入进HAP包中。

   通过readelf -d xxx.so命令可以读取so文件中依赖的so文件，以下图libavcodec.so为例。该so同时依赖了libswreasample.so\libavutil.so\libz.so\libc.so，需要确保如上so均打包进入HAP中或者存在于HarmonyOS的系统库中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qCq6J17eTgGhV-376iztJw/zh-cn_image_0000002628548512.png "点击放大")

## 分析结论

应用打包缺少so动态库文件及其依赖的其他动态库或者错误的so文件均会导致应用在启动过程中闪退。

## 修改建议

1. 修改C/C++源码。

   根据cppcrash反馈的报错原因和堆栈调用定位代码出错原因，修改C/C++源码。
2. 将需要的so放置于libs\${OHOS\_ARCH}目录下。

   将so放置于libs\${OHOS\_ARCH}目录下后，编译HAP时会自动将so打包进去。
3. 重新编译去除so库版本号，避免软链接文件造成干扰。

   修改源码的编译文件，去除版本号的相关定义，重新编译生成库文件。
4. 保障so链接完整性。

   通过readelf等工具排查清楚so依赖的其他库文件，将该so所有的依赖库文件均放置于libs\${OHOS\_ARCH}目录下。
