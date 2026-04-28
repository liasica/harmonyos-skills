---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub
title: EventHub
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > EventHub
category: harmonyos-references
scraped_at: 2026-04-28T07:58:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d6303574ff3205ebb0680810602adf0c299169610f5dc92653f56ded8e9c2129
---

EventHub是系统提供的基于发布-订阅模式实现的事件通信机制。通过事件名，实现了发送方和订阅方之间的解耦，支持不同业务模块间的高效数据传递和状态同步。

主要用于[UIAbility组件与UI的数据通信](../harmonyos-guides/uiability-data-sync-with-ui.md)。

不同的Context对象拥有不同的EventHub对象，不同EventHub对象之间无法直接通信。事件的订阅、取消订阅、触发都作用在某一个具体的EventHub对象上。

由于Worker、Taskpool通过Actor模型实现[多线程并发](../harmonyos-guides/multi-thread-concurrency-overview.md#多线程并发模型)，不同虚拟机实例之间拥有独占的内存，因此EventHub对象不能用于线程间的数据通信。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 约束限制

PhonePC/2in1TabletTVWearable

* 不支持在进程间通过Eventhub对象进行数据通信。
* 不支持在Worker、TaskPool线程间通过EventHub对象进行数据通信。如需进行跨线程通信，参考[使用Emitter进行线程间通信](../harmonyos-guides/itc-with-emitter.md)。
* 不支持同一线程内不同Context对象的EventHub对象间进行数据通信。
* 通过[sendableContextManager](js-apis-app-ability-sendablecontextmanager.md)转换后的Context对象与原先的Context对象属于不同Context对象，不支持其EventHub对象间的数据通信。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

开发者需要通过Context对象获取EventHub。以下示例通过UIAbility实例的Context对象获取其EventHub对象。

```
1. import { common, UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. eventFunc() {
5. console.info('eventFunc is called');
6. }

8. onCreate() {
9. // 调用方式一（推荐）
10. this.context.eventHub.on('myEvent', this.eventFunc);

12. // 调用方式二
13. let eventhub = this.context.eventHub as common.EventHub;
14. eventhub.on('myEvent', this.eventFunc);
15. }
16. }
```

## EventHub.on

PhonePC/2in1TabletTVWearable

on(event: string, callback: Function): void;

订阅指定事件。

说明

callback被emit触发时，调用方是EventHub对象，如果要修改callback中this的指向，可以使用箭头函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件名称。 |
| callback | Function | 是 | 事件回调，事件触发后调用。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例1：**

callback被emit触发时，调用方是EventHub对象。EventHub对象没有value属性，因此结果是undefined。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. value: number = 12;

7. onCreate() {
8. try {
9. this.context.eventHub.on('myEvent', this.eventFunc);
10. } catch (e) {
11. let code: number = (e as BusinessError).code;
12. let msg: string = (e as BusinessError).message;
13. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
14. }
15. }

17. onForeground() {
18. try {
19. // 结果：
20. // eventFunc is called, value: undefined
21. this.context.eventHub.emit('myEvent');
22. } catch (e) {
23. let code: number = (e as BusinessError).code;
24. let msg: string = (e as BusinessError).message;
25. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
26. }
27. }

29. eventFunc() {
30. console.info(`eventFunc is called, value: ${this.value}`);
31. }
32. }
```

**示例2：**

callback使用箭头函数时，调用方是EntryAbility对象。EntryAbility对象里存在value属性，因此结果是12。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. value: number = 12;

7. onCreate() {
8. try {
9. // 支持使用匿名函数订阅事件
10. this.context.eventHub.on('myEvent', () => {
11. console.info(`anonymous eventFunc is called, value: ${this.value}`);
12. });
13. } catch (e) {
14. let code: number = (e as BusinessError).code;
15. let msg: string = (e as BusinessError).message;
16. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
17. }
18. }

20. onForeground() {
21. try {
22. // 结果：
23. // anonymous eventFunc is called, value: 12
24. this.context.eventHub.emit('myEvent');
25. } catch (e) {
26. let code: number = (e as BusinessError).code;
27. let msg: string = (e as BusinessError).message;
28. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
29. }
30. }

32. eventFunc() {
33. console.info(`eventFunc is called, value: ${this.value}`);
34. }
35. }
```

## EventHub.off

PhonePC/2in1TabletTVWearable

off(event: string, callback?: Function): void;

取消订阅指定事件。

* 传入callback：取消指定的callback对指定事件的订阅，当该事件触发后，将不会回调该callback。
* 不传callback：取消所有callback对指定事件的订阅。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件名称。 |
| callback | Function | 否 | 事件回调。如果不传callback，则取消订阅该事件下所有callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate() {
6. try {
7. this.context.eventHub.on('myEvent', this.eventFunc1);
8. this.context.eventHub.off('myEvent', this.eventFunc1); // 取消eventFunc1对myEvent事件的订阅
9. this.context.eventHub.on('myEvent', this.eventFunc1);
10. this.context.eventHub.on('myEvent', this.eventFunc2);
11. this.context.eventHub.off('myEvent'); // 取消eventFunc1和eventFunc2对myEvent事件的订阅
12. } catch (e) {
13. let code: number = (e as BusinessError).code;
14. let msg: string = (e as BusinessError).message;
15. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
16. }
17. }

19. eventFunc1() {
20. console.info('eventFunc1 is called');
21. }

23. eventFunc2() {
24. console.info('eventFunc2 is called');
25. }
26. }
```

## EventHub.emit

PhonePC/2in1TabletTVWearable

emit(event: string, ...args: Object[]): void;

触发指定事件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 事件名称。 |
| ...args | Object[] | 否 | 可变参数，事件触发时，传递给回调函数的参数。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate() {
6. this.context.eventHub.on('myEvent', this.eventFunc);
7. }

9. onDestroy() {
10. try {
11. // 结果：
12. // eventFunc is called,undefined,undefined
13. this.context.eventHub.emit('myEvent');
14. // 结果：
15. // eventFunc is called,1,undefined
16. this.context.eventHub.emit('myEvent', 1);
17. // 结果：
18. // eventFunc is called,1,2
19. this.context.eventHub.emit('myEvent', 1, 2);
20. } catch (e) {
21. let code: number = (e as BusinessError).code;
22. let msg: string = (e as BusinessError).message;
23. console.error(`EventHub emit error, code: ${code}, msg: ${msg}`);
24. }
25. }

27. eventFunc(argOne: number, argTwo: number) {
28. console.info(`eventFunc is called, ${argOne}, ${argTwo}`);
29. }
30. }
```
