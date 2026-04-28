---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-memblock-getaddr
title: GetAddr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > MemBlock > GetAddr
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d92bc3e21e5de445f99f91026020f75c661675a3da2512e914df3dc50799e881
---

## 函数功能

* 获取只读的device内存地址。
* 获取可读写的device内存地址。

## 函数原型

* 获取只读的device内存地址场景：

  ```
  1. const void *GetAddr() const
  ```
* 获取可读写的device内存地址场景：

  ```
  1. void *GetAddr()
  ```

## 参数说明

无

## 返回值

* 获取只读的device内存地址场景：

  | 类型 | 描述 |
  | --- | --- |
  | void\* | 只读的device内存地址。 |
* 获取可读写的device内存地址场景：

  | 类型 | 描述 |
  | --- | --- |
  | void\* | 可读写的device内存地址。 |

## 异常处理

无

## 约束说明

无
