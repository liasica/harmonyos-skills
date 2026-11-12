---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/speech-kit-faq-0002
title: AI字幕与AI识图多语言配置常见问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化语音（Speech） > 常见问题 > AI字幕与AI识图多语言配置常见问题
category: harmonyos-faqs
scraped_at: 2026-11-12T10:00:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:738a21eefaa8c88811e6cb5fbd0cfdc55f15d032e2ee17eeb4b93453a38a218c
---

**Q：若需在同一个应用中同时使用AI字幕控件（中英文）和AI识图（含其他语种），如何协调多语言配置？是否存在冲突或依赖问题？**

**A**：[AI字幕控件](../harmonyos-guides/speech-aicaption-guide.md)提供对应音频语种的字幕不涉及多语言配置。[AI识图](../harmonyos-guides/vision-imageanalyzer.md)支持划词手动选择语种翻译，仅[自定义的文字分析菜单项](../doccenter-references/api/vision-image-analyzer.md#setcustomtextmenuitems)名称涉及多语言配置。因此无协调问题，且无冲突或依赖问题。
