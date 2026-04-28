---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d7fff4dd8481081065e8015d1df931b126c95128726200f2d776b4980ce08b3d
---

## 函数功能

TensorDesc构造函数和析构函数。

## 函数原型

```
1. TensorDesc();
2. ~TensorDesc() = default;
3. explicit TensorDesc(Shape shape, Format format = FORMAT_ND, DataType dt = DT_FLOAT);
4. TensorDesc(const TensorDesc &desc);
5. TensorDesc(TensorDesc &&desc);
6. TensorDesc &operator=(const TensorDesc &desc);
7. TensorDesc &operator=(TensorDesc &&desc);
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
