---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commonevent
title: "@ohos.commonEvent (公共事件模块)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @ohos.commonEvent (公共事件模块)
category: harmonyos-references
scraped_at: 2026-10-11T07:26:30+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:256c3ef3fba2f4ce06096d4f1307001731451b36665432cb4c4b113cbda60d82
---

本模块提供了公共事件的能力，包括公共事件的权限列表，发布公共事件，订阅或取消订阅公共事件，获取或修改公共事件结果代码、结果数据等。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[@ohos.commonEventManager](js-apis-commoneventmanager.md)替代。

## 导入模块

```ts
import commonEvent from '@ohos.commonEvent';
```

## Support

[系统公共事件](../harmonyos-guides/common-event-glossary.md#system-common-event系统公共事件)是指由系统服务或系统应用发布的事件，订阅这些系统公共事件需要特定的权限。发布或订阅这些事件需要使用如下链接中的枚举定义。

全部系统公共事件枚举定义请参见[系统公共事件定义](commonevent-definitions.md)。

## commonEvent.publish(deprecated)

publish(event: string, callback: AsyncCallback<void>): void

以回调形式发布公共事件。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发布的公共事件。字符串长度不超过254字节，超出部分会被截断。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import Base from '@ohos.base';

// 发布公共事件回调
let publishCallBack = (err: Base.BusinessError) => {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('publish');
    }
}

// 发布公共事件
commonEvent.publish("event", publishCallBack);
```

## commonEvent.publish(deprecated)

publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void

以回调形式发布公共事件。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.publish](js-apis-commoneventmanager.md#commoneventmanagerpublish-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 表示要发布的公共事件。字符串长度不超过254字节，超出部分会被截断。 |
| options | [CommonEventPublishData](js-apis-inner-commonevent-commoneventpublishdata.md) | 是 | 表示发布公共事件的属性。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当公共事件发布成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

// 公共事件相关信息
let options:CommonEventManager.CommonEventPublishData = {
    code: 0,             // 公共事件的初始代码
    data: "initial data", // 公共事件的初始数据
    isOrdered: true  // 有序公共事件
};

// 发布公共事件回调
let publishCallBack = (err: Base.BusinessError) => {
    if (err.code) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("publish");
    }
}

// 发布公共事件
commonEvent.publish("event", options, publishCallBack);
```

## commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void

以回调形式创建订阅者。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.createSubscriber](js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |
| callback | AsyncCallback<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md)> | 是 | 回调函数。当创建公共事件订阅者成功，err为undefined，data为获取到的公共事件订阅者，否则为错误对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及取消订阅的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者回调
let createCallBack = (err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCallBack);
```

## commonEvent.createSubscriber(deprecated)

createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>

以Promise形式创建订阅者。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.createSubscriber](js-apis-commoneventmanager.md#commoneventmanagercreatesubscriber-1)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 是 | 表示订阅信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md)> | Promise对象，返回订阅者对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及取消订阅的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo).then((commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    console.info("createSubscriber");
    subscriber = commonEventSubscriber;
}).catch((err:Base.BusinessError) => {
    console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
});
```

## commonEvent.subscribe(deprecated)

subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void

以回调形式订阅公共事件。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.subscribe](js-apis-commoneventmanager.md#commoneventmanagersubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<[CommonEventData](js-apis-inner-commonevent-commoneventdata.md)> | 是 | 回调函数。当订阅公共事件成功，err为undefined，data为获取到的公共事件数据，否则为错误对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber; // 用于保存创建成功的订阅者对象，后续使用其完成订阅及取消订阅的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
let subscribeCallBack = (err:Base.BusinessError, data:CommonEventManager.CommonEventData) => {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
let createCallBack = (err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
         // 订阅公共事件
        commonEvent.subscribe(subscriber, subscribeCallBack);
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCallBack);
```

## commonEvent.unsubscribe(deprecated)

unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void

以回调形式取消订阅公共事件。

**说明** 

从API version 7 开始支持，从API version 9 开始废弃，建议使用[commonEventManager.unsubscribe](js-apis-commoneventmanager.md#commoneventmanagerunsubscribe)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | [CommonEventSubscriber](js-apis-inner-commonevent-commoneventsubscriber.md) | 是 | 表示订阅者对象。 |
| callback | AsyncCallback<void> | 否 | 回调函数。当取消公共事件订阅成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import Base from '@ohos.base';
import CommonEventManager from '@ohos.commonEventManager';

let subscriber:CommonEventManager.CommonEventSubscriber;    // 用于保存创建成功的订阅者对象，后续使用其完成订阅及取消订阅的动作

// 订阅者信息
let subscribeInfo:CommonEventManager.CommonEventSubscribeInfo = {
    events: ["event"]
};

// 订阅公共事件回调
let subscribeCallBack = (err:Base.BusinessError, data:CommonEventManager.CommonEventData) => {
    if (err.code) {
        console.error(`subscribe failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("subscribe " + JSON.stringify(data));
    }
}

// 创建订阅者回调
let createCallBack = (err:Base.BusinessError, commonEventSubscriber:CommonEventManager.CommonEventSubscriber) => {
    if (err.code) {
        console.error(`createSubscriber failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("createSubscriber");
        subscriber = commonEventSubscriber;
         // 订阅公共事件
        commonEvent.subscribe(subscriber, subscribeCallBack);
    }
}

// 取消订阅公共事件回调
let unsubscribeCallback = (err: Base.BusinessError) => {
    if (err.code) {
        console.error(`unsubscribe failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("unsubscribe");
    }
}

// 创建订阅者
commonEvent.createSubscriber(subscribeInfo, createCallBack);

// 取消订阅公共事件
// 注意：需在subscriber创建成功后（即createCallBack回调执行后）调用，此处仅展示API用法
commonEvent.unsubscribe(subscriber, unsubscribeCallback);
```
