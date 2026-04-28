---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-429
title: 如何区分onPageHide的两种场景：应用退到后台，以及有新的页面打开
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何区分onPageHide的两种场景：应用退到后台，以及有新的页面打开
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b86fc1cd8d75dbee6fd03434bc5e032dd1ea1aedd64d447dcabe6fca412d3b26
---

**问题描述**

如何判断当前Page的onPageHide是由用户手动隐藏App进程到桌面引发的，还是用户打开新的页面遮盖住了当前Entry页面引发的？

**解决措施**

应用退到后台会触发UIAbility组件的[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)生命周期回调，而新的页面打开不会触发，可在Page的onPageHide回调中通过调用UIAbilityContext的getAbilityState()方法，结合onBackground触发状态进行综合判断。
