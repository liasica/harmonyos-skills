---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143
title: 编译报错“The local dependency below in module %s is invalid”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The local dependency below in module %s is invalid”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5c5d8e735f81c434a8147cdf6400048df43e2e9437a5d91e05abc341e4d61838
---

**错误描述**

模块内添加本地依赖项无效。

**可能原因**

当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/33p9S488ScOWso6_JGSR8g/zh-cn_image_0000002194158324.png?HW-CC-KV=V1&HW-CC-Date=20260429T062053Z&HW-CC-Expire=86400&HW-CC-Sign=F7A1A5DD37B2489AA1AE30064B119D1A90EC6AB98896A79E82674AEE5E7B405A)

**解决措施**

设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。
