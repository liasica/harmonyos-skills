---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-68
title: 关于emitter、eventHub的使用场景
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 关于emitter、eventHub的使用场景
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:47+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:fc864c8a9a3c7558bb10ad14abd6cdb5d014da67c8373463d83d57d8e4a33b1b
---

Emitter提供跨线程事件的发送和处理功能，包括事件的持续订阅、单次订阅、取消订阅及事件队列的发送。

1. 订阅事件

   ```
   1. import { emitter } from '@kit.BasicServicesKit';

   3. const TAG: string = 'ThreadModel';
   ```

   [EmitterAndEventHub1.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub1.ets#L21-L23)

   ```
   1. // Define an event with an eventId of 1
   2. let event: emitter.InnerEvent = {
   3. eventId: 1
   4. };

   6. // Execute the callback after receiving an event with eventId 1
   7. let callback = (eventData: emitter.EventData): void => {
   8. this.getUIContext().getPromptAction().showToast({
   9. message: JSON.stringify(eventData)
   10. });
   11. };

   13. // Subscribe to events with eventId 1
   14. emitter.on(event,callback);
   15. this.getUIContext().getPromptAction().showToast({
   16. message: 'subscribe_success'
   17. });
   ```

   [EmitterAndEventHub2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub2.ets#L27-L43)
2. 发送事件

   ```
   1. import { emitter } from '@kit.BasicServicesKit';
   ```

   [EmitterAndEventHub.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub.ets#L21-L22)

   ```
   1. // Define an event with an eventId of 1 and a priority of Low
   2. let event: emitter.InnerEvent = {
   3. eventId: 1,
   4. priority: emitter.EventPriority.LOW
   5. };

   7. let eventData: emitter.EventData = {
   8. data: {
   9. content: 'c',
   10. id: 1,
   11. isEmpty: false
   12. }
   13. };

   15. // Send an event with eventId 1 and the event content is eventData
   16. emitter.emit(event,eventData);
   ```

   [EmitterAndEventHub.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/EmitterAndEventHub.ets#L26-L41)

   EventHub提供同线程内事件的发送与处理功能，包括事件订阅、取消订阅及触发。以UIAbility组件与UI的数据同步为例，具体使用方法请参考相关文档。

   **参考链接**

   [UIAbility组件与UI的数据同步](../harmonyos-guides/uiability-data-sync-with-ui.md)
