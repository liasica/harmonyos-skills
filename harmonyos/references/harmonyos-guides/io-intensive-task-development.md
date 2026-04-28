---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/io-intensive-task-development
title: I/O密集型任务开发指导 (TaskPool)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 耗时任务并发场景 > I/O密集型任务开发指导 (TaskPool)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:393728130637322138dd966acc6df5882c5c31cd41badfab8aedd4f0bceac083
---

使用异步并发可以解决单次I/O任务阻塞的问题。对于I/O密集型任务，若线程中的其他任务仍可能被阻塞，建议采用多线程并发来处理。

I/O密集型任务的性能关键在于I/O操作的速度和效率，而非CPU的处理能力。这类任务需要频繁进行磁盘读写和网络通信。此处通过频繁读写系统文件来模拟I/O密集型并发任务的处理。

1. 定义并发函数，内部密集调用I/O能力。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';

   3. // 定义并发函数，内部密集调用I/O能力
   4. // 写入文件的实现
   5. export async function write(data: string, filePath: string): Promise<void> {
   6. let file: fileIo.File = await fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   7. await fileIo.write(file.fd, data);
   8. fileIo.close(file);
   9. }
   ```

   ```
   1. import { write } from './write'
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { taskpool } from '@kit.ArkTS';
   4. import { common } from '@kit.AbilityKit';

   6. @Concurrent
   7. async function concurrentTest(context: common.UIAbilityContext): Promise<boolean> {
   8. let filePath1: string = context.filesDir + '/path1.txt'; // 应用文件路径
   9. let filePath2: string = context.filesDir + '/path2.txt';
   10. // 循环写文件操作
   11. let fileList: string[] = [];
   12. fileList.push(filePath1);
   13. fileList.push(filePath2);
   14. const writePromises: Promise<boolean | void>[] = [];
   15. for (let i: number = 0; i < fileList.length; i++) {
   16. const writePromise = write('Hello World!', fileList[i]).then(() => {
   17. console.info(`Succeeded in writing the file. FileList: ${fileList[i]}`);
   18. }).catch((err: BusinessError) => {
   19. console.error(`Failed to write the file. Code is ${err.code}, message is ${err.message}`)
   20. return false;
   21. });
   22. writePromises.push(writePromise);
   23. }
   24. try {
   25. await Promise.all(writePromises);
   26. return true;
   27. } catch (error) {
   28. return false;
   29. }
   30. }
   ```
2. 使用TaskPool执行包含密集I/O的并发函数，通过调用[execute()](../harmonyos-references/js-apis-taskpool.md#taskpoolexecute)方法执行任务，并在回调中处理调度结果。示例中获取filePath1和filePath2的方式请参见[获取应用文件路径](application-context-stage.md#获取应用文件路径)。在TaskPool中使用context时，需先在并发函数外部准备好，并通过参数传递给并发函数。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State message: string = 'Hello World';
   5. uiContext = this.getUIContext();

   7. build() {
   8. Row() {
   9. Column() {
   10. Text(this.message)
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. .onClick(() => {
   14. let context = this.uiContext?.getHostContext() as common.UIAbilityContext;
   15. // 使用TaskPool执行包含密集I/O的并发函数
   16. // 数组较大时，I/O密集型任务分发也会抢占UI主线程，需要使用多线程能力
   17. taskpool.execute(concurrentTest, context).then(() => {
   18. // 调度结果处理
   19. console.info('taskpool: execute success')
   20. })
   21. this.message = 'success';
   22. })
   23. }
   24. .width('100%')
   25. }
   26. .height('100%')
   27. }
   28. }
   ```
