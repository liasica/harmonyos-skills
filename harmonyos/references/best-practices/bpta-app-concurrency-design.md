---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-concurrency-design
title: 应用并发设计
breadcrumb: 最佳实践 > 应用框架 > ArkTS语言 > 应用并发设计
category: best-practices
scraped_at: 2026-04-29T14:10:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:25f6aade2c9349667593f0bf1c829a1115690618fb18dac911a8bb9da0c8cac4
---

## 概述

ArkTS是HarmonyOS APP的开发语言，它在保持TypeScript（简称TS）基本语法风格的基础上，一方面规范强化静态检查提升开发者代码的规范性；另一方面基于TypeScript增强了一些特性提升开发体验和执行效率，尤其是在并发能力上的提升。

本文档主要面向HarmonyOS APP的设计人员或开发人员，介绍应用在并行任务方案设计过程中，可能会遇到的典型场景以及对应的推荐设计方案，同时给出了方案的关键点及参考案例。

## 典型业务场景

根据当前HarmonyOS APP开发过程中遇到的实际并发业务场景，总结提炼出如下典型场景，可供更多APP参考，设计其并发业务方案。

|  |  |  |  |
| --- | --- | --- | --- |
| 场景编号 | 场景分类 | 场景名称 | 简述 |
| 1 | 并发能力选择 | [耗时任务并发执行场景](bpta-app-concurrency-design.md#section15392153922413) | 相对独立的耗时任务放到单独的子线程中执行，推荐TaskPool |
| 2 | [常驻任务并发执行场景](bpta-app-concurrency-design.md#section76941238135110) | 常驻的耗时任务放到单独的子线程中执行，推荐Worker |
| 3 | [传统共享内存并发业务](bpta-app-concurrency-design.md#section196265243512) | 开发共享内存并发业务，推荐TaskPool和Worker的API |
| 4 | [长时任务并发执行场景](bpta-app-concurrency-design.md#section484614505514) | 长时间运行的任务不独占线程执行，推荐TaskPool长时任务 |
| 5 | 并发任务管理 | [多任务关联执行（串行顺序依赖）](bpta-app-concurrency-design.md#section843404931116) | 有顺序的任务不希望并发执行 |
| 6 | [多任务关联执行（树状依赖）](bpta-app-concurrency-design.md#section154701412191218) | 任务存在依赖关系，等待依赖执行完再调度 |
| 7 | [多任务同步等待结果（任务组）](bpta-app-concurrency-design.md#section13759133112128) | 多个任务等待全部结果返回后再进行后续操作 |
| 8 | [多任务优先级调度](bpta-app-concurrency-design.md#section873704510120) | 设置不同任务的优先级 |
| 9 | [任务延时调度](bpta-app-concurrency-design.md#section18304175813129) | 任务延时调度 |
| 10 | 线程间通信 | [同语言线程间通信（ArkTS内）](bpta-app-concurrency-design.md#section35851753051) | 介绍ArkTS线程间通信机制 |
| 11 | [跨语言多线程通信（C++与ArkTS）](bpta-app-concurrency-design.md#section101785720619) | 介绍C++与ArkTS线程间通信机制 |
| 12 | [线程间模块共享（单例模式）](bpta-app-concurrency-design.md#section19259192873) | 介绍进程内单例场景 |
| 13 | [线程间不可变数据共享](bpta-app-concurrency-design.md#section154816558122) | 介绍不可变数据共享场景 |
| 14 | [生产者与消费者模式](bpta-app-concurrency-design.md#section9833163071612) | 介绍生产者与消费者模式 |

## 并发能力整体架构

### 并发能力概述

并发能力框架如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BKVW_pTvQX60duqgZ1RvuQ/zh-cn_image_0000002194011076.png?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=6D796BE2A8A503773FC5EF31CA613D9D87F24E8A846EEDD0A88A40F9ACE373DA "点击放大")

* **主线程：**执行UI业务、不耗时操作、单次I/O任务，与其他ArkTS线程共享系统I/O线程池，不阻塞ArkTS线程。
* **TaskPool****高并发任务池：**执行耗时任务，封装任务入口，统计模块负载，开发者无需管理线程生命周期。
* **Worker****线程：**执行常驻任务，CPU密集型、耗时任务，限制线程个数为64。
* **FFRT****任务池：**
  1. 系统任务，如异步I/O任务，由系统分发到FFRT线程，开发者无需关注。
  2. 用户任务：开发者创建的C/C++耗时任务，支持负载均衡及线程生命周期管理。
* **Pthread****线程：**采用C/C++开发的模块，后台运行或耗时的ArkTS无关业务，不限制线程个数。

## 并发模型与业界模型的差异

### 共享内存并发模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Oxh-FxCUQJa4a7DxDpWVmQ/zh-cn_image_0000002194011072.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=2FE63672390F670D47788E5EB72B613F7981AB24CC67CF9ECB8417F349B8543E "点击放大")

共享内存模型采用线程和锁的并发机制，不同线程共享内存并通过锁保护临界区。对于包含I/O操作或锁的业务，为防止阻塞，需开启多个线程执行不同业务。线程情况如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/31DtrlTITlCRqtArEW3H3Q/zh-cn_image_0000002194011068.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=FFDCB4EFF87386FFF426835DF242A6D02CCBF84EDDCA805C2F8D2FEB8F67F9AA "点击放大")

因此，应用经常存在几百个线程，增加调度开销和内存占用。

### ArkTS并发模型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/rIwFxN9yTJiUfcUAQJ139w/zh-cn_image_0000002194011084.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=F9D9D7103DA62E78A7C53F1A1F826AEE5C0001D9F60380031D23C3BACE3207F6 "点击放大")

ArkTS采用内存隔离的线程模型，不同线程间通过消息通信，线程内无锁化运行。业务内部的I/O操作由系统分发到后台的I/O任务池，不阻塞ArkTS上层逻辑，线程情况如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/8NfihLEhQx2HX3pbyc7EhQ/zh-cn_image_0000002229336865.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=4A6012CD2265E16BEE1CA5C5EDA9A39CA01AAFDC84350070B94E6E6B4F4C8BB1 "点击放大")

异步I/O不阻塞ArkTS线程，TaskPool及I/O线程池由系统管理，提升能效。

ArkTS语言支持了TaskPool和Worker的并发能力，接下来简单介绍TaskPool和Worker的功能。

TaskPool的运作机制可参考[TaskPool简介](../harmonyos-guides/taskpool-introduction.md)，TaskPool提供任务分发入口，支持分发任务到不同优先级队列。TaskPool底层管理一定数量的工作线程，从队列获取任务执行。工作线程根据任务数量及线程数量自动扩缩容，保证执行效率。工作线程容量无法无限制扩充，上限数量为核心数减1。

Worker的运作机制可参考[Worker简介](../harmonyos-guides/worker-introduction.md)，空任务的Worker线程的内存占用大约2MB左右，因此需要控制线程的数量，避免内存过大。

### ArkTS与传统共享内存并行化的差异

通过并发模型对比，ArkTS中的异步I/O操作分发到I/O任务池，不阻塞执行。Java需大量线程进行阻塞I/O操作，导致线程数较多。

ArkTS采用内存隔离的并发模型，不支持跨线程共享对象，必须进行线程间数据通信。Java可以直接访问不同线程的对象，但需要使用锁确保数据的线程安全。

## 并发能力选择

### 概述

不同的业务场景使用不同的并发能力，本章对常见场景进行分类，介绍各类场景的HarmonyOS APP开发方案。

### 耗时任务并发执行场景

* **场景描述**

  在应用业务实现过程中，对于相对独立的耗时任务，如果在主线程中执行会阻塞主线程的UI业务，导致卡顿丢帧等问题，影响用户体验。需要将这些独立的耗时任务放到单独的子线程中执行。典型的耗时任务包括CPU密集型任务、I/O密集型任务和同步任务。

  常见的业务场景如下所示：

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 | | |
  | CPU密集型 | I/O密集型 | 同步任务 |
  | 图片/视频编解码 | 将图片或视频进行编解码再展示 | **√** | **√** | **×** |
  | 压缩/解压缩 | 对本地压缩包进行解压操作，或者本地文件的压缩操作 | **√** | **√** | **×** |
  | JSON解析 | 对JSON字符串的序列化和反序列化操作 | **√** | **×** | **×** |
  | 模型运算 | 对数据进行模型运算分析等 | **√** | **×** | **×** |
  | 网络下载 | 密集网络请求下载资源、图片、文件等 | **×** | **√** | **×** |
  | 数据库操作 | 将聊天记录、页面布局信息、音乐列表信息等保存到数据库，或者应用二次启动时，读取数据库展示相关信息 | **×** | **√** | **×** |

  上述业务场景均为独立的耗时任务，任务执行周期短，与外部交互较少，仅包含有限的输入和输出。这些任务可以分发到后台线程执行，再获取结果。使用TaskPool可以简化开发工作量，避免管理复杂的生命周期，防止线程泛滥。开发者只需将这些独立任务放入TaskPool队列，等待结果即可。
* **实现方案介绍**

  ArkTS提供了任务池（TaskPool）的并发能力，可以将独立的耗时任务分发到子线程中执行，满足上述业务场景并行化执行的诉求，开发者只需要如下三个步骤即可完成任务并发编程。实现方案介绍：

  步骤一：将需要在子线程执行的任务封装成一个@Concurrent修饰的函数。

  步骤二：通过TaskPool的任务执行接口将任务分发到子线程。

  步骤三：异步执行结束后在宿主线程接收结果，进行后续处理。
* **业务实现中的关键点**
  1. TaskPool中执行的任务需要考虑通信开销。

     由于TaskPool采用内存隔离的并发模型，对象跨线程传输存在性能开销，需控制线程间传递对象的大小及交互频率（200 KB的典型耗时约1 ms）。
  2. TaskPool中执行的任务不能因阻塞导致执行时间过长（非异步任务的执行时间不应超过3分钟）。

     执行时间超过3分钟的任务会占据任务池中的线程，导致其他任务无法调度，因此系统会回收这些任务。

     网络下载、文件访问等异步I/O操作由系统分发到I/O线程池，不受上述规则约束。
  3. TaskPool中执行的任务不能有上下文依赖。

     TaskPool任务在子线程中执行，与宿主线程上下文环境不同，因此需确保任务的独立性，内部实现的依赖应通过参数传入或通过[ArkTS模块化](../harmonyos-guides/arkts-runtime-module.md)导入的方式完成。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';

  5. // ...
  6. @Concurrent
  7. async function foo(a: number, b: number) {
  8. return a + b;
  9. }

  11. function executeTaskPool() {
  12. taskpool.execute(foo, 1, 2).then((ret: Object) => { // Result processing
  13. hilog.info(DOMAIN, TAG, FORMAT, 'Return:' + ret);
  14. }).catch((err: BusinessError) => {
  15. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  16. });
  17. }
  ```

  [ConcurrencyCapabilitySelection1.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrencyCapabilitySelection1.ets#L20-L42)
* **与业界方案特殊差异说明**

  业界均采用线程池方案，与TaskPool无特殊差异。
* **不推荐应用实现方式**

  不建议用Worker实现独立的耗时任务。

### 常驻任务并发执行场景

* **场景描述**

  在应用业务实现过程中，对于长耗时（大于3分钟）且并发量较小的常驻任务场景，使用Worker在后台线程中运行这些耗时逻辑，避免阻塞主线程而导致丢帧卡顿等影响用户体验的问题。

  常驻任务不是指可以在后台保活运行的任务，而是指相比于短时任务，运行时间更长的任务，其生命周期可能与主线程一致。

  常见的业务场景如下所示：

  |  |  |  |
  | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 |
  | 游戏中台场景 | 启动子线程作为游戏业务的主逻辑线程，UI线程只负责渲染 | 常驻任务 |
  | 产线硬件压测 | 需要阻塞调用硬件能力，做老化测试，阻塞式 | 阻塞任务 |
* **实现方案介绍**

  ArkTS提供了Worker的并发能力，支持Worker线程与宿主线程之间进行通信，开发者需要主动创建或关闭Worker线程。实现方案介绍：

  步骤一：创建Worker对象；

  步骤二：在Worker线程中绑定Worker对象，并处理需要在子线程执行的逻辑；

  步骤三：宿主线程可以与子线程双向通信，处理数据。
* **业务实现中的关键点**
  1. Worker的生命周期需要开发者自行维护

     由于Worker一旦创建不会主动销毁，若不处于任务状态会持续运行，这会导致资源浪费。因此，需要及时关闭空闲的Worker。
  2. 同时运行的Worker子线程数量限制为64个。
  3. Worker的一些监听事件的回调

     onmessage是宿主线程接收来自其创建的Worker发送的消息时被调用的事件处理程序，处理程序在宿主线程中执行。

     onerror表示Worker执行过程中发生异常时被调用的事件处理程序，该处理程序在宿主线程中执行。

     onmessageerror表示当Worker对象接收到无法序列化的消息时，在宿主线程中执行的事件处理程序。

     onexit表示Worker销毁时的事件处理程序，该处理程序在宿主线程中执行。
* **参考链接**

  [@ohos.worker (启动一个Worker)](../harmonyos-references/js-apis-worker.md)
* **与业界方案特殊差异说明**

  与业界方案一致，均采用独立线程执行常驻任务。
* **不推荐应用实现方式**

  常驻任务不建议作为任务分发给TaskPool。

### 传统共享内存并发业务

* **场景描述**

  在当前的HarmonyOS应用开发过程中，多数应用是通过共享内存模型语言（如Java）开发的原型应用迁移过来的。其中，并发多线程是差异较大的部分，开发者在应用初期调研阶段需要考虑并发的差异，并设计应用的架构。
* **实现方案介绍**

  ArkTS语言的并发多线程开发，推荐使用TaskPool和Worker的API进行开发。

  TaskPool适用于独立任务，任务在线程中执行，无需关注线程生命周期。为了线程池调度效率，不建议执行常驻任务。

  Worker适用于长时间占据线程的任务，需要主动管理线程生命周期。
* **业务实现中的关键点**

  应用开发时，若不频繁进行I/O操作，无需开启独占线程。

  在并发场景下，注意内存隔离线程模型的差异，确保子线程任务独立，减少与外部的数据交互，降低性能开销。

  如果需要使用内存共享，可以通过Node-API到C++层进行，或定义Sendable对象实现线程间数据共享。
* **与业界方案特殊差异说明**

  Java上的并发多使用内存共享的跨线程对象访问。HarmonyOS APP开发时，注意内存隔离线程模型差异。
* **不推荐应用实现方式**

  控制并发任务的粒度，避免频繁跨线程交互。

### 长时任务并发执行场景

* **场景描述**

  在应用业务实现过程中，对于需要长时间运行的独立耗时任务，如果放在主线程中执行会阻塞UI业务，导致卡顿和丢帧，影响用户体验。应将这个独立的长时任务放到单独的子线程中执行。

  典型的长时任务场景如下所示：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | 定期传感器数据采集 | 周期性采集一些传感器信息（例如位置信息、速度传感器等），应用运行阶段常驻运行。 |
  | Socket端口信息监听 | 长时间监听Socket数据，不定时需要响应处理。 |

  上述业务场景均为独立的长时任务，每个任务的执行周期较长，与外部的交互较为简单。将这些任务分发到后台线程后，需要不定期响应以获取结果。使用TaskPool可以简化开发工作量，避免管理复杂的生命周期和线程泛滥。开发者只需将独立的长时任务放入TaskPool队列，然后等待结果即可。
* **实现方案介绍**

  ArkTS提供了任务池（TaskPool）的并发能力，可以将长时间任务分发到子线程中执行，满足上述业务场景并行化执行的需求。开发者只需以下三个步骤即可完成任务并发编程。实现方案如下：

  第一步：将需要在子线程执行的任务封装成一个@Concurrent修饰的函数；

  第二步：通过TaskPool的长时任务执行接口将任务分发到子线程；

  第三步：任务执行过程中，不定期接收数据，返回给宿主线程处理。
* **业务实现中的关键点**

  长时任务与阻塞任务不同，它运行周期较长，但每次执行不会长时间阻塞线程。因此，不建议将需要独占线程的任务封装为长时任务。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';
  4. const DOMAIN = 0x0000;
  5. const TAG = 'ConcurrencyCapabilitySelection2';
  6. const FORMAT = '%{public}s';
  7. @Concurrent
  8. async function foo() {
  9. try {
  10. // Long listening and other tasks
  11. taskpool.Task.sendData();
  12. } catch (err) {
  13. hilog.error(0x0000, 'TAG', '%{public}s', `sendData failed. Cause code: ${err.code},message: ${err.message}`);
  14. }
  15. }

  17. function executeTaskPool() {
  18. let longTask: taskpool.LongTask = new taskpool.LongTask(foo);
  19. longTask.onReceiveData((msg: Object) => {
  20. // Listening callback
  21. hilog.info(DOMAIN, TAG, FORMAT, `onReceiveData, ${msg}`);
  22. });

  24. taskpool.execute(longTask).then(() => {
  25. hilog.info(DOMAIN, TAG, FORMAT, 'execute success');
  26. }).catch((err: BusinessError) => {
  27. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  28. });
  29. }
  ```

  [ConcurrencyCapabilitySelection2.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrencyCapabilitySelection2.ets#L20-L50)
* **与业界方案特殊差异说明**

  业界通常使用单独的线程池，HarmonyOS使用可调度的任务。
* **不推荐应用实现方式**

  对于非驻留的长期任务，不建议使用Worker实现。

  说明

  长时任务是指长时间不间断运行的独立任务，例如监听某个事件，发起执行后不会再接收发起方的输入。虽然也可以使用Worker（推荐用于常驻后台任务），但更推荐使用TaskPool，因为TaskPool更方便且资源消耗更低。[TaskPool和Worker的实现特点对比](../harmonyos-guides/taskpool-vs-worker.md#实现特点对比)。

## 并发任务管理

### 概述

目前已提供多种任务执行方式，可以管理任务的执行顺序和优先级。本章节将对需要控制任务执行方式的场景进行分类，并分别介绍各类任务执行场景下的HarmonyOS APP开发方案设计。

### 多任务关联执行（串行顺序依赖）

* **场景描述**

  在应用业务实现过程中，使用串行队列机制，使多个任务按特定顺序依次执行，避免并发和乱序。串行队列确保任务执行顺序与数据一致性，防止多线程竞争和死锁，简化多线程编程，适用于后置任务依赖前置任务的场景。

  常见的业务场景如下所示：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | API执行队列 | 调用模块接口，存在执行顺序要求 |
  | 渲染指令队列 | 操作DOM树、渲染等，需要按顺序执行 |
  | 启动时遍历程序包 | 启动遍历小程序包、清理包、资源加载等串行操作 |
* **实现方案介绍**

  ArkTS 提供串行队列（SequenceRunner）功能，可以将多个任务加入到串行队列中，使任务按顺序执行。此外，还可以创建多组串行队列进行分组管理，以满足上述场景的串行执行需求。以下步骤介绍了如何创建和执行串行任务队列。

  步骤一：创建需要串行执行的任务task\_1 ~ task\_n；

  步骤二：创建串行队列runner；

  步骤三：按照需要执行的顺序，依次将任务添加至runner内。
* **业务实现中的关键点**
  1. 添加到串行队列的任务，不支持添加依赖addDependency；

     额外添加的任务依赖可能导致串行队列冲突，即使添加的依赖本身遵循串行队列顺序也会被拦截。
  2. 添加到串行队列的任务，同样也受TaskPool执行任务的约束与限制；

     当串行队列任务执行失败或被取消时，后续任务仍会执行。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';
  4. // ...
  5. @Concurrent
  6. function additionDelay(delay: number): void {
  7. let start: number = new Date().getTime();
  8. while (new Date().getTime() - start < delay) {
  9. continue;
  10. }
  11. }

  13. @Concurrent
  14. function waitForRunner(resString: string): string {
  15. return resString;
  16. }

  18. async function seqRunner() {
  19. let result: string = '';
  20. let task1: taskpool.Task = new taskpool.Task(additionDelay, 300);
  21. let task2: taskpool.Task = new taskpool.Task(additionDelay, 200);
  22. let task3: taskpool.Task = new taskpool.Task(additionDelay, 100);
  23. let task4: taskpool.Task = new taskpool.Task(waitForRunner, 50);

  25. let runner: taskpool.SequenceRunner = new taskpool.SequenceRunner();
  26. runner.execute(task1).then(() => {
  27. result += 'a';
  28. }).catch((err: BusinessError) => {
  29. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  30. });

  32. runner.execute(task2).then(() => {
  33. result += 'b';
  34. }).catch((err: BusinessError) => {
  35. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  36. });

  38. runner.execute(task3).then(() => {
  39. result += 'c';
  40. }).catch((err: BusinessError) => {
  41. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  42. });

  44. await runner.execute(task4).catch((err: BusinessError) => {
  45. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  46. });
  47. hilog.info(DOMAIN, TAG, FORMAT, 'SequenceRunner: result is :' + result);
  48. }
  ```

  [ConcurrentTaskManagement1.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrentTaskManagement1.ets#L20-L71)
* **与业界方案特殊差异说明**

  对于串行队列中任务执行失败后的处理，业界尚无统一规范。

  当前HarmonyOS APP开发中，即使某个任务执行失败，后续任务仍然会继续执行。如果后续任务依赖上一个任务的结果输出，开发者需考虑任务失败场景的异常处理。

### 多任务关联执行（树状依赖）

* **场景描述**

  任务依赖机制用于管理并发任务的执行顺序。通过任务依赖，可以指定一个任务在另一个任务完成后才能执行，从而构建复杂的任务执行流程。任务依赖帮助开发者控制任务间的依赖关系，确保任务按预期顺序执行。在TaskPool中，任务依赖通过调用[addDependency()](../harmonyos-references/js-apis-taskpool.md#adddependency11)和[removeDependency()](../harmonyos-references/js-apis-taskpool.md#removedependency11)方法实现。

  常见的业务场景如下所示：

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 | | |
  | CPU密集型 | I/O密集型 | 同步任务 |
  | 图片解码 | 解析一张大图，将大图数据拆成n份并放到n个任务中执行，执行完后通过这n个任务都依赖的一个任务对结果进行处理并返回 | **√** | **√** | **×** |
  | 数据库操作 | A任务执行需要B任务执行结果。B任务执行完将结果更新到数据库，再执行依赖B的A任务，A任务从数据库中获取B任务结果 | **×** | **√** | **×** |
  | 网络下载 | A任务下载数据，B任务对数据进行处理。B任务执行依赖A任务结果 | **×** | **√** | **×** |
* **实现方案介绍**

  TaskPool提供[addDependency()](../harmonyos-references/js-apis-taskpool.md#adddependency11)和[removeDependency()](../harmonyos-references/js-apis-taskpool.md#removedependency11)两个接口，用于设置任务的依赖关系。默认情况下，任务不依赖其他任务。

  TaskPool维护任务依赖关系列表，调用[addDependency()](../harmonyos-references/js-apis-taskpool.md#adddependency11)/[removeDependency()](../harmonyos-references/js-apis-taskpool.md#removedependency11)更新列表。任务执行前查询列表，若任务依赖其他任务，则等待依赖任务完成；若任务被其他任务依赖，任务执行结束将依赖任务加入队列。
* **业务实现中的关键点**
  1. 合理设置任务依赖关系。如果两个任务的执行不依赖对方的结果，则无需设置依赖关系。
  2. 设置依赖关系时，应确保高优先级任务不依赖于低优先级任务，以防止高优先级任务的优先级设置失效。
  3. 任务依赖与任务组、串行队列的交互表现如下：

     - 已经执行过的任务不能设置依赖关系。

     - 任务组中的任务不能设置依赖关系。

     - 串行队列中的任务不能设置依赖关系。

     - 具有依赖关系的任务执行结束后不能再次执行。

     - 具有依赖关系的任务不能放入任务组。

     - 具有依赖关系的任务不能放入串行队列。
* **案例参考**

  ```
  1. import { taskpool } from '@kit.ArkTS';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError } from '@kit.BasicServicesKit';

  5. // ...
  6. @Concurrent
  7. function updateSAB(args: Uint32Array) {
  8. if (args[0] == 0) {
  9. args[0] = 100;
  10. return 100;
  11. } else if (args[0] == 100) {
  12. args[0] = 200;
  13. return 200;
  14. } else if (args[0] == 200) {
  15. args[0] = 300;
  16. return 300;
  17. }
  18. return 0;
  19. }

  21. function executeTaskPool() {
  22. let sab = new SharedArrayBuffer(20);
  23. let typedArray = new Uint32Array(sab);
  24. let task1 = new taskpool.Task(updateSAB, typedArray);
  25. let task2 = new taskpool.Task(updateSAB, typedArray);
  26. let task3 = new taskpool.Task(updateSAB, typedArray);
  27. try {
  28. task1.addDependency(task2);
  29. task2.addDependency(task3);
  30. } catch (err) {
  31. hilog.error(DOMAIN, TAG, FORMAT, `sendData failed. Cause code: ${err.code},message: ${err.message}`);
  32. }

  34. taskpool.execute(task1).then((res: object) => {
  35. hilog.info(DOMAIN, TAG, FORMAT, 'taskpool:: execute task1 res: ' + res);
  36. }).catch((err: BusinessError) => {
  37. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  38. });

  40. taskpool.execute(task2).then((res: object) => {
  41. hilog.info(DOMAIN, TAG, FORMAT, 'taskpool:: execute task2 res: ' + res);
  42. }).catch((err: BusinessError) => {
  43. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  44. });

  46. taskpool.execute(task3).then((res: object) => {
  47. hilog.info(DOMAIN, TAG, FORMAT, 'taskpool:: execute task3 res: ' + res);
  48. }).catch((err: BusinessError) => {
  49. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  50. });
  51. }
  ```

  [ConcurrentTaskManagement2.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrentTaskManagement2.ets#L20-L75)
* **与业界方案特殊差异说明**

  业界实现的多数任务依赖机制，与TaskPool提供的任务依赖机制表现无明显差异。

### 多任务同步等待结果（任务组）

* **场景描述**

  多个任务并发执行，所有任务完成后统一返回完整结果。若任意任务失败或取消，整个任务结果将失败。

  |  |  |  |
  | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 |
  | 图片解析生成直方图 | 一张图片，为了并发加速，拆分成多个ArrayBuffer进行解析，在所有任务解析完成后统一返回结果将解析结果拼成一个完整的直方图进行渲染 | CPU密集型 |
* **实现方案介绍**

  任务组能力目前通过TaskPool模块提供，以图片生成直方图为例进行介绍。

  步骤一：定义并发函数（@Concurrent function），将承载图片数据的ArrayBuffer的解析逻辑封装在一个并发函数中；

  步骤二：遍历ArrayBuffer，每个ArrayBuffer对应构造一个并发解析任务，将这些任务都添加到任务组中；

  步骤三：通过TaskPool执行任务组，并在回调函数中执行直方图的拼接逻辑或异常处理逻辑。
* **业务实现中的关键点**
  1. 任务组任务应达成统一目的，输出统一结果。
  2. 任务组的结果在所有任务执行结束后统一返回，因此需要先执行完的任务优先处理的场景不要使用任务组。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';

  5. // ...
  6. // Define asynchronous tasks
  7. @Concurrent
  8. function imageProcessing(arrayBuffer: ArrayBuffer): ArrayBuffer {
  9. // Here add business logic, the input is ArrayBuffer, and the output is an ArrayBuffer storing the parsed results.
  10. let message: ArrayBuffer = arrayBuffer;
  11. return message;
  12. }

  14. let taskGroup: taskpool.TaskGroup = new taskpool.TaskGroup();
  15. let TASK_POOL_CAPACITY: number = 10;

  17. function histogramStatistic(pixelBuffer: ArrayBuffer): void {
  18. // Add tasks to the task group
  19. let byteLengthOfTask: number = pixelBuffer.byteLength / TASK_POOL_CAPACITY;
  20. for (let i = 0; i < TASK_POOL_CAPACITY; i++) {
  21. let dataSlice: ArrayBuffer = (i === TASK_POOL_CAPACITY - 1) ? pixelBuffer.slice(i * byteLengthOfTask) :
  22. pixelBuffer.slice(i * byteLengthOfTask, (i + 1) * byteLengthOfTask);
  23. let task: taskpool.Task = new taskpool.Task(imageProcessing, dataSlice);
  24. try {
  25. taskGroup.addTask(task);
  26. } catch (err) {
  27. hilog.error(DOMAIN, TAG, FORMAT, `addTask failed. Cause code: ${err.code},message: ${err.message}`);
  28. }
  29. }
  30. try {
  31. taskpool.execute(taskGroup, taskpool.Priority.HIGH).then((res: Object[]): void | Promise<void> => {
  32. // Result data processing
  33. hilog.info(DOMAIN, TAG, FORMAT, `res:${res}`);
  34. }).catch((error: BusinessError) => {
  35. hilog.error(DOMAIN, TAG, FORMAT, `taskpool excute error: ${error}`);
  36. });
  37. } catch (error) {
  38. hilog.error(DOMAIN, TAG, FORMAT, `taskpool excute error: ${error}`);
  39. }
  40. }
  ```

  [ConcurrentTaskManagement3.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrentTaskManagement3.ets#L20-L63)

### 多任务优先级调度

* **场景描述**

  优先级反映了任务在当前业务场景下的重要性。在并发场景中，系统和线程池的资源是有限的。在资源固定的情况下，系统会优先分配更多资源处理高优先级任务，确保这些任务的即时性，而低优先级任务的调度会相应延迟。TaskPool 提供了多任务优先级调度机制，帮助开发者根据业务需求合理设置优先级。

  常见的业务场景如下所示：

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 | | |
  | CPU密集型 | I/O密集型 | 即时性 |
  | 处理高分辨率图片数据，处理时间约为500毫秒 | 拍摄输入或美化图片时，会将图片数据放在TaskPool中处理，并需要在一定毫秒内将数据返回主线程渲染。为保证任务的即时性，避免影响用户体验，可以设置高优先级使任务被优先调度。 | **√** | **×** | **√** |
  | 日志落盘 | 将业务日志信息写到文件或数据库中，优先级较低。 | **×** | **√** | **×** |
* **实现方案介绍**

  TaskPool提供四种优先级属性：HIGH、MEDIUM、LOW 和 IDLE。

  目前，仅taskpool.Task支持优先级属性设置，function类型不支持。默认优先级为MEDIUM。开发者可通过taskpool.execute()接口显式指定优先级。

  TaskPool 对高、中、低优先级任务的调度比例为 5:5:1。具体来说，每调用 5 个高优先级任务后会调用 1 个中优先级任务，每调用 5 个中优先级任务后会调用 1 个低优先级任务。通过配置这一比例关系，确保高优先级任务优先执行，同时中优先级任务得到合理调度，低优先级任务不会被忽略。

  优先级机制与QoS（quality-of-service）底层对接，3种属性对应不同的线程优先级。高优先级任务在TaskPool队列中优先调度，并在CPU调度中获得更多系统资源。

  [Priority](../harmonyos-references/js-apis-taskpool.md#priority)的IDLE优先级是用来标记需要在后台运行的耗时任务（例如数据同步、备份。），它的优先级别是最低的。这种优先级标记的任务只会在所有线程都空闲的情况下触发执行，并且只会占用一个线程来执行。
* **业务实现中的关键点**
  1. 合理设置高优先级任务的数量。如果在特定场景下高优先级任务过多，任务池将无法有效区分优先级差异，导致优先级调度可能退化为按入队顺序执行。此外，高优先级任务会抢占系统资源，影响其他线程和应用的执行。
  2. 依赖多个任务的执行时需要考虑优先级的分配。避免高优先级任务依赖低优先级任务的执行，以防止优先级倒置。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';

  5. // ...
  6. function executeTaskPool(bufferArray: ArrayBuffer): void {
  7. taskpool.execute(execColorInfo, bufferArray, taskpool.Priority.HIGH).catch((error: BusinessError) => {
  8. hilog.error(DOMAIN, TAG, FORMAT, `taskpool excute error: ${error}`);
  9. });
  10. }

  12. @Concurrent
  13. async function execColorInfo(bufferArray: ArrayBuffer): Promise<ArrayBuffer> {
  14. if (!bufferArray) {
  15. return new ArrayBuffer(0);
  16. }
  17. const newBufferArr = bufferArray;
  18. let colorInfo = new Uint8Array(newBufferArr);
  19. let PIXEL_STEP = 2;
  20. for (let i = 0; i < colorInfo?.length; i += PIXEL_STEP) {
  21. // data processing
  22. }
  23. hilog.info(0x0000, 'ConcurrentTaskManagement4', '%{public}s', `execColorInfo success`);
  24. return newBufferArr;
  25. }
  ```

  [ConcurrentTaskManagement4.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrentTaskManagement4.ets#L20-L48)
* **与业界方案特殊差异说明**

  业界普遍提供了优先级机制，与TaskPool中的优先级没有显著差异。
* **不推荐应用实现方式**

  不推荐过多设置高优先级或不合理优先级。

### 任务延时调度

* **场景描述**

  在应用业务实现过程中，不是所有任务都需立刻执行，部分任务需延时一段时间后才需执行。

  常见的业务场景如下所示：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | 缓存业务延时执行，不影响冷启动耗时 | 应用启动时，存在大量低优先级任务，例如二级界面的资源下载等，需设置3秒后执行，防止影响冷启动耗时。 |
* **实现方案介绍**

  TaskPool提供了延时执行的能力。目前，仅taskpool.Task支持延时执行。开发者只需以下三个步骤即可完成延时实现。

  步骤一：创建Task对象；

  步骤二：调用taskpool.executeDelayed实现延时执行，依次填写延时时间delayTime、执行任务task和任务优先级priority（不填默认为MEDIUM）。

  步骤三：接收延时任务返回的数据并作处理。
* **业务实现中的关键点**
  1. 非必需情况下不建议使用任务延时调度。在业务复杂的场景中使用任务延时调度可能会导致结果处理时序问题，进而影响应用业务的正常运行。
  2. 不建议将多个任务延时到同一时间执行。这可能导致任务排队，从而影响部分任务在指定延时时间后立即执行。
* **案例参考**

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';

  5. // ...
  6. @Concurrent
  7. function concurrentTask(num: number): number {
  8. hilog.info(0x0000, 'TAG', '%{public}s', 'Add the task that needs to be executed with delay');
  9. return num;
  10. }

  12. function executeTaskPool() {
  13. // create a task
  14. let task: taskpool.Task = new taskpool.Task(concurrentTask, 100);
  15. // Delayed execution of task
  16. taskpool.executeDelayed(3000, task, taskpool.Priority.HIGH).then((value: Object) => {
  17. // Processing delayed task results
  18. hilog.info(DOMAIN, TAG, FORMAT, 'taskpool result: ' + value);
  19. }).catch((err: BusinessError) => {
  20. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  21. });
  22. }
  ```

  [ConcurrentTaskManagement5.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/ConcurrentTaskManagement5.ets#L20-L45)
* **与业界方案特殊差异说明**

  业界大部分提供了任务延时调度功能，与TaskPool中的任务延时调度无明显差异。
* **不推荐应用实现方式**

  在非必须场景中，不建议使用任务延时调度，以防止延时结果处理不当。

## 线程间通信

### 概述

线程间通信指并发多线程间的数据交换，已支持ArkTS、C++等开发语言。不同语言和线程间的通信场景将在下文详细展开。

### 同语言线程间通信（ArkTS内）

* **场景描述**

  ArkTS线程包含主线程、TaskPool线程和Worker线程，这些线程可以通过不同接口通信。

  常见业务场景如下所示：

  |  |  |
  | --- | --- |
  | **常见业务场景** | **具体业务描述** |
  | 宿主JS线程与TaskPool线程 | 使用TaskPool分发任务到子线程。TaskPool子任务与其宿主线程之间需要通信的场景 |
  | 宿主JS线程与Worker线程 | 使用Worker启动子线程，执行任务。Worker子线程与其宿主线程之间需要通信的场景 |
  | 任意JS线程与任意JS线程 | 描述其他任意两个JS线程需要通信的场景 |
* **实现方案介绍**

  |  |  |  |
  | --- | --- | --- |
  | **跨线程交互场景** | **通信方式** | **通信优先级** |
  | 宿主JS线程到TaskPool线程 | 参数传递后分发任务，过程中不支持正向通信。 | 支持 |
  | TaskPool线程到宿主JS线程 | 结果返回时，sendData触发宿主线程的异步回调，底层实现为uv\_async\_send。 | 不支持 |
  | 宿主JS线程到Worker线程 | 采用postMessage和onmessage进行异步通信 | 不支持 |
  | Worker线程到宿主JS线程 | 异步方式：使用postMessage和onmessage进行异步通信  同步方式：Worker线程可以同步调用宿主线程注册的方法并返回结果。 | 不支持 |
  | 任意JS线程与任意JS线程 | 使用@ohos.emitter实现双向异步通信功能。 | 支持 |
* **业务实现中的关键点**

  推荐使用TaskPool和Worker的接口进行ArkTS线程通信。
* **参考链接**

  [@ohos.worker (启动一个Worker)](../harmonyos-references/js-apis-worker.md)

  [@ohos.taskpool（启动任务池）](../harmonyos-references/js-apis-taskpool.md)

  [@ohos.events.emitter (Emitter)](../harmonyos-references/js-apis-emitter.md)
* **与业界方案特殊差异说明**

  线程通信采用消息循环的机制，与业界一致。

### 跨语言多线程通信（C++与ArkTS）

* **场景描述**

  ArkTS线程包含ArkTS运行环境，包括主线程、TaskPool线程和Worker线程。HarmonyOS支持通过Node-API开发C++业务，开发者可以在C++层创建线程，因此C++线程需要与ArkTS线程通信。

  常见业务场景如下所示：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | ArkTS线程（ArkTS）与pthread线程 | ArkTS线程的ArkTS部分与pthread线程的通信场景 |
  | ArkTS线程（C++部分） 与 pthread线程 | ArkTS线程的C++部分与pthread线程的通信场景 |
  | pthread线程与pthread线程 | C++线程间的通信场景 |
* **实现方案介绍**

  |  |  |  |
  | --- | --- | --- |
  | **跨线程交互场景** | **通信方式** | **通信优先级** |
  | ArkTS线程（ArkTS）到pthread线程 | 不支持，需要转到C++ | 不涉及 |
  | pthread线程到ArkTS线程（ArkTS） | 使用napi\_threadsafe\_function通信。 | 支持 |
  | pthread线程到 ArkTS线程（C++部分） |
  | ArkTS线程（C++部分）到pthread线程 | 开发者自定义 | 开发者自定义行为 |
  | pthread线程与pthread线程 |
* **案例参考**

  ```
  1. // napi_init.cpp
  2. struct CallbackData {
  3. napi_env env;
  4. napi_async_work asyncWork = nullptr;
  5. napi_threadsafe_function tsfn = nullptr;
  6. int32_t data = -1;
  7. };

  9. static void CallJs(napi_env env, napi_value jsCb, void *context, void *data) {
  10. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
  11. napi_value global;
  12. assert(napi_get_global(env, &global) == napi_ok);
  13. napi_value number;
  14. assert(napi_create_int32(env, callbackData->data, &number) == napi_ok);
  15. assert(napi_call_function(env, global, jsCb, 1, &number, nullptr) == napi_ok);
  16. }
  17. static void NativeThread(void *data) {
  18. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
  19. /* Cross-thread call */
  20. {
  21. assert(napi_acquire_threadsafe_function(callbackData->tsfn) == napi_ok);

  23. callbackData->data = 123456;
  24. napi_status status = napi_call_threadsafe_function(callbackData->tsfn, callbackData, napi_tsfn_blocking);
  25. assert(status == napi_ok);
  26. }
  27. }
  28. static void ThreadFinished(napi_env env, void *data, [[maybe_unused]] void *context) {
  29. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);

  31. assert(napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release) == napi_ok);
  32. ;
  33. callbackData->asyncWork = nullptr;
  34. callbackData->tsfn = nullptr;
  35. delete callbackData;
  36. }
  37. static napi_value NativeCall(napi_env env, napi_callback_info info) {
  38. napi_value resourceName = nullptr;
  39. CallbackData *callbackData = new CallbackData;
  40. callbackData->env = env;

  42. napi_value jsCb = nullptr;
  43. size_t argc = 1;

  45. assert(napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr) == napi_ok);
  46. assert(argc == 1);

  48. assert(napi_create_string_utf8(env, "Call thread-safe function from c++ thread", NAPI_AUTO_LENGTH, &resourceName) ==
  49. napi_ok);
  50. napi_status status;
  51. status = napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, callbackData, ThreadFinished,
  52. callbackData, CallJs, &(callbackData->tsfn));
  53. assert(status == napi_ok);
  54. return nullptr;
  55. }
  ```

  [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/cpp/napi_init.cpp#L49-L103)

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';
  2. import nativeModule from 'libentry.so';
  3. // ...
  4. @Component
  5. export struct InterThreadCommunication1 {
  6. build() {
  7. NavDestination() {
  8. Column() {
  9. Button($r('app.string.multithreaded_communication_title'))
  10. .width('100%')
  11. .onClick(() => {
  12. nativeModule.nativeCall((a: number) => {
  13. hilog.info(DOMAIN, TAG, FORMAT, 'Received data from thread-function: %{public}d', a);
  14. })
  15. hilog.info(DOMAIN, TAG, FORMAT, `click nativeCall success`);
  16. })
  17. }
  18. // ...
  19. }
  20. .title($r('app.string.multithreaded_communication_title'))
  21. }
  22. }
  ```

  [InterThreadCommunication1.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/InterThreadCommunication1.ets#L20-L55)
* **与业界方案特殊差异说明**
  1. Java与C++通信时，业界使用JNI调用，与Node-API机制类似。
  2. Java与C++通信时，业界支持C++线程通过attach方式反射调用Java方法。HarmonyOS APP开发时需通过napi\_threadsafe\_function异步通信。
* **不推荐应用实现方式**

  不建议在C++层增加wait等同步机制，这会导致卡死或掉帧等问题。

### 线程间模块共享（单例模式）

* **场景描述**

  进程的唯一ArkTS实例初始化流程复杂，整体耗时较长。如果在主线程中进行初始化，会导致应用启动时间延长并阻塞主线程的执行。因此，建议将这些实例的初始化流程放在ArkTS子线程中进行。初始化完成后，主线程可以直接使用该实例。

  常见的业务场景如下所示：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | SDK初始化 | 在ArkTS子线程中调用API的Init初始化得到一个单例对象，完成后传给其他ArkTS线程使用 |
* **实现方案介绍（方案一）**

  步骤一：使用C++单例模式封装，并在上层封装JS壳，子线程中进行初始化。

  步骤二：初始化完成后通知主线程，主线程导入并使用该单例对象。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/R73ypdwKS8SMKzX0RD3QDg/zh-cn_image_0000002194011080.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T061043Z&HW-CC-Expire=86400&HW-CC-Sign=1E204A29F3EE1E73895871E78A5177F6207D5817D3C9C9A516494814406C2E07 "点击放大")
* **业务实现中的关键点**
  1. JS模块对象

     模块定义的导出对象即为使用者导入时获得的对象。

     JS模块对象中的JS函数通过Node-API方法绑定到模块的Native静态方法。调用JS函数时，实际会调用Native静态方法来提供功能。
  2. Native Instance

     模块对象的成员对象（ExternalReference）通过Native Class的GetCurrentInstance（标准单例实现）获取，进程内同模块均指向同一个Native单例。此设计适用于已有线程安全C++类的Native实现，Native成员方法需进行同步保护。

     该模块对象即使包含其他JS成员，也类似于“局部变量”，即线程间不共享。
  3. Native静态方法

     Native静态方法提供对应模块的Native功能实现。通过napi\_get\_cb\_info获取JS绑定函数的`this`对象，从而通过this获取绑定在JS模块对象上的Native实例，再调用Native实例对应的Native成员方法，即可完成对应功能的实现。

     说明

     同上，方法实现中不能进行非线程安全的全局变量操作。
  4. 生命周期问题

     模块对象通常在主线程退出时进行析构。

     若需精细化控制，可以绑定finalizeCallback进行管理。线程对象回收时，该线程会调用析构方法。
* **案例参考**

  ```
  1. // napi_init.cpp
  2. class Singleton {
  3. public:
  4. static Singleton &GetInstance() {
  5. static Singleton instance;
  6. return instance;
  7. }
  8. static napi_value GetAddress(napi_env env, napi_callback_info info) {
  9. uint64_t addressVal = reinterpret_cast<uint64_t>(&GetInstance());
  10. napi_value napiAddress = nullptr;
  11. napi_create_bigint_uint64(env, addressVal, &napiAddress);
  12. return napiAddress;
  13. }
  14. static napi_value GetSetSize(napi_env env, napi_callback_info info) {
  15. std::lock_guard<std::mutex> lock(Singleton::GetInstance().numberSetMutex_);
  16. uint32_t setSize = Singleton::GetInstance().numberSet_.size();
  17. napi_value napiSize = nullptr;
  18. napi_create_uint32(env, setSize, &napiSize);
  19. return napiSize;
  20. }
  21. static napi_value Store(napi_env env, napi_callback_info info) {
  22. size_t argc = 1;
  23. napi_value args[1] = {nullptr};
  24. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  25. if (argc != 1) {
  26. napi_throw_error(env, "ERROR: ", "store args number must be one");
  27. return nullptr;
  28. }
  29. napi_valuetype type = napi_undefined;
  30. napi_typeof(env, args[0], &type);
  31. if (type != napi_number) {
  32. napi_throw_error(env, "ERROR: ", "store args is not number");
  33. return nullptr;
  34. }
  35. std::lock_guard<std::mutex> lock(Singleton::GetInstance().numberSetMutex_);
  36. uint32_t value = 0;
  37. napi_get_value_uint32(env, args[0], &value);
  38. Singleton::GetInstance().numberSet_.insert(value);
  39. return nullptr;
  40. }

  42. private:
  43. Singleton() {}                                    // Private constructor to prevent external instantiation of objects
  44. Singleton(const Singleton &) = delete;            // Do not copy the constructor
  45. Singleton &operator=(const Singleton &) = delete; // The assignment operator is prohibited

  47. public:
  48. std::unordered_set<uint32_t> numberSet_{};
  49. std::mutex numberSetMutex_{};
  50. };
  ```

  [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/cpp/napi_init.cpp#L110-L159)

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';
  4. import singleton from 'libentry.so';

  6. // ...
  7. @Concurrent
  8. function getAddress() {
  9. let address = singleton.getAddress();
  10. hilog.info(0x0000, 'TAG', '%{public}s', 'taskpool:: address is ' + address);
  11. }

  13. @Concurrent
  14. function store(a: number, b: number, c: number) {
  15. let size = singleton.getSetSize();
  16. hilog.info(0x0000, 'TAG', '%{public}s', 'set size is ' + size + ' before store');
  17. singleton.store(a);
  18. singleton.store(b);
  19. singleton.store(c);
  20. size = singleton.getSetSize();
  21. hilog.info(0x0000, 'TAG', '%{public}s', 'set size is ' + size + ' after store');
  22. }

  24. @Component
  25. export struct InterThreadCommunication2 {
  26. build() {
  27. NavDestination() {
  28. Column() {
  29. Button($r('app.string.singleton_pattern_title'))
  30. .width('100%')
  31. .onClick(() => {
  32. let address = singleton.getAddress();
  33. hilog.info(DOMAIN, TAG, FORMAT, `host thread address is ${address}`);
  34. let task1 = new taskpool.Task(getAddress);
  35. taskpool.execute(task1).catch((err: BusinessError) => {
  36. hilog.error(DOMAIN, TAG, FORMAT,
  37. `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  38. });

  40. let task2 = new taskpool.Task(store, 1, 2, 3);
  41. taskpool.execute(task2).catch((err: BusinessError) => {
  42. hilog.error(DOMAIN, TAG, FORMAT,
  43. `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  44. });

  46. let task3 = new taskpool.Task(store, 4, 5, 6);
  47. taskpool.execute(task3).catch((err: BusinessError) => {
  48. hilog.error(DOMAIN, TAG, FORMAT,
  49. `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  50. });
  51. })
  52. }
  53. // ...
  54. }
  55. .title($r('app.string.singleton_pattern_title'))
  56. }
  57. }
  ```

  [InterThreadCommunication2.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/InterThreadCommunication2.ets#L20-L90)
* **实现方案介绍（方案二）**

  步骤一：使用ArkTS对象定义Sendable类的单例，封装为共享模块（进程内共享），并在子线程中初始化。

  步骤二：初始化完成后通知主线程，主线程使用该单例对象。
* **业务实现中的关键点**

  Sendable类需要满足一定的约束，可参考[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md#sendable装饰器)。
* **案例参考**

  ```
  1. // Demo.ets
  2. "use shared"

  4. @Sendable
  5. export class Demo {
  6. private static instance: Demo;

  8. private constructor() {
  9. }

  11. public static getInstance(): Demo {
  12. if (!Demo.instance) {
  13. Demo.instance = new Demo();
  14. }
  15. return Demo.instance;
  16. }

  18. public init(): void {
  19. // initialization logic
  20. }
  21. }
  ```

  [Demo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/Demo.ets#L21-L41)

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { taskpool } from '@kit.ArkTS';
  4. import { Demo } from './Demo';
  5. const DOMAIN = 0x0000;
  6. const TAG = 'InterThreadCommunication3';
  7. const FORMAT = '%{public}s';
  8. @Concurrent
  9. function initSingleton(): void {
  10. let demo = Demo.getInstance();
  11. demo.init();
  12. hilog.info(0x0000, 'InterThreadCommunication3', '%{public}s', `initSingleton success`);
  13. // Notify the main thread that initialization is complete
  14. }

  16. async function executeTaskPool(): Promise<void> {
  17. let task = new taskpool.Task(initSingleton);
  18. await taskpool.execute(task).then(() => {
  19. hilog.info(0x0000, 'InterThreadCommunication3', '%{public}s', `executeTaskPool success`);
  20. }).catch((err: BusinessError) => {
  21. hilog.error(DOMAIN, TAG, FORMAT, `taskpool execute error. Cause code: ${err.code},message: ${err.message}`);
  22. });
  23. }
  ```

  [InterThreadCommunication3.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/InterThreadCommunication3.ets#L20-L44)
* **与业界方案特殊差异说明**

  Java存在ClassLoader机制，所有类型是静态且唯一的，因此可以方便地导入类并支持单例模式。而在HarmonyOS APP开发中，需要借助共享模块来保证类只加载一次，确保唯一性。

### 线程间不可变数据共享

* **场景描述**

  定义为Sendable类型的对象在发送到其他TS线程后可被多线程读写，开发者需要通过异步锁机制进行管理。为确保数据在多线程访问时的准确性，可以使用锁机制或使对象变为只读。

  以下是一些常见的业务场景：

  |  |  |
  | --- | --- |
  | 常见业务场景 | 具体业务描述 |
  | 全局环境变量共享 | 应用启动时生成的资源加载入口、配置参数和全局变量等不需要更新的变量，可通过冻结能力冻结后共享到多个ArkTS子线程 |
  | 一次性产物不可变共享 | 业务阶段性生成的页面布局数据，在工作线程生成后传输并缓存在UI线程，缓存后不会修改，可能会多次作为UI渲染的输入使用 |
* **实现方案介绍**

  通过冻结API，将共享对象变为只读。

  步骤一：定义业务逻辑，生成所需的Sendable对象。

  步骤二：发送到其他ArkTS线程前，使用Object.Freeze API冻结该对象。

  步骤三：通过taskpool或worker的消息通信机制将对象共享到其他ArkTS线程。
* **业务实现中的关键**

  冻结后的对象不可修改，尝试修改将导致抛出ArkTS异常。
* **案例参考**

  以全局环境变量共享为例：

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';
  2. import { worker } from '@kit.ArkTS';
  3. import { freezeObj } from './freezeObj';
  4. // ...
  5. @Sendable
  6. export class GlobalConfig {
  7. // Some configuration properties and methods
  8. init() {
  9. // Initialization-related logic
  10. freezeObj(this) // Freeze the current object after initialization is completed.
  11. }
  12. }

  14. function executeTaskPool() {
  15. try {
  16. let globalConfig = new GlobalConfig();
  17. globalConfig.init();
  18. const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets`', { name: 'Worker1' });
  19. workerInstance.postMessage(globalConfig);
  20. hilog.info(DOMAIN, TAG, FORMAT, `executeTaskPool success`);
  21. } catch (err) {
  22. hilog.error(DOMAIN, TAG, FORMAT, `postMessage failed. Cause code: ${err.code},message: ${err.message}`);
  23. }
  24. }
  ```

  [InterThreadCommunication4.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/InterThreadCommunication4.ets#L20-L47)

  ```
  1. // The worker file path is: entry/ets/workers/Worker.ets
  2. // Worker.ets
  3. import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
  4. import { GlobalConfig } from '../pages/InterThreadCommunication4';
  5. import { hilog } from '@kit.PerformanceAnalysisKit';

  7. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
  8. workerPort.onmessage = (e: MessageEvents) => {
  9. let globalConfig: GlobalConfig = e.data;
  10. hilog.info(0x0000, 'TAG', '%{public}s', `globalConfig: ${globalConfig}`);
  11. // use the globalConfig object
  12. }
  ```

  [Worker.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/workers/Worker.ets#L20-L31)

  ```
  1. // freezeObj.ts
  2. export function freezeObj(obj: any) {
  3. Object.freeze(obj);
  4. }
  ```

  [freezeObj.ts](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/UseSendable/entry/src/main/ets/pages/freezeObj.ts#L20-L23)
* **与业界方案特殊差异说明**

  内存共享模型中，Java/C++对象在不同线程间均可见。Sendable对象需要将对象引用发送到其他线程才能使用。

### 生产者与消费者模式

* **场景描述**

  生产者与消费者模式表现为以下几个特征：

  1. 生产者可以是单个或多个，同时并发地生产数据。

  2. 消费者可以单个或多个并发地消费数据；

  3. 存在一个数据缓存区。生产者将数据存储在缓存区，消费者从缓存区取数据。缓存区满时通知生产者停止生产，缓存区空时通知消费者休眠。

  常见的业务场景如下所示：

  |  |  |  |
  | --- | --- | --- |
  | 常见业务场景 | 具体业务描述 | 场景类型 |
  | 阅读应用页面预加载 | 用户每次翻页或跳转后，需要预加载多张前后页。将前后页的加载请求缓存到一个加载队列中，并并发执行队列中的页面布局解析任务。 | CPU密集型+IO密集型 |
  | 本地文件上传 | 用户在主线程中一次上传一个或多个文件。上传文件的请求被存储在上传队列中，并发处理队列中的文件上传到云端。 | CPU密集型+IO密集型 |
* **实现方案介绍**

  以阅读应用场景为例：

  步骤一：用户每次翻页时，系统会生成多个前后页的预加载请求。

  步骤二：通过网络接口从云端下载多个页面的原始数据。

  步骤三：通过taskpool并发解析页面原始数据生成page对象。page对象描述页面布局和组成部分。

  步骤四：taskpool执行结果返回到UI线程的缓存队列。

  步骤五：渲染缓存队列中临近当前页的page对象。
* **业务实现中的关键**
  1. 如果Page对象回到主线程仅需使用其中的数据，可以考虑通过序列化在线程间传递。如果Page对象引用了多个自定义类型的对象，为了将其完整地返回UI线程，需要将其定义为Sendable类型的对象。
  2. 如果页面原始数据是TS线程间共享的，可以在UI线程执行下载任务（异步并发，不阻塞UI线程）。如果不是，则需在taskpool工作线程中执行下载，
  3. 对时延敏感的场景不建议使用并发模块处理相关逻辑。并发功能可将负载从UI线程转移到工作线程，但会增加时延（并发不排队时约为500μs）。
* **与业界方案特殊差异说明**

  1. 内存共享模型如Java/C++对象在不同线程间可见。ArkTS的线程间内存隔离模型中，对象在不同线程间使用需要序列化（拷贝），Sendable对象需要将对象引用发送到其他线程才可使用。

  2. Sendable对象存在较多约束，尽量只将必须共享的对象定义为Sendable对象，普通ArkTS对象持有Sendable对象并串联整个流程。

## 示例代码

* [基于Sendable实现多线程功能](https://gitcode.com/harmonyos_samples/UseSendable)
