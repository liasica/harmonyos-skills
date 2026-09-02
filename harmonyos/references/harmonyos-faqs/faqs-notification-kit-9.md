---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-9
title: emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:255f1a06d21486ea36cef949b814e9d4c7ae86b8d9b219abb156c69c1585eac6
---

是的，emitter.off取消订阅某个事件后，所有订阅这个事件的地方都不会再收到这个事件的消息。

参考代码如下：

```ts
emitter.off(1);
```

## 参考链接

[emitter.off](../harmonyos-references/js-apis-emitter.md#emitteroff)
