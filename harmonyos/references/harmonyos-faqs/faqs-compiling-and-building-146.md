---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146
title: 编译报错“Invalid form name 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid form name 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2226bdc4d070b6a2876ae6cfa8ca0e98130efcf412e3bdab77a7e336a59b974d
---

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/yJLudJiSQQ-ro0eRJ3iOww/zh-cn_image_0000002194158436.png "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
