---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-malloc
title: Malloc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Allocator > Malloc
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:874ad56f994459a29ad7e454210db84cb11a13991c675ea2162c72cda7cb5118
---

## 函数功能

在开发者内存池中根据指定size大小申请device内存。

## 函数原型

```cpp
virtual MemBlock *Malloc(size_t size) = 0
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| size | 输入 | 指定需要申请内存大小。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| MemBlock\* | 返回[MemBlock](cannkit-memblock-construction-and-destructor.md)指针。 |

## 异常处理

无

## 约束说明

纯虚函数开发者必须实现。
