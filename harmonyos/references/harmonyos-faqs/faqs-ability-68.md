---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-68
title: 关于emitter、eventHub的使用场景
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 关于emitter、eventHub的使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11c293b94f160d9b12f012ed32b1af42db1c640499eb662b262913ca6939b20e
---

Emitter提供跨线程事件的发送和处理功能，包括事件的持续订阅、单次订阅、取消订阅及事件队列的发送。

1. 订阅事件

   ```typescript
   import { emitter } from '@kit.BasicServicesKit'; 
    
   const TAG: string = 'ThreadModel';
   ```

   ```typescript
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
2. 发送事件

   ```typescript
   import { emitter } from '@kit.BasicServicesKit';
   ```

   ```typescript
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

   **参考链接**

   [UIAbility组件与UI的数据同步](../harmonyos-guides/uiability-data-sync-with-ui.md)
