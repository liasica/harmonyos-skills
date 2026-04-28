---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-35
title: ExtensionAbility如何与主进程通信
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > ExtensionAbility如何与主进程通信
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:195807e6190c3193da1e1867430df12a26051e8e1537f97345e3f95dfbf95778
---

实现步骤：

ExtensionAbility端发布事件：

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

5. // Publish public event callbacks
6. function publishCB(err: BusinessError) {
7. if (err) {
8. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
9. } else {
10. console.info(`Succeeded in publishing common event.`);
11. }
12. }
13. // Publish public events
14. try {
15. commonEventManager.publish("event", publishCB);
16. } catch (error) {
17. let err: BusinessError = error as BusinessError;
18. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
19. }
```

[PublishCB.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/PublishCB.ets#L21-L39)

主进程端订阅事件：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { commonEventManager } from '@kit.BasicServicesKit';

4. // Define subscribers to save successfully created subscriber objects, which can be used to complete subscription and unsubscribe actions in the future
5. let subscriber: commonEventManager.CommonEventSubscriber;
6. // Subscriber information
7. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
8. events: ["event"]
9. };
10. // Subscribe to public event callbacks
11. function SubscribeCB(err: BusinessError, data: commonEventManager.CommonEventData) {
12. if (err) {
13. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
14. } else {
15. console.info(`Succeeded in subscribing, data is ` + JSON.stringify(data));
16. }
17. }
18. // Create subscriber callback
19. function createCB(err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) {
20. if(!err) {
21. console.info(`Succeeded in creating subscriber.`);
22. subscriber = commonEventSubscriber;
23. // Subscribe to public events
24. try {
25. commonEventManager.subscribe(subscriber, SubscribeCB);
26. } catch (error) {
27. let err: BusinessError = error as BusinessError;
28. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
29. }
30. } else {
31. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
32. }
33. }
34. // Create subscribers
35. try {
36. commonEventManager.createSubscriber(subscribeInfo, createCB);
37. } catch (error) {
38. let err: BusinessError = error as BusinessError;
39. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
40. }
```

[SubscribeCB.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/SubscribeCB.ets#L21-L60)
