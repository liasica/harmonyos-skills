---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-fault-type
title: 故障类型
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障类型及日志规格说明 > 故障类型
category: best-practices
scraped_at: 2026-04-28T08:22:56+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b29994daf04f79f1035c51dbf4b7880f674c01f152f113e02b8db6e9494e0d5f
---

## 应用异常退出

### CppCrash

CppCrash指的是C/C++运行时崩溃，CppCrash进程崩溃检测基于操作系统信号机制，故障按照崩溃信号分类，详见[系统处理的崩溃信号](../harmonyos-guides/cppcrash-guidelines.md#系统处理的崩溃信号)。

### JS Crash

JS Crash为未处理的JS异常导致应用意外退出，JS Crash异常包含不同的场景，详见[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。

## 应用冻屏

用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用冻屏（AppFreeze），即应用无响应或卡死。应用冻屏包含多个场景的超时检测，详见[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。

## 地址越界

地址越界检测主要用于辅助开发者在调试和压测阶段发现内存非法访问问题。地址越界检测支持多种类型问题检测，详见[地址越界经典问题类型](bpta-stability-address-sanitizer-catagory.md)。

## 资源泄漏

资源泄漏指句柄、线程、内存等资源未正确释放导致的长期占用问题，详见[Resource Leak（资源泄漏）检测](../harmonyos-guides/resource-leak-guidelines.md)。
