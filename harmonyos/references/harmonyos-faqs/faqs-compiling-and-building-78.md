---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-78
title: DevEco Studio编译报“Operation not permitted”无权限错误
breadcrumb: FAQ > DevEco Studio > 编译构建 > DevEco Studio编译报“Operation not permitted”无权限错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:941455d4a608426a93fc2e04d5edec1c8f333bddf3ab5cb804afe7c204c7a66f
---

**问题描述**

DevEco Studio安装完成后一直报Operation not permitted无权限，具体报错如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/7Rut4BHFSj2PS0HKpLVcGA/zh-cn_image_0000002194158416.png?HW-CC-KV=V1&HW-CC-Date=20260429T062037Z&HW-CC-Expire=86400&HW-CC-Sign=9FCF5AAB566BCF2392FD8C2A9D888EA41481CC8301A6C47E95B36C8609027792)

**解决方案**

通过以下命令查看是否有com.example.myapplication标识

xattr -l /path/to/es2abc

用以下命令删除该标识

xattr -d com.example.myapplication/path/to/es2abc

根因：mac系统对文件访问有限制
