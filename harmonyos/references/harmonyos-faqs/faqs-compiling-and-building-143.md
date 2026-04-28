---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143
title: 编译报错“The local dependency below in module %s is invalid”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The local dependency below in module %s is invalid”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e73406d68c0520e9cbf9ec7bfdf114a25ed9d317d125df68ed89e479497f0185
---

**错误描述**

模块内添加本地依赖项无效。

**可能原因**

当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/33p9S488ScOWso6_JGSR8g/zh-cn_image_0000002194158324.png?HW-CC-KV=V1&HW-CC-Date=20260428T002938Z&HW-CC-Expire=86400&HW-CC-Sign=1172E191FD0DE30A1DAA63ED83DD11CF4E92CF18330D57F6E90E482E6AD57E63)

**解决措施**

设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。
