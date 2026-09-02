---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > Init
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48d33967fed9983f551bd347117a414e4fedf4053266b215e1f967ab4fb7cf40
---

## 函数功能

使用最大容量初始化本实例。

## 函数原型

```cpp
void Init(size_t capacity)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| capacity | 输入 | 初始化本实例的容量。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
size_t capacity = 100U;
size_t total_size = capacity * sizeof(int64_t) + sizeof(ContinuousVector);
auto holder = std::unique_ptr<uint8_t[]>(new (std::nothrow) uint8_t[total_size]);
reinterpret_cast<ContinuousVector *>(holder.get())->Init(capacity); // 100U
```
