---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ndk-development-faq-0005
title: 三方SO库版本后缀使用与CMake配置常见问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 常见问题 > 三方SO库版本后缀使用与CMake配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:55+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:fb481a9b6094a2c0602b1d71e817e0666e941d8be0bf1eb6257d279b6a98198e
---

**Q：使用系统的工具链编译 OpenCV 3.1.0 的共享库文件（.so）时，由于生成的共享库文件后缀为 .so.x.y.z，无法直接用于应用包，该如何处理？**

**A**：当前应用的so文件由DevEco Studio打包带入，允许应用通过libxxx.so.x的方式提供so文件。如果需要同时带入两个版本的so文件，real name和so name名字必须相同，明确到主版本号libxxx.so.x，不需要带上.y.z。因此，目前libxxx.so是可以使用的，而libxxx.3.1和libxxx.so.3.1.0需要改为libxxx.x的形式使用。接下来需要在CMakeLists.txt文件中重新配置并编译。

例如：

当引用libxxx.so，libxxx.so.0等后缀类型的so库时，直接在CMakeLists.txt文件中配置即可；

当引用libxxx.so.1.2，libxxx.so.1.2.0等后缀类型的so库时，不能直接将其重命名为libxxx.so后使用，要重命名为libxxx.so.1（明确到主版本号libxxx.so.x），然后在CMakeLists.txt文件中配置使用。
