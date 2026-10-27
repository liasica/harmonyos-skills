---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8
title: "编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:25f7df6ffe4c9dcc31ef124eae64dd2c0176808ff2c0a5119d33bdb3c2fd49c3
---

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/oThYfAIGT8mddlNkoGAFZg/zh-cn_image_0000002654797835.png)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/JA9r9w5iQN6Rkjfjp50Qbg/zh-cn_image_0000002624638380.png)
