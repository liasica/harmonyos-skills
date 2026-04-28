---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-13
title: 测试报告中，用例执行详情为红色，且无数据是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 测试报告中，用例执行详情为红色，且无数据是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:45e6c5f6c62ef6df546a27de63c11d6474cb48fb63fb81911f716779a74230aa
---

报告中用例详情表头为红色，表示用例未能成功执行。可以点击报告右上角的执行日志查看具体的错误信息。常见的失败原因包括：用例抛出未捕获的异常、待测应用未安装、设备断开连接等。建议先在PyCharm中运行和调试脚本，确保脚本能够顺利执行，然后再使用DevEco Testing进行正式测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/80_OX3DhSUKocd-i0qpHSQ/zh-cn_image_0000002229758345.png?HW-CC-KV=V1&HW-CC-Date=20260428T003031Z&HW-CC-Expire=86400&HW-CC-Sign=6ACBD61E9B8148BF6D64418BBEF64D28795CEC75E8793DA05BD4C9BC2C03C329 "点击放大")
