---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-range-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f2a3fbfc1e46a8457dddb033d7861d6c7efd95fd01c2a8e35cfce606dbc1a55f
---

## 函数功能

Range构造函数，对应如下3个汇总构造方法：

* 默认构造一个上下界为nullptr的range实例。
* 构造一个通过指定上下界的range实例。
* 只传入一个任意类型的指针构造一个上下界相同的range实例。

分别对应下述3种构造函数原型。

## 函数原型

```cpp
Range() // 默认构造函数，上下界均为空指针
Range(T *min, T* max) : min_(min), max_(max) // 开发者指定上界max，下界min
Range(T *same_ele) : min_(same_ele), max_(same_ele) // 上下界均为same_ele
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| min | 输入 | 下界的指针，类型为T\*。 |
| max | 输入 | 上界的指针，类型为T\*。 |
| same\_ele | 输入 | 构造相同上下界range实例时使用，上下界均使用same\_ele赋值，类型为T\*。 |

## 返回值

返回开发者指定构造的range对象。

## 约束说明

无

## 调用示例

```cpp
// 1. 默认构造
Range<int> range1; // 上下界均为nullptr
// 2. 开发者指定上下界
int min = 0;
int max = 1024;
Range<int> range2(&min, &max); // 上界为1024Bytes，下界为0
// 3. 构造上下界相同的range
Range<int> range3(&min); // 上下界均为0
```
