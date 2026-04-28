---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-free
title: Free
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Allocator > Free
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36135aacf9a2c35a8b76889b04e277a240a2024f49b7da462911ababf54081c3
---

## 函数功能

根据指定的MemBlock释放内存到内存池。

## 函数原型

```
1. virtual void Free(MemBlock *block) = 0;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| block | 输入 | 内存block指针。 |

## 返回值

无

## 异常处理

无

## 约束说明

虚函数开发者必须实现。
