---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-30
title: 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c7fed068c969aaa43cefff24bedfaa74c0f8d1bf67b0b96b2ccb55389c165b08
---

**问题现象**

工程构建时，出现ArkTS语法告警提示，详情请参见FAQ。

报错信息：

1. ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2. ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/U0KtVJKeQuGB2OpPdvmxWw/zh-cn_image_0000002429325678.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=66E63277EB34E74961702E5907B55FF2200DFFAB8AE00D6AE77BD0771D9F9EFA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/_kzMvndTSRelKakpenBmYQ/zh-cn_image_0000002429485750.png?HW-CC-KV=V1&HW-CC-Date=20260428T002912Z&HW-CC-Expire=86400&HW-CC-Sign=1B86DB16AA3B0BB7C3C60E56B37F1CC13C1750E4585E312435243E63B3558C5B)

**解决措施**

该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](../harmonyos-guides/arkts.md)
