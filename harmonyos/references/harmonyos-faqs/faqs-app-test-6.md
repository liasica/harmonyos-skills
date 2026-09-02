---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6
title: 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ca83c71421abda053d660de514b6e83bb58caf8717abbe51cdf60cfc6de829fa
---

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/lluXWoKER46oH2aR8lsSDQ/zh-cn_image_0000002229604113.png "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/kp6pb6oYRUGyxBtJjkyJUQ/zh-cn_image_0000002194158732.png "点击放大")
