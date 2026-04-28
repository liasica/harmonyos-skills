---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-thread-leak-detection
title: 线程泄漏类问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 资源泄漏类问题检测 > 线程泄漏类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:54+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e169abc05c67f24d981ca664cd0545eba96dcf8965a3da0b56259b49ea20d84c
---

## 概述

线程泄漏是指程序在运行过程中，动态创建了线程，但没能正确释放或终止这些线程，导致线程数量持续增长。每个线程会占用一个线程栈，线程泄漏不仅会导致内存泄漏，而且如果线程持续占用CPU，还会导致CPU资源耗尽。

在使用`pthread\_create`创建线程后，即使子线程能自行结束，也要使用pthread\_join或pthread\_detach来回收子线程的资源。

## 实现原理

每个进程的/proc/[pid]/status节点里，有个“Thread:”字段，这个字段后面跟的数字就是pid对应进程的线程总数，采用的方式是在系统进程里遍历每个进程下的/proc/[pid]/status文件，获得每个进程的线程数，当超过一定阈值，则认为是该进程发生了线程泄漏异常。

## 约束和限制

目前的维测信息打印的是该进程的所有线程在维测时刻的瞬时运行栈，而不是调用pthread\_create创建线程问题点的栈。

## 检测步骤

如果不知道明确的复现步骤，可以尝试如下方法：

1. 打开“开发者选项”，同时打开它下面的子开关“系统资源泄漏日志”；
2. 在应用中调用HiDebug.setAppResourceLimit设置thread泄漏上限值，默认为700，如果想快速复现问题，建议设置成更小的值；
3. 启动[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/)工具进行稳定性测试，开发者可以选择应用探索测试，如果检测到异常，从工具中能获取到异常日志。

   说明

   需导入ohos.hidebug模块，该API从API version 12开始支持
