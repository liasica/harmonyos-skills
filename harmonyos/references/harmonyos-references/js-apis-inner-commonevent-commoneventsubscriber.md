---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventsubscriber
title: commonEventSubscriber
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > commonEvent > commonEventSubscriber
category: harmonyos-references
scraped_at: 2026-04-28T08:09:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0239783becf0be38506b0786c8a7614691e76b0ade8c2949f54504d3e833665
---

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## CommonEventSubscriber

PhonePC/2in1TabletTVWearable

表示公共事件的订阅者。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

### 使用说明

在使用CommonEventSubscriber的功能前，需要通过commonEventManager.createSubscriber获取subscriber对象。

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 定义订阅者，用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
5. let subscriber: commonEventManager.CommonEventSubscriber | null = null;
6. // 订阅者信息
7. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
8. events: ['event']
9. };
10. // 创建订阅者
11. subscriber = commonEventManager.createSubscriberSync(subscribeInfo);
```

### getCode

PhonePC/2in1TabletTVWearable

getCode(callback: AsyncCallback<number>): void

获取有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。返回有序公共事件传递的数据（number类型）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.getCode((err: BusinessError, code: number) => {
2. if (err) {
3. console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
7. });
```

### getCode

PhonePC/2in1TabletTVWearable

getCode(): Promise<number>

获取有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回有序公共事件传递的数据（number类型）。 |

**示例：**

```
1. subscriber.getCode().then((code: number) => {
2. console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to get code. Code is ${err.code}, message is ${err.message}`);
5. });
```

### getCodeSync10+

PhonePC/2in1TabletTVWearable

getCodeSync(): number

获取有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 表示有序公共事件传递的数据（number类型）。 |

**示例：**

```
1. let code: number = subscriber.getCodeSync();
2. console.info(`Succeeded in getting code, code is ${JSON.stringify(code)}`);
```

### setCode

PhonePC/2in1TabletTVWearable

setCode(code: number, callback: AsyncCallback<void>): void

设置有序公共事件传递的数据（number类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置有序公共事件传递的数据（number类型）成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setCode(1, (err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in setting code.`);
7. });
```

### setCode

PhonePC/2in1TabletTVWearable

setCode(code: number): Promise<void>

设置有序公共事件传递的数据（number类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setCode(1).then(() => {
2. console.info(`Succeeded in setting code.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
5. });
```

### setCodeSync10+

PhonePC/2in1TabletTVWearable

setCodeSync(code: number): void

设置有序公共事件传递的数据（number类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. try {
2. subscriber.setCodeSync(1);
3. } catch (error) {
4. let err: BusinessError = error as BusinessError;
5. console.error(`Failed to set code. Code is ${err.code}, message is ${err.message}`);
6. }
```

### getData

PhonePC/2in1TabletTVWearable

getData(callback: AsyncCallback<string>): void

获取有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。返回有序公共事件传递的数据（string类型）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. // 获取有序公共事件传递的数据（string类型）回调
2. subscriber.getData((err: BusinessError, data: string) => {
3. if (err) {
4. console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
5. return;
6. }
7. console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
8. });
```

### getData

PhonePC/2in1TabletTVWearable

getData(): Promise<string>

获取有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回有序公共事件传递的数据（string类型）。 |

**示例：**

```
1. subscriber.getData().then((data: string) => {
2. console.info(`Succeeded in getting data, data is ${JSON.stringify(data)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to get data. Code is ${err.code}, message is ${err.message}`);
5. });
```

### getDataSync10+

PhonePC/2in1TabletTVWearable

getDataSync(): string

获取有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 有序公共事件传递的数据（string类型）。 |

**示例：**

```
1. let data: string = subscriber.getDataSync();
2. console.info(`Succeeded in getting data, data is ${data}`);
```

### setData

PhonePC/2in1TabletTVWearable

setData(data: string, callback: AsyncCallback<void>): void

设置有序公共事件传递的数据（string类型）。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置有序公共事件传递的数据（string类型）成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setData('publish_data_changed', (err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in setting data.`);
7. });
```

### setData

PhonePC/2in1TabletTVWearable

setData(data: string): Promise<void>

设置有序公共事件传递的数据（string类型）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setData('publish_data_changed').then(() => {
2. console.info(`Succeeded in setting data.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
5. });
```

### setDataSync10+

PhonePC/2in1TabletTVWearable

setDataSync(data: string): void

设置有序公共事件传递的数据（string类型）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. try {
2. subscriber.setDataSync('publish_data_changed');
3. } catch (error) {
4. let err: BusinessError = error as BusinessError;
5. console.error(`Failed to set data. Code is ${err.code}, message is ${err.message}`);
6. }
```

### setCodeAndData

PhonePC/2in1TabletTVWearable

setCodeAndData(code: number, data: string, callback:AsyncCallback<void>): void

设置有序公共事件数据。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置有序公共事件传递的数据成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setCodeAndData(1, 'publish_data_changed', (err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in setting code and data.`);
7. });
```

### setCodeAndData

PhonePC/2in1TabletTVWearable

setCodeAndData(code: number, data: string): Promise<void>

设置有序公共事件传递的数据。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.setCodeAndData(1, 'publish_data_changed').then(() => {
2. console.info(`Succeeded in setting code and data.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
5. });
```

### setCodeAndDataSync10+

PhonePC/2in1TabletTVWearable

setCodeAndDataSync(code: number, data: string): void

设置有序公共事件传递的数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 有序公共事件传递的数据（number类型）。 |
| data | string | 是 | 有序公共事件传递的数据（string类型）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. try {
2. subscriber.setCodeAndDataSync(1, 'publish_data_changed');
3. } catch (error) {
4. let err: BusinessError = error as BusinessError;
5. console.error(`Failed to set code and data. Code is ${err.code}, message is ${err.message}`);
6. }
```

### isOrderedCommonEvent

PhonePC/2in1TabletTVWearable

isOrderedCommonEvent(callback: AsyncCallback<boolean>): void

查询当前公共事件是否为有序公共事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示有序公共事件；返回false表示无序公共事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.isOrderedCommonEvent((err: BusinessError, isOrdered:boolean) => {
2. if (err) {
3. console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
7. });
```

### isOrderedCommonEvent

PhonePC/2in1TabletTVWearable

isOrderedCommonEvent(): Promise<boolean>

查询当前公共事件是否为有序公共事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示有序公共事件；返回false表示无序公共事件。 |

**示例：**

```
1. subscriber.isOrderedCommonEvent().then((isOrdered:boolean) => {
2. console.info(`isOrderedCommonEvent ${JSON.stringify(isOrdered)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`isOrderedCommonEvent failed, code is ${err.code}, message is ${err.message}`);
5. });
```

### isOrderedCommonEventSync10+

PhonePC/2in1TabletTVWearable

isOrderedCommonEventSync(): boolean

查询当前公共事件是否为有序公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示有序公共事件；返回false表示无序公共事件。 |

**示例：**

```
1. let isOrdered: boolean = subscriber.isOrderedCommonEventSync();
2. console.info(`isOrderedCommonEventSync ${JSON.stringify(isOrdered)}`);
```

### isStickyCommonEvent

PhonePC/2in1TabletTVWearable

isStickyCommonEvent(callback: AsyncCallback<boolean>): void

检查当前公共事件是否为一个粘性事件。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.isStickyCommonEvent((err: BusinessError, isSticky:boolean) => {
2. if (err) {
3. console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
7. });
```

### isStickyCommonEvent

PhonePC/2in1TabletTVWearable

isStickyCommonEvent(): Promise<boolean>

检查当前公共事件是否为一个粘性事件。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |

**示例：**

```
1. subscriber.isStickyCommonEvent().then((isSticky:boolean) => {
2. console.info(`isStickyCommonEvent ${JSON.stringify(isSticky)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`isStickyCommonEvent failed, code is ${err.code}, message is ${err.message}`);
5. });
```

### isStickyCommonEventSync10+

PhonePC/2in1TabletTVWearable

isStickyCommonEventSync(): boolean

检查当前公共事件是否为一个粘性事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示是粘性公共事件；返回false表示不是粘性公共事件。 |

**示例：**

```
1. let isSticky: boolean = subscriber.isStickyCommonEventSync();
2. console.info(`isStickyCommonEventSync ${JSON.stringify(isSticky)}`);
```

### abortCommonEvent

PhonePC/2in1TabletTVWearable

abortCommonEvent(callback: AsyncCallback<void>): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当添加有序公共事件中止状态成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.abortCommonEvent((err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in aborting common event.`);
7. });
8. subscriber.finishCommonEvent((err: BusinessError) => {
9. if (err) {
10. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in finishing common event.`);
14. });
```

### abortCommonEvent

PhonePC/2in1TabletTVWearable

abortCommonEvent(): Promise<void>

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. subscriber.abortCommonEvent().then(() => {
2. console.info(`Succeeded in aborting common event.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to abort common event. Code is ${err.code}, message is ${err.message}`);
5. });
6. subscriber.finishCommonEvent().then(() => {
7. console.info(`Succeeded in finishing common event.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
10. });
```

### abortCommonEventSync10+

PhonePC/2in1TabletTVWearable

abortCommonEventSync(): void

添加有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```
1. subscriber.abortCommonEventSync();
2. subscriber.finishCommonEvent().then(() => {
3. console.info(`Succeeded in finishing common event.`);
4. }).catch((err: BusinessError) => {
5. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
6. });
```

### clearAbortCommonEvent

PhonePC/2in1TabletTVWearable

clearAbortCommonEvent(callback: AsyncCallback<void>): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当清理有序公共事件中止状态成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.clearAbortCommonEvent((err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in clearing abort common event.`);
7. });
8. subscriber.finishCommonEvent((err: BusinessError) => {
9. if (err) {
10. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
11. return;
12. }
13. console.info(`Succeeded in finishing common event.`);
14. });
```

### clearAbortCommonEvent

PhonePC/2in1TabletTVWearable

clearAbortCommonEvent(): Promise<void>

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. subscriber.clearAbortCommonEvent().then(() => {
2. console.info(`Succeeded in clearing abort common event.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to clear abort common event. Code is ${err.code}, message is ${err.message}`);
5. });
6. subscriber.finishCommonEvent().then(() => {
7. console.info(`Succeeded in finishing common event.`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
10. });
```

### clearAbortCommonEventSync10+

PhonePC/2in1TabletTVWearable

clearAbortCommonEventSync(): void

清理有序公共事件的中止状态。当该接口与[finishCommonEvent](js-apis-inner-commonevent-commoneventsubscriber.md#finishcommonevent9)配合使用时，可以使该公共事件继续向下一个订阅者传递。

**系统能力：** SystemCapability.Notification.CommonEvent

**示例：**

```
1. subscriber.clearAbortCommonEventSync();
2. subscriber.finishCommonEvent().then(() => {
3. console.info(`Succeeded in finishing common event.`);
4. }).catch((err: BusinessError) => {
5. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
6. });
```

### getAbortCommonEvent

PhonePC/2in1TabletTVWearable

getAbortCommonEvent(callback: AsyncCallback<boolean>): void

获取当前有序公共事件是否处于中止状态。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.getAbortCommonEvent((err: BusinessError, abortEvent: boolean) => {
2. if (err) {
3. console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
7. });
```

### getAbortCommonEvent

PhonePC/2in1TabletTVWearable

getAbortCommonEvent(): Promise<boolean>

获取当前有序公共事件是否处于中止状态。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |

**示例：**

```
1. subscriber.getAbortCommonEvent().then((abortEvent: boolean) => {
2. console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to get abort common event. Code is ${err.code}, message is ${err.message}`);
5. });
```

### getAbortCommonEventSync10+

PhonePC/2in1TabletTVWearable

getAbortCommonEventSync(): boolean

获取当前有序公共事件是否处于中止状态。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |

**示例：**

```
1. let abortEvent: boolean = subscriber.getAbortCommonEventSync();
2. console.info(`Succeeded in getting abort common event, abortEvent is ${JSON.stringify(abortEvent)}`);
```

### getSubscribeInfo

PhonePC/2in1TabletTVWearable

getSubscribeInfo(callback: AsyncCallback<CommonEventSubscribeInfo>): void

获取订阅者的订阅信息。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md)> | 是 | 回调函数。返回订阅者的订阅信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.getSubscribeInfo((err: BusinessError, subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
2. if (err) {
3. console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
7. });
```

### getSubscribeInfo

PhonePC/2in1TabletTVWearable

getSubscribeInfo(): Promise<CommonEventSubscribeInfo>

获取订阅者的订阅信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md)> | Promise对象。返回订阅者的订阅信息。 |

**示例：**

```
1. subscriber.getSubscribeInfo().then((subscribeInfo: commonEventManager.CommonEventSubscribeInfo) => {
2. console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo)}`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to get subscribe info. Code is ${err.code}, message is ${err.message}`);
5. });
```

### getSubscribeInfoSync10+

PhonePC/2in1TabletTVWearable

getSubscribeInfoSync(): CommonEventSubscribeInfo

获取订阅者的订阅信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CommonEventSubscribeInfo](js-apis-inner-commonevent-commoneventsubscribeinfo.md) | 表示订阅者的订阅信息。 |

**示例：**

```
1. let subscribeInfo1: commonEventManager.CommonEventSubscribeInfo = subscriber.getSubscribeInfoSync();
2. console.info(`Succeeded in getting subscribe info, subscribe info is ${JSON.stringify(subscribeInfo1)}`);
```

### finishCommonEvent9+

PhonePC/2in1TabletTVWearable

finishCommonEvent(callback: AsyncCallback<void>): void

用于订阅者结束对当前有序公共事件的处理。使用callback异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当订阅者结束当前有序公共事件成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |

**示例：**

```
1. subscriber.finishCommonEvent((err: BusinessError) => {
2. if (err) {
3. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
4. return;
5. }
6. console.info(`Succeeded in finishing common event.`);
7. });
```

### finishCommonEvent9+

PhonePC/2in1TabletTVWearable

finishCommonEvent(): Promise<void>

用于订阅者结束对当前有序公共事件的处理。使用Promise异步回调。

**系统能力：** SystemCapability.Notification.CommonEvent

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. subscriber.finishCommonEvent().then(() => {
2. console.info(`Succeeded in finishing common event.`);
3. }).catch((err: BusinessError) => {
4. console.error(`Failed to finish common event. Code is ${err.code}, message is ${err.message}`);
5. });
```
