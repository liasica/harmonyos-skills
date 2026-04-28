---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-105
title: 编译报错“no such file or directory, realpath 'xxx'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“no such file or directory, realpath 'xxx'”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5cb4d5abe43bdd5a759cc3782148450b3dc15dd0db8bad855c6baad8a51f5ae8
---

**问题现象**

DevEco Studio编译时出现错误，提示“no such file or directory, realpath 'xxx'”错误信息。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/gNbAz-BLRuOdk2ppG_YPgQ/zh-cn_image_0000002229758637.png?HW-CC-KV=V1&HW-CC-Date=20260428T002927Z&HW-CC-Expire=86400&HW-CC-Sign=B007607879DB22163C891D4EE1EDC7A0751798614A7AAEF58B882F97390B8666)

**解决措施**

“no such file or directory”是一种常见的错误提示，表示当前工程无法找到指定文件或目录。该错误可能由以下原因引起：

1. 检查报错路径是否真实存在。
2. 检查文件或目录路径的正确性，包括文件名、目录名和字母大小写。
3. 检查权限：如果文件或目录存在，确保工程有足够权限访问。
