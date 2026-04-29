---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:440c0bcc473b1d7ecaa9d5322a7ec6d51971db134d4fdb4470c388cbb18ce689
---

**错误描述**

针对Hap模块，配置user\_grant权限时必须包含reason和usedScene属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason和usedScene属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ds-dZMcpSx21X36AfQKM1A/zh-cn_image_0000002194158708.png?HW-CC-KV=V1&HW-CC-Date=20260429T062057Z&HW-CC-Expire=86400&HW-CC-Sign=556AC74881CD358064FA004F8424256C7F7F6D32DB965B46AAD574D77BAAC541)

**解决措施**

对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。

对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。
