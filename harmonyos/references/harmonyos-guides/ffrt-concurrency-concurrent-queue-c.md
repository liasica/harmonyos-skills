---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ffrt-concurrency-concurrent-queue-c
title: Function Flow Runtime并发队列(C)
breadcrumb: 指南 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > Function Flow Runtime开发样例(C) > Function Flow Runtime并发队列(C)
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:28+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:cb51f41a00083a1937db49f4cd0c1b520c5be89c2847365c6dc0fd7e52e75353
---

## 概述

FFRT并发队列提供了设置任务优先级（Priority）和队列并发度的能力，使得队列中的任务能同时在多个线程上执行，获得更高的并行效果。

* **队列并发度**：通过队列最大并发度设置，可以控制同一时刻同时执行的任务数量。这有助于避免任务并发过多对系统资源造成冲击，从而保证系统的稳定性和性能。
* **任务优先级**：用户可以为每个任务设置优先级，不同的任务将严格按照优先级进行调度和执行。相同优先级的任务按照排队顺序执行，高优先级的任务将优先于低优先级的任务执行，确保关键任务能够及时处理。

## 示例：银行服务系统

举例实现一个银行服务系统，每个客户向系统提交一个服务请求，可以区分普通用户和VIP用户，VIP用户的服务请求可以优先得到执行。银行系统中有2个窗口，可以并行取出用户提交的服务请求办理。

可以利用FFRT的并行队列范式做如下建模：

* **排队逻辑**：并行队列。
* **服务窗口**：并行队列的并发度，同时也对应FFRT Worker数量。
* **用户等级**：并行队列任务优先级。

实现代码如下所示：

```
1. #include <cstdio>
2. #include <unistd.h>
3. #include "hilog/log.h"
4. #include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"

6. #undef LOG_TAG
7. #define LOG_TAG "ConcurrentTag"
```

```
1. const int SLEEP_TIME = 100 * 1000;
2. const int BANK_CONCURRENCY = 2;

4. ffrt_queue_t CreateBankSystem(const char *name, int concurrency)
5. {
6. ffrt_queue_attr_t queue_attr;
7. (void)ffrt_queue_attr_init(&queue_attr);
8. ffrt_queue_attr_set_max_concurrency(&queue_attr, concurrency);

10. // 创建一个并发队列
11. ffrt_queue_t queue = ffrt_queue_create(ffrt_queue_concurrent, name, &queue_attr);

13. // 队列创建完后需要销毁队列属性
14. ffrt_queue_attr_destroy(&queue_attr);
15. if (!queue) {
16. OH_LOG_INFO(LOG_APP, "create queue failed");
17. return NULL;
18. }

20. OH_LOG_INFO(LOG_APP, "create bank system successfully");
21. return queue;
22. }

24. void DestroyBankSystem(ffrt_queue_t queue_handle)
25. {
26. ffrt_queue_destroy(queue_handle);
27. OH_LOG_INFO(LOG_APP, "destroy bank system successfully");
28. }

30. void BankBusiness(void *arg)
31. {
32. usleep(SLEEP_TIME);
33. const char *data = (const char *)arg;
34. OH_LOG_INFO(LOG_APP, "saving or withdraw for %{public}s", data);
35. }

37. // 封装提交队列任务函数
38. ffrt_task_handle_t CommitRequest(ffrt_queue_t bank, void (*func)(void *), const char *name,
39. ffrt_queue_priority_t level, int delay)
40. {
41. ffrt_task_attr_t task_attr;
42. (void)ffrt_task_attr_init(&task_attr);
43. ffrt_task_attr_set_name(&task_attr, name);
44. ffrt_task_attr_set_queue_priority(&task_attr, level);
45. ffrt_task_attr_set_delay(&task_attr, delay);

47. return ffrt_queue_submit_h_f(bank, func, (void*)name, &task_attr);
48. }

50. // 封装取消队列任务函数
51. int CancelRequest(ffrt_task_handle_t request)
52. {
53. return ffrt_queue_cancel(request);
54. }

56. // 封装等待队列任务函数
57. void WaitForRequest(ffrt_task_handle_t task)
58. {
59. ffrt_queue_wait(task);
60. }

62. int ConcurrentQueueCExec()
63. {
64. ffrt_queue_t bank = CreateBankSystem("Bank", BANK_CONCURRENCY);
65. if (!bank) {
66. printf("create bank system failed\n");
67. OH_LOG_INFO(LOG_APP, "create bank system failed");
68. return -1;
69. }

71. ffrt_task_handle_t task1 = CommitRequest(bank, BankBusiness, "customer1", ffrt_queue_priority_low, 0);
72. ffrt_task_handle_t task2 = CommitRequest(bank, BankBusiness, "customer2", ffrt_queue_priority_low, 0);
73. // VIP享受更优先的服务
74. ffrt_task_handle_t task3 = CommitRequest(bank, BankBusiness, "customer3 VIP", ffrt_queue_priority_high, 0);
75. ffrt_task_handle_t task4 = CommitRequest(bank, BankBusiness, "customer4", ffrt_queue_priority_low, 0);
76. ffrt_task_handle_t task5 = CommitRequest(bank, BankBusiness, "customer5", ffrt_queue_priority_low, 0);

78. // 取消客户4的服务
79. CancelRequest(task4);

81. // 等待所有的客户服务完成
82. WaitForRequest(task5);
83. DestroyBankSystem(bank);

85. ffrt_task_handle_destroy(task1);
86. ffrt_task_handle_destroy(task2);
87. ffrt_task_handle_destroy(task3);
88. ffrt_task_handle_destroy(task4);
89. ffrt_task_handle_destroy(task5);
90. return 0;
91. }
```

说明

ffrt\_queue\_submit\_h\_f接口可以接收裸函数指针任务作为参数，如果任务存在前后处理可以参见[ffrt\_alloc\_auto\_managed\_function\_storage\_base](ffrt-api-guideline-c.md#ffrt_alloc_auto_managed_function_storage_base)函数查看如何构造任务结构体。

## 接口说明

上述样例中涉及到主要的FFRT的接口包括：

| 名称 | 描述 |
| --- | --- |
| [ffrt\_queue\_create](ffrt-api-guideline-c.md#ffrt_queue_t) | 创建队列。 |
| [ffrt\_queue\_destroy](ffrt-api-guideline-c.md#ffrt_queue_t) | 销毁队列。 |
| [ffrt\_task\_attr\_set\_queue\_priority](ffrt-api-guideline-c.md#ffrt_task_attr_t) | 设置队列任务优先级。 |
| [ffrt\_queue\_attr\_set\_max\_concurrency](ffrt-api-guideline-c.md#ffrt_queue_attr_t) | 设置并发队列的并发度。 |
| [ffrt\_queue\_submit\_h\_f](ffrt-api-guideline-c.md#ffrt_queue_t) | 向队列提交一个任务。  **说明**：从API version 20开始，支持该接口。 |

说明

* 如何使用FFRT C++ API详见：[FFRT C++接口三方库使用指导](ffrt-development-guideline.md#using-ffrt-c-api-1)。
* 使用FFRT C接口或C++接口时，都可以通过FFRT C++接口三方库简化头文件包含，即使用#include "ffrt/ffrt.h"头文件包含语句。

## 约束限制

1. ffrt\_queue\_attr\_t必须先调用ffrt\_queue\_attr\_init初始化后再设置/获取属性，不再使用后需要显式调用ffrt\_queue\_attr\_destroy释放资源。
2. ffrt\_queue\_t必须在进程退出前显式调用ffrt\_queue\_destroy释放资源。
3. 并发队列最大并发度建议控制在合理范围内，配置过大超过Worker线程数没有意义，配置过小可能导致系统资源利用率不足。
