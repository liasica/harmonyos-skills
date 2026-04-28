---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ffrt-concurrency-graph-cpp
title: Function Flow Runtime图依赖并发(C++)
breadcrumb: 指南 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > Function Flow Runtime开发样例(C++) > Function Flow Runtime图依赖并发(C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:29+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:aafeec745daea55de747517f90121d6e76956e7d035e122abf061bcadbfb5ccd
---

## 概述

FFRT图依赖并发范式支持任务依赖和数据依赖两种方式构建任务依赖图。任务依赖图中每个节点表示一个任务，边表示任务之间的依赖关系。任务依赖分为输入依赖in\_deps和输出依赖out\_deps。

构建任务依赖图的两种不同方式：

* 当使用任务依赖方式构建任务依赖图时，使用任务句柄handle来对应一个任务对象。
* 当使用数据依赖方式构建任务依赖图时，数据对象表达抽象为数据签名，每个数据签名唯一对应一个数据对象。

### 任务依赖

说明

当任务句柄出现在一个任务的in\_deps中时，任务句柄对应的任务是该任务的前置任务；当任务句柄出现在一个任务的out\_deps中时，任务句柄对应的任务是该任务的后继任务。

任务依赖适用于任务之间有明确顺序或逻辑流程要求的场景，例如：

* 顺序执行的任务，例如：先进行数据预处理任务，然后再进行模型训练任务。
* 逻辑流程控制，例如：商品交易过程中，通常是先下单，然后是制作，最后是物流运输。
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/bqDTUYufThGjGd_2EpRh-Q/zh-cn_image_0000002583438503.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=4F0022472E3BF3109D61F032EFCAE63772F92096FF43FC114EB0DA6916D9E117)

为表述方便，本文中的数据流图均以圆圈表示Task，方块表示数据。

可以得出以下结论：

* task1与task2/task3构成Producer-Consumer依赖，即：task2/task3需要等到task1写完A之后才能读A。
* task2/task3与task4构成Consumer-Producer依赖，即：task4需要等到task2/task3读完A之后才能写A。
* task4与task5构成Producer-Producer依赖，即：task5需要等到task4写完A之后才能写A。

## 示例：流媒体视频处理

用户上传视频到流媒体平台，处理步骤包含：视频解析A、视频转码B、视频缩略图生成C、视频水印添加D和视频发布E，其中步骤B和步骤C可以并行执行。任务流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/dhIdTxe9QuedXRhqPoEgvQ/zh-cn_image_0000002552958458.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=6ABA73DBC9E9D8D8CDBA1F5DEE36424E737580D963567DC2E2634DE3C12C4E20)

借助FFRT提供了图依赖并发范式，可以描述任务依赖关系，同时并行化上述视频处理流程，代码如下所示：

```
1. #include <iostream>
2. #include "hilog/log.h"
3. #include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"

5. #undef LOG_TAG
6. #define LOG_TAG "ParallelCppTag"
```

```
1. const int FIB_NUM = 5;

3. int DependenceCppExec()
4. {
5. // 提交任务
6. auto handle_A = ffrt::submit_h([] () { OH_LOG_INFO(LOG_APP, "视频解析"); });
7. auto handle_B = ffrt::submit_h([] () { OH_LOG_INFO(LOG_APP, "视频转码"); }, {handle_A});
8. auto handle_C = ffrt::submit_h([] () { OH_LOG_INFO(LOG_APP, "视频生成缩略图"); }, {handle_A});
9. auto handle_D = ffrt::submit_h([] () { OH_LOG_INFO(LOG_APP, "视频添加水印"); }, {handle_B, handle_C});
10. ffrt::submit([] () { OH_LOG_INFO(LOG_APP, "视频发布"); }, {handle_D});

12. // 等待所有任务完成
13. ffrt::wait();
14. return 0;
15. }
```

预期的输出可能为：

```
1. 视频解析
2. 视频转码
3. 视频生成缩略图
4. 视频添加水印
5. 视频发布
```

## 示例：斐波那契数列

斐波那契数列中每个数字是前两个数字之和，计算斐波那契数的过程可以很好地通过数据对象来表达任务依赖关系。使用FFRT并发编程框架计算斐波那契数的代码如下所示：

```
1. #include <iostream>
2. #include "hilog/log.h"
3. #include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"

5. #undef LOG_TAG
6. #define LOG_TAG "ParallelCppTag"
```

```
1. void Fib(int x, int& y)
2. {
3. if (x <= 1) {
4. y = x;
5. } else {
6. int y1;
7. int y2;

9. // 提交任务并构建数据依赖
10. ffrt::submit([&]() { Fib(x - 1, y1); }, {&x}, {&y1});
11. // 斐波那契数列所需递归-2
12. ffrt::submit([&]() { Fib(x - 2, y2); }, {&x}, {&y2});

14. // 等待任务完成
15. ffrt::wait({&y1, &y2});
16. y = y1 + y2;
17. }
18. }

20. int FibCppExec()
21. {
22. int y;
23. Fib(FIB_NUM, y);
24. std::cout << "Fibonacci(5) is " << y << std::endl;
25. OH_LOG_INFO(LOG_APP, "Fibonacci(5) is %{pubilc}d", y);
26. return y;
27. }
```

预期输出为：

```
1. Fibonacci(5) is 5
```

示例中将fibonacci(x-1)和fibonacci(x-2)作为两个任务提交给FFRT，在两个任务完成之后将结果进行累加。虽然单个任务只是拆分成两个子任务，但是子任务又可以继续进行拆分，因此整个计算图的并行度是非常高的。

各个任务在FFRT内部形成了一棵调用树：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/a1T_yLqgRYS0GsWmZEVlnQ/zh-cn_image_0000002583478459.png?HW-CC-KV=V1&HW-CC-Date=20260427T234428Z&HW-CC-Expire=86400&HW-CC-Sign=52DD0FADABE6C093E244D3D7790599E6058159E496E13480E4B6085186F4EC4D)

## 接口说明

上述样例中涉及到主要的FFRT的接口包括：

| 名称 | 描述 |
| --- | --- |
| [submit](https://gitcode.com/openharmony/resourceschedule_ffrt/blob/master/docs/ffrt-api-guideline-cpp.md#submit) | 提交任务调度执行。 |
| [submit\_h](https://gitcode.com/openharmony/resourceschedule_ffrt/blob/master/docs/ffrt-api-guideline-cpp.md#submit_h) | 提交任务调度执行并返回任务句柄。 |
| [wait](https://gitcode.com/openharmony/resourceschedule_ffrt/blob/master/docs/ffrt-api-guideline-cpp.md#wait) | 等待上下文所有任务完成。 |

说明

* 如何使用FFRT C++ API详见：[FFRT C++接口三方库使用指导](ffrt-development-guideline.md#using-ffrt-c-api-1)。
* 使用FFRT C接口或C++接口时，都可以通过FFRT C++接口三方库简化头文件包含，即使用#include "ffrt/ffrt.h"头文件包含语句。

## 约束限制

* 使用submit接口进行任务提交时，每个任务的输入依赖和输出依赖的数量之和不能超过8个。
* 使用submit\_h接口进行任务提交时，每个任务的输入依赖和输出依赖的数量之和不能超过7个。
* 参数既作为输入依赖又作为输出依赖的时候，统计依赖数量时只统计一次，如输入依赖是{&x}，输出依赖也是{&x}，实际依赖的数量是 1。
