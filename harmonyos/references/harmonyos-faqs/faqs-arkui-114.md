---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-114
title: ArkUI中icon资源锯齿感严重
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArkUI中icon资源锯齿感严重
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:07574dd2c1cc9b0070c78eb77d8fb968e7c56bad87c82b318a3efe2271f52dec
---

**解决方案**

Image组件的插值效果interpolation默认为ImageInterpolation.None，可能会导致锯齿问题，因此可以通过设置interpolation为High/Medium/Low来减少锯齿效果。

**参考链接**

[ImageInterpolation](../harmonyos-references/ts-basic-components-image.md#imageinterpolation)
