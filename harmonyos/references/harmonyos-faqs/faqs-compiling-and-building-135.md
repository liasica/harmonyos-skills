---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-135
title: 编译报错“The service widget file contains one or more references to HSPs”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The service widget file contains one or more references to HSPs”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:8addd3af20833f0ac3855033a3611395f56f9fb571d9cf3adb8272788219095d
---

**错误描述**

服务卡片文件包含一个或多个HSP模块的引用。

**可能原因**

服务卡片文件中引用了HSP模块类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/_cNJEj3cQ1aqvnKMlOzxGA/zh-cn_image_0000002654837929.png?HW-CC-KV=V1&HW-CC-Date=20261112T233207Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC340D080BBC164F3678A955756527667A428244AC34A10420942677DC442132)

**解决措施**

在服务卡片文件中，移除关于HSP类型模块的引用。
