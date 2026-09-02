---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoverheadlength
title: GetOverHeadLength
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVectorVector > GetOverHeadLength
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:25f6865b7ea56fb5f51f44f3c41f6787fc02a2d9ce081edeab400e41b93eafb5
---

## 函数功能

获取数据描述信息的长度。

## 函数原型

```cpp
static size_t GetOverHeadLength(const size_t capacity)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| capacity | 输入 | 实例的最大容量。 |

## 返回值

数据描述信息的长度。

## 约束说明

无

## 调用示例

```cpp
size_t capacity = 100U;
auto length = ContinuousVectorVector::GetOverHeadLength(capacity);
```
