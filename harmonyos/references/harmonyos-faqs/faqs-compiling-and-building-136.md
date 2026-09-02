---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-136
title: "编译报错“The required attribute: module-name is missing”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute: module-name is missing”"
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:49f4e2a74a64ef78f5772e5c1f58c78e1c9d54beddf83c62ef2de0d38d278a95
---

**错误描述**

缺少必需属性：module-name。

**可能原因**

1. build-profile.json5 文件中缺少模块名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8ThzjvgJRxyF8WEofHoDUg/zh-cn_image_0000002229758649.png)
2. 在hvigorconfig.ts中动态添加模块时未设置模块名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/s1WuBstLQWasNjtjh5FTDA/zh-cn_image_0000002194158776.png)

**解决措施**

1. 进入项目根目录下的build-profile.json5文件，确保module下有非空的name字段。
2. 进入项目根目录下的hvigorconfig.ts文件，确保includeNode方法的参数name字段存在且非空。

**参考链接**

[Hvigor脚本文件](../harmonyos-guides/ide-hvigor-life-cycle.md#section810245135914)
