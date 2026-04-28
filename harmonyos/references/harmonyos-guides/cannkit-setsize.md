---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setsize
title: SetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > SetSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:637c5720a14700435676c492b9a61ba036a91391260c22e046e8b0d26f0eb936
---

## 函数功能

设置tensor数据的内存大小。

## 函数原型

```
1. void SetSize(const size_t size)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| size | 输入 | tensor的内存大小，单位为字节。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. std::vector<int> a = {10};
2. auto addr = reinterpret_cast<void *>(a.data());
3. TensorData td(addr, HostAddrManager, 100U, kOnHost);
4. td.SetSize(10U);
```
