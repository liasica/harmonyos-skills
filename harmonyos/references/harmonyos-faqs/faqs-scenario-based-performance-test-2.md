---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-2
title: Can't find component with [BY.text('XXX')] 的报错是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > Can't find component with [BY.text('XXX')] 的报错是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1f078661cccab0b52373457c4785b66c3da6a2ad6d9107c109a6f1ae71a258eb
---

1. 查找控件时，如果场景中不存在该控件，检查是否符合预期。
2. 查找条件中可能包含不可视字符。可以从UiViewer中找到对应控件并复制其信息。
3. 如果与上一步的时间间隔过短，查找控件时界面可能尚未完全加载，导致控件未出现。

   可能由于脚本问题，查找控件时会进入非预期场景，例如在前面的步骤中进入了另一个界面，此时界面中不存在该控件。
