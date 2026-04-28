---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-135
title: 编译报错“The service widget file contains one or more references to HSPs”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The service widget file contains one or more references to HSPs”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:84525021f372c908cc9cf5faa2a47853f5ee43284ca662fb9239b45dff86d6c0
---

**错误描述**

服务卡片文件包含一个或多个HSP模块的引用。

**可能原因**

服务卡片文件中引用了HSP模块类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/NS6BHLVASPyCriem3g09hg/zh-cn_image_0000002229758293.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=91348CF528CE6109912B26A660B810F4771CF49C66CA44869733E68335F00A57)

**解决措施**

在服务卡片文件中，移除关于HSP类型模块的引用。
