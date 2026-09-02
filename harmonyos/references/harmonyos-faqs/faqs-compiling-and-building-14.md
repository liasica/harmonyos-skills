---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-14
title: JDK版本不匹配导致编译失败
breadcrumb: FAQ > DevEco Studio > 编译构建 > JDK版本不匹配导致编译失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dfd4128da701b7af14368ca23bd39fedbef12981a274a9d66705412146fc4b91
---

**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/mbapAiSyQEKWlUudpQTDCg/zh-cn_image_0000002229604033.png)

**解决措施**

该问题需使用配套的JDK 17版本解决，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值为JDK 17。如果是Linux系统，可参考命令行方式构建服务或应用的[配置JDK](../harmonyos-guides/ide-command-line-building-app.md#section195447475220)。
