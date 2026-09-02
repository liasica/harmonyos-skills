---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensordesc
title: GetTensorDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetTensorDesc
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:387003bd6384e3421db001e7b85d03f360992adbcd042cd4a5a30fc7e1935713
---

## 函数功能

获取Tensor的描述符。

## 函数原型

```cpp
TensorDesc GetTensorDesc() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [TensorDesc](cannkit-tensordesc-construction-and-destructor.md) | 返回当前Tensor的描述符。 |

## 异常处理

无

## 约束说明

修改返回的TensorDesc信息，不影响Tensor对象中已有的TensorDesc信息。
