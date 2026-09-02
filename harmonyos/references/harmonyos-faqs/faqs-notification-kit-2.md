---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-notification-kit-2
title: 如何让事件只在一个UIAbility实例中传递
breadcrumb: FAQ > 应用服务开发 > 用户通知服务（Notification Kit） > 如何让事件只在一个UIAbility实例中传递
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:e1134b9ac23bb99a867e3e4b22355c493799e81a251ddaa3356fe210c116b42e
---

在UIAbility中使用EventHub订阅事件，EventHub模块提供了事件中心，订阅、取消订阅、触发事件的能力。

参考代码如下：

```ts
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    this.context.eventHub.on('myEvent', this.eventFunc);
    // result：
    // eventFunc is called,undefined,undefined
    this.context.eventHub.emit('myEvent');
    // result：
    // eventFunc is called,1,undefined
    this.context.eventHub.emit('myEvent', 1);
    // result：
    // eventFunc is called,1,2
    this.context.eventHub.emit('myEvent', 1, 2);
  }

  eventFunc(argOne: number, argTwo: number) {
    console.log(`eventFunc is called, ${argOne}, ${argTwo}`);
  }
}
```

## 参考链接

[使用EventHub进行数据通信](../harmonyos-guides/uiability-data-sync-with-ui.md#使用eventhub进行数据通信)
