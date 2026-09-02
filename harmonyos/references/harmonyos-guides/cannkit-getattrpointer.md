---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getattrpointer
title: GetAttrPointer
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > RuntimeAttrs > GetAttrPointer
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:6a13ba6ac1e6b7c30555822ca11fab6e26c9f1a189938162c33f8fcac57e44f4
---

## 函数功能

获取指定索引的算子属性，返回指向此属性的指针。

## 函数原型

```cpp
template<typename T>  const T *GetAttrPointer(size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 指定的输出类型 | 属性类型。 |
| index | 输入 | 属性在IR原型定义中的索引。 |

## 返回值

指向属性的指针。

## 约束说明

无

## 调用示例

```cpp
#include "register/op_def_registry.h"

namespace optiling {
static ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    const gert::RuntimeAttrs* runtime_attrs = context->GetAttrs();
    const gert::ContinuousVector* attr0 = runtime_attrs->GetAttrPointer<gert::ContinuousVector>(0);
    return ge::GRAPH_SUCCESS;
}
}
```
