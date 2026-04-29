---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-tsan-detection
title: 使用TSan检测线程问题
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 线程并发类问题检测 > 使用TSan检测线程问题
category: best-practices
scraped_at: 2026-04-29T14:14:02+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8a0260da643a8cd015473e6be31ee5467161bd1587de5b790746bafcec4dace3
---

## 原理概述

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。

TSan使能分为两个阶段：Instrumentation阶段（完成代码插桩）和Runtime阶段（负责竞争判断和报告输出）。

## 功能介绍

### 应用场景

TSan能够检测出如下问题：

* 数据竞争检测：数据竞争（Data Race）是指两个或多个线程在没有适当的同步机制情况下同时访问相同的内存位置，其中至少有一个线程在写入。数据竞争是导致多线程程序行为不可预测的主要原因之一。

* 锁错误检测：TSan不仅能检测数据竞争，还能检测与锁相关的错误：
  + 死锁（Deadlock）：死锁是指两个或多个线程互相等待对方释放锁，导致程序无法继续执行。
  + 双重解锁（Double Unlock）：同一线程尝试解锁已经解锁的锁。
  + 未持有锁解锁：一个线程尝试解锁一个它未持有的锁。

* 条件变量错误检测：条件变量用于线程之间的通信和同步，常见错误包括：
  + 未持有锁等待：一个线程在未持有相关锁的情况下调用wait。
  + 未持有锁唤醒：一个线程在未持有相关锁的情况下调用signal或broadcast。

常见TSan异常检测类型有data race，heap-use-after-free，signal handler spoils errno等，详见[TSan异常检测类型](bpta-stability-tsan-detection.md#section1180812915516)部分。

## 错误报告

当TSan检测到错误时，它会生成详细的报告，包括：

* 错误类型：例如数据竞争、死锁等。
* 内存地址：涉及的内存地址。
* 线程信息：涉及的线程ID和线程创建的堆栈跟踪。
* 源代码位置：每一个内存访问的源代码位置和堆栈跟踪。
* 上下文信息：访问类型（读/写）、访问大小等。

## 使用约束

* TSan仅支持API 12及以上版本。
* ASan、TSan、UBSan、HWASan、GWP-ASan不能同时开启，五个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如GPU图形渲染）可能会受影响。
* TSan不支持静态链接libc或libc++库。

## 使能TSan

可通过以下两种方式使能TSan。每种方式分为DevEco Studio场景和流水线场景。

### 方式一

**DevEco Studio场景**

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/PzrgVPGoR6G5iywiUD8nsQ/zh-cn_image_0000002370405548.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=6277D642347DCE2BCCD744E520AED3964A391B6162C91898151C11616635B264)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/AvbhKhfKTqCuhRQ0OjBEdA/zh-cn_image_0000002404045261.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=BDE52686B2F69BF8F4D7CA83111D469E89B7760EFFBCF45C8E85E2EDF7B56355)

**流水线场景**

在hvigorw命令后加上**ohos-debug-tsan=true**的选项，执行hvigorw命令，更多options参考[命令行构建工具（hvigorw）](../harmonyos-guides/ide-hvigor-commandline.md)。

```
1. hvigorw [taskNames...] ohos-debug-tsan=true  <options>
```

同上，如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSAN模式编译so文件。

### 方式二

**DevEco Studio场景**

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/VxmqiPQnRPSEzFeDzjudQA/zh-cn_image_0000002370565432.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=833CB29450EF77095BE7D2749D25455EDB3319AE59B3AAF5CCF2CEC77D8E48A8)
2. 设置模块级构建TSan插桩。

   在需要使能TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/s1yk25DORGm9MWfQRwkuiQ/zh-cn_image_0000002404125101.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=A46F3F8BE2F25BD3B2BF0D4524BEADB229FD74ED1E8CA6EE035505719F0C818F)

**流水线场景**

在hvigorw命令后加上**ohos-debug-tsan=true**的选项，执行hvigorw命令，更多options参考[命令行构建工具（hvigorw）](../harmonyos-guides/ide-hvigor-commandline.md)。

```
1. hvigorw [taskNames...] ohos-debug-tsan=true  <options>
```

同上，如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSAN模式编译so文件。

## TSan异常检测类型

### Data race

**背景**

多个线程在没有正确加锁的情况下，同时访问同一块数据，并且至少有一个线程是写操作，对数据的读取和修改产生了竞争，从而导致各种不可预计的问题

**错误代码实例**

```
1. int Global = 12;

4. void Set1() {
5. *(char *)&Global = 4;
6. }

9. void Set2() {
10. Global=43;
11. }

14. void *Thread1(void *x){
15. Set1();
16. return x;
17. }

20. static napi_value Add(napi_env env, napi_callback_info info){
21. ...
22. pthread_t t;
23. pthread_create(&t, NULL, Thread1, NULL);
24. Set2();
25. pthread_join(t, NULL);
26. ...
27. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L6-L32)

**影响**

对数据的读取和修改产生了竞争，从而导致各种不可预计的问题

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: data race

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/TADj1Im8RB6T7nt6lNxbIQ/zh-cn_image_0000002537311043.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=E4839E5D3E4CE75D9A2BE6F2D378CD11151625BDADFAABE120216D100D019181)

**修改方法**

加锁或者其它线程同步的方法

**推荐建议**

多线程访问同一内存时，需要注意线程同步机制，必要时加锁

### data race on vptr

**背景**

一个线程在删除某个对象（obj）、一个线程在调用虚函数（obj->vcall）

**错误代码实例**

```
1. #include <semaphore.h>
2. #include <pthread.h>

5. struct A {
6. A() {
7. sem_init(&sem_, 0, 0);
8. }
9. virtual void F() {
10. }
11. void Done() {
12. sem_post(&sem_);
13. }
14. virtual ~A() {
15. sem_wait(&sem_);
16. sem_destroy(&sem_);
17. }
18. sem_t sem_;
19. };

22. struct B : A {
23. virtual void F() {
24. }
25. virtual ~B() { }
26. };

29. static A *obj = new B;

32. void *Thread1(void *x) {
33. obj->F();
34. obj->Done();
35. return NULL;
36. }

39. void *Thread2(void *x) {
40. delete obj;
41. return NULL;
42. }

45. static napi_value Add(napi_env env, napi_callback_info info){
46. ...
47. pthread_t t[2];
48. pthread_create(&t[0], NULL, Thread1, NULL);
49. pthread_create(&t[1], NULL, Thread2, NULL);
50. pthread_join(t[0], NULL);
51. pthread_join(t[1], NULL);
52. ...
53. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L36-L88)

**影响**

线程行为发生冲突，程序崩溃

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: data race on vptr（ctor/dtor vs virtual call）

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/wGlc0JhtSp2cDeEUs-oHaw/zh-cn_image_0000002537431253.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=0DC114EEBFCF9148622E190B0309394CEB02CFD81C615D37C684EEBC3AD9123F)

**修改方法**

设置合适的线程同步机制，如锁。

**推荐建议**

确保设置合适的线程同步机制，来保证线程执行逻辑先后的准确性。

### Use After Free

**heap-use-after-free**

**背景**

使用了释放的内存（多线程层面）。

**错误代码实例**

```
1. #include <pthread.h>

4. int *mem;
5. pthread_mutex_t mtx;

8. void *Thread1(void *x) {
9. pthread_mutex_lock(&mtx);
10. free(mem);
11. pthread_mutex_unlock(&mtx);
12. return NULL;
13. }

16. __attribute__((noinline)) void *Thread2(void *x) {
17. pthread_mutex_lock(&mtx);
18. mem[0] = 42;
19. pthread_mutex_unlock(&mtx);
20. return NULL;
21. }

24. static napi_value Add(napi_env env, napi_callback_info info){
25. ...
26. mem = (int*)malloc(100);
27. pthread_mutex_init(&mtx, 0);
28. pthread_t t;
29. pthread_create(&t, NULL, Thread1, NULL);
30. Thread2(0);
31. pthread_join(t, NULL);
32. pthread_mutex_destroy(&mtx);
33. ...
34. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L92-L125)

**影响**

导致程序存在安全漏洞，并有崩溃风险。

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: heap-use-after-free

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/lYJZZ5qmSQykB-VRUFV2CQ/zh-cn_image_0000002537431429.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=A35C689F3C5CE5F0290D5F2B9EEE8ABCF742F77EA53962E36687BC4CE903C53F)

**修改方法**

已释放的内存不要使用，释放的内存需要标记，方便其它线程判断

**推荐建议**

使用合理的线程同步机制

### Signal Check

**signal handler spoils errno**

**背景**

信号处理函数中修改了errno变量

**错误代码实例**

```
1. #include "napi/native_api.h"
2. #include <signal.h>
3. #include <sys/types.h>
4. #include <errno.h>
5. #include <malloc.h>
6. #include <pthread.h>

9. static void MyHandler(int, siginfo_t *s, void *c) {
10. errno = 1;
11. done = 1;
12. }

15. static void* sendsignal(void *p) {
16. pthread_kill(mainth, SIGPROF);
17. return 0;
18. }

21. static __attribute__((noinline)) void loop() {
22. while (done == 0) {
23. volatile char *p = (char*)malloc(1);
24. p[0] = 0;
25. free((void*)p);
26. }
27. }

30. static napi_value Add(napi_env env, napi_callback_info info){
31. ...
32. mainth = pthread_self();
33. struct sigaction act = {};
34. act.sa_sigaction = &MyHandler;
35. sigaction(SIGPROF, &act, 0);
36. pthread_t th;
37. pthread_create(&th, 0, sendsignal, 0);
38. loop();
39. pthread_join(th, 0);
40. ...
41. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L129-L169)

**影响**

导致程序存在安全漏洞，并有崩溃风险。

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: signal handler spoils errno

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/vw6Dh4DnQc6NkZHIY7CyHw/zh-cn_image_0000002505631712.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=464BABF78684B7CEA82F3044612F5CCB6F4EF64E378055572F8CE72C9A1F979E)

**修改方法**

不要在信号处理函数中修改error变量

**推荐建议**

将MyHandler中的error赋值语句去掉

### signal unsafe call inside of a signal

**背景**

信号处理函数中调用了非信号安全的函数（比如malloc）

**错误代码实例**

```
1. #include "napi/native_api.h"
2. #include <signal.h>
3. #include <sys/types.h>
4. #include <malloc.h>
5. #include <pthread.h>
6. #include <sys/types.h>
7. #include <unistd.h>
8. #include <stdio.h>

11. pthread_t mainth;
12. volatile int done;

15. static void handler(int, siginfo_t*, void*) {
16. volatile char *p = (char*)malloc(1);
17. p[0] = 0;
18. free((void*)p);
19. }

22. static napi_value Add(napi_env env, napi_callback_info info)
23. {
24. ...
25. struct sigaction act = {};
26. act.sa_sigaction = &handler;
27. sigaction(SIGPROF, &act, 0);
28. kill(getpid(), SIGPROF);
29. sleep(1);
30. fprintf(stderr, "DONE\n");
31. ...
32. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L173-L204)

**影响**

导致程序存在安全漏洞，并有崩溃风险。

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: signal-unsafe call inside of a signal

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置**。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mvUVfkP-RFm9oHXKUyzgYA/zh-cn_image_0000002537311831.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=1A6CEA7C91F467EAD3A0C3179A6605BAD17536666EB86BC05824EB5665482748)

**修改方法**

将信号处理函数中的malloc去掉，在其外部预先分配内存。

**推荐建议**

建议信号处理程序之外预先分配内存，或者尽可能避免在信号处理程序中进行内存分配和复杂的操作。如果需要在程序中替换malloc，可以考虑使用\_\_malloc\_hook或者宏定义等方法

### Mutex Check

**unlock of an unlocked mutex（or by a wrong thread）**

**背景**

解锁一个已经解锁/自己不拥有的锁

**错误代码实例**

```
1. #include "napi/native_api.h"
2. #include <pthread.h>
3. #include <iostream>

6. pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

9. void* unlocker(void* arg) {
10. pthread_mutex_unlock(&mutex);
11. return nullptr;
12. }

15. static napi_value Add(napi_env env, napi_callback_info info){
16. ...
17. pthread_t tid;
18. pthread_create(&tid, nullptr, unlocker, nullptr);
19. pthread_join(tid, nullptr);
20. ...
21. }
```

[UseTSANToDetectThreadingIssues.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/ThreadIssueDetection/entry/src/main/ets/cpp/UseTSANToDetectThreadingIssues.cpp#L208-L228)

**影响**

导致程序存在安全漏洞，并有崩溃风险。

开启TSan检测后，触发demo中的函数，应用闪退报TSan，包含字段：ThreadSanitizer: unlock of an unlocked mutex（or by a wrong thread）

**定位思路**

如果有工程代码，直接开启TSan检测，debug模式运行后复现该错误，可以触发TSan，直接点击堆栈中的超链接定位到代码行，能看到错误代码的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ASji8YXvQ1i0SZbwsJM5Gw/zh-cn_image_0000002505472236.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=099EB00C068D881A405CB708B287F0319E88B053EF5AC562FBCFE4EE47BF20F5)

**修改方法**

先使用try\_lock()接口获取锁，再使用unlock()接口解锁

**推荐建议**

尽量不要释放自己线程未持有的锁
