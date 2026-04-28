---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-45
title: 如何让两个HSP不相互依赖，使用对方的组件
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何让两个HSP不相互依赖，使用对方的组件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a0f6dab7e9a4a0dbbc2d22b532927575a1385b9b8dc0e894d6499445795b9a9f
---

可以将需要共用的组件抽离出来，然后放到一个共享包中使用，或者使用动态import实现依赖解耦。

**参考链接**

[HAR模块间动态import依赖解耦](../harmonyos-guides/arkts-dynamic-import.md#har模块间动态import依赖解耦)
