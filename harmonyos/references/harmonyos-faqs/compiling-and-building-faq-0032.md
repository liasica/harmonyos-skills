---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0032
title: HAP/HAR/HSP包编译常见问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > HAP/HAR/HSP包编译常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7c311b446e82a978783b259fec0726f4f84a9728f68be85ab88283c6d8a1c11e
---

**Q：从包管理的角度，保证代码安全的措施有哪些？**

**A**：从包管理的角度，保证代码安全的措施如下：

* 编译：编译时，HAR和HSP支持代码混淆。
* 打包：打包时为每个HSP/HAP单独签名，签名后的应用才允许安装。
* 安装：终端设备上的应用市场用于安装和卸载应用，不支持其他安装方式。
* 运行时：提供应用沙箱机制，这是一种以安全防护为目的的隔离机制，防止数据遭受恶意路径穿越访问。

参考链接：[混淆加固](../harmonyos-guides/ide-build-obfuscation.md)，[Stage模型应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)，[应用安装卸载与更新开发指导](../harmonyos-guides/application-package-install-uninstall.md)，[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。

**Q：以libstd为例，C++的标准库放在哪里了，有没有打到hap包中？**

**A**：libc++\_shared.so被打包到应用目录下，每个应用都有一份独立的文件。

**Q：HSP/HAR包中如何引用外部编译的so库文件？**

**A**：操作步骤如下：

1. libxxx.so库文件放入HAR或HSP的libs/arm64-v8a目录。设备类型不同时，需添加对应子目录。新版的arm64为libs/arm64-v8a，老版的arm64为libs/armeabi-v7a，x86模拟器为libs/x86\_64。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/U29gmM7XT2KXWZ7hWv2QTA/zh-cn_image_0000002803249445.png)

2. 在src/main/cpp/CMakeLists.txt文件中链接so库文件。例如：target\_link\_libraries(entry PUBLIC libxxx)。

**Q：HSP打包后，为什么会生成HAR包，它是否会导致App包大小膨胀？**

**A**：HSP编译生成的HAR包仅包含配置文件和接口定义，不包含代码逻辑。该HAR包仅用于开发阶段，不会影响App包的大小。
