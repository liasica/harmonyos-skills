---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-139
title: XComponent 怎么设置成透明
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > XComponent 怎么设置成透明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:549c8b50df0d2e15b4f79c9f0a39344c0abb35cce712cd4d43958f6dc012029e
---

XComponent显示的内容，可由开发者自定义绘制，通用属性中的背景设置、透明度设置和图像效果按照type有限支持。当type为TEXTURE时通用属性可以支持背景颜色设置、透明度设置和图像效果中的shadow属性，建议使用EGL/OpenGLES提供的接口设置相关内容。

**参考链接**

[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)，[背景设置](../harmonyos-references/ts-universal-attributes-background.md)，[透明度设置](../harmonyos-references/ts-universal-attributes-opacity.md)，[图像效果](../harmonyos-references/ts-universal-attributes-image-effect.md)
