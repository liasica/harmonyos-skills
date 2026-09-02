---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-5
title: 如何监听系统公共事件，如熄屏、亮屏、开机等
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何监听系统公共事件，如熄屏、亮屏、开机等
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:59f437b66be82d9f9b4d509090db63a2f82cd72aa7a4f17e11a45f2af28aa26f
---

CES（Common Event Service，公共事件服务）为应用程序提供订阅、发布和退订公共事件的能力。可以通过订阅系统公共事件来监听熄屏、亮屏和开机事件。开机事件使用“COMMON\_EVENT\_BOOT\_COMPLETED”来监听。

参考代码如下：

```ts
import { commonEventManager } from '@kit.BasicServicesKit';

let subscriber:commonEventManager.CommonEventSubscriber;
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ['usual.event.SCREEN_OFF'], // Subscribe to screen out public events
  priority:80
}
commonEventManager.createSubscriber(subscribeInfo, (err, data) => {
  if (err) {
    console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in creating subscriber1.');
  subscriber = data;
  // Subscribe to public event callbacks
  commonEventManager.subscribe(subscriber, (err, data) => {
    if (err) {
      console.error(`Failed to subscribe common event. Code is ${err.code}, message is ${err.message}`);
      return;
    } else {
      console.info(`Succeeded in subscribe common event Succeeded1 `);
    }
  })
})
```

## 参考链接

[系统定义的公共事件](../harmonyos-references/commoneventmanager-definitions.md)
