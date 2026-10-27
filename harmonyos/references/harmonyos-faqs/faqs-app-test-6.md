---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6
title: 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
breadcrumb: FAQ > DevEco Studio > 应用测试 > 原有工程使用新的DevEco Studio版本打开，运行测试用例失败
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:01+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9d45fd5651274e867b409e2db09f89f3762fe1903f1c6367ef1447ba60bfe38f
---

**问题现象**

如果工程是在DevEco Studio 3.1.0.400之前版本创建的，升级DevEco Studio至3.1.0.400及以上版本后，原有工程运行测试用例会失败，并提示“A page configured in 'test\_pages.json' must have one and only one '@Entry' decorator”。

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/zmW9qcj9RWinNOoxVo_Qew/zh-cn_image_0000002654798187.png "点击放大")

**解决措施**

将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Ke-XEQRDQ8qjeezt-syFjw/zh-cn_image_0000002624638726.png "点击放大")
