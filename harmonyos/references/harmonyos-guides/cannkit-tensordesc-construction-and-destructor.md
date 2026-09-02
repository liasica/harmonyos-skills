---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd267b3a6d0320ad74df56e322811e2a684fe3de4e614dbe0509bd66229f7103
---

## 函数功能

TensorDesc构造函数和析构函数。

## 函数原型

```cpp
TensorDesc();
~TensorDesc() = default;
explicit TensorDesc(Shape shape, Format format = FORMAT_ND, DataType dt = DT_FLOAT);
TensorDesc(const TensorDesc &desc);
TensorDesc(TensorDesc &&desc);
TensorDesc &operator=(const TensorDesc &desc);
TensorDesc &operator=(TensorDesc &&desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| shape | 输入 | Shape对象。 |
| format | 输入 | Format对象，默认取值FORMAT\_ND。  关于Format数据类型的定义，请参见[Format](cannkit-ge-format.md)。 |
| dt | 输入 | DataType对象，默认取值DT\_FLOAT。  关于DataType数据类型的定义，请参见[DataType](cannkit-ge-datatype.md)。 |
| desc | 输入 | 待拷贝或者移动的TensorDesc对象。 |

## 返回值

TensorDesc构造函数返回TensorDesc类型的对象。

## 异常处理

无

## 约束说明

无
