---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146
title: 编译报错“Invalid form name 'xxx'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid form name 'xxx'.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b9fda1db5c540868961427f6cbaad962daa044841ca0e940ed8427e3fc05224e
---

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/BdEqs4FvTMip6NStxGFNnQ/zh-cn_image_0000002654837943.png "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
