---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187
title: debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
breadcrumb: FAQ > DevEco Studio > 编译构建 > debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ea3730faab4e91cf537fc252846585e5c33b85a062f20560738c42112234868c
---

**解决措施**

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/5MCO05-lQ7-THoZ5m1IGJQ/zh-cn_image_0000002372892821.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=CDD082F3571006C39B14959FADA7D0D197EB77B43AAAC2B97A9D9FC9210C4C6F)

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

**参考链接**

[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)
