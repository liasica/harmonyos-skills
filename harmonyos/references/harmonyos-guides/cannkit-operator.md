---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator
title: operator
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TensorData > operator
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:889ec1ed3f92d90f3b6b76dacdb93dfa15579fea86df24ac5b214b07dbfb848f
---

## 函数功能

禁用拷贝赋值函数。

使用移动赋值函数。

## 函数原型

```
1. TensorData& operator= (const TensorData &other)=delete
2. TensorData& operator= (TensorData &&other) noexcept
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个TensorData对象。 |

## 返回值

返回一个持有other对象资源的新TensorData对象。

## 约束说明

无

## 调用示例

```
1. auto addr = reinterpret_cast<void *>(0x10);
2. TensorData td(addr, HostAddrManager, 100U, kOnHost);
3. TensorData new_td = std::move(td);
```
