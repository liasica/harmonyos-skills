---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-stack-fault-mode
title: 栈内存过大导致内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > RSS内存泄漏故障模式说明 > 栈内存过大导致内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:93b55c3c69c263f3817a32aedc6874f7b8eb0845621777a4bf528e53da953dd2
---

## 概述

应用的栈内存过大属于RSS内存泄漏的二级根因之一。本文旨在为开发者介绍栈内存过大的可能根因，并结合案例介绍开发态与运维态的问题分析思路。

## 根因描述

栈内存作为程序运行时的基础内存区域，通常用于存储局部变量、函数调用链、返回地址等信息。在传统认知中，栈内存由系统自动管理，函数返回时自动释放，业界通常认为栈内存不会发生泄漏。然而，在HarmonyOS系统的实际开发与运维过程中，栈内存过大也会导致严重的内存泄漏问题。

栈内存过大导致内存泄漏，根源在于线程生命周期管理失衡，具体表现为两类典型问题：

* 线程数过多：每个线程都拥有独立栈空间（主线程上限8MB，子线程上限1MB），线程数量激增时栈内存会快速累积。例如1500个线程仅栈内存最高就可达1.5GB，叠加堆内存和映射内存后极易触发系统管控，同时引发调度开销、锁竞争和缓存命中率下降等连锁问题。
* 线程未释放（僵尸线程）：线程因死锁、不可中断I/O或无限循环无法退出，线程对应的栈内存及其持有的锁、句柄、连接等资源无法回收。如某进程创建800个子线程，任务执行完毕却未释放，栈内存占用最高达800MB。此类泄漏一般具有隐蔽性和渐进性，长期运行后方才显现，治理难度较大。

## 问题分析思路

### 运维态问题分析思路

开发者可以根据[基础日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section112542151112)对日志中的轻量化Smaps维测日志进行分析，如果Category类型中“stack”的内存最大，那么可以将当前遇到的RSS内存泄漏问题精确到栈内存泄漏问题。如果要进一步分析泄漏点，开发者可以参考[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)获取内存栈日志后，将日志导入DevEco Studio，按照[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)对调用栈进行分析并找到泄漏点。

**说明** 

应用内存泄漏的速度对应用内存栈的有效性影响较大，过快或过慢都可能导致内存调用栈无法命中泄漏点。对于快速泄漏问题，推荐开发者参考[订阅资源泄漏事件（ArkTS）](../harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts.md)方法，在订阅资源泄漏事件的同时，通过configEventPolicy()方法补充订阅应用页面切换信息，以此分析泄漏场景，并在开发态对泄漏问题进行复现和定位。

### 开发态问题分析思路

如果应用发生了RSS内存泄漏，可以参考[开发态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section1663214591559)，结合场景复现并使用DevEco Studio中Profiler工具的Allocation功能定位栈内存泄漏问题。

## 案例分析

为直观展示栈内存过大导致内存泄漏的问题定位方法，下文结合线程申请过多导致内存泄漏的负向案例介绍了开发态与运维态下的问题分析过程。

### 案例：线程申请过多导致内存泄漏

此负向案例为应用大量申请线程未释放导致栈内存过大，系统检测到应用发生RSS内存泄漏后在前台管控此应用，最终造成应用闪退故障。

**运维态分析思路**

如果开发者在运维态遇到此问题，可以按照如下步骤进行分析：

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，在沙箱中接收到故障日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 在故障日志中找到关键字LOGGER\_MEMCHECK\_SAMPLIFY\_SMAPS\_INFO，并读取数据如下：

   ```screen
   LOGGER_MEMCHECK_SAMPLIFY_SMAPS_INFO
          Size         Rss        Swap                Category      Counts    Name
           512           0          52       arkts-static heap           2    [anon:ArkTs Static Object Space]
          1028          12           0                    stack          1    [anon:stack:55575]
          1028          12           0                    stack          1    [anon:stack:55576]
          1028          12           0                    stack          1    [anon:stack:55577]
          1028          12           0                    stack          1    [anon:stack:55578]
   ......
   ```
3. 分析Smaps维测日志，并按照Category列进行聚类，对每种类型的Rss列、Swap列求和，得到每种内存类型的申请总量，经过排序发现stack类型的内存总量最大，因此可初步定界当前RSS内存泄漏故障为栈内存泄漏问题。
4. 通过[内存栈日志获取方法](bpta-stability-rssleak-fault-mode-overreview.md#section18531162841113)拿到Profiler日志后，使用DevEco Studio中Profiler工具导入内存栈日志，而后按照[内存栈日志分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section94641340515)进一步分析泄漏点：
   1. 打开DevEco Studio中的Profiler组件，单击下图1处导入获取的内存栈日志。
   2. 单击选择System Resources下的Threads泳道，如下图2处。
   3. 单击下图3处Call Trees查看内存申请调用栈。
   4. 单击下图4处选择Created & Existing，筛选申请并且未释放的内存及其调用栈。
   5. 筛选出线程个数申请异常的线程及其调用栈，如下图5处框选的内容：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/0f4Vjo7gR42qyfRWQZUKTQ/zh-cn_image_0000002729611091.png "点击放大")
5. 分析调用栈指向的代码段，发现应用循环申请线程，且该线程一直运行未释放，最终导致了RSS内存泄漏：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/j36IpJlvRJuOF9rPvSDMjg/zh-cn_image_0000002699891764.png)

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现RSS内存泄漏的场景，可以按照以下步骤排查是否为线程栈泄漏问题并定位：

1. 参考[开发态问题分析方法](bpta-stability-rssleak-fault-mode-overreview.md#section1663214591559)，使用hidumper --mem-smaps pid命令获取指定进程的详细内存使用情况，如果输出的结果中存在大量Category列为stack类型的内存，可以判断应用发生了线程泄漏问题。

   ```screen
   # hidumper --mem-smaps 43709

   -------------------------------[memory]-------------------------------

                                       Shared      Shared      Private     Private
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts      Category                         Name
   ......
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43766]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43767]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43768]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43770]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43802]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43817]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:43878]
   28          0           0           0           0           0           0           0           0           1           stack                            [anon:signal_stack:654]
   ......
   1028        12          12          0           0           12          0           0           0           1           stack                            [anon:stack:43766]
   1028        12          12          0           0           12          0           0           0           1           stack                            [anon:stack:43767]
   1028        16          16          0           0           16          0           0           0           1           stack                            [anon:stack:43768]
   8196        24          24          0           0           24          0           0           0           1           stack                            [anon:stack:43816]
   1028        28          28          0           0           28          0           0           0           1           stack                            [anon:stack:43817]
   1028        8           8           0           0           8           0           0           0           1           stack                            [anon:stack:43878]
   ......
   ```
2. 尝试复现此场景并使用DevEco Studio中Profiler工具的Allocation功能抓取内存异常增长点。
3. 录制完成后，单击System Resources下的Threads泳道，发现线程数异常增长。
4. 先单击下图1处Call Trees按钮，再单击下图2处筛选Created & Existing，找到异常的线程申请调用栈如下图3处框中所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/iWENcmBoQbWCKXcn_UVHSA/zh-cn_image_0000002699731878.png "点击放大")
5. 分析调用栈指向的代码段，发现应用正在循环申请线程，且该线程一直运行未释放，最终导致了RSS内存泄漏：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ZdA5p7EPR0KJUGs9iKKhRg/zh-cn_image_0000002729491133.png)

## 修复建议

1. **线程生命周期管理规范化**
   * 所有通过new Thread()创建的线程，必须在启动后明确调用join()等待结束，或调用detach()设置为分离状态，确保线程退出时系统自动回收资源。
   * 使用线程池统一管理，避免遗漏资源回收逻辑。
2. **循环退出条件的完整性**
   * 所有while(true)、for(;;)等无限循环必须包含明确的退出路径，如基于计数器阈值、时间戳截止或外部取消标志。
   * 循环体内部必须检查线程中断状态，并且能响应外部中断请求。
3. **锁获取的超时与公平性**
   * 避免嵌套锁，必须嵌套时确保所有线程以相同顺序获取锁，消除死锁产生的必要条件。
