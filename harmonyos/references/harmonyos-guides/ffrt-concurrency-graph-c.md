---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ffrt-concurrency-graph-c
title: Function Flow Runtime图依赖并发(C)
breadcrumb: 指南 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > Function Flow Runtime开发样例(C) > Function Flow Runtime图依赖并发(C)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:29+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:d8f777228413e534f38d60d2c21d8c5528adaa7f0853ab17a20a4619be6ae09e
---

## 概述

FFRT图依赖并发范式支持任务依赖和数据依赖两种方式构建任务依赖图。任务依赖图中每个节点代表一个任务，边代表任务之间的依赖关系。任务依赖分为输入依赖in\_deps和输出依赖out\_deps。

构建任务依赖图的两种不同方式：

* 当使用任务依赖方式构建任务依赖图时，使用任务句柄handle来对应一个任务对象。
* 当使用数据依赖方式构建任务依赖图时，数据对象表达抽象为数据签名，每个数据签名唯一对应一个数据对象。

### 任务依赖

说明

当任务句柄出现在一个任务的in\_deps中时，任务句柄对应的任务是该任务的前置任务；当任务句柄出现在一个任务的out\_deps中时，任务句柄对应的任务是该任务的后继任务。

任务依赖适用于任务之间有明确顺序或逻辑流程要求的场景，例如：

* 顺序执行的任务，例如：先进行数据预处理任务，然后再进行模型训练任务。
* 逻辑流程控制，例如：商品交易过程需依次执行下单、制作和物流运输三个步骤。
* 多级任务链，例如：流媒体视频处理过程中，视频解析后可以进行视频转码和视频生成缩略图，然后是视频添加水印，最后是视频发布。

### 数据依赖

说明

当数据对象的签名出现在一个任务的in\_deps中时，该任务称为数据对象的消费者任务，消费者任务执行不改变其输入数据对象的内容；

当数据对象的签名出现在任务的out\_deps中时，该任务称为数据对象的生产者任务，生产者任务执行改变其输出数据对象的内容，从而生成该数据对象的一个新的版本。

数据依赖适用于任务之间通过数据生产和消费关系来触发执行的场景。

一个数据对象可能存在多个版本，每个版本对应一个生产者任务和零个，一个或多个消费者任务，根据生产者任务和消费者任务的下发顺序定义数据对象的多个版本的顺序，以及每个版本所对应的生产者和消费者任务。

数据依赖解除的任务进入就绪状态允许被调度执行，依赖解除状态指任务所有输入数据对象版本的生产者任务执行完成，且所有输出数据对象版本的所有消费者任务执行完成的状态。

FFRT在运行时可动态构建任务之间的基于生产者/消费者的数据依赖关系并遵循任务数据依赖状态执行调度，包括：

* Producer-Consumer依赖

  一个数据对象版本的生产者任务和该数据对象版本的消费者任务之间形成的依赖关系，也称为Read-after-Write依赖。
* Consumer-Producer依赖

  一个数据对象版本的消费者任务和该数据对象的下一个版本的生产者任务之间形成的依赖关系，也称为Write-after-Read依赖。
* Producer-Producer依赖

  一个数据对象版本的生产者任务和该数据对象的下一个版本的生产者任务之间形成的依赖关系，也称为Write-after-Write依赖。

例如，存在一组任务与数据A的关系表述为：

```
1. task1(OUT A);
2. task2(IN A);
3. task3(IN A);
4. task4(OUT A);
5. task5(OUT A);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/IcQu3vmRTZG0-fsOIg3MmA/zh-cn_image_0000002583438503.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=E2D69BD71063677EB90C34F141D28C57901EE2E637DFEE0340D0C5219B53C408)

为表述方便，本文中的数据流图均以圆圈表示Task，方块表示数据。

可以得出以下结论：

* task1与task2/task3构成Producer-Consumer依赖，即：task2/task3需要等到task1写完A之后才能读A。
* task2/task3与task4构成Consumer-Producer依赖，即：task4需要等到task2/task3读完A之后才能写A。
* task4与task5构成Producer-Producer依赖，即：task5需要等到task4写完A之后才能写A。

## 示例：流媒体视频处理

用户上传视频到流媒体平台，处理步骤包含：视频解析A、视频转码B、视频缩略图生成C、视频水印添加D和视频发布E，其中步骤B和步骤C可以并行执行。任务流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/1uoEPipNQRKgQuIzbBeA0A/zh-cn_image_0000002552958458.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=587EF98C7101213DCED4092AB1CCA3C8BAF6EE6D089F9372CDE1AD12B2D65986)

借助FFRT提供了图依赖并发范式，可以描述任务依赖关系，同时并行化上述视频处理流程，代码如下所示：

```
1. #include <cstdio>
2. #include "hilog/log.h"
3. #include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"

5. #undef LOG_TAG
6. #define LOG_TAG "ParallelTag"
```

```
1. void FuncTaskA(void* arg)
2. {
3. OH_LOG_INFO(LOG_APP, "视频解析");
4. printf("视频解析\n");
5. }

7. void FuncTaskB(void* arg)
8. {
9. OH_LOG_INFO(LOG_APP, "视频转码");
10. printf("视频转码\n");
11. }

13. void FuncTaskC(void* arg)
14. {
15. OH_LOG_INFO(LOG_APP, "视频生成缩略图");
16. printf("视频生成缩略图\n");
17. }

19. void FuncTaskD(void* arg)
20. {
21. OH_LOG_INFO(LOG_APP, "视频添加水印");
22. printf("视频添加水印\n");
23. }

25. void FuncTaskE(void* arg)
26. {
27. OH_LOG_INFO(LOG_APP, "视频发布");
28. printf("视频发布\n");
29. }

31. int DependenceCExec()
32. {
33. // 提交任务A
34. ffrt_task_handle_t hTaskA = ffrt_submit_h_f(FuncTaskA, NULL, NULL, NULL, NULL);

36. // 提交任务B和C
37. ffrt_dependence_t taskA_deps[] = {{ffrt_dependence_task, hTaskA}};
38. ffrt_deps_t dTaskA = {1, taskA_deps};
39. ffrt_task_handle_t hTaskB = ffrt_submit_h_f(FuncTaskB, NULL, &dTaskA, NULL, NULL);
40. ffrt_task_handle_t hTaskC = ffrt_submit_h_f(FuncTaskC, NULL, &dTaskA, NULL, NULL);

42. // 提交任务D
43. ffrt_dependence_t taskBC_deps[] = {{ffrt_dependence_task, hTaskB}, {ffrt_dependence_task, hTaskC}};
44. ffrt_deps_t dTaskBC = {2, taskBC_deps};
45. ffrt_task_handle_t hTaskD = ffrt_submit_h_f(FuncTaskD, NULL, &dTaskBC, NULL, NULL);

47. // 提交任务E
48. ffrt_dependence_t taskD_deps[] = {{ffrt_dependence_task, hTaskD}};
49. ffrt_deps_t dTaskD = {1, taskD_deps};
50. ffrt_submit_f(FuncTaskE, NULL, &dTaskD, NULL, NULL);

52. // 等待所有任务完成
53. ffrt_wait();

55. ffrt_task_handle_destroy(hTaskA);
56. ffrt_task_handle_destroy(hTaskB);
57. ffrt_task_handle_destroy(hTaskC);
58. ffrt_task_handle_destroy(hTaskD);
59. return 0;
60. }
```

预期的输出可能为：

```
1. 视频解析
2. 视频转码
3. 视频生成缩略图
4. 视频添加水印
5. 视频发布
```

说明

ffrt\_submit\_h\_f和ffrt\_submit\_f接口可以接收裸函数指针任务作为参数，如果任务存在前后处理可以参见[ffrt\_alloc\_auto\_managed\_function\_storage\_base](ffrt-api-guideline-c.md#ffrt_alloc_auto_managed_function_storage_base)函数查看如何构造任务结构体。

## 示例：斐波那契数列

斐波那契数列中每个数字是前两个数字之和，计算斐波那契数的过程可以很好地通过数据对象来表达任务依赖关系。使用FFRT并发编程框架计算斐波那契数的代码如下所示：

```
1. #include <cstdio>
2. #include "hilog/log.h"
3. #include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"

5. #undef LOG_TAG
6. #define LOG_TAG "ParallelTag"
```

```
1. const int FIB_NUM = 5;
2. typedef struct {
3. int x;
4. int* y;
5. } FibFfrtS;

7. void FibFfrt(void* arg)
8. {
9. FibFfrtS* p = (FibFfrtS*)arg;
10. int x = p->x;
11. int* y = p->y;

13. if (x <= 1) {
14. *y = x;
15. } else {
16. int y1;
17. int y2;
18. FibFfrtS s1 = {x - 1, &y1};
19. FibFfrtS s2 = {x - 2, &y2};

21. // 构建数据依赖
22. ffrt_dependence_t dx_deps[] = {{ffrt_dependence_data, &x}};
23. ffrt_deps_t dx = {1, dx_deps};
24. ffrt_dependence_t dy1_deps[] = {{ffrt_dependence_data, &y1}};
25. ffrt_deps_t dy1 = {1, dy1_deps};
26. ffrt_dependence_t dy2_deps[] = {{ffrt_dependence_data, &y2}};
27. ffrt_deps_t dy2 = {1, dy2_deps};
28. ffrt_dependence_t dy12_deps[] = {{ffrt_dependence_data, &y1}, {ffrt_dependence_data, &y2}};
29. ffrt_deps_t dy12 = {2, dy12_deps};

31. // 分别提交任务
32. ffrt_submit_f(FibFfrt, &s1, &dx, &dy1, NULL);
33. ffrt_submit_f(FibFfrt, &s2, &dx, &dy2, NULL);

35. // 等待任务完成
36. ffrt_wait_deps(&dy12);
37. *y = y1 + y2;
38. }
39. }

41. int FibCExec()
42. {
43. int r;
44. FibFfrtS s = {FIB_NUM, &r};
45. ffrt_dependence_t dr_deps[] = {{ffrt_dependence_data, &r}};
46. ffrt_deps_t dr = {1, dr_deps};
47. ffrt_submit_f(FibFfrt, &s, NULL, &dr, NULL);

49. // 等待任务完成
50. ffrt_wait_deps(&dr);
51. OH_LOG_INFO(LOG_APP, "Fibonacci result: %{public}d", r);
52. printf("Fibonacci(5) is %d\n", r);
53. return r;
54. }
```

预期输出为：

```
1. Fibonacci(5) is 5
```

示例中将fibonacci(x-1)和fibonacci(x-2)作为两个任务提交给FFRT，在两个任务完成之后将结果进行累加。虽然单个任务只是拆分成两个子任务，但是子任务又可以继续进行拆分，因此整个计算图的并行度是非常高的。

说明

ffrt\_submit\_f接口可以接收裸函数指针任务作为参数，如果任务存在前后处理可以参见[ffrt\_alloc\_auto\_managed\_function\_storage\_base](ffrt-api-guideline-c.md#ffrt_alloc_auto_managed_function_storage_base)函数查看如何构造任务结构体。

各个任务在FFRT内部形成了一棵调用树：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/ydWM2LdhSWq6_k0fDahM_w/zh-cn_image_0000002583478459.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=D93F4A73F02C960313ED7BE526F31F2BF493FF10491DE1E519E4B36FCAA0658C)

## 接口说明

上述样例中涉及到主要的FFRT的接口包括：

| 名称 | 描述 |
| --- | --- |
| [ffrt\_submit\_f](ffrt-api-guideline-c.md#ffrt_submit_f) | 提交任务调度执行。  **说明**：从API version 20开始，支持该接口。 |
| [ffrt\_submit\_h\_f](ffrt-api-guideline-c.md#ffrt_submit_h_f) | 提交任务调度执行并返回任务句柄。  **说明**：从API version 20开始，支持该接口。 |
| [ffrt\_wait\_deps](ffrt-api-guideline-c.md#ffrt_wait_deps) | 等待依赖的任务完成。 |

说明

* 如何使用FFRT C++ API详见：[FFRT C++接口三方库使用指导](ffrt-development-guideline.md#using-ffrt-c-api-1)。
* 使用FFRT C接口或C++接口时，均可通过FFRT C++接口三方库简化头文件包含，即使用#include "ffrt/ffrt.h"头文件包含语句。

## 约束限制

* 使用ffrt\_submit\_base接口进行任务提交时，每个任务的输入依赖和输出依赖的数量之和不能超过8个。
* 使用ffrt\_submit\_h\_base接口进行任务提交时，每个任务的输入依赖和输出依赖的数量之和不能超过7个。
* 当参数同时作为输入依赖和输出依赖时，统计依赖数量时只统计一次，如输入依赖是{&x}，输出依赖也是{&x}，实际依赖的数量是1。
