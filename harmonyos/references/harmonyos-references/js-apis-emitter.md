---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-emitter
title: "@ohos.events.emitter (Emitter)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > @ohos.events.emitter (Emitter)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:165c5b13cac17c3c6e12c7a944ef52d72046ffc5856292ebfc09fba99b59fcbd
---

本模块提供进程内线程间或线程内事件的发送与处理能力。开发者可以使用本模块的 API，订阅事件（持续订阅或单次订阅）、取消订阅事件，发送事件到事件队列中，以及查询事件的订阅数量，从而实现同一进程内不同线程之间、以及同一线程内的事件通信。适用于跨线程通信、模块解耦、事件驱动等场景，能够帮助开发者实现轻量级的发布-订阅模式，降低组件间的耦合度，提升代码的可维护性和可扩展性。

提供两种事件处理入口，开发者可根据隔离需求选择：

* **命名空间级 API**（emitter 命名空间下的 on、once、off、emit、getListenerCount 等函数）：提供进程内全局范围的事件订阅与发布能力。该入口基于全局事件队列工作，同进程内任意线程均可订阅和发布事件，适用于跨线程事件通信。
* **实例级 API**（Emitter 类）：提供同一 Emitter 实例范围内的事件订阅与发布能力。不同 Emitter 实例之间相互隔离，开发者可创建多个独立的事件通信通道，适用于需要事件隔离或按实例分组的场景。

**API 组合使用关系说明：**

本模块的事件通信遵循"订阅 → 发布 → 处理 → 取消订阅"的组合调用模式。无论是命名空间级 API 还是实例级 API，均需先订阅事件，再由其他线程或同一线程发布事件，收到事件后执行回调处理；当不再需要接收事件时，应取消订阅以释放资源。同时，事件订阅具有明确的生命周期，开发者应注意资源管理：

* **持续订阅**（on）：订阅后持续有效，直至调用 off 取消订阅。若未取消，订阅将一直保留。
* **单次订阅**（once）：订阅后，仅在首次接收到事件并执行回调后自动取消，无需手动调用 off。
* **取消订阅的时机**：调用 off 取消订阅后，已通过 emit 发布但尚未执行的事件也将被取消，不再触发回调。同时需要注意，取消指定回调时，需传入对应的 callback 函数；若未指定，表示取消该事件的所有订阅。

**说明** 

本模块首批接口从API version 7开始支持。后续版本新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { emitter } from '@kit.BasicServicesKit';
```

## emitter.on

on(event: InnerEvent, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 持续订阅的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)在订阅事件时无需指定，也不生效。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

// 收到eventId为1的事件后执行回调处理函数
emitter.on(innerEvent, callback);
```

## emitter.on11+

on(eventId: string, callback: Callback<EventData>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// 收到eventId为"eventId"的事件后执行回调处理函数
emitter.on('eventId', callback);
```

## emitter.on12+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};
// 收到eventId为"eventId"的事件后执行回调函数
emitter.on('eventId', callback);
```

## emitter.once

once(event: InnerEvent, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调处理函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 单次订阅的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)在订阅事件时无需指定，也不生效。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let innerEvent: emitter.InnerEvent = {
  eventId: 1
};

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// 收到eventId为1的事件后执行该回调处理函数
emitter.once(innerEvent, callback);
```

## emitter.once11+

once(eventId: string, callback: Callback<EventData>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调处理函数后，自动取消订阅。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// 收到eventId为"eventId"的事件后执行该回调函数
emitter.once('eventId', callback);
```

## emitter.once12+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅指定的事件，在接收到该事件且执行完对应的回调处理函数后，自动取消订阅。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 接收到该事件时需要执行的回调处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};
// 收到eventId为"eventId"的事件后执行回调函数
emitter.once('eventId', callback);
```

## emitter.off

off(eventId: number): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID，由开发者定义，用于辨别事件。 |

**示例：**

```ts
// 取消eventId为1的所有事件回调处理函数
emitter.off(1);
```

## emitter.off11+

off(eventId: string): void

取消事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |

**示例：**

```ts
// 取消eventId为"eventId1"的所有事件回调处理函数
emitter.off('eventId1');
```

## emitter.off10+

off(eventId: number, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron)或[once](js-apis-emitter.md#emitteronce)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | 是 | 事件ID，由开发者定义，用于辨别事件。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的callback一致。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// 取消eventId为1的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off(1, callback);
```

## emitter.off11+

off(eventId: string, callback: Callback<EventData>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron11)或[once](js-apis-emitter.md#emitteronce11)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit11)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的callback一致。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};
// 取消eventId为"eventId1"的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off('eventId1', callback);
```

## emitter.off12+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用[on](js-apis-emitter.md#emitteron12)或[once](js-apis-emitter.md#emitteronce12)接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emitteremit12)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，指定要取消订阅的事件处理函数，需与订阅时使用的callback一致。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};
// 取消eventId为"eventId1"的事件回调处理函数，callback对象应使用订阅时的对象
// 如果该回调处理函数没有被订阅，则不做任何处理
emitter.off('eventId1', callback);
```

## emitter.emit

emit(event: InnerEvent, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [InnerEvent](js-apis-emitter.md#innerevent) | 是 | 发送的事件，其中[EventPriority](js-apis-emitter.md#eventpriority)用于指定事件被发送的优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let innerEvent: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};

emitter.emit(innerEvent, eventData);
```

## emitter.emit11+

emit(eventId: string, data?: EventData): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter.emit('eventId', eventData);
```

## emitter.emit12+

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
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

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};
emitter.emit('eventId', eventData);
```

## emitter.emit11+

emit(eventId: string, options: Options, data?: EventData): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};

emitter.emit('eventId', options, eventData);
```

## emitter.emit12+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
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

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter.emit('eventId', options, eventData);
```

## emitter.getListenerCount11+

getListenerCount(eventId: number | string): number

获取指定事件的订阅数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | number | string | 是 | 事件ID，由开发者定义，用于辨别事件。  string类型：不可为空字符串，大小不超过10240字节，超出部分会被截断。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```ts
let count: number = emitter.getListenerCount('eventId');
```

## EventPriority

表示事件的优先级。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMMEDIATE | 0 | 表示事件先于HIGH优先级投递。 |
| HIGH | 1 | 表示事件先于LOW优先级投递。 |
| LOW | 2 | 表示事件先于IDLE优先级投递，事件的默认优先级是LOW。 |
| IDLE | 3 | 表示在没有其他事件的情况下，才投递该事件。 |

## InnerEvent

订阅或发送的事件，订阅事件时EventPriority不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventId | number | 否 | 否 | 事件ID，由开发者定义，用于辨别事件。 |
| priority | [EventPriority](js-apis-emitter.md#eventpriority) | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

## EventData

发送事件时传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | { [key: string]: any } | 否 | 是 | 发送事件时传递的数据，支持数据类型包括Array、ArrayBuffer、Boolean、DataView、Date、Error、Map、Number、Object、Primitive（除了symbol）、RegExp、Set、String、TypedArray，数据大小最大为16MB，超出限制时事件发送失败。 |

## Options11+

发送事件的优先级。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [EventPriority](js-apis-emitter.md#eventpriority) | 否 | 是 | 事件的优先级，默认值为EventPriority.LOW。 |

## GenericEventData<T>12+

发送事件时传递的泛型数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | T | 否 | 是 | 发送事件时传递的数据。T：泛型类型，由开发者根据业务需要自定义具体的数据类型。 |

## Emitter22+

该功能支持在同一进程的同一Emitter类实例中，跨不同线程或同一线程内发送和处理事件。它能够实现持续订阅事件、单次订阅事件、取消订阅事件以及将事件发送到事件队列，适用于需要基于独立实例进行线程间通信和事件管理的场景，不同Emitter实例类之间相互隔离，互不影响。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

### constructor22+

constructor()

构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**示例：**

```ts
let emitter1: emitter.Emitter = new emitter.Emitter();
```

### on22+

on(eventId: string, callback: Callback<EventData>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.on('eventId', callback);
```

### on22+

on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

持续订阅当前Emitter类实例指定的事件，并在接收到该事件时，使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 持续订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};

emitter1.on('eventId', callback);
```

### once22+

once(eventId: string, callback: Callback<EventData>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完对应的回调处理函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.once('eventId', callback);
```

### once22+

once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

单次订阅当前Emitter类实例指定的事件，在接收到该事件且执行完对应的回调处理函数后，自动取消订阅。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，在接收到该事件时被调用。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

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

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};

emitter1.once('eventId', callback);
```

### off22+

off(eventId: string): void

取消当前Emitter类实例事件ID为eventId的所有订阅。

使用该接口取消某个事件订阅后，已通过[emit](js-apis-emitter.md#emit22)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |

**示例：**

```ts
let emitter1: emitter.Emitter = new emitter.Emitter();

emitter1.off('eventId');
```

### off22+

off(eventId: string, callback: Callback<EventData>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](js-apis-emitter.md#on22)或[once](js-apis-emitter.md#once22)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](js-apis-emitter.md#emit22)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[EventData](js-apis-emitter.md#eventdata)> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.EventData> = (eventData: emitter.EventData) => {
  console.info(`eventData: ${JSON.stringify(eventData)}`);
};

emitter1.off('eventId', callback);
```

### off22+

off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void

取消订阅当前Emitter类实例的事件。仅当已使用[on](js-apis-emitter.md#on22-1)或[once](js-apis-emitter.md#once22-1)接口订阅了事件ID为eventId且回调处理函数为callback的事件时，该接口才生效。

使用该接口取消事件订阅后，已通过[emit](js-apis-emitter.md#emit22-1)接口发布但尚未被执行的事件将被取消。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| callback | Callback<[GenericEventData<T>](js-apis-emitter.md#genericeventdatat12)> | 是 | 回调函数，指定要取消订阅的事件处理函数。 |

**示例：**

```ts
import { Callback } from '@kit.BasicServicesKit';

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

let emitter1: emitter.Emitter = new emitter.Emitter();

let callback: Callback<emitter.GenericEventData<Sample>> = (eventData: emitter.GenericEventData<Sample>): void => {
  console.info(`eventData: ${JSON.stringify(eventData?.data)}`);
  if (eventData?.data instanceof Sample) {
    eventData?.data?.printCount();
  }
};

emitter1.off('eventId', callback);
```

### emit22+

emit(eventId: string, data?: EventData): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
let emitter1: emitter.Emitter = new emitter.Emitter();
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter1.emit('eventId', eventData);
```

### emit22+

emit<T>(eventId: string, data?: GenericEventData<T>): void

发送指定事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
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

let emitter1: emitter.Emitter = new emitter.Emitter();

let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit('eventId', eventData);
```

### emit22+

emit(eventId: string, options: Options, data?: EventData): void

发送指定优先级事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [EventData](js-apis-emitter.md#eventdata) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.EventData = {
  data: {
    "content": "content",
    "id": 1,
  }
};

emitter1.emit('eventId', options, eventData);
```

### emit22+

emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void

发送指定优先级事件到当前Emitter类实例。

该接口支持跨线程传输数据对象，需要遵循数据跨线程传输的规格约束，详见[线程间通信对象](../harmonyos-guides/serializable-overview.md)。目前不支持使用[@State装饰器](../harmonyos-guides/arkts-state.md)、[@Observed装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)等装饰器修饰的复杂类型数据。

该接口发布某个事件后，不保证该事件立刻执行，执行时间取决于事件队列里面的事件数量以及各事件的执行效率。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 发送的事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。 |
| options | [Options](js-apis-emitter.md#options11) | 是 | 事件优先级。 |
| data | [GenericEventData<T>](js-apis-emitter.md#genericeventdatat12) | 否 | 事件携带的数据，默认为空。 |

**示例：**

```ts
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

let emitter1: emitter.Emitter = new emitter.Emitter();

let options: emitter.Options = {
  priority: emitter.EventPriority.HIGH
};
let eventData: emitter.GenericEventData<Sample> = {
  data: new Sample()
};

emitter1.emit('eventId', options, eventData);
```

### getListenerCount22+

getListenerCount(eventId: string): number

获取当前Emitter类实例指定事件的订阅数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 事件ID。  不可为空字符串，大小不超过10240字节，超出部分会被截断。。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定事件的订阅数。 |

**示例：**

```ts
let emitter1: emitter.Emitter = new emitter.Emitter();
let count: number = emitter1.getListenerCount('eventId');
```
