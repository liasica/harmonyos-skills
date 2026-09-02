---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-9
title: AI字幕控件和AI识图的多语言配置以及依赖问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > AI字幕控件和AI识图的多语言配置以及依赖问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:6caa888620d47b2818065203aea8c1b95ce283ca94f484758b6d284bfef4c450
---

## 问题现象

若需在同一个应用中同时使用AI字幕控件（中英文）和AI识图（含其他语种），如何协调多语言配置？是否存在冲突或依赖问题？

## 解决方案

[AI字幕控件](../harmonyos-guides/speech-aicaption-guide.md)提供对应音频语种的字幕不涉及多语言配置。[AI识图](../harmonyos-guides/vision-imageanalyzer.md)支持划词手动选择语种翻译，仅[自定义的文字分析菜单项](../harmonyos-references/vision-image-analyzer.md#setcustomtextmenuitems)名称涉及多语言配置。因此无协调问题，且无冲突或依赖问题。
