---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146
title: 编译报错“Invalid form name 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid form name 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:34f3af1530ba6cd658da734219b43cdd7b9900086cbea26bd71bfc0bd329666e
---

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yJLudJiSQQ-ro0eRJ3iOww/zh-cn_image_0000002194158436.png?HW-CC-KV=V1&HW-CC-Date=20260429T062053Z&HW-CC-Expire=86400&HW-CC-Sign=07EB032F499185DB540C2F420C597A2B3A7644000749BA62857817F42E63654B "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
