---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-140
title: 编译报错“Cannot resolved import statement”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot resolved import statement”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fae2197a656341b55349a76c7cc3f0b25f9dbed6f2eea344bccc6f65ca8c6a77
---

**错误描述**

在编译过程中，提示“Cannot resolved import statement”错误信息。

**可能原因**

导入文件时，大小写不一致会导致问题（导入到单个文件夹时，默认寻址小写 “index.ets”文件，但该文件夹下仅存在大写“index.ets”文件）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/rEx4QHk3QsG4mVtpsCeGVA/zh-cn_image_0000002194318384.png?HW-CC-KV=V1&HW-CC-Date=20260428T002936Z&HW-CC-Expire=86400&HW-CC-Sign=23C3F0AB059A56224DE862447B38C098365D70BF725FF341D2CCC545EB090C40)

**解决措施**

检查import文件的大小写。
