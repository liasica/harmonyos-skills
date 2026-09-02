---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settensordesc
title: SetTensorDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetTensorDesc
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f41f7dde1c7afe1f7b6750cfb905950a8d584ec6cbeb572e7acd383a7e83bae
---

## 函数功能

设置Tensor的描述符（TensorDesc）。

## 函数原型

```cpp
graphStatus SetTensorDesc(const TensorDesc &tensor_desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| tensor\_desc | 输入 | 需设置的Tensor描述符。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
