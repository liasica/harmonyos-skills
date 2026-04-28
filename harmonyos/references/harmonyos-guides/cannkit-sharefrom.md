---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-sharefrom
title: ShareFrom
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > ShareFrom
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:737aacd963d111c5e01f03155b9dc00da0bd8d62b93101de6434a191bd453adc
---

## 函数功能

使当前的TensorData对象共享另一个对象的内存以及内存管理函数。

## 函数原型

```
1. ge::graphStatus ShareFrom(const TensorData &other)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个TensorData对象。 |

## 返回值

成功时返回 ge::GRAPH\_SUCCESS。

## 约束说明

无

## 调用示例

```
1. std::vector<int> a = {10};
2. auto addr = reinterpret_cast<void *>(a.data());
3. TensorData td1(addr, HostAddrManager, 100U, kOnHost);
4. TensorData td2(addr, nullptr);
5. td2.ShareFrom(td1);
```
