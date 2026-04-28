---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-378
title: 是否支持对页面等ArkUI组件相关元素进行插桩
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 是否支持对页面等ArkUI组件相关元素进行插桩
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9174db715dbb1f9fe6202ffae5b6490d4c2d1e8d3c20d9f08acf6bc9d076268
---

ArkUI相关的接口在编译时会进行转换，开发态使用的对象或方法在运行时可能不存在。由于ArkUI组件在编译时会被转换为不同形态，导致运行时无法定位原始声明，因此，Aspect类提供的插桩和替换接口不适用于ArkUI组件相关元素。
