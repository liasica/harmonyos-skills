---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-95
title: ConstraintSize尺寸设置不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ConstraintSize尺寸设置不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:40880f284197222976f2720f52fb6d041be2bc4be726d0e5d8d4be273b57a813
---

**问题现象**

constraintSize约束组件尺寸时，子组件内设置百分比宽度，例如width('100%')会采用constraintSize约束中的最大宽乘百分比，导致撑开组件，看起来constraintSize设置没生效。

**解决措施**

可以在外层使用Scroll组件，设置constraintSize，当子组件占用空间超过设置的约束值时，会显示滚动条。
