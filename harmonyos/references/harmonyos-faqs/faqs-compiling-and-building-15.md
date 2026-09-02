---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-15
title: LABEL_VALUE_ERROR处理指导
breadcrumb: FAQ > DevEco Studio > 编译构建 > LABEL_VALUE_ERROR处理指导
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7389c9ddbe8fb2d68c0845484d0171c370684b3e97e9fce8f149d3aa92817d7
---

**问题现象**

在工程同步、编译构建过程中，提示**LABEL\_VALUE\_ERROR**错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/BOT4StrJT4SDg_eHY4wuaA/zh-cn_image_0000002229758717.png)

**解决措施**

该问题由config.json文件的资源引用规则变更引起，需将“label”字段的取值修改为资源引用方式。

1. 在**resources > base > element**中的string.json中添加对应的字符串信息。
2. 在config.json中重新引用该字符串资源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/30CC_2ZEQqaXYVia3Q-jMQ/zh-cn_image_0000002194158844.png)
