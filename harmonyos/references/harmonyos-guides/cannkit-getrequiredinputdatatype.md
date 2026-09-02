---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputdatatype
title: GetRequiredInputDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferDataTypeContext > GetRequiredInputDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f3793e3697cca8ded2150c7822fca8e435bff6c3c23707ca86b4efa9614b6fc
---

## 函数功能

根据算子原型定义中的输入索引获取对应必选输入的数据类型。

## 函数原型

```cpp
ge::DataType GetRequiredInputDataType(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

返回指定输入的数据类型，若输入的ir\_index非法，返回DT\_UNDEFINED。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferDataTypeForXXX(InferDataTypeContext *context) {
  auto data_type = context->GetRequiredInputDataType(1);
  // ...
}
```
