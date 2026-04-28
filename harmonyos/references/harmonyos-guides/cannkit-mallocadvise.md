---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mallocadvise
title: MallocAdvise
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Allocator > MallocAdvise
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d59e70ac17975bfcd8f3ccfe33260bb282853249a04f3000473e42d86d9b0a3
---

## 函数功能

在开发者内存池中根据指定size大小申请device内存，建议申请的内存地址为addr。

## 函数原型

```
1. virtual MemBlock *MallocAdvise(size_t size, void *addr)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| size | 输入 | 指定需要申请内存大小。 |
| addr | 输入 | 建议申请的内存地址为addr。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| MemBlock\* | 返回[MemBlock](cannkit-memblock-construction-and-destructor.md)指针。 |

## 异常处理

无

## 约束说明

虚函数需要开发者实现，如若未实现，默认同[Malloc](cannkit-malloc.md)功能相同。
