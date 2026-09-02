---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-15
title: LABEL_VALUE_ERROR处理指导
breadcrumb: FAQ > DevEco Studio > 编译构建 > LABEL_VALUE_ERROR处理指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:8dea98c53c93c2809ea79dcee5948c0fc49fb7ee758de57aa3accd58ef2763a8
---

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/6gOUCNkIQECgjbJ8aYcZwA/zh-cn_image_0000002654797843.png)

**解决措施**

该问题由config.json文件的资源引用规则变更引起，需将“label”字段的取值修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/3uzqBCG5R0aoZwSguj4vsw/zh-cn_image_0000002624638388.png)
