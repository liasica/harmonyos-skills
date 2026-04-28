---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-1
title: 执行报告用例的其中一个步骤，在视频中动效为什么只录了一半
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 执行报告用例的其中一个步骤，在视频中动效为什么只录了一半
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ccabcb3e8740a7feb395a36fc6c68093de799d9e9fe367e11aa3aefd13a13ef0
---

启动App的步骤中，App在打开到一半时视频就结束了，没有加载完成的录屏部分。

上一步操作的动效时间较长，如果在动效未结束时就返回结果并开始下一步操作，会导致录屏中步骤不完整。可以在create\_tag方法中添加wait\_time参数，等待指定时间以采集并分析这段时间的数据。
