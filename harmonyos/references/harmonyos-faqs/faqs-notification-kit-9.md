---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-9
title: emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > emitter.off取消订阅某个事件后，是不是所有订阅该事件的地方都不会再收到该事件的消息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:415c23cb1c01c5b235c543a00e596b0c58054b7816c0efc233ba2a872ed5bfdf
---

是的，emitter.off取消订阅某个事件后，所有订阅这个事件的地方都不会再收到这个事件的消息。

参考代码如下：

```
1. emitter.off(1);
```

[EmitterOff.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/pages/EmitterOff.ets#L22-L22)

**参考链接**

[emitter.off](../harmonyos-references/js-apis-emitter.md#emitteroff)
