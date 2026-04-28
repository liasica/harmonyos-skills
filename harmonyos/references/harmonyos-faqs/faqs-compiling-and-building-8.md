---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8
title: 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:eaf96cdd7cb5acd1321e04d46af63eeeb1b02bedcedc23e34490453ca86f9da7
---

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yz6xI9DQT32n7jrtB9cLHw/zh-cn_image_0000002229758241.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=4855AA6D03AAC6B9056C4553339BD6041A535BF4F45A321CAA05ACE06E180F3B)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ORqbl1TkTbu_fbLcnxIy5g/zh-cn_image_0000002194158380.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=DE3530D042674246A724C3A3D59FFCC4DA2A20576A2C8ED3DBA182C27D8AC437)
