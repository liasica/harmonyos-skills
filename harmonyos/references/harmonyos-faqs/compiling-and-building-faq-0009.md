---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0009
title: Release包混淆开启后运行异常问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > Release包混淆开启后运行异常问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:9cddcd6a1cd20d971a295c051661d7c6a41a7acaa084da35894e7b96c039e506
---

**Q：debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃，如何排查？**

**A**：解决措施：

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/hwNzP_yfRsmfnXq1C8xkpw/zh-cn_image_0000002765026946.png "点击放大")

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

参考链接：[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)。
