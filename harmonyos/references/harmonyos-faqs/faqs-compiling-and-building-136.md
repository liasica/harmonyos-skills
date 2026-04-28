---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-136
title: 编译报错“The required attribute: module-name is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute: module-name is missing”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ad267f350d99b006227ffa1c50210b1ddb17bde40a6d2c6bc450d076303fe2d9
---

**错误描述**

缺少必需属性：module-name。

**可能原因**

1. build-profile.json5 文件中缺少模块名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8ThzjvgJRxyF8WEofHoDUg/zh-cn_image_0000002229758649.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=954895E04E490F218139D970CD0B3D31D804878108B5C00593BFA9F2F2496435)
2. 在hvigorconfig.ts中动态添加模块时未设置模块名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/s1WuBstLQWasNjtjh5FTDA/zh-cn_image_0000002194158776.png?HW-CC-KV=V1&HW-CC-Date=20260428T002935Z&HW-CC-Expire=86400&HW-CC-Sign=9036C6BBD35980FF25D7FAD200F5DD026ECF663D365B8E4F4D1B1B32B78E9ABE)

**解决措施**

1. 进入项目根目录下的build-profile.json5文件，确保module下有非空的name字段。
2. 进入项目根目录下的hvigorconfig.ts文件，确保includeNode方法的参数name字段存在且非空。

**参考链接**

[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)
