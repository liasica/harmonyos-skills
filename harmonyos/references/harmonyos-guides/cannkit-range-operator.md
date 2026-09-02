---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-range-operator
title: operator==
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > operator==
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:41e910b376c2e58ec8535b82a2ff7ae5a27848bcf6235028edd3e1c3677015ca
---

## 函数功能

判断与另外一个range对象是否相等，如果两个range的上下界的地址相同，或者上下界的值相同，这两个对象相等。

## 函数原型

```cpp
bool operator==(const Range<T>&rht) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| rht | 输入 | 另一个Range对象。 |

## 返回值

true：相等。

false：不相等。

## 约束说明

无

## 调用示例

```cpp
int min = 0;
int max = 1024;
int max2 = 1024;
Range<int> range1(&min, &max); // 上界为1024Bytes，下界为0
Range<int> range2(&min, &max); // 上界为1024Bytes，下界为0
Range<int> range3(&min, &max2); // 上界为1024Bytes，下界为0
 
auto ret1 = range1 == range2; // true
auto ret2 = range1 == range3; // true
```
