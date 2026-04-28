---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-78
title: DevEco Studio编译报“Operation not permitted”无权限错误
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio编译报“Operation not permitted”无权限错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5ecbeca3d32c59c4576fd0d0950177fc082e45eece7ce89aebf1b77bb491cf3f
---

**问题描述**

DevEco Studio安装完成后一直报Operation not permitted无权限，具体报错如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/7Rut4BHFSj2PS0HKpLVcGA/zh-cn_image_0000002194158416.png?HW-CC-KV=V1&HW-CC-Date=20260428T002922Z&HW-CC-Expire=86400&HW-CC-Sign=13B7DD80110A6BF4F0D59E402AC43F932FCA9DD7769C4CC0941401BC3801CA13)

**解决方案**

通过以下命令查看是否有com.example.myapplication标识

xattr -l /path/to/es2abc

用以下命令删除该标识

xattr -d com.example.myapplication/path/to/es2abc

根因：mac系统对文件访问有限制
