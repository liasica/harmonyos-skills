---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdatatype
title: SetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8f293f379136fef890a25386b38131d68d880be5c704f7bff58e081b3e5ca683
---

## 函数功能

设置Tensor的Datatype。

## 函数原型

```cpp
graphStatus SetDataType(const ge::DataType &dtype);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dtype | 输入 | 需设置的DataType值。  关于DataType类型，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
