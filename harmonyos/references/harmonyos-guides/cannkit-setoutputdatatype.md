---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoutputdatatype
title: SetOutputDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferDataTypeContext > SetOutputDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b0f048b83c25b800f9ea775b3bb7eaaf26c573cb1b842a0b505ce174ea4ffd8
---

## 函数功能

根据输出索引，设置指定输出的数据类型。

## 函数原型

```cpp
ge::graphStatus SetOutputDataType(const size_t index, const ge::DataType datatype);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子IR原型定义中的输出索引，从0开始计数。 |
| datatype | 输入 | 需要设置的输出数据类型。  关于DataType的说明，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

返回设置的结果状态，状态说明请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

index非法时，返回失败。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto ret = context->SetOutputDataType(0, ge::DataType::DT_FLOAT);
  // ...
}
```
