---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-14
title: 时延类指标出现负数是什么原因
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 时延类指标出现负数是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7367b78f1b57aecaddd0d78146524eca481b1818b8a242af9383ecb312f47471
---

**响应时延**

-2：起始点错误

-3：结束点异常，通常是因为没有进行点击或滑动操作

-4：步骤未采集到视频

-5：步骤未采集到trace

-6：值异常，大于800ms。未检测到触摸或滑动操作，可能是由于图像质量导致误识别。

**完成时延**

-2：找到的结束点早于起始点，通常表示页面没有发生变化。
