---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getmax
title: GetMax
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > GetMax
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e18402d76f4ba5f89e3a57e9a65eb837328b335f4409c95143d334cb1abd621
---

## 函数功能

获取最大的T对象指针。

## 函数原型

```cpp
const T *GetMax() const;
T *GetMax();
```

## 参数说明

无

## 返回值

返回最大的T对象指针。

## 约束说明

无

## 调用示例

```cpp
int min = -1;
int max = 1024;
Range<int> range(&min,&max);
 
auto ret = range.GetMax(); // ret指针指向max
```
