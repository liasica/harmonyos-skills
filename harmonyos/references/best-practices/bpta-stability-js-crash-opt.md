---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-crash-opt
title: JS Crash类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用异常退出类问题优化建议 > JS Crash类问题优化建议
category: best-practices
scraped_at: 2026-10-16T07:06:54+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:4f88975b3ab762e8e223b1b4e9e6e6386a87703cbe82a5dad540de8ba7a4b351
---

## 优化建议1：Source Maps归档保存

生产环境归档SourceMap便于后续源码还原，遇到JS Crash应先进行[堆栈轨迹分析](../harmonyos-guides-V5/ide-release-app-stack-analysis-V5.md)。

**说明** 

编译时SourceMap的获取位置详见：[ArkTS调试产物sourceMap](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section666114451518)。

## 优化建议2：崩溃预防机制

可使用errorManager注册错误观测器。注册后可以捕获到应用产生的JS Crash，应用崩溃时进程不会退出。详见[错误管理开发指导](../harmonyos-guides/errormanager-guidelines.md)。
