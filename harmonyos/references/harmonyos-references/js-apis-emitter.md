---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter
title: @ohos.events.emitter (Emitter)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > @ohos.events.emitter (Emitter)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c08fc06f96a2dd19a8a73cf0d3b3cf4d2f49640934fb1b57cb41d8851062ca9
---

本模块提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。

说明

本模块首批接口从API version 7开始支持。后续版本新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { emitter } from '@kit.BasicServicesKit';
```

## emitter.on

PhonePC/2in1TabletTVWearable

on(event: InnerEvent, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 持续订阅的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)，在订阅事件时无需指定，也不生效。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let innerEvent: emitter.InnerEvent = {
4. eventId: 1
5. };

7. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
8. console.info(`eventData: ${JSON.stringify(eventData)}`);
9. }

11. // 收到eventId为1的事件后执行回调函数
12. emitter.on(innerEvent, callback);
```

## emitter.on11+

PhonePC/2in1TabletTVWearable

on(eventId: string, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
4. console.info(`eventData: ${JSON.stringify(eventData)}`);
5. }
6. // 收到eventId为"eventId"的事件后执行回调函数
7. emitter.on(`eventId`, callback);
```

## emitter.on12+

PhonePC/2in1TabletTVWearable

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. @Sendable
4. class Sample {
5. constructor() {
6. this.count = 100;
7. }
8. printCount() {
9. console.info('Print count : ' + this.count);
10. }
11. count: number;
12. }

14. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
15. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
16. if (eventData?.data instanceof Sample) {
17. eventData?.data?.printCount();
18. }
19. }
20. // 收到eventId为"eventId"的事件后执行回调函数
21. emitter.on("eventId", callback);
```

## emitter.once

PhonePC/2in1TabletTVWearable

once(event: InnerEvent, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 单次订阅的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)，在订阅事件时无需指定，也不生效。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let innerEvent: emitter.InnerEvent = {
4. eventId: 1
5. };

7. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
8. console.info(`eventData: ${JSON.stringify(eventData)}`);
9. }
10. // 收到eventId为1的事件后执行该回调函数
11. emitter.once(innerEvent, callback);
```

## emitter.once11+

PhonePC/2in1TabletTVWearable

once(eventId: string, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
4. console.info(`eventData: ${JSON.stringify(eventData)}`);
5. }
6. // 收到eventId为"eventId"的事件后执行该回调函数
7. emitter.once("eventId", callback);
```

## emitter.once12+

PhonePC/2in1TabletTVWearable

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅指定的事件，在接收到该事件且执行完相应的回调函数后，自动取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. @Sendable
4. class Sample {
5. constructor() {
6. this.count = 100;
7. }
8. printCount() {
9. console.info('Print count : ' + this.count);
10. }
11. count: number;
12. }

14. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
15. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
16. if (eventData?.data instanceof Sample) {
17. eventData?.data?.printCount();
18. }
19. }
20. // 收到eventId为"eventId"的事件后执行回调函数
21. emitter.once("eventId", callback);
```

## emitter.off

PhonePC/2in1TabletTVWearable

off(eventId: number): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID。 |

**示例：**

```
1. // 取消eventId为1的所有事件回调处理函数
2. emitter.off(1);
```

## emitter.off11+

PhonePC/2in1TabletTVWearable

off(eventId: string): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**示例：**

```
1. // 取消eventId为"eventId1"的所有事件回调处理函数
2. emitter.off("eventId1");
```

## emitter.off10+

PhonePC/2in1TabletTVWearable

off(eventId: number, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron)或[once](js-apis-emitter.md#emitteronce)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 事件的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
4. console.info(`eventData: ${JSON.stringify(eventData)}`);
5. }
6. // 取消eventId为1的事件回调处理函数，callback对象应使用订阅时的对象
7. // 如果该回调处理函数没有被订阅，则不做任何处理
8. emitter.off(1, callback);
```

## emitter.off11+

PhonePC/2in1TabletTVWearable

off(eventId: string, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron11)或[once](js-apis-emitter.md#emitteronce11)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 事件的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
4. console.info(`eventData: ${JSON.stringify(eventData)}`);
5. }
6. // 取消eventId为"eventId1"的事件回调处理函数，callback对象应使用订阅时的对象
7. // 如果该回调处理函数没有被订阅，则不做任何处理
8. emitter.off("eventId1", callback);
```

## emitter.off12+

PhonePC/2in1TabletTVWearable

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron12)或[once](js-apis-emitter.md#emitteronce12)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit12)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 事件的回调处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. @Sendable
4. class Sample {
5. constructor() {
6. this.count = 100;
7. }
8. printCount() {
9. console.info('Print count : ' + this.count);
10. }
11. count: number;
12. }

14. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
15. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
16. if (eventData?.data instanceof Sample) {
17. eventData?.data?.printCount();
18. }
19. }
20. // 取消eventId为"eventId1"的事件回调处理函数，callback对象应使用订阅时的对象
21. // 如果该回调处理函数没有被订阅，则不做任何处理
22. emitter.off("eventId1", callback);
```

## emitter.emit

PhonePC/2in1TabletTVWearable

emit(event: InnerEvent, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 发送的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)用于指定事件被发送的优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. let eventData: emitter.EventData = {
2. data: {
3. "content": "content",
4. "id": 1,
5. }
6. };

8. let innerEvent: emitter.InnerEvent = {
9. eventId: 1,
10. priority: emitter.EventPriority.HIGH
11. };

13. emitter.emit(innerEvent, eventData);
```

## emitter.emit11+

PhonePC/2in1TabletTVWearable

emit(eventId: string, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. let eventData: emitter.EventData = {
2. data: {
3. "content": "content",
4. "id": 1,
5. }
6. };

8. emitter.emit("eventId", eventData);
```

## emitter.emit12+

PhonePC/2in1TabletTVWearable

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. @Sendable
2. class Sample {
3. constructor() {
4. this.count = 100;
5. }
6. printCount() {
7. console.info('Print count : ' + this.count);
8. }
9. count: number;
10. }

12. let eventData: emitter.GenericEventData<Sample> = {
13. data: new Sample()
14. };
15. emitter.emit("eventId", eventData);
```

## emitter.emit11+

PhonePC/2in1TabletTVWearable

emit(eventId: string, options: Options, data?: EventData): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. let eventData: emitter.EventData = {
2. data: {
3. "content": "content",
4. "id": 1,
5. }
6. };

8. let options: emitter.Options = {
9. priority: emitter.EventPriority.HIGH
10. };

12. emitter.emit("eventId", options, eventData);
```

## emitter.emit12+

PhonePC/2in1TabletTVWearable

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. @Sendable
2. class Sample {
3. constructor() {
4. this.count = 100;
5. }
6. printCount() {
7. console.info('Print count : ' + this.count);
8. }
9. count: number;
10. }

12. let options: emitter.Options = {
13. priority: emitter.EventPriority.HIGH
14. };
15. let eventData: emitter.GenericEventData<Sample> = {
16. data: new Sample()
17. };

19. emitter.emit("eventId", options, eventData);
```

## emitter.getListenerCount11+

PhonePC/2in1TabletTVWearable

getListenerCount(eventId: number | string): number

获取指定事件的订阅数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | string | 是 | 事件ID，string类型的eventId取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```
1. let count: number = emitter.getListenerCount("eventId");
```

## EventPriority

PhonePC/2in1TabletTVWearable

表示事件的优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Notification.Emitter

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMMEDIATE | 0 | 表示事件先于HIGH优先级投递。 |
| HIGH | 1 | 表示事件先于LOW优先级投递。 |
| LOW | 2 | 表示事件优于IDLE优先级投递，事件的默认优先级是LOW。 |
| IDLE | 3 | 表示在没有其他事件的情况下，才投递该事件。 |

## InnerEvent

PhonePC/2in1TabletTVWearable

订阅或发送的事件，订阅事件时EventPriority不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID，由开发者定义，用于辨别事件。 |
| priority | [EventPriority](js-apis-emitter.md#eventpriority) | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

## EventData

PhonePC/2in1TabletTVWearable

发送事件时传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | { [key: string]: any } | 否 | 是 | 发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小最大为16M。 |

## Options11+

PhonePC/2in1TabletTVWearable

发送事件的优先级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [EventPriority](js-apis-emitter.md#eventpriority) | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

## GenericEventData<T>12+

PhonePC/2in1TabletTVWearable

发送事件时传递的泛型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | T | 否 | 是 | 发送事件时传递的数据。T：泛型类型。 |

## Emitter22+

PhonePC/2in1TabletTVWearable

该功能支持在同一进程的同一Emitter类实例中，跨不同线程或同一线程内发送和处理事件。它能够实现持续订阅事件、单次订阅事件、取消订阅事件以及将事件发送到事件队列。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

### constructor22+

PhonePC/2in1TabletTVWearable

constructor()

构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**示例：**

```
1. let emitter1: emitter.Emitter = new emitter.Emitter();
```

### on22+

PhonePC/2in1TabletTVWearable

on(eventId: string, callback: Callback<EventData>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let emitter1: emitter.Emitter = new emitter.Emitter();

5. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
6. console.info(`eventData: ${JSON.stringify(eventData)}`);
7. }

9. emitter1.on(`eventId`, callback);
```

### on22+

PhonePC/2in1TabletTVWearable

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let emitter1: emitter.Emitter = new emitter.Emitter();

5. @Sendable
6. class Sample {
7. constructor() {
8. this.count = 100;
9. }
10. printCount() {
11. console.info('Print count : ' + this.count);
12. }
13. count: number;
14. }

16. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
17. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
18. if (eventData?.data instanceof Sample) {
19. eventData?.data?.printCount();
20. }
21. }

23. emitter1.on("eventId", callback);
```

### once22+

PhonePC/2in1TabletTVWearable

once(eventId: string, callback: Callback<EventData>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let emitter1: emitter.Emitter = new emitter.Emitter();

5. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
6. console.info(`eventData: ${JSON.stringify(eventData)}`);
7. }

9. emitter1.once("eventId", callback);
```

### once22+

PhonePC/2in1TabletTVWearable

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完相应的回调函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let emitter1: emitter.Emitter = new emitter.Emitter();

5. @Sendable
6. class Sample {
7. constructor() {
8. this.count = 100;
9. }
10. printCount() {
11. console.info('Print count : ' + this.count);
12. }
13. count: number;
14. }

16. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
17. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
18. if (eventData?.data instanceof Sample) {
19. eventData?.data?.printCount();
20. }
21. }

23. emitter1.once("eventId", callback);
```

### off22+

PhonePC/2in1TabletTVWearable

off(eventId: string): void

取消当前Emitter类实例事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emit22)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**示例：**

```
1. let emitter1: emitter.Emitter = new emitter.Emitter();

3. emitter1.off("eventId");
```

### off22+

PhonePC/2in1TabletTVWearable

off(eventId: string, callback: Callback<EventData>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](js-apis-emitter.md#on22)或[once](js-apis-emitter.md#once22)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](js-apis-emitter.md#emit22)接口发布但尚未执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let emitter1: emitter.Emitter = new emitter.Emitter();

5. let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
6. console.info(`eventData: ${JSON.stringify(eventData)}`);
7. }

9. emitter1.off("eventId", callback);
```

### off22+

PhonePC/2in1TabletTVWearable

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](js-apis-emitter.md#on22-1)或[once](js-apis-emitter.md#once22-1)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](js-apis-emitter.md#emit22-1)接口发布但尚未执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. @Sendable
4. class Sample {
5. constructor() {
6. this.count = 100;
7. }
8. printCount() {
9. console.info('Print count : ' + this.count);
10. }
11. count: number;
12. }

14. let emitter1: emitter.Emitter = new emitter.Emitter();

16. let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
17. console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
18. if (eventData?.data instanceof Sample) {
19. eventData?.data?.printCount();
20. }
21. }

23. emitter1.off("eventId", callback);
```

### emit22+

PhonePC/2in1TabletTVWearable

emit(eventId: string, data?: EventData): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始支持元服务。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. let emitter1: emitter.Emitter = new emitter.Emitter();
2. let eventData: emitter.EventData = {
3. data: {
4. "content": "content",
5. "id": 1,
6. }
7. };

9. emitter1.emit("eventId", eventData);
```

### emit22+

PhonePC/2in1TabletTVWearable

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. @Sendable
2. class Sample {
3. constructor() {
4. this.count = 100;
5. }
6. printCount() {
7. console.info('Print count : ' + this.count);
8. }
9. count: number;
10. }

12. let emitter1: emitter.Emitter = new emitter.Emitter();

14. let eventData: emitter.GenericEventData<Sample> = {
15. data: new Sample()
16. };

18. emitter1.emit("eventId", eventData);
```

### emit22+

PhonePC/2in1TabletTVWearable

emit(eventId: string, options: Options, data?: EventData): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始支持元服务。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. let emitter1: emitter.Emitter = new emitter.Emitter();

3. let options: emitter.Options = {
4. priority: emitter.EventPriority.HIGH
5. };
6. let eventData: emitter.EventData = {
7. data: {
8. "content": "content",
9. "id": 1,
10. }
11. };

13. emitter1.emit("eventId", options, eventData);
```

### emit22+

PhonePC/2in1TabletTVWearable

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```
1. @Sendable
2. class Sample {
3. constructor() {
4. this.count = 100;
5. }
6. printCount() {
7. console.info('Print count : ' + this.count);
8. }
9. count: number;
10. }

12. let emitter1: emitter.Emitter = new emitter.Emitter();

14. let options: emitter.Options = {
15. priority: emitter.EventPriority.HIGH
16. };
17. let eventData: emitter.GenericEventData<Sample> = {
18. data: new Sample()
19. };

21. emitter1.emit("eventId", options, eventData);
```

### getListenerCount22+

PhonePC/2in1TabletTVWearable

getListenerCount(eventId: string): number

获取当前Emitter类实例指定事件的订阅数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID，取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```
1. let emitter1: emitter.Emitter = new emitter.Emitter();
2. let count = emitter1.getListenerCount("eventId");
```
