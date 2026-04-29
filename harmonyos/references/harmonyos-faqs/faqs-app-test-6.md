---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6
title: 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b3805ba4b52148757302a2a448894e6f686a24494bd7522aef21c0611701477f
---

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/lluXWoKER46oH2aR8lsSDQ/zh-cn_image_0000002229604113.png?HW-CC-KV=V1&HW-CC-Date=20260429T062134Z&HW-CC-Expire=86400&HW-CC-Sign=4CBDBD68603237ADA84106BA114959ED50560AB7404EF853F455EC5966296486 "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/kp6pb6oYRUGyxBtJjkyJUQ/zh-cn_image_0000002194158732.png?HW-CC-KV=V1&HW-CC-Date=20260429T062134Z&HW-CC-Expire=86400&HW-CC-Sign=3B3A4F3CC71CF53E2EA08D1B8AF4F4177416588CB1A57BDB413B85224C57A4F1 "点击放大")
