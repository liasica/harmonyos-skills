---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-thread-priority-setting
title: 高负载场景线程优先级设置
breadcrumb: 最佳实践 > NDK开发 > 高负载场景线程优先级设置
category: best-practices
scraped_at: 2026-04-28T08:20:55+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1311b9687442ca6f2870316af9de865cab8186ad093498ef3f0f0a3381b19356
---

## 概述

在现代软件开发中，多线程或多进程的并发处理已成为常态。在多线程环境中，不同线程执行的任务可能具有不同的重要性和紧急程度。在高负载情况下，系统资源（如CPU时间）变得尤为宝贵，此时若关键线程（例如UI渲染线程）因频繁被非关键线程抢占而无法获得足够的连续执行时间和资源保障，可能会导致画面卡顿、延迟等问题，从而严重影响用户体验。

## 解决思路

在负载较重的时候，为了让关键的任务能够拿到足够的资源，系统会依据任务的重要性，给任务分配相应的时间片，重要性越高的任务，可以分配到越多的时间片。那么开发者在可以识别自己应用中的关键线程的情况下，针对各个线程的任务紧急程度，给予关键线程相对较高的QoS等级以防止被其他线程打断，从而保证应用的流畅运行和更好的用户体验。

### QoS

[服务质量（QoS）](../harmonyos-guides/qos-guidelines.md)一文介绍了QoS的基本概念、原理、各个QoS等级适用的场景及负载特征及相关接口的用法。

在操作系统层面，QoS等级是一种用于区分不同线程优先级和服务质量的技术。通常系统会自动识别主线程，并在前台焦点情况下为其配置高于开放给应用开发者调用的QoS等级，以确保其优先执行。

与ArkTS端 [taskpool.Priority](../harmonyos-references/js-apis-taskpool.md#priority) 的线程优先级类似，QoS提供的优先级等级也都会相对应的映射到内核的优先级上。不过QoS提供的等级更多，自适应调度策略更强，它们属于两套不同的逻辑。

[FFRT（Function Flow运行时）](../harmonyos-guides/ffrt-overview.md)的QoS提供了ffrt\_qos\_inherit（-1）到ffrt\_qos\_user\_initiated（3）5个优先等级，它与当前的QoS接口有着同一套底层逻辑。两者的差别在于，当前开发所用的QoS接口是直接开放给应用线程的，而FFRT的QoS则是面向任务的优先级配置，关于线程编程模型和任务编程模型的对比详见 [FFRT 概述](../harmonyos-guides/ffrt-overview.md)。

## 场景示例

下面是一个在高负载情况下，配置了不同QoS等级的两个关键线程完成相同计算任务所花时间的对比图，从界面的运行结果可以看到在高负载情况下，配置了高优先级的线程执行完计算所花的时间更少一些。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/uC43GoUVRMOGUweGx4mj8g/zh-cn_image_0000002193851680.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002054Z&HW-CC-Expire=86400&HW-CC-Sign=4C47FCF7D225C54A81639CF3F23184C72ECEDF96A59E4B6CECC4A87F80E033FB "点击放大")

具体实现步骤如下：

1、实现负载线程所要完成的任务。

```
1. // the Load task
2. void AddLoads(int n) {
3. if (!n) {
4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "invalid input.");
5. return;
6. }

8. // set QoS level
9. int ret = OH_QoS_SetThreadQoS(QoS_Level::QOS_BACKGROUND);
10. if (ret) {
11. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "set load thread QoS level failed.");
12. return;
13. }

15. // bind cpu
16. cpu_set_t mask;
17. CPU_SET(*g_affinity, &mask);
18. if (sched_setaffinity(0, sizeof(mask), &mask) != 0) {
19. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "bind load thread failed");
20. return;
21. }
22. // Perform load calculation
23. for (int i = 0; i < BOUND; i++) {
24. for (int j = 0; j < BOUND; j++) {
25. int x = (i + j) - n;
26. printf("%d", x);
27. }
28. }
29. // reset load flag
30. g_addLoad = false;
31. }
```

[main.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NdkQoS/entry/src/main/cpp/main.cpp#L105-L135)

2、实现高、低QoS等级计算线程（关键线程）所要完成的计算任务（斐波那契数列计算）。先通过 [OH\_QoS\_SetThreadQoS](../harmonyos-guides/qos-guidelines.md#oh_qos_setthreadqos) 接口设置当前线程的QoS等级，再执行 DoFib() 斐波那契数列计算。

```
1. // Perform Fibonacci sequence calculations
2. long long DoFib(double n) {
3. if (n == ONE) {
4. return ONE;
5. }
6. if (n == TWO) {
7. return TWO;
8. }
9. return DoFib(n - ONE) + DoFib(n - TWO);
10. }

12. void SetQoS(QoS_Level level) {
13. // set QoS level
14. int ret = OH_QoS_SetThreadQoS(level);
15. if (!ret) {
16. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "QoS", "set qos level success.");
17. //  query qos level
18. QoS_Level queryLevel = QOS_DEFAULT;
19. ret = OH_QoS_GetThreadQoS(&queryLevel);
20. if (!ret) {
21. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "QoS", "the qos level of current thread : %{public}d",
22. queryLevel);
23. } else {
24. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "get qos level failed.");
25. return;
26. }
27. } else {
28. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "get level qos failed!");
29. return;
30. }

32. // bind cpu
33. cpu_set_t mask;
34. CPU_SET(*g_affinity, &mask);
35. if (sched_setaffinity(0, sizeof(mask), &mask) != 0) {
36. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "bind qos thread failed");
37. return;
38. }
39. auto startTime = std::chrono::system_clock::now();
40. // Execute computational tasks
41. long long res = DoFib(DEPTH);
42. auto endTime = std::chrono::system_clock::now();
43. g_durationTime = std::chrono::duration<double, std::milli>(endTime - startTime).count();
44. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "QoS", "calculate res is: %{public}llu", res);

46. // Reset QoS level
47. ret = OH_QoS_ResetThreadQoS();
48. if (!ret) {
49. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "QoS", "reset qos level success.");
50. } else {
51. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "reset qos level failed!");
52. return;
53. }

55. // after reset QoS, query QoS again will fail
56. QoS_Level queryLevelTwo;
57. ret = OH_QoS_GetThreadQoS(&queryLevelTwo);
58. if (!ret) {
59. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "QoS", "the qos level after: %{public}d", queryLevelTwo);
60. return;
61. } else {
62. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "QoS", "query qos level failed after reset.");
63. return;
64. }
65. }
```

[main.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NdkQoS/entry/src/main/cpp/main.cpp#L37-L101)

3、然后分别将计算线程（关键线程）设置低、高QoS等级来对比两者在相同的高负载情况下完成相同层级的斐波那契数列计算所花时间。

* **给计算线程配置低QoS等级**

  ```
  1. static napi_value lowQoSCalculate(napi_env env, napi_callback_info info) {
  2. g_durationTime = 0;
  3. // Simulate system load
  4. if (!g_addLoad) {
  5. std::vector<std::thread> loadThreads;
  6. for (int i = 0; i < TASKS; i++) {
  7. // Activate threads to execute load tasks
  8. loadThreads.emplace_back(std::thread(AddLoads, TASKS));
  9. loadThreads[i].detach();
  10. }
  11. g_addLoad = true;
  12. }

  14. // set QOS_BACKGROUND level
  15. QoS_Level level = QoS_Level::QOS_BACKGROUND;
  16. std::thread task(SetQoS, level);
  17. task.join();

  19. // Return calculation time
  20. napi_value res;
  21. napi_create_double(env, g_durationTime, &res);
  22. return res;
  23. }
  ```

  [main.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NdkQoS/entry/src/main/cpp/main.cpp#L164-L186)

计算线程（线程id：39260）设置低QoS等级trace图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/9v7X3XzOSxqZmHJ-WAwLwg/zh-cn_image_0000002193851672.png?HW-CC-KV=V1&HW-CC-Date=20260428T002054Z&HW-CC-Expire=86400&HW-CC-Sign=74E857AB9D5972371F59AF63C0301516386CA19F13CC1CABAFE81DE0210B5F56 "点击放大")

如上图所示，计算线程执行完计算任务耗时726.8毫秒。

* **给计算线程配置高QoS等级**

  ```
  1. static napi_value highQoSCalculate(napi_env env, napi_callback_info info) {
  2. g_durationTime = 0;
  3. // Simulate system load
  4. if (!g_addLoad) {
  5. std::vector<std::thread> loadThreads;
  6. for (int i = 0; i < TASKS; i++) {
  7. // Activate threads to execute load tasks
  8. loadThreads.emplace_back(std::thread(AddLoads, TASKS));
  9. loadThreads[i].detach();
  10. }
  11. g_addLoad = true;
  12. }
  13. // set QOS_USER_INTERACTIVE level
  14. QoS_Level level = QoS_Level::QOS_USER_INTERACTIVE;
  15. std::thread task(SetQoS, level);
  16. task.join();

  18. // Return calculation time
  19. napi_value res;
  20. napi_create_double(env, g_durationTime, &res);
  21. return res;
  22. }
  ```

  [main.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NdkQoS/entry/src/main/cpp/main.cpp#L139-L160)

计算线程（线程id：39204）设置高QoS等级trace图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/_KZ1umIDQOaKqOOrf7R-xA/zh-cn_image_0000002193851676.png?HW-CC-KV=V1&HW-CC-Date=20260428T002054Z&HW-CC-Expire=86400&HW-CC-Sign=76B2B214DB1993321FA8107B52DAC5FD1B5D22ABB9A0F6B96F1C64BE340E23B8 "点击放大")

如上图所示，计算线程执行完计算任务耗时323.9毫秒。

说明

该示例只在高负载压力下有效。

在低负载情况下，由于系统资源相对充足，大多数线程能够获得足够的CPU时间，因此优先级设置对线程执行效率的影响不明显。

## 总结

| 方案 | 斐波那契数列项数 | 计算耗时 |
| --- | --- | --- |
| 低QoS等级 QOS\_BACKGROUND | 34 | 726.8毫秒 |
| 高QoS等级 QOS\_USER\_INTERACTIVE | 34 | 323.9毫秒 |

通过上述对比可以发现， **高负载压力下**，高QoS优先级的线程可以更快的执行完计算任务。因此在实践中我们通过合理设置线程优先级，给关键线程以相对较高的QoS等级可以有效地避免关键线程被打断，从而保证应用程序的稳定性和响应性。

注意

由于整机资源有限，若应用内部方法均设置高QoS等级，将导致资源相互抢占。此外，高QoS等级线程会相比低等级线程获取更多资源，过度提升线程QoS等级可能引起其他线程饥饿，从而影响整个系统的稳定运行。因此，线程QoS等级的设置需要结合具体应用场景和需求。

## 示例代码

* [基于QoS设置线程优先级](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/NdkQoS)
