---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-452
title: Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0b137ccc2a7f77770454585927af1d8f068a63020089292f916545d5b4772a71
---

**问题分析**

[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)被调用的时候Tabs组件尚未完成渲染，这会导致preloadItems方法预加载不存在的索引。

**解决方案**

TabContent中的[onWillShow()](../harmonyos-references/ts-container-tabcontent.md#onwillshow12)方法能够实现预加载功能，但是Tabs每次切换时都会触发onWillShow()回调，需要做节流处理。
