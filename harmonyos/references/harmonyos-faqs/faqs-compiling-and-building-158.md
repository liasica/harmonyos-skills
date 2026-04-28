---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3194ade44460cf5578eb5f62c130edd9e39fe98fb5f7d278cd20be22e16bd0fd
---

**错误描述**

针对Hap模块，配置user\_grant权限时必须包含reason和usedScene属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason和usedScene属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ds-dZMcpSx21X36AfQKM1A/zh-cn_image_0000002194158708.png?HW-CC-KV=V1&HW-CC-Date=20260428T002942Z&HW-CC-Expire=86400&HW-CC-Sign=3238060B55C06CCE9F3229C8D932FD683D6645BCC8F023D7AB86F3A5C2531FDB)

**解决措施**

对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。

对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。
