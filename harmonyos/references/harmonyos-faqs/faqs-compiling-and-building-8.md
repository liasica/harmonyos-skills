---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8
title: "编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
breadcrumb: "FAQ > DevEco Studio > 编译构建 > 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3506fdc64cc4910d69e81ce0cf604e9ff69f3d02532ac76ffd7309814d70dd35
---

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yz6xI9DQT32n7jrtB9cLHw/zh-cn_image_0000002229758241.png)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ORqbl1TkTbu_fbLcnxIy5g/zh-cn_image_0000002194158380.png)
