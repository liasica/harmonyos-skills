---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-13
title: 测试报告中，用例执行详情为红色，且无数据是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 测试报告中，用例执行详情为红色，且无数据是什么原因
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:04+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:d65ad42b9a7cc32907074d2ed91d8cc75b9b308a7003c46bec7f49fa19337e90
---

报告中用例详情表头为红色，表示用例未能成功执行。可以点击报告右上角的执行日志查看具体的错误信息。常见的失败原因包括：用例抛出未捕获的异常、待测应用未安装、设备断开连接等。建议先在PyCharm中运行和调试脚本，确保脚本能够顺利执行，然后再使用DevEco Testing进行正式测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/6frGtCrFRWytNbY3xQKfYQ/zh-cn_image_0000002624478982.png "点击放大")
