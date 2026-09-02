---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-local-file-and-data-multithreaded-io
title: 多线程操作密集型关系型数据库和文件读写
breadcrumb: 最佳实践 > 应用框架 > 数据和文件 > 多线程操作密集型关系型数据库和文件读写
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:5f0dbf6001ed5c99ed603d18a4e0c1b6df4b455c94fc2a961fbf423eefd8f0fd
---

## 概述

应用中的每个进程都会有一个主线程，主线程主要承担执行UI绘制操作、管理ArkTS引擎实例的创建和销毁、分发和处理事件、管理Ability生命周期等职责，具体可参见[线程模型概述](../harmonyos-guides/thread-model-stage.md)。在主线程中执行耗时操作将会引起UI绘制卡顿，因此，开发应用时应当尽量避免将耗时的操作放在主线程中执行。ArkTS提供了多线程并发能力，多线程并发允许在同一时间段内同时执行多段代码，本文介绍如何利用多线程解决密集型文件和数据库读写时造成主线程阻塞的问题。

## 实现原理

在密集型读写操作时，由于系统会进行大量任务分发和数据拷贝，这两项任务均会阻塞主线程，系统提供了TaskPool和Sendable避免阻塞。

其中，任务池（TaskPool）旨在为应用程序构建多线程运行环境，它具有易用性，并且可以避免对于主线程的占用；Sendable对象则提供了并发实例间高效的通信效率，凭借其引用传递的能力，在多并发实例的数据交互等场景中可避免传统通信方式的效率低下问题，从而进一步提升系统在密集型读写这类复杂场景下的性能表现，为系统的高效稳定运行提供有力支持。

## 使用TaskPool进行读写

本章介绍使用TaskPool进行读写的方案，以及讨论其对于性能的提升。

### 实现原理

任务池（TaskPool）作用是为应用程序提供一个多线程的运行环境，降低整体资源的消耗、提高系统的整体性能，且开发者无需关心线程实例的生命周期。更多原理请详见[TaskPool简介](../harmonyos-guides/taskpool-introduction.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/uYxJ8jSlS0WlYi3tFjUcGA/zh-cn_image_0000002229337461.png "点击放大")

TaskPool在执行密集型I/O读写方面具有以下优势：

1. 自动任务分发：当调用TaskPool执行密集型读写时，其线程池会自动将任务分发到子线程完成，无需人工干预，实现了高效的任务分配流程。
2. 不阻塞主线程：通过在子线程完成任务，有效避免了对主线程的阻塞，确保主线程能够继续执行其他操作，维持系统整体的流畅运行。
3. 资源节约：TaskPool本身通过系统统一线程管理，结合动态调度及负载均衡算法可节约系统资源，这也为执行密集型读写提供了更优的系统资源环境，保障操作的顺利进行。

### TaskPool文件读写

**开发步骤**

1. 封装write()函数，使用@Concurrent进行装饰，执行的并发函数需要使用该装饰器修饰，否则无法通过相关校验。

   ```typescript
   @Concurrent
   function writeFile(fd: number[], content: string, times: number) {
     for (let i: number = 0; i < times; i++) {
       fileIo.write(fd[i], content).catch(() => {
         hilog.error(0x0000, 'FileTaskPool', '%{public}s', 'writeFile error');
       });
     }
   }
   ```
2. 封装read()函数，同样地，也使用@Concurrent进行装饰。在读文件时使用循环读取，这也是大文件读取时常用的方法，使用Array<ArrayBuffer>存储一个大文件中的信息。

   ```typescript
   @Concurrent
   function readFile(fd: number[], path: string, fileName: string, times: number): Array<Array<ArrayBuffer>> {
     let result: Array<Array<ArrayBuffer>> = [];
     for (let i = 0; i < times; i++) {
       let buffSize: number = 4096;
       try {
         let state = fileIo.statSync(path + fileName + JSON.stringify(i) + CommonConstants.FILE_SUFFIX);
         if (state.size === 0){
           return result;
         }
         let buffer: ArrayBuffer = new ArrayBuffer(Math.min(buffSize, state.size));
         let off: number = 0;
         let len: number = fileIo.readSync(fd[i], buffer, { offset: off, length: buffSize });
         let readLen: number = 0;
         let bufferList: Array<ArrayBuffer> = [];
         while (len > 0) {
           readLen += len;
           bufferList.push(buffer);
           off = off + len;
           if ((state.size - readLen) < buffSize) {
             buffSize = state.size - readLen;
           }
           len = fileIo.readSync(fd[i], buffer, { offset: off, length: buffSize });
         }
         result.push(bufferList);
       } catch (error) {
         hilog.error(0x0000, 'FileTaskPool', '%{public}s', 'readFile error');
       }
     }
     return result;
   }
   ```
3. 使用taskpool.execute()执行任务时，传入的第一个参数是调用的函数名，其余参数则是该函数的参数。

   ```typescript
   async write(): Promise<void> {
     try {
       await taskpool.execute(writeFile, this.fd, this.content, this.times);
     } catch (error) {
       hilog.error(0x0000, 'FileTaskPool', '%{public}s', 'write error');
     }
     // ...
     return;
   }

   async read(): Promise<number> {
     try {
       let value = await taskpool.execute(readFile, this.fd, this.path, this.fileName,
         this.times) as object as Array<Array<ArrayBuffer>>;
       // ...
       return value.length;
     } catch (error) {
       hilog.error(0x0000, 'FileTaskPool', '%{public}s', 'read error');
       return 0;
     }
   }
   ```

### TaskPool关系型数据库读写

**开发步骤**

1. 封装关系型数据库的写数据库的函数，使用@Concurrent进行装饰。

   ```typescript
   @Concurrent
   async function insert(context: common.UIAbilityContext, valueBucket: Array<relationalStore.ValuesBucket>,
     config: relationalStore.StoreConfig) {
     try {
       const store = await relationalStore.getRdbStore(context, config);
       store.batchInsert('EMPLOYEE', valueBucket).catch(() => {
         hilog.error(0x0000, 'DatabaseTaskPool', '%{public}s', 'batchInsert error');
       });
     } catch (error) {
       hilog.error(0x0000, 'DatabaseTaskPool', '%{public}s', 'batchInsert error');
     }
   }
   ```
2. 封装数据库读出的函数，使用getRow()和goToNextRow()循环读出符合查询条件的数据，这里读出所有数据。

   ```typescript
   @Concurrent
   async function read(context: common.UIAbilityContext, config: relationalStore.StoreConfig) {
     try {
       const store = await relationalStore.getRdbStore(context, config);
       const predicates = new relationalStore.RdbPredicates('EMPLOYEE');
       const resultSet = store.querySync(predicates);
       let ValuesBucketArray: ValuesBucket[] = [];
       if (resultSet.rowCount === 0) {
         return ValuesBucketArray;
       }
       resultSet.goToFirstRow();
       do {
         const ValuesBucket = resultSet.getRow() as ValuesBucket;
         ValuesBucketArray.push(ValuesBucket);
       } while (resultSet.goToNextRow());
       resultSet.close();
       return ValuesBucketArray;
     } catch (error) {
       hilog.error(0x0000, 'DatabaseTaskPool', '%{public}s', 'batchInsert error');
       return;
     }
   }
   ```
3. taskpool.execute()执行任务。

   ```typescript
   async insertRDB(): Promise<void> {
     try {
       await taskpool.execute(insert, this.context, this.valueBucketArray, STORE_CONFIG);
     } catch (error) {
       hilog.error(0x0000, 'DatabaseTaskPool', '%{public}s', 'insertRDB error');

     }
     return;
   }
   ```

## 使用Sendable进一步提升性能

在上一章节中介绍了如何使用TaskPool进行读写，解决了密集型读写场景下任务分发的的问题，但是实际开发中还面临密集的数据传递问题，系统提供了@Sendable进行解决，本章将介绍如何在TaskPool基础上使用@Sendable。

### 实现原理

为了实现Sendable数据在不同并发实例间的引用传递，Sendable共享对象会分配在共享堆中，以实现跨并发实例的内存共享。数据类型参考[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)。

共享堆（SharedHeap）是进程级别的堆空间，与虚拟机本地堆（LocalHeap）不同的是，LocalHeap只能被单个并发实例访问，而SharedHeap可以被所有线程访问。一个Sendable共享对象的跨线程行为是引用传递。因此，Sendable可能被多个并发实例引用，判断Sendable共享对象是否存活，取决于所有并发实例的对象是否存在对此Sendable共享对象的引用，更多原理请见[Sendable的实现原理](../harmonyos-guides/arkts-sendable.md#sendable的实现原理)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ARkyBLmmTLex4mi6EQIKKA/zh-cn_image_0000002229451953.png)

在密集型I/O处理场景中，文件读写会涉及大量数据的传输，而数据库读写则通常被封装成class进行传递，Sendable用引用代替拷贝，可以有效地降低序列化时间，从而提升性能，Sendable主要可以解决两个场景的问题：

* 跨并发实例传输大数据（例如可能达到100KB以上的数据）。
* 跨并发实例传递带方法的class实例对象。

### 文件读写大数据使用@Sendable传输

**开发步骤**

1. 在使用@Sendable进行文件写入操作时，首先需要定义Sendable对象存放写入数据，然后封装TaskPool函数传入。

   ```typescript
   @Sendable
   class Content {
     content: string;

     constructor(content: string) {
       this.content = content;
     }
   }
   ```

   ```typescript
   @Concurrent
   function writeFile(fd: number[], content: Content, times: number) {
     for (let i: number = 0; i < times; i++) {
       fileIo.write(fd[i], content.content).catch(() => {
         hilog.error(0x0000, 'FileSendable', '%{public}s', 'writeFile error');
       });
     }
   }
   ```
2. 接下来进行读取操作，封装TaskPool函数，需要使用collections.Array代替Array，collections.ArrayBuffer代替ArrayBuffer接收结果值，在使用Sendable时，需要注意该数据类型Sendable是否支持，详情请见[sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)。

   ```typescript
   @Concurrent
   function readFile(fd: number[], path: string, fileName: string,
     times: number): collections.Array<collections.Array<collections.ArrayBuffer>> {
     let result: collections.Array<collections.Array<collections.ArrayBuffer>> =
       new collections.Array<collections.Array<collections.ArrayBuffer>>();
     for (let i = 0; i < times; i++) {
       let buffSize: number = 4096;
       try {
         let state = fileIo.statSync(path + fileName + JSON.stringify(i) + CommonConstants.FILE_SUFFIX);
         if (state.size === 0) {
           return result;
         }
         let buffer: collections.ArrayBuffer = new collections.ArrayBuffer(Math.min(buffSize, state.size));
         let off: number = 0;
         let len: number = fileIo.readSync(fd[i], buffer as ArrayBuffer, { offset: off, length: buffSize });
         let readLen: number = 0;
         let bufferList: collections.Array<collections.ArrayBuffer> = new collections.Array<collections.ArrayBuffer>();
         while (len > 0) {
           readLen += len;
           bufferList.push(buffer);
           off = off + len;
           if ((state.size - readLen) < buffSize) {
             buffSize = state.size - readLen;
           }
           len = fileIo.readSync(fd[i], buffer as ArrayBuffer, { offset: off, length: buffSize });
         }
         result.push(bufferList);
       } catch (error) {
         hilog.error(0x0000, 'FileSendable', '%{public}s', 'readFile error');
       }
     }
     return result;
   }
   ```
3. taskpool.execute()执行任务。

   ```typescript
   async write(): Promise<void> {
     try {
       await taskpool.execute(writeFile, this.fd, this.content, this.times);
     } catch (error) {
       hilog.error(0x0000, 'FileSendable', '%{public}s', 'execute error');
     }
     // ...
     return;
   }

   async read(): Promise<number> {
     try {
       let value = await taskpool.execute(readFile, this.fd, this.path, this.fileName,
         this.times) as collections.Array<collections.Array<collections.ArrayBuffer>>;
       // ...
       return value.length;
     } catch (error) {
       hilog.error(0x0000, 'FileSendable', '%{public}s', 'read error');
       return 0;
     }
   }
   ```

### 关系型数据库读写使用@Sendable

**开发步骤**

1. 在关系型数据库写入操作时，同样需要封装写入数据使用@Sendable进行装饰，传入TaskPool函数中。

   ```typescript
   @Sendable
   class SharedValuesBucket {
     NAME: string;
     AGE: number;
     SALARY: number;

     constructor(NAME: string, AGE: number, SALARY: number) {
       this.NAME = NAME;
       this.AGE = AGE;
       this.SALARY = SALARY;
     }
   }
   ```

   ```typescript
   @Concurrent
   async function insert(context: common.UIAbilityContext, valueBucket: Array<SharedValuesBucket>,
     config: relationalStore.StoreConfig) {
     try {
       const store = await relationalStore.getRdbStore(context, config);
       store.batchInsert('EMPLOYEE', valueBucket as object as Array<relationalStore.ValuesBucket>).catch(() => {
         hilog.error(0x0000, 'SharedValuesBucket', '%{public}s', 'batchInsert error');
       });
     } catch (error) {
       hilog.error(0x0000, 'SharedValuesBucket', '%{public}s', 'batchInsert error');
     }
   }
   ```
2. 在读取时，关系型数据库模块提供了getSendableRow()可以直接获取当前行数据的Sendable形式。

   ```typescript
   @Concurrent
   async function read(context: common.UIAbilityContext, config: relationalStore.StoreConfig) {
     try {
       const store = await relationalStore.getRdbStore(context, config);
       const predicates = new relationalStore.RdbPredicates('EMPLOYEE');
       const resultSet = store.querySync(predicates);
       let ValuesBucketArray: sendableRelationalStore.ValuesBucket[] = [];
       if (resultSet.rowCount === 0) {
         return ValuesBucketArray;
       }
       resultSet.goToFirstRow();
       do {
         const ValuesBucket = resultSet.getSendableRow();
         ValuesBucketArray.push(ValuesBucket);
       } while (resultSet.goToNextRow());
       resultSet.close();
       return ValuesBucketArray;
     } catch (error) {
       hilog.error(0x0000, 'SharedValuesBucket', '%{public}s', 'read error');
       return;
     }
   }
   ```
3. taskpool.execute()执行任务。

   ```typescript
   async insertRDB(): Promise<void> {
     try {
       await taskpool.execute(insert, this.context, this.valueBucketArray, STORE_CONFIG);
     } catch (error) {
       hilog.error(0x0000, 'SharedValuesBucket', '%{public}s', 'insertRDB error');
     }
     return;
   }

   async readRDB(): Promise<number> {
     try {
       let value = await taskpool.execute(read, this.context, STORE_CONFIG) as sendableRelationalStore.ValuesBucket[];
       return value.length;
     } catch (error) {
       hilog.error(0x0000, 'SharedValuesBucket', '%{public}s', 'readRDB error');
       return 0;
     }
   }
   ```

## 示例代码

* [基于Taskpool和@Sendable的关系型数据库和文件读写](https://gitcode.com/harmonyos_samples/MultiThreadIO/tree/master)
