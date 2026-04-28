---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-17
title: 测试过程中没有显示用例包步骤且指标监控中无数据
breadcrumb: FAQ > DevEco Testing > 回归测试 > 测试过程中没有显示用例包步骤且指标监控中无数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13df33e30a18b1fce2bfa7abb59d627dfe9035247c73cf055b2ad5120c02d9cd
---

在用例脚本中，导入并使用hypium.advance.deveco\_testing.step中的Step函数标记步骤（from hypium.advance.deveco\_testing.step import Step）。否则，回归测试过程中无法正确读取测试步骤，导致指标监控为空。
