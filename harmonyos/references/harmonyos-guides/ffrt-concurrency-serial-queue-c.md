---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ffrt-concurrency-serial-queue-c
title: Function Flow Runtime串行队列(C)
breadcrumb: 指南 > 系统 > 基础功能 > Function Flow Runtime Kit（任务并发调度服务） > Function Flow Runtime开发样例(C) > Function Flow Runtime串行队列(C)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1e5a9605d32f3471cf891404556ece8ce19002c6a57683baf23cba52686aff79
---

## 概述

FFRT串行队列基于协程调度模型实现，提供高效的消息队列功能，支持异步通信、流量削峰、无锁化状态和资源管理以及架构解耦等多种业务场景。FFRT串行队列支持以下功能：

* **​队列创建销毁**​，支持创建和销毁队列，创建时可指定队列名称和优先级。每个队列功能上相当于一个单独的线程，队列中的任务相对于用户线程异步执行。
* **任务延迟**​，支持在任务提交时设置延迟时间（delay），单位为微秒（us）。延迟任务将在uptime（提交时刻+延迟时间）后调度执行。
* **​串行调度**​，同一队列中的任务按照uptime升序排列，严格串行执行。确保队列中上一个任务完成后，下一个任务才会开始执行。
* **​任务取消**​，支持根据任务句柄取消未出队的任务。若任务已开始执行或执行完成，则无法取消。
* **​任务等待**​，支持根据任务句柄等待任务完成。指定任务完成时，队列中所有uptime早于该任务的任务均已执行完成。
* **任务优先级**​，支持在任务提交时设置单个任务的优先级。优先级仅在任务出队后相对于系统其他负载生效，不影响同一队列内任务的串行顺序。若未设置任务优先级，则默认继承队列的优先级。

## 示例：异步日志系统

举例实现一个异步日志系统，主线程将日志任务提交到队列，后台线程从队列中取出任务并写入文件。这种方式既能保证日志的顺序性，又能避免文件写入操作阻塞主线程。

借助FFRT并行化框架API，开发者只需专注于业务逻辑的实现，无需关注异步线程管理、线程安全及调度效率等问题。

用例简化了异常处理和线程安全相关的一些逻辑，实现代码如下所示：

```c
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include "hilog/log.h"
#include "ffrt/ffrt.h" // 来自 OpenHarmony 第三方库 "@ppd/ffrt"
```

```
#undef LOG_TAG
#define LOG_TAG "SerialTag"

typedef struct {
    FILE *logFile;          // 日志文件指针
    ffrt_queue_t queue;     // 任务队列
} LoggerT;

// 全局Logger变量
LoggerT* g_logger = nullptr;

// 初始化日志系统
LoggerT *LoggerCreate(const char *filename)
{
    LoggerT *logger = (LoggerT *)malloc(sizeof(LoggerT));
    if (!logger) {
        OH_LOG_ERROR(LOG_APP, "Failed to allocate memory for LoggerT");
        return nullptr;
    }

    // 打开日志文件
    logger->logFile = stdout;
    if (!logger->logFile) {
        OH_LOG_ERROR(LOG_APP, "Failed to open log file");
        free(logger);
        return nullptr;
    }
    OH_LOG_INFO(LOG_APP, "Log file opened: %{public}s", filename);

    // 创建任务队列
    logger->queue = ffrt_queue_create(ffrt_queue_serial, "logger_queue_c", NULL);
    if (!logger->queue) {
        OH_LOG_ERROR(LOG_APP, "Failed to create queue");
        fclose(logger->logFile);
        free(logger);
        return nullptr;
    }

    return logger;
}

// 销毁日志系统
void LoggerDestroy(LoggerT *logger)
{
    if (logger) {
        // 销毁队列
        if (logger->queue) {
            ffrt_queue_destroy(logger->queue);
        }

        // 关闭日志文件
        if (logger->logFile) {
            fclose(logger->logFile);
            OH_LOG_INFO(LOG_APP, "Log file closed");
        }

        free(logger);
    }
}

// 日志任务
void WriteTask(void *arg)
{
    char *message = (char *)arg;
    if (g_logger && g_logger->logFile) {
        OH_LOG_INFO(LOG_APP, "Writing message %{public}s", message);
        fflush(g_logger->logFile);
    }

    free(message);
}

// 添加日志任务
void LoggerLog(LoggerT *logger, const char *message)
{
    if (!logger || !logger->queue) {
        return;
    }

    // 复制消息字符串
    char *messageCopy = strdup(message);
    if (!messageCopy) {
        OH_LOG_ERROR(LOG_APP, "Failed to allocate memory for message");
        return;
    }

    ffrt_queue_submit_f(logger->queue, WriteTask, messageCopy, NULL);
}

int SerialQueueCExec()
{
    // 初始化全局logger
    g_logger = LoggerCreate("log_c.txt");
    if (!g_logger) {
        return -1;
    }

    // 使用全局logger添加日志任务
    LoggerLog(g_logger, "Log message 1");
    LoggerLog(g_logger, "Log message 2");
    LoggerLog(g_logger, "Log message 3");

    // 模拟主线程继续执行其他任务
    sleep(1);

    // 销毁全局logger
    LoggerDestroy(g_logger);
    g_logger = nullptr;
    return 0;
}
```

**说明** 

ffrt\_queue\_submit\_h\_f接口可以接收裸函数指针任务作为参数，如果任务存在前后处理可以参见[ffrt\_alloc\_auto\_managed\_function\_storage\_base](ffrt-api-guideline-c.md#ffrt_alloc_auto_managed_function_storage_base)函数查看如何构造任务结构体。

## 接口说明

上述样例中涉及到主要的FFRT的接口如下，详情请参考[ffrt\_queue\_t](ffrt-api-guideline-c.md#ffrt_queue_t)下的方法：

| 名称 | 描述 |
| --- | --- |
| ffrt\_queue\_create | 创建队列。 |
| ffrt\_queue\_destroy | 销毁队列。 |
| ffrt\_queue\_submit\_f | 向队列提交一个任务。  **说明**：从API version 20开始，支持该接口。 |

**说明** 

* 如何使用FFRT C++ API详见：[FFRT C++接口三方库使用指导](ffrt-development-guideline.md#使用ffrt-c-api-1)。
* 使用FFRT C接口或C++接口时，都可以通过FFRT C++接口三方库简化头文件包含，即使用#include "ffrt/ffrt.h"头文件包含语句。

## 约束限制

* **避免提交超长任务** FFRT内置进程级队列任务超时检测机制。当串行任务执行时间超过预设阈值（默认30秒）时，系统将打印和上报异常日志，并触发预设的进程超时回调函数（如已配置）。
* **同步原语使用规范** 在提交给FFRT的任务闭包中，避免使用std::mutex、std::condition\_variable和std::recursive\_mutex，标准库同步原语会长时间占用FFRT Worker线程。请替换为FFRT提供的同步原语：ffrt::mutex、ffrt::condition\_variable或ffrt::recursive\_mutex，其用法与标准库相同。
* **全局变量中的队列管理** 若在全局变量中管理串行队列，随业务进程销毁，测试程序中需注意生命周期解耦问题。在测试用例结束时，需显式释放串行队列，其他资源可随全局变量释放。原因是全局变量在主函数结束后析构，而串行队列的释放依赖于FFRT框架中的其他资源，此时这些资源可能已被销毁。
