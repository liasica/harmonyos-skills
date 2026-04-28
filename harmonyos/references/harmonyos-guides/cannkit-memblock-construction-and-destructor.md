---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-memblock-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > MemBlock > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:888dc27f359f2dfa463d2493ca02006dfd17350a3b255afa998e906cad7987f8
---

## 函数功能

MemBlock构造函数和析构函数。

## 函数原型

```
1. MemBlock(Allocator &allocator, void *addr, size_t block_size)
2. : allocator_(allocator), addr_(addr), count_(1U), block_size_(block_size) {}
3. virtual ~MemBlock() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| allocator | 输入 | 开发者根据[Allocator](cannkit-allocator-construction-and-destructor.md)派生的类的引用。 |
| addr | 输入 | device内存地址。 |
| block\_size | 输入 | device内存addr的大小。 |

## 返回值

MemBlock构造函数返回MemBlock类型的对象。

## 异常处理

无

## 约束说明

开发者继承[Allocator](cannkit-allocator-construction-and-destructor.md)后，申请内存需要返回MemBlock类型指针，开发者只需按构造函数构造MemBlock对象即可，析构函数根据开发者需求可以自定义，避免内存泄露。
