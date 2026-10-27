---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-78
title: DevEco Studio编译报“Operation not permitted”无权限错误
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio编译报“Operation not permitted”无权限错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:f688a4d8598054d445e198282c500cc75645a6001e50b65fa83035c8fcab9150
---

**问题描述**

DevEco Studio安装完成后一直报Operation not permitted无权限，具体报错如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Ah_lnK6jSiGt0JQKarja8Q/zh-cn_image_0000002654797899.png)

**解决方案**

通过以下命令查看是否有com.example.myapplication标识

xattr -l /path/to/es2abc

用以下命令删除该标识

xattr -d com.example.myapplication/path/to/es2abc

根因：mac系统对文件访问有限制
