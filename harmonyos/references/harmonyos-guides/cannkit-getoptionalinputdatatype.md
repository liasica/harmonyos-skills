---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoptionalinputdatatype
title: GetOptionalInputDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferDataTypeContext > GetOptionalInputDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5cc4cc8361c2de7698ce3aa5f9585ae6ff7cb52f43e78cc15732774012451b7c
---

## 函数功能

根据算子原型定义中的输入索引获取对应可选输入的数据类型。

## 函数原型

```cpp
ge::DataType GetOptionalInputDataType(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 可选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

返回指定输入的数据类型，若输入的ir\_index非法或该输入没有实例化，返回DT\_UNDEFINED。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetOptionalInputDataType(1);
  // ...
}
```
