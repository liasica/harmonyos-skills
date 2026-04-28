---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-3
title: 为什么我的应用在开始稳定性测试后一直反复拉起退出，且最后测试中断结束，报告中展示测试中断？
breadcrumb: FAQ > DevEco Testing > 专项测试 > 稳定性基础质量测试 > 为什么我的应用在开始稳定性测试后一直反复拉起退出，且最后测试中断结束，报告中展示测试中断？
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b9d7998b85ca88ce1751cb9c6344163567144ff5113a282ec43843efe4a578c8
---

Testing在执行稳定性测试服务前会打开系统DFX的MemDebug开关，检测应用踩内存问题，当检测到问题后，应用可能闪退，此时测试服务将无法正常遍历应用，导致测试中断，如果您仍然想继续遍历应用其他稳定性问题，请重启设备后，进入稳定性基础质量服务卡片中的高级配置选项-关闭MemDebug开关，重新执行测试服务。
