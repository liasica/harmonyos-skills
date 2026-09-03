---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-data-race-fault-mode
title: 数据竞争异常访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 数据竞争异常访问故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:de2b947563ddece837d5d99d4a838b3031bc250dc063601416652b69aaaf23d7
---

多个线程在未正确同步的情况下同时访问共享资源，可能引发数据竞争和并发访问异常。多个线程对同一数据进行读写操作时，可能导致数据状态异常或程序运行结果不确定，严重时甚至引发应用崩溃。由于线程执行时序导致该问题通常具有偶现性，难以稳定复现。[使能TSan](bpta-stability-tsan-detection.md#section14181102916475)（ThreadSanitizer）后，可记录冲突访问线程及其调用栈。本文结合典型案例，展示此类问题的日志特征与定位方法，具体包括：

* [多线程内存读写冲突](bpta-stability-data-race-fault-mode.md#section897465273712)
* [多线程C++对象读写冲突](bpta-stability-data-race-fault-mode.md#section11589111619382)
* [多线程并发内存释放后使用](bpta-stability-data-race-fault-mode.md#section686213314382)
* [信号处理非法修改errno](bpta-stability-data-race-fault-mode.md#section1827017116513)
* [信号处理调用非信号安全函数](bpta-stability-data-race-fault-mode.md#section129181254165220)
* [非法重复解锁](bpta-stability-data-race-fault-mode.md#section690519775319)

## 多线程内存读写冲突

### 根因描述

多线程内存读写冲突是指多个线程访问同一内存位置，其中至少一个线程执行写操作。TSan基于运行时内存插桩与访问跟踪机制检测数据竞争。当同时满足以下两个条件时，会触发异常告警：

1. 并发访问：两个或多个线程并发访问同一内存区域，且访问之间未建立有效的同步关系。
2. 冲突检查：多个并发访问操作中，至少存在一个写操作。

### 问题分析思路

多线程内存读写冲突通常由以下几种原因引起：

1. 全局变量跨线程共享：多个线程直接读写同一个全局变量，缺乏锁保护。
2. 堆内存跨线程共享后访问：通过指针将堆内存传递给多个线程使用，但访问过程中缺少同步保护，导致多个线程同时读写同一内存区域。
3. 栈内存跨线程引用：将局部变量地址传递给其他线程时，需要确认栈对象生命周期和访问同步，避免多个线程同时访问或访问已经失效的栈内存。
4. 结构体成员竞争：对结构体的不同成员进行并发访问。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字data race，确认问题属于多线程数据竞争异常。结合Read/Write of size和Previous read/write of size字段，确认发生冲突的线程、访问地址、访问大小以及读写类型，判断属于“写-写”冲突还是“读-写”冲突。结合Location is字段辅助判断冲突地址对应的内存类型，例如全局变量或堆对象。
2. 分析各个线程的调用栈，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。结合解析出的代码，分析问题根因。

### 关键字

此类问题一般可以通过日志中的关键字data race确认故障类型，并结合Read/Write of size、Previous read/write of size等字段进一步确认发生冲突的线程、访问地址以及读写类型。

### 案例分析

**案例**：多线程共享数据读写竞争导致异常访问

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==44827==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: data race (pid=44827)
     Write of size 4 at 0x0057149e83d0 by thread T56:
       #0 0x57147a8720  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a871c) (BuildId: e1c2ab39dfe25e44270263d1dd40f8c36760f8e5)
       #1 0x57147a8f8c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8f88) (BuildId: e1c2ab39dfe25e44270263d1dd40f8c36760f8e5)
       #2 0x555718a540  (/system/lib64/ndk/libffrt.so+0x8a53c) (BuildId: 91caabab1d7cb63c0b34b9fb2c74ca60)

     Previous write of size 1 at 0x0057149e83d0 by thread T58:
       #0 0x57147a86dc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a86d8) (BuildId: e1c2ab39dfe25e44270263d1dd40f8c36760f8e5)
       #1 0x57147a8764  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8760) (BuildId: e1c2ab39dfe25e44270263d1dd40f8c36760f8e5)
       #2 0x55572b97f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)

     Location is global '<null>' at 0x000000000000 (libentry.so+0x5e83d0)
     ...
   SUMMARY: ThreadSanitizer: data race (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a871c) (BuildId: e1c2ab39dfe25e44270263d1dd40f8c36760f8e5)
   ```

   证据1：data race证明为多线程数据竞争异常。

   ```screen
   WARNING: ThreadSanitizer: data race (pid=44827)
   ```

   证据2：Write of size和Previous write of size表明两个线程对同一地址发生“写-写”冲突，Location is global表明冲突地址属于全局变量。

   ```screen
   Write of size 4 at 0x0057149e83d0 by thread T56:
   ...
   Previous write of size 1 at 0x0057149e83d0 by thread T58:
   ...
   Location is global '<null>' at 0x000000000000 (libentry.so+0x5e83d0)
   ```

   日志中表明线程T56正在向地址0x0057149e83d0对应的内存区域执行写操作；线程T58在此之前也对同一内存地址执行过写操作。Location is global表明该竞争对象位于全局变量区域，即多个线程正在竞争访问同一个全局变量。
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，分别对日志中线程T56和线程T58的调用栈帧（重点关注各线程调用栈中的 #0、#1 帧）地址信息进行符号解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/IcyuvBYdRzyVqRewGkguhA/zh-cn_image_0000002699732134.png)

   1. 代码第143行：创建多个线程共享访问全局变量DataRaceGlobal。
   2. 代码第160行：执行DataRaceSet1()函数，通过字符指针修改该地址对应的内存内容，该操作本质上是对共享变量执行写操作。
   3. 代码第161行：执行DataRaceSet2()函数，直接对共享变量进行赋值操作，同样属于对共享变量的写操作。因此两个线程对同一内存位置执行并发写操作，且访问过程不存在同步保护，导致数据访问顺序不确定，产生“写-写”数据竞争。

**问题结论与总结**

多线程同时修改共享全局变量DataRaceGlobal，线程间未建立有效同步关系，导致两个写操作竞争同一内存区域，造成多线程内存读写冲突。

**修复建议**

1. 对于简单变量的并发读写，优先使用原子操作，保证数据访问的原子性，避免多个线程同时修改导致数据竞争。
2. 对于涉及多个操作或复杂共享数据结构的场景，使用互斥锁保护临界区，确保同一时间只有一个线程访问共享数据。

## 多线程C++对象读写冲突

### 根因描述

多线程C++对象读写冲突是指多个线程在缺少同步保护的情况下，同时访问同一个C++对象，其中至少有一个线程执行写操作，导致对象内部数据访问存在竞争风险。TSan从底层内存访问角度检测线程间的数据竞争，当多个线程对同一对象的成员变量、对象状态等内部数据进行并发访问时，底层内存读写操作可能发生冲突，从而触发数据竞争异常。

### 问题分析思路

多线程C++对象读写冲突通常由以下几种原因引起：

1. 并发push\_back()：多个线程同时向vector添加元素，可能导致vector内部状态损坏。
2. 迭代器失效后再使用：在迭代过程中修改容器，迭代器指向了无效内存。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字data race，确认问题属于多线程数据竞争异常访问。重点关注以下字段Read/Write of size、Previous read/write of size，了解不同线程分别进行了什么操作，确认冲突类型，可能是“写-写”冲突、“读-写”冲突等。日志Location is后的字段可以确认竞争内存位置，是否访问同一内存地址，可能存在全局变量竞争、堆对象竞争、对象成员竞争等。
2. 分析报错栈，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。结合解析出的代码分析问题根因。重点分析C++对象模型相关问题。例如对象成员读写竞争、对象状态修改竞争、STL容器内部状态竞争、迭代器失效访问和对象生命周期竞争等。

### 关键字

此类问题一般通过日志中的关键字data race确认故障类型，并结合Read/Write of size、Previous read/write of size分析对象访问冲突；通过Location is heap block/global判断竞争对象的内存类型，结合调用栈进一步定位根因。

### 案例分析

**案例一：**对象销毁与虚函数调用竞争

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==44670==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: data race on vptr (ctor/dtor vs virtual call) (pid=44670)
     Write of size 8 at 0x00571340a350 by thread T52:
       #0 0x57163a9154  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a9150) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #1 0x57163a90a8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a90a4) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #2 0x57163a90e8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a90e4) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #3 0x57163a869c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8698) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #4 0x5556d797f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)

     Previous read of size 8 at 0x00571340a350 by thread T51:
       #0 0x57163a8580  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a857c) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #1 0x5556d797f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)

     Location is heap block of size 40 at 0x00571340a350 allocated by main thread:
       #0 0x5556d77bd0  (/system/lib64/libclang_rt.tsan.so+0x77bcc) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #1 0x5715e3264c  (/data/storage/el1/bundle/libs/arm64/libc++_shared.so+0xb2648) (BuildId: eb9713b5d6c922165f7e536deb32107a24e0535d)
       #2 0x57163a7e2c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a7e28) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
       #3 0x5555668a98  (/lib/ld-musl-aarch64.so.1+0x9ca94) (BuildId: f284dd56109782ccbd4e823e5cb5ad46)
       #4 0x55e828c2d8  (/system/lib64/platformsdk/libace_napi.z.so+0x4c2d4) (BuildId: 06ec1a6195a5c70310af542a69ff2ebe)
       ...
   SUMMARY: ThreadSanitizer: data race on vptr (ctor/dtor vs virtual call) (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a9150) (BuildId: d710d92ecd0863dd9fca3fbf187ad81aa292cac8)
   ```

   证据1：日志中出现data race on vptr关键字。

   该关键字表明多个线程同时访问同一个C++多态对象内部的虚函数表指针（vptr）。由于vptr与对象的虚函数调用和析构过程相关，可判定该数据竞争发生在C++对象使用与销毁过程中，属于多线程C++对象生命周期访问竞争问题。

   ```screen
   WARNING: ThreadSanitizer: data race on vptr (ctor/dtor vs virtual call) (pid=44670)
   ```

   证据2：Write of size和Previous read of size表明两个线程对同一地址发生“写-读”冲突；Location is确认内存冲突位置。

   ```screen
   Write of size 8 at 0x00571340a350 by thread T52:
   ...
   Previous read of size 8 at 0x00571340a350 by thread T51:
   ...
   Location is heap block of size 40 at 0x00571340a350 allocated by main thread:
   ```

   日志中表明线程T52正在向地址0x00571340a350对应的内存区域执行写操作；线程T51表示对同一地址进行过读操作。Location is heap表示竞争对象存储在堆中，allocated by main thread表示由主线程申请分配，当前存在多个线程对该堆内存区域进行并发访问。
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Vie6RSmnQJKTOI2DRsEqVA/zh-cn_image_0000002729491391.png "点击放大")

   1. 代码第126行：线程1执行obj->F()，通过基类指针调用派生类虚函数。由于虚函数调用依赖对象内部的 vptr，需要读取对象内存中的虚函数表指针信息。
   2. 代码第132行：线程2触发对象析构流程，对象销毁过程中会访问并修改对象内部状态，同时释放对象占用的内存资源。 线程1在调用虚函数时访问对象内部vptr，线程2同时执行销毁对象操作，两个线程对同一个内部数据产生并发访问。由于对象生命周期管理过程中缺少同步保护，导致对象访问和对象销毁之间产生数据竞争，检测到data race on vptr异常。

**问题结论与总结**

obj->F()和delete obj并发执行时，一个线程可能在调用虚函数，另一个线程在析构对象，导致悬空指针访问或虚表损坏，造成多线程C++对象读写冲突。

**修复建议**

1. 建议使用互斥锁保护对象生命周期。
2. 确保销毁前所有线程已退出。

**案例二：**vector并发push\_back()导致容器状态损坏

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==55532==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: data race (pid=55532)
     Read of size 8 at 0x00557d754628 by thread T68:
       #0 0x5696254a64  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x94a60) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #1 0x56963010f4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x1410f0) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #2 0x55572397f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)

     Previous write of size 8 at 0x00557d754628 by thread T67:
       #0 0x5696281a2c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc1a28) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #1 0x5696281680  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc167c) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #2 0x5696254aa4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x94aa0) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #3 0x56963010f4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x1410f0) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
       #4 0x55572397f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)

     Location is heap block of size 24 at 0x00557d754620 allocated by main thread:
       #0 0x5557237bd0  (/system/lib64/libclang_rt.tsan.so+0x77bcc) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)
       #1 0x56938f264c  (/data/storage/el1/bundle/libs/arm64/libc++_shared.so+0xb2648) (BuildId: 252d99223528097ecf4c584b7d12da122cd20ef9)
       #2 0x5567722678  (/system/lib64/platformsdk/libace_napi.z.so+0x62674) (BuildId: 790355d8b83b7c804589de4d345e30e5)
       ...
   SUMMARY: ThreadSanitizer: data race (/data/storage/el1/bundle/libs/arm64/libentry.so+0x94a60) (BuildId: 7d2a5a0a7a16d58f142c4923b2adea80e2f278ea)
   ```

   证据1：日志中出现data race关键字，可初步判定为数据竞争异常问题。

   ```screen
   WARNING: ThreadSanitizer: data race (pid=55532)
   ```

   证据2：Read of size和Previous write of size表明两个线程对同一地址发生“读-写”冲突；Location is确认内存冲突位置。

   ```screen
   Read of size 8 at 0x00557d754628 by thread T68:
   ...
   Previous write of size 8 at 0x00557d754628 by thread T67:
   ...
   Location is heap block of size 24 at 0x00557d754620 allocated by main thread:
   ```

   日志中表明线程T68正在向地址0x00557d754628对应的内存区域执行读操作；线程T67在此之前对同一内存地址执行写操作。Location is heap表示竞争对象位于堆内存区域，allocated by main thread表示该堆内存由主线程申请分配，说明当前存在多个线程对同一堆内存区域进行并发访问，导致读写操作之间产生数据竞争。
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/BhywQuXoTTSqsZZXXN6-XA/zh-cn_image_0000002699892018.png "点击放大")

   1. 代码第236行：线程1调用非线程安全容器std::vector的读写操作push\_back()。
   2. 代码第237行：线程2调用非线程安全容器std::vector的读写操作push\_back()，并发修改vector内部的相关内容，产生数据竞争，导致容器状态异常。

**问题结论与总结**

多个线程同时调用std::vector::push\_back()对同一个vector对象进行写操作。由于std::vector本身不是线程安全容器，push\_back()操作会同时修改vector内部状态，包括元素存储区域、size、capacity以及底层数据指针等。当多个线程未进行同步保护而并发修改这些数据时，会导致线程之间产生竞争。在执行过程中，某个线程可能正在进行元素插入或内存扩容操作，另一个线程同时访问或修改vector内部状态，使vector内部数据结构处于不一致状态。最终可能导致：数据写入丢失、vector元素数量异常、非法内存访问和容器内部状态损坏等问题。

**修复建议**

1. 使用互斥锁保护共享vector。
2. 使用线程私有vector，最后统一合并。

**案例三：**多线程容器修改导致迭代器失效访问

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==1037==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: data race (pid=1037)
     Write of size 8 at 0x00557d757868 by thread T45:
       #0 0x5692cc1a2c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc1a28) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #1 0x5692cc1680  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc167c) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #2 0x5692c94aa4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x94aa0) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #3 0x5692d41804  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x141800) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #4 0x5556db97f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)

     Previous read of size 8 at 0x00557d757868 by thread T44:
       #0 0x5692d414f8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x1414f4) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #1 0x5692d4138c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x141388) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
       #2 0x5556db97f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)

     Location is heap block of size 24 at 0x00557d757860 allocated by main thread:
       #0 0x5556db7bd0  (/system/lib64/libclang_rt.tsan.so+0x77bcc) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)
       #1 0x5692f7264c  (/data/storage/el1/bundle/libs/arm64/libc++_shared.so+0xb2648) (BuildId: 252d99223528097ecf4c584b7d12da122cd20ef9)
       #2 0x55673a2678  (/system/lib64/platformsdk/libace_napi.z.so+0x62674) (BuildId: 790355d8b83b7c804589de4d345e30e5)
       ...
   SUMMARY: ThreadSanitizer: data race (/data/storage/el1/bundle/libs/arm64/libentry.so+0xc1a28) (BuildId: c5ece9966450ae177a14cd0b5b32b31c2e9a080e)
   ```

   证据1：日志中出现data race关键字，可初步判定为数据竞争异常问题。

   ```screen
   WARNING: ThreadSanitizer: data race (pid=1037)
   ```

   证据2：Write of size和Previous read of size表明两个线程对同一地址发生“写-读”冲突；Location is确认内存冲突位置。

   ```screen
   Write of size 8 at 0x00557d757868 by thread T45:
   ...
   Previous read of size 8 at 0x00557d757868 by thread T44:
   ...
    Location is heap block of size 24 at 0x00557d757860 allocated by main thread:
   ```

   日志中表明线程T45正在向地址0x00557d757868对应的内存区域执行写操作；线程T44在此之前对同一内存地址执行读操作。Location is heap表示竞争对象位于堆内存区域，allocated by main thread表示该堆内存由主线程申请分配，说明当前存在多个线程对同一堆内存区域进行并发访问，导致写读操作之间产生数据竞争。
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/fzW0OoW6SgCX_Jt1zttxEA/zh-cn_image_0000002729611345.png "点击放大")

   1. 代码第279行：线程1依赖容器迭代器进行读取。
   2. 代码第280行：线程2修改容器结构，但未使用任何同步机制保证访问顺序。

**问题结论与总结**

在该场景中，一个线程通过迭代器对容器进行遍历读取操作，另一个线程同时对同一容器执行push\_back()操作。由于STL容器并不是线程安全容器，修改操作可能改变容器内部存储结构，例如重新分配内存、移动元素或释放原有存储空间。当容器发生结构变化后，原线程持有的迭代器仍然指向修改前的旧地址，该迭代器已经失效。如果线程继续通过该迭代器访问元素，将导致访问无效内存区域，造成多线程C++对象读写冲突。

**修复建议**

1. 对容器访问增加同步保护。
2. 使用数据副本避免共享访问。
3. 使用线程安全的数据结构。

## 多线程并发内存释放后使用

### 根因描述

多线程并发内存释放后使用是指某个线程释放一块堆内存后，其他线程仍持有指向该内存的指针，并继续访问已经释放的内存对象。此类问题通常由跨线程对象生命周期管理不当引起。当应用开启TSan检测后，工具会跟踪内存分配、释放以及访问行为。当检测到线程访问已经释放的堆内存时，会报告heap-use-after-free异常，并记录相关线程的调用栈信息。

### 问题分析思路

多线程并发内存释放后使用通常由以下几种原因引起：

1. 对象通过原始指针跨线程传递。
2. 对象释放后未及时清理或仍继续使用失效指针。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字heap-use-after-free，确认问题属于内存释放后继续访问异常。重点分析共享对象的生命周期管理，确认对象的创建、使用、释放分别发生在哪些线程，以及释放操作是否早于其他线程最后一次访问。重点排查裸指针跨线程传递、释放与访问缺少同步保护、线程退出顺序异常等问题，确认是否存在对象已经释放但仍被线程持有并访问的情况。
2. 分析报错栈，确认冲突代码位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。结合解析出的代码，分析问题根因。

### 关键字

此类问题一般可以通过日志中的关键字heap-use-after-free，确认为多线程并发内存释放后使用问题。

### 案例分析

**案例：**使用了已释放的内存

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==56349==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: heap-use-after-free (pid=56349)
     Write of size 4 at 0x005722327830 by main thread (mutexes: write M0):
       #0 0x57173e847c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8478) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #1 0x57173e8c00  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8bfc) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #2 0x55e496c2f8  (/system/lib64/platformsdk/libace_napi.z.so+0x6c2f4) (BuildId: 06ec1a6195a5c70310af542a69ff2ebe)

     Previous write of size 8 at 0x005722327830 by thread T56 (mutexes: write M0):
       #0 0x5556ff8290  (/system/lib64/libclang_rt.tsan.so+0x7828c) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #1 0x57173e83f0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a83ec) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #2 0x5556ff97f4  (/system/lib64/libclang_rt.tsan.so+0x797f0) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)

     Location is global '<null>' at 0x000000000000 ([anon:SizeClassAllocator]+0x27830)

     Mutex M0 (0x005717629080) created at:
       #0 0x5556ffb07c  (/system/lib64/libclang_rt.tsan.so+0x7b078) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #1 0x57173e8bd8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8bd4) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #2 0x55e496c2f8  (/system/lib64/platformsdk/libace_napi.z.so+0x6c2f4) (BuildId: 06ec1a6195a5c70310af542a69ff2ebe)

     Thread T56 (tid=56643, finished) created by main thread at:
       #0 0x5556ff9894  (/system/lib64/libclang_rt.tsan.so+0x79890) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #1 0x57173e8bf4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8bf0) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #2 0x55e496c2f8  (/system/lib64/platformsdk/libace_napi.z.so+0x6c2f4) (BuildId: 06ec1a6195a5c70310af542a69ff2ebe)

   SUMMARY: ThreadSanitizer: heap-use-after-free (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8478) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
   ```

   证据1：heap-use-after-free证明为多线程并发内存释放后使用问题。

   ```screen
   WARNING: ThreadSanitizer: heap-use-after-free (pid=56349)
   ```

   证据2：Write of size和Previous write of size表明两个线程对同一地址发生“写-写”冲突；Location is global表明冲突地址属于全局变量。

   ```screen
   Write of size 4 at 0x005722327830 by main thread (mutexes: write M0):
   ...
   Previous write of size 8 at 0x005722327830 by thread T56 (mutexes: write M0):
   ...
   Location is global '<null>' at 0x000000000000 ([anon:SizeClassAllocator]+0x27830)
   ```

   日志中表明主线程正在向地址0x005722327830对应的内存区域执行写操作，且访问该内存时持有互斥锁M0；线程T56在此之前对同一内存地址执行写操作，同时持有互斥锁M0。Location is global表示竞争对象位于全局变量区域，说明多个线程正在访问同一全局存储区域，存在数据竞争风险。
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/BMnDVyErSpmdRqVYNRQoeQ/zh-cn_image_0000002699732136.png "点击放大")

   1. 代码第88行：Previous write of size 8栈顶位置。
   2. 代码第95行：Write of size 4栈顶位置。多线程共享原始指针mem，虽然通过互斥锁保护了释放和访问操作，但未建立对象生命周期管理机制。释放线程执行free()后，其他线程仍可能通过旧指针访问已经释放的内存区域，导致内存释放后使用。

**问题结论与总结**

共享内存mem的释放和使用缺少生命周期约束，虽然通过mutex避免了同时访问，但无法保证访问发生在释放之前，造成多线程并发内存释放后使用问题。

**修复建议**

1. 建议在free释放内存后将指针置空，并增加空指针检查，确保不会导致多线程并发内存释放后使用现象。
2. 建议使用智能指针管理对象生命周期，避免通过裸指针手动控制对象释放时机。

## 信号处理非法修改errno

### 根因描述

信号处理函数在执行过程中可能修改当前线程保存的errno状态，覆盖主程序原有的错误码信息，导致后续错误处理逻辑获取到不正确的错误原因。由于信号可能在程序执行的任意时刻触发，若信号处理函数中调用了会修改errno的函数，且未提前保存并恢复原始errno，可能导致程序行为异常。

### 问题分析思路

信号处理非法修改errno通常由以下几种原因引起：

1. 信号处理函数中调用非异步信号安全函数，可能修改当前执行上下文的状态（包括errno），破坏主流程依赖的错误码信息。
2. 主程序在信号触发后立即检查errno。
3. 信号处理函数未保存/恢复errno。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字signal handler spoils errno，重点关注信号处理函数是否非法修改errno或调用非异步信号安全函数，分析信号触发过程中是否覆盖主线程原有错误状态，导致错误码异常或程序行为不符合预期。
2. 分析报错栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，解析调用栈，定位到具体代码行。结合解析出的代码，分析问题根因。重点检查在handler内部是否存在调用非异步信号安全函数、是否直接或间接修改errno等。

### 关键字

此类问题一般可以通过日志中的关键字signal handler spoils errno，确认为信号处理非法修改errno问题。

### 案例分析

**案例：**信号处理函数中修改了errno变量

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==25179==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: signal handler spoils errno (pid=25179)
     Signal 27 handler invoked at:
       #0 0x571452818c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8188) (BuildId: 3870db3853cf3654709c6af3560552f12c8c49c6)
       #1 0x57145282c4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a82c0) (BuildId: 3870db3853cf3654709c6af3560552f12c8c49c6)
       #2 0x5714528b64  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8b60) (BuildId: 3870db3853cf3654709c6af3560552f12c8c49c6)
       #3 0x55e7931c84  (/system/lib64/platformsdk/libace_napi.z.so+0x71c80) (BuildId: 450a6d44bdb4f26d59104e95c83ef40c)

   SUMMARY: ThreadSanitizer: signal handler spoils errno (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8188) (BuildId: 3870db3853cf3654709c6af3560552f12c8c49c6) 
   ==appspawn==25179==Process memory map follows:
   ```

   证据1：signal handler spoils errno证明为信号处理非法修改errno问题。

   ```screen
   WARNING: ThreadSanitizer: signal handler spoils errno (pid=25179)
   ```
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，对调用栈中的#0、#1和#2栈帧信息进行符号解析，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/8FYawawLSOO3MfDPih3AAA/zh-cn_image_0000002729491393.png)

   第63行代码表示信号处理函数破坏主程序原本的errno状态，errno是用于保存最近一次系统调用或库函数失败原因的错误码。如果信号处理函数修改了errno，会覆盖主程序原本有效的错误信息。

**问题结论与总结**

MyHandler中errno = 1的赋值破坏了错误码errno的设计用途，导致被中断的库函数或后续代码读取到错误的errno值，造成了信号处理非法修改errno。

**修复建议**

1. 避免直接在信号处理函数中使用errno。
2. 使用pthread\_mutex保护共享变量，替代信号机制。

## 信号处理调用非信号安全函数

### 根因描述

信号处理调用非信号安全函数是指在信号处理函数中调用了非异步信号安全函数。异步信号安全是指函数在被信号处理函数调用时，即使信号打断正常执行流程，也能够保证自身状态一致性，不会导致死锁、数据损坏或未定义行为。非异步信号安全函数在信号上下文中执行时，可能破坏内部状态，引发程序异常。

### 问题分析思路

信号处理调用非信号安全函数通常由以下几种原因引起：

* 信号处理函数与主程序竞争同一个锁。
* 信号处理函数调用内存管理函数时，可能与被中断的内存操作产生内部状态竞争。
* 信号处理函数修改主程序正在使用的全局状态。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字signal-unsafe call inside of a signal，重点关注信号处理函数中是否调用了非异步信号安全函数，分析这些函数是否可能引发死锁、数据状态破坏或不可预测行为。
2. 分析报错栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。结合解析出的代码，分析问题根因。例如信号上下文中调用了不允许调用的函数、信号打断持锁流程后再次进入锁保护逻辑，造成死锁风险和异步信号执行过程中修改了主流程依赖的数据，导致状态一致性破坏等。

### 关键字

此类问题一般可以通过日志中的关键字signal-unsafe call inside of a signal，确认为信号处理调用非信号安全函数问题。

### 案例分析

**案例：**信号处理函数中调用了非信号安全的函数

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==1115==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: signal-unsafe call inside of a signal (pid=1115)
       #0 0x5556ff7bd0  (/system/lib64/libclang_rt.tsan.so+0x77bcc) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #1 0x5717a681c0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a81bc) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #2 0x5557000eec  (/system/lib64/libclang_rt.tsan.so+0x80ee8) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
       #3 0x5717a68a54  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a8a50) (BuildId: c23646f8a2d025be0ecce4de074efdd30421f56c)
       #4 0x55e2b2c2f8  (/system/lib64/platformsdk/libace_napi.z.so+0x6c2f4) (BuildId: 06ec1a6195a5c70310af542a69ff2ebe)

   SUMMARY: ThreadSanitizer: signal-unsafe call inside of a signal (/system/lib64/libclang_rt.tsan.so+0x77bcc) (BuildId: 9e4eea1ddd93d526588139cd32aca12ad326c523)
   ```

   证据1：signal-unsafe call inside of a signal证明为信号处理调用非信号安全函数问题。

   ```screen
   WARNING: ThreadSanitizer: signal-unsafe call inside of a signal (pid=1115)
   ```
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析#1，定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/hVuDrCSJRkmAGIZCl9R67g/zh-cn_image_0000002699892020.png "点击放大")

   1. 代码第56行：调用了malloc()函数。
   2. 代码第58行：调用了free()函数，这两个函数不是异步信号安全函数，因此在信号处理上下文中调用会导致未定义行为。

**问题结论与总结**

信号处理函数handler中调用malloc()/free()等非异步信号安全函数。信号可能在任意执行点打断程序，handler执行期间无法保证函数内部状态安全，可能导致内存管理状态异常或程序不可预测行为，造成了信号处理调用非信号安全函数。

**修复建议**

1. 建议使用预分配的缓冲区替代malloc()/free()用法。
2. 建议使用volatile sig\_atomic\_t类型标志，避免动态内存操作。

## 非法重复解锁

### 根因描述

非法重复解锁是指对同一个同步原语（如互斥锁）执行超过其生命周期规则的解锁操作，例如重复解锁、解锁未持有的锁或由非持有线程释放锁。当锁的加锁与解锁操作不匹配时，会破坏同步原语的内部状态，可能导致未定义行为、程序异常或线程同步失效。

### 问题分析思路

非法重复解锁通常由以下几种原因引起：

1. 控制流分支导致的不平衡：在if-else、switch、异常处理等分支中，锁的获取和释放路径不一致。
2. 双重解锁：解锁两次同一把锁。
3. 跨线程解锁：一个线程尝试解锁另一个线程持有的锁。
4. 解锁未锁定的锁：程序在未获取锁的情况下调用unlock。

问题分析步骤如下：

1. 查看TSan日志中的报错关键字unlock of an unlocked mutex，重点关注线程是否对同一把锁执行了多次解锁操作，分析锁的加锁与解锁流程是否匹配，确认是否存在未持有锁时调用 unlock、异常流程提前释放锁、多个线程错误释放同一锁等情况。重点检查锁的生命周期管理和所有解锁路径，避免导致未定义行为、程序崩溃或同步状态异常。
2. 分析报错栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。结合解析出的代码，分析问题根因。

### 关键字

此类问题一般可以通过日志中的关键字unlock of an unlocked mutex，确认为非法重复解锁问题。

### 案例分析

**案例：**解锁一个已经解锁/自己不拥有的锁

**问题现象**

应用运行过程中触发TSan检测，应用闪退并生成TSan故障日志。

**问题分析**

1. 查看TSan日志中的报错关键字，确认故障类型。

   ```screen
   Reason:TSAN
   ==appspawn==47165==ThreadSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   ==================
   WARNING: ThreadSanitizer: unlock of an unlocked mutex (or by a wrong thread) (pid=47165)
       #0 0x5556b960d4  (/system/lib64/libclang_rt.tsan.so+0x960d0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)
       #1 0x57134e7ff0  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a7fec) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #2 0x57134e7ec8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a7ec4) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #3 0x57134e88b4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a88b0) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #4 0x55e8b71c84  (/system/lib64/platformsdk/libace_napi.z.so+0x71c80) (BuildId: 450a6d44bdb4f26d59104e95c83ef40c)

     Location is stack of main thread.

     Location is global '<null>' at 0x000000000000 ([stack]+0x7ef5a8)

     Mutex M0 (0x007fffff05a8) created at:
       #0 0x5556b7b07c  (/system/lib64/libclang_rt.tsan.so+0x7b078) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae)
       #1 0x57134e7e0c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a7e08) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #2 0x57134e7ea4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a7ea0) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #3 0x57134e88b4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x3a88b0) (BuildId: 5b10acd6634163d6c34262d172117b894406cd26)
       #4 0x55e8b71c84  (/system/lib64/platformsdk/libace_napi.z.so+0x71c80) (BuildId: 450a6d44bdb4f26d59104e95c83ef40c)

   SUMMARY: ThreadSanitizer: unlock of an unlocked mutex (or by a wrong thread) (/system/lib64/libclang_rt.tsan.so+0x960d0) (BuildId: 076da34c4d416d0e2540bbbb3105ad76348edaae) 
   ==appspawn==47165==Process memory map follows:
   ```

   证据1：unlock of an unlocked mutex证明为非法重复解锁问题。

   ```screen
   WARNING: ThreadSanitizer: unlock of an unlocked mutex (or by a wrong thread) (pid=47165)
   ```
2. 结合解析出的代码，分析问题根因。

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，完成调用栈解析#1，#2定位到具体代码行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/HM8zdti2RyeVcK6OdJ2KGQ/zh-cn_image_0000002729611347.png "点击放大")

   1. 代码第43行：执行第一次local\_lock.unlock()后，互斥锁已处于未锁定状态。
   2. 代码第44行：第二次调用local\_lock.unlock()时，pthread\_mutex\_unlock()尝试解锁一个未被任何线程持有的互斥锁，导致了非法重复解锁问题。

**问题结论与总结**

两次调用local\_lock.unlock()导致pthread\_mutex\_unlock()执行未定义操作，造成了非法重复解锁。

**修复建议**

1. 建议使用mutex管理锁的状态。
2. 添加is\_locked检查保护，防止重复解锁。
