---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-28
title: 编译构建时报错：签名工具错误问题汇总
breadcrumb: FAQ > DevEco Studio > 签名服务 > 编译构建时报错：签名工具错误问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b80a64e1c59e505b85d6ff78dca7dae11104065be1c6b4eea80fad1ec48a6e37
---

## 问题现象

场景一：

编译构建时报错：The keystore was created by a newer JDK version,please use the same JDK version.。

场景二：

编译构建时报错：No signing certificate "iOS Development" found。

场景三：

项目包名修改后安装时报错：BundleName in the project configuration does not match that in the SigningConfigs.。

场景四：

上传软件包时提示：The app package is not signed. Check the build environment to make sure you have used the signature file.。

## 背景知识

* 由于签名工具基于Java语言开发，需要在Java环境运行。参考：[应用包签名工具](https://gitee.com/openharmony/developtools_hapsigner)。
* [配置调试签名](../harmonyos-guides/ide-signing.md#section54361623194519)。
* [工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md)。

## 问题定位

场景一：

根据报错提示：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app，推测是本地的JDK版本低于DevEco自带的JDK版本。检查DevEco Studio和本地配置的JDK版本。

场景二：

从报错信息看，核心问题是签名证书缺失。

场景三：

app.json5中包名已经修改，但工程级build-profile.json5配置文件仍绑定旧包名的签名文件。

场景四：

检查build-profile.json5文件products中是否配置了signingConfig字段，该字段用于指定产物对应的签名配置。

## 分析结论

场景一：

当前使用的JDK版本和生产密钥对使用的JDK版本不匹配。

场景二：

签名证书缺失，导致编译流程中断。

场景三：

确认项目包名与签名配置不匹配。

场景四：

build-profile.json5文件products中缺少signingConfig字段，导致软件包未签名。

## 修改建议

场景一：

常见出错场景：

* 使用IDE生产密钥对时，IDE默认会调用软件内预置的JDK，而用户使用本地的低版本JDK进行签名时则会报错。
* 用户本地使用高版本JDK生成密钥对时，又通过IDE进行签名，IDE中预置的JDK版本低于用户的JDK，导致报错。

解决方案：

检查当前使用的JDK版本和生产密钥对使用的JDK版本，使用版本匹配的JDK执行签名命令。

配置JDK方法：[配置方法](../harmonyos-guides/ide-command-line-building-app.md#section195447475220)。

场景二：

重新配置签名，参考：[配置调试签名](../harmonyos-guides/ide-signing.md#section54361623194519)。

场景三：

修改包名后需要在build-profile.json5中把signingConfigs属性值删除，然后同步后重新签名才可以安装成功。

场景四：

在[工程级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)的products中添加signingConfig字段，指定对应的签名配置名称，重新编译构建后即可正常上传软件包。
