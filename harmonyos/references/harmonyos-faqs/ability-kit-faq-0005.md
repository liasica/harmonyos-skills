---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0005
title: Emitter与EventHub事件通信机制常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > Emitter与EventHub事件通信机制常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:24+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:80e7470a9cf038960adc92663786b2829c3b0b918e97f2a91446e53bc59000a0
---

**Q：emitter和eventHub有哪些使用场景？**

**A**：Emitter提供跨线程事件的发送和处理功能，包括事件的持续订阅、单次订阅、取消订阅及事件队列的发送。

1. 订阅事件：

   ```ts
   import { emitter } from '@kit.BasicServicesKit'; 

   const TAG: string = 'ThreadModel';
   ```

   ```ts
   // Define an event with an eventId of 1
   let event: emitter.InnerEvent = {
     eventId: 1
   };

   // Execute the callback after receiving an event with eventId 1
   let callback = (eventData: emitter.EventData): void => {
     this.getUIContext().getPromptAction().showToast({
       message: JSON.stringify(eventData)
     });
   };

   // Subscribe to events with eventId 1
   emitter.on(event,callback);
   this.getUIContext().getPromptAction().showToast({
     message: 'subscribe_success'
   });
   ```
2. 发送事件：

   ```ts
   import { emitter } from '@kit.BasicServicesKit';
   ```

   ```ts
   // Define an event with an eventId of 1 and a priority of Low 
   let event: emitter.InnerEvent = {
     eventId: 1,
     priority: emitter.EventPriority.LOW
   };

   let eventData: emitter.EventData = {
     data: {
       content: 'c',
       id: 1,
       isEmpty: false
     }
   };

   // Send an event with eventId 1 and the event content is eventData
   emitter.emit(event,eventData);
   ```

   EventHub提供同线程内事件的发送与处理功能，包括事件订阅、取消订阅及触发。以UIAbility组件与UI的数据同步为例，具体使用方法请参考相关文档。

   参考链接：[UIAbility组件与UI的数据同步](../harmonyos-guides/uiability-data-sync-with-ui.md)。
