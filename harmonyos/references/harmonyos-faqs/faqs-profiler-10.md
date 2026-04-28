---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-10
title: 如何解决体检工具诊断结果代码行跳转不准确的问题
breadcrumb: FAQ > DevEco Studio > 性能分析 > 如何解决体检工具诊断结果代码行跳转不准确的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f6d036e0f9b66b405f0dc967302508f5307557388991971232f5ebef5d1aac30
---

1. 保证被检测应用和当前工程代码版本保持一致。
2. 在导入检测报告前clean工程删除sourceMaps文件，并且导入过程中编译构建失败，最终会导致源码跳转不准确。需要解决编译失败的问题，重新导入报告。
3. 建议使用debug模式编译生成安装包进行检测。
