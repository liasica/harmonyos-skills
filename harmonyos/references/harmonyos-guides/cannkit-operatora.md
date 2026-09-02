---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatora
title: operator==
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > operator==
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0e3d35e082e8a39502c7120cc133e29b236e292356ec8b9b6235e0fc9dc7885
---

## 函数功能

判断与另外一个shape对象是否相等，如果两个shape的dim num相等，并且dim num内每个dim的值都相等，则认为两个shape相等。

## 函数原型

```cpp
bool operator==(const Shape &rht) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| rht | 输入 | 另一个Shape对象。 |

## 返回值

true：相等。

false：不相等。

## 约束说明

无

## 调用示例

```cpp
Shape shape0({3, 256, 256});
Shape shape1({1, 3, 256, 256});
auto is_same_shape = shape0 == shape1; // 返回值为false，不相等
```
