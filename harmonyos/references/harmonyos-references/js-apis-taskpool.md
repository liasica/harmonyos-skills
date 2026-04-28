---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool
title: @ohos.taskpool (启动任务池)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.taskpool (启动任务池)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:03+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:5600c76957e923572fafae3eec7553c76430117447c55c028c1628139b0ff3a1
---

任务池（taskpool）的作用是为应用程序提供多线程运行环境，降低资源消耗并提升系统性能，且您无需关心线程的生命周期。您可以使用任务池API创建后台任务（Task），并进行如执行任务或取消任务等操作。理论上，任务池API允许创建的任务数量不受限制，但由于内存限制，不建议这样做。此外，不建议在任务中执行阻塞操作，尤其是无限期阻塞操作，因为长时间的阻塞操作会占用工作线程，可能阻塞其他任务的调度，影响应用性能。

创建同一优先级的任务时，可以自行决定其执行顺序。任务的实际执行顺序与调用任务池API提供的任务执行接口的顺序一致。任务的默认优先级为MEDIUM。

当同一时间待执行的任务数量大于任务池工作线程数量，任务池会根据负载均衡机制进行扩容，增加工作线程数量，减少整体等待时长。同样，当执行的任务数量减少，工作线程数量大于执行任务数量，部分工作线程处于空闲状态，任务池会根据负载均衡机制进行缩容，减少工作线程数量。

任务池API返回错误码。如需了解各错误码的详细信息，请参阅文档[语言基础类库错误码](errorcode-utils.md)。

请查阅[TaskPool注意事项](../harmonyos-guides/taskpool-introduction.md#taskpool注意事项)，了解使用TaskPool时的相关注意点。

文档中涉及以下任务概念：

* 任务组任务：对应为[TaskGroup](js-apis-taskpool.md#taskgroup10)任务。
* 串行队列任务：对应为[SequenceRunner](js-apis-taskpool.md#sequencerunner-11)任务。
* 异步队列任务：对应为[AsyncRunner](js-apis-taskpool.md#asyncrunner18)任务。
* 周期任务：由[executePeriodically](js-apis-taskpool.md#taskpoolexecuteperiodically12)执行的任务。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { taskpool } from '@kit.ArkTS';
```

## taskpool.execute

PhonePC/2in1TabletTVWearable

execute(func: Function, ...args: Object[]): Promise<Object>

将待执行的函数放入taskpool的内部任务队列，函数不会立即执行，而是等待分发到工作线程执行。在当前执行模式下，不支持取消任务。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | Function | 是 | 执行的逻辑需要传入一个函数，该函数必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰。支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | Object[] | 否 | 执行逻辑的函数所需要的入参，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. taskpool.execute(printArgs, 100).then((value: Object) => { // 100: test number
8. console.info("taskpool result: " + value);
9. });
```

## taskpool.execute13+

PhonePC/2in1TabletTVWearable

execute<A extends Array<Object>, R>(func: (...args: A) => R | Promise<R>, ...args: A): Promise<R>

校验并发函数的参数类型和返回类型后，将函数添加到taskpool的任务队列。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | (...args: A) => R | Promise<R> | 是 | 执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | A | 否 | 执行逻辑的函数所需要的入参，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<R> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. @Concurrent
8. function testWithThreeParams(a: number, b: string, c: number): string {
9. return b;
10. }

12. @Concurrent
13. function testWithArray(args: [number, string]): string {
14. return "success";
15. }

17. taskpool.execute<[number], number>(printArgs, 100).then((value: number) => { // 100: test number
18. console.info("taskpool result: " + value); // "taskpool result: 100"
19. });

21. taskpool.execute<[number, string, number], string>(testWithThreeParams, 100, "test", 100).then((value: string) => {
22. console.info("taskpool result: " + value); // "taskpool result: test"
23. });

25. taskpool.execute<[[number, string]], string>(testWithArray, [100, "test"]).then((value: string) => {
26. console.info("taskpool result: " + value); // "taskpool result: success"
27. });
```

## taskpool.execute

PhonePC/2in1TabletTVWearable

execute(task: Task, priority?: Priority): Promise<Object>

将创建好的任务添加到taskpool的内部任务队列中，任务不会立即执行，而是等待分发到工作线程执行。当前模式支持设置任务优先级和通过cancel取消任务。任务不能是任务组任务、串行队列任务或异步队列任务。长时任务只能调用一次，非长时任务可以多次调用执行。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要在任务池中执行的任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 该参数表示等待执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
8. let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
9. let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
10. taskpool.execute(task1, taskpool.Priority.LOW).then((value: Object) => {
11. console.info("taskpool result1: " + value);
12. });
13. taskpool.execute(task2, taskpool.Priority.MEDIUM).then((value: Object) => {
14. console.info("taskpool result2: " + value);
15. });
16. taskpool.execute(task3, taskpool.Priority.HIGH).then((value: Object) => {
17. console.info("taskpool result3: " + value);
18. });
```

## taskpool.execute13+

PhonePC/2in1TabletTVWearable

execute<A extends Array<Object>, R>(task: GenericsTask<A, R>, priority?: Priority): Promise<R>

将创建好的泛型任务放入taskpool的内部任务队列，校验任务的参数类型和返回值类型。使用Promise异步回调。

execute任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [GenericsTask<A, R>](js-apis-taskpool.md#genericstask13) | 是 | 需要在任务池中执行的泛型任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 等待执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<R> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let task1: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 100); // 100: test number
8. let task2: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 200); // 200: test number
9. let task3: taskpool.Task = new taskpool.GenericsTask<[number], number>(printArgs, 300); // 300: test number
10. taskpool.execute<[number], number>(task1, taskpool.Priority.LOW).then((value: number) => {
11. console.info("taskpool result1: " + value);
12. });
13. taskpool.execute<[number], number>(task2, taskpool.Priority.MEDIUM).then((value: number) => {
14. console.info("taskpool result2: " + value);
15. });
16. taskpool.execute<[number], number>(task3, taskpool.Priority.HIGH).then((value: number) => {
17. console.info("taskpool result3: " + value);
18. });
```

## taskpool.execute10+

PhonePC/2in1TabletTVWearable

execute(group: TaskGroup, priority?: Priority): Promise<Object[]>

将创建好的任务组放入taskpool内部任务队列，任务组中的任务不会立即执行，而是等待分发到工作线程执行。任务组中任务全部执行完成后，结果数组统一返回。此模式适用于执行关联任务。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group | [TaskGroup](js-apis-taskpool.md#taskgroup10) | 是 | 需要在任务池中执行的任务组。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 等待执行的任务组的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object[]> | Promise对象数组，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
8. taskGroup1.addTask(printArgs, 10); // 10: test number
9. taskGroup1.addTask(printArgs, 20); // 20: test number
10. taskGroup1.addTask(printArgs, 30); // 30: test number

12. let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
13. let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
14. let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
15. let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
16. taskGroup2.addTask(task1);
17. taskGroup2.addTask(task2);
18. taskGroup2.addTask(task3);
19. taskpool.execute(taskGroup1).then((res: Array<Object>) => {
20. console.info("Succeeded in excuting task, res is:" + res);
21. });
22. taskpool.execute(taskGroup2).then((res: Array<Object>) => {
23. console.info("Succeeded in excuting task, res is:" + res);
24. });
```

## taskpool.executeDelayed11+

PhonePC/2in1TabletTVWearable

executeDelayed(delayTime: number, task: Task, priority?: Priority): Promise<Object>

延时执行任务。当前执行模式可以设置任务优先级，并且可以尝试调用cancel取消任务。该任务不能是任务组任务、串行队列任务、异步队列任务或周期任务。如果任务不是长时任务，可以多次调用executeDelayed执行；如果是长时任务，则仅支持执行一次。使用Promise异步回调。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delayTime | number | 是 | 延时时间。单位为ms。delayTime值必须要大于等于0。 |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要延时执行的任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 延时执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |
| 10200028 | The delayTime is less than zero. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. // import BusinessError
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Concurrent
5. function printArgs(args: number): void {
6. console.info("printArgs: " + args);
7. }

9. let t: number = Date.now();
10. console.info("taskpool start time is: " + t);
11. let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
12. taskpool.executeDelayed(1000, task).then(() => { // 1000: delayTime is 1000ms
13. console.info('Succeeded in executing task');
14. }).catch((e: BusinessError) => {
15. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
16. })
```

## taskpool.executeDelayed13+

PhonePC/2in1TabletTVWearable

executeDelayed<A extends Array<Object>, R>(delayTime: number, task: GenericsTask<A, R>, priority?: Priority): Promise<R>

延时执行泛型任务，不校验任务的参数类型和返回值类型。使用Promise异步回调。

executeDelayed任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| delayTime | number | 是 | 延时时间。单位为ms。delayTime值必须要大于等于0。 |
| task | [GenericsTask<A, R>](js-apis-taskpool.md#genericstask13) | 是 | 需要延时执行的泛型任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 延时执行的任务的优先级，默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<R> | Promise对象，返回任务函数的执行结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200028 | The delayTime is less than zero. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. // import BusinessError
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Concurrent
5. function printArgs(args: number): string {
6. console.info("printArgs: " + args);
7. return "success";
8. }

10. let task: taskpool.Task = new taskpool.GenericsTask<[number], string>(printArgs, 100); // 100: test number
11. taskpool.executeDelayed<[number], string>(1000, task).then((res: string) => { // 1000: delayTime is 1000ms
12. console.info('Succeeded in executing task');
13. }).catch((e: BusinessError) => {
14. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
15. })
```

## taskpool.executePeriodically12+

PhonePC/2in1TabletTVWearable

executePeriodically(period: number, task: Task, priority?: Priority): void

周期任务每隔period时长执行一次。当前执行模式支持设置任务优先级，并可以通过调用cancel取消周期任务的执行。周期任务不能是任务组任务、串行队列任务或异步队列任务，不能再次调用执行接口，且执行的任务不能拥有依赖关系。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| period | number | 是 | 周期时长。单位为ms。period值必须要大于等于0。 |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要周期执行的任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 周期执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**错误码：**

以下错误码的详细介绍，请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |
| 10200028 | The period is less than zero. |
| 10200050 | The concurrent task has been executed and cannot be executed periodically. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): void {
3. console.info("printArgs: " + args);
4. }

6. @Concurrent
7. function testExecutePeriodically(args: number): void {
8. let t = Date.now();
9. while ((Date.now() - t) < args) {
10. continue;
11. }
12. taskpool.Task.sendData(args); // 向宿主线程发送消息
13. }

15. function printResult(data: number): void {
16. console.info("taskpool: data is: " + data);
17. }

19. function taskpoolTest() {
20. try {
21. let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
22. taskpool.executePeriodically(1000, task); // 1000: period is 1000ms
23. } catch (e) {
24. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
25. }

27. try {
28. let periodicTask: taskpool.Task = new taskpool.Task(testExecutePeriodically, 200); // 200: test number
29. periodicTask.onReceiveData(printResult);
30. taskpool.executePeriodically(1000, periodicTask); // 1000: period is 1000ms
31. } catch (e) {
32. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
33. }
34. }

36. taskpoolTest();
```

## taskpool.executePeriodically13+

PhonePC/2in1TabletTVWearable

executePeriodically<A extends Array<Object>, R>(period: number, task: GenericsTask<A, R>, priority?: Priority): void

周期执行泛型任务，每隔period时长执行一次。不校验任务的参数类型和返回值类型。

executePeriodically任务的校验是结合new GenericsTask一起用的，参数、返回值类型需与new GenericsTask中的类型保持一致。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| period | number | 是 | 周期时长。单位为ms。period值必须要大于等于0。 |
| task | [GenericsTask<A, R>](js-apis-taskpool.md#genericstask13) | 是 | 需要周期执行的泛型任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 周期执行的任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200006 | An exception occurred during serialization. |
| 10200014 | The function is not marked as concurrent. |
| 10200028 | The period is less than zero. |
| 10200050 | The concurrent task has been executed and cannot be executed periodically. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): void {
3. console.info("printArgs: " + args);
4. }

6. @Concurrent
7. function testExecutePeriodically(args: number): void {
8. let t = Date.now();
9. while ((Date.now() - t) < args) {
10. continue;
11. }
12. taskpool.Task.sendData(args); // 向宿主线程发送消息
13. }

15. function printResult(data: number): void {
16. console.info("taskpool: data is: " + data);
17. }

19. function taskpoolTest() {
20. try {
21. let task: taskpool.Task = new taskpool.GenericsTask<[number], void>(printArgs, 100); // 100: test number
22. taskpool.executePeriodically<[number], void>(1000, task); // 1000: period is 1000ms
23. } catch (e) {
24. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
25. }

27. try {
28. let periodicTask: taskpool.Task = new taskpool.GenericsTask<[number], void>(testExecutePeriodically, 200); // 200: test number
29. periodicTask.onReceiveData(printResult);
30. taskpool.executePeriodically<[number], void>(1000, periodicTask); // 1000: period is 1000ms
31. } catch (e) {
32. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
33. }
34. }

36. taskpoolTest();
```

## taskpool.cancel

PhonePC/2in1TabletTVWearable

cancel(task: Task): void

取消任务池中的任务。当任务在taskpool等待队列中，取消该任务后该任务将不再执行，并返回任务被取消的异常；当任务已经在taskpool工作线程执行，取消该任务并不影响任务继续执行，执行结果在catch分支返回，搭配isCanceled使用可以对任务取消行为作出响应。taskpool.cancel对其之前的taskpool.execute、taskpool.executeDelayed或taskpool.executePeriodically生效。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](js-apis-taskpool.md#taskresult20)>的泛型标记，来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要取消执行的任务。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200015 | The task to cancel does not exist. |
| 10200055 | The asyncRunner task has been canceled. |

从API version 10开始，此接口调用时不再涉及上报错误码10200016。

**正在执行的任务取消示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Concurrent
4. function inspectStatus(arg: number): number {
5. // 第一次检查任务是否已经取消并作出响应
6. if (taskpool.Task.isCanceled()) {
7. console.info("task has been canceled before 2s sleep.");
8. return arg + 2;
9. }
10. // 2s sleep
11. let t: number = Date.now();
12. while (Date.now() - t < 2000) {
13. continue;
14. }
15. // 第二次检查任务是否已经取消并作出响应
16. if (taskpool.Task.isCanceled()) {
17. console.info("task has been canceled after 2s sleep.");
18. return arg + 3;
19. }
20. return arg + 1;
21. }

23. function concurrentFunc() {
24. let task1: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
25. let task2: taskpool.Task = new taskpool.Task(inspectStatus, 200); // 200: test number
26. let task3: taskpool.Task = new taskpool.Task(inspectStatus, 300); // 300: test number
27. let task4: taskpool.Task = new taskpool.Task(inspectStatus, 400); // 400: test number
28. let task5: taskpool.Task = new taskpool.Task(inspectStatus, 500); // 500: test number
29. let task6: taskpool.Task = new taskpool.Task(inspectStatus, 600); // 600: test number
30. taskpool.execute(task1).then((res: Object) => {
31. console.info(`Succeeded in excuting task. result: ` + res);
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to execute task. Code: ${err.code}, message: ${err.message}`);
34. });
35. taskpool.execute(task2);
36. taskpool.execute(task3);
37. taskpool.execute(task4);
38. taskpool.execute(task5);
39. taskpool.execute(task6);
40. // 1s后取消task
41. setTimeout(() => {
42. try {
43. taskpool.cancel(task1);
44. } catch (e) {
45. console.error(`Failed to cancel task. Code: ${e.code}, message: ${e.message}`);
46. }
47. }, 1000);
48. }

50. concurrentFunc();
```

## taskpool.cancel10+

PhonePC/2in1TabletTVWearable

cancel(group: TaskGroup): void

取消任务池中的任务组。如果任务组中的任务未全部执行结束，返回undefined作为任务组结果。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](js-apis-taskpool.md#taskresult20)>的泛型标记，来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group | [TaskGroup](js-apis-taskpool.md#taskgroup10) | 是 | 需要取消执行的任务组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200018 | The task group to cancel does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Concurrent
4. function printArgs(args: number): number {
5. let t: number = Date.now();
6. while (Date.now() - t < 2000) {
7. continue;
8. }
9. console.info("printArgs: " + args);
10. return args;
11. }

13. function concurrentFunc() {
14. let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
15. taskGroup1.addTask(printArgs, 10); // 10: test number
16. let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
17. taskGroup2.addTask(printArgs, 100); // 100: test number
18. taskpool.execute(taskGroup1).then((res: Array<Object>) => {
19. console.info(`Succeeded in excuting task. res is: ` + res);
20. });
21. taskpool.execute(taskGroup2).then((res: Array<Object>) => {
22. console.info(`Succeeded in excuting task. res is: ` + res);
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to excute task. Code: ${err.code}, message: ${err.message}`);
25. });
26. setTimeout(() => {
27. try {
28. taskpool.cancel(taskGroup2);
29. } catch (e) {
30. console.error(`Failed to cancel task. Code: ${e.code}, message: ${e.message}`);
31. }
32. }, 1000);
33. }

35. concurrentFunc();
```

## taskpool.cancel18+

PhonePC/2in1TabletTVWearable

cancel(taskId: number): void

通过任务ID取消任务池中的任务。如果任务在taskpool等待队列中，取消后任务将不再执行，并返回任务取消的异常。如果任务已在taskpool工作线程中执行，取消不影响任务继续执行，执行结果在catch分支返回。使用isCanceled可以对任务取消行为作出响应。taskpool.cancel对其之前的taskpool.execute或taskpool.executeDelayed生效。在其他线程调用taskpool.cancel时，需注意其行为是异步的，可能影响之后的taskpool.execute或taskpool.executeDelayed。

从API version 20开始，支持在执行cancel操作后，在catch分支里使用BusinessError<[taskpool.TaskResult](js-apis-taskpool.md#taskresult20)>的泛型标记。这可以用来获取任务中抛出的异常信息或最终的执行结果。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | number | 是 | 需要取消执行的任务的ID。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200015 | The task to cancel does not exist. |
| 10200055 | The asyncRunner task has been canceled. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Concurrent
4. function printArgs(args: number): number {
5. let t: number = Date.now();
6. while (Date.now() - t < 2000) {
7. continue;
8. }
9. if (taskpool.Task.isCanceled()) {
10. console.info("task has been canceled after 2s sleep.");
11. return args + 1;
12. }
13. console.info("printArgs: " + args);
14. return args;
15. }

17. @Concurrent
18. function cancelFunction(taskId: number) {
19. try {
20. taskpool.cancel(taskId);
21. } catch (e) {
22. console.error(`Failed to cancel task. Code: ${e.code}, message: ${e.message}`);
23. }
24. }

26. function concurrentFunc() {
27. let task = new taskpool.Task(printArgs, 100); // 100: test number
28. taskpool.execute(task).catch((err: BusinessError) => {
29. console.error(`Failed to excute task. Code: ${err.code}, message: ${err.message}`);
30. });
31. setTimeout(() => {
32. let cancelTask = new taskpool.Task(cancelFunction, task.taskId);
33. taskpool.execute(cancelTask);
34. }, 1000);
35. }

37. concurrentFunc();
```

## taskpool.terminateTask12+

PhonePC/2in1TabletTVWearable

terminateTask(longTask: LongTask): void

中止任务池中的长时任务，在长时任务执行完成后调用。中止后，执行长时任务的线程可能会被回收。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**： 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| longTask | [LongTask](js-apis-taskpool.md#longtask12) | 是 | 需要中止的长时任务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. @Concurrent
2. function longTask(arg: number): number {
3. let t: number = Date.now();
4. while (Date.now() - t < arg) {
5. continue;
6. }
7. console.info("longTask has been executed.");
8. return arg;
9. }

11. function concurrentFunc() {
12. let task1: taskpool.LongTask = new taskpool.LongTask(longTask, 1000); // 1000: sleep time
13. taskpool.execute(task1).then((res: Object) => {
14. taskpool.terminateTask(task1);
15. console.info("taskpool longTask result: " + res);
16. });
17. }

19. concurrentFunc();
```

## taskpool.isConcurrent12+

PhonePC/2in1TabletTVWearable

isConcurrent(func: Function): boolean

检查函数是否为并发函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**： 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | Function | 是 | 需要检查的函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果被检查函数标注了[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)，则返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. @Concurrent
2. function test() {}

4. let result: Boolean = taskpool.isConcurrent(test);
5. console.info("result is: " + result);
```

## taskpool.getTaskPoolInfo10+

PhonePC/2in1TabletTVWearable

getTaskPoolInfo(): TaskPoolInfo

获取任务池的线程信息和任务信息。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskPoolInfo](js-apis-taskpool.md#taskpoolinfo10) | 任务池的内部信息。 |

**示例：**

```
1. let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
```

## taskpool.getTask22+

PhonePC/2in1TabletTVWearable

getTask(taskId: number, taskName?: string): Task | undefined

通过taskId或taskId与taskName获取对应的Task实例。

说明

* 如果传入的taskId查询不到对应的Task实例，则会返回undefined；
* 如果传入的taskId能够查询到对应的Task实例，但是调用getTask方法的线程和创建Task实例的线程不一致，则会返回undefined；
* 如果传入了taskId和taskName，通过taskId查询到的Task实例的name和传入的taskName不一致，则会返回undefined。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskId | number | 是 | 任务ID。 |
| taskName | string | 否 | 任务名称。默认值为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Task](js-apis-taskpool.md#task) | undefined | 返回Task实例；当情况异常时，返回undefined，具体可见上文说明。 |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function addNum(num1: number, num2: number) {
5. return num1 + num2;
6. }

8. function checkTask() {
9. try {
10. taskpool.getTask(null);
11. } catch (e) {
12. console.error("error:" + e);
13. // error:BusinessError: Parameter error. The input parameters are invalid, the type of the first param must be number.
14. }

16. let task1:taskpool.Task = new taskpool.Task("addNum", addNum, 1, 2);
17. let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "addNum"); // task2 is not undefined
18. let task3:taskpool.Task | undefined = taskpool.getTask(task1.taskId, "add"); // task3 is undefined
19. let task4:taskpool.Task | undefined = taskpool.getTask(0); // task4 is undefined
20. }

22. function dealTask() {
23. let task1:taskpool.Task = new taskpool.Task(addNum, 1, 2);
24. let task2:taskpool.Task | undefined = taskpool.getTask(task1.taskId);
25. if (task2 === undefined) {
26. return;
27. }

29. taskpool.execute(task2).then((result) => {
30. console.info("task2 result: " + result); // task2 result: 3
31. })
32. }
```

## Priority

PhonePC/2in1TabletTVWearable

表示所创建任务（Task）执行时的优先级。工作线程优先级跟随任务优先级更新，对应关系参考[QoS等级定义](../harmonyos-guides/qos-guidelines.md#qos等级定义)。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH | 0 | 任务为高优先级。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MEDIUM | 1 | 任务为中优先级。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LOW | 2 | 任务为低优先级。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| IDLE12+ | 3 | 任务为后台任务。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. let t: number = Date.now();
4. while (Date.now() - t < 1000) { // 1000: delay 1s
5. continue;
6. }
7. console.info("printArgs: " + args);
8. return args;
9. }

11. let allCount = 100; // 100: test number
12. let taskArray: Array<taskpool.Task> = [];
13. // 创建400个任务并添加至taskArray
14. for (let i: number = 0; i < allCount; i++) {
15. let task1: taskpool.Task = new taskpool.Task(printArgs, i);
16. taskArray.push(task1);
17. let task2: taskpool.Task = new taskpool.Task(printArgs, i * 10); // 10: test number
18. taskArray.push(task2);
19. let task3: taskpool.Task = new taskpool.Task(printArgs, i * 100); // 100: test number
20. taskArray.push(task3);
21. let task4: taskpool.Task = new taskpool.Task(printArgs, i * 1000); // 1000: test number
22. taskArray.push(task4);
23. }

25. // 从taskArray中获取不同的任务并给定不同优先级执行
26. for (let i: number = 0; i < taskArray.length; i+=4) { // 4: 每次执行4个任务，循环取任务时需后移4项，确保执行的是不同的任务
27. taskpool.execute(taskArray[i], taskpool.Priority.HIGH);
28. taskpool.execute(taskArray[i + 1], taskpool.Priority.LOW);
29. taskpool.execute(taskArray[i + 2], taskpool.Priority.MEDIUM);
30. taskpool.execute(taskArray[i + 3], taskpool.Priority.IDLE);
31. }
```

## Task

PhonePC/2in1TabletTVWearable

调用Task中的任何接口前必须先使用构造函数创建Task对象。任务可以多次执行，也可以放入任务组、串行队列或异步队列执行，还支持添加依赖关系。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| function | Function | 否 | 否 | 创建任务时需要传入的函数，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| arguments | Object[] | 否 | 是 | 创建任务传入函数所需的参数，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name11+ | string | 否 | 否 | 创建任务时指定的任务名称。不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| taskId18+ | number | 否 | 否 | 任务的ID。任务的标识符，系统默认提供全局唯一值，不建议修改此值。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| totalDuration11+ | number | 否 | 否 | 执行任务总耗时。单位为ms。不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ioDuration11+ | number | 否 | 否 | 执行任务异步IO耗时。单位为ms。不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| cpuDuration11+ | number | 否 | 否 | 执行任务CPU耗时。单位为ms。不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(func: Function, ...args: Object[])

Task的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | Function | 是 | 执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | Object[] | 否 | 任务执行传入函数的入参，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: string): string {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let task: taskpool.Task = new taskpool.Task(printArgs, "this is my first Task");
```

### constructor11+

PhonePC/2in1TabletTVWearable

constructor(name: string, func: Function, ...args: Object[])

Task的构造函数用于创建任务，并可指定任务名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 任务名称。 |
| func | Function | 是 | 执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | Object[] | 否 | 任务执行时传入函数的参数。支持的类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: string): string {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let taskName: string = "taskName";
8. let task: taskpool.Task = new taskpool.Task(taskName, printArgs, "this is my first Task");
9. let name: string = task.name;
```

### isCanceled10+

PhonePC/2in1TabletTVWearable

static isCanceled(): boolean

检查当前正在运行的任务是否已取消。使用此方法前，需要先创建一个Task对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前正在运行的任务被取消返回true，否则返回false。 |

**示例：**

```
1. @Concurrent
2. function inspectStatus(arg: number): number {
3. // do something
4. if (taskpool.Task.isCanceled()) {
5. console.info("task has been canceled.");
6. // do something
7. return arg + 1;
8. }
9. // do something
10. return arg;
11. }
```

说明

isCanceled方法需要和taskpool.cancel方法搭配使用，如果不调用cancel方法，isCanceled方法默认返回false。

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Concurrent
4. function inspectStatus(arg: number): number {
5. // 第一次检查任务是否已经取消并作出响应
6. if (taskpool.Task.isCanceled()) {
7. console.info("task has been canceled before 2s sleep.");
8. return arg + 2;
9. }
10. // 延时2s
11. let t: number = Date.now();
12. while (Date.now() - t < 2000) {
13. continue;
14. }
15. // 第二次检查任务是否已经取消并作出响应
16. if (taskpool.Task.isCanceled()) {
17. console.info("task has been canceled after 2s sleep.");
18. return arg + 3;
19. }
20. return arg + 1;
21. }

23. let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
24. taskpool.execute(task).then((res: Object) => {
25. console.info("Succeeded in executing task, result: " + res);
26. }).catch((e: BusinessError) => {
27. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
28. });
29. // 不调用cancel，isCanceled()默认返回false，task执行的结果为101
```

### setTransferList10+

PhonePC/2in1TabletTVWearable

setTransferList(transfer?: ArrayBuffer[]): void

设置任务的传输列表。使用该方法前需要先构造Task。不调用该接口，则传给任务的数据中的ArrayBuffer默认transfer转移。

说明

此接口可以设置任务池中ArrayBuffer的transfer列表，transfer列表中的ArrayBuffer对象在传输时不会复制buffer内容到工作线程而是转移buffer控制权至工作线程，传输后当前的ArrayBuffer失效。若ArrayBuffer为空，则不会transfer转移。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transfer | ArrayBuffer[] | 否 | 可传输对象是ArrayBuffer的实例对象，默认为空数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 10200029 | An ArrayBuffer cannot be set as both a transfer list and a clone list. |

**示例：**

```
1. @Concurrent
2. function testTransfer(arg1: ArrayBuffer, arg2: ArrayBuffer): number {
3. console.info("testTransfer arg1 byteLength: " + arg1.byteLength);
4. console.info("testTransfer arg2 byteLength: " + arg2.byteLength);
5. return 100;
6. }

8. let buffer: ArrayBuffer = new ArrayBuffer(8);
9. let view: Uint8Array = new Uint8Array(buffer);
10. let buffer1: ArrayBuffer = new ArrayBuffer(16);
11. let view1: Uint8Array = new Uint8Array(buffer1);

13. console.info("testTransfer view byteLength: " + view.byteLength);
14. console.info("testTransfer view1 byteLength: " + view1.byteLength);
15. // 执行结果为：
16. // testTransfer view byteLength: 8
17. // testTransfer view1 byteLength: 16

19. let task: taskpool.Task = new taskpool.Task(testTransfer, view, view1);
20. task.setTransferList([view.buffer, view1.buffer]);
21. taskpool.execute(task).then((res: Object) => {
22. console.info("test result: " + res);
23. }).catch((e: string) => {
24. console.error("test catch: " + e);
25. })
26. console.info("testTransfer view2 byteLength: " + view.byteLength);
27. console.info("testTransfer view3 byteLength: " + view1.byteLength);
28. // 经过transfer转移之后值为0，执行结果为：
29. // testTransfer view2 byteLength: 0
30. // testTransfer view3 byteLength: 0
```

### setCloneList11+

PhonePC/2in1TabletTVWearable

setCloneList(cloneList: Object[] | ArrayBuffer[]): void

设置任务的拷贝列表。在使用该方法前，需先构造Task对象。

说明

需搭配[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md#sendable装饰器)使用，否则会抛异常。建议开发者使用该装饰器以避免异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cloneList | Object[] | ArrayBuffer[] | 是 | - 传入数组的类型必须为[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)或ArrayBuffer。  - 所有传入cloneList的对象持有的[Sendable class](../harmonyos-guides/arkts-sendable.md#sendable-class)实例或ArrayBuffer类型对象，在线程间传输的行为都会变成拷贝传递，即修改传输后的对象不会对原有对象产生任何影响。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200029 | An ArrayBuffer cannot be set as both a transfer list and a clone list. |

**示例：**

```
1. // sendable.ets
2. // 定义两个Sendable class：BaseClass及其子类DeriveClass
3. @Sendable
4. export class BaseClass {
5. private str: string = "sendable: BaseClass";
6. static num :number = 10;
7. str1: string = "sendable: this is BaseClass's string";
8. num1: number = 5;
9. isDone1: boolean = false;

11. private fibonacciRecursive(n: number): number {
12. if (n <= 1) {
13. return n;
14. } else {
15. return this.fibonacciRecursive(n - 1) + this.fibonacciRecursive(n - 2);
16. }
17. }

19. private privateFunc(num: number): number{
20. let res: number = this.fibonacciRecursive(num);
21. console.info("sendable: BaseClass privateFunc res is: " + res);
22. return res;
23. }

25. publicFunc(num: number): number {
26. return this.privateFunc(num);
27. }

29. get GetNum(): number {
30. return this.num1;
31. }
32. set SetNum(num: number) {
33. this.num1 = num;
34. }

36. constructor() {
37. console.info(this.str);
38. this.isDone1 = true;
39. }
40. }

42. @Sendable
43. export class DeriveClass extends BaseClass {
44. name: string = "sendable: this is DeriveClass";
45. printName() {
46. console.info(this.name);
47. }
48. constructor() {
49. super();
50. }
51. }
```

```
1. // index.ets
2. // 宿主线程（这里的宿主线程为UI主线程）调用taskpool，在taskpool线程中调用BaseClass和DeriveClass的方法、访问对应属性
3. import { taskpool } from '@kit.ArkTS';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { BaseClass, DeriveClass } from './sendable';

7. @Concurrent
8. function testFunc(arr: Array<BaseClass>, num: number): number {
9. let baseInstance1 = arr[0];
10. console.info("sendable: str1 is: " + baseInstance1.str1);
11. baseInstance1.SetNum = 100;
12. console.info("sendable: num1 is: " + baseInstance1.GetNum);
13. console.info("sendable: isDone1 is: " + baseInstance1.isDone1);
14. // 获取斐波那契数列第num项的结果
15. let res: number = baseInstance1.publicFunc(num);
16. return res;
17. }

19. @Concurrent
20. function printLog(arr: Array<DeriveClass>): void {
21. let deriveInstance = arr[0];
22. deriveInstance.printName();
23. }

25. @Entry
26. @Component
27. struct Index {
28. @State message: string = 'Hello World';

30. build() {
31. Row() {
32. Column() {
33. Text(this.message)
34. .fontSize(50)
35. .fontWeight(FontWeight.Bold)
36. Button() {
37. Text("TaskPool Test");
38. }.onClick(() => {
39. // task1访问调用BaseClass.str1/BaseClass.SetNum/BaseClass.GetNum/BaseClass.isDone1/BaseClass.publicFunc
40. let baseInstance1: BaseClass = new BaseClass();
41. let array1 = new Array<BaseClass>();
42. array1.push(baseInstance1);
43. let task1 = new taskpool.Task(testFunc, array1, 10);
44. task1.setCloneList(array1);
45. taskpool.execute(task1).then((res: Object) => {
46. console.info("sendable: task1 res is: " + res);
47. }).catch((e:BusinessError) => {
48. console.error(`sendable: task1 execute Code is ${e.code}, message is ${e.message}`);
49. })

51. // task2调用DeriveClass.printName
52. let deriveInstance: DeriveClass = new DeriveClass();
53. let array2 = new Array<DeriveClass>();
54. array2.push(deriveInstance);
55. let task2 = new taskpool.Task(printLog, array2);
56. task2.setCloneList(array2);
57. taskpool.execute(task2).then(() => {
58. console.info("sendable: task2 execute success");
59. }).catch((e:BusinessError) => {
60. console.error(`sendable: task2 execute Code is ${e.code}, message is ${e.message}`);
61. })
62. })
63. .height('15%')
64. .width('30%')
65. }
66. .width('100%')
67. }
68. .height('100%')
69. }
70. }
```

### sendData11+

PhonePC/2in1TabletTVWearable

static sendData(...args: Object[]): void

任务执行过程中向宿主线程发送消息并触发回调。使用此方法前需构造Task。

说明

* 该接口应在taskpool的线程中调用。
* 避免在回调函数中调用该方法，否则可能导致消息无法传递到宿主线程。
* 避免在异步函数中调用该方法，否则可能导致消息无法传递到宿主线程。如果在异步函数中使用，则需要使用await来确保该异步函数在任务中同步执行完成。
* 调用该接口时，请确保处理数据的回调函数已在宿主线程注册。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | Object[] | 否 | 可传输对象默认转移，作为回调函数的参数。支持的参数类型请参见[序列化支持类型](js-apis-taskpool.md#序列化支持类型)，默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200006 | An exception occurred during serialization. |
| 10200022 | The function is not called in the TaskPool thread. |
| 10200023 | The function is not called in the concurrent function. |
| 10200024 | The callback is not registered on the host side. |

**示例：**

```
1. @Concurrent
2. function sendDataTest(num: number): number {
3. let res: number = num * 10;
4. taskpool.Task.sendData(res);
5. return num;
6. }

8. function printLog(data: number): void {
9. console.info("taskpool: data is: " + data);
10. }

12. async function taskpoolTest(): Promise<void> {
13. try {
14. let task: taskpool.Task = new taskpool.Task(sendDataTest, 1);
15. task.onReceiveData(printLog);
16. await taskpool.execute(task);
17. } catch (e) {
18. console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
19. }
20. }

22. taskpoolTest();
```

```
1. // 异步函数中调用该方法
2. @Concurrent
3. async function sendDataTest(num: number) {
4. let func = async () => {
5. let asyncSleep = async (time: number): Promise<Object> => {
6. return new Promise(resolve => setTimeout(resolve, time));
7. }
8. await asyncSleep(10000);
9. let res: number = num * 10;
10. taskpool.Task.sendData(res);
11. }
12. await func(); // 需要使用await来确保该异步函数在任务中同步执行完成。
13. }

15. function taskpoolTest() {
16. try {
17. let task: taskpool.Task = new taskpool.Task(sendDataTest, 10);
18. task.onReceiveData((data: number) => {
19. console.info("taskpool: data is: " + data);
20. });
21. taskpool.execute(task);
22. } catch (e) {
23. console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
24. }
25. }

27. taskpoolTest();
```

### onReceiveData11+

PhonePC/2in1TabletTVWearable

onReceiveData(callback?: Function): void

为任务注册回调函数，接收并处理任务池工作线程的数据。使用此方法前，需构造Task。

说明

不支持为同一任务定义多种回调函数。如果多次赋值，只有最后一次赋值的回调函数会生效。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 否 | 处理数据的回调函数，发送到宿主线程的数据将会作为入参传入该回调函数。不传参可以取消注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. @Concurrent
2. function ConcurrentFunc(num: number): number {
3. let res: number = num * 10;
4. taskpool.Task.sendData(res);
5. return num;
6. }

8. function printLog(data: number): void {
9. console.info("taskpool: data is: " + data);
10. }

12. async function testFunc(): Promise<void> {
13. try {
14. let task: taskpool.Task = new taskpool.Task(ConcurrentFunc, 1);
15. task.onReceiveData(printLog);
16. await taskpool.execute(task);
17. } catch (e) {
18. console.error(`taskpool: error code: ${e.code}, info: ${e.message}`);
19. }
20. }

22. testFunc();
```

### addDependency11+

PhonePC/2in1TabletTVWearable

addDependency(...tasks: Task[]): void

为当前任务添加对其他任务的依赖。使用该方法前需先构造Task。该任务和被依赖的任务不能是任务组任务、串行队列任务、异步队列任务、已执行任务或周期任务。存在依赖关系的任务（依赖其他任务的任务或被依赖的任务）执行后不可再次执行。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tasks | [Task](js-apis-taskpool.md#task)[] | 否 | 被依赖的任务数组。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200026 | There is a circular dependency. |
| 10200052 | The periodic task cannot have a dependency. |
| 10200056 | The task has been executed by the AsyncRunner. |

**示例：**

```
1. @Concurrent
2. function delay(args: number): number {
3. let t: number = Date.now();
4. while ((Date.now() - t) < 1000) {
5. continue;
6. }
7. return args;
8. }

10. let task1:taskpool.Task = new taskpool.Task(delay, 100);
11. let task2:taskpool.Task = new taskpool.Task(delay, 200);
12. let task3:taskpool.Task = new taskpool.Task(delay, 200);

14. console.info("dependency: add dependency start");
15. task1.addDependency(task2);
16. task2.addDependency(task3);
17. console.info("dependency: add dependency end");

19. console.info("dependency: start execute second");
20. taskpool.execute(task1).then(() => {
21. console.info("dependency: second task1 success");
22. })
23. taskpool.execute(task2).then(() => {
24. console.info("dependency: second task2 success");
25. })
26. taskpool.execute(task3).then(() => {
27. console.info("dependency: second task3 success");
28. })
```

### removeDependency11+

PhonePC/2in1TabletTVWearable

removeDependency(...tasks: Task[]): void

删除当前任务对其他任务的依赖。在使用该方法之前，需要先构造Task对象。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tasks | [Task](js-apis-taskpool.md#task)[] | 否 | 被依赖的任务数组。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200027 | The dependency does not exist. |
| 10200052 | The periodic task cannot have a dependency. |
| 10200056 | The task has been executed by the AsyncRunner. |

**示例：**

```
1. @Concurrent
2. function delay(args: number): number {
3. let t: number = Date.now();
4. while ((Date.now() - t) < 1000) {
5. continue;
6. }
7. return args;
8. }

10. let task1:taskpool.Task = new taskpool.Task(delay, 100);
11. let task2:taskpool.Task = new taskpool.Task(delay, 200);
12. let task3:taskpool.Task = new taskpool.Task(delay, 200);

14. console.info("dependency: add dependency start");
15. task1.addDependency(task2);
16. task2.addDependency(task3);
17. console.info("dependency: add dependency end");
18. console.info("dependency: remove dependency start");
19. task1.removeDependency(task2);
20. task2.removeDependency(task3);
21. console.info("dependency: remove dependency end");

23. console.info("dependency: start execute");
24. taskpool.execute(task1).then(() => {
25. console.info("dependency: task1 success");
26. })
27. taskpool.execute(task2).then(() => {
28. console.info("dependency: task2 success");
29. })
30. taskpool.execute(task3).then(() => {
31. console.info("dependency: task3 success");
32. })
```

### onEnqueued12+

PhonePC/2in1TabletTVWearable

onEnqueued(callback: CallbackFunction): void

注册回调函数，任务入队时将调用该函数。若任务执行前未注册回调函数，将抛出异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CallbackFunction](js-apis-taskpool.md#callbackfunction12) | 是 | 需注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200034 | The executed task does not support the registration of listeners. |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function delay(args: number): number {
5. let t: number = Date.now();
6. while ((Date.now() - t) < 1000) {
7. continue;
8. }
9. return args;
10. }

12. let task: taskpool.Task = new taskpool.Task(delay, 1);
13. task.onEnqueued(() => {
14. console.info("taskpool: onEnqueued");
15. });
16. taskpool.execute(task).then(() => {
17. console.info("taskpool: execute task success");
18. });
```

### onStartExecution12+

PhonePC/2in1TabletTVWearable

onStartExecution(callback: CallbackFunction): void

注册回调函数，任务执行前将调用该函数。若任务执行前未注册回调函数，将抛出异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CallbackFunction](js-apis-taskpool.md#callbackfunction12) | 是 | 需注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200034 | The executed task does not support the registration of listeners. |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function delay(args: number): number {
5. let t: number = Date.now();
6. while ((Date.now() - t) < 1000) {
7. continue;
8. }
9. return args;
10. }

12. let task: taskpool.Task = new taskpool.Task(delay, 1);
13. task.onStartExecution(() => {
14. console.info("taskpool: onStartExecution");
15. });
16. taskpool.execute(task).then(() => {
17. console.info("taskpool: execute task success");
18. });
```

### onExecutionFailed12+

PhonePC/2in1TabletTVWearable

onExecutionFailed(callback: CallbackFunctionWithError): void

注册一个回调函数，并在任务执行失败时调用它（周期任务不支持）。需在任务执行前注册，否则会抛异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CallbackFunctionWithError](js-apis-taskpool.md#callbackfunctionwitherror12) | 是 | 需注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200034 | The executed task does not support the registration of listeners. |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { HashMap } from '@kit.ArkTS';

5. @Concurrent
6. function test(args: number) {
7. let t = Date.now();
8. while ((Date.now() - t) < 100) {
9. continue;
10. }
11. let hashMap1: HashMap<string, number> = new HashMap();
12. hashMap1.set('a', args);
13. return hashMap1;
14. }

16. let task2 = new taskpool.Task(test, 1);
17. task2.onExecutionFailed((e: Error) => {
18. console.info("taskpool: onExecutionFailed error is " + e);
19. })
20. taskpool.execute(task2).then(() => {
21. console.info("taskpool: execute task success");
22. }).catch((e:BusinessError) => {
23. console.error(`taskpool: error code: ${e.code}, error info: ${e.message}`);
24. })
```

### onExecutionSucceeded12+

PhonePC/2in1TabletTVWearable

onExecutionSucceeded(callback: CallbackFunction): void

注册一个回调函数，并在任务执行成功时调用它（周期任务不支持）。需在任务执行前注册，否则会抛异常。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CallbackFunction](js-apis-taskpool.md#callbackfunction12) | 是 | 需注册的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameters are invalid. |
| 10200034 | The executed task does not support the registration of listeners. |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function delay(args: number): number {
5. let t: number = Date.now();
6. while ((Date.now() - t) < 1000) {
7. continue;
8. }
9. return args;
10. }

12. let task: taskpool.Task = new taskpool.Task(delay, 1);
13. task.onExecutionSucceeded(() => {
14. console.info("taskpool: onExecutionSucceeded");
15. });
16. taskpool.execute(task).then(() => {
17. console.info("taskpool: execute task success");
18. });
```

### isDone12+

PhonePC/2in1TabletTVWearable

isDone(): boolean

检查任务是否已完成。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 任务执行完成时返回true，任务未执行完成时返回false。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Concurrent
4. function inspectStatus(arg: number): number {
5. // 1s sleep
6. let t: number = Date.now();
7. while (Date.now() - t < 1000) {
8. continue;
9. }
10. return arg + 1;
11. }

13. async function taskpoolCancel(): Promise<void> {
14. let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
15. taskpool.execute(task).then((res: Object) => {
16. console.info("Succeeded in executing task, result: " + res);
17. }).catch((e: BusinessError) => {
18. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
19. });

21. setTimeout(() => {
22. if (!task.isDone()) {
23. taskpool.cancel(task);
24. }
25. }, 3000); // 延时3s，确保任务已执行
26. }

28. taskpoolCancel();
```

## CallbackFunction12+

PhonePC/2in1TabletTVWearable

type CallbackFunction = () => void

注册的回调函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

## CallbackFunctionWithError12+

PhonePC/2in1TabletTVWearable

type CallbackFunctionWithError = (e: Error) => void

注册带有错误码的回调函数类型。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| e | Error | 是 | 错误信息。 |

## LongTask12+

PhonePC/2in1TabletTVWearable

表示长时任务。LongTask继承自[Task](js-apis-taskpool.md#task)。

长时任务不设置执行时间上限，长时间运行不会触发超时异常，但不支持将同一任务多次执行或者将该任务加入任务组（TaskGroup）。

执行长时任务的线程会持续存在，直到任务完成并调用[terminateTask](js-apis-taskpool.md#taskpoolterminatetask12)后，该线程在空闲时被回收。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**示例：**

```
1. @Concurrent
2. function printArgs(args: string): string {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let task: taskpool.LongTask = new taskpool.LongTask(printArgs, "this is my first LongTask");
```

## GenericsTask13+

PhonePC/2in1TabletTVWearable

表示泛型任务。GenericsTask继承自[Task](js-apis-taskpool.md#task)。

相比创建Task，创建GenericsTask可以在编译阶段校验并发函数的传参和返回值类型。其余行为与Task相同。

**系统能力：** SystemCapability.Utils.Lang

### constructor13+

PhonePC/2in1TabletTVWearable

constructor(func: (...args: A) => R | Promise<R>, ...args: A)

GenericsTask的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | (...args: A) => R | Promise<R> | 是 | 执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | A | 否 | 任务执行传入函数的入参，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: string): string {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. @Concurrent
8. function testWithThreeParams(a: number, b: string, c: number): string {
9. return b;
10. }

12. @Concurrent
13. function testWithArray(args: [number, string]): string {
14. return "success";
15. }

17. let task1: taskpool.Task = new taskpool.GenericsTask<[string], string>(printArgs, "this is my first LongTask");

19. let task2: taskpool.Task = new taskpool.GenericsTask<[number, string, number], string>(testWithThreeParams, 100, "test", 100);

21. let task3: taskpool.Task = new taskpool.GenericsTask<[[number, string]], string>(testWithArray, [100, "test"]);
```

### constructor13+

PhonePC/2in1TabletTVWearable

constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)

GenericsTask的构造函数，可以指定任务名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 泛型任务名称。 |
| func | (...args: A) => R | Promise<R> | 是 | 执行的逻辑需要传入函数，必须使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰，支持的函数返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | A | 否 | 任务执行传入函数的入参，支持的参数类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: string): string {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let taskName: string = "taskName";
8. let task: taskpool.Task = new taskpool.GenericsTask<[string], string>(taskName, printArgs, "this is my first Task");
9. let name: string = task.name;
```

## TaskGroup10+

PhonePC/2in1TabletTVWearable

表示任务组，一次执行一组任务，适用于执行一组有关联的任务。如果所有任务正常执行，异步执行完毕后返回所有任务结果的数组，数组中元素的顺序与[addTask](js-apis-taskpool.md#addtask10-1)的顺序相同；如果任意任务失败，则会抛出对应异常。如果任务组中存在多个任务失败的情况，则会抛出第一个失败任务的异常。任务组可以多次执行，但执行后不能新增任务。

### constructor10+

PhonePC/2in1TabletTVWearable

constructor()

TaskGroup的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**示例：**

```
1. let taskGroup = new taskpool.TaskGroup();
```

### constructor11+

PhonePC/2in1TabletTVWearable

constructor(name: string)

TaskGroup的构造函数，支持指定任务组名称。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 任务组名称。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let taskGroupName: string = "groupName";
2. let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup(taskGroupName);
3. let name: string = taskGroup.name;
```

### addTask10+

PhonePC/2in1TabletTVWearable

addTask(func: Function, ...args: Object[]): void

将待执行的函数添加到任务组中。使用该方法前需要先构造TaskGroup。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| func | Function | 是 | 需要传入使用[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)装饰的函数。支持的返回值类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)。 |
| args | Object[] | 否 | 任务执行函数的入参，支持的类型请参考[序列化支持类型](js-apis-taskpool.md#序列化支持类型)，默认值为undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200014 | The function is not marked as concurrent. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
8. taskGroup.addTask(printArgs, 100); // 100: test number
```

### addTask10+

PhonePC/2in1TabletTVWearable

addTask(task: Task): void

将创建好的任务添加到任务组中。使用此方法前需要先构造TaskGroup。任务组不能添加其他任务组中的任务、串行队列任务、异步队列任务、有依赖关系的任务、长时任务、周期任务和已执行的任务。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要添加到任务组中的任务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 10200014 | The function is not marked as concurrent. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function printArgs(args: number): number {
3. console.info("printArgs: " + args);
4. return args;
5. }

7. let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
8. let task: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
9. taskGroup.addTask(task);
```

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name11+ | string | 否 | 否 | 创建任务组时指定的任务组名称。 |

## SequenceRunner 11+

PhonePC/2in1TabletTVWearable

表示串行队列的任务，用于执行一组需要串行执行的任务。

### constructor11+

PhonePC/2in1TabletTVWearable

constructor(priority?: Priority)

SequenceRunner的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. let runner: taskpool.SequenceRunner = new taskpool.SequenceRunner();
```

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(name: string, priority?: Priority)

SequenceRunner的构造函数。构造一个全局串行队列，如果名字相同，将返回同一个串行队列。

说明

* 底层通过单例模式保证了：创建同名串行队列时，获取到同一个实例。
* 无法修改串行队列的优先级。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 串行队列的名字。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner("runner1", taskpool.Priority.LOW);
```

### execute11+

PhonePC/2in1TabletTVWearable

execute(task: Task): Promise<Object>

执行串行任务。使用该方法前需先构造SequenceRunner。串行队列不能执行任务组任务、其他串行队列任务、异步队列任务、有依赖关系的任务和已执行的任务。使用Promise异步回调。

说明

* 不支持加入存在依赖的任务。
* 前面的任务执行失败或取消不会影响后续任务的执行。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要添加到串行任务队列中的任务。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回任务执行的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 10200006 | An exception occurred during serialization. |
| 10200025 | dependent task not allowed. |
| 10200051 | The periodic task cannot be executed again. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. @Concurrent
2. function additionDelay(delay: number): void {
3. let start: number = new Date().getTime();
4. while (new Date().getTime() - start < delay) {
5. continue;
6. }
7. }
8. @Concurrent
9. function waitForRunner(finalString: string): string {
10. return finalString;
11. }
12. async function seqRunner() {
13. let finalString:string = "";
14. let task1:taskpool.Task = new taskpool.Task(additionDelay, 3000);
15. let task2:taskpool.Task = new taskpool.Task(additionDelay, 2000);
16. let task3:taskpool.Task = new taskpool.Task(additionDelay, 1000);
17. let task4:taskpool.Task = new taskpool.Task(waitForRunner, finalString);

19. let runner:taskpool.SequenceRunner = new taskpool.SequenceRunner();
20. runner.execute(task1).then(() => {
21. finalString += 'a';
22. console.info("seqrunner: task1 done.");
23. });
24. runner.execute(task2).then(() => {
25. finalString += 'b';
26. console.info("seqrunner: task2 done");
27. });
28. runner.execute(task3).then(() => {
29. finalString += 'c';
30. console.info("seqrunner: task3 done");
31. });
32. await runner.execute(task4);
33. console.info("seqrunner: task4 done, finalString is " + finalString);
34. }
```

## AsyncRunner18+

PhonePC/2in1TabletTVWearable

表示异步队列。可以指定任务执行的并发度和排队策略。

### constructor18+

PhonePC/2in1TabletTVWearable

constructor(runningCapacity: number, waitingCapacity?: number)

AsyncRunner的构造函数。构造一个非全局的异步队列，如果参数相同，返回的是不同的异步队列。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| runningCapacity | number | 是 | 指定任务执行的最大并发度，该参数应为正整数，负数时报错，非整数时会向下取整。 |
| waitingCapacity | number | 否 | 指定等待任务的列表容量，取值需大于等于0，负数时报错，输入非整数时会向下取整。默认值为0，表示等待任务列表的容量没有限制。如果设置大于0的值，则表示排队策略为丢弃策略，当加入的任务数量超过该值时，等待列表中处于队头的任务会被丢弃。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. let runner: taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
```

### constructor18+

PhonePC/2in1TabletTVWearable

constructor(name: string, runningCapacity: number, waitingCapacity?: number)

AsyncRunner的构造函数用于构造一个全局异步队列。如果队列名称相同，将返回同一个异步队列实例。

说明

* 底层通过单例模式确保创建同名的异步队列时，获取同一个实例。
* 无法修改并发度和等待任务列表容量。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 异步队列的名字。 |
| runningCapacity | number | 是 | 指定任务执行的最大并发度，该参数应为正整数。负数时报错，非整数会向下取整。 |
| waitingCapacity | number | 否 | 指定等待任务的列表容量，取值需大于等于0，负数时报错，非整数时会向下取整。默认值为0，表示等待任务列表的容量没有限制。如果设置大于0的值，则表示排队策略为丢弃策略，当加入的任务数量超过该值时，等待列表中处于队头的任务会被丢弃。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

**示例：**

```
1. let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
```

### execute18+

PhonePC/2in1TabletTVWearable

execute(task: Task, priority?: Priority): Promise<Object>

执行异步任务。使用该方法前需要先构造AsyncRunner。使用Promise异步回调。

说明

* 不支持执行任务组中的任务。
* 不支持执行串行队列中的任务。
* 不支持执行其他异步队列任务。
* 不支持执行周期性任务。
* 不支持执行延迟任务。
* 不支持执行存在依赖的任务。
* 不支持执行已执行过的任务。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [Task](js-apis-taskpool.md#task) | 是 | 需要添加到异步队列中的任务。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 指定任务的优先级，该参数默认值为taskpool.Priority.MEDIUM。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回任务执行的结果。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200006 | An exception occurred during serialization. |
| 10200025 | dependent task not allowed. |
| 10200051 | The periodic task cannot be executed again. |
| 10200054 | The asyncRunner task is discarded. |
| 10200057 | The task cannot be executed by two APIs. |

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Concurrent
5. function additionDelay(delay: number): void {
6. let start: number = new Date().getTime();
7. while (new Date().getTime() - start < delay) {
8. continue;
9. }
10. }
11. async function asyRunner() {
12. let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner("runner1", 5, 5);
13. for (let i = 0; i < 30; i++) {
14. let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
15. runner.execute(task).then(() => {
16. console.info("asyncRunner: task" + i + " done.");
17. }).catch((e: BusinessError) => {
18. console.error("asyncRunner: task" + i + " error." + e.code + "-" + e.message);
19. });
20. }
21. }

23. async function asyRunner2() {
24. let runner:taskpool.AsyncRunner = new taskpool.AsyncRunner(5);
25. for (let i = 0; i < 20; i++) {
26. let task:taskpool.Task = new taskpool.Task(additionDelay, 1000);
27. runner.execute(task).then(() => {
28. console.info("asyncRunner: task" + i + " done.");
29. });
30. }
31. }
```

## State10+

PhonePC/2in1TabletTVWearable

表示任务（Task）状态的枚举。当任务创建成功后，调用execute，任务进入taskpool等待队列，状态设置为WAITING；任务从等待队列出来进入taskpool工作线程中，任务状态更新为RUNNING；当任务执行完成，返回结果后任务状态重置为WAITING；当主动cancel任务时，将任务状态更新为CANCELED。

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WAITING | 1 | 任务正在等待。 |
| RUNNING | 2 | 任务正在执行。 |
| CANCELED | 3 | 任务已被取消。 |

## TaskInfo10+

PhonePC/2in1TabletTVWearable

任务的内部信息。

**系统能力：** SystemCapability.Utils.Lang

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name12+ | string | 否 | 否 | 任务的名字，不建议修改此值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| taskId | number | 否 | 否 | 任务的ID。任务的标识符，系统默认提供全局唯一值，不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| state | [State](js-apis-taskpool.md#state10) | 否 | 否 | 任务的状态。state标识任务的当前状态，不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| duration | number | 否 | 是 | 任务执行至当前所用的时间，默认为0，单位为ms。当返回为0时，表示任务未执行；返回为空时，表示没有任务执行。不建议修改此值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ThreadInfo10+

PhonePC/2in1TabletTVWearable

工作线程的内部信息。

**系统能力：** SystemCapability.Utils.Lang

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tid | number | 否 | 否 | 工作线程的标识符。如果返回为空，表示当前没有任务执行。不建议修改此值。 |
| taskIds | number[] | 否 | 是 | 在当前线程上运行的任务ID列表。返回为空时，代表没有任务执行。不建议修改此值。 |
| priority | [Priority](js-apis-taskpool.md#priority) | 否 | 是 | 当前线程的优先级。返回为空时，代表没有任务执行。 不建议修改此值。 |

## TaskPoolInfo10+

PhonePC/2in1TabletTVWearable

任务池的内部信息。

**系统能力：** SystemCapability.Utils.Lang

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| threadInfos | [ThreadInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#threadinfo10) | 否 | 否 | 工作线程的内部信息。不建议修改此值。 |
| taskInfos | [TaskInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool#taskinfo10) | 否 | 否 | 任务的内部信息。不建议修改此值。 |

## TaskResult20+

PhonePC/2in1TabletTVWearable

处于等待或执行过程中的任务进行取消操作后，在catch分支里捕获到BusinessError里的补充信息。其他场景下该信息为undefined。

**系统能力：** SystemCapability.Utils.Lang

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Utils.Lang

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | Object | 否 | 是 | 任务执行结果。默认为undefined。 不建议修改此值。 |
| error | Error | Object | 否 | 是 | 错误信息。默认和BusinessError的message字段一致。不建议修改此值。 |

说明

任务被取消后，有如下两种情况：

* 如果当前任务是处于等待阶段，则result的值为undefined，error的值和BusinessError的message字段一致；
* 如果当前任务正在运行，有异常抛出的情况下result的值为undefined，error的值为抛出的异常信息；没有异常的情况下，result为任务执行完成后的结果，error的值和BusinessError的message字段一致。

**示例**

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit'

4. @Concurrent
5. function loop(): Error | number {
6. let start: number = Date.now();
7. while (Date.now() - start < 1500) {
8. }
9. if (taskpool.Task.isCanceled()) {
10. return 0;
11. }
12. while (Date.now() - start < 3000) {
13. }
14. if (taskpool.Task.isCanceled()) {
15. throw new Error("this is loop error");
16. }
17. return 1;
18. }

20. // 执行前取消
21. function waitingCancel() {
22. let task = new taskpool.Task(loop);
23. taskpool.executeDelayed(2000, task).catch((e:BusinessError<taskpool.TaskResult>) => {
24. console.error(`waitingCancel task catch code: ${e.code}, message: ${e.message}`);
25. // waitingCancel task catch code: 0, message: taskpool:: task has been canceled
26. if (e.data !== undefined) {
27. console.error(`waitingCancel task catch data: result: ${e.data.result}, error: ${e.data.error}`);
28. // waitingCancel task catch data: result: undefined, error: taskpool:: task has been canceled
29. }
30. })
31. setTimeout(() => {
32. taskpool.cancel(task);
33. }, 1000);
34. }

36. // 执行过程中取消
37. function runningCancel() {
38. let task = new taskpool.Task(loop);
39. taskpool.execute(task).catch((e:BusinessError<taskpool.TaskResult>) => {
40. console.error(`runningCancel task catch code: ${e.code}, message: ${e.message}`);
41. // runningCancel task catch code: 0, message: taskpool:: task has been canceled
42. if (e.data !== undefined) {
43. console.error(`runningCancel task catch data: result: ${e.data.result}, error: ${e.data.error}`);
44. // runningCancel task catch data: result: 0, error: taskpool:: task has been canceled
45. }
46. })
47. setTimeout(() => {
48. taskpool.cancel(task);
49. }, 1000);
50. }

52. // 执行过程中抛异常
53. function runningCancelError() {
54. let task = new taskpool.Task(loop);
55. taskpool.execute(task).catch((e:BusinessError<taskpool.TaskResult>) => {
56. console.error(`runningCancelError task catch code: ${e.code}, message: ${e.message}`);
57. // runningCancelError task catch code: 0, message: taskpool:: task has been canceled
58. if (e.data !== undefined) {
59. console.error(`runningCancelError task catch data: result: ${e.data.result}, error: ${e.data.error}`);
60. // runningCancelError task catch data: result: undefined, error: Error: this is loop error
61. }
62. })
63. setTimeout(() => {
64. taskpool.cancel(task);
65. }, 2000);
66. }
```

## 其他说明

PhonePC/2in1TabletTVWearable

### 序列化支持类型

序列化支持类型参考[线程间通信对象概述](../harmonyos-guides/serializable-overview.md)里的介绍。

### 简单使用

**示例一**

```
1. // 支持普通函数、引用入参传递
2. @Concurrent
3. function printArgs(args: string): string {
4. console.info("func: " + args);
5. return args;
6. }

8. async function taskpoolExecute(): Promise<void> {
9. // taskpool.execute(task)
10. let task: taskpool.Task = new taskpool.Task(printArgs, "create task, then execute");
11. console.info("taskpool.execute(task) result: " + await taskpool.execute(task));
12. // taskpool.execute(function)
13. console.info("taskpool.execute(function) result: " + await taskpool.execute(printArgs, "execute task by func"));
14. }

16. taskpoolExecute();
```

**示例二**

```
1. // b.ets
2. export let c: string = "hello";
```

```
1. // 引用import变量
2. // a.ets(与b.ets位于同一目录中)
3. import { c } from "./b";

5. @Concurrent
6. function printArgs(a: string): string {
7. console.info(a);
8. console.info(c);
9. return a;
10. }

12. async function taskpoolExecute(): Promise<void> {
13. // taskpool.execute(task)
14. let task: taskpool.Task = new taskpool.Task(printArgs, "create task, then execute");
15. console.info("taskpool.execute(task) result: " + await taskpool.execute(task));

17. // taskpool.execute(function)
18. console.info("taskpool.execute(function) result: " + await taskpool.execute(printArgs, "execute task by func"));
19. }

21. taskpoolExecute();
```

**示例三**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 支持async函数
4. @Concurrent
5. async function delayExecute(): Promise<Array<Object>> {
6. let ret = await Promise.all<Object>([
7. new Promise<Object>(resolve => setTimeout(resolve, 1000, "resolved"))
8. ]);
9. return ret;
10. }

12. async function taskpoolExecute(): Promise<void> {
13. taskpool.execute(delayExecute).then((result: Object) => {
14. console.info("Succeeded in excuting task, result: " + result);
15. }).catch((e: BusinessError) => {
16. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
17. });
18. }

20. taskpoolExecute();
```

**示例四**

```
1. // c.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Concurrent
5. function strSort(inPutArr: Array<string>): Array<string> {
6. let newArr = inPutArr.sort();
7. return newArr;
8. }

10. export async function func1(): Promise<void> {
11. console.info("taskpoolTest start");
12. let strArray: Array<string> = ['c test string', 'b test string', 'a test string'];
13. let task: taskpool.Task = new taskpool.Task(strSort, strArray);
14. console.info("func1 result:" + await taskpool.execute(task));
15. }

17. export async function func2(): Promise<void> {
18. console.info("taskpoolTest2 start");
19. let strArray: Array<string> = ['c test string', 'b test string', 'a test string'];
20. taskpool.execute(strSort, strArray).then((result: Object) => {
21. console.info("Succeeded in excuting task, result: " + result);
22. }).catch((e: BusinessError) => {
23. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
24. });
25. }
```

```
1. // index.ets
2. import { func1, func2 } from "./c";

4. func1();
5. func2();
```

**示例五**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 任务取消成功
4. @Concurrent
5. function inspectStatus(arg: number): number {
6. // 第一次检查任务是否已经取消并作出响应
7. if (taskpool.Task.isCanceled()) {
8. console.info("task has been canceled before 2s sleep.");
9. return arg + 2;
10. }
11. // 2s sleep
12. let t: number = Date.now();
13. while (Date.now() - t < 2000) {
14. continue;
15. }
16. // 第二次检查任务是否已经取消并作出响应
17. if (taskpool.Task.isCanceled()) {
18. console.info("task has been canceled after 2s sleep.");
19. return arg + 3;
20. }
21. return arg + 1;
22. }

24. async function taskpoolCancel(): Promise<void> {
25. let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
26. taskpool.execute(task).then((res: Object) => {
27. console.info("Succeeded in excuting task, result: " + res);
28. }).catch((e: BusinessError) => {
29. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
30. });
31. // 1s后取消task
32. setTimeout(() => {
33. try {
34. taskpool.cancel(task);
35. } catch (e) {
36. console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
37. }
38. }, 1000);
39. }

41. taskpoolCancel();
```

**示例六**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 已执行的任务取消失败
4. @Concurrent
5. function inspectStatus(arg: number): number {
6. // 第一次检查任务是否已经取消并作出响应
7. if (taskpool.Task.isCanceled()) {
8. return arg + 2;
9. }
10. // 延时0.5s
11. let t: number = Date.now();
12. while (Date.now() - t < 500) {
13. continue;
14. }
15. // 第二次检查任务是否已经取消并作出响应
16. if (taskpool.Task.isCanceled()) {
17. return arg + 3;
18. }
19. return arg + 1;
20. }

22. async function taskpoolCancel(): Promise<void> {
23. let task: taskpool.Task = new taskpool.Task(inspectStatus, 100); // 100: test number
24. taskpool.execute(task).then((res: Object) => {
25. console.info("Succeeded in excuting task, result: " + res);
26. }).catch((e: BusinessError) => {
27. console.error(`Failed to execute task. Code: ${e.code}, message: ${e.message}`);
28. });

30. setTimeout(() => {
31. try {
32. taskpool.cancel(task); // 任务已执行,取消失败
33. } catch (e) {
34. console.error(`taskpool: cancel error code: ${e.code}, info: ${e.message}`);
35. }
36. }, 3000); // 延时3s，确保任务已执行
37. }

39. taskpoolCancel();
```

**示例七**

```
1. // 待执行的任务组取消成功
2. @Concurrent
3. function printArgs(args: number): number {
4. let t: number = Date.now();
5. while (Date.now() - t < 1000) {
6. continue;
7. }
8. console.info("printArgs: " + args);
9. return args;
10. }

12. async function taskpoolGroupCancelTest(): Promise<void> {
13. let taskGroup1: taskpool.TaskGroup = new taskpool.TaskGroup();
14. taskGroup1.addTask(printArgs, 10); // 10: test number
15. taskGroup1.addTask(printArgs, 20); // 20: test number
16. taskGroup1.addTask(printArgs, 30); // 30: test number
17. let taskGroup2: taskpool.TaskGroup = new taskpool.TaskGroup();
18. let task1: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
19. let task2: taskpool.Task = new taskpool.Task(printArgs, 200); // 200: test number
20. let task3: taskpool.Task = new taskpool.Task(printArgs, 300); // 300: test number
21. taskGroup2.addTask(task1);
22. taskGroup2.addTask(task2);
23. taskGroup2.addTask(task3);
24. taskpool.execute(taskGroup1).then((res: Array<Object>) => {
25. console.info("taskpool execute res is:" + res);
26. }).catch((e: string) => {
27. console.error("taskpool execute error is:" + e);
28. });
29. taskpool.execute(taskGroup2).then((res: Array<Object>) => {
30. console.info("taskpool execute res is:" + res);
31. }).catch((e: string) => {
32. console.error("taskpool execute error is:" + e);
33. });

35. try {
36. taskpool.cancel(taskGroup2);
37. } catch (e) {
38. console.error(`Failed to cancel task. Code: ${e.code}, message: ${e.message}`);
39. }
40. }

42. taskpoolGroupCancelTest()
```

**示例八**

```
1. // 分别创建执行100个高、中、低优先级的任务，查看其各项信息
2. @Concurrent
3. function delay(): void {
4. let start: number = new Date().getTime();
5. while (new Date().getTime() - start < 500) {
6. continue;
7. }
8. }

10. let highCount: number = 0;
11. let mediumCount: number = 0;
12. let lowCount: number = 0;
13. let allCount: number = 100;
14. for (let i = 0; i < allCount; i++) {
15. let task1: taskpool.Task = new taskpool.Task(delay);
16. let task2: taskpool.Task = new taskpool.Task(delay);
17. let task3: taskpool.Task = new taskpool.Task(delay);
18. taskpool.execute(task1, taskpool.Priority.LOW).then(() => {
19. lowCount++;
20. }).catch((e: string) => {
21. console.error("low task error: " + e);
22. })
23. taskpool.execute(task2, taskpool.Priority.MEDIUM).then(() => {
24. mediumCount++;
25. }).catch((e: string) => {
26. console.error("medium task error: " + e);
27. })
28. taskpool.execute(task3, taskpool.Priority.HIGH).then(() => {
29. highCount++;
30. }).catch((e: string) => {
31. console.error("high task error: " + e);
32. })
33. }
34. let start: number = new Date().getTime();
35. while (new Date().getTime() - start < 1000) {
36. continue;
37. }
38. let taskpoolInfo: taskpool.TaskPoolInfo = taskpool.getTaskPoolInfo();
39. let tid: number = 0;
40. let taskIds: Array<number> = [];
41. let priority: number = 0;
42. let taskId: number = 0;
43. let state: number = 0;
44. let duration: number = 0;
45. let name: string = "";
46. let threadIS = Array.from(taskpoolInfo.threadInfos);
47. for (let threadInfo of threadIS) {
48. tid = threadInfo.tid;
49. if (threadInfo.taskIds != undefined && threadInfo.priority != undefined) {
50. taskIds.length = threadInfo.taskIds.length;
51. priority = threadInfo.priority;
52. }
53. console.info("taskpool---tid is:" + tid + ", taskIds is:" + taskIds + ", priority is:" + priority);
54. }
55. let taskIS = Array.from(taskpoolInfo.taskInfos);
56. for (let taskInfo of taskIS) {
57. taskId = taskInfo.taskId;
58. state = taskInfo.state;
59. if (taskInfo.duration != undefined) {
60. duration = taskInfo.duration;
61. name = taskInfo.name;
62. }
63. console.info("taskpool---taskId is:" + taskId + ", state is:" + state + ", duration is:" + duration + ", name is:" + name);
64. }
```
