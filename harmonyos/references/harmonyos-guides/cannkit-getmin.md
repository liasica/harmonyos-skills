---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmin
title: GetMin
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > GetMin
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75f44913d016275ef6368128152ef78d264087383808aaec9132f931ef7022b7
---

## 函数功能

获取最小的T对象指针。

## 函数原型

```
1. const T *GetMin() const;
2. T *GetMin();
```

## 参数说明

无

## 返回值

返回最小的T对象指针。

## 约束说明

无

## 调用示例

```
1. int min = -1;
2. int max = 1024;
3. Range<int> range(&min,&max);

5. auto ret = range.GetMin(); // ret指针指向min
```
