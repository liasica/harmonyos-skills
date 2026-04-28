---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159
title: 编译报错“The reason attribute are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason attribute are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5732e1fdb30af55ad5ecee02f7529401d35c2af79d3cc13277a01ce70fc60427
---

**错误描述**

针对Har和Hsp模块，配置user\_grant权限时必须包含reason属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/RHhkA6FERNeu3dvBOKCW9w/zh-cn_image_0000002229758313.png?HW-CC-KV=V1&HW-CC-Date=20260428T002942Z&HW-CC-Expire=86400&HW-CC-Sign=BEBF46700CD07015AEAEE440A27F414438D6E49D2112AA5D6D36E8416C9CCAA8)

**解决措施**

hap模块的module.json5文件中添加reason和usedScene字段。

在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。
