---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187
title: debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
breadcrumb: FAQ > DevEco Studio > 编译构建 > debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d25fde3ef3d1307f2d8a770569c51ec7d17ff3fd08cb7162167d55b1d8a6a306
---

**解决措施**

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/5MCO05-lQ7-THoZ5m1IGJQ/zh-cn_image_0000002372892821.png?HW-CC-KV=V1&HW-CC-Date=20260428T002946Z&HW-CC-Expire=86400&HW-CC-Sign=FC63C0BE0CC55F970C7F672255711285C7CC2165DA5FBE51570DA95CAB8EE9E9)

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

**参考链接**

[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)
