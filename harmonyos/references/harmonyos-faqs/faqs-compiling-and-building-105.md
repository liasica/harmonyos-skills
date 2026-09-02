---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-105
title: 编译报错“no such file or directory, realpath 'xxx'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“no such file or directory, realpath 'xxx'”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6d88f40c51aa460b336e5d9f511211b9c0b3d9f4e0e69f99cd3874179a56106b
---

**问题现象**

DevEco Studio编译时出现错误，提示“no such file or directory, realpath 'xxx'”错误信息。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/gNbAz-BLRuOdk2ppG_YPgQ/zh-cn_image_0000002229758637.png)

**解决措施**

“no such file or directory”是一种常见的错误提示，表示当前工程无法找到指定文件或目录。该错误可能由以下原因引起：

1. 检查报错路径是否真实存在。
2. 检查文件或目录路径的正确性，包括文件名、目录名和字母大小写。
3. 检查权限：如果文件或目录存在，确保工程有足够权限访问。
