---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager
title: @ohos.commonEventManager (公共事件模块)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > @ohos.commonEventManager (公共事件模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:37+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4f870e14ccff3dcbe8f7f5d92dee60b2307a3e94ae3994fa2941c6ba28b37e4f
---

本模块提供了公共事件相关的能力，包括发布公共事件、订阅公共事件、以及退订公共事件。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
```

## Support

PhonePC/2in1TabletTVWearable

系统公共事件是指由系统服务或系统应用发布的事件，订阅这些公共事件需要特定的权限、使用相应的值，详见[系统定义的公共事件](commoneventmanager-definitions.md)。

## commonEventManager.publish

PhonePC/2in1TabletTVWearable

publish(event: string, callback: AsyncCallback<void>): void

发布公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发送的公共事件。详见[系统定义的公共事件定义](commoneventmanager-definitions.md)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[事件错误码](errorcode-commoneventservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1500003 | The common event sending frequency too high. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 发布公共事件
4. try {
5. commonEventManager.publish('event', (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
8. return;
9. }
10. console.info(`Succeeded in publishing common event.`);
11. });
12. } catch (error) {
13. let err: BusinessError = error as BusinessError;
14. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
15. }
```

## commonEventManager.publish

PhonePC/2in1TabletTVWearable

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

发布公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发布的公共事件。详见[系统定义的公共事件定义](commoneventmanager-definitions.md)。 |
| options | [CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md) | 是 | 表示发布公共事件的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[事件错误码](errorcode-commoneventservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1500003 | The common event sending frequency too high. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500009 | Failed to obtain system parameters. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 公共事件相关信息，以发布有序公共事件为例
4. let options: commonEventManager.CommonEventPublishData = {
5. code: 0,
6. data: 'initial data',
7. isOrdered: true // 有序公共事件
8. }

10. // 发布公共事件
11. try {
12. commonEventManager.publish('event', options, (err: BusinessError) => {
13. if (err) {
14. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
15. return;
16. }
17. console.info(`Succeeded in publishing common event.`);
18. });
19. } catch (error) {
20. let err: BusinessError = error as BusinessError;
21. console.error(`Failed to publish common event. Code is ${err.code}, message is ${err.message}`);
22. }
```

## commonEventManager.createSubscriber

PhonePC/2in1TabletTVWearable

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

创建订阅者。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |
| callback | AsyncCallback<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1)> | 是 | 回调函数。当公共事件订阅者创建成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };

10. // 创建订阅者
11. try {
12. commonEventManager.createSubscriber(subscribeInfo,
13. (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
14. if(!err) {
15. console.info(`Succeeded in creating subscriber.`);
16. subscriber = commonEventSubscriber;
17. return;
18. }
19. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
20. });
21. } catch (error) {
22. let err: BusinessError = error as BusinessError;
23. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
24. }
```

## commonEventManager.createSubscriber

PhonePC/2in1TabletTVWearable

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

创建订阅者。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1)> | Promise对象，返回创建成功的订阅者对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };
9. // 创建订阅者
10. commonEventManager.createSubscriber(subscribeInfo).then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
11. console.info(`Succeeded in creating subscriber.`);
12. subscriber = commonEventSubscriber;
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
15. });
```

## commonEventManager.createSubscriberSync10+

PhonePC/2in1TabletTVWearable

createSubscriberSync(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber

createSubscriber的同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1) | 返回订阅者对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };
9. // 创建订阅者
10. try {
11. subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
12. } catch (error) {
13. let err: BusinessError = error as BusinessError;
14. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
15. }
```

## commonEventManager.subscribe

PhonePC/2in1TabletTVWearable

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

订阅公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<[CommonEventData](js-apis-inner-commonevent-commoneventdata.md)> | 是 | 回调函数。当公共事件订阅成功后，事件触发时执行的回调函数；否则订阅失败时，err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[事件错误码](errorcode-commoneventservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500010 | The count of subscriber exceed system specification. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };

10. // 创建订阅者
11. try {
12. commonEventManager.createSubscriber(subscribeInfo,
13. (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
14. if(!err) {
15. console.info(`Succeeded in creating subscriber.`);
16. subscriber = commonEventSubscriber;
17. // 订阅公共事件
18. try {
19. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
20. if (err) {
21. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
25. });
26. } catch (error) {
27. let err: BusinessError = error as BusinessError;
28. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
29. }
30. return;
31. }
32. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
33. });
34. } catch (error) {
35. let err: BusinessError = error as BusinessError;
36. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
37. }
```

## commonEventManager.unsubscribe

PhonePC/2in1TabletTVWearable

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

取消订阅公共事件。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<void> | 否 | 回调函数。当取消公共事件订阅成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[事件错误码](errorcode-commoneventservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };

10. // 创建订阅者
11. try {
12. commonEventManager.createSubscriber(subscribeInfo,
13. (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
14. if(!err) {
15. console.info(`Succeeded in creating subscriber.`);
16. subscriber = commonEventSubscriber;
17. // 订阅公共事件
18. try {
19. commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
20. if (err) {
21. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. console.info(`Succeeded in subscribing, data is ${JSON.stringify(data)}`);
25. });
26. } catch (error) {
27. let err: BusinessError = error as BusinessError;
28. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
29. }
30. return;
31. }
32. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
33. });
34. } catch (error) {
35. let err: BusinessError = error as BusinessError;
36. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
37. }

39. // 取消订阅公共事件
40. // 等待异步接口subscribe执行完毕，开发者根据实际业务选择是否需要添加setTimeout
41. setTimeout(() => {
42. try {
43. commonEventManager.unsubscribe(subscriber, (err: BusinessError) => {
44. if (err) {
45. console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
46. return;
47. }
48. // subscriber不再使用时需要将其置为null，避免内存泄露
49. subscriber = null;
50. console.info(`Succeeded in unsubscribing.`);
51. });
52. } catch (error) {
53. let err: BusinessError = error as BusinessError;
54. console.error(`Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
55. }
56. }, 500);
```

## commonEventManager.subscribeToEvent20+

PhonePC/2in1TabletTVWearable

subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>

订阅公共事件，并返回订阅成功或失败信息。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1) | 是 | 表示订阅者对象。 |
| callback | Callback<[CommonEventData](js-apis-inner-commonevent-commoneventdata.md)> | 是 | 表示接收公共事件数据的回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[事件错误码](errorcode-commoneventservice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1500007 | Failed to send the message to the common event service. |
| 1500008 | Failed to initialize the common event service. |
| 1500010 | The count of subscriber exceed system specification. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
4. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
5. // 订阅者信息
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ["event"]
8. };

10. // 创建订阅者
11. try {
12. commonEventManager.createSubscriber(subscribeInfo,
13. (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
14. if (err) {
15. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
16. } else {
17. console.info(`Succeeded in creating subscriber.`);
18. subscriber = commonEventSubscriber;
19. // 订阅公共事件
20. try {
21. commonEventManager.subscribeToEvent(subscriber, (data: commonEventManager.CommonEventData) => {
22. console.info(`Succeeded to receive common event, data is ` + JSON.stringify(data));
23. }).then(() => {
24. console.info(`Succeeded to subscribe.`);
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
27. });
28. } catch (error) {
29. let err: BusinessError = error as BusinessError;
30. console.error(`Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
31. }
32. }
33. });
34. } catch (error) {
35. let err: BusinessError = error as BusinessError;
36. console.error(`Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
37. }
```

## CommonEventData10+

PhonePC/2in1TabletTVWearable

type CommonEventData = \_CommonEventData

表示公共事件的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| [\_CommonEventData](js-apis-inner-commonevent-commoneventdata.md) | 表示公共事件的数据。 |

## CommonEventSubscriber10+

PhonePC/2in1TabletTVWearable

type CommonEventSubscriber = \_CommonEventSubscriber

描述公共事件的订阅者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| [\_CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md#commoneventsubscriber-1) | 描述公共事件的订阅者。 |

## CommonEventSubscribeInfo10+

PhonePC/2in1TabletTVWearable

type CommonEventSubscribeInfo = \_CommonEventSubscribeInfo

用于表示订阅者的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| [\_CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 用于表示订阅者的信息。 |

## CommonEventPublishData10+

PhonePC/2in1TabletTVWearable

type CommonEventPublishData = \_CommonEventPublishData

描述公共事件内容和属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 类型 | 说明 |
| --- | --- |
| [\_CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md) | 描述公共事件内容和属性。 |
