---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memory-overflow-fault-mode
title: 内存越界访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 内存越界访问故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:ffc8eb5679f29381669e482b6bb295fa304339dcc4b9f68d54d1fea371ac6070
---

堆、栈内存对象均具有明确的有效地址范围。索引计算错误可能导致程序读写对象边界之外的地址，引发内存越界访问，造成数据异常或应用崩溃。开启检测能力后，可在越界访问时记录异常地址、访问大小和现场调用栈等信息。

本文结合HWASan（Hardware-assisted AddressSanitizer）、ASan（AddressSanitizer）和GWP-ASan（GWP-ASan Will Provide Allocation SANity）典型案例，介绍堆、栈内存越界访问的日志特征与定位方法，具体包括：

* [HWASan堆内存越界访问](bpta-stability-memory-overflow-fault-mode.md#section736683302917)
* [ASan堆内存越界访问](bpta-stability-memory-overflow-fault-mode.md#section1856818444350)
* [GWP-ASan堆内存越界访问](bpta-stability-memory-overflow-fault-mode.md#section76131953611)
* [HWASan栈内存越界访问](bpta-stability-memory-overflow-fault-mode.md#section03007321117)
* [ASan栈内存越界访问](bpta-stability-memory-overflow-fault-mode.md#section17970836152619)

## HWASan堆内存越界访问

### 根因描述

堆内存越界访问，通常是指代码访问了堆上已申请内存块边界之外的区域，包括上越界和下越界两类。此类问题本质上是：程序申请了一段堆内存，但后续使用时，下标、偏移、长度或对象大小计算错误，导致访问超出了该堆对象的合法范围。当应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测能力后，运行时会对指针和内存标签进行校验。一旦访问越过堆对象边界，应用就会因触发tag-mismatch异常而退出。

### 问题分析思路

此类问题，通常情况下，会有如下几种可能：

1. 申请内存大小与实际使用大小不匹配。
2. 数组下标、偏移量、循环边界计算错误。
3. memcpy()、memmove()、memset()、strcpy()等接口长度传参错误。

问题分析步骤如下：

1. 查看HWASan日志中的报错关键字段，确认故障类型。重点关注是否存在heap-buffer-overflow等信息。若日志中已明确给出Cause: heap-buffer-overflow，可初步将问题定性为堆内存越界访问。同时结合READ/WRITE of size等字段，区分本次异常属于读越界还是写越界。
2. 分析日志中is located X bytes to the right/left of Y-byte region等信息，判断越界发生在对象左边界还是右边界，并确认越界了多少size。由于HWASan判定机制原因，如果size超过1000以上，优先怀疑是use-after-free的问题。
3. 分析报错栈，通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
4. 分析分配栈，确认堆对象由哪个函数申请，并结合申请大小、使用方式等信息，进一步判断越界产生的原因。
5. 若步骤1~4仍无法定位根因，且发现分配栈和报错栈没有关联，可以查看是否存在ringbuffer满了的情况。HWASan依赖ringbuffer记录分配栈，在高频malloc()/free()的场景下，ringbuffer可能被写满并覆盖历史记录。建议修改ringbuffer上限大小并重新复现压测。

### 关键字

重点关注heap-buffer-overflow、READ/WRITE、right of/left等字段，用于确认故障类型、访问类型（读/写）及越界方向。确认是堆内存越界访问后，优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：字符串缺少结束符导致对内存上越界

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志，故障日志显示为heap-buffer-overflow读越界。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Cause: heap-buffer-overflow，并显示当前异常为READ of size 1，可初步确认该问题属于堆内存越界读。

   ```screen
   Module name:XXXXX
   Version:6.0.0.735
   Pid:18212
   Uid:20020052
   Reason:heap-buffer-overflow
   ==appspawn==18212==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000100f466e1 at pc 0x005a430f9d38
   READ of size 1 at 0x000100f466e1 tags: f9/01(f9) (ptr/mem) in thread 18310
       #0 0x5a430f9d38  (/lib/ld-musl-aarch64-asan.so.1+0x19ed38) (BuildId: c6e182d3bbb6f96e51d042120532d4b3)
       #1 0x5ab5d88f0c  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x5c8f0c) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
       #2 0x5ab5b1a0ac  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x35a0ac) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
       ...

   [0x000100f466e0,0x000100f46700) is a small allocated heap chunk; size: 32 offset: 1, Allocated By 18310
   Currently allocated here:
       #0 0x5a4446b970  (/system/asan/lib64/libclang_rt.hwasan.so+0x2b970) (BuildId: a2031fbf7d31e0be7d1e53fa375bc405637a720b)
       #1 0x5ab5b1a0ac  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x45a0ac) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
       ...
   Cause: heap-buffer-overflow
   0x000100f466e1 is located 0 bytes to the right of 1-byte region [0x000100f466e0,0x000100f466e1)
   allocated here:
       #0 0x5a4446b970  (/system/asan/lib64/libclang_rt.hwasan.so+0x2b970) (BuildId: a2031fbf7d31e0be7d1e53fa375bc405637a720b)
       #1 0x5ab5b1a0ac  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x45a0ac) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
       ...
   ```
2. 分析越界边界信息，确认越界特征。

   证据2：信息表明，异常属于上越界，且刚刚越过申请内存的边界。

   ```screen
   Cause: heap-buffer-overflow
   0x000100f466e1 is located 0 bytes to the right of 1-byte region [0x000100f466e0,0x000100f466e1)
   ```

   该越界地址位于[0x000100f466e0,0x000100f466e1)这段1字节堆区域的右边界之外，表明代码在读取一个比较小的堆对象时继续向后访问，最终触发HWASan检测。
3. 分析报错栈，定位触发异常的位置。

   证据3：

   ```screen
   ==appspawn==18212==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000100f466e1 at pc 0x005a430f9d38
   READ of size 1 at 0x000100f466e1 tags: f9/01(f9) (ptr/mem) in thread 18310
       #0 0x5a430f9d38  (/lib/ld-musl-aarch64-asan.so.1+0x19ed38) (BuildId: c6e182d3bbb6f96e51d042120532d4b3)
       #1 0x5ab5d88f0c  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x5c8f0c) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
   ```

   通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用），解析报错栈除系统库外的第一个业务栈，定位到具体的代码行，命令如下：

   ```screen
   llvm-addr2line -Cfpie /data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so 0x5c8f0c
   ```

   解析后代码如下图所示，越界发生在位置1：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/aeEZ416VSxqGMdltT0y-ng/zh-cn_image_0000002693605642.png)

   应用侧将imageValue.data传入atoi()的流程中。atoi()是基于C字符串语义的接口，它会一直循环遍历字符串，直到遇到非数字字符或'\0'才停止。因此，如果传入的数据没有以'\0'结尾，则atoi()会继续向后读取，存在越界风险。初步猜测，该问题可能与字符串未加结束符相关。继续追溯数据来源发现，imageValue.data由位置2处通过引用赋值得到，因此需要进一步分析OH\_PictureMetadata\_GetProperty()接口里对imageValue.data的赋值流程。
4. 分析分配栈，进一步确认产生越界的原因。

   证据4：

   ```screen
   Cause: heap-buffer-overflow
   0x000100f466e1 is located 0 bytes to the right of 1-byte region [0x000100f466e0,0x000100f466e1)
   allocated here:
       #0 0x5a4446b970  (/system/asan/lib64/libclang_rt.hwasan.so+0x2b970) (BuildId: a2031fbf7d31e0be7d1e53fa375bc405637a720b)
       #1 0x5ab5b1a0ac  (/data/storage/el1/bundle/com.huawei.hmos.photobrowser/browserlibrary/libs/arm64/libHuaweiImageEditor.so+0x45a0ac) (BuildId: 69576485bdb7e5e28f6ce1245c8e137b168b5828)
   ```

   解析分配栈#1，定位到具体业务代码行如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/e7OGV1lmSJy9GkyzBcMeAQ/zh-cn_image_0000002723285073.png)

   结合源码发现，1号位置传入的value变量是通过2号位置的memcpy\_s()拷贝得到。source传入的是字符串指针，实际包含末尾的'\0'结束符；但source\_size却直接使用val.size()，该值仅统计有效字符长度，不包含末尾的'\0'。因此，回调返回的字符串本身未显式包含'\0'结束符，后续继续按照C字符串处理，导致堆内存上越界访问。

**问题结论与总结**

该问题的根本原因是：OH\_PictureMetadata\_GetProperty()返回的字符串未加末尾'\0'结束符，但调用方将其作为C字符串传入atoi()处理，导致atoi()持续向后读取并最终发生堆内存读越界。

**修复建议**

atoi()属于危险函数，对于通过外部接口获取的数据，应做校验如数据长度是否合法、是否以'\0'结尾、是否确实为数字字符串等，避免未经校验直接传入atoi()、strlen()、strcmp()等依赖C字符串约定的接口。

**案例二**：未校验缓冲区边界导致堆内存上越界

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志，故障日志显示为heap-buffer-overflow写越界。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Cause: heap-buffer-overflow，并显示当前异常为WRITE of size 1，可初步确认该问题属于堆内存越界写。

   ```screen
   Module name:com.example.sanitzerdemo
   Version:1.0.0
   Pid:59315
   Uid:20020225
   Reason:heap-buffer-overflow
   ==appspawn==59315==ERROR: HWAddressSanitizer: tag-mismatch on address 0x00010065518a at pc 0x00622e54fc9c
   WRITE of size 1 at 0x00010065518a tags: 06/0a(06) (ptr/mem) in thread 59315
       #0 0x622e54fc9c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xfc9c) (BuildId: e3e597aa173012c654732b13c047067e1886992b)
       #1 0x622e54fb74  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xfb74) (BuildId: e3e597aa173012c654732b13c047067e1886992b)
       #2 0x622e5503bc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x103bc) (BuildId: e3e597aa173012c654732b13c047067e1886992b)
       #3 0x6210072e54  (/system/lib64/platformsdk/libace_napi.z.so+0x72e54) (BuildId: 1b237bc53a63dae13a2b44989f68017a)

   [0x000100655180,0x0001006551a0) is a small allocated heap chunk; size: 32 offset: 10, Allocated By 59315

   Cause: heap-buffer-overflow
   0x00010065518a is located 0 bytes to the right of 10-byte region [0x000100655180,0x00010065518a)
   allocated here:
       #0 0x617fbe4a94  (/system/lib64/libclang_rt.hwasan.so+0x24a94) (BuildId: 0e5c342d2c6f83688605941d1eb2b8b10d075263)
       #1 0x622e54fb08  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xfb08) (BuildId: e3e597aa173012c654732b13c047067e1886992b)
       #2 0x622e5503bc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x103bc) (BuildId: e3e597aa173012c654732b13c047067e1886992b)
       #3 0x6210072e54  (/system/lib64/platformsdk/libace_napi.z.so+0x72e54) (BuildId: 1b237bc53a63dae13a2b44989f68017a)
   ```
2. 分析越界边界信息，确认越界特征。

   证据2：该信息说明，异常地址正好位于申请内存右边界之外，属于典型的“刚越过边界”的写越界。这块内存的大小是10 byte。

   ```screen
   Cause: heap-buffer-overflow
   0x00010065518a is located 0 bytes to the right of 10-byte region [0x000100655180,0x00010065518a)
   ```
3. 分析报错栈，定位触发异常的位置。

   证据3：解析调用栈，定位到具体业务代码行如下图所示，越界访问发生在位置1：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/8pvKHTPtRHCduzZUNquUGg/zh-cn_image_0000002693765528.png)

   Append()函数会直接将字符写入buffer\_[length]，然后自增length。此处明显是个危险操作，如果length超过buffer的大小，就会发生写越界。

**问题结论与总结**

该问题的根本原因是：字符串写入时未加校验，当length超过buffer大小后，仍继续追加字符。

**修复建议**

字符串写入时，应增加边界校验，确保写入长度不超过目标缓冲区大小。

**案例三**：ringbuffer满了导致堆栈非现场

**问题现象**

分析已有堆栈，无法确认根因，堆栈非第一现场。

**问题分析**

证据1：

```screen
Module name:xxxx
Version:5.1.5.353
Pid:24864
Uid:20020042
Reason:heap-buffer-overflow
==appspawn==24864==ERROR: HWAddressSanitizer: tag-mismatch on address 0x000600146000 at pc 0x00599f120840
READ of size 8 at 0x000600146000 tags: df/40 (ptr/mem) in thread 24864
#0 0x599f120840  (/data/storage/el1/bundle/arkwebcore_asan/libs/arm64//libarkweb_engine.so+0x7ae0840) (BuildId: 3dc2d56f0c958c088f6ef139a6a3e3953e8b814b)
#1 0x599fa894d0  (/data/storage/el1/bundle/arkwebcore_asan/libs/arm64//libarkweb_engine.so+0x84494d0) (BuildId: 3dc2d56f0c958c088f6ef139a6a3e3953e8b814b)
#2 0x599f5d1eec  (/data/storage/el1/bundle/arkwebcore_asan/libs/arm64//libarkweb_engine.so+0x7f91eec) (BuildId: 3dc2d56f0c958c088f6ef139a6a3e3953e8b814b)
 
[0x000600146000,0x0006001460c0) is a small unallocated heap chunk; size: 192 offset: 0, Allocated By 25010
Searched 1086630 records, find 0 with same addr 0x000600146000

Cause: heap-buffer-overflow
0x000600146000 is located 9216 bytes to the left of 168-byte region [0x000600148400,0x0006001484a8)
allocated here:
#0 0x595ec6b03c  (/system/asan/lib64/libclang_rt.hwasan.so+0x2b03c) (BuildId: 85ec92e5c808b63464374c75fb5f422d1fcabbac): 
#1 0x599a6a62f4  (/data/storage/el1/bundle/arkwebcore_asan/libs/arm64//libarkweb_engine.so+0x30662f4) (BuildId: 3dc2d56f0c958c088f6ef139a6a3e3953e8b814b)
#2 0x599a6a619c  (/data/storage/el1/bundle/arkwebcore_asan/libs/arm64//libarkweb_engine.so+0x306619c) (BuildId: 3dc2d56f0c958c088f6ef139a6a3e3953e8b814b)
 
Thread: T0 0x005a00002000 stack: [0x007fa37a6000,0x007fa3fa5000) sz: 8384512 tls: [0x00595dc6b290,0x00595dc6ba18) rb:(1023000/1023000) records(25065821/o:0) tid: 24864
Thread: T1 0x005a00006000 stack: [0x00598926f000,0x00598946f720) sz: 2098976 tls: [0x00598946f720,0x005989487a29) rb:(0/1023) records(0/o:0) tid: 24876
Thread: T2 0x005a0000a000 stack: [0x00598926f000,0x00598946f720) sz: 2098976 tls: [0x00598946f720,0x005989487a29) rb:(2/1023) records(2/o:0) tid: 24876
...
Thread: T68 0x005a00112000 stack: [0x0059b5851000,0x0059b5a51e80) sz: 2100864 tls: [0x0059b5a51e80,0x0059b5a6c8a1) rb:(1023/1023) records(71212/o:0) tid: 25010
```

对日志进行解栈分析后发现，按照步骤1~4无法定位根因，调用栈为非现场栈，可进一步分析相关线程的ringbuffer占用情况。ringbuffer用于记录线程近期的堆内存分配、释放等历史信息，写满后新记录会覆盖较早的记录。本案例异常涉及主线程（tid:24864）和子线程（tid:25010），两个线程的ringbuffer状态如下：

```screen
Thread: T0 0x005a00002000 stack: [0x007fa37a6000,0x007fa3fa5000) sz: 8384512 tls: [0x00595dc6b290,0x00595dc6ba18) rb:(1023000/1023000) records(25065821/o:0) tid: 24864
Thread: T68 0x005a00112000 stack: [0x0059b5851000,0x0059b5a51e80) sz: 2100864 tls: [0x0059b5a51e80,0x0059b5a6c8a1) rb:(1023/1023) records(71212/o:0) tid: 25010
```

主线程和子线程的ringbuffer占用分别为1023000/1023000和1023/1023，均已达到容量上限，说明两个线程的ringbuffer均已写满。其中，rb格式为“当前占用条目数/容量上限”，表示ringbuffer的使用情况，records表示该线程累计记录的内存操作次数，可作为ringbuffer实际需求容量的参考上限。

当records明显超过ringbuffer上限时，表明在运行过程中，新数据已多次覆盖了ringbuffer中的分配栈记录，从而可能导致历史分配栈丢失。本案例中，主线程records达到25065821，子线程达到71212，均远大于各自ringbuffer容量（1023000和1023），说明记录的栈可能已经被覆盖。

**问题结论与总结**

HWASan依赖ringbuffer记录内存分配栈和报错栈。在高频malloc()/free()或高并发场景下，ringbuffer可能被快速写满并覆盖历史记录，导致历史栈信息丢失，调用栈为非现场栈，从而影响问题定位。

**修复建议**

可通过在app.json5中配置heap\_history\_size和heap\_history\_size\_main\_thread参数，适当增大ringbuffer容量后重新压测复现问题。示例如下：

```json
{
  "app": {
    "appEnvironments": [
      {
        "name": "HWASAN_OPTIONS",
        "value": "heap_history_size=10230 heap_history_size_main_thread=10230000"
      },
    ],
    ...
  }
}
```

参数说明如下：

| 参数 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| heap\_history\_size | 1023 | 否 | 指定各个线程用于保存其堆内存释放记录的ringbuffer容量。 |
| heap\_history\_size\_main\_thread | 102300 | 否 | 指定主线程用于保存其堆内存释放记录的ringbuffer容量。 |

## ASan堆内存越界访问

### 根因描述

当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测能力后，会在堆对象前后插入redzone，并通过影子内存（Shadow Memory）标记应用内存是否可访问。当程序访问到堆对象边界之外的redzone区域时，ASan会检测到非法访问，并上报heap-buffer-overflow，应用进程通常会中止退出。

### 问题分析思路

此类问题，通常情况下，会有如下几种可能：

1. 申请内存大小与实际使用大小不匹配。
2. 数组下标、偏移量、循环边界计算错误。
3. memcpy()、memmove()、memset()、strcpy()等接口长度传参错误。

问题分析步骤如下：

1. 查看ASan日志中的报错关键字段，确认故障类型。重点关注是否存在heap-buffer-overflow等信息。若日志中已明确给出heap-buffer-overflow，可初步将问题定性为堆内存越界访问。同时结合READ/WRITE of size等字段，区分本次异常属于读越界还是写越界。
2. 分析日志中is located X bytes to the right/left of Y-byte region [start, end)等信息，判断是上越界还是下越界，并确认越界了多少size。
3. 分析报错栈，llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
4. 分析分配栈，确认堆对象由哪个函数申请，并结合申请大小、使用方式等信息，进一步判断越界产生的原因。
5. 结合ASan Shadow信息辅助确认。ASan日志中的Shadow bytes可辅助判断异常地址所处内存状态。

### 关键字

重点关注heap-buffer-overflow、READ/WRITE、right/left of等字段，用于确认故障类型、访问类型（读/写）、越界方向和内存分配位置。确认属于堆内存越界访问后，优先分析业务侧调用栈帧及对应代码，并结合分配栈和Shadow bytes信息辅助定位根因。

### 案例分析

**案例一**：未校验缓冲区边界导致堆内存上越界

**问题现象**

应用运行过程中触发ASan检测，应用闪退并生成ASan故障日志，故障日志显示为heap-buffer-overflow写越界。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出heap-buffer-overflow，并显示当前异常为WRITE of size 1，可确认该问题属于堆内存上越界写。

   ```screen
   Module name:xxxx
   Version:6.1.0.166
   Pid:7769
   Uid:20020064
   Reason:heap-buffer-overflow
   ==appspawn==46804==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x006dd7c7c080 at pc 0x007c07f56bf0 bp 0x007fec4a81e0 sp 0x007fec4a81d8
   WRITE of size 1 at 0x006dd7c7c080 thread T0 (xample.dfx_test)
       #0 0x7c07f56bec  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x256bec) (BuildId: 749b1ab3684661ce4f308078e717067b1486605a)
       #1 0x7ade2a7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #2 0x7fee9c29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #3 0x7fee016900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
    
   0x006dd7c7c080 is located 0 bytes to the right of 1024-byte region [0x006dd7c7bc80,0x006dd7c7c080)
   allocated by thread T0 (xample.dfx_test) here:
       #0 0x5a56eab758  (/system/lib64/libclang_rt.asan.so+0xeb758) (BuildId: e535b144d2e5a0b26e777a78001e130175ae94be)
       #1 0x7c07f56b6c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x256b6c) (BuildId: 749b1ab3684661ce4f308078e717067b1486605a)
       #2 0x7ade2a7c90  (/system/lib64/platformsdk/libace_napi.z.so+0x67c90) (BuildId: 76bc1ed675edcc5f429a976d6c9b955d)
       #3 0x7fee9c29f4  (/system/lib64/module/arkcompiler/stub.an+0xe179f4)
       #4 0x7fee016900  (/system/lib64/module/arkcompiler/stub.an+0x46b900)
    
   SUMMARY: AddressSanitizer: heap-buffer-overflow (/data/storage/el1/bundle/libs/arm64/libentry.so+0x256bec) (BuildId: 749b1ab3684661ce4f308078e717067b1486605a) 
   Shadow bytes around the buggy address:
     0x001dbaf8f7c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     0x001dbaf8f7d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     0x001dbaf8f7e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     0x001dbaf8f7f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
     0x001dbaf8f800: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   =>0x001dbaf8f810:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001dbaf8f820: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001dbaf8f830: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001dbaf8f840: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001dbaf8f850: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
     0x001dbaf8f860: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   Shadow byte legend (one shadow byte represents 8 application bytes):
     Addressable:           00
     Partially addressable: 01 02 03 04 05 06 07 
     Heap left redzone:       fa
     Freed heap region:       fd
     Stack left redzone:      f1
     Stack mid redzone:       f2
     Stack right redzone:     f3
     Stack after return:      f5
     Stack use after scope:   f8
     Global redzone:          f9
     Global init order:       f6
     Poisoned by user:        f7
     Container overflow:      fc
     Array cookie:            ac
     Intra object redzone:    bb
     ASan internal:           fe
     Left alloca redzone:     ca
     Right alloca redzone:    cb
   ```
2. 分析越界边界信息，确认越界特征。

   证据2：该信息说明，这块内存的申请大小是1024，且异常地址正好位于申请内存的右边界上，属于上越界。

   ```screen
   0x006dd7c7c080 is located 0 bytes to the right of 1024-byte region [0x006dd7c7bc80,0x006dd7c7c080)
   ```
3. 分析报错栈，定位触发异常的位置。

   证据3：解析调用栈llvm-addr2line -Cfipe libentry.so 0x256bec，定位到具体业务代码如下图所示，越界访问发生在位置1：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/mKlHvrtPRTG8STTxd70qNg/zh-cn_image_0000002723404999.png)

   该行在循环中持续写入heap\_buffer，但循环上限是1500，超过了实际申请的1024 字节缓冲区大小，因此在i == 1024时触发写越界。
4. 结合ASan Shadow信息辅助确认。

   证据4：

   ```screen
   Shadow bytes around the buggy address:
     ...
     0x001dbaf8f800: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   =>0x001dbaf8f810:[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
   ```

   异常地址对应的Shadow值为 fa，fa表示堆内存redzone，即ASan在堆对象边界外插入的不可访问区域，用于检测堆越界访问。其中，Shadow值00表示对应映射内存可正常访问，fa表示对应内存不可访问。从日志可以看出，异常地址落在连续可访问区域00右侧的第一个fa位置，可以辅助判断该问题属于堆内存上越界。

**问题结论与总结**

该问题是由于业务代码申请了1024字节堆内存，但实际循环写入1500字节，导致访问超过堆对象合法范围。属于典型的内存申请与使用不匹配，没有注意数组边界。

**修复建议**

确保申请内存大小与实际写入长度一致，写入前校验数组下标和buffer大小。

## GWP-ASan堆内存越界访问

### 根因描述

当应用[GWP-ASan使能](bpta-stability-gwpasan-detection.md#section2735718353)后，运行时会对堆内存分配进行采样，并将命中采样的堆对象分配至特殊的受保护内存区域。当程序访问超出对象边界的保护页时，GWP-ASan会捕获该非法内存访问行为，并生成相应的故障日志。

### 问题分析思路

此类问题，通常情况下，会有如下几种可能：

1. 申请内存大小与实际使用大小不匹配。
2. 数组下标、偏移量、循环边界计算错误。
3. memcpy()、memmove()、memset()、strcpy()等接口长度传参错误。

问题分析步骤如下：

1. 查看日志中的报错关键字段，确认故障类型。重点关注是否存在Buffer Overflow/Underflow等信息。
2. 分析越界边界信息，确认越界位置。分析日志中X bytes to the left of a Y-byte allocation at等信息，判断越界发生在对象左边界还是右边界，并确认越界了多少size。
3. 分析报错栈，llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
4. 分析分配栈，确认堆对象由哪个函数申请，并结合申请大小、使用方式等信息，进一步判断越界产生的原因。

### 关键字

此类问题日志关键词为：Buffer Overflow/Underflow。确认是堆内存越界类型的故障后，优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：字节数与元素下标混用导致堆内存上越界

**问题现象**

应用运行时触发GWP-ASan检测，生成故障日志，显示Buffer Overflow越界。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Buffer Overflow，说明当前访问地址位于所申请堆内存的右边界之外，属于堆内存上越界访问。

   ```screen
   *** GWP-ASan detected a memory error ***
   Buffer Overflow at 0x5bfb29c000 (4096 bytes to the right of a 1024-byte allocation at 0x5bfb29b000) by thread 18082 here:
    #0 0x5d555c93e4  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x93e4) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #1 0x5d555ccdec  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcdec) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #2 0x5d555ccd84  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcd84) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #3 0x5d555cc884  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xc884) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #4 0x5b4b8cea54  (/lib/ld-musl-aarch64.so.1+0x1dca54) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #5 0x5b4b7a6394  (/lib/ld-musl-aarch64.so.1+0xb4394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
   0x5bfb29c000 was allocated by thread 18082 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dad0  (/lib/ld-musl-aarch64.so.1+0x14bad0) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 0x5b4b860168  (/lib/ld-musl-aarch64.so.1+0x16e168) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #3 0x5b4b8e8e88  (/lib/ld-musl-aarch64.so.1+0x1f6e88) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #4 0x5d555c93d0  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x93d0) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #5 0x5d555ccdec  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcdec) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #6 0x5d555ccd84  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcd84) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #7 0x5d555cc884  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xc884) (BuildId: bd62f2189214ed4486ec200dbf54542ff571104d)
    #8 0x5b4b8cea54  (/lib/ld-musl-aarch64.so.1+0x1dca54) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #9 0x5b4b7a6394  (/lib/ld-musl-aarch64.so.1+0xb4394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
   *** End GWP-ASan report ***
   ```
2. 分析越界边界信息，确认越界特征。

   证据2：

   ```screen
   at 0x5bfb29c000 (4096 bytes to the right of a 1024-byte allocation at 0x5bfb29b000)
   ```

   申请内存起始地址为0x5bfb29b000，申请大小为1024字节，随后异常访问地址为0x5bfb29c000，该地址已超出申请内存的右边界3072字节（4096-1024）。因此，本次访问属于距离起始内存块较远的堆内存上越界访问。
3. 分析报错栈，定位触发异常的位置。

   证据3：解析报错栈llvm-addr2line -Cfipe libsample.so 0x93e4，定位到具体业务代码如下图所示，越界访问发生在位置1：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/KKuR0-BrQS-X9vy8qi4JYQ/zh-cn_image_0000002693605644.png)

   malloc(bufferSize)申请了1024字节的堆内存，而buffer的类型为int\*。1个int占4字节，因此该内存最多只能存放256个 int，合法下标范围为buffer[0]至buffer[255]。代码中使用buffer[bufferSize]，实际访问的是buffer[1024]，对应相对起始地址4096字节的偏移（1024 × 4）。该地址已经超出所申请内存的右边界3072字节，与日志中4096 bytes to the right of a 1024-byte allocation的描述一致。因此，本次问题的根因是将表示字节数的bufferSize直接作为int数组下标使用，造成字节数与元素个数混用，最终触发堆内存上越界访问。

**问题结论与总结**

该问题是由于业务代码将申请内存的字节数误用作数组下标。代码申请了1024字节堆内存，该内存仅能容纳256个int元素，但实际访问了buffer[1024]，导致访问地址远超所申请内存的右边界，最终触发堆内存上越界。

**修复建议**

申请数组内存时，应明确区分字节数和元素个数，并保证访问下标小于实际元素数量。可根据申请的字节数计算可容纳的元素个数。

**案例二**：负下标访问导致堆内存下越界

**问题现象**

应用运行时触发GWP-ASan检测，生成故障日志，显示Buffer Overflow越界。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出Buffer Underflow，说明当前访问地址位于申请堆内存的左边界之外，属于堆内存下越界访问。

   ```screen
   *** GWP-ASan detected a memory error ***
   Buffer Underflow at 0x5bfb29cffc (4 bytes to the left of a 1024-byte allocation at 0x5bfb29d000) by thread 61754 here:
    #0 0x5d55749460  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x9460) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #1 0x5d5574cdf0  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcdf0) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #2 0x5d5574cd88  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcd88) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #3 0x5d5574c888  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xc888) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #4 0x5b4b8cea54  (/lib/ld-musl-aarch64.so.1+0x1dca54) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #5 0x5b4b7a6394  (/lib/ld-musl-aarch64.so.1+0xb4394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
   0x5bfb29cffc was allocated by thread 61754 here:
    #0 0x5b4b83e394  (/lib/ld-musl-aarch64.so.1+0x14c394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #1 0x5b4b83dad0  (/lib/ld-musl-aarch64.so.1+0x14bad0) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #2 0x5b4b860168  (/lib/ld-musl-aarch64.so.1+0x16e168) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #3 0x5b4b8e8e88  (/lib/ld-musl-aarch64.so.1+0x1f6e88) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #4 0x5d55749454  (/data/storage/el1/bundle/libs/arm64/libsample.so+0x9454) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #5 0x5d5574cdf0  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcdf0) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #6 0x5d5574cd88  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xcd88) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #7 0x5d5574c888  (/data/storage/el1/bundle/libs/arm64/libsample.so+0xc888) (BuildId: 00b8f3471cfecb119d13fe4d8c227253fee9cae4)
    #8 0x5b4b8cea54  (/lib/ld-musl-aarch64.so.1+0x1dca54) (BuildId: 35422f66114500c7d794bf84b3fd302b)
    #9 0x5b4b7a6394  (/lib/ld-musl-aarch64.so.1+0xb4394) (BuildId: 35422f66114500c7d794bf84b3fd302b)
   *** End GWP-ASan report ***
   ```
2. 分析越界边界信息，确认越界特征

   证据2：

   ```screen
   at 0x5bfb29cffc (4 bytes to the left of a 1024-byte allocation at 0x5bfb29d000)
   ```

   申请内存起始地址为0x5bfb29d000，申请大小为1024字节，然后异常访问地址为0x5bfb29cffc，异常地址位于申请内存起始地址左边界4字节。因此，本次访问属于堆内存下越界。
3. 分析报错栈，定位触发异常的位置。

   证据3：解析报错栈 llvm-addr2line -Cfipe libsample.so+0x9460，定位到具体业务代码如下图所示，越界访问发生在位置1：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4-u4ClxXQSewSGDMbrXHrQ/zh-cn_image_0000002723285075.png)

   buffer[-1]会访问buffer起始地址之前的一个int。一个int为4字节，因此正好对应日志中的：4 bytes to the left of a1024-byte allocation。

**问题结论与总结**

该问题是由于业务代码申请了1024字节堆内存，但实际访问了申请内存起始地址之前的4字节区域，导致访问超过堆对象合法范围。本问题属于典型的数组下标越界，根因是访问数组时未校验下标下限。

**修复建议**

确保访问堆内存前校验数组下标和buffer边界，禁止使用负下标访问数组。

## HWASan栈内存越界访问

### 根因描述

栈内存越界，是指程序向栈区申请了特定的内存空间后，在读写数据时超出了该空间设定的边界，导致访问了不属于它的内存区域，从而引发程序数据损坏或逻辑异常，包含上越界和下越界。当应用[开启HWASan](../harmonyos-guides/ide-hwasan.md#section38898177587)检测能力后，运行时会对指针和内存标签进行校验。一旦访问越过保护页，应用就会触发stack tag-mismatch异常进而退出。

### 问题分析思路

此类问题，通常情况下，有几种可能：

1. 栈上局部变量内存大小与实际使用大小不匹配，如字符串操作不当。
2. 数组下标越界，如偏移量、循环边界计算错误。

问题分析步骤如下：

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。
2. 分析报错栈，llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
3. 结合业务代码，进一步判断越界产生的原因。

### 关键字

此类问题日志关键词为：stack tag-mismatch。确认是栈内存越界类型的故障后，优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：负下标访问导致栈内存下越界

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志，故障日志显示为stack tag-mismatch写越界。

**问题分析**

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。

   证据1：日志中给出stack tag-mismatch，说明是一个栈内存使用错误。同时WRITE of size 1 at 0x007e30edbc9f表示程序向地址0x007e30edbc9f写入1字节时触发异常。

   ```screen
   Reason:stack tag-mismatch
   ==appspawn==8081==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e30edbc9f at pc 0x00650153840c
   WRITE of size 1 at 0x007e30edbc9f tags: 5c/00 (ptr/mem) in thread 8081
       #0 0x650153840c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb840c) (BuildId: 8b63901e46d3a0ce16ac9bf84bf3dbc1be014da8)
       #1 0x5aec17010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Cause: stack tag-mismatch
   Address 0x007e30edbc9f is located in stack of thread 8081
   Thread: T0 0x005b00002000 stack: [0x007e306ea000,0x007e30ee9000) sz: 8384512 tls: [0x005a5cfd18f0,0x005a5cfd1feb) rb:(102300/102300/102300) records(1403725/o:0) tid: 8081
   ```
2. 分析报错栈，定位到具体业务代码行。

   证据2：通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行。

   ```screen
   ==appspawn==8081==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e30edbc9f at pc 0x00650153840c
   WRITE of size 1 at 0x007e30edbc9f tags: 5c/00 (ptr/mem) in thread 8081
       #0 InjectStackBufferUnderflow(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:306)
       #1 0x5aec17010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
   ```

   通过解析后的#0帧信息可以直观地看出，触发本次内存异常的具体位置为napi\_init.cpp文件的第306行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/38uL5Zc1QhyC55NlhnjOfA/zh-cn_image_0000002693765530.png)
3. 结合业务代码，进一步判断越界产生的原因。

   程序定义了包含42个char元素的数组，合法索引范围是buffer[0]到buffer[41]，buffer[subscript]试图访问第-1个元素，是栈内存下越界访问。

**问题结论与总结**

该问题属于典型的数组下标越界问题，使用了buffer[subscript]试图访问第-1个元素，没有注意数组左边界。

**修复建议**

校验数组下标和buffer边界，禁止使用超过边界的下标访问数组。

**案例二**：内存拷贝超出缓冲区边界导致栈内存上越界

**问题现象**

应用运行过程中触发HWASan检测，应用闪退并生成HWASan故障日志，故障日志显示为stack tag-mismatch写越界。

**问题分析**

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。

   证据1：日志中给出stack tag-mismatch，说明是一个栈内存使用错误。同时WRITE of size 5 at 0x007e093b2cd3表示程序向地址0x007e093b2cd3写入5字节时触发异常。

   ```screen
   Reason:stack tag-mismatch
   ==appspawn==49272==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e093b2cd3 at pc 0x005ac88a7178
   WRITE of size 5 at 0x007e093b2cd3 tags: 96/06(96) (ptr/mem) in thread 49272
   Invalid access starting at offset 3
       #0 0x5ac88a7178  (/system/lib64/libclang_rt.hwasan.so+0x27178) (BuildId: 29cd839fde93692a63b6bd1b64b35830f6de6e33)
       #1 0x5b70af7e08  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb7e08) (BuildId: a12eb0b9ce683ad6964819d87f4b992d31c33409)
       #2 0x5b53db010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Cause: stack tag-mismatch
   Address 0x007e093b2cd3 is located in stack of thread 49272
   Thread: T0 0x005c00002000 stack: [0x007e08bc1000,0x007e093c0000) sz: 8384512 tls: [0x005ac71c88f0,0x005ac71c8feb) rb:(102300/102300/102300) records(1286855/o:0) tid: 49272
   Previously allocated frames:
     record_addr:0x5b4c9ec4b0 record:0xb2cf005b70af7d7c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb7d7c) (BuildId: a12eb0b9ce683ad6964819d87f4b992d31c33409)
     record_addr:0x5b4c9ec4a8 record:0xbd2c005b70af6d88  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6d88) (BuildId: a12eb0b9ce683ad6964819d87f4b992d31c33409)
     record_addr:0x5b4c9ec4a0 record:0xbaf3005b70af6c0c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xb6c0c) (BuildId: a12eb0b9ce683ad6964819d87f4b992d31c33409)
   Searched 107650 records, find 0 with same addr 0x007e093b2cd3
   ```
2. 分析报错栈，定位到具体业务代码行。

   证据2：通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#1的符号解析，定位到具体业务代码行。

   ```screen
   ==appspawn==49272==ERROR: HWAddressSanitizer: tag-mismatch on address 0x007e093b2cd3 at pc 0x005ac88a7178
   WRITE of size 5 at 0x007e093b2cd3 tags: 96/06(96) (ptr/mem) in thread 49272
   Invalid access starting at offset 3
       #0 0x5ac88a7178  (/system/lib64/libclang_rt.hwasan.so+0x27178) (BuildId: 29cd839fde93692a63b6bd1b64b35830f6de6e33)
       #1 InjectMemcpyParamOverlap(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:244)
       #2 0x5b53db010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
   ```

   通过解析后的#1帧信息可以直观地看出，触发本次内存异常的具体位置为napi\_init.cpp文件的第244行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/mSZ5quq2QeSaihpxelzslw/zh-cn_image_0000002723405001.png)
3. 结合业务代码，进一步判断越界产生的原因。

   程序定义了包含5个有效字母的字符串，合法索引范围是buffer到buffer+5，memcpy()试图写入buffer+6，是栈内存上越界访问。

**问题结论与总结**

该问题属于典型的字符串操作不当问题，没有注意字符串右边界。

**修复建议**

校验字符串操作，使用安全的字符串函数。

## ASan栈内存越界访问

### 根因描述

栈内存越界，是指程序向栈区申请了特定的内存空间后，在读写数据时超出了该空间设定的边界，导致访问了不属于它的内存区域，从而引发程序数据损坏或逻辑异常，包含上越界和下越界。当应用[开启ASan](../harmonyos-guides/ide-asan.md#section111599216114)检测能力后，运行时会对指针和内存标签进行校验。一旦访问越过保护页，应用就会触发stack-buffer-overflow/stack-buffer-underflow异常进而退出。

### 问题分析思路

此类问题，通常情况下，有几种可能：

1. 栈上局部变量内存大小与实际使用大小不匹配，如字符串操作不当。
2. 数组下标越界，如偏移量、循环边界计算错误。

问题分析步骤如下：

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。
2. 分析报错栈，llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体业务代码行。
3. 结合业务代码，进一步判断越界产生的原因。

### 关键字

此类问题日志关键词为：stack-buffer-overflow/stack-buffer-underflow。确认是栈内存越界类型的故障后，优先分析业务侧调用栈帧代码。

### 案例分析

**案例一**：负下标访问导致栈内存下越界

**问题现象**

应用运行过程中触发ASan检测，应用闪退并生成ASan故障日志，故障日志显示为stack-buffer-underflow写越界。

**问题分析**

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。

   证据1：日志中给出stack-buffer-underflow，说明是一个栈内存下越界错误。同时WRITE of size 1 at 0x007e0eb55bdf表示程序向地址0x007e0eb55bdf写入1字节时触发异常。

   ```screen
   Reason:stack-buffer-underflow
   ==appspawn==62569==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==62569==ERROR: AddressSanitizer: stack-buffer-underflow on address 0x007e0eb55bdf at pc 0x007b3ed9074c bp 0x007e0eb55bb0 sp 0x007e0eb55ba8
   WRITE of size 1 at 0x007e0eb55bdf thread T0 (e.myapplication)
       #0 0x7b3ed90748  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xd0748) (BuildId: 6deec5f7da2a968662207c8b5aa0dfbc4e55b0fa)
       #1 0x7a2b03010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
       #2 0x7e111361e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
       #3 0x7e10728dac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)

   Address 0x007e0eb55bdf is located in stack of thread T0 (e.myapplication) at offset 31 in frame
       #0 0x7b3ed905ec  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xd05ec) (BuildId: 6deec5f7da2a968662207c8b5aa0dfbc4e55b0fa)
   ```
2. 分析报错栈，定位到具体业务代码行。

   证据2：通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#0的符号解析，定位到具体业务代码行。

   ```screen
   Reason:stack-buffer-underflow
   ==appspawn==62569==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==62569==ERROR: AddressSanitizer: stack-buffer-underflow on address 0x007e0eb55bdf at pc 0x007b3ed9074c bp 0x007e0eb55bb0 sp 0x007e0eb55ba8
   WRITE of size 1 at 0x007e0eb55bdf thread T0 (e.myapplication)
       #0 InjectStackBufferUnderflow(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:306)
       #1 0x7a2b03010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)
       #2 0x7e111361e8  (/system/lib64/module/arkcompiler/stub.an+0xe8b1e8)
       #3 0x7e10728dac  (/system/lib64/module/arkcompiler/stub.an+0x47ddac)

   Address 0x007e0eb55bdf is located in stack of thread T0 (e.myapplication) at offset 31 in frame
       #0 InjectStackBufferUnderflow(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:303)
   ```

   通过解析后的#0帧信息可以直观地看出，触发本次内存异常的具体位置为napi\_init.cpp文件的第306行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/4rRdYH6ZTbmRQxYgS15N4A/zh-cn_image_0000002693605646.png)
3. 结合业务代码，进一步判断越界产生的原因。

   程序定义了包含42个char元素的数组，合法索引范围是buffer[0]到buffer[41]，buffer[subscript]试图访问第-1个元素，是栈内存下越界访问。

**问题结论与总结**

该问题属于典型的数组下标越界问题，使用了buffer[subscript]试图访问第-1个元素，没有注意数组左边界。

**修复建议**

校验数组下标和buffer边界，禁止使用超过边界的下标访问数组。

**案例二**：内存拷贝超出缓冲区边界导致栈内存上越界

**问题现象**

应用运行过程中触发ASan检测，应用闪退并生成ASan故障日志，故障日志显示为stack-buffer-overflow写越界。

**问题分析**

1. 查看日志内容，确认故障类型。分析越界边界信息，确认越界位置。

   证据1：日志中给出stack-buffer-overflow，说明是一个栈内存上越界错误。同时WRITE of size 10 at 0x007e5ab98c06表示程序向地址0x007e5ab98c06写入10字节时触发异常。

   ```screen
   Reason:stack-buffer-overflow
   ==appspawn==4511==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==4511==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x007e5ab98c06 at pc 0x005a0861ec58 bp 0x007e5ab98ba0 sp 0x007e5ab97b78
   WRITE of size 10 at 0x007e5ab98c06 thread T0 (e.myapplication)
       #0 0x5a0861ec54  (/system/lib64/libclang_rt.asan.so+0xdec54) (BuildId: f56f0195024955df4ca655d4a88c5c0cb1a29e1a)
       #1 0x7baf9cfca4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xcfca4) (BuildId: 6deec5f7da2a968662207c8b5aa0dfbc4e55b0fa)
       #2 0x7a9547010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Address 0x007e5ab98c06 is located in stack of thread T0 (e.myapplication) at offset 38 in frame
       #0 0x7baf9cfb78  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xcfb78) (BuildId: 6deec5f7da2a968662207c8b5aa0dfbc4e55b0fa)
   ```
2. 分析报错栈，定位到具体业务代码行。

   证据2：通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）、DevEco Studio自带的堆栈跟踪分析等类似工具，完成调用栈#1的符号解析，定位到具体业务代码行。

   ```screen
   Reason:stack-buffer-overflow
   ==appspawn==4511==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process)
   =================================================================
   ==appspawn==4511==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x007e5ab98c06 at pc 0x005a0861ec58 bp 0x007e5ab98ba0 sp 0x007e5ab97b78
   WRITE of size 10 at 0x007e5ab98c06 thread T0 (e.myapplication)
       #0 0x5a0861ec54  (/system/lib64/libclang_rt.asan.so+0xdec54) (BuildId: f56f0195024955df4ca655d4a88c5c0cb1a29e1a)
       #1 InjectMemcpyParamOverlap(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:244)
       #2 0x7a9547010c  (/system/lib64/platformsdk/libace_napi.z.so+0x7010c) (BuildId: 226dc0ffc65e2899a5e810b4acb58e65)

   Address 0x007e5ab98c06 is located in stack of thread T0 (e.myapplication) at offset 38 in frame
       #0 InjectMemcpyParamOverlap(napi_env__*, napi_callback_info__*) at (C:/Users/Desktop/C/entry/src/main/cpp/napi_init.cpp:242)
   ```

   通过解析后的#1帧信息可以直观地看出，触发本次内存异常的具体位置为napi\_init.cpp文件的第244行，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bHLquiJ4RAi0p99lPP5LaQ/zh-cn_image_0000002723285077.png)
3. 结合业务代码，进一步判断越界产生的原因。

   程序定义了包含5个有效字母的字符串，合法索引范围是buffer到buffer+5，memcpy()试图写入buffer+6，是栈内存上越界访问。

**问题结论与总结**

该问题属于典型的字符串操作不当问题，没有注意字符串右边界。

**修复建议**

校验字符串操作，使用安全的字符串函数。
