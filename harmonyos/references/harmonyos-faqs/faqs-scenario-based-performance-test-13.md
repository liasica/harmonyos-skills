---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-13
title: 测试报告中，用例执行详情为红色，且无数据是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 测试报告中，用例执行详情为红色，且无数据是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67c39ec29728f451abf41c82bb490e0c245e1818cae49f9a23d07407603d2857
---

报告中用例详情表头为红色，表示用例未能成功执行。可以点击报告右上角的执行日志查看具体的错误信息。常见的失败原因包括：用例抛出未捕获的异常、待测应用未安装、设备断开连接等。建议先在PyCharm中运行和调试脚本，确保脚本能够顺利执行，然后再使用DevEco Testing进行正式测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/80_OX3DhSUKocd-i0qpHSQ/zh-cn_image_0000002229758345.png?HW-CC-KV=V1&HW-CC-Date=20260429T062150Z&HW-CC-Expire=86400&HW-CC-Sign=69E1AD306856A4799833AE8A4B638B7BE315FB7A8A260B77CD9E5BAB971F5339 "点击放大")
