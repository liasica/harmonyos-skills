---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorb
title: operator!=
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > operator!=
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:25f0e8f99bafeca84b602355889f3bd07e3b0e15464c680c66e60dfb9a50c227
---

## 函数功能

判断与另一个Shape对象是否不等。

## 函数原型

```cpp
bool operator!=(const Shape &rht) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| rht | 输入 | 另一个Shape对象。 |

## 返回值

true：不相等。

false：相等。

## 约束说明

无

## 调用示例

```cpp
Shape shape0({3, 256, 256});
Shape shape1({1, 3, 256, 256});
auto is_diff_shape = shape0 != shape1; // 返回值为true，不相等
```
