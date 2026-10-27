---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-143
title: 编译报错“The local dependency below in module %s is invalid”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The local dependency below in module %s is invalid”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:bf4abe59bc63bf4ad9da1348cbdd087a7dd7bab1e26a63b19238d43b62f167a8
---

**错误描述**

模块内添加本地依赖项无效。

**可能原因**

当设置"harLocalDependencyCheck": true时，若har模块添加模块外依赖，将触发该编译报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/W7YA_eJlQ7yZzBfYe8efjA/zh-cn_image_0000002624478628.png)

**解决措施**

设置"harLocalDependencyCheck": true时，确保模块的oh-package.json5文件中，在dependencies和dynamicDependencies下指定的本地依赖都在当前模块目录下。
