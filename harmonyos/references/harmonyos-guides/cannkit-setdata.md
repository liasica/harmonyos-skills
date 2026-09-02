---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdata
title: SetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > SetData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5aa2934e3f3a4177471fda9fadb27a2550a8b591e62be73dce6ac648ff679f54
---

## 函数功能

设置Tensor的数据。

## 函数原型

```cpp
void SetData(TensorData &&data)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data | 输入 | 需要设置的数据。  关于TensorData类型的定义，请参见[TensorData](cannkit-construction-and-destructor-functions.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
void *a = &t;
TensorData td(a, nullptr);
t.SetData(std::move(td));
```
