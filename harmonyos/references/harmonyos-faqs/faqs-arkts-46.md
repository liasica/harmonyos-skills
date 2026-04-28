---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-46
title: 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:01+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:763fbeccedd110fac007c01f01bf82143573917a9d9c9402db494fe7d1733eaa
---

可以利用TaskPool接口转换，具体分为以下四个场景：

* 场景一：主线程将独立任务放到子线程执行。代码示例：

  共享内存写法：

  ```
  1. class Task {
  2. static run(args) {
  3. // Do some independent tasks
  4. }
  5. }
  6. let thread = new Thread(() => {
  7. let result = Task.run(args)
  8. // deal with result
  9. })
  ```

  [TaskPool.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TaskPool.txt#L21-L29)

  ArkTS写法：

  ```
  1. import { taskpool } from '@kit.ArkTS';

  3. @Concurrent
  4. function run(args: number) {
  5. // Do some independent tasks
  6. }
  7. let task: taskpool.Task = new taskpool.Task(run, 100); // 100: test number
  8. taskpool.execute(task).then((res) => {
  9. // Return result
  10. });
  ```

  [TaskPoolContrast.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TaskPoolContrast.ets#L21-L30)
* 场景二：主线程在子线程使用类对象实例。代码示例：

  共享内存写法：

  ```
  1. class Material {
  2. action(args) {
  3. // Do some independent tasks
  4. }
  5. }
  6. let material = new Material()
  7. let thread = new Thread(() => {
  8. let result = material.action(args)
  9. // deal with result
  10. })
  ```

  [TaskPool.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TaskPool.txt#L33-L42)

  ArkTS写法：

  ```
  1. import { taskpool } from '@kit.ArkTS';

  3. @Concurrent
  4. function runner(material: Material): void {
  5. return material.action(100); // 100: test number
  6. }
  7. @Sendable
  8. class Material {
  9. action(args: number) {
  10. // Do some independent tasks
  11. }
  12. }
  13. let material = new Material()
  14. taskpool.execute(runner, material).then((ret) => {
  15. // Return result
  16. })
  ```

  [TaskPoolContrast2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TaskPoolContrast2.ets#L21-L36)
* 场景三：子线程更新主线程状态。代码示例：

  共享内存写法：

  ```
  1. class Task {
  2. run(args) {
  3. // deal with result
  4. runOnUiThread(() => {
  5. UpdateUI(result)
  6. })
  7. }
  8. }
  9. let task = new Task()
  10. let thread = new Thread(() => {
  11. let result = task.run(args)
  12. // Processing results
  13. })
  ```

  [TaskPool.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TaskPool.txt#L46-L58)

  ArkTS写法：

  ```
  1. import taskpool from '@ohos.taskpool'

  3. // let result: Object[] | undefined = undefined

  5. @Concurrent
  6. function runner(task:Task) {
  7. task.run()
  8. }
  9. @Sendable
  10. class Task {
  11. run(args?: Object[] | undefined) {
  12. // Do some independent tasks
  13. taskpool.Task.sendData(JsResult)
  14. }
  15. }
  16. let task = new Task()
  17. let run = new taskpool.Task(runner, task)
  18. run.onReceiveData((result?: Function | undefined) => {
  19. UpdateUI(result)
  20. })
  21. taskpool.execute(run).then((ret) => {
  22. // Return result
  23. })
  ```

  [TaskPoolContrast3.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TaskPoolContrast3.ets#L21-L43)
* 场景四：子线程同步调用主线程接口。代码示例：

  ```
  1. class SdkU3d {
  2. static getInst() {
  3. return SdkMgr.getInst();
  4. }
  5. getPropStr(str: string) {
  6. return xx;
  7. }
  8. }
  9. let thread = new Thread(() => {
  10. // In the game thread
  11. let sdk = SdkU3d.getInst()
  12. let ret = sdk.getPropStr("xx")
  13. })
  ```

  [TaskPool.txt](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/TaskPool.txt#L62-L74)

  ArkTS写法：

  ```
  1. import { MessageEvents, taskpool, worker } from '@kit.ArkTS';
  2. class SdkU3d {
  3. static getInst(): Object {
  4. return SdkMgr.getInst();
  5. }
  6. getPropStr(str: string) { }
  7. }
  8. let workerInstance = new worker.ThreadWorker("xx/worker.ts");
  9. workerInstance.registerGlobalCallObject("instance_xx", SdkU3d.getInst());
  10. workerInstance.postMessage("start");
  11. // In the game worker thread
  12. const mainPort = worker.workerPort;
  13. mainPort.onmessage = (e: MessageEvents): void => {
  14. let ret = mainPort.callGlobalCallObjectMethod("instance_xx", "getPropStr", 100); // 100: test number
  15. }
  ```

  [TaskPoolContrast4.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TaskPoolContrast4.ets#L21-L35)

**参考链接**

[并发概述](../harmonyos-guides/concurrency-overview.md)
