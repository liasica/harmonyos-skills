---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-138
title: 编译报错“The srcPath is not a relative path：xxx”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The srcPath is not a relative path：xxx”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a73aa36acab1746c3e27a18565fc3b4063420514dc850daa4c3265f535077885
---

**错误描述**

srcPath字段配置值必须为相对路径。

**可能原因**

开发者在hvigorconfig.ts文件中使用includeNode方法时，srcPath必须是相对路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/t5bYQn-MTaGs8RZDESYPpA/zh-cn_image_0000002654837933.png)

**解决措施**

确保项目的hvigorconfig.ts文件中使用includeNode时的传参srcPath为相对路径。

**参考链接**

[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)
