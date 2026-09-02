---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-7
title: 使用应用过程中卡死，无法响应用户任何操作
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 使用应用过程中卡死，无法响应用户任何操作
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8b9ebfcfa6d07f1989fad1d9f9bdbcee31a8430ec4268bb9243fdd86207bc9c8
---

## 问题现象

应用在使用过程中卡死无响应。

## 背景知识

* 内存泄漏相关日志文件[JS内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#js内存泄漏日志规格)、[native内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#native内存泄漏日志规格)和[ashmem/ion/gpu/gpu\_rs内存泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#ashmemdmagpugpu_rs内存泄漏日志规格)。
* ION（Interprocess Communication Over Non-Contiguous Memory）内存是负责内存管理的一个关键子系统，ION内存管理器的主要目的是提供一个统一的接口，用于在硬件设备和用户空间之间分配和共享内存。
* ashmem是图片共享内存，图片共享内存通常有以下几种命名方式：

  ```screen
  /dev/ashmem/PixelMap RawData, uniqueId: xxxx_xx
  /dev/ashmem/JPEG RawData, uniqueId: 1845_2 (deleted)
  /dev/ashmem/EXT RawData
  ```

## 问题定位

### 场景一

1. 从设备的data->log->memory\_leak目录下查看文件名为memleak-kernel-[module]-0-sample.txt的采样文件，从采样文件中可以看到内存类型，内存门限和应用ION内存峰值。从下面的表中可以查看应用ION内存随时间上涨情况。

   ```screen
   memoryName:ion
   softThreshold:3000(MB)
   hardThreshold:4500(MB)
   topMemory:7015044(KB)

   time(s) kernelMemory(KB)realtime
   0               209             105868          2024/12/04 22:03:21
   1               429             113868          2024/12/04 22:07:01
   2               649             436416          2024/12/04 22:10:41
   3               869             448168          2024/12/04 22:14:21
   4               1089            448168          2024/12/04 22:18:01
   5               1309            448168          2024/12/04 22:21:41
   6               1529            457352          2024/12/04 22:25:21
   7               1749            457352          2024/12/04 22:29:01
   8               1969            677156          2024/12/04 22:32:41
   9               2189            461448          2024/12/04 22:36:21
   10              2409            452264          2024/12/04 22:40:01
   11              2629            452264          2024/12/04 22:43:41
   12              2849            850260          2024/12/04 22:47:21
   13              3069            914380          2024/12/04 22:51:01
   14              3289            957984          2024/12/04 22:54:41
   15              3509            478868          2024/12/04 22:59:22
   16              3729            608372          2024/12/04 23:03:02
   17              3949            7015044         2024/12/04 23:15:17
   ```
2. 打开内存映射文件memleak-kernel-[module]-0-[timestamp].txt，并筛选出包含"Total dmabuf size of"的行，可以看到应用进程占用的ION内存的情况。

   ```screen
   Total dmabuf size of hiaiserver: 12582912 bytes
   Total dmabuf size of CameraDaemon: 4194304 bytes
   Total dmabuf size of composer_host: 68116480 bytes
   Total dmabuf size of render_service: 5513801728 bytes
   ```
3. 目前因为采用了统一渲染机制，大部分ION内存都是在render\_service进程分配使用的，如果发现应用使用ION超标了，那么按照历史经验，高概率怀疑是PixelMap C++对象泄漏。需要排查是否存在PixelMap C++对象泄漏，参考文档[ION泄漏](../best-practices/bpta-stability-leak-way.md#section5493141412410)。

### 场景二

1. 从memory\_leak目录下查看文件名为memleak-native-[process\_name]-[pid]-smaps.txt的内存映射文件，搜索关键字LOGGER\_MEMCHECK\_SMAPS\_INFO，查看该进程的smaps汇总信息。

   ```screen
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime:	2025/04/09 10:58:12

   -------------------------------[memory]-------------------------------

   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
   // ...
   160880      18360       13580       9560        0           8800        0           7364        7364        5                             /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so
   34844       2984        2936        48          0           2936        0           968         689         21                            [anon:native_heap:jemalloc meta]                                         
   2663248     2655276     2654156     0           2240        0           2653036     0           0           1765                          anon_inode:dev/ashmem/EXTRawData          
   128         8           4           0           8           0           0           0           0           2                             anon_inode:dev/ashmem/shared_memory/149B66719F7D3586B4F043474A5845FC
   // ...
   46069784    2969996     2942807     126900      2860        186740      2653496     113136      81977       6437                          Summary
   ```
2. 从内存映射文件中可以看到，anon\_inode:dev/ashmem/EXTRawData(图片共享内存)占用的Pss内存最大，应用出现ashmem内存泄漏，根据EXTRawData关键字基本可以断定是PixelMap对象泄漏，排查方法参考[ashmem泄漏](../best-practices/bpta-stability-leak-way.md#section2825227501)。

## 分析结论

### 场景一

应用进程存在ION内存泄漏。

### 场景二

应用存在ashmem图片共享内存资源泄漏。

## 修改建议

### 场景一

使用完成后及时释放PixelMap C++对象，可参考API文档[release](../harmonyos-references/arkts-apis-image-pixelmap.md#release7)和[OH\_PixelmapNative\_Destroy()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)，推荐在页面切换、应用退后台等场景下手动释放老页面PixelMap。

### 场景二

减少加载图片资源的数量，使用完成后及时释放PixelMap C++对象，可参考API文档[release](../harmonyos-references/arkts-apis-image-pixelmap.md#release7)和[OH\_PixelmapNative\_Destroy()](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)。
