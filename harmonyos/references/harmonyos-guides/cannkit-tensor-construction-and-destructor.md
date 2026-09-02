---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c5195023e850f4d340add3349b46eb7c0ddaa1ade11d0d15a250c0d6bc734493
---

## 函数功能

Tensor构造函数和析构函数。

## 函数原型

```cpp
Tensor();
~Tensor() = default;
explicit Tensor(const TensorDesc &tensor_desc);
Tensor(const TensorDesc &tensor_desc, const std::vector<uint8_t> &data);
Tensor(const TensorDesc &tensor_desc, const uint8_t *data, size_t size);
Tensor(TensorDesc &&tensor_desc, std::vector<uint8_t> &&data);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| tensor\_desc | 输入 | TensorDesc对象，需设置的Tensor描述符。 |
| data | 输入 | 需设置的数据。 |
| size | 输入 | 数据的长度，单位为字节。 |

## 返回值

Tensor构造函数返回Tensor类型的对象。

## 异常处理

无

## 约束说明

无
