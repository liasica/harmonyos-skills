---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmax
title: GetMax
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > GetMax
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e126c92723a2577b2a53ceb9231e6a10a8406c4ef0c091820b588797f3f58d39
---

## 函数功能

获取最大的T对象指针。

## 函数原型

```
1. const T *GetMax() const;
2. T *GetMax();
```

## 参数说明

无

## 返回值

返回最大的T对象指针。

## 约束说明

无

## 调用示例

```
1. int min = -1;
2. int max = 1024;
3. Range<int> range(&min,&max);

5. auto ret = range.GetMax(); // ret指针指向max
```
