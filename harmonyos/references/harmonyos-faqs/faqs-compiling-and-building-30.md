---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-30
title: 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:064548834bf874fd4ebf0fe0cf87ebfa0de77a865c5b7afd52415b7495156e0c
---

**问题现象**

工程构建时，出现ArkTS语法告警提示，详情请参见FAQ。

报错信息：

1. ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2. ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/U0KtVJKeQuGB2OpPdvmxWw/zh-cn_image_0000002429325678.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=7ED1552F555F6DAA276AD3110C26C2519BDAF06EA8B2B9568E802D42064966CF)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/_kzMvndTSRelKakpenBmYQ/zh-cn_image_0000002429485750.png?HW-CC-KV=V1&HW-CC-Date=20260429T062025Z&HW-CC-Expire=86400&HW-CC-Sign=FBF48B9BDC21C9D35C106536CF0B3041A27570ADB23C4EC405D1A2485D2644DC)

**解决措施**

该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](../harmonyos-guides/arkts.md)
