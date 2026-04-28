---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-range-operator
title: operator==
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Range > operator==
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20cf81ba1b52cd01061e78494290c4e539d666218c7936507155920c0efb4c7a
---

## 函数功能

判断与另外一个range对象是否相等，如果两个range的上下界的地址相同，或者上下界的值相同，这两个对象相等。

## 函数原型

```
1. bool operator==(const Range<T>&rht) const
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

```
1. int min = 0;
2. int max = 1024;
3. int max2 = 1024;
4. Range<int> range1(&min, &max); // 上界为1024Bytes，下界为0
5. Range<int> range2(&min, &max); // 上界为1024Bytes，下界为0
6. Range<int> range3(&min, &max2); // 上界为1024Bytes，下界为0

8. auto ret1 = range1 == range2; // true
9. auto ret2 = range1 == range3; // true
```
