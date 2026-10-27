---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-51
title: 使用hdc命令安装release HAP包到设备时上报“INSTALL_FAILED_APP_SOURCE_NOT_TRUSTED”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 使用hdc命令安装release HAP包到设备时上报“INSTALL_FAILED_APP_SOURCE_NOT_TRUSTED”错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:46+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:5a43ba5e7366b43b6b2cfe95bc4264321fa01b58b5e7782101e0c53b489c97d0
---

**问题现象**

release HAP包用hdc命令安装到手机上时报错："INSTALL\_FAILED\_APP\_SOURCE\_NOT\_TRUSTED"。

**解决措施**

HarmonyOS 开发者中心发布的证书仅支持上架使用，不支持本地安装。签名中心只为预置应用申请Profile，不支持本地调试。

**参考链接**

[调试概述](../harmonyos-guides/ide-debug-device.md)
