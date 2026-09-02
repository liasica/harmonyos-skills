---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-35
title: ExtensionAbility如何与主进程通信
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > ExtensionAbility如何与主进程通信
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b031aa55072d65679e57b947a636ddc54e0227947458aac0ff57f3e4244888e
---

实现步骤：

ExtensionAbility端发布事件：

```typescript
import { commonEventManager } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Publish public event callbacks
function publishCB(err: BusinessError) {
  if (err) {
    console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in publishing common event.`);
  }
}
// Publish public events
try {
  commonEventManager.publish("event", publishCB);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
}
```

主进程端订阅事件：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { commonEventManager } from '@kit.BasicServicesKit';

// Define subscribers to save successfully created subscriber objects, which can be used to complete subscription and unsubscribe actions in the future
let subscriber: commonEventManager.CommonEventSubscriber;
// Subscriber information
let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
  events: ["event"]
};
// Subscribe to public event callbacks
function SubscribeCB(err: BusinessError, data: commonEventManager.CommonEventData) {
  if (err) {
    console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in subscribing, data is ` + JSON.stringify(data));
  }
}
// Create subscriber callback
function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
  if(!err) {
    console.info(`Succeeded in creating subscriber.`);
    subscriber = commonEventSubscriber;
    // Subscribe to public events
    try {
      commonEventManager.subscribe(subscriber, SubscribeCB);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
    }
  } else {
    console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
  }
}
// Create subscribers
try {
  commonEventManager.createSubscriber(subscribeInfo, createCB);
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
}
```
