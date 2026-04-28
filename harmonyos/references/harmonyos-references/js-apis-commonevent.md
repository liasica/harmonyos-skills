---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commonevent
title: @ohos.commonEvent (公共事件模块)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @ohos.commonEvent (公共事件模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2747753b25e533638888e85fb0b62f0d05cb3b5174bef00c66b2c6b4b16e2a3b
---

本模块提供了公共事件的能力，包括公共事件的权限列表，发布公共事件，订阅或取消订阅公共事件，获取或修改公共事件结果代码、结果数据等。

说明

* 从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.commonEventManager](js-apis-commoneventmanager.md)。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import commonEvent from '@ohos.commonEvent';
```

## Support

PhonePC/2in1TabletTVWearable

系统公共事件是指由系统服务或系统应用发布的事件，订阅这些系统公共事件需要特定的权限。发布或订阅这些事件需要使用如下链接中的枚举定义。

全部系统公共事件枚举定义请参见[系统公共事件定义](commonevent-definitions.md)。

## commonEvent.publish(deprecated)

PhonePC/2in1TabletTVWearable

publish(event: string, callback: AsyncCallback<void>): void

发布公共事件（回调形式）。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发送的公共事件。 |
| callback | AsyncCallback<void> | 是 | 表示指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';

3. //发布公共事件回调
4. function publishCB(err:Base.BusinessError) {
5. if (err.code) {
6. console.error(`publish failed, code is ${err.code}`);
7. } else {
8. console.info("publish");
9. }
10. }

12. //发布公共事件
13. commonEvent.publish("event", publishCB);
```

## commonEvent.publish(deprecated)

PhonePC/2in1TabletTVWearable

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

以回调的形式发布公共事件。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发布的公共事件。 |
| options | [CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md) | 是 | 表示发布公共事件的属性。 |
| callback | AsyncCallback<void> | 是 | 表示指定的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import CommonEventManager from '@ohos.commonEventManager';

4. //公共事件相关信息
5. let options:CommonEventManager.CommonEventPublishData = {
6. code: 0,             //公共事件的初始代码
7. data: "initial data",//公共事件的初始数据
8. isOrdered: true  //有序公共事件
9. }

11. //发布公共事件回调
12. function publishCB(err:Base.BusinessError) {
13. if (err.code) {
14. console.error(`publish failed, code is ${err.code}`);
15. } else {
16. console.info("publish");
17. }
18. }

20. //发布公共事件
21. commonEvent.publish("event", options, publishCB);
```

## commonEvent.createSubscriber(deprecated)

PhonePC/2in1TabletTVWearable

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

以回调形式创建订阅者。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |
| callback | AsyncCallback<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md)> | 是 | 表示创建订阅者的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import CommonEventManager from '@ohos.commonEventManager';

4. let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

6. // 订阅者信息
7. let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
8. events: ["event"]
9. };

11. // 创建订阅者回调
12. function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
13. if (err.code) {
14. console.error(`createSubscriber failed, code is ${err.code}`);
15. } else {
16. console.info("createSubscriber");
17. subscriber = commonEventSubscriber;
18. }
19. }

21. // 创建订阅者
22. commonEvent.createSubscriber(subscribeInfo, createCB);
```

## commonEvent.createSubscriber(deprecated)

PhonePC/2in1TabletTVWearable

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

以Promise形式创建订阅者。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.createSubscriber](js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md)> | 返回订阅者对象。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import CommonEventManager from '@ohos.commonEventManager';

4. let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

6. // 订阅者信息
7. let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
8. events: ["event"]
9. };

11. // 创建订阅者
12. commonEvent.createSubscriber(subscribeInfo).then((commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
13. console.info("createSubscriber");
14. subscriber = commonEventSubscriber;
15. }).catch((err:Base.BusinessError) => {
16. console.error(`createSubscriber failed, code is ${err.code}`);
17. });
```

## commonEvent.subscribe(deprecated)

PhonePC/2in1TabletTVWearable

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

以回调形式订阅公共事件。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.subscribe](js-apis-commoneventmanager.md#commoneventmanagersubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<[CommonEventData](js-apis-inner-commonevent-commoneventdata.md)> | 是 | 表示接收公共事件数据的回调函数。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import CommonEventManager from '@ohos.commonEventManager';

4. let subscriber:CommonEventManager.CommonEventSubscriber;// 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

6. // 订阅者信息
7. let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
8. events: ["event"]
9. };

11. // 订阅公共事件回调
12. function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
13. if (err.code) {
14. console.error(`subscribe failed, code is ${err.code}`);
15. } else {
16. console.info("subscribe " + JSON.stringify(data));
17. }
18. }

20. // 创建订阅者回调
21. function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
22. if (err.code) {
23. console.error(`createSubscriber failed, code is ${err.code}`);
24. } else {
25. console.info("createSubscriber");
26. subscriber = commonEventSubscriber;
27. // Subscribe to a common event.
28. commonEvent.subscribe(subscriber, subscribeCB);
29. }
30. }

32. // 创建订阅者
33. commonEvent.createSubscriber(subscribeInfo, createCB);
```

## commonEvent.unsubscribe(deprecated)

PhonePC/2in1TabletTVWearable

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

以回调形式取消订阅公共事件。

说明

从 API version 7开始支持，从API version 9开始废弃。建议使用[commonEventManager.unsubscribe](js-apis-commoneventmanager.md#commoneventmanagerunsubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<void> | 否 | 表示取消订阅的回调方法。 |

**示例：**

```
1. import Base from '@ohos.base';
2. import CommonEventManager from '@ohos.commonEventManager';

4. let subscriber:CommonEventManager.CommonEventSubscriber;    // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作

6. // 订阅者信息
7. let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
8. events: ["event"]
9. };

11. // 订阅公共事件回调
12. function subscribeCB(err:Base.BusinessError, data:CommonEventManager.CommonEventData) {
13. if (err.code) {
14. console.error(`subscribe failed, code is ${err.code}`);
15. } else {
16. console.info("subscribe " + JSON.stringify(data));
17. }
18. }

20. // 创建订阅者回调
21. function createCB(err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) {
22. if (err.code) {
23. console.error(`createSubscriber failed, code is ${err.code}`);
24. } else {
25. console.info("createSubscriber");
26. subscriber = commonEventSubscriber;
27. // Subscribe to a common event.
28. commonEvent.subscribe(subscriber, subscribeCB);
29. }
30. }

32. // 取消订阅公共事件回调
33. function unsubscribeCB(err:Base.BusinessError) {
34. if (err.code) {
35. console.error(`unsubscribe failed, code is ${err.code}`);
36. } else {
37. console.info("unsubscribe");
38. }
39. }

41. // 创建订阅者
42. commonEvent.createSubscriber(subscribeInfo, createCB);

44. // 取消订阅公共事件
45. commonEvent.unsubscribe(subscriber, unsubscribeCB);
```
