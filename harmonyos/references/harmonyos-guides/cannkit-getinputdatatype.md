---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputdatatype
title: GetInputDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferDataTypeContext > GetInputDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6e2123f07d665a2108affc0bd4ee1ee4a0e4125b9b674180b3094e27206f396
---

## 函数功能

根据算子输入索引获取对应输入的数据类型。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```cpp
ge::DataType GetInputDataType(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子的输入索引，从0开始计数。 |

## 返回值

返回指定输入的数据类型。

若输入index非法，返回DT\_UNDEFINED。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetInputDataType(0);
  // ...
}
```
