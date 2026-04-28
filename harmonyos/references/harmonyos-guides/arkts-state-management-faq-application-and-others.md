---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-application-and-others
title: 应用内状态管理和其他常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理常见问题 > 应用内状态管理和其他常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edc31c7d23cb520bb999f571cfd366cfc391ea9fe417ae935f556b13964c3d77
---

本文将介绍应用内状态管理的常见问题以及其他常见问题。

## 在并发线程中使用ArkUI装饰器导致报错

### 懒加载包含装饰器的文件

状态管理装饰器仅限于在UI线程使用，不允许在未加载ArkUI框架的[并发线程](multi-thread-concurrency-overview.md)中使用。由于并发线程未加载完整的ArkUI框架逻辑，因此框架中定义的状态管理装饰器也不会被加载到并发线程中。若在并发线程中使用状态管理装饰器，将出现ReferenceError: xxx is not defined。在如下示例中，尽管并发线程并未实际使用[@Observed](arkts-observed-and-objectlink.md)装饰的类，但仍会打印ReferenceError: Observed is not defined的报错信息。这是因为并发线程在逐层解析文件依赖时，最终会加载到定义@Observed装饰器的Observed.ets文件，从而触发该错误。

【反例】

```
1. // src/main/ets/pages/LazyImportNeg.ets
2. import { ErrorEvent, worker, MessageEvents } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Button('New Worker')
9. .onClick(() => {
10. // 创建Worker对象。
11. const newWorker = new worker.ThreadWorker('../workers/LazyImportWorkerNeg.ets');

13. // 注册onmessage回调，捕获宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息。该回调在宿主线程执行。
14. newWorker.onmessage = (e: MessageEvents) => {
15. let data: string = e.data;
16. console.info('newWorker onmessage is: ', data);
17. };

19. // 注册onAllErrors回调，捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常。该回调在宿主线程执行。
20. newWorker.onAllErrors = (err: ErrorEvent) => {
21. console.error('workerInstance onAllErrors message is: ' + err.message);
22. };

24. // 注册onmessageerror回调，当Worker对象接收到无法序列化的消息时被调用，在宿主线程执行。
25. newWorker.onmessageerror = () => {
26. console.error('workerInstance onmessageerror');
27. };

29. // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行。
30. newWorker.onexit = (e: number) => {
31. // Worker正常退出时，code为0；异常退出时，code为1。
32. console.info('workerInstance onexit code is: ', e);
33. };

35. // 发送消息给Worker线程。
36. newWorker.postMessage('[Main] message from the main thread');
37. })
38. }
39. }
```

```
1. // src/main/ets/workers/LazyImportWorkerNeg.ets
2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
3. import { testWithoutObserved } from '../pages/LazyImportFuncNeg';

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. // 注册onmessage回调，当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用，在Worker线程执行。
8. workerPort.onmessage = (e: MessageEvents) => {
9. // 调用testWithoutObserved函数。
10. testWithoutObserved();
11. let data: string = e.data;
12. console.info('workerPort onmessage is: ', data);

14. // 向宿主线程发送消息。
15. workerPort.postMessage('[Worker] message from the workerPort');
16. };

18. // 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在Worker线程执行。
19. workerPort.onmessageerror = () => {
20. console.error('workerPort onmessageerror');
21. };

23. // 注册onerror回调，捕获Worker在执行过程中发生的异常，在Worker线程执行。
24. workerPort.onerror = (err: ErrorEvent) => {
25. console.error('workerPort onerror err is: ', err.message);
26. };
```

```
1. // src/main/ets/pages/LazyImportFuncNeg.ets
2. import { innerTest } from './LazyImportObservedNeg';

4. export function testWithObserved(): void {
5. innerTest();
6. console.info('ImportObserved::testWithObserved call');
7. }

9. export function testWithoutObserved(): void {
10. console.info('ImportObserved::testWithoutObserved call');
11. }
```

```
1. // src/main/ets/pages/LazyImportObservedNeg.ets
2. export function innerTest(): void {
3. console.info('Observed::innerTest call');
4. }

6. @Observed
7. export class Person {
8. public name: string;
9. public age: number;

11. constructor(name: string, age: number) {
12. this.name = name;
13. this.age = age;
14. }
15. }
```

可以使用[lazy import](arkts-lazy-import.md)懒加载包含装饰器的文件，子线程则不会加载到对应文件。

【正例】

```
1. // src/main/ets/pages/LazyImportPos.ets
2. import { ErrorEvent, worker, MessageEvents } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Button('New Worker')
9. .onClick(() => {
10. // 创建Worker对象。
11. const newWorker = new worker.ThreadWorker('../workers/LazyImportWorkerPos.ets');

13. // 注册onmessage回调，捕获宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息。该回调在宿主线程执行。
14. newWorker.onmessage = (e: MessageEvents) => {
15. let data: string = e.data;
16. console.info('newWorker onmessage is: ', data);
17. };

19. // 注册onAllErrors回调，捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常。该回调在宿主线程执行。
20. newWorker.onAllErrors = (err: ErrorEvent) => {
21. console.error('workerInstance onAllErrors message is: ' + err.message);
22. };

24. // 注册onmessageerror回调，当Worker对象接收到无法序列化的消息时被调用，在宿主线程执行。
25. newWorker.onmessageerror = () => {
26. console.error('workerInstance onmessageerror');
27. };

29. // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行。
30. newWorker.onexit = (e: number) => {
31. // Worker正常退出时，code为0；异常退出时，code为1。
32. console.info('workerInstance onexit code is: ', e);
33. };

35. // 发送消息给Worker线程。
36. newWorker.postMessage('[Main] message from the main thread');
37. })
38. }
39. }
```

```
1. // src/main/ets/workers/LazyImportWorkerPos.ets
2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
3. import { testWithoutObserved } from '../pages/LazyImportFuncPos';

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. // 注册onmessage回调，当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用，在Worker线程执行。
8. workerPort.onmessage = (e: MessageEvents) => {
9. // 调用testWithoutObserved函数。
10. testWithoutObserved();
11. let data: string = e.data;
12. console.info('workerPort onmessage is: ', data);

14. // 向宿主线程发送消息。
15. workerPort.postMessage('[Worker] message from the workerPort');
16. };

18. // 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在Worker线程执行。
19. workerPort.onmessageerror = () => {
20. console.error('workerPort onmessageerror');
21. };

23. // 注册onerror回调，捕获Worker在执行过程中发生的异常，在Worker线程执行。
24. workerPort.onerror = (err: ErrorEvent) => {
25. console.error('workerPort onerror err is: ', err.message);
26. };
```

```
1. // src/main/ets/pages/LazyImportFuncPos.ets
2. // 使用lazy import懒加载包含装饰器的文件。
3. import lazy { innerTest } from './LazyImportObservedPos';

5. export function testWithObserved(): void {
6. innerTest();
7. console.info('ImportObserved::testWithObserved call');
8. }

10. export function testWithoutObserved(): void {
11. console.info('ImportObserved::testWithoutObserved call');
12. }
```

```
1. // src/main/ets/pages/LazyImportObservedPos.ets
2. export function innerTest(): void {
3. console.info('Observed::innerTest call');
4. }

6. @Observed
7. export class Person {
8. public name: string;
9. public age: number;

11. constructor(name: string, age: number) {
12. this.name = name;
13. this.age = age;
14. }
15. }
```

### 装饰器使用隔离

子线程中调用的函数所在的文件中定义了状态管理装饰器，在加载时同样会加载到对应文件，打印ReferenceError报错。由于调用的函数与状态管理装饰器的定义存在于同一文件，使用懒加载的方式无法解决该问题，此时可以将调用函数移出该文件单独定义。

【反例】

```
1. // src/main/ets/pages/DecUseIsolationNeg.ets
2. import { ErrorEvent, worker, MessageEvents } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Button('New Worker')
9. .onClick(() => {
10. // 创建Worker对象。
11. const newWorker = new worker.ThreadWorker('../workers/UseIsolationWorkerNeg.ets');

13. // 注册onmessage回调，捕获宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息。该回调在宿主线程执行。
14. newWorker.onmessage = (e: MessageEvents) => {
15. let data: string = e.data;
16. console.info('newWorker onmessage is: ', data);
17. };

19. // 注册onAllErrors回调，捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常。该回调在宿主线程执行。
20. newWorker.onAllErrors = (err: ErrorEvent) => {
21. console.error('workerInstance onAllErrors message is: ' + err.message);
22. };

24. // 注册onmessageerror回调，当Worker对象接收到无法序列化的消息时被调用，在宿主线程执行。
25. newWorker.onmessageerror = () => {
26. console.error('workerInstance onmessageerror');
27. };

29. // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行。
30. newWorker.onexit = (e: number) => {
31. // Worker正常退出时，code为0；异常退出时，code为1。
32. console.info('workerInstance onexit code is: ', e);
33. };

35. // 发送消息给Worker线程。
36. newWorker.postMessage('[Main] message from the main thread');
37. })
38. }
39. }
```

```
1. // src/main/ets/workers/UseIsolationWorkerNeg.ets
2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
3. import { testWithObserved } from '../pages/UseIsolationFuncNeg';

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. // 注册onmessage回调，当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用，在Worker线程执行。
8. workerPort.onmessage = (e: MessageEvents) => {
9. // 调用testWithObserved函数。
10. testWithObserved();
11. let data: string = e.data;
12. console.info('workerPort onmessage is: ', data);

14. // 向宿主线程发送消息。
15. workerPort.postMessage('[Worker] message from the workerPort');
16. };

18. // 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在Worker线程执行。
19. workerPort.onmessageerror = () => {
20. console.error('workerPort onmessageerror');
21. };

23. // 注册onerror回调，捕获Worker在执行过程中发生的异常，在Worker线程执行。
24. workerPort.onerror = (err: ErrorEvent) => {
25. console.error('workerPort onerror err is: ', err.message);
26. };
```

```
1. // src/main/ets/pages/UseIsolationFuncNeg.ets
2. import { innerTest } from './UseIsolationObservedNeg';

4. export function testWithObserved(): void {
5. innerTest();
6. console.info('ImportObserved::testWithObserved call');
7. }

9. export function testWithoutObserved(): void {
10. console.info('ImportObserved::testWithoutObserved call');
11. }
```

```
1. // src/main/ets/pages/UseIsolationObservedNeg.ets
2. export function innerTest(): void {
3. console.info('Observed::innerTest call');
4. }

6. @Observed
7. export class Person {
8. public name: string;
9. public age: number;

11. constructor(name: string, age: number) {
12. this.name = name;
13. this.age = age;
14. }
15. }
```

【正例】

```
1. // src/main/ets/pages/DecUseIsolationPos.ets
2. import { ErrorEvent, worker, MessageEvents } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Button('New Worker')
9. .onClick(() => {
10. // 创建Worker对象。
11. const newWorker = new worker.ThreadWorker('../workers/UseIsolationWorkerPos.ets');

13. // 注册onmessage回调，捕获宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息。该回调在宿主线程执行。
14. newWorker.onmessage = (e: MessageEvents) => {
15. let data: string = e.data;
16. console.info('newWorker onmessage is: ', data);
17. };

19. // 注册onAllErrors回调，捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常。该回调在宿主线程执行。
20. newWorker.onAllErrors = (err: ErrorEvent) => {
21. console.error('workerInstance onAllErrors message is: ' + err.message);
22. };

24. // 注册onmessageerror回调，当Worker对象接收到无法序列化的消息时被调用，在宿主线程执行。
25. newWorker.onmessageerror = () => {
26. console.error('workerInstance onmessageerror');
27. };

29. // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行。
30. newWorker.onexit = (e: number) => {
31. // Worker正常退出时，code为0；异常退出时，code为1。
32. console.info('workerInstance onexit code is: ', e);
33. };

35. // 发送消息给Worker线程。
36. newWorker.postMessage('[Main] message from the main thread');
37. })
38. }
39. }
```

```
1. // src/main/ets/workers/UseIsolationWorkerPos.ets
2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
3. import { testWithObserved } from '../pages/UseIsolationFuncPos';

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. // 注册onmessage回调，当Worker线程收到来自其宿主线程通过postMessage接口发送的消息时被调用，在Worker线程执行。
8. workerPort.onmessage = (e: MessageEvents) => {
9. // 调用testWithObserved函数。
10. testWithObserved();
11. let data: string = e.data;
12. console.info('workerPort onmessage is: ', data);

14. // 向宿主线程发送消息。
15. workerPort.postMessage('[Worker] message from the workerPort');
16. };

18. // 注册onmessageerror回调，当Worker对象接收到一条无法被序列化的消息时被调用，在Worker线程执行。
19. workerPort.onmessageerror = () => {
20. console.error('workerPort onmessageerror');
21. };

23. // 注册onerror回调，捕获Worker在执行过程中发生的异常，在Worker线程执行。
24. workerPort.onerror = (err: ErrorEvent) => {
25. console.error('workerPort onerror err is: ', err.message);
26. };
```

```
1. // src/main/ets/pages/UseIsolationFuncPos.ets
2. import { innerTest } from './UseIsolationAdditionPos';

4. export function testWithObserved(): void {
5. innerTest();
6. console.info('ImportObserved::testWithObserved call');
7. }

9. export function testWithoutObserved(): void {
10. console.info('ImportObserved::testWithoutObserved call');
11. }
```

```
1. // src/main/ets/pages/UseIsolationAdditionPos.ets
2. // 函数拆分，装饰器使用隔离。
3. export function innerTest(): void {
4. console.info('Addition::innerTest call');
5. }
```

```
1. // src/main/ets/pages/UseIsolationObservedPos.ets
2. @Observed
3. export class Person {
4. public name: string;
5. public age: number;

7. constructor(name: string, age: number) {
8. this.name = name;
9. this.age = age;
10. }
11. }
```
