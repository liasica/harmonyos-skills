---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-26
title: 如何使用DevEco Studio进行C/C++代码断点调试
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何使用DevEco Studio进行C/C++代码断点调试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4fd266fc3f7577309174398c4c2338a8e529287b0957220fc158dd9cd60aad8c
---

**问题现象**

在DevEco Studio上的C/C++代码处打断点，调试运行时断点不生效。

**可能原因**

DevEco Studio进行ArkTS/JS + Native混合调试时需要配置DevEco Studio的调试模式。

**解决措施**

选择配置项：Run/Debug Configurations > Debugger > Dual(ArkTS/JS + Native)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/6E8uYcKBQ2akATLeiKBPBQ/zh-cn_image_0000002654838117.png "点击放大")
