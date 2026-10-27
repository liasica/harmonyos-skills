---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-30
title: "工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:46babdbfb414800a82cc509429b86719f8936c78f3e010ebba135981f582f1ef
---

**问题现象**

工程构建时，出现ArkTS语法告警提示，详情请参见FAQ。

报错信息：

1. ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2. ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/cLLnUfdOR52_wLrG72qO9Q/zh-cn_image_0000002624478498.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/3VSMcjwTRKSc_W8fPseURQ/zh-cn_image_0000002654797857.png)

**解决措施**

该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](../harmonyos-guides/arkts.md)
