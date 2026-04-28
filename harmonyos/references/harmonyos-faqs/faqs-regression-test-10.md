---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-10
title: 选择测试包后报错提示“应用解析异常，请稍后重试”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 选择测试包后报错提示“应用解析异常，请稍后重试”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9a78fc9e63d8f26cef311925d111762593c2025d4e2366a8246ddea8fb1d6132
---

在生成可执行测试包时，如果应用名在测试设备上解析失败，请检查打包时填写的应用名是否正确，并确认设备上是否已安装该应用。

如果未填写应用名或应用名错误，请重新生成测试包并创建测试任务。

如果已安装应用且应用名称正确，请在命令行执行“hdc shell bm dump -n 应用名”，以查看应用解析异常的原因。
