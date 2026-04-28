---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-basic-quality-test-1
title: 报告中为什么会出现未执行检测
breadcrumb: FAQ > DevEco Testing > 专项测试 > 性能基础质量测试 > 报告中为什么会出现未执行检测
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a3ae5fee776b3121c997c68e079b81f5eb8df4677e42f4bc833e0d8c14ef6fa0
---

如遇到以下几种场景，将不执行检测项。

场景1：在应用测试过程中，如果测试用例的执行条件不满足，则不会执行相关测试场景。例如，如果应用页面仅有一屏且不支持滑动，则本次遍历中，滑动相关指标将无数据；如果某些指标检测动效场景，而在遍历过程中未遇到动效场景，则流畅相关指标将无数据。

场景2：由于需要通过查找桌面应用图标名来检测应用，请确保被测应用放置在桌面上，不要放在文件夹中，否则会出现批量未检测项。

场景3：使用WebView类应用进行测试时，会出现测试数据不准确和批量未执行检测项的问题。

场景4：偶现应用解析异常，导致批量出现未检测项。请重新执行任务以恢复。

场景5：应用内操作测试主要支持ArkUI控件类应用（包括ReactNative框架开发的应用）。对于WebView页面遍历，系统版本需为HarmonyOS 6.0及以上。

场景6：不支持Flutter应用及第三方自研的自定义控件识别。
