---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-183
title: 组件被隐藏后 onVisibleAreaChange 事件触发了两次
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 组件被隐藏后 onVisibleAreaChange 事件触发了两次
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:21+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:360dc88f4e62aa734e7d21e31a59ae90066ed67de203561d1f8bdf658d0bd058
---

**问题现象**

绑定ratios为[0, 1]时，组件突然消失会触发两次onVisibleAreaChange方法。

**解决措施**

如果希望仅触发一次，需要设置一个ratios。
