---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-threadleak-fault-mode
title: 应用线程泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 线程泄漏故障模式说明 > 应用线程泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:73999035b751255429da8a635cab2a4326b779222107450a95fa45fd8a083f71
---

## 概述

应用运行期间，若存在线程生命周期管理不规范或线程池参数配置不合理等问题，极易造成线程数量持续上涨。一旦线程总量突破系统阈值，系统将判定发生线程泄漏并启动分级限流管控策略，严重时系统会终止应用进程。

本文旨在为开发者介绍线程泄漏的几种常见根因，并基于案例介绍开发态与运维态的问题分析思路。

## 根因描述

应用创建的线程未能正常退出、线程阻塞无法完成回收或是短时间批量创建线程，均会造成线程数量持续累积，进而引发线程泄漏。

线程泄漏的常见原因，有以下几类：

1. 缺少线程退出机制导致的泄漏：pthread\_create()创建的线程未设定退出机制，线程一直存活。
2. 死锁/IO阻塞导致的泄漏：资源死锁或IO阻塞导致线程无法正常执行退出流程，线程资源得不到释放回收。
3. 线程爆炸导致的泄漏：短时间内密集任务导致创建大量线程，子线程数量超限，形成线程泄漏。

## 问题分析思路

### 运维态问题分析思路

开发者可以通过[运维态问题分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section6755104234513)对获取到的线程泄漏维测日志进行分析，定位线程泄漏原因。

### 开发态问题分析思路

开发者如果在应用调试过程中发生了线程泄漏问题，可以根据[开发态问题分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section4840142124519)定位线程泄漏原因。

## 案例分析

为直观展示线程泄漏的根因定位方法，下文结合无退出机制导致线程泄漏、死锁导致线程泄漏两个负向案例介绍了开发态与运维态下的问题分析过程。

### 案例一：无退出机制导致线程泄漏

此负向案例通过调用pthread\_create()批量创建线程，但未执行pthread\_join()完成线程回收，构造线程泄漏场景。系统检测到应用发生线程泄漏后在后台管控此应用，重新打开应用时，用户感知应用冷启。

**运维态分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到维测日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 在维测日志中可查询Top 10 Thread Name信息，如下所示：应用创建了2002个名称为example.dfx\_test的线程，据此判定存在线程泄漏。

   ```text
   Top 10 Thread Name:
   2002    example.dfx_test
   11      V8 DefaultWorke
   5       OS_GC_Thread
   1       OS_FFRT_3_2
   1       OS_FFRT_3_5
   1       OS_FFRT_Delay
   1       OS_EVENT_POLL
   1       OS_IPC_0_3003
   1       OS_IPC_1_3004
   1       OS_AppEvent_Ls
   ```
3. 以线程名“example.dfx\_test”为关键词在维测日志中查询到对应的线程快照信息如下：

   ```text
   ……
   Tid:16238, Name:example.dfx_test
   state=S, utime=1, stime=0, priority=10, nice=-10, clk=100
   #00 pc 00000000001f12e8 /system/lib/ld-musl-aarch64.so.1(sleep+64)(24a92346fd47c2687706c034d692ae3f)
   #01 pc 0000000000207b68 /data/storage/el1/bundle/libs/arm64/libentry.so(LogLeakExplosionTask(void*)+72)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #02 pc 00000000001e3ba8 /system/lib/ld-musl-aarch64.so.1(start+240)(24a92346fd47c2687706c034d692ae3f)
   Tid:16668, Name:example.dfx_test
   state=S, utime=1, stime=0, priority=10, nice=-10, clk=100
   #00 pc 00000000001f12e8 /system/lib/ld-musl-aarch64.so.1(sleep+64)(24a92346fd47c2687706c034d692ae3f)
   #01 pc 0000000000207b68 /data/storage/el1/bundle/libs/arm64/libentry.so(LogLeakExplosionTask(void*)+72)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #02 pc 00000000001e3ba8 /system/lib/ld-musl-aarch64.so.1(start+240)(24a92346fd47c2687706c034d692ae3f)
   ……
   ```

   通过分析该组线程快照能够发现：发生泄漏的批量线程均处于睡眠状态（state=S）无法正常退出回收，进而造成线程数量持续堆积。开发者可结合业务逻辑，按照线程创建链路定位具体泄漏点。
4. 参考[线程泄漏调用栈日志获取方法](bpta-stability-threadleak-fault-mode-overreview.md#section2975173711173)获取线程申请调用栈后，可以通过[线程泄漏调用栈日志分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section19835127163117)进行下一步分析：
   * 单击下图1处按钮，导入线程泄漏调用栈日志。
   * 单击下图2处选择Threads泳道。
   * 单击下图3处Call Trees查看线程申请调用栈。
   * 单击下图4处选择Created & Existing，筛选申请并且未释放的线程及其调用栈。
   * 如下图5、6处框选的内容所示，可识别出线程数量申请异常的线程及其调用栈。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/YOUB25b8Q2C7mSXr8kSGlA/zh-cn_image_0000002729477841.png "点击放大")
5. 结合调用栈可定位至对应业务逻辑，研读业务代码后确认：每次单击“Thread-No-Exit-Leak”按钮，ArkTS层响应单击事件，进而调用Native接口LeakThreadNoExit()批量创建线程；重复单击该按钮后，线程持续堆积，最终引发线程泄漏。
   * ArkTS层函数如下图所示：响应按钮单击动作，调用Native层的LeakThreadNoExit()函数。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/NANkLYvmQ1mjfszcEhsnQg/zh-cn_image_0000002729597805.png)
   * Native层LeakThreadNoExit()函数如下图所示：通过分析，该函数接收ArkTS层传入的指定数量参数，每次执行均通过pthread\_create()创建线程，但线程生命周期结束前未调用pthread\_join()完成线程资源回收，存在资源泄漏隐患。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/m2iikTYLT_OlrCotCfi-lA/zh-cn_image_0000002699878480.png)
   * 线程执行函数ThreadLeakNoExit()如下图所示：函数内部为无限while(1)循环，持续睡眠，不存在任何跳出循环的逻辑，线程启动后会永久运行，无法自行退出销毁。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/VXuisPDXSPiZUdX24f3lhQ/zh-cn_image_0000002699718590.png)
   * 线程依靠死循环常驻进程无法退出，叠加LeakThreadNoExit()缺少线程回收逻辑，反复调用该接口会持续新增常驻线程，线程数量不断上涨，最终引发线程泄漏。

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现线程泄漏的场景。开发者可尝试复现此场景，并通过DevEco Studio中Profiler工具的Allocation功能抓取线程异常增长的泄漏点，对抓取结果进行分析，详细使用可参考[故障分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section496433010306)。

1. 录制完成获得结果后，单击System Resources中的Threads泳道。观测到线程数量达到1014个，存在异常增长现象，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/fFwXJ9SnQgWfGrjl4l0w5A/zh-cn_image_0000002729477843.png "点击放大")
2. 单击下图1处Call Trees按钮，单击下图2处再筛选Created & Existing，可以识别出线程数量申请异常的线程及其调用栈，申请调用栈如下图3处框中所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/VXf3EhEtT32TNLKCxXCfSA/zh-cn_image_0000002729597807.png "点击放大")
3. 结合调用栈定位对应业务逻辑，研读业务代码后确认：每次单击“Thread-No-Exit-Leak”按钮，ArkTS层响应单击事件，进而调用Native接口LeakThreadNoExit()批量创建线程；重复单击该按钮后，线程持续堆积，最终引发线程泄漏。
   * ArkTS层函数如下图所示：响应按钮单击动作，调用Native层的LeakThreadNoExit()函数。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/z70HhXyrQtmUAUDyF8IXFg/zh-cn_image_0000002699878482.png)
   * Native层LeakThreadNoExit()函数如下图所示：通过分析，该函数接收ArkTS层传入的指定数量参数，每次执行均通过pthread\_create()创建线程，但线程生命周期结束前未调用pthread\_join()完成线程资源回收，存在资源泄漏隐患。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/bPl33lvLQb2bh02Nbqd-nQ/zh-cn_image_0000002699718592.png)
   * 线程执行函数ThreadLeakNoExit()如下图所示：函数内部为无限while(1)循环，持续睡眠，不存在任何跳出循环的逻辑，线程启动后会永久运行，无法自行退出销毁。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/c5I3T70cRfy0yvH7pyELrA/zh-cn_image_0000002729477847.png)
   * 线程依靠死循环常驻进程无法退出，叠加LeakThreadNoExit()缺少线程回收逻辑，反复调用该接口会持续新增常驻线程，线程数量不断上涨，最终引发线程泄漏。

**修复建议**

1. 线程创建后设置分离属性或调用pthread\_join()接口，避免线程泄漏。
2. 创建线程需显式设置线程名称，方便后续问题排查定位。
3. 线程创建成功后，正常及异常退出路径均要做线程资源回收，防止异常分支遗漏回收造成线程泄漏。

### 案例二：死锁导致线程泄漏

此负向案例通过构造典型的AB-BA死锁场景，线程永久阻塞无法退出，进而产生死锁型线程泄漏。系统检测到应用发生线程泄漏后在后台管控此应用，重新打开应用时，用户感知应用冷启。

**运维态分析思路**

1. 通过订阅[资源泄漏事件](../harmonyos-guides/resource-leak-events.md)，开发者可以在沙箱中接收到维测日志/data/storage/el2/log/resourcelimit/RESOURCE\_OVERLIMIT\_XXXX\_XXXX.log。
2. 在维测日志中查询到Top 10 Thread Name信息，如下所示：应用创建了1012个名称为example.dfx\_test的线程，据此判定存在线程泄漏。

   ```text
   Top 10 Thread Name:
   1012	example.dfx_test
   11	V8 DefaultWorke
   5	OS_GC_Thread
   1	OS_FFRT_3_0
   1	OS_FFRT_3_1
   1	OS_FFRT_3_2
   1	OS_FFRT_3_3
   1	OS_FFRT_4_0
   1	OS_FFRT_5_2
   1	OS_FFRT_5_3
   ```
3. 以线程名“example.dfx\_test”为关键词在维测日志中查询到对应的线程快照信息如下：

   ```text
   ……
   Tid:61219, Name:example.dfx_test
   state=S, utime=1, stime=0, priority=10, nice=-10, clk=100
   #00 pc 00000000001df2bc /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+156)(24a92346fd47c2687706c034d692ae3f)
   #01 pc 00000000001e53e8 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+536)(24a92346fd47c2687706c034d692ae3f)
   #02 pc 00000000000c631c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::mutex::lock()+8)(f80bf3c981494745bc22d1fb7c905b715120a802)
   #03 pc 00000000002079bc /data/storage/el1/bundle/libs/arm64/libentry.so(std::__n1::lock_guard<std::__n1::mutex>::lock_guard[abi:v15004](std::__n1::mutex&)+36)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #04 pc 0000000000207a20 /data/storage/el1/bundle/libs/arm64/libentry.so(ThreadDeadlockB(void*)+44)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #05 pc 00000000001e3ba8 /system/lib/ld-musl-aarch64.so.1(start+240)(24a92346fd47c2687706c034d692ae3f)
   Tid:61220, Name:example.dfx_test
   state=S, utime=1, stime=0, priority=10, nice=-10, clk=100
   #00 pc 00000000001df2bc /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+156)(24a92346fd47c2687706c034d692ae3f)
   #01 pc 00000000001e53e8 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+536)(24a92346fd47c2687706c034d692ae3f)
   #02 pc 00000000000c631c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::mutex::lock()+8)(f80bf3c981494745bc22d1fb7c905b715120a802)
   #03 pc 00000000002079bc /data/storage/el1/bundle/libs/arm64/libentry.so(std::__n1::lock_guard<std::__n1::mutex>::lock_guard[abi:v15004](std::__n1::mutex&)+36)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #04 pc 00000000002078ec /data/storage/el1/bundle/libs/arm64/libentry.so(ThreadDeadlockA(void*)+44)(c7b58260ef12cb6981b2d34fb0063bae65cf3e9a)
   #05 pc 00000000001e3ba8 /system/lib/ld-musl-aarch64.so.1(start+240)(24a92346fd47c2687706c034d692ae3f)
   ……
   ```

   分析线程快照发现大量线程状态为休眠阻塞（state=S），栈均卡在\_\_pthread\_mutex\_timedlock\_inner互斥锁等待逻辑。Tid 61219线程与Tid 61220线程分别执行了libentry.so的ThreadDeadlockA()、ThreadDeadlockB()业务函数，两个线程互相在等待对方持有的锁导致出现死锁现象，线程无法正常退出，大量同类线程堆积。开发者可根据业务场景排查源码中锁的使用是否正常，定位锁冲突问题。
4. 参考[线程泄漏调用栈日志获取方法](bpta-stability-threadleak-fault-mode-overreview.md#section2975173711173)获取线程申请调用栈后，可以按照[线程泄漏调用栈日志分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section19835127163117)进行下一步分析：
   * 单击下图1处按钮，导入线程泄漏调用栈日志。
   * 单击下图2处选择Threads泳道。
   * 单击下图3处Call Trees查看线程申请调用栈。
   * 单击下图4处选择Created & Existing，筛选申请并且未释放的线程及其调用栈。
   * 如下图5、6处框选的内容所示，可以识别出线程数量申请异常的线程及其调用栈。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/tJH0vfx7QEqu2B0XliT_PQ/zh-cn_image_0000002729597809.png "点击放大")
5. 结合调用栈可定位至对应业务逻辑，研读业务代码后确认：每次单击“Blocked-Thread-Leak”按钮，ArkTS层响应单击事件，进而调用Native接口LeakThreadBlocked()批量创建线程；重复单击该按钮后，线程持续堆积，最终引发线程泄漏。
   * ArkTS层函数如下图所示：响应按钮单击动作，调用Native层的LeakThreadBlocked()函数。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/1eLcGjn1QqaLYGqBFSdX0Q/zh-cn_image_0000002699878484.png)
   * Native层LeakThreadBlocked()函数如下图所示：该方法每次执行都会通过pthread\_create()批量创建ThreadDeadlockA、ThreadDeadlockB线程并记录线程ID，但全程没有调用pthread\_join()回收线程资源。

     **说明** 

     由pthread\_create()创建的线程默认为joinable属性，若不主动join，即便线程正常结束，系统也不会释放线程资源，存在泄漏风险。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8M_-vnjNSumYyE2KH91R3w/zh-cn_image_0000002699718594.png)
   * 分析业务线程执行函数ThreadDeadlockA()与ThreadDeadlockB()如下图所示：两个线程采用相反顺序获取g\_mutex\_a、g\_mutex\_b，形成AB-BA锁序冲突进而触发死锁，线程互相等待锁资源，永久阻塞无法退出。同时线程阻塞后栈上lock\_guard对象无法析构释放互斥锁，锁资源也会持续占用。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/U4uY44baRQ690JlZ7x6tWA/zh-cn_image_0000002729477849.png)
   * 死锁造成线程常驻进程无法销毁，叠加LeakThreadBlocked()缺少线程回收逻辑，多次单击按钮调用该接口后，进程内线程数量不断堆积，最终引发线程泄漏。

**开发态分析思路**

对于开发态存在的问题，开发者大致能够推断出当前出现线程泄漏的场景。开发者可尝试复现此场景，并通过DevEco Studio中Profiler工具的Allocation功能抓取线程异常增长的泄漏点，对抓取结果进行分析，详细使用可参考[故障分析方法](bpta-stability-threadleak-fault-mode-overreview.md#section496433010306)。

1. 录制完成获得结果后，单击System Resources中的Threads泳道，观测到线程数量达到1993个，存在异常增长现象，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/JINSBIU5RDSz3oJoKa2hdQ/zh-cn_image_0000002729597811.png "点击放大")
2. 单击下图1处Call Trees按钮，单击下图2处再筛选Created & Existing，可以识别出线程数量申请异常的线程及其调用栈，申请调用栈如下图3处框中所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/2ncTrLTRRyilroDebHt5rQ/zh-cn_image_0000002699878486.png "点击放大")
3. 结合调用栈可定位至对应业务逻辑，研读业务代码后确认：每次单击“Blocked-Thread-Leak”按钮，ArkTS层响应单击事件，进而调用Native接口LeakThreadBlocked()批量创建线程；重复单击该按钮后，线程持续堆积，最终引发线程泄漏。
   * ArkTS层函数如下图所示：响应按钮单击动作，调用Native层的LeakThreadBlocked()函数。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/gfqRbRqETyWBc7QuH0GJww/zh-cn_image_0000002699718596.png)
   * Native层LeakThreadBlocked()函数如下图所示：该方法每次执行都会通过pthread\_create()批量创建ThreadDeadlockA、ThreadDeadlockB线程并记录线程ID，但全程没有调用pthread\_join()回收线程资源。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Ub569djQQDW8ik1WCURQEw/zh-cn_image_0000002729477851.png)
   * 继续分析业务线程执行函数ThreadDeadlockA()与ThreadDeadlockB()如下图所示：两个线程采用相反顺序获取g\_mutex\_a、g\_mutex\_b，形成AB-BA锁序冲突进而触发死锁，线程互相等待锁资源，永久阻塞无法退出。同时线程阻塞后栈上lock\_guard对象无法析构释放互斥锁，锁资源也会持续占用。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/BDdq6jr3Qg2ZE6h0cECSZQ/zh-cn_image_0000002729597813.png)
   * 死锁造成线程常驻进程无法销毁，叠加LeakThreadBlocked()缺少线程回收逻辑，多次单击按钮调用该接口后，进程内线程数量不断堆积，最终引发线程泄漏。

**修复建议**

1. 优化线程创建逻辑，采用分离线程或配套join回收机制，解决大批量线程永久资源泄漏。
2. 增加入参上限校验、自定义线程名、线程退出控制标记，提升接口稳定性与问题可排查性。
3. 调整两处线程锁的获取顺序，统一加锁次序，推荐使用scoped\_lock()一次性申请多锁，消除AB-BA死锁风险。
