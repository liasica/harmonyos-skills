---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-5
title: 如何监听系统公共事件，如熄屏、亮屏、开机等
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何监听系统公共事件，如熄屏、亮屏、开机等
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2abe313a20fc48168bb22c2cada2ecf983ae855ca4bae0772456e5ba42d05689
---

CES（Common Event Service，公共事件服务）为应用程序提供订阅、发布和退订公共事件的能力。可以通过订阅系统公共事件来监听熄屏、亮屏和开机事件。开机事件使用“COMMON\_EVENT\_BOOT\_COMPLETED”来监听。

参考代码如下：

```
1. import { commonEventManager } from '@kit.BasicServicesKit';

3. let subscriber:commonEventManager.CommonEventSubscriber;
4. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
5. events: ['usual.event.SCREEN_OFF'], // Subscribe to screen out public events
6. priority:80
7. }
8. commonEventManager.createSubscriber(subscribeInfo, (err, data) => {
9. if (err) {
10. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in creating subscriber1.');
14. subscriber = data;
15. // Subscribe to public event callbacks
16. commonEventManager.subscribe(subscriber, (err, data) => {
17. if (err) {
18. console.error(`Failed to subscribe common event. Code is ${err.code}, message is ${err.message}`);
19. return;
20. } else {
21. console.info(`Succeeded in subscribe common event Succeeded1 `);
22. }
23. })
24. })
```

[CommonEvent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Notificationkit/entry/src/main/ets/pages/CommonEvent.ets#L21-L44)

**参考链接**

[系统定义的公共事件](../harmonyos-references/commoneventmanager-definitions.md)
