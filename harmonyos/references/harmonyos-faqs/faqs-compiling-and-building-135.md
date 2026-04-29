---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-135
title: 编译报错“The service widget file contains one or more references to HSPs”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The service widget file contains one or more references to HSPs”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9332c1302e98185981007dd2e9856a7bb20f273499274f373f18c23dbe1b34b7
---

**错误描述**

服务卡片文件包含一个或多个HSP模块的引用。

**可能原因**

服务卡片文件中引用了HSP模块类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/NS6BHLVASPyCriem3g09hg/zh-cn_image_0000002229758293.png?HW-CC-KV=V1&HW-CC-Date=20260429T062050Z&HW-CC-Expire=86400&HW-CC-Sign=B8441064BB5EF71A30661E19D79CF65A4DF005F9B7EFD7E9061CB06C71C8F399)

**解决措施**

在服务卡片文件中，移除关于HSP类型模块的引用。
