---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-472
title: Tabs如何禁止点击切换，以及禁止滑动内容页切换TabContent
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs如何禁止点击切换，以及禁止滑动内容页切换TabContent
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:28705d4d338f97db0a76d69056fce821dc776d1d4493b0ac91194c2594fc147c
---

**问题描述**

当点击一个Tabs时，怎么禁止点击切换TabContent，因为业务场景当未登录时候，不允许切换，点击后跳转登录界面。

注：Tabs已设置.scrollable(false)，不可滑动切换，只可以点击切换。

**解决措施**

通过监听onContentWillChange，拦截TabContent内容变化，return为false表示不变化。可以实现禁止点击切换以及滑动内容页切换。

如果单纯禁止滑动内容页切换，也可以通过scrollable接口来控制，false表示禁止滑动内容页切换。
