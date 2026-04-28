---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks
title: ArkTSUtils.locks
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.utils (ArkTS工具库) > ArkTSUtils.locks
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-03-30
content_hash: sha256:6642933f55bce2fbf92e2a474689f2c2617a3567c6467c3e7ab4587c794bdb8f
---

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了异步锁能力。为了开发者的开发效率，AsyncLock对象支持跨并发实例引用传递。

由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此我们在ArkTS中仅支持异步锁（非阻塞式锁）。

使用异步锁的方法需要标记为async，调用方需要await修饰调用，才能保证时序正确。因此会导致外层调用函数全部标记成async。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ArkTSUtils } from '@kit.ArkTS'
```

## AsyncLockCallback

PhonePC/2in1TabletTVWearable

type AsyncLockCallback<T> = () => T | Promise<T>

这是一个补充类型别名，表示[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)函数所有重载中的回调。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

## AsyncLock

PhonePC/2in1TabletTVWearable

实现异步锁功能的类，允许在锁下执行异步操作。该类使用[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md)装饰。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 否 | 锁的名称。 |

**示例：**

```
1. // 示例一：
2. @Sendable
3. class A {
4. count_: number = 0;
5. async getCount(): Promise<number> {
6. let lock: ArkTSUtils.locks.AsyncLock = ArkTSUtils.locks.AsyncLock.request("lock_1");
7. return lock.lockAsync(() => {
8. return this.count_;
9. })
10. }
11. async setCount(count: number) {
12. let lock: ArkTSUtils.locks.AsyncLock = ArkTSUtils.locks.AsyncLock.request("lock_1");
13. await lock.lockAsync(() => {
14. this.count_ = count;
15. })
16. }
17. }

19. // 示例二：
20. @Sendable
21. class A {
22. count_: number = 0;
23. lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
24. async getCount(): Promise<number> {
25. return this.lock_.lockAsync(() => {
26. return this.count_;
27. })
28. }
29. async setCount(count: number) {
30. await this.lock_.lockAsync(() => {
31. this.count_ = count;
32. })
33. }
34. }

36. @Concurrent
37. async function foo(a: A) {
38. await a.setCount(10)
39. }
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

默认构造函数。创建一个异步锁。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let lock = new ArkTSUtils.locks.AsyncLock();
```

### request

PhonePC/2in1TabletTVWearable

static request(name: string): AsyncLock

使用指定的名称查找或创建（如果未找到）异步锁实例。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 按指定名称查找或创建异步锁实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AsyncLock](arkts-apis-arkts-utils-locks.md#asynclock) | 返回查找到或创建后的异步锁实例。 |

**示例：**

```
1. let lockName = 'isAvailableLock';
2. let lock = ArkTSUtils.locks.AsyncLock.request(lockName);
```

### query

PhonePC/2in1TabletTVWearable

static query(name: string): AsyncLockState

查询指定异步锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要查询的锁的名称，仅可查询通过[request接口](arkts-apis-arkts-utils-locks.md#request)获取的锁（即与[request接口](arkts-apis-arkts-utils-locks.md#request)入参锁名称保持一致）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AsyncLockState](arkts-apis-arkts-utils-locks.md#asynclockstate) | 包含状态描述的异步锁状态实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200030 | The lock does not exist. |

**示例：**

```
1. // 查询已存在的锁信息
2. let lock = ArkTSUtils.locks.AsyncLock.request("queryTestLock");
3. let state = ArkTSUtils.locks.AsyncLock.query('queryTestLock');
4. let pending: ArkTSUtils.locks.AsyncLockInfo[] = state.pending;
5. let held: ArkTSUtils.locks.AsyncLockInfo[] = state.held;
6. // 输出当前处于pending状态的锁数量
7. console.info(`Number of pending locks: ${pending.length}`);
8. // 输出当前处于held状态的锁数量
9. console.info(`Number of held locks: ${held.length}`);

11. // 查询不存在的锁信息，会抛出错误信息：The lock does not exist.
12. try {
13. let state1 = ArkTSUtils.locks.AsyncLock.query('queryTestLock1');
14. } catch (e) {
15. console.error(`Error is: ${e}`);
16. }
```

### queryAll

PhonePC/2in1TabletTVWearable

static queryAll(): AsyncLockState[]

查询所有现有锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AsyncLockState](arkts-apis-arkts-utils-locks.md#asynclockstate)[] | 包含锁状态信息的异步锁状态数组。 |

**示例：**

```
1. // 查询已存在的锁信息
2. let lock1 = ArkTSUtils.locks.AsyncLock.request("queryTestLock1");
3. let lock2 = ArkTSUtils.locks.AsyncLock.request("queryTestLock2");
4. let states: ArkTSUtils.locks.AsyncLockState[] = ArkTSUtils.locks.AsyncLock.queryAll();
5. // 输出当前存在的锁数量
6. console.info("The states size is " + states.length);
```

### lockAsync

PhonePC/2in1TabletTVWearable

lockAsync<T>(callback: AsyncLockCallback<T>): Promise<T>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)的同一线程中以异步方式执行。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback<T>](arkts-apis-arkts-utils-locks.md#asynclockcallback) | 是 | 获取锁后要调用的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | 回调执行后将解决的Promise。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200030 | The lock does not exist. |

**示例：**

```
1. let lock = new ArkTSUtils.locks.AsyncLock();
2. let p1 = lock.lockAsync<void>(() => {
3. // 执行某些操作
4. });
```

### lockAsync

PhonePC/2in1TabletTVWearable

lockAsync<T>(callback: AsyncLockCallback<T>, mode: AsyncLockMode): Promise<T>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)的同一线程中以异步方式执行。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback<T>](arkts-apis-arkts-utils-locks.md#asynclockcallback) | 是 | 获取锁后要调用的函数。 |
| mode | [AsyncLockMode](arkts-apis-arkts-utils-locks.md#asynclockmode) | 是 | 锁的操作模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | 回调执行后将解决的Promise。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200030 | The lock does not exist. |

**示例：**

```
1. let lock = new ArkTSUtils.locks.AsyncLock();
2. let p1 = lock.lockAsync<void>(() => {
3. // 执行某些操作
4. }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE);
```

### lockAsync

PhonePC/2in1TabletTVWearable

lockAsync<T, U>(callback: AsyncLockCallback<T>, mode: AsyncLockMode, options: AsyncLockOptions<U>): Promise<T | U>

在获取的锁下执行操作。该方法首先获取锁，然后调用回调，最后释放锁。回调在调用[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)的同一线程中以异步方式执行。在[AsyncLockOptions](arkts-apis-arkts-utils-locks.md#asynclockoptions)中可以提供一个可选的超时值。在这种情况下，如果超时前未能获取锁，lockAsync将返回被拒绝的Promise并带上一个BusinessError实例。这种情况下，错误信息将包含持有的锁和等待的锁的信息以及可能的死锁警告。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncLockCallback<T>](arkts-apis-arkts-utils-locks.md#asynclockcallback) | 是 | 获取锁后要调用的函数。 |
| mode | [AsyncLockMode](arkts-apis-arkts-utils-locks.md#asynclockmode) | 是 | 锁的操作模式。 |
| options | [AsyncLockOptions<U>](arkts-apis-arkts-utils-locks.md#asynclockoptions) | 是 | 锁的操作选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T | U> | 回调执行后解决的Promise，或者在超时情况下被拒绝。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200030 | The lock does not exist. |
| 10200031 | Timeout exceeded. |

**示例：**

```
1. let lock = new ArkTSUtils.locks.AsyncLock();
2. let options = new ArkTSUtils.locks.AsyncLockOptions<void>();
3. options.timeout = 1000;
4. let p: Promise<void> = lock.lockAsync<void, void>(
5. () => {
6. // 执行某些操作
7. },
8. ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE,
9. options
10. );
```

## AsyncLockMode

PhonePC/2in1TabletTVWearable

锁操作对应的模式枚举。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHARED | 1 | 共享锁模式。如果指定了此模式，允许​​多个线程或并发任务同时获取锁并执行操作。多用于读操作、无数据竞争的并行任务。 |
| EXCLUSIVE | 2 | 独占锁模式。如果指定了此模式，仅允许持有锁的任务执行。 它与任何其他锁均不兼容​​，包括其他独占锁和共享锁。多用于写操作、数据更新、状态修改等可能产生竞争的场景。 |

**示例：**

```
1. let lock = new ArkTSUtils.locks.AsyncLock();
2. // shared0可获取锁并开始执行
3. lock.lockAsync(async () => {
4. console.info('shared0');
5. await new Promise<void>((resolve) => setTimeout(resolve, 1000));
6. }, ArkTSUtils.locks.AsyncLockMode.SHARED);
7. // shared1可获取锁并开始执行，无需等待shared0
8. lock.lockAsync(async () => {
9. console.info('shared1');
10. await new Promise<void>((resolve) => setTimeout(resolve, 1000));
11. }, ArkTSUtils.locks.AsyncLockMode.SHARED);
12. // exclusive0需等待shared0、1执行完后才可获取锁并执行
13. lock.lockAsync(async () => {
14. console.info('exclusive0');
15. await new Promise<void>((resolve) => setTimeout(resolve, 1000));
16. }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE);
17. // shared2需等待exclusive0执行完后才可获取锁并执行
18. lock.lockAsync(async () => {
19. console.info('shared2');
20. await new Promise<void>((resolve) => setTimeout(resolve, 1000));
21. }, ArkTSUtils.locks.AsyncLockMode.SHARED);
22. // shared3需等待exclusive0执行完后才可获取锁并执行，无需等待shared2
23. lock.lockAsync(async () => {
24. console.info('shared3');
25. await new Promise<void>((resolve) => setTimeout(resolve, 1000));
26. }, ArkTSUtils.locks.AsyncLockMode.SHARED);
```

## AsyncLockOptions

PhonePC/2in1TabletTVWearable

class AsyncLockOptions<T>

表示锁操作选项的类。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### constructor

PhonePC/2in1TabletTVWearable

constructor()

默认构造函数。创建一个所有属性均具有默认值的异步锁配置项实例。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let s: ArkTSUtils.locks.AbortSignal<string> = { aborted: false, reason: 'Aborted' };
2. let options = new ArkTSUtils.locks.AsyncLockOptions<string>();
3. options.isAvailable = false;
4. options.signal = s;
5. let lock = new ArkTSUtils.locks.AsyncLock();
6. let p = lock.lockAsync<void, string>(
7. () => {
8. // 执行某些操作
9. },
10. ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE,
11. options,
12. );
```

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isAvailable | boolean | 否 | 否 | 当前锁是否可用。取值为true，则只有在尚未持有锁定请求时才会授予该锁定请求；为false则表示将等待当前锁被释放。默认为 false。 |
| signal | [AbortSignal<T>](arkts-apis-arkts-utils-locks.md#abortsignal)|null | 否 | 否 | 用于终止异步操作的对象。当signal.aborted为true时，锁请求将被丢弃；当signal.aborted为false时，请求会继续等待获取锁；当signal为null时，请求正常排队运行。默认为 null。 |
| timeout | number | 否 | 否 | 锁的超时时间，单位为毫秒。若该值大于零，且操作运行时间超过该时间，[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)将返回被拒绝的Promise。默认为 0。 |

## AsyncLockState

PhonePC/2in1TabletTVWearable

用于存储异步锁实例上当前执行的所有锁操作的信息的类。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| held | [AsyncLockInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks#asynclockinfo) | 否 | 否 | 持有的锁信息。 |
| pending | [AsyncLockInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks#asynclockinfo) | 否 | 否 | 等待中的锁信息。 |

## AsyncLockInfo

PhonePC/2in1TabletTVWearable

关于锁的信息。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 锁的名称。 |
| mode | [AsyncLockMode](arkts-apis-arkts-utils-locks.md#asynclockmode) | 否 | 否 | 锁的模式。 |
| contextId | number | 否 | 否 | [AsyncLockMode](arkts-apis-arkts-utils-locks.md#asynclockmode)调用者的执行上下文标识符。 |

## AbortSignal

PhonePC/2in1TabletTVWearable

用于终止异步操作的对象。该类的实例必须在其创建的同一线程中访问。从其他线程访问此类的字段会导致未定义的行为。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| aborted | boolean | 否 | 否 | 是否终止异步操作。为true时表示终止异步操作，为false时表示异步操作未被终止。 |
| reason | T | 否 | 否 | 终止的原因。此值将用于拒绝[lockAsync](arkts-apis-arkts-utils-locks.md#lockasync)返回的Promise。 |

## ConditionVariable18+

PhonePC/2in1TabletTVWearable

实现异步等待功能的类，支持异步等待通知操作。该类使用[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md)装饰。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

### constructor18+

PhonePC/2in1TabletTVWearable

constructor()

默认构造函数。创建一个异步等待通知操作的对象。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let conditionVariable = new ArkTSUtils.locks.ConditionVariable();
```

### request18+

PhonePC/2in1TabletTVWearable

static request(name: string): ConditionVariable

使用指定的名称查找或创建（如果未找到）异步等待通知操作的对象。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 按指定名称查找或创建等待通知操作的对象名称，字符串无特别限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ConditionVariable](arkts-apis-arkts-utils-locks.md#conditionvariable18) | 返回查找到或创建后的异步等待通知操作的实例。 |

**示例：**

```
1. let conditionVariable = ArkTSUtils.locks.ConditionVariable.request("conditionName");
```

### wait18+

PhonePC/2in1TabletTVWearable

wait(): Promise<void>

异步调用进入等待中，将在被唤醒后继续执行。使用Promise异步回调。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
2. conditionVariable.wait().then(() => {
3. console.info(`Thread being awakened, then continue...`); // 被唤醒后输出日志
4. });
```

### waitFor18+

PhonePC/2in1TabletTVWearable

waitFor(timeout : number) : Promise<void>

异步调用进入等待中, 将在被唤醒或者等待时间结束后继续执行。使用Promise异步回调。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 是 | 等待时间，单位为ms，正整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
2. conditionVariable.waitFor(3000).then(() => {
3. console.info(`Thread being awakened, then continue...`); // 被唤醒后输出日志
4. });
```

### notifyAll18+

PhonePC/2in1TabletTVWearable

notifyAll() : void

通知所有等待的线程。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
2. conditionVariable.waitFor(3000).then(() => {
3. console.info(`Thread being awakened, then continue...`); // 被唤醒后输出日志
4. });
5. // 通知所有等待的线程。
6. conditionVariable.notifyAll();
```

### notifyOne18+

PhonePC/2in1TabletTVWearable

notifyOne() : void

通知第一个等待的线程。

**元服务API**：从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
2. conditionVariable.waitFor(3000).then(() => {
3. console.info(`Thread a being awakened, then continue...`); // 被唤醒后输出日志
4. });
5. // 通知第一个等待的线程。
6. conditionVariable.notifyOne();
```
