---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-regression-test-12
title: 选择测试包后报错提示“测试包解析失败，请查看测试指南排查失败原因”
breadcrumb: FAQ > DevEco Testing > 回归测试 > 选择测试包后报错提示“测试包解析失败，请查看测试指南排查失败原因”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5d36c46e2038e7e6d86f40a0d0b433eda8b2af1b07ccfd18c4a03eff3d6040c
---

出现该报错有以下两种原因：

1. 用户选择的测试包中没有可执行测试用例，请参考测试指南和基于Python的应用UI测试编写测试用例。
2. 选择的可执行测试包中未指定应用名，需使用回归测试插件生成可执行测试包。
