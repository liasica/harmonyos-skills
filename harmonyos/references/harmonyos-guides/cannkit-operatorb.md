---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorb
title: operator!=
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > operator!=
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:77851214ce6061f61d0a0ccc2c2d5d24415b504d6fcbad5229f655df8409fe74
---

## 函数功能

判断与另一个Shape对象是否不等。

## 函数原型

```
1. bool operator!=(const Shape &rht) const
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

```
1. Shape shape0({3, 256, 256});
2. Shape shape1({1, 3, 256, 256});
3. auto is_diff_shape = shape0 != shape1; // 返回值为true，不相等
```
