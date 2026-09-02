---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputdesc
title: GetRequiredInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetRequiredInputDesc
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1c4fdb6bca727662d55eb0da521d06d86a8e6a30f72180788d039e3068558a2
---

## 函数功能

根据算子原型定义中的输入索引获取对应必选输入的tensor描述信息。

## 函数原型

```cpp
const CompileTimeTensorDesc *GetRequiredInputDesc(const size_t ir_index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |

## 返回值

CompileTimeTensorDesc指针，index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见[CompileTimeTensorDesc](cannkit-compiletimetensordesc-constructor.md)。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
// 假设某个算子的IR原型的第0个输入是普通输入，且实际有1个输入
auto optional_input_td = extend_context->GetRequiredInputDesc(0); // 拿到第0个输入的tensor描述
```
