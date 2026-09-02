---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-63
title: Emitter线程间通信对象传递问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > Emitter线程间通信对象传递问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eae886ee6b97da640a8bb4634eaa714b820ff4d60a2736b2ff7f221d5a4cf921
---

## 问题现象

Emitter发送的数据中如果包含复杂对象，在订阅回调中无法获取复杂对象的属性。

## 背景知识

* [使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)。
* [sendable使用场景](../harmonyos-guides/sendable-guide.md)。

## 解决方案

线程间通信共享对象，需封装成sendable对象。代码示例如下：

```ts
import { emitter } from '@kit.BasicServicesKit';

@Sendable
class Sample {
  constructor() {
    this.count = 100;
  }

  printCount() {
    console.info('Print count : ' + this.count);
  }

  count: number;
}

class SelfEventData implements emitter.EventData {
  data: Sample = new Sample();
}

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

let eventData = new SelfEventData();

// 订阅事件
emitter.on('eventId', (eventData: SelfEventData) => {
  console.log('Event received:', eventData.data);
  eventData.data.printCount();
});

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('点击')
        .onClick(() => {
          console.log('Button clicked');
          // 点击后打印当前 count 值
          console.log('Current count:', eventData.data.count);
          // 发送事件
          emitter.emit('eventId', options, eventData);
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
