---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0897a9856b4caffb300fa3e3f90140673d03348f50a045046574a69b5c4f7406
---

## 函数功能

ComputeNodeInfo类的构造函数。

## 函数原型

```cpp
ComputeNodeInfo() = delete;
ComputeNodeInfo(const ComputeNodeInfo &) = delete;
ComputeNodeInfo(ComputeNodeInfo &&) = delete;
ComputeNodeInfo &operator=(const ComputeNodeInfo &) = delete;
ComputeNodeInfo &operator=(ComputeNodeInfo &&) = delete;
```

## 参数说明

无

## 返回值

无

## 约束说明

POD类型，当前不允许通过调用构造函数显式构造，可通过显式申请内存构造。
