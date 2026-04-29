---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8
title: 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:503bf8916292efb68c15da3c4ee5f63ff58ebb35e278fc141d3f25ebabf054da
---

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yz6xI9DQT32n7jrtB9cLHw/zh-cn_image_0000002229758241.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=61BFD2C982E3F5DB350D5AECAD45A4E87F10600628B42CE1FB4282C838A658AC)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1. 在工程中右键选择New > Module...。
2. 选择Static Library模板。
3. 配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ORqbl1TkTbu_fbLcnxIy5g/zh-cn_image_0000002194158380.png?HW-CC-KV=V1&HW-CC-Date=20260429T062021Z&HW-CC-Expire=86400&HW-CC-Sign=E173755DBAAFCE0DAC9982DE531BA5EE27682F694FA1FE601779B0B410B62553)
