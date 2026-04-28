---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-14
title: JDK版本不匹配导致编译失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > JDK版本不匹配导致编译失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4ef85f2e30ff5d2458868b3232ec9a19ef79f8ec6aaad9f6d13f8defba6f2452
---

**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/mbapAiSyQEKWlUudpQTDCg/zh-cn_image_0000002229604033.png?HW-CC-KV=V1&HW-CC-Date=20260428T002908Z&HW-CC-Expire=86400&HW-CC-Sign=06D525CF2506DB66D6B7F57E437D4C8652CC226BB776FAAF823698F31D09D2F2)

**解决措施**

该问题需使用配套的JDK 17版本解决，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值为JDK 17。如果是Linux系统，可参考命令行方式构建服务或应用的[配置JDK](../harmonyos-guides/ide-command-line-building-app.md#section195447475220)。
