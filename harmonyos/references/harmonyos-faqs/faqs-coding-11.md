---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-11
title: 如何过滤编辑器对超大文件的扫描
breadcrumb: FAQ > DevEco Studio > 代码编辑 > 如何过滤编辑器对超大文件的扫描
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:958427173d49688c5e0056631018c8425e772c45e61a2ea01efdef3a3da1d162
---

**问题现象**

在工程中，如果存在由ProtoBuf等工具自动生成的超大源码文件（例如，超过十万行的源码文件），编辑器在扫描和加载这些文件时会占用大量系统运行内存。如果不需要在这些文件中使用代码编辑功能，可以通过配置编辑器来限制扫描单个文件的最大大小，从而进行过滤。

**解决措施**

以过滤大小超过10 MB的文件为例，通过DevEco Studio菜单栏的“Help > Edit Custom Properties...”选项，打开idea.properties配置文件，在文件中新增一行arkts.server.max.intellisense.filesize=10240，然后重启DevEco Studio。编辑器将过滤大小超过10 MB的文件。arkts.server.max.intellisense.filesize字段应配置为大于0的整数值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/cCmZbDRmS6awXRcLgDshxA/zh-cn_image_0000002194318272.png?HW-CC-KV=V1&HW-CC-Date=20260429T062014Z&HW-CC-Expire=86400&HW-CC-Sign=585ACE49281B63A6C93BC667587E3177DB2AD4E72FA7E85883FCE4EAECAFB854)
