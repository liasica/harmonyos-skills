---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146
title: 编译报错“Invalid form name 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid form name 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f1edf03206a94b7f5d3f84f391fe638c8c33923b7c1afe5d93be8d9377f794af
---

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yJLudJiSQQ-ro0eRJ3iOww/zh-cn_image_0000002194158436.png?HW-CC-KV=V1&HW-CC-Date=20260428T002939Z&HW-CC-Expire=86400&HW-CC-Sign=826219531621B7832FBDD0415C6DAA490F5910FE4E7EE74960F9E647E27DF1D3 "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
