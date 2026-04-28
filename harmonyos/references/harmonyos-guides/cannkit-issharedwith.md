---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-issharedwith
title: IsSharedWith
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > IsSharedWith
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cdaa22d9cfd0e19d7a46a39d20636c9a4fd7c5317404f3f3e6b0709038324a0b
---

## 函数功能

判断当前TensorData对象与另一个对象是否共享一块内存以及使用同一个内存管理函数。

## 函数原型

```
1. bool IsSharedWith(const TensorData &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个TensorData对象。 |

## 返回值

true代表两个对象共享一块内存以及使用同一个内存管理函数。

false反之。

## 约束说明

无

## 调用示例

```
1. auto addr = reinterpret_cast<void *>(0x10);
2. TensorData td1(addr, HostAddrManager, 100U, kOnHost);
3. TensorData td2(addr, HostAddrManager, 100U, kOnHost);
4. bool is_shared_td = td1.IsSharedWith(td2); // true
```
