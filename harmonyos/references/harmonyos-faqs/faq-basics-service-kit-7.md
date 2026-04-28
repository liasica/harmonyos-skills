---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-7
title: eventId一样时，Emitter多次调用on是否能注册多个回调
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > eventId一样时，Emitter多次调用on是否能注册多个回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:20+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c48052a8ec0083e91210b34d7ec1cc7de82ff380b26f97984fe10544712f6f5d
---

**解决方案**

针对同一个eventId多次注册订阅时，若关联的回调对象为同一个，则只会生效第一次注册的回调对象，若关联的回调对象不同，则多个回调对象均生效，由on的顺序决定回调顺序。使用off注销时，eventId与回调对象需配对，否则回调注销失败。

**参考资料**

[events.emitter (Emitter)](../harmonyos-references/js-apis-emitter.md)
