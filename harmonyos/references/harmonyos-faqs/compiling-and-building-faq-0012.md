---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0012
title: JDK版本不匹配导致编译失败问题排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > JDK版本不匹配导致编译失败问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d29c6dd4018cb2dde0cffb2a9c33dab6abb85b83bdf73d88da583b926b95adb5
---

**Q：通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/5CF6a3TlQjOo-NlyhKS9Ng/zh-cn_image_0000002799531795.png "点击放大")

**A**：该问题需使用配套的JDK 17版本解决，请根据如下方法进行修正：

1. 下载并安装JDK 17版本。
2. 修改JAVA\_HOME环境变量，取值为JDK 17。如果是Linux系统，可参考命令行方式构建服务或应用的[配置JDK](../harmonyos-guides/ide-command-line-building-app.md#section195447475220)。
