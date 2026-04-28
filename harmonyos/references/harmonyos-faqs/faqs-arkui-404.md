---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-404
title: Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:995e3d4cd0ea3c79e3d26e8ee945d631e5b5e40e6a9b31ac1c99bad31b32b606
---

**问题描述**

NavDestination是否有缓存页面的功能，每次pushStack后都要刷新页面。

**解决措施**

NavDestination不支持缓存功能，页面出栈后会被销毁。
