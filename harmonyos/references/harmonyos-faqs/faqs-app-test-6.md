---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6
title: 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67a8be4851cc9726533c4c27e8fb81b1ccbbdeb095673dc7209b8c23c44d50a4
---

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/lluXWoKER46oH2aR8lsSDQ/zh-cn_image_0000002229604113.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=3DCB515F942D4202FC787FC4D93D413D0B7F8A4532CCC57307191565602BFD9A "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/kp6pb6oYRUGyxBtJjkyJUQ/zh-cn_image_0000002194158732.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=40BED6AD8875CCF08945A3BF4CF3480FC09322DF4A3753658429944C72BDDF4E "点击放大")
