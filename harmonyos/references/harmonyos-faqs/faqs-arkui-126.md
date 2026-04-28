---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-126
title: XComponent组件如何设置背景颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > XComponent组件如何设置背景颜色
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e74c2615b2047c8bbca2bec5e89ac9b5d0775c37e373ae583e87a2f5b20c0c8b
---

XComponent组件仅在XComponentType为TEXTURE时支持设置，XComponentType为SURFACE类型时不支持通用属性包括背景颜色设置，需采用EGL/OpenGLES或子组件内容设置。

**参考链接**

[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)
