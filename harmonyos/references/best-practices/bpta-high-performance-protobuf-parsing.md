---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-performance-protobuf-parsing
title: 高性能Protobuf解析
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 对象序列化性能优化 > 高性能Protobuf解析
category: best-practices
scraped_at: 2026-04-28T08:22:35+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:aae7b719ed494173f7f9f958429088ed74e1cadf173abd43e2f9ea57f64e400f
---

## 概述

在跨语言通信场景中，[Protocol Buffers](https://protobuf.dev/)通过序列化和反序列化机制实现结构化数据的高效交互。[TurboTransProtobuf](https://gitcode.com/openharmony-sig/turbo_trans/tree/turbo_trans_protobuf)是基于ArkTS的高性能Protocol Buffers解析方案，针对现有的[protobufjs](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fprotobufjs)方案进行了多维度优化：

* 全量类型支持：完整兼容.proto定义中的所有数据类型（包括map、oneof、any、数组等），同时适配singular、optional、required等关键字。
* 系统生态兼容：原生支持Sendable类型，可无缝适配hvigor插件的代码生成流程，确保工程构建与运行的一致性。
* 双协议兼容：无需额外配置，原生兼容proto2与proto3两种Protocol Buffers协议版本。
* 高性能优化：核心序列化/反序列化逻辑通过Native层实现，与protobufjs实现方案相比，性能提升超过20%。

本文将围绕Protocol Buffers序列化和反序列化的典型场景，以TurboTransProtobuf框架为核心，介绍其使用要点及性能优势。

## 反序列化为业务对象

### 使用场景

在数据存储与网络传输场景中，Protocol Buffers数据被广泛应用，涉及数据的序列化与反序列化。例如，后端业务通过其他语言生成Protocol Buffers二进制数据，客户端通过网络请求获取数据，并将其转换为业务对象。开发者通常使用第三方库protobufjs实现序列化与反序列化功能，当数据量大时，可能导致解析超时或内存溢出等问题。针对此类问题，可选择TurboTransProtobuf库予以解决。

### 实现原理

TurboTransProtobuf通过Native层优化与代码生成实现高性能反序列化。当开发者使用TurboTransProtobufPlugin插件时，插件将根据.proto文件定义的结构生成对应的ArkTS类型文件，并通过以下流程实现性能优化：

1. 元数据收集与校验
   * 开发者通过.proto文件定义数据结构。
   * TurboTransProtobufPlugin在编译期解析.proto文件，收集字段信息并校验合法性。
2. 代码生成
   * 基于 .proto 结构生成高效的encode()/decode()方法，支持[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md#sendable装饰器)以避免跨线程传输时的内存拷贝。
3. 路径绑定
   * 插件在编译期间自动生成对应的ArkTS代码(.ets文件)，并同步更新项目中对.proto类的引用路径。

### 开发步骤

1. 引入TurboTransProtobufPlugin和TurboTransProtobuf三方库。
   * 插件引入，在工程根目录下的 hvigor/hvigor-config.json5 文件内加入如下配置：

     ```
     1. "dependencies": {
     2. // ...
     3. "@hadss/turbo-trans-protobuf-plugin": "latest"
     4. },
     ```

     [hvigor-config.json5](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/hvigor/hvigor-config.json5#L4-L9)
   * 三方库引入，在工程目录或者模块下使用ohpm方式安装：

     ```
     1. ohpm install @hadss/turbo-trans-protobuf
     ```
2. 插件生效还需在工程根目录的 hvigorfile.ts 文件中添加相关插件配置，参考如下：

   ```
   1. import { turboTransProtobufPlugin } from "@hadss/turbo-trans-protobuf-plugin";

   3. export default {
   4. system: appTasks,
   5. plugins: [
   6. // ...
   7. turboTransProtobufPlugin({
   8. saveDir: 'src/main/ets/model',   // Save directory for generated code
   9. scanDir: ['protofile'],          // Directories to scan for .proto files
   10. sendable: true,                  // Whether to enable @Sendable support
   11. }),
   12. ]
   13. }
   ```

   [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/hvigorfile.ts#L20-L34)
3. 依据Protocol Buffers规范编写.proto文件，并将其保存在模块路径中，对应示例代码工程根目录下的 entry/protofile/UserProfile.proto 文件。

   ```
   1. syntax = "proto2";
   2. message UserProfile {
   3. required int32 age = 1;
   4. optional string name = 2;
   5. optional int64 birth_year = 3;
   6. optional fixed32 height = 4;
   7. required bool is_student = 5;
   8. }
   ```

   [UserProfile.proto](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/protofile/UserProfile.proto#L17-L24)

   插件将基于步骤2完成的配置项，在编译阶段自动生成ets代码，生成结果将按照 hvigorfile.ts 中saveDir配置的路径存储。在示例代码工程中，对应的生成文件路径为entry/src/main/ets/model/UserProfile.ets（位于工程根目录下）。
4. 通过[@Concurrent装饰器](../harmonyos-guides/taskpool-introduction.md#concurrent装饰器)定义子线程任务，在任务内部调用步骤3中插件自动生成代码中暴露的静态方法decode()，以完成相应的数据处理逻辑。

   ```
   1. @Concurrent
   2. function decodeUser(buf: ArrayBuffer): UserProfile | undefined {
   3. try {
   4. return UserProfile.decode(buf);
   5. } catch (error) {
   6. Logger.error(`UserProfile decode error: ${JSON.stringify(error)}`);
   7. return undefined;
   8. }
   9. }
   ```

   [DecodeBusinessTypePage.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/pages/DecodeBusinessTypePage.ets#L24-L33)
5. 通过taskpool.execute()调度子线程将二进制格式数据反序列化为业务对象。

   ```
   1. let res = await taskpool.execute(decodeUser, encodeBuf) as UserProfile | undefined;
   ```

   [DecodeBusinessTypePage.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/pages/DecodeBusinessTypePage.ets#L61-L61)

## 跨线程数据传输

### 使用场景

在并发编程环境中，通常需要在线程间传递数据。当数据以Protocol Buffers格式存储时，高效地进行序列化和反序列化成为关键。在实时消息处理场景中，跨线程数据传输的效率直接影响应用的整体性能。例如，客户端请求处理线程完成业务逻辑后，需将结果传递给I/O线程进行网络发送，若序列化和反序列化过程耗时过长，将严重影响业务逻辑的执行效率，导致应用界面卡顿，影响用户体验。

### 实现原理

TurboTransProtobuf在跨线程数据传输方面采用了以下优化策略：

* Sendable对象转换：通过TurboTransProtobufPlugin插件，生成[@Sendable装饰器](../harmonyos-guides/arkts-sendable.md#sendable装饰器)的类，支持跨线程内存共享。

### 开发步骤

1. 配置[插件和第三方库](bpta-high-performance-protobuf-parsing.md#li139972026192313)依赖后，确保在工程根目录下的 hvigorfile.ts 文件内将sendable属性设置为true：

   ```
   1. import { turboTransProtobufPlugin } from "@hadss/turbo-trans-protobuf-plugin";

   3. export default {
   4. system: appTasks,
   5. plugins: [
   6. // ...
   7. turboTransProtobufPlugin({
   8. saveDir: 'src/main/ets/model',   // Save directory for generated code
   9. scanDir: ['protofile'],          // Directories to scan for .proto files
   10. sendable: true,                  // Whether to enable @Sendable support
   11. }),
   12. ]
   13. }
   ```

   [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/hvigorfile.ts#L20-L34)

   使用DevEco Studio编译或者使用hvigorw命令编译后，将生成带有@Sendable装饰器的类。
2. 通过@Concurrent装饰器定义子线程任务，在任务内部调用步骤1中插件自动生成代码中暴露的静态方法encode()，以完成相应的数据处理逻辑。

   ```
   1. @Concurrent
   2. function encodeUser(obj: UserProfile): ArrayBuffer | undefined {
   3. try {
   4. return UserProfile.encode(obj);
   5. } catch (error) {
   6. Logger.error(`UserProfile encode error: ${JSON.stringify(error)}`);
   7. return undefined;
   8. }
   9. }
   ```

   [CrossThreadTransferPage.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/pages/CrossThreadTransferPage.ets#L24-L32)
3. 通过TurboTransProtobuf生成的代码创建的业务对象天然支持Sendable特性。此类对象在跨线程传输时，系统将以内存共享方式传递数据，避免跨线程拷贝导致的性能损耗。

   ```
   1. let message_simple = new UserProfile();
   2. message_simple.age = 25;
   3. message_simple.name = 'Alice';
   4. message_simple.birth_year = 1999;
   5. message_simple.height = 175;
   6. message_simple.is_student = true;
   7. let res = await taskpool.execute(encodeUser, message_simple) as ArrayBuffer | undefined;
   ```

   [CrossThreadTransferPage.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/pages/CrossThreadTransferPage.ets#L52-L58)

## Protobuf大数据解析

### 使用场景

在大数据处理场景中，处理通过网络传输的大型Protocol Buffers数据（几十MB至一百MB）是常见的性能挑战。在主线程直接解析此类数据可能导致应用卡顿，甚至导致AppFreeze，严重影响用户体验。典型应用场景包括：

* 弹幕数据处理：在直播场景中实时接收海量弹幕消息（如百万条弹幕/分钟），通过Protocol Buffers格式解析并渲染至界面。
* 实时日志分析：电商平台实时接收用户行为日志，单次请求可能包含百万条记录。
* 远程数据迁移：通过网络接口批量导入或导出结构化数据（如历史订单记录）。
* 物联网设备数据处理：解析从网络接口获取的设备上报数据（如传感器数据流）。

在这些场景中，若在主线程直接解析大数据，可能因内存占用过高或CPU密集操作导致应用无响应。通过将解析任务调度到子线程，并结合内存优化策略，可显著提升应用流畅性。

### 实现原理

在Protobuf大数据解析场景中，服务端生成大数据后，在子线程中通过分片处理将数据拆分为可并行传输的片段，利用异步传输机制发送至客户端。客户端接收分片数据后，在子线程中重组合并数据，待所有分片接收完成后，统一进行反序列化操作。TurboTransProtobuf通过以下机制优化大数据解析性能：

* Native层性能优化：核心反序列化逻辑通过Native层实现，相比纯JavaScript方案（如ProtobufJS）性能提升超过20%。在创建对象时，直接通过Native创建sendable对象，确保反序列化结果可直接跨线程传输，避免内存拷贝。
* 子线程解析：利用HarmonyOS的[worker](../harmonyos-guides/worker-introduction.md)功能，将大数据解析任务调度至子线程执行，防止主线程阻塞。

### 开发步骤

1. 配置插件和第三方库依赖后，确保在工程根目录下的 hvigorfile.ts 文件内将sendable属性设置为true：

   ```
   1. import { turboTransProtobufPlugin } from "@hadss/turbo-trans-protobuf-plugin";

   3. export default {
   4. system: appTasks,
   5. plugins: [
   6. // ...
   7. turboTransProtobufPlugin({
   8. saveDir: 'src/main/ets/model',   // Save directory for generated code
   9. scanDir: ['protofile'],          // Directories to scan for .proto files
   10. sendable: true,                  // Whether to enable @Sendable support
   11. }),
   12. ]
   13. }
   ```

   [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/hvigorfile.ts#L20-L34)

   使用DevEco Studio编译或者使用hvigorw命令编译后，将生成带有@Sendable装饰器的类。
2. 服务端生成数据后，在子线程中进行序列化操作，并通过分片处理将数据拆分为可并行传输的片段，随后将数据分片发送至客户端。

   ```
   1. workerInstance = new worker.ThreadWorker('entry/ets/workers/ServerWorker.ets');
   2. // ...
   3. let arrayBuffer: ArrayBuffer | undefined;
   4. // ...
   5. arrayBuffer = await taskpool.execute(encodeBulletBatch,
   6. DataGenerateUtil.generateBulletBatch(res.data)) as ArrayBuffer | undefined;
   7. // ...
   8. if (arrayBuffer) {
   9. try {
   10. this.workerInstance.postMessage(arrayBuffer);
   11. } catch (err) {
   12. Logger.error(`Failed to post message to worker: ${JSON.stringify(err)}`);
   13. }
   14. this.workerInstance.onmessage = (e: MessageEvents) => {
   15. let data: ArrayBuffer = e.data;
   16. this.sendBigData(client, data);
   17. };
   18. }
   ```

   [TcpServerUtil.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/utils/TcpServerUtil.ets#L34-L125)
3. 客户端接收到分片数据后，在子线程中通过重组合并数据，待所有分片接收完成后，统一进行反序列化操作。生成的Sendable对象无需拷贝，通过内存共享机制直接传递至主线程。

   ```
   1. workerPort.onmessage = (event: MessageEvents) => {
   2. const data: ArrayBuffer = event.data;
   3. const unpackedChunk = unpackArrayBuffer(data);
   4. // ...
   5. workerPort.postMessage(unpackedChunk.chunkIndex);
   6. // ...

   8. // Reassemble fragmented data in worker thread
   9. const reassembledBuffer = ArrayBufferAssemblerUtil.receiveChunk(
   10. unpackedChunk.dataId,
   11. unpackedChunk.chunkIndex,
   12. unpackedChunk.totalChunks,
   13. unpackedChunk.chunkData
   14. );
   15. if (reassembledBuffer) {
   16. ArrayBufferAssemblerUtil.clean();
   17. // Transfer Sendable object to main thread via memory sharing
   18. let res: BulletBatch | null | undefined = null;
   19. // Deserialize and send in single operation
   20. // ...
   21. res = BulletBatch.decode(reassembledBuffer);
   22. workerPort.postMessageWithSharedSendable(res);
   23. // ...
   24. }
   25. };
   ```

   [ClientWorker.ets](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/blob/master/entry/src/main/ets/workers/ClientWorker.ets#L32-L68)

## 示例代码

[基于TurboTransProtobuf实现高性能Protobuf解析](https://gitcode.com/HarmonyOS_Samples/turbo-trans-protobuf/tree/master)
