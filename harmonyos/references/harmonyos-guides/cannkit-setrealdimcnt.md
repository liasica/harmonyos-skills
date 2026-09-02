---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setrealdimcnt
title: SetRealDimCnt
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetRealDimCnt
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b443ff61a4c58d071031f588504990074e6e5183be1939cbc2697799a0fc9d7
---

## 函数功能

向TensorDesc中设置Tensor的实际维度数目。

通过[GetShape](cannkit-tensordesc-getshape.md)接口返回的Shape的维度可能存在补1的场景，因此可以通过该接口设置Shape的实际维度个数。

## 函数原型

```cpp
void SetRealDimCnt(const int64_t real_dim_cnt);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| real\_dim\_cnt | 输入 | 需设置的TensorDesc的实际数据维度数目信息。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
