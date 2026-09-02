---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-13
title: 测试报告中，用例执行详情为红色，且无数据是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 测试报告中，用例执行详情为红色，且无数据是什么原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e716ad8f83187db87075067a4b8cc4b4ba4503d9919ce686fdca16c7b270e885
---

报告中用例详情表头为红色，表示用例未能成功执行。可以点击报告右上角的执行日志查看具体的错误信息。常见的失败原因包括：用例抛出未捕获的异常、待测应用未安装、设备断开连接等。建议先在PyCharm中运行和调试脚本，确保脚本能够顺利执行，然后再使用DevEco Testing进行正式测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/bg73ek1yT4-bIWRaVIeAhQ/zh-cn_image_0000002624478982.png "点击放大")
