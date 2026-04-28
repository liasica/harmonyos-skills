---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-11
title: 选择测试包后，若出现“请添加测试步骤，具体请参考测试指南”的报错提示，请参考测试指南。
breadcrumb: FAQ > DevEco Testing > 回归测试 > 选择测试包后，若出现“请添加测试步骤，具体请参考测试指南”的报错提示，请参考测试指南。
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:96de16025e46563e61a06ea5d564566e23ced8155630353efc16cc680ea0e3bb
---

回归测试服务按步骤上报执行结果。若测试包中待执行用例未使用Step接口声明步骤信息，则会出现报错。

在用例脚本中，请导入并使用hypium.advance.deveco\_testing.step模块中的Step函数来标记步骤（from hypium.advance.deveco\_testing.step import Step），否则回归测试过程中无法正确读取测试步骤。
