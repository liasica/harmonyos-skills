---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187
title: debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
breadcrumb: FAQ > DevEco Studio > 编译构建 > debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:42bf7ad87a4a7e8c6899ce9026f8a31935ec45a6350451ca7f88c545ddebd4da
---

**解决措施**

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/xR4B3P6ITuijPIGgprAA3A/zh-cn_image_0000002624478700.png)

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

**参考链接**

[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)
