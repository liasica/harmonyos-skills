---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159
title: 编译报错“The reason attribute are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason attribute are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:df5e2f8f23159557d6b986e23e0bd17ddac9761f95f400c2c83f9e931df231ff
---

**错误描述**

针对Har和Hsp模块，配置user\_grant权限时必须包含reason属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/RHhkA6FERNeu3dvBOKCW9w/zh-cn_image_0000002229758313.png?HW-CC-KV=V1&HW-CC-Date=20260429T062057Z&HW-CC-Expire=86400&HW-CC-Sign=3E495E42C6A9146B68B11156EC2879C3568B5BE5FC8B47EC48495E20F2824F0F)

**解决措施**

hap模块的module.json5文件中添加reason和usedScene字段。

在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。
