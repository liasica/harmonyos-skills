---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmin
title: GetMin
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > GetMin
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3aafa918a2662fa6370d3d3498aa5d52e81c9a67e660d47e7937f9f90531545
---

## 函数功能

获取最小的T对象指针。

## 函数原型

```cpp
const T *GetMin() const;
T *GetMin();
```

## 参数说明

无

## 返回值

返回最小的T对象指针。

## 约束说明

无

## 调用示例

```cpp
int min = -1;
int max = 1024;
Range<int> range(&min,&max);
 
auto ret = range.GetMin(); // ret指针指向min
```
